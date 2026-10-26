#!/usr/bin/env python3
"""Rewrite "**Label.** text" pseudo-headings into docs-style structure.

- A standalone paragraph that opens with "**Label.**" becomes a subheading
  one level below the enclosing heading, with the text as its paragraph.
- A list item or callout line that opens with "**Label.**" becomes "**Label:**".

Code fences are left alone. Safe to re-run.
Usage: python3 scripts/fix_bold_leads.py
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
SKIP = {".git", ".obsidian", "_meta", "scripts"}

PARA = re.compile(r"^\*\*([^*]{2,80}?)\.\*\* +(.*)$")
ITEM = re.compile(r"^((?:> ?)*(?: *(?:[-*+]|\d+\.) +)?)\*\*([^*]{2,80}?)\.\*\*( +)")
HEADING = re.compile(r"^(#{1,6}) ")


def fix(text):
    out, fence, level, changed = [], False, 1, 0
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if line.lstrip("> ").startswith("```"):
            fence = not fence
        if fence:
            out.append(line)
            continue
        h = HEADING.match(line)
        if h:
            level = len(h.group(1))
        m = PARA.match(line)
        prev_blank = i == 0 or lines[i - 1].strip() == ""
        if m and prev_blank:
            out += [f"{'#' * min(level + 1, 6)} {m.group(1)}", "", m.group(2)]
            changed += 1
            continue
        new = ITEM.sub(lambda m: f"{m.group(1)}**{m.group(2)}:**{m.group(3)}", line, count=1)
        changed += new != line
        out.append(new)
    return "\n".join(out), changed


def main():
    total = files = 0
    for path in sorted(ROOT.rglob("*.md")):
        if SKIP & set(path.relative_to(ROOT).parts):
            continue
        text, n = fix(path.read_text())
        if n:
            path.write_text(text)
            total += n
            files += 1
    print(f"rewrote {total} lines in {files} files")


if __name__ == "__main__":
    main()
