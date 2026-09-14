#!/usr/bin/env python3
"""Build a fleet-wide report index from every agent's published reports.

The Aetherforce fleet publishes narrative reports into the AFLinks repo from
multiple agents, each with its own folder and authoring convention:

  synthesis/            Drunvalo       deep synthesis briefings (kind=synthesis)
  paradigm/             The Connector  Paradigm Signal Reports (kind=paradigm-signal)
  sources/*scout-finds* Scooter        scout field/finds reports (kind=scout-finds)

Each report is parsed for: frontmatter description (teaser), H1 or name
(title), date, and the author/agent who wrote it. Attribution is read from
each file's own conventions — never assumed from the folder. The output is a
single JSON array, newest first, consumed by the home-page strip and
synthesis.html.

Usage:  python3 build_synthesis_index.py
Output: synthesis/synthesis_index.json
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "synthesis" / "synthesis_index.json"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
H1_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
DATE_RE = re.compile(r"^(20\d{2}-\d{2}-\d{2})")

# Author conventions, tried in order per file:
#   1. frontmatter "author:" field
#   2. "*Synthesis created by X ...*" footer (Drunvalo's older briefings)
#   3. "*Synthesis by X — date*" footer (Drunvalo's newer briefings)
#   4. "*By X — date*" (The Connector's paradigm reports)
#   5. "**Scout:** X" body line (Scooter's finds reports)
AUTHOR_PATTERNS = [
    re.compile(r"^author:\s*(.+)$", re.MULTILINE),
    re.compile(r"Synthesis\s+created\s+by\s+([A-Za-z][A-Za-z .'()\-]*)", re.MULTILINE),
    re.compile(r"Synthesis\s+by\s+([A-Za-z][A-Za-z .'()\-]*)", re.MULTILINE),
    re.compile(r"^\*?By\s+([A-Za-z][A-Za-z .'()\-]*?)\s*[—–-]\s*\d{4}", re.MULTILINE),
    re.compile(r"\*\*Scout:\*\*\s*([A-Za-z][A-Za-z .'()\-]*?)(?=\s*[—–-]|\s*$)", re.MULTILINE),
]

# Footer style: "*Sources: 5 translations, ...*" (NOT inline "**Source:** `file`")
SOURCES_SUMMARY_RE = re.compile(r"^\*(?!\*)\s*Sources?:\s*(?!`)(.+?)\*?\s*$", re.MULTILINE)
# Inline style: "**Source:** `translations/xxx.md`, `translations/yyy.md`"
SOURCE_REF_RE = re.compile(r"\*\*Sources?:\*\*\s*([^\n]+)")

# File globs per report kind, with the fleet agent behind them
SOURCES = [
    ("synthesis",   "synthesis",            "*.md"),
    ("paradigm-signal", "paradigm",         "*.md"),
    ("scout-finds", "sources",              "*scout-finds*.md"),
]


def parse_frontmatter(text):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    fm = m.group(1)
    out = {}
    name = re.search(r"^name:\s*(.+)$", fm, re.MULTILINE)
    if name:
        out["name"] = name.group(1).strip().strip('"')
    desc = re.search(r"^description:\s*(.+)$", fm, re.MULTILINE)
    if desc:
        out["description"] = desc.group(1).strip().strip('"')
    author = re.search(r"^author:\s*(.+)$", fm, re.MULTILINE)
    if author:
        out["author"] = author.group(1).strip().strip('"')
    date = re.search(r"^date:\s*(.+)$", fm, re.MULTILINE)
    if date:
        out["date"] = date.group(1).strip().strip('"')
    return out


def parse_report(path: Path, kind: str):
    text = path.read_text(encoding="utf-8", errors="replace")
    fm = parse_frontmatter(text)

    teaser = fm.get("description", "")
    title = ""
    m = H1_RE.search(text)
    if m:
        title = m.group(1).strip()
    if not title:
        title = fm.get("name", "")

    date = ""
    m = DATE_RE.match(path.name)
    if m:
        date = m.group(1)
    if not date:
        date = fm.get("date", "")

    author = ""
    for pat in AUTHOR_PATTERNS:
        m = pat.search(text)
        if m:
            author = m.group(1).strip()
            if author:
                break

    # Scout finds frontmatter names often carry the scout attribution
    if not author and kind == "scout-finds":
        name = fm.get("name", "")
        ms = re.search(r"Scout\s*\(([A-Za-z][A-Za-z .'()\-]*)\)", name)
        if ms:
            author = ms.group(1).strip()
    if not author and kind == "scout-finds":
        # "**Agent**: Drunvalo" header block (AetherForce Scout Report style)
        m = re.search(r"\*\*Agent\*\*:\s*([A-Za-z][A-Za-z .'()\-]*?)(?=\s*\n|$)", text)
        if m:
            author = m.group(1).strip()
    if not author and kind == "scout-finds":
        # "Scout (Scooter) 04:00 round..." in frontmatter description
        desc = fm.get("description", "")
        m = re.search(r"Scout\s*\(([A-Za-z][A-Za-z .'()\-]*)\)", desc)
        if not m:
            # "Scooter scout round" in frontmatter description
            m = re.search(r"([A-Za-z][A-Za-z .'()\-]*?)\s+scout round", desc, re.IGNORECASE)
        if m:
            author = m.group(1).strip()
    if not author and kind == "scout-finds":
        # "(Scooter)" in the H1 title
        m = re.search(r"\(([A-Za-z][A-Za-z .'()\-]*)\)", title)
        if m:
            author = m.group(1).strip()
    # Trim any trailing role/institution text captured by greedy patterns
    # e.g. "Drunvalo for the AetherForce Living Library." → "Drunvalo"
    author = re.sub(r"\s+for\s+.*$", "", author).rstrip(".").strip()

    # Distilled sources line: footer summary when present, else count of
    # distinct linked archive files.
    sources_summary = ""
    m = SOURCES_SUMMARY_RE.search(text)
    if m:
        sources_summary = m.group(1).strip().strip("*").strip()
    linked = set(re.findall(r"`([^`]+)`", " ".join(SOURCE_REF_RE.findall(text))))
    sources_count = sum(1 for p in linked if not p.startswith("http"))
    sources = sources_summary
    if not sources and sources_count:
        sources = f"{sources_count} source files linked"

    return {
        "file": path.name,
        "path": str(path.relative_to(ROOT)),
        "slug": path.stem,
        "kind": kind,
        "date": date,
        "title": title,
        "teaser": teaser,
        "author": author or "Unknown agent",
        "sources": sources,
        "sources_count": sources_count,
    }


def main():
    entries = []
    for kind, folder, pattern in SOURCES:
        dirpath = ROOT / folder
        if not dirpath.exists():
            continue
        for path in sorted(dirpath.glob(pattern)):
            if path.name == "synthesis_index.json":
                continue
            entries.append(parse_report(path, kind))

    # newest first; stable tie-break by kind then slug
    entries.sort(key=lambda e: (e["date"], e["kind"], e["slug"]), reverse=True)
    OUT.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"build_synthesis_index: {len(entries)} reports -> {OUT.relative_to(ROOT)}")
    for e in entries[:6]:
        print(f"  [{e['kind']:>16}] {e['date']}  {e['author']:>12}  {e['title'][:52]}")


if __name__ == "__main__":
    sys.exit(main())