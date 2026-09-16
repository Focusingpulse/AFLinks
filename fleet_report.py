#!/usr/bin/env python3
"""
Cure 8er (The Synthesist) — fleet report helper.

Called by the Synthesist crons (daily-review, translate-gear1, translate-gear2)
so the AFLinks site's Fleet HUD and "Living Log" show this agent's work as it
happens. It:

  1. Checks in to the family ledger (cron-coordination/family.py --member cure-8er)
  2. Appends today's entry to ACTIVITY-LOG.md (living-library/tools/update_activity_log.py)
  3. Pull-rebases + commits + pushes every projection of those shared repos found
     on this machine, so whichever copy the site build reads has the update.

Usage:
  python fleet_report.py --summary "translated chunks 001-005" [--count 5] [--unit chunks] [--files "path1,path2"]

  --count    cumulative count for this member (delta is computed from prior run)
  --unit     unit label for the count (default: chunks)
"""
import argparse
import datetime
import glob
import os
import subprocess
import sys

HOME = os.path.expanduser("~")
AGENTS_ROOT = os.path.join(HOME, ".letta", "agents")
MEMBER = "cure-8er"
AGENT_LABEL = "The Synthesist (Cure 8er)"


def log(msg):
    print(msg, flush=True)


def git(repo, *args):
    """Run git in a repo; return (returncode, stdout+stderr)."""
    try:
        r = subprocess.run(
            ["git", "-C", repo] + list(args),
            capture_output=True, text=True, timeout=60,
        )
        return r.returncode, (r.stdout + r.stderr).strip()
    except Exception as e:
        return 1, str(e)


def find_repos(name):
    """Find every projection of a shared repo (e.g. 'living-library')."""
    pattern = os.path.join(AGENTS_ROOT, "*", name)
    found = []
    for p in sorted(glob.glob(pattern)):
        if os.path.isdir(os.path.join(p, ".git")):
            found.append(p)
    # Also check the current machine's other known roots
    for extra in [
        os.path.join(HOME, "Documents", "AFLinks", name),
        os.path.join(HOME, "workspace", name),
    ]:
        if os.path.isdir(os.path.join(extra, ".git")):
            found.append(extra)
    # Dedup, keep order
    seen = set()
    out = []
    for p in found:
        rp = os.path.normpath(p)
        if rp not in seen:
            seen.add(rp)
            out.append(rp)
    return out


def check_in_family(summary, count, unit):
    """Check in to every cron-coordination projection via family.py."""
    reported = 0
    for repo in find_repos("cron-coordination"):
        fam = os.path.join(repo, "family.py")
        if not os.path.isfile(fam):
            log(f"  [ledger] {repo}: no family.py, skipping")
            continue
        # pull-rebase before reading/writing (fleet rule)
        git(repo, "pull", "--rebase", "--quiet")
        cmd = [sys.executable, fam, "check-in",
               "--member", MEMBER, "--status", "ok", "--summary", summary]
        if count is not None:
            cmd += ["--entries-count", str(count)]
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
            log(f"  [ledger] {repo}: rc={r.returncode} {r.stdout.strip()[:120]} {r.stderr.strip()[:120]}")
            reported += 1
        except Exception as e:
            log(f"  [ledger] {repo}: ERROR {e}")
    return reported


def append_activity(summary, count, unit, files):
    """Append to ACTIVITY-LOG.md in every living-library projection, commit+push."""
    reported = 0
    for repo in find_repos("living-library"):
        upd = os.path.join(repo, "tools", "update_activity_log.py")
        if not os.path.isfile(upd):
            log(f"  [log] {repo}: no update_activity_log.py, skipping")
            continue
        git(repo, "pull", "--rebase", "--quiet")
        cmd = [sys.executable, upd,
               "--agent", AGENT_LABEL,
               "--summary", summary]
        if count is not None:
            cmd += ["--count", str(count), "--unit", unit]
        if files:
            cmd += ["--files", files]
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
            log(f"  [log] {repo}: rc={r.returncode} {r.stdout.strip()[:120]} {r.stderr.strip()[:120]}")
        except Exception as e:
            log(f"  [log] {repo}: ERROR {e}")
            continue
        # commit + push (update_activity_log.py leaves this to the caller)
        git(repo, "add", "ACTIVITY-LOG.md")
        rc, out = git(repo, "commit", "-q", "-m",
                      f"activity: {AGENT_LABEL} - {summary[:80]}")
        if rc != 0 and "nothing to commit" not in out:
            log(f"  [log] {repo}: commit rc={rc} {out[:200]}")
        rc2, out2 = git(repo, "push", "--quiet")
        if rc2 != 0:
            log(f"  [log] {repo}: push rc={rc2} {out2[:200]}")
        else:
            log(f"  [log] {repo}: committed + pushed")
            reported += 1
    return reported


def main():
    ap = argparse.ArgumentParser(description="Cure 8er fleet report")
    ap.add_argument("--summary", required=True)
    ap.add_argument("--count", type=int, default=None)
    ap.add_argument("--unit", default="chunks")
    ap.add_argument("--files", default="")
    a = ap.parse_args()

    log(f"[fleet_report] {datetime.datetime.now(datetime.timezone.utc).isoformat()}Z")
    log(f"[fleet_report] summary: {a.summary}")

    n_ledger = check_in_family(a.summary, a.count, a.unit)
    n_log = append_activity(a.summary, a.count, a.unit, a.files)

    log(f"[fleet_report] done: {n_ledger} ledger(s), {n_log} log(s) updated")


if __name__ == "__main__":
    main()