#!/usr/bin/env python3
"""Build the machine-readable index of the vault and check its links.

Reads every note's frontmatter and body (the notes are the source of truth) and writes:
  _meta/vault_index.json   every node and typed edge, for agents and scripts
  llms.txt                 a plain-text map of the vault for LLM agents
  Persona Map.md           the generated persona -> notes table (between markers)

Then it prints a health report: stubs left, unresolved links, missing fields.
Exit code 1 if any wiki link points at a note that does not exist.

Usage: python3 scripts/build_index.py [--quiet]
"""
from collections import defaultdict
from pathlib import Path
import json
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", ".obsidian", "_templates", "_assets", "scripts", "_meta"}
EDGE_KEYS = ["chapter", "prev", "next", "evolved_from", "evolved_into", "cloud_equivalent",
             "related", "prereqs", "unlocks", "notes"]
LINK_RE = re.compile(r"\[\[([^\]#|\\]+)(?:#[^\]|\\]*)?(?:\\?\|[^\]]*)?\]\]")
BOLD_LEAD = re.compile(r"^(?:> ?)*(?: *(?:[-*+]|\d+\.) +)?\*\*[^*]{2,80}?\.\*\* ")
MANIFEST = yaml.safe_load((ROOT / "_meta" / "manifest.yaml").read_text())
PERSONAS = MANIFEST["personas"]
GEN_START = "<!-- GENERATED:persona-map START (scripts/build_index.py) -->"
GEN_END = "<!-- GENERATED:persona-map END -->"


def notes():
    for path in sorted(ROOT.rglob("*.md")):
        rel = path.relative_to(ROOT)
        if rel.parts[0] in SKIP_DIRS or rel.name in {"AGENTS.md", "CLAUDE.md", "README.md"}:
            continue
        yield path, rel


def split(text):
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            return yaml.safe_load(text[4:end]) or {}, text[end + 4:]
    return {}, text


def as_list(v):
    if v is None or v == "":
        return []
    return v if isinstance(v, list) else [v]


def targets(values):
    out = []
    for v in as_list(values):
        out += [m.group(1).strip() for m in LINK_RE.finditer(str(v))]
    return out


def main():
    quiet = "--quiet" in sys.argv
    nodes, errors = {}, []
    for path, rel in notes():
        try:
            meta, body = split(path.read_text())
        except yaml.YAMLError as e:
            errors.append(f"bad frontmatter: {rel}: {e}")
            continue
        nodes[path.stem] = {"path": str(rel), "meta": meta, "body": body}

    # Links may also point at non-note files (embedded .base, images) by full filename.
    titles = set(nodes) | {p.name for p in ROOT.rglob("*") if p.is_file() and p.suffix != ".md"
                           and p.relative_to(ROOT).parts[0] not in {".git", ".obsidian"}}
    out_nodes, edges, unresolved, missing = [], [], defaultdict(set), []
    for title, n in nodes.items():
        m = n["meta"]
        for key in EDGE_KEYS:
            for t in targets(m.get(key)):
                edges.append({"source": title, "target": t, "type": key})
                if t not in titles:
                    unresolved[t].add(title)
        if "\u2014" in n["body"] or "\u2014" in json.dumps(m, default=str, ensure_ascii=False):
            errors.append(f"em dash found: {n['path']}")
        in_fence = False
        for line in n["body"].split("\n"):
            if line.lstrip("> ").startswith("```"):
                in_fence = not in_fence
            elif not in_fence and BOLD_LEAD.match(line):
                errors.append(f"bold run-in label '**X.**' (use a ### heading or '**X:**'): {n['path']}")
                break
        body_links = sorted(set(m_.group(1).strip() for m_ in LINK_RE.finditer(n["body"])))
        for t in body_links:
            if t not in titles:
                unresolved[t].add(title)
        if m.get("type") in {"concept", "path"} and m.get("status") == "written":
            for key in ("summary", "last_verified", "chapter", "depth"):
                if not m.get(key):
                    missing.append(f"{title}: {key}")
        out_nodes.append({
            "title": title,
            "path": n["path"],
            "type": m.get("type"),
            "status": m.get("status"),
            "level": m.get("level"),
            "section": m.get("section"),
            "depth": m.get("depth"),
            "summary": m.get("summary") or "",
            "personas": as_list(m.get("personas")),
            "aliases": as_list(m.get("aliases")),
            "clouds": as_list(m.get("clouds")),
            "last_verified": str(m.get("last_verified") or ""),
            "links_out": body_links,
        })

    order = {}
    for ch in MANIFEST["chapters"]:
        order[f"Chapter {ch['number']} - {ch['title']}"] = len(order)
        for n in ch["notes"]:
            order[n["title"]] = len(order)
    out_nodes.sort(key=lambda x: (x["level"] if isinstance(x["level"], int) else -1,
                                  order.get(x["title"], len(order)), x["title"]))
    index = {
        "description": "Databricks Brain vault index. Nodes are notes; edges are typed frontmatter links. "
                       "Body wiki links are listed per node in links_out. Regenerate with scripts/build_index.py.",
        "personas": PERSONAS,
        "depths": {"101": "Beginner", "201": "Practitioner", "301": "Advanced", "401": "Expert"},
        "edge_types": EDGE_KEYS,
        "nodes": out_nodes,
        "edges": edges,
    }
    (ROOT / "_meta" / "vault_index.json").write_text(json.dumps(index, indent=1, ensure_ascii=False) + "\n")
    write_llms_txt(out_nodes)
    write_persona_map(out_nodes)

    by_status = defaultdict(int)
    for n in out_nodes:
        by_status[(n["type"], n["status"])] += 1
    if not quiet:
        print("notes:", len(out_nodes), "edges:", len(edges))
        for (t, s), c in sorted(by_status.items(), key=str):
            print(f"  {t:9} {s:8} {c}")
        for e in errors:
            print("ERROR", e)
        for f in missing:
            print("MISSING", f)
    for t, srcs in sorted(unresolved.items()):
        print(f"UNRESOLVED [[{t}]] <- {', '.join(sorted(srcs)[:5])}{' ...' if len(srcs) > 5 else ''}")
    if unresolved or errors:
        sys.exit(1)


def write_llms_txt(nodes):
    lines = [
        "# Databricks Brain",
        "",
        "> An Obsidian knowledge graph that teaches Databricks from zero to expert, told as one story:",
        "> pre-Databricks history (chapters 01-05), the Databricks platform (06-10), the three clouds and",
        "> administration (11-14), migrating a business (15), plus a front door for business readers (00),",
        "> learning paths by persona (80), and a glossary (90).",
        "",
        "Agent instructions: AGENTS.md. Full typed graph: _meta/vault_index.json. Blueprint: _meta/manifest.yaml.",
        "Depth: 101 beginner, 201 practitioner, 301 advanced, 401 expert.",
        "",
    ]
    section = None
    for n in nodes:
        if n["type"] == "glossary":
            continue
        sec = n["section"] or "Hubs"
        if sec != section:
            section = sec
            lines += ["", f"## {sec}", ""]
        depth = f" [{n['depth']}]" if n["depth"] else ""
        summary = f": {n['summary']}" if n["summary"] else ""
        lines.append(f"- [{n['title']}]({n['path'].replace(' ', '%20')}){depth}{summary}")
    gloss = [n for n in nodes if n["type"] == "glossary"]
    lines += ["", "## Glossary", "", ", ".join(f"[{n['title']}]({n['path'].replace(' ', '%20')})" for n in gloss), ""]
    (ROOT / "llms.txt").write_text("\n".join(lines))


def write_persona_map(nodes):
    path = ROOT / "Persona Map.md"
    if not path.exists():
        return
    block = [GEN_START, ""]
    for key, label in PERSONAS.items():
        picks = [n for n in nodes if key in n["personas"] and n["type"] in {"concept", "path"}]
        picks.sort(key=lambda n: (n["depth"] or 0, n["level"] or 0))
        block += [f"### {label}", "", "| Depth | Note | Why |", "|---|---|---|"]
        block += [f"| {n['depth']} | [[{n['title']}]] | {n['summary']} |" for n in picks]
        block.append("")
    block.append(GEN_END)
    text = path.read_text()
    new = "\n".join(block)
    if GEN_START in text:
        text = re.sub(re.escape(GEN_START) + r".*?" + re.escape(GEN_END), new.replace("\\", "\\\\"), text, flags=re.S)
    else:
        text = text.rstrip() + "\n\n" + new + "\n"
    path.write_text(text)


if __name__ == "__main__":
    main()
