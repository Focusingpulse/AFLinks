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
## REMAINING (downloading to /root/downloads as of 2026-09-14 10:25 UTC)
1. Jacques Ravatin (~661MB)
2. Limited Design Technology (~566MB)
3. Louis Turenne (~1.5GB)
4. Misc Literature (~377MB)
5. Radiesthesia Images (~284MB)

## HARD RULES
- **GitHub rejects any file >100MB.** Skip them; record in `radiesthesia_large_excluded` (title, size_mb, md5, reason).
- **library_feed.json conflicts on nearly every rebase** (fleet rebuilds it). Resolve by taking the commit's version (`git show ":3:library_feed.json"`), then continue.
- **Push races**: fleet pushes constantly. Use a retry loop (fetch → rebase → push, up to 5x).
- build_library_feed.py DOES regenerate `radiesthesia_books` from `books/radiesthesia/**` on disk (md5-cached), so the key survives future syncs.

## Recipe per completed zip
extract → per-file md5 → skip >100MB (record) → skip dupes → copy to books/radiesthesia/<slug>/ → append feed entry → rm zip → commit → retry-push.
