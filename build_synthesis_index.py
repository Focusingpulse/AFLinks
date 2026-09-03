#!/usr/bin/env python3
"""Build synthesis/synthesis_index.json from synthesis/*.md.

Scans the synthesis briefing markdown files (one per day, named
YYYY-MM-DD-<slug>.md), parses the YAML frontmatter `description` as the
teaser, the first `# H1` as the title, the filename prefix as the date, the
`*Synthesis by ...*` line as the author, and the trailing `Sources:` line for
the source count. Writes a single JSON array sorted newest-first.

The home page strip and synthesis.html both render from this index, so any
time a new briefing lands in synthesis/, re-running this script (wired into
cron_job.sh step [3b/5]) refreshes the whole site automatically.

Usage:  python3 build_synthesis_index.py
Output: synthesis/synthesis_index.json
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SYNTH_DIR = ROOT / "synthesis"
OUT = SYNTH_DIR / "synthesis_index.json"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
H1_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
AUTHOR_RE = re.compile(r"Synthesis\s+(?:created\s+)?by\s+([A-Za-z][A-Za-z .'-]*)", re.MULTILINE)
# Footer style: "*Sources: 5 translations, 1 synthesis reference, 2 database files*"
# (NOT the inline "**Source:** `file.md`" refs — reject those via lookahead + backtick check)
SOURCES_SUMMARY_RE = re.compile(r"^\*(?!\*)\s*Sources?:\s*(?!`)(.+?)\*?\s*$", re.MULTILINE)
# Inline style: "**Source:** `translations/xxx.md`, `translations/yyy.md`"
SOURCE_REF_RE = re.compile(r"\*\*Sources?:\*\*\s*([^\n]+)")
DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})[-_]")


def parse_briefing(path: Path):
    text = path.read_text(encoding="utf-8", errors="replace")

    fm = FRONTMATTER_RE.match(text)
    teaser = ""
    if fm:
        m = re.search(r"^description:\s*(.+)$", fm.group(1), re.MULTILINE)
        if m:
            teaser = m.group(1).strip().strip('"')

    title = ""
    m = H1_RE.search(text)
    if m:
        title = m.group(1).strip()

    date = ""
    m = DATE_RE.match(path.name)
    if m:
        date = m.group(1)

    author = ""
    m = AUTHOR_RE.search(text)
    if m:
        author = m.group(1).strip()

    # Distilled "sources" line: the footer summary when present, else the
    # count of distinct archive files linked via inline **Source:** refs.
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
        "slug": path.stem,
        "date": date,
        "title": title,
        "teaser": teaser,
        "author": author,
        "sources": sources,
        "sources_count": sources_count,
    }


def main():
    files = sorted(SYNTH_DIR.glob("*.md"))
    entries = [parse_briefing(p) for p in files]
    # newest first; stable tie-break by filename for same-day entries
    entries.sort(key=lambda e: (e["date"], e["slug"]), reverse=True)
    OUT.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"build_synthesis_index: {len(entries)} briefings -> {OUT.relative_to(ROOT)}")
    for e in entries[:3]:
        print(f"  {e['date']}  {e['title'][:70]}")


if __name__ == "__main__":
    sys.exit(main())