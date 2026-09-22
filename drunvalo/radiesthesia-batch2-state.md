---
description: Live state of radiesthesia archive batch 2 (2026-09-14). Cron "radio-batch2-finish" (id 013b2d33, cloud, every 30m) continues this. Delete this file when done.
date: 2026-09-14
---

# Radiesthesia Batch 2 — Live State

## Source
Proton Drive share (Chris): https://drive.proton.me/urls/MM2YV9Z9PM#0EL-9viWFcTn
- fragment key = E2E decryption key; use `cdp open` not `cdp nav`
- **page reload kills transfers** — click once, leave page alone
- per-row `Download` button (query `tr`, click the button whose text is "Download")
- browser watchdog: `cdp open <url>` if eval protocol-times-out

## DONE
- Batch 1: 59 PDFs (8 authors) — merged
- Ibrahim Karim (7 PDFs), Dowsing Rod Science (8 MP4s)
- Christopher Hills Supersensonics (~35 files; 3 oversized excluded) — pushed
- Enel (28 files; 2 oversized excluded) — pushed
- Tom Graves (5 PDFs) — pushed 2026-09-14 17:40 UTC
- Servranx Brothers (85 PDFs) — pushed 2026-09-14 17:47 UTC
- Videos (14 MP4s) — pushed 2026-09-14 17:49 UTC
- Rugerro Moretto (5 PDFs) — pushed 2026-09-14 18:08 UTC
- Jacques Ravatin (32 files; 2 oversized excluded) — pushed by fleet
- Limited Design Technology (68 files) — pushed by fleet
- Misc Literature (83 files) — pushed by fleet
- Radiesthesia Images (723 files) — pushed by fleet

## REMAINING
None — batch 2 complete.

## FINAL STATUS (2026-09-14 19:37 UTC)
All 5 remaining folders successfully merged and pushed:
1. Radiesthesia Images (723 files, 284MB) — pushed
2. Misc Literature (83 files, 377MB) — pushed
3. Limited Design Technology (68 files, 1 oversized excluded) — pushed
4. Jacques Ravatin (32 files, 2 oversized excluded) — pushed
5. Louis Turenne (30 files, 7 oversized excluded) — pushed

Total batch 2 additions: ~936 files, ~1.6GB (excluding oversized)
Oversized files (>100MB, GitHub hard limit): 10 total, recorded in library_feed.json radiesthesia_large_excluded

## DISK SPACE CONSTRAINT
- 9.8GB disk, 90% used (1.1GB available)
- Process one folder at a time, push, then clean before next
- 2 files >100MB excluded from Jacques Ravatin:
  - L-Emergence-de-l-Enel-Ou-l-Immergence-Des-Reperes-Tome-I-Jacques-Ravatin.pdf (151MB, c6cd42638b311557e45c8693136ecb28)
  - L-Emergence-de-l-Enel-Ou-l-Immergence-Des-Reperes-Tome-IV-Jacques-Ravatin.pdf (234MB, 65ca94135ff362d4e9e40ea359e603f3)

## HARD RULES
- **GitHub rejects any file >100MB.** Skip them; record in `radiesthesia_large_excluded` (title, size_mb, md5, reason).
- **library_feed.json conflicts on nearly every rebase** (fleet rebuilds it). Resolve by taking the commit's version (`git show ":3:library_feed.json"`), then continue.
- **Push races**: fleet pushes constantly. Use a retry loop (fetch → rebase → push, up to 5x).
- build_library_feed.py DOES regenerate `radiesthesia_books` from `books/radiesthesia/**` on disk (md5-cached), so the key survives future syncs.

## Recipe per completed zip
extract → per-file md5 → skip >100MB (record) → skip dupes → copy to books/radiesthesia/<slug>/ → append feed entry → rm zip → commit → retry-push.
