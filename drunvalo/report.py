#!/usr/bin/env python3
"""
Drunvalo (The Pattern Keeper) — self-report helper for the AFLinks site.

Appends an entry to drunvalo/ACTIVITY.md and updates drunvalo/status.json
so the site's fleet card + "what's new" feed reflect this run.

Usage (from the AFLinks repo root):
  python3 drunvalo/report.py \
    --summary "+2 resources added to Village Library" \
    --count 2 --unit resources \
    --files "index.html" \
    --status ok

The caller commits and pushes (this script only writes the two files).
Pure stdlib. Safe to run from any machine with a checkout.
"""
import argparse
import datetime
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ACTIVITY_PATH = os.path.join(BASE, "drunvalo", "ACTIVITY.md")
STATUS_PATH = os.path.join(BASE, "drunvalo", "status.json")


def parse_date_sections(content):
    """Return [(insert_idx, date_str, section_text), ...] newest-section-first."""
    sections = []
    for m in re.finditer(r"^## (\d{4}-\d{2}-\d{2})\s*$", content, re.MULTILINE):
        sections.append((m.start(), m.group(1)))
    return sections


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary", required=True, help="One-line summary")
    parser.add_argument("--count", type=int, default=None)
    parser.add_argument("--unit", default="")
    parser.add_argument("--files", default="", help="Comma-separated repo-relative paths")
    parser.add_argument("--status", default="ok", help="ok | error | skipped")
    args = parser.parse_args()

    now = datetime.datetime.now(datetime.timezone.utc)
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M") + " UTC"

    # --- status.json ---
    status = {}
    if os.path.exists(STATUS_PATH):
        with open(STATUS_PATH, encoding="utf-8") as f:
            status = json.load(f)
    status["last_run"] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    status["last_status"] = args.status
    status["last_summary"] = args.summary[:300]
    os.makedirs(os.path.dirname(STATUS_PATH), exist_ok=True)
    with open(STATUS_PATH, "w", encoding="utf-8") as f:
        json.dump(status, f, ensure_ascii=False, indent=2)

    # --- ACTIVITY.md ---
    agent_line = "### Drunvalo (The Pattern Keeper) — " + time_str
    count_part = ""
    if args.count is not None:
        count_part = f"**+{args.count} {args.unit}** — "
    entry_lines = [agent_line, f"{count_part}{args.summary}"]
    if args.files:
        entry_lines.append("")
        for fp in args.files.split(","):
            fp = fp.strip()
            if fp:
                entry_lines.append(f"- [`{fp}`]({fp})")
    entry_lines.append("")
    entry = "\n".join(entry_lines)

    if os.path.exists(ACTIVITY_PATH):
        with open(ACTIVITY_PATH, encoding="utf-8") as f:
            content = f.read()
    else:
        content = ""

    sections = parse_date_sections(content)
    if sections and sections[0][1] == date_str:
        # Today exists — insert right after the date header line
        idx = sections[0][0]
        nl = content.index("\n", idx)
        content = content[:nl + 1] + "\n" + entry + content[nl + 1:]
    else:
        # New date section — insert at top (before first section or append)
        new_section = f"## {date_str}\n\n{entry}\n"
        if sections:
            content = content[:sections[0][0]] + new_section + "\n" + content[sections[0][0]:]
        else:
            content = content.rstrip() + f"\n\n{new_section}\n"

    with open(ACTIVITY_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Drunvalo report written: {args.summary[:80]} ({time_str})")


if __name__ == "__main__":
    main()