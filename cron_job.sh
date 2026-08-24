#!/usr/bin/env bash
# AFLinks master cron job — ONE shot, do everything, report briefly.
# Family-aware: checks the shared ledger, respects budget, reports staleness.
# Designed for economy: single bash call per wake, no agent reasoning needed.
set -uo pipefail

REPO=/root/workspace/AFLinks
FAMILY=/root/workspace/cron-coordination/family.py
cd "$REPO"

# --- Family gate: respect shared budget ---
echo "[0] Family check"
if ! python3 "$FAMILY" run-gate --member aflinks --essential 2>/dev/null; then
  # fallback: read ledger directly via small inline check
  MODE=$(python3 -c "import json;d=json.load(open('${FAMILY%/*}/cron_ledger.json'));print(d.get('family_budget',{}).get('mode','high'))" 2>/dev/null || echo high)
  if [ "$MODE" = "low" ]; then
    echo "  Family budget LOW — aflinks skipping non-essential batch this cycle"
    python3 "$FAMILY" check-in --member aflinks --status skipped --summary "budget low, skipped" 2>/dev/null || true
    exit 0
  fi
fi

# --- Watchdog: note any stale siblings ---
STALE=$(python3 "$FAMILY" staleness 2>/dev/null || echo "")
if [ -n "$STALE" ]; then
  echo "  Watchdog: $STALE"
fi

echo "[1/5] Pull latest"
git pull --rebase --quiet origin main 2>&1 | tail -1 || git pull --quiet origin main 2>&1 | tail -1

echo "[2/5] Ensure pypdfium2 (skip if present)"
python3 -c "import pypdfium2; print('already installed')" 2>/dev/null || pip install -q pypdfium2 2>&1 | tail -1

echo "[3/5] Run queue (scrape/process next batch)"
OUT=$(python3 run_queue.py 2>&1)
echo "$OUT" | tail -25

# Extract progress summary for the ledger
ENTRIES=$(python3 -c "import json;d=json.load(open('index.json'));print(len(d))" 2>/dev/null || echo "?")
SUMMARY=$(echo "$OUT" | grep -E "Processing|Total entries|Progress|New:|Existing:" | tail -4 | tr '\n' ' ' | cut -c1-280)

echo "[4/5] Commit and push progress"
git add -A
if git diff --cached --quiet; then
  echo "  Nothing to commit this run"
else
  git commit -q -m "AFLinks scrape: batch progress and incremental merge

👾 Generated with [Letta Code](https://letta.com)

Co-Authored-By: Letta Code <noreply@letta.com>"
  git push --quiet origin main 2>&1 | tail -2 || true
fi

echo "[5/5] Family check-in"
python3 "$FAMILY" check-in --member aflinks --status ok --summary "$SUMMARY" --entries-count "$ENTRIES" 2>/dev/null || true
python3 "$FAMILY" archive-growth --entries "$ENTRIES" 2>/dev/null || true

# --- Completion check ---
if [ -f ALL_SITES_COMPLETE.txt ]; then
  echo "CALLBACK_DELETE_CRON"
fi

echo "DONE"