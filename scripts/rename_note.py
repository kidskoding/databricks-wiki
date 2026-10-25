#!/usr/bin/env python3
"""Rename a note and rewrite every wiki link that points at it.

Keeps the old title in the note's `aliases`, updates the H1, the manifest entry,
and links in both bodies and frontmatter ([[Old]], [[Old|x]], [[Old\\|x]], [[Old#h]]).

Usage: python3 scripts/rename_note.py "Old Title" "New Title" [...more pairs]
Then run scripts/scaffold.py (to refresh reading-order tables) and scripts/build_index.py.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent


def rename(old, new):
    matches = [p for p in ROOT.rglob(f"{old}.md") if ".git" not in p.parts and "_templates" not in p.parts]
    if len(matches) != 1:
        sys.exit(f"expected one note named {old!r}, found {len(matches)}")
    src = matches[0]
    dst = src.with_name(f"{new}.md")
    if dst.exists():
        sys.exit(f"{dst} already exists")

    link = re.compile(r"\[\[" + re.escape(old) + r"(?=[\]#|\\])")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text()
        updated = link.sub(f"[[{new}", text)
        if updated != text:
            path.write_text(updated)

    text = src.read_text()
    text = re.sub(r"^# .*$", f"# {new}", text, count=1, flags=re.M)
    # Keep the old title searchable as an alias.
    m = re.search(r"^aliases:(.*)$", text, flags=re.M)
    if m and old not in text[m.start():text.find("\n---", m.start())]:
        if m.group(1).strip() == "[]":
            text = text.replace(m.group(0), f"aliases:\n  - {old}", 1)
        else:
            text = text.replace(m.group(0), f"aliases:{m.group(1)}\n  - {old}", 1)
    src.write_text(text)
    src.rename(dst)

    manifest = ROOT / "_meta" / "manifest.yaml"
    mtext = manifest.read_text()
    mtext = re.sub(r"(title: )" + re.escape(old) + r"$", r"\g<1>" + new, mtext, flags=re.M)
    mtext = re.sub(r"(?<=[\[, ])" + re.escape(old) + r"(?=[\],])", new, mtext)
    manifest.write_text(mtext)
    print(f"renamed {src.relative_to(ROOT)} -> {dst.name}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or len(args) % 2:
        sys.exit(__doc__)
    for i in range(0, len(args), 2):
        rename(args[i], args[i + 1])
