---
description: Live state of radiesthesia archive batch 2 (2026-09-14). Cron "rhostudio-batch2-finish" continues this work. Delete this file when batch 2 is fully merged.
date: 2026-09-14
---

# Radiesthesia Batch 2 — Live State

## Source
Proton Drive share from Chris: https://drive.proton.me/urls/MM2YV9Z9PM#0EL-9viWFcTn
(fragment key = E2E decryption key; use `cdp open` not `cdp nav`; page reload kills transfers)

## Already merged (74 entries in library_feed.json)
- Batch 1: 59 PDFs in books/radiesthesia/{abbe-mermet,antonio-rodriguez,belizal-chaumery-morel,bruce-copen,dave-erina-cowan,frances-nixon,jean-de-la-foye,robert-gilbert}/ (~355MB)
- Batch 2 partial: 7 Ibrahim Karim PDFs in books/radiesthesia/ibrahim-karim-biogeometry/ + 8 Dowsing Rod Science MP4s in books/radiesthesia/dowsing-rod-science/ (~391MB)

## Remaining folders downloading to /root/downloads (clicked individually via per-row Download button)
1. Christopher Hills - Supersensonics (~812MB) — mp3s/audio?
2. Enel — ?
3. Jacques Ravatin (~661MB)
4. Limited Design Technology (~566MB)
5. Louis Turenne (~1.5GB) — large
6. Misc Literature (~377MB)
7. Radiesthesia Images (~284MB)

## Recipe per completed zip
```bash
cd /tmp && rm -rf ex && mkdir ex && cd ex && unzip -q '/root/downloads/<folder>.zip'
# dedupe by md5 against books/radiesthesia/** and within batch, skip _-prefixed
# copy to books/radiesthesia/<slug>/ with spaces -> hyphens
# append json entries to library_feed.json radiesthesia_books (title, author, pdf, size_mb, md5, provenance)
cd /root/workspace/aflinks && git add books/radiesthesia/<slug> library_feed.json && git commit -m "radiesthesia batch2 <slug>" && (git pull --rebase origin main || true) && git push origin main
```

## Stuck downloads
If a .crdownload stalls >20 min, re-click the folder's row Download in the browser page via `cdp eval` over the tr list. Two folders stuck at tiny sizes initially (62B / 1330B) — Enel and Radiesthesia Images likely.

## Completion criteria (then delete this cron + this file)
- All 7 folders above extracted, deduped, copied into books/radiesthesia/, feed entries added, committed and pushed.
- Update drunvalo/blind-spots-progress-2026-09-14.md item 3 to Done.
