#!/usr/bin/env python3
"""Query the Databricks Brain vault from any agent harness.

Offline, standard library only. Reads `_meta/vault_index.json` (rebuilt by
scripts/build_index.py) and the notes themselves, and answers in well under a second.

Usage:
  python3 scripts/brain.py context "how do I give analysts read access to one schema"
  python3 scripts/brain.py search "private connectivity aws" [-k 8] [--type concept]
  python3 scripts/brain.py note "Unity Catalog" [--level summary|standard|full] [--section "How it works"]
  python3 scripts/brain.py resolve "Delta Live Tables"
  python3 scripts/brain.py neighbors "Unity Catalog" [--edge evolved_from]
  python3 scripts/brain.py history "Unity Catalog"
  python3 scripts/brain.py cloud "VNet Injection"
  python3 scripts/brain.py path analyst
  python3 scripts/brain.py primer

Add --json to any command for machine-readable output.
"""
from __future__ import annotations

import argparse
import difflib
import json
import math
import re
import sys
from collections import Counter, defaultdict
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "_meta" / "vault_index.json"
PRIMER = ROOT / "_meta" / "primer.md"

TOKEN_RE = re.compile(r"[a-z0-9_]+")
HEADING_RE = re.compile(r"^(#{1,3})\s+(.*)$")
CALLOUT_RE = re.compile(r"^>\s*\[!(\w+)\][-+]?\s*(.*)$")
STOP = set("""a an and are as at be by can do does for from has have how i in is it its of on or
that the this to was what when where which who why will with you your use using""".split())
# Sections that hold the most answer-worthy text get a small ranking boost.
SECTION_WEIGHT = {"summary": 1.4, "overview": 1.3, "how it works": 1.2, "common misconceptions": 1.1}
LEVELS = {
    "summary": {"summary", "overview"},
    "standard": {"context", "summary", "overview", "how it works", "small-business considerations",
                 "cloud differences", "common misconceptions"},
}


def tokens(text: str) -> list[str]:
    return [t for t in TOKEN_RE.findall(text.lower()) if t not in STOP and len(t) > 1]


# ---------------------------------------------------------------- loading


@lru_cache(maxsize=1)
def vault():
    data = json.loads(INDEX.read_text())
    nodes = {n["title"]: n for n in data["nodes"]}
    out_edges, in_edges = defaultdict(list), defaultdict(list)
    for e in data["edges"]:
        out_edges[e["source"]].append(e)
        in_edges[e["target"]].append(e)
    names = {}
    for n in nodes.values():
        names[n["title"].lower()] = n["title"]
    for n in nodes.values():  # aliases never override a real title
        for a in n["aliases"]:
            names.setdefault(str(a).lower(), n["title"])
    return data, nodes, out_edges, in_edges, names


def body(title: str) -> str:
    node = vault()[1][title]
    text = (ROOT / node["path"]).read_text()
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        text = text[end + 4:] if end != -1 else text
    return text.strip()


def sections(title: str) -> list[dict]:
    """Split a note into sections by heading; callouts before the first ## become their own sections."""
    out, cur = [], {"heading": "Intro", "lines": []}
    for line in body(title).splitlines():
        h = HEADING_RE.match(line)
        c = CALLOUT_RE.match(line)
        if h and len(h.group(1)) >= 2:
            out.append(cur)
            cur = {"heading": h.group(2).strip(), "lines": []}
        elif c and c.group(1) in {"story", "eli5"}:
            out.append(cur)
            cur = {"heading": "Context" if c.group(1) == "story" else "Summary", "lines": []}
        elif c and c.group(1) in {"azure", "aws", "gcp"}:
            cur["lines"].append(f"[{c.group(1).upper()}]")
        elif h:  # the H1 title
            continue
        else:
            if line.startswith("Mastery: `INPUT"):
                continue
            cur["lines"].append(line)
    out.append(cur)
    result = []
    for s in out:
        text = "\n".join(s["lines"]).strip()
        if text:
            result.append({"heading": s["heading"], "text": text})
    return result


@lru_cache(maxsize=1)
def search_index():
    """BM25 over every section of every written note, plus a title/alias/summary field."""
    _, nodes, *_ = vault()
    docs = []
    for title, n in nodes.items():
        meta_text = " ".join([title, title, " ".join(map(str, n["aliases"])), n["summary"]])
        docs.append({"title": title, "heading": "(title)", "text": n["summary"], "tok": tokens(meta_text),
                     "weight": 2.0})
        try:
            secs = sections(title)
        except FileNotFoundError:
            continue
        for s in secs:
            if s["heading"].lower() in {"recall", "next steps"} or s["heading"].lower().startswith("sources"):
                continue
            w = SECTION_WEIGHT.get(s["heading"].lower(), 1.0)
            docs.append({"title": title, "heading": s["heading"], "text": s["text"],
                         "tok": tokens(title + " " + s["heading"] + " " + s["text"]), "weight": w})
    df = Counter()
    for d in docs:
        d["tf"] = Counter(d["tok"])
        d["len"] = len(d["tok"]) or 1
        df.update(d["tf"].keys())
    avg = sum(d["len"] for d in docs) / len(docs)
    n = len(docs)
    idf = {t: math.log(1 + (n - f + 0.5) / (f + 0.5)) for t, f in df.items()}
    return docs, idf, avg


def resolve(name: str) -> dict:
    """Map any name (title, alias, old product name, near-miss) to a note title."""
    _, nodes, _, _, names = vault()
    key = name.strip().lower()
    if key in names:
        title = names[key]
        renamed = title.lower() != key
        return {"query": name, "title": title, "match": "alias" if renamed else "title",
                "summary": nodes[title]["summary"], "path": nodes[title]["path"]}
    close = difflib.get_close_matches(key, list(names), n=3, cutoff=0.75)
    if close:
        title = names[close[0]]
        return {"query": name, "title": title, "match": "fuzzy", "summary": nodes[title]["summary"],
                "path": nodes[title]["path"], "candidates": [names[c] for c in close]}
    hits = search(name, k=3)
    return {"query": name, "title": hits[0]["title"] if hits else None, "match": "search",
            "candidates": [h["title"] for h in hits]}


def search(query: str, k: int = 8, type_: str | None = None, cloud: str | None = None) -> list[dict]:
    docs, idf, avg = search_index()
    nodes = vault()[1]
    q = tokens(query)
    k1, b = 1.4, 0.75
    scored = []
    for d in docs:
        node = nodes[d["title"]]
        if type_ and node["type"] != type_:
            continue
        if cloud and cloud not in node["clouds"] and f"[{cloud.upper()}]" not in d["text"]:
            continue
        s = 0.0
        for t in q:
            f = d["tf"].get(t)
            if f:
                s += idf.get(t, 0) * f * (k1 + 1) / (f + k1 * (1 - b + b * d["len"] / avg))
        if s:
            if node["type"] == "glossary":
                s *= 0.8  # prefer concept notes when both match
            scored.append((s * d["weight"], d))
    scored.sort(key=lambda x: -x[0])
    out, seen = [], Counter()
    for s, d in scored:
        if seen[d["title"]] >= 2:  # at most two sections per note
            continue
        seen[d["title"]] += 1
        out.append({"title": d["title"], "section": d["heading"], "score": round(s, 2),
                    "path": nodes[d["title"]]["path"], "depth": nodes[d["title"]]["depth"],
                    "snippet": snippet(d["text"], q)})
        if len(out) >= k:
            break
    return out


def snippet(text: str, q: list[str], width: int = 320) -> str:
    flat = re.sub(r"\s+", " ", re.sub(r"^>\s?", "", text, flags=re.M)).strip()
    low = flat.lower()
    pos = min([low.find(t) for t in q if low.find(t) != -1] or [0])
    start = max(0, pos - width // 3)
    piece = flat[start:start + width]
    return ("..." if start else "") + piece + ("..." if start + width < len(flat) else "")


# ---------------------------------------------------------------- note views


def note(title: str, level: str = "standard", section: str | None = None) -> dict:
    r = resolve(title)
    t = r["title"]
    if not t:
        return {"error": f"no note matches {title!r}", "candidates": r.get("candidates", [])}
    n = vault()[1][t]
    secs = sections(t)
    if section:
        secs = [s for s in secs if s["heading"].lower().startswith(section.lower())]
    elif level in LEVELS:
        secs = [s for s in secs if s["heading"].lower() in LEVELS[level]]
    meta = {k: n[k] for k in ("title", "path", "type", "status", "section", "depth", "summary",
                              "aliases", "clouds", "last_verified")}
    if r["match"] != "title":
        meta["resolved_from"] = title
    return {"meta": meta, "sections": secs, "edges": edge_summary(t)}


def edge_summary(title: str) -> dict:
    _, _, out_e, in_e, _ = vault()
    out = defaultdict(list)
    for e in out_e[title]:
        if e["target"] not in out[e["type"]]:
            out[e["type"]].append(e["target"])
    for e in in_e[title]:  # undirected relations read the same from both ends
        if e["type"] in {"related", "cloud_equivalent"} and e["source"] not in out[e["type"]]:
            out[e["type"]].append(e["source"])
        if e["type"] == "evolved_into" and e["source"] not in out["evolved_from"]:
            out["evolved_from"].append(e["source"])
        if e["type"] == "evolved_from" and e["source"] not in out["evolved_into"]:
            out["evolved_into"].append(e["source"])
    return dict(out)


def neighbors(title: str, edge: str | None = None) -> dict:
    t = resolve(title)["title"]
    nodes = vault()[1]
    edges = edge_summary(t)
    if edge:
        edges = {edge: edges.get(edge, [])}
    return {"title": t, "edges": {k: [{"title": x, "summary": nodes[x]["summary"] if x in nodes else ""}
                                      for x in v] for k, v in edges.items()}}


def history(title: str, generations: int = 2) -> dict:
    """Walk evolved_from back and evolved_into forward, a few generations each way."""
    t = resolve(title)["title"]

    def walk(start, key):
        seen, frontier, chain = {start}, [start], []
        for gen in range(1, generations + 1):
            nxt = []
            for x in frontier:
                for y in edge_summary(x).get(key, []):
                    if y not in seen:
                        seen.add(y)
                        nxt.append(y)
                        chain.append({"generation": gen, "from": x, "to": y})
            frontier = nxt
        return chain

    return {"title": t, "ancestors": walk(t, "evolved_from"), "descendants": walk(t, "evolved_into")}


def cloud(title: str) -> dict:
    t = resolve(title)["title"]
    text = body(t)
    per_cloud = {}
    for c in ("azure", "aws", "gcp"):
        m = re.search(rf"^>\s*\[!{c}\][-+]?.*\n((?:>.*\n?)*)", text, flags=re.M)
        if m:
            per_cloud[c] = re.sub(r"^>\s?", "", m.group(1), flags=re.M).strip()
    nodes = vault()[1]
    eq = [{"title": x, "summary": nodes[x]["summary"], "clouds": nodes[x]["clouds"]}
          for x in edge_summary(t).get("cloud_equivalent", []) if x in nodes]
    return {"title": t, "per_cloud": per_cloud, "equivalents": eq}


def path(persona: str) -> dict:
    data, nodes, *_ = vault()
    key = persona.lower()
    personas = data["personas"]
    if key not in personas:  # accept a label or a fuzzy key
        match = [k for k, v in personas.items() if key in k or key in v.lower()]
        key = match[0] if match else key
    paths = [n for n in nodes.values() if n["type"] == "path" and key in n["personas"]]
    if not paths:
        return {"error": f"no learning path for {persona!r}", "personas": personas}
    best = sorted(paths, key=lambda n: (len(n["personas"]), n["title"]))[0]
    return {"persona": key, "path": best["title"], "summary": best["summary"],
            "route": ordered_links(best["title"]),
            "other_paths": [p["title"] for p in paths if p is not best]}


def ordered_links(title: str) -> list[str]:
    """Wiki links in the order they appear in a note's body (a path's reading order)."""
    nodes, out = vault()[1], []
    for m in re.finditer(r"\[\[([^\]#|\\]+)", body(title)):
        t = m.group(1).strip()
        if t in nodes and t not in out and t != title:
            out.append(t)
    return out


def context(question: str, budget: int = 1800) -> dict:
    """The one-call answer bundle: entities named in the question, then the best sections, within a word budget."""
    _, nodes, _, _, names = vault()
    q_low = question.lower()
    entities = []
    for name, title in sorted(names.items(), key=lambda kv: -len(kv[0])):
        if len(name) > 3 and re.search(rf"(?<![a-z0-9]){re.escape(name)}(?![a-z0-9])", q_low) \
                and title not in entities and nodes[title]["type"] != "glossary":
            entities.append(title)
        if len(entities) >= 4:
            break
    renamed = [{"you_said": n, "current": t} for n, t in names.items()
               if len(n) > 3 and n != t.lower() and re.search(rf"(?<![a-z0-9]){re.escape(n)}(?![a-z0-9])", q_low)
               and nodes[t]["type"] != "glossary"]
    chunks, used = [], 0
    for t in entities:
        for s in sections(t):
            if s["heading"].lower() in {"summary", "overview"}:
                words = len(s["text"].split())
                if used + words <= budget:
                    chunks.append({"title": t, "section": s["heading"], "text": s["text"]})
                    used += words
    docs, *_ = search_index()
    by_key = {(d["title"], d["heading"]): d for d in docs}
    for h in search(question, k=12):
        if any(c["title"] == h["title"] and c["section"] == h["section"] for c in chunks):
            continue
        d = by_key.get((h["title"], h["section"]))
        text = d["text"] if d else h["snippet"]
        words = len(text.split())
        if used + words > budget:
            text = " ".join(text.split()[: max(0, budget - used)])
            words = len(text.split())
        if words < 40:
            break
        chunks.append({"title": h["title"], "section": h["section"], "text": text})
        used += words
    return {"question": question, "renamed_terms": renamed, "entities": entities,
            "chunks": chunks, "words": used,
            "read_next": sorted({c["title"] for c in chunks}),
            "note": "Facts come from the vault's verified notes; check last_verified and each note's sources."}


# ---------------------------------------------------------------- output


def render(cmd: str, res) -> str:
    if isinstance(res, dict) and "error" in res:
        return f"error: {res['error']}\n" + json.dumps({k: v for k, v in res.items() if k != "error"}, indent=1)
    if cmd == "search":
        return "\n\n".join(f"{i}. [[{h['title']}]] > {h['section']} (depth {h['depth']}, {h['path']})\n   {h['snippet']}"
                           for i, h in enumerate(res, 1)) or "no results"
    if cmd == "note":
        m = res["meta"]
        head = f"# {m['title']}\n{m['summary']}\n(depth {m['depth']}, {m['section']}, verified {m['last_verified']}, {m['path']})"
        if m.get("resolved_from"):
            head += f"\nResolved from: {m['resolved_from']}"
        secs = "\n\n".join(f"## {s['heading']}\n{s['text']}" for s in res["sections"])
        edges = "\n".join(f"- {k}: {', '.join(v)}" for k, v in res["edges"].items() if v)
        return f"{head}\n\n{secs}\n\n## Graph\n{edges}"
    if cmd == "context":
        parts = [f"Question: {res['question']}"]
        if res["renamed_terms"]:
            parts.append("Current names: " + "; ".join(f"{r['you_said']} -> {r['current']}" for r in res["renamed_terms"]))
        for c in res["chunks"]:
            parts.append(f"### [[{c['title']}]] > {c['section']}\n{c['text']}")
        parts.append("Read next: " + ", ".join(f"[[{t}]]" for t in res["read_next"]))
        return "\n\n".join(parts)
    return json.dumps(res, indent=1, ensure_ascii=False)


def run(cmd: str, args: dict):
    if cmd == "search":
        return search(args["query"], int(args.get("k", 8)), args.get("type"), args.get("cloud"))
    if cmd == "note":
        return note(args["title"], args.get("level", "standard"), args.get("section"))
    if cmd == "resolve":
        return resolve(args["name"])
    if cmd == "neighbors":
        return neighbors(args["title"], args.get("edge"))
    if cmd == "history":
        return history(args["title"], int(args.get("generations", 2)))
    if cmd == "cloud":
        return cloud(args["title"])
    if cmd == "path":
        return path(args["persona"])
    if cmd == "context":
        return context(args["question"], int(args.get("budget", 1800)))
    if cmd == "primer":
        return PRIMER.read_text() if PRIMER.exists() else "primer not built yet: see _meta/primer.md"
    raise ValueError(f"unknown command {cmd}")


def main(argv=None):
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--json", action="store_true", default=argparse.SUPPRESS, help="machine-readable output")
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter, parents=[common])
    sub = p.add_subparsers(dest="cmd", required=True)
    _add = sub.add_parser
    sub.add_parser = lambda *a, **k: _add(*a, parents=[common], **k)
    s = sub.add_parser("search"); s.add_argument("query"); s.add_argument("-k", type=int, default=8)
    s.add_argument("--type", choices=["concept", "glossary", "chapter", "path", "hub"]); s.add_argument("--cloud", choices=["azure", "aws", "gcp"])
    s = sub.add_parser("note"); s.add_argument("title"); s.add_argument("--level", default="standard", choices=["summary", "standard", "full"]); s.add_argument("--section")
    s = sub.add_parser("resolve"); s.add_argument("name")
    s = sub.add_parser("neighbors"); s.add_argument("title"); s.add_argument("--edge")
    s = sub.add_parser("history"); s.add_argument("title"); s.add_argument("--generations", type=int, default=2)
    s = sub.add_parser("cloud"); s.add_argument("title")
    s = sub.add_parser("path"); s.add_argument("persona")
    s = sub.add_parser("context"); s.add_argument("question"); s.add_argument("--budget", type=int, default=1800)
    sub.add_parser("primer")
    a = vars(p.parse_args(argv))
    cmd, as_json = a.pop("cmd"), a.pop("json", False)
    res = run(cmd, a)
    if isinstance(res, str):
        print(res)
    else:
        print(json.dumps(res, indent=1, ensure_ascii=False) if as_json else render(cmd, res))


if __name__ == "__main__":
    main()
