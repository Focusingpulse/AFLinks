---
description: Live state of radiesthesia archive batch 2 (2026-09-14). Cron "radio-batch2-finish" DELETED 2026-09-14 19:15 UTC — task blocked on LFS migration. Delete this file when batch2 is actually finished.
date: 2026-09-14
---

# Radiesthesia Batch 2 — Live State

## Status: BLOCKED (cron deleted)

Cron `radio-batch2-finish` (id 013b2d33) was deleted 2026-09-14 19:15 UTC.
Reason: the task cannot make progress — see blockers below. Re-create it once
the LFS migration is done and the browser downloads can restart.

## Blockers (as of 2026-09-14 19:15 UTC)

1. **LFS migration not approved yet.** GitHub rejects any file >100MB without
   LFS. Two Christopher Hills PDFs (111MB, 139MB) already excluded; Louis
   Turenne (~1.5GB) and other large folders likely contain more >100MB files.
   Migration requires `git lfs migrate import --include='*.pdf,*.mp4' --everything`
   + force push — needs Chris's approval (history rewrite affects all fleet members).
2. **Sandbox was reset.** /root/downloads is empty, /root/workspace/aflinks is
   gone, no browser running. All remaining folders must be re-downloaded from
   the Proton Drive share.
3. **Git clone of AFLinks times out** from this sandbox (multiple attempts:
   full, shallow, sparse, blob-less — all hung >2-3 min). Raw file fetch and the
   GitHub Contents API work fine, so status/report updates can still be pushed
   via the API. The clone problem makes in-repo processing impossible until
   it resolves (possibly repo-size related; may work again after LFS migration
   reduces blob traffic, or from a fresh sandbox).

## DONE (already merged + pushed)
- Batch 1: 59 PDFs (8 authors) — merged
- Ibrahim Karim (7 PDFs), Dowsing Rod Science (8 MP4s)
- Christopher Hills Supersensonics (~35 files; 3 oversized excluded) — pushed
- Enel (28 files; 2 oversized excluded) — pushed
- Tom Graves (5 PDFs) — pushed 2026-09-14 17:40 UTC
- Servranx Brothers (85 PDFs) — pushed 2026-09-14 17:47 UTC
- Videos (14 MP4s) — pushed 2026-09-14 17:49 UTC
- Rugerro Moretto (5 PDFs) — pushed 2026-09-14 18:08 UTC

## REMAINING (needs re-download after unblock)
- Jacques Ravatin (2 files >100MB already identified for exclusion)
- Limited Design Technology (~566MB), Louis Turenne (~1.5GB), Misc Literature (~377MB),
  Radiesthesia Images (~284MB), Stylianos (~67MB), Water Dowsing (~268MB),
  Abbe Mermet, Antonio Rodriguez, Belizal/Chaumery, Bruce Copen, Dave Cowan,
  De La Foye, Energy Activation Telegram, Frances Nixon, Robert Gilbert

## Source
Proton Drive share (Chris): https://drive.proton.me/urls/MM2YV9Z9PM#0EL-9viWFcTn
- fragment key = E2E decryption key; use `cdp open` not `cdp nav`
- **page reload kills transfers** — click once, leave page alone
- per-row `Download` button (query `tr`, click the button whose text is "Download")
- browser watchdog: `cdp open <url>` if eval protocol-times-out

## HARD RULES
- **GitHub rejects any file >100MB.** Skip them; record in `radiesthesia_large_excluded` (title, size_mb, md5, reason).
- **library_feed.json conflicts on nearly every rebase** (fleet rebuilds it). Resolve by taking the commit's version (`git show ":3:library_feed.json"`), then continue.
- **Push races**: fleet pushes constantly. Use a retry loop (fetch → rebase → push, up to 5x).
- build_library_feed.py DOES regenerate `radiesthesia_books` from `books/radiesthesia/**` on disk (md5-cached), so the key survives future syncs.

## Recipe per completed zip
extract → per-file md5 → skip >100MB (record) → skip dupes → copy to books/radiesthesia/<slug>/ → append feed entry → rm zip → commit → retry-push.
