#!/usr/bin/env python3
"""
Watchtower staleness_report — PROPOSAL DRAFT (Issue 4, 2026-10-30).

Provenance: `should_run` + `staleness_report` ported from
Aether-commons-kit/ledger/family.py (the evolved blueprint copy, 283 lines).
AFLinks' root family.py (175 lines) is the older check-in/check-out CLI and
lacks both functions — that drift was flagged in Issue 2 §2.3 and committed
for port in Issue 3 §5.3.

Adaptation for AFLinks: instead of reading the cron-coordination ledger (whose
overnight clobbers are a standing flag), this reads the fleet's lane status
files directly — per the fleet lesson recorded in Issue 3: "status files are
becoming the real ledger." Timestamp keys vary by lane (forge uses
`updated`/`last_heartbeat`, drunvalo uses `last_run`, feeds use `generated_at`),
so each lane lists the keys it may carry, tried in order.

Deliberately NOT wired into any cron or into fleet_report.py (that helper
belongs to Cure 8er / the Synthesist crons). This is a Watchtower-lane
proposal: run it by hand, or wire it into a future watchtower scan after
review. Exit code 1 if any lane is overdue, so a cron can gate on it.

Usage:
  python3 watchtower/staleness_report.py [--json]
"""

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

AF_ROOT = Path(__file__).resolve().parents[1]

# Per-lane staleness limits (hours). Cadences observed in ACTIVITY/commit logs:
# daily lanes 24h; synthesist is a weekly-tolerant analysis lane (168h);
# paradigm_lenses was regenerated on a ~monthly cadence (720h); quest cards
# arrived with the village quest-sync lane (~48h when alive).
STALE_AFTER_HOURS = {
    "scout": 24,
    "forge": 24,
    "navigator": 24,
    "drunvalo": 24,
    "synthesist": 168,
    "paradigm (connector)": 24,
    "watchtower": 24,
    "feed (library_feed.json)": 24,
    "stats (stats.json)": 24,
    "paradigm_lenses": 720,
    "quest-queue (newest card)": 48,
    "clean-chem counts.md": 24,
}

# lane -> (path relative to AFLinks root, timestamp keys to try in order)
LANES = {
    "scout": ("scout/status.json", ["updated", "last_run", "generated_at"]),
    "forge": ("forge/status.json", ["updated", "last_heartbeat", "last_run"]),
    "navigator": ("navigator/status.json", ["updated", "last_run", "generated_at"]),
    "drunvalo": ("drunvalo/status.json", ["last_run", "updated"]),
    "synthesist": ("synthesist/status.json", ["last_run", "updated"]),
    "paradigm (connector)": ("paradigm/status.json", ["updated", "last_run", "generated_at"]),
    "watchtower": ("watchtower/status.json", ["last_run", "updated"]),
    "feed (library_feed.json)": ("library_feed.json", ["generated_at", "updated"]),
    "stats (stats.json)": ("stats.json", ["generated_at", "updated"]),
    "paradigm_lenses": ("paradigm_lenses.json", ["generated_at", "generated", "updated"]),
}

TS_RE = re.compile(r"(\d{4}-\d{2}-\d{2})[T ](\d{2}:\d{2})(?::(\d{2}))?")


def _parse_ts(value):
    """Parse an ISO-ish timestamp string to a naive-UTC datetime, or None."""
    if not value:
        return None
    if isinstance(value, (int, float)):
        return None  # epoch fields not used by any current lane file
    m = TS_RE.search(str(value))
    if not m:
        return None
    sec = int(m.group(3) or 0)
    return dt.datetime.strptime(f"{m.group(1)} {m.group(2)}:{sec:02d}", "%Y-%m-%d %H:%M:%S")


def _lane_last_run(lane):
    """Return (datetime, source_detail) for a lane, or (None, reason)."""
    if lane == "quest-queue (newest card)":
        qdir = AF_ROOT / "synthesis" / "quest-queue"
        if not qdir.is_dir():
            return None, "quest-queue dir missing"
        dates = []
        for f in qdir.glob("*.md"):
            m = re.match(r"(\d{4}-\d{2}-\d{2})", f.name)
            if m:
                dates.append(m.group(1))
        if not dates:
            return None, "no dated cards"
        return _parse_ts(max(dates) + " 00:00"), f"newest card {max(dates)}"
    if lane == "clean-chem counts.md":
        candidates = []
        env = __import__("os").environ.get("CLEAN_CHEM_DIR")
        if env:
            candidates.append(Path(env))
        candidates.append(AF_ROOT.parent / "clean-chem-intel")
        for c in candidates:
            p = c / "counts.md"
            if p.is_file():
                text = p.read_text(errors="replace")[:2000]
                m = re.search(r"_Updated: (\d{4}-\d{2}-\d{2} \d{2}:\d{2}) UTC_", text)
                if m:
                    return _parse_ts(m.group(1)), str(p)
                return None, "no Updated header"
        return None, "clean-chem-intel not found"
    rel, keys = LANES[lane]
    p = AF_ROOT / rel
    if not p.is_file():
        return None, "file missing"
    try:
        data = json.loads(p.read_text(errors="replace"))
    except Exception as e:
        return None, f"unparseable ({e.__class__.__name__})"
    for k in keys:
        ts = _parse_ts(data.get(k))
        if ts:
            return ts, f"{rel}#{k}"
    return None, f"no timestamp key among {keys}"


def staleness_report(now=None):
    """Return list of overdue lanes: (lane, hours_since_run, limit_hours, detail).

    Ported from Aether-commons-kit/ledger/family.py, adapted to lane status
    files (see module docstring).
    """
    now = now if now is not None else dt.datetime.utcnow()
    out = []
    for lane, limit in STALE_AFTER_HOURS.items():
        ts, detail = _lane_last_run(lane)
        if ts is None:
            out.append((lane, None, limit, detail))
            continue
        hours = (now - ts).total_seconds() / 3600
        if hours > limit:
            out.append((lane, round(hours, 1), limit, detail))
    return out


def should_run(member, essential=False):
    """Budget gate. Returns (run: bool, reason: str).

    Ported from Aether-commons-kit/ledger/family.py. Reads the family budget
    mode from the cron-coordination ledger if a clone is sibling to AFLinks;
    defaults to allowing when the ledger is absent (AFLinks-side callers have
    no obligation to carry it).
    """
    ledger_path = AF_ROOT.parent / "cron-coordination" / "cron_ledger.json"
    mode = "high"
    if ledger_path.is_file():
        try:
            mode = json.loads(ledger_path.read_text(errors="replace")).get(
                "family_budget", {}
            ).get("mode", "high")
        except Exception:
            pass
    if mode == "low" and not essential:
        return False, f"family budget low; member {member} skipped (non-essential)"
    return True, f"budget {mode}; run allowed"


def main():
    ap = argparse.ArgumentParser(description="Fleet lane staleness report (watchtower proposal)")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    args = ap.parse_args()

    overdue = staleness_report()
    ok, reason = should_run("watchtower-staleness-report")
    if args.json:
        print(json.dumps({
            "generated_at": dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "budget_gate": {"run": ok, "reason": reason},
            "overdue": [
                {"lane": l, "hours": h, "limit_hours": lim, "detail": d}
                for l, h, lim, d in overdue
            ],
        }, indent=1))
    else:
        print(f"stale lanes ({len(overdue)} of {len(STALE_AFTER_HOURS)} tracked):")
        for lane, hours, limit, detail in sorted(
            overdue, key=lambda r: -(r[1] or 1e9)
        ):
            h = "NEVER/UNREADABLE" if hours is None else f"{hours}h"
            print(f"  {lane:28s} {h:>16s}  (limit {limit}h)  [{detail}]")
        print(f"budget gate: {reason}")
    sys.exit(1 if overdue else 0)


if __name__ == "__main__":
    main()
