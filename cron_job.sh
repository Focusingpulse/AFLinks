#!/usr/bin/env bash
# AFLinks master cron job — ONE shot, do everything, report briefly.
# Designed for economy: single bash call per wake, no agent reasoning needed.
set -euo pipefail

REPO=/root/workspace/AFLinks
cd "$REPO"

echo "[1/5] Pull latest"
git pull --rebase --quiet origin main 2>&1 | tail -1 || git pull --quiet origin main 2>&1 | tail -1

echo "[2/5] Ensure pypdfium2 (skip if present)"
python3 -c "import pypdfium2; print('already installed')" 2>/dev/null || pip install -q pypdfium2 2>&1 | tail -1

echo "[3/5] Run queue (scrape/process next batch)"
python3 run_queue.py 2>&1 | tail -25

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

echo "[5/5] Completion check"
if [ -f ALL_SITES_COMPLETE.txt ]; then
  echo "CALLBACK_DELETE_CRON"
fi

echo "DONE"