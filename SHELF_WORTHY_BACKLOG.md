# Shelf-Worthy Backlog — AFLinks

Status of every visible feature, verified by live audit on 2026-08-31.
Legend: ✅ verified working · 🔧 fixed this pass · ⚠️ known gap · 🧹 remove/hide

## Data layer (the treasure)

| Feature | Status | Notes |
|---|---|---|
| Archive index (11,982 docs) | ✅ | All categorized; 1,103 (9%) lack text previews (media/corrupt/await-OCR) |
| Concept tags on every record | ✅ | `concepts` field present; tagger runs each sync |
| Researcher index (59 DB / 1,193 extracted) | ✅ | Feed top-12 researchers render with sources |
| Patent index (2,339 DB) | ✅ | Patent tags render on cards + modal |
| viXra streaming | ✅ | 5,810+ entries merged; queue continues |
| Atsyukovsky Book 5 translation | ✅ | 62 translations published; reader modal works |
| Declassified records (16 finds, 9 countries) | 🔧 | Files now ship to site; cards open in reader modal (were unclickable) |
| Scout finds | 🔧 | Empty find entries filtered — no more dead cards |
| Slim search index | 🔧 | `search_index.json` 13.4MB vs 21MB full; detail modal lazy-loads chunked full records |

## Link integrity (audited this pass)

| Check | Result |
|---|---|
| Hardcoded remote URLs (51) — AF articles/shop/resources, Rex, GitHub, Telegram | ✅ 0 broken |
| In-site assets (books/, sources/, translations/, index.json) | ✅ all present |
| Dynamic source URLs (30-doc sample: viXra PDFs, tuks, rex) | ✅ 0 broken |
| Declassified/ dir shipped | 🔧 was absent from site — now published |

`audit_links.py` is the repeatable link-integrity layer (add to a weekly cron).

## Remaining gaps (the real backlog)

1. ✅ **AF category map coverage — DEEP-LINKED (Aug 31)** — 48 categories now each carry 1-5 specific verified articles (93 total permalinks, all HTTP 200, WordPress REST inventory of 534 posts). Featured fallback extended 18 → 34. Automated consistency check: map titles === URL keys (no silent collection-page fallback). Only Finance/Economics intentionally unmapped (no honest AF article; featured fallback still gives specific pages).
2. ✅ **Category normalization DONE (Aug 31)** — 47 → 44 canonical labels: Biology/Health→Biology, Water/Hydrogen→Water, Environmental→Environment/Climate (all zero-overlap splits, merged additively). Energy vs Energy Generation kept (genuinely distinct). `normalize_categories.py` idempotent; concept-map canonicalized; feed-builder guards against dead labels; AF map consolidated. Verified: 0 docs/feed entries with absorbed labels.
3. **Search depth cap** — slim index searches title/categories/600-char preview. Full-doc search needs tokenized posting (Web Worker) — defer until 30k+.
4. ✅ **Preview fill DONE for text-fixable docs (Aug 31)** — `fix_previews.py` (cloud, pymupdf text + Tesseract OCR fallback) filled **316 PDFs**: 251 viXra + 67 tuks. Docs with previews 10,879 → 11,195. Remaining 788 are media wrappers (mp3/mp4/zip/torrent — not text-fixable) + 99 dead hosts + 2 no-text. `preview_manifest.json` + `PREVIEW_CONTRACT.md` in repo for external OCR workers. Marked unreachable entries retry-able with --retry-unreachable.
5. **lens.html** — no data fetch; verify it's a static curated page vs a broken feature. If placeholder, hide it or wire it.
6. **Declassified record content** — each md should carry real outbound URLs to the source; spot-verify all 16.
7. ✅ **Vault seam/vesica FIXED (Aug 31)** — audited all 276 meta pairs (0 dead). Fixed two click-through defects: (1) seam rows now open the FULL connected fabric (both + crossings) via ?seam=1, so crossing docs shown in the vault appear in the result set; (2) id-space mismatch (seam index string ids vs search index int ids) resolved with coercion — seam clicks previously landed empty. Verified: sample seam opens 2,670 real docs.
8. **Translation reader for Book 5** — progress bar + assembled reader confirmed working; verify chunk manifest stays current as book5-translate cron runs.

## Scale agenda (target 20–30k docs)

- viXra: 46k papers available; queue at ~6,923 crawled, processing continues every sync
- Workers now live: i-sis.org.uk (~2k), padrak.com/ine (~130) — crons `aflinks-worker-isis`, `aflinks-worker-padrak`
- Remaining sites available to take: ether.sciences.free.fr (~50), filestore.orgfree.com (~200), psionicresearch.com, strikefoundation.earth, cernohajev.omeka.net, magneticenergy.org, newphysics.se, merlib.lackluster.org, borderlands.de (Wayback), keychests.com (Wayback)
- Each site = one worker (see PARALLEL_SCRAPE.md). Friend agents with spare accounts can each take one.

## Rule of the vault
Every visible card opens something real. Any feature that cannot be made functional gets hidden until it can — no "coming soon", no decorative text.