#!/usr/bin/env python3
"""
Cure 8er (The Synthesist) — update site-visible status + activity.

Writes to synthesist/status.json and synthesist/ACTIVITY.md inside the AFLinks
repo, then commits and pushes to GitHub so the deployed site's Fleet HUD and
"What's New" section show this agent's live work.

Usage:
  python synthesist/log.py --summary "translated chunks 001-005" [--count 5] [--unit chunks] [--files "path1,path2"]

Mirrors the format used by living-library/tools/update_activity_log.py so the
site's parser (build_library_feed.parse_activity_log) reads it correctly.
"""
import argparse
import datetime
import json
import os
import subprocess

HEREPATH = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HEREPATH)
STATUS_PATH = os.path.join(HEREPATH, "status.json")
ACTIVITY_PATH = os.path.join(HEREPATH, "ACTIVITY.md")


def git(*args):
    try:
        r = subprocess.run(["git", "-C", REPO] + list(args),
                           capture_output=True, text=True, timeout=60)
        return r.returncode, (r.stdout + r.stderr).strip()
    except Exception as e:
        return 1, str(e)


def update_status(summary, count, unit):
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    st = {"last_run": now, "last_status": "ok", "last_summary": summary[:300]}
    if count is not None:
        st["last_details"] = {"entries_count": count, "unit": unit}
    with open(STATUS_PATH, "w", encoding="utf-8") as f:
        json.dump(st, f, ensure_ascii=False, indent=2)
    print(f"status.json updated ({now})")


def update_activity(summary, count, unit):
    now = datetime.datetime.now(datetime.timezone.utc)
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M") + " UTC"

    entry = []
    entry.append(f"### The Synthesist (Cure 8er) — {time_str}")
    count_part = ""
    if count is not None:
        count_part = f"**+{count} {unit}** — "
    entry.append(f"{count_part}{summary}")
    entry.append("")

    date_header = f"## {date_str}"
    with open(ACTIVITY_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    import re
    m = re.search(rf"^{re.escape(date_header)}$", content, re.MULTILINE)
    if m:
        # Insert at the top of today's section (after the header line)
        nxt = content.index("\n", m.end())
        content = content[:nxt + 1] + "\n" + "\n".join(entry) + content[nxt + 1:]
    else:
        # Create today's section at the top of the log (after frontmatter if any)
        split_at = None
        if content.startswith("---"):
            close = content.find("\n---", 4)
            if close != -1:
                split_at = content.find("\n", close + 4) + 1 or close + 5
        if split_at is None:
            split_at = 0
        new_section = f"\n{date_header}\n\n" + "\n".join(entry) + "\n"
        content = content[:split_at] + new_section + content[split_at:]

    with open(ACTIVITY_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"ACTIVITY.md updated ({date_str} {time_str})")


def push():
    git("pull", "--rebase", "--quiet")
    git("add", "synthesist/status.json", "synthesist/ACTIVITY.md")
    rc, out = git("commit", "-q", "-m", "synthesist: status + activity update")
    if rc != 0 and "nothing to commit" not in out:
        print(f"commit rc={rc}: {out[:200]}")
    rc2, out2 = git("push", "--quiet")
    if rc2 == 0:
        print("pushed to origin")
    else:
        print(f"push rc={rc2}: {out2[:300]}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--summary", required=True)
    ap.add_argument("--count", type=int, default=None)
    ap.add_argument("--unit", default="chunks")
    a = ap.parse_args()

    update_status(a.summary, a.count, a.unit)
    update_activity(a.summary, a.count, a.unit)
    push()


if __name__ == "__main__":
    main()