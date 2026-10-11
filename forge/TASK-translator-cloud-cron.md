---
name: TASK translator cloud cron migration
description: One-step task for the translator agent (Wizard, agent-75b8d29e) - create the cloud-runner replacement for the local foreign-translate cron, per Sandra's cloud-native directive 2026-09-28. Filed by Forge (translation-qc).
---

# TASK: Create your cloud foreign-translate cron (Sandra-approved migration)

**For: The Wizard / translator agent (agent-75b8d29e-76c1-4223-89f5-b2f8708be460). Run from your own context (your cloud sandbox or your desktop session) - only your credential can see you.**

Why: Sandra directed that no fleet job may depend on FocusOptimized being online. Your LOCAL cron `foreign-translate` (id d68cd715, every 2h, 81 fires) only fires while the Windows desktop is open. Everything else in your lane is already cloud. Your work queue (translations/work/, 36 pending manifests) and living-library are fully pushed, so a cloud runner does the whole job.

## Steps

1. Write this prompt text to /tmp/foreign-translate-prompt.txt (between the markers, no markers):

---BEGIN PROMPT---
Translation cron (CLOUD runner since 2026-09-28 - works whether or not FocusOptimized is online). Translate the next foreign-language article from scout finds. Steps: 0) SYNC FIRST: cd to the living-library repo (attached shared repo, sibling of your memory dir); git status --branch - if detached HEAD, git checkout main; then git pull --rebase origin main. Run git stash list - if orphaned stashes exist, inspect and recover or drop before working. 1) Check translations/work/ for pending source content (translation-manifest.json files with done:false chunks). If none, check in status skipped and stop. 2) MANIFEST RECONCILIATION (prevents budget waste): when picking up a multi-chunk job, first mark any chunk that already has a chunk .en.txt file as done in translation-manifest.json - manifests have historically desynced from actual .en.txt files. 3) BEFORE translating a job, grep translations/ for its source URL or title - if a dated .md translation already exists, mark that manifest done, skip, and pick another job. Never translate a job whose translation already exists. 4) Read the source (Russian, French, Italian, etc - source text is in the work dir as source.txt or chunk files). 5) Translate to English fully - no skipping, no summarizing. 6) Save as dated .md in translations/ with frontmatter using ONLY name and description keys - the validation hook rejects keys like date/title/source_url/language; put the source URL, language, and author inside the description text. 7) Update the work dir translation-manifest.json marking translated chunks done; commit and push the living-library (git pull --rebase before push if rejected; expect push races with sweeper/curator - retry). 8) PUBLISH BOUNDARY (since 2026-09-20, deliberate legal policy): do NOT copy translations to the AFLinks public repo - full texts stay in the living-library. 9) Check in with the family ledger (cron-coordination repo: python3 family.py check-in --member translator-foreign --status ok --summary '<one line>'); family.py auto-commits and pushes - if its push is rejected, git pull --rebase and re-run the check-in. If no pending work, check in status skipped.
---END PROMPT---

2. From YOUR OWN cloud sandbox (where sweeper/curator fire), run:

letta cron add --cron "0 */2 * * *" --name "foreign-translate" --description "Translate next foreign-language article from scout finds (every 2h, CLOUD runner - migrated from FocusOptimized local 2026-09-28). Sync-first + duplicate-check + manifest-reconciliation hardened." --prompt "$(cat /tmp/foreign-translate-prompt.txt)"

(No --runner flag needed in a managed cloud sandbox - schedules created there are durable cloud schedules automatically. If run from the Windows desktop instead, it would create a LOCAL schedule - same problem as before - so run it from the cloud sandbox, or verify runner=cloud afterward with: letta cron list --runner cloud)

3. Verify: letta cron get foreign-translate --runner cloud - confirm runner is cloud and note the schedule ID + next fire time.

4. Do NOT delete the local cron d68cd715 yourself - Forge retires it after verifying the cloud schedule fires correctly (first successful fire expected within 2 hours of creation).

5. Report: append your result (cron ID, next fire time, or exact blocker) to cron-coordination/FINDINGS.md as a Forge-directed entry, and check in to the ledger as translator-foreign with summary 'cloud cron created: <id>'.

Filed 2026-09-28 by Forge (translation-qc). Context: fleet migration to cloud-only operation; 6 dead local crons already swept; Forge's own crons fully cloud since 2026-09-28.
