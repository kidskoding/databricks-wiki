#!/usr/bin/env python3
"""Create missing chapter notes and stubs from _meta/manifest.yaml.

Safe to re-run: it never overwrites a note that already exists, except chapter
notes' generated reading-order block (between the GENERATED markers), which is
rebuilt so it always matches the manifest.

Usage: python3 scripts/scaffold.py
"""
from pathlib import Path
import re

import yaml

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = yaml.safe_load((ROOT / "_meta" / "manifest.yaml").read_text())
DEPTH_LABEL = {101: "101 Beginner", 201: "201 Practitioner", 301: "301 Advanced", 401: "401 Expert"}
GEN_START = "<!-- GENERATED:reading-order START (scripts/scaffold.py) -->"
GEN_END = "<!-- GENERATED:reading-order END -->"


def link(title):
    return f"[[{title}]]"


def fm(data):
    """Render frontmatter with wiki links quoted, the way Obsidian expects."""
    lines = ["---"]
    for key, value in data.items():
        if isinstance(value, list):
            if not value:
                lines.append(f"{key}: []")
            else:
                lines.append(f"{key}:")
                lines.extend(f'  - "{v}"' if "[[" in str(v) or ":" in str(v) else f"  - {v}" for v in value)
        elif value is None or value == "":
            lines.append(f"{key}:")
        elif isinstance(value, str) and ("[[" in value or ":" in value or value.startswith(("'", '"'))):
            lines.append(f'{key}: "{value}"')
        else:
            lines.append(f"{key}: {value}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def chapter_title(ch):
    return f"Chapter {ch['number']} - {ch['title']}"


def build_order():
    """One reading chain through the whole vault: chapter note, its notes, next chapter note..."""
    order = []
    for ch in MANIFEST["chapters"]:
        order.append(chapter_title(ch))
        order.extend(n["title"] for n in ch["notes"])
    return order


def stub_body(note, ch):
    kind = ch.get("note_type", "concept")
    body = [
        f"# {note['title']}",
        "",
        f"> [!todo] Stub",
        f"> {note['summary']}",
        f"> Write this note from `_templates/{'Path' if kind == 'path' else 'Concept'}.md`. See `AGENTS.md`.",
        "",
    ]
    return "\n".join(body)


def note_summary(ch, n):
    """Prefer the summary in the note's own frontmatter: it is the source of truth once written."""
    path = ROOT / ch["folder"] / f"{n['title']}.md"
    if path.exists():
        text = path.read_text()
        if text.startswith("---\n"):
            meta = yaml.safe_load(text[4:text.find("\n---", 4)]) or {}
            if meta.get("summary"):
                return str(meta["summary"]).replace("|", "\\|")
    return n["summary"]


def reading_order_block(ch):
    rows = [GEN_START, "", "| # | Note | Depth | What it covers |", "|---|---|---|---|"]
    for i, n in enumerate(ch["notes"], 1):
        rows.append(f"| {i} | [[{n['title']}]] | {DEPTH_LABEL[n['depth']]} | {note_summary(ch, n)} |")
    rows += ["", GEN_END]
    return "\n".join(rows)


def main():
    order = build_order()
    pos = {t: i for i, t in enumerate(order)}
    created = 0

    def neighbours(title):
        i = pos[title]
        prev = link(order[i - 1]) if i > 0 else link("start_here")
        nxt = link(order[i + 1]) if i + 1 < len(order) else link("start_here")
        return prev, nxt

    for ch in MANIFEST["chapters"]:
        folder = ROOT / ch["folder"]
        folder.mkdir(exist_ok=True)
        level = int(ch["number"])
        ctitle = chapter_title(ch)

        # Chapter note
        cpath = folder / f"{ctitle}.md"
        prev, nxt = neighbours(ctitle)
        block = reading_order_block(ch)
        if cpath.exists():
            text = cpath.read_text()
            text = re.sub(re.escape(GEN_START) + r".*?" + re.escape(GEN_END), block.replace("\\", "\\\\"), text, flags=re.S)
            cpath.write_text(text)
        else:
            meta = {
                "type": "chapter",
                "status": "stub",
                "part": ch["part"],
                "level": level,
                "section": ch["section"],
                "summary": ch["summary"],
                "prev": prev,
                "next": nxt,
                "notes": [link(n["title"]) for n in ch["notes"]],
                "last_verified": "",
                "tags": ["chapter"],
            }
            body = "\n".join([
                f"# {ctitle}",
                "",
                "> [!story] Previously",
                "> (to write)",
                "",
                f"**{ch['summary']}**",
                "",
                "## The story of this chapter",
                "",
                "(to write)",
                "",
                "## Notes in reading order",
                "",
                block,
                "",
                "> [!nextup] Up next",
                f"> {nxt}",
                "",
            ])
            cpath.write_text(fm(meta) + "\n" + body)
            created += 1

        # Concept / path stubs
        kind = ch.get("note_type", "concept")
        for n in ch["notes"]:
            path = folder / f"{n['title']}.md"
            if path.exists():
                continue
            prev, nxt = neighbours(n["title"])
            meta = {
                "type": kind,
                "status": "stub",
                "level": level,
                "section": ch["section"],
                "depth": n["depth"],
                "summary": n["summary"],
                "personas": n.get("personas", []),
                "chapter": link(ctitle),
                "prev": prev,
                "next": nxt,
                "evolved_from": [link(t) for t in n.get("evolved_from", [])],
                "evolved_into": [link(t) for t in n.get("evolved_into", [])],
                "cloud_equivalent": [link(t) for t in n.get("cloud_equivalent", [])],
                "related": [link(t) for t in n.get("related", [])],
                "aliases": n.get("aliases", []),
                "prereqs": [],
                "unlocks": [],
                "clouds": ["aws", "azure", "gcp"],
                "mastery": "new",
                "last_verified": "",
                "tags": [kind, "flashcards"] if kind == "concept" else [kind],
            }
            path.write_text(fm(meta) + "\n" + stub_body(n, ch))
            created += 1

    # Hubs
    for hub in MANIFEST["hubs"]:
        path = ROOT / f"{hub['title']}.md"
        if path.exists():
            continue
        meta = {"type": "hub", "status": "stub", "summary": hub["summary"], "related": [], "last_verified": "", "tags": ["hub"]}
        path.write_text(fm(meta) + f"\n# {hub['title']}\n\n> [!todo] Stub\n> {hub['summary']}\n")
        created += 1

    # Glossary
    gdir = ROOT / "90_glossary"
    gdir.mkdir(exist_ok=True)
    for term in MANIFEST["glossary"]:
        path = gdir / f"{term}.md"
        if path.exists():
            continue
        meta = {
            "type": "glossary",
            "status": "stub",
            "level": 90,
            "section": "Glossary",
            "depth": 101,
            "summary": "",
            "related": [],
            "aliases": [],
            "last_verified": "",
            "tags": ["glossary", "flashcards"],
        }
        path.write_text(fm(meta) + f"\n# {term}\n\n> [!todo] Stub\n> Write from `_templates/Glossary.md`.\n")
        created += 1

    print(f"created {created} notes")


if __name__ == "__main__":
    main()
