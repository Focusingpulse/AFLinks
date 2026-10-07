# Drunvalo Activity Log

## 2026-10-06 08:10 UTC — aetherforce-translation-qc

**Status**: ✅ OK

**Task**: Translation QC cron (4h, cloud sandbox)

### Context
Full clone no longer fits on sandbox disk (repo .git alone >4.4G, 9.8G disk). Killed clone, ran entirely via Contents API + raw fetches.

### QC Results
| Check | Result | Status |
|-------|--------|--------|
| Feed entries not in DB (basename-normalized) | 7 (Forge Oct-6 batch) | ➕ Added |
| Same-file duplicate groups | 0 | ✅ |
| Title-similarity clusters (difflib ≥0.75) | 3 → 1 real dupe folded | ✅ |
| date=="unknown" sweep | 0 | ✅ |
| Dangling person→work refs | 0 | ✅ |
| Dangling cross_refs | 4 (synthesis- prefix ids) | 🔧 Fixed |
| Source URL verification | 7/7 HTTP 200 | ✅ |

### Fixes Applied
- **+7 works** to research-index: Zenin (ru, water environment), Koltovoy (ja, ether models survey), Hoshino (ja, new aether theory — gravitation), Amici (it, radionics & ancient Egypt), Mizuno (ja, cold fusion project), Takahashi Akito (ja, cold fusion frontier 2011), Arias Salguero (es, art of the Zahorí / Costa Rica dowsing)
- **Folded 1 dupe pair**: campi-elettromagnetici-e-memoria-dell-acqua-it == electromagnetic-fields-and-the-memory-of-water-a-challenge-that-continues-it (both 2026-09-11, it, same Rome Coherence paper)
- **+4 persons**: Stanislav Zenin, Nikolai Koltovoy, Akito Takahashi, Mario Enrique Arias Salguero
- **Updated 3 persons**: hoshino, amici, mizuno (new works_in_collection links)
- **Fixed 4 cross_refs** in synthesis-teslaphoresis-experimental-bridge (synthesis- prefixed ids → actual bare-slug ids; known schema pitfall, this time in my own synthesis cron's entry)
- Index sizes after: **481 works, 407 persons**

### Notes
- translations/ empty by design (publish boundary 2026-09-20)
- tag_concepts.py dead (reads index.json) — skipped
- 2 of 3 title clusters were distinct works (fr-Wikipedia vs cours; two Akhand Jyoti articles) — left in place

## 2026-10-06 06:13 UTC — aetherforce-database-refresh

**Status**: ✅ OK

**Task**: Daily database refresh cron (cloud sandbox)

### Context
Clone timed out at 90s (repo size ~97k files). Used Contents API fallback for QC checks.

### Indexes Checked
- **research-index.json**: 474 works (up from 263 on 2026-09-25)
- **person-index.json**: 403 persons (up from 226)
- **library_feed.json**: 30MB (verified via blob sha, Contents API returns encoding=none)

### QC Results
| Check | Count | Status |
|-------|-------|--------|
| Class 7 duplicates (same file, different ids) | 0 | ✅ |
| Class 9 unknown dates | 0 | ✅ |
| Dangling cross-refs | 3 | ⚠️ Expected (synthesis entries) |
| Dangling person work refs | 0 | ✅ |
| Stub works (no themes/claims) | 45 | ⚠️ By design (Forge dossiers) |

### Notes
- **translations/ empty**: Expected (publish boundary 2026-09-20)
- **Builder not run**: No living-library projection in sandbox
- **Growth**: +211 works, +177 persons since 2026-09-25 (Forge batch translations)

### Report
- [report-2026-10-06-061300.json](./report-2026-10-06-061300.json)

---

# Drunvalo Activity Log

## 2026-09-25 20:00 UTC — aetherforce-translation-qc

**Status**: ✅ OK

**Task**: QC database indexes (publish boundary: translations/ retired)

### Context
As of 2026-09-20, full translated text is no longer published to the public repo (Berne Art. 8). QC now targets database indexes and feed integrity, not translation files.

### Indexes Checked
- **research-index.json**: 263 works (up from 247 on 2026-09-23)
- **person-index.json**: 226 persons (up from 221)
- **synthesis_index.json**: 117 reports, newest entry 2026-09-22
- **library_feed.json**: 25.6 MB (verified via blob sha, Contents API returns encoding=none for large files)

### Issues Found & Fixed
- **Dangling author ref**: Work `torsion-7900km-nonlocal-water-experiment-scalarwave-zh` had author `scalarwave-cc` which doesn't exist in person-index. Fixed by removing the author (scalarwave.cc is the source domain, not a person).
  - Commit: [fc40ec7](https://github.com/Focusingpulse/AFLinks/commit/fc40ec73c9ec5a54985ba3d7ea0704600d292db8)

### Issues By Design
- **102 stub works**: Works with empty themes/claims. These are Forge dossiers that live in agent memory; DB entries are map pointers only.
- **Empty translations/ dir**: Expected (publish boundary).

### Checks Passed
- No duplicate work IDs
- No duplicate person IDs
- Synthesis index current (newest entry >= newest file)
- Library feed populated (verified via sha)
- No dangling cross-refs (except the one fixed above)

### Report
- [report-2026-09-25-200620.json](./report-2026-09-25-200620.json)

---

## 2026-09-15 08:10 UTC — aetherforce-translation-qc

**Status**: ✅ OK

**Task**: QC recent AFLinks translations, fix issues, update DB

### Files Checked (5 most recent)
1. `2026-09-15-enel-energeia-reprints-2025-2026-fr-en.md` — Frontmatter incomplete (fixed)
2. `2026-09-15-andre-simoneton-radiovitalite-fr-en.md` — Complete, no issues
3. `2026-09-14-radionique-machine-shelf-2026-fr-en.md` — Frontmatter incomplete (fixed)
4. `2026-09-14-frandeau-fortuna-major-patent-fr-en.md` — Frontmatter incomplete (fixed)
5. `2026-09-14-francis-marquette-cera-fr-en.md` — Frontmatter incomplete (fixed)

### Issues Found & Fixed
- **Missing frontmatter fields**: Files 1, 3, 4, 5 were missing standard translation metadata (`source_language`, `language`, `translator`, `source`, `sources`, `date_published`)
- **Fix applied**: Added complete frontmatter to all 4 affected files

### Commits
- [19f3ed6](https://github.com/Focusingpulse/AFLinks/commit/19f3ed63fe0f12efaeabfd889d7de2741334329c) — Enel Energeia reprints frontmatter fix
- [eaf879d](https://github.com/Focusingpulse/AFLinks/commit/eaf879d5b91a38d56fa141a0e99d4598f7091020) — French radionics machine shelf frontmatter fix
- [23b0d8c](https://github.com/Focusingpulse/AFLinks/commit/23b0d8c94134bb54e1b078dc3ac4c83e34af7fe0) — Frandeau Fortuna Major patent frontmatter fix
- [c9d0855](https://github.com/Focusingpulse/AFLinks/commit/c9d0855a3dd1170a86f052ef63f5ce46389a0e06) — Francis Marquette C.E.R.A. frontmatter fix
- [a83bf88](https://github.com/Focusingpulse/AFLinks/commit/a83bf884663c44b957adac57dc74c7e6f869438d) — Status report push

### Database Updates
None required — all researchers mentioned in translations (Enel, Guy Thieux, André Simoneton, Frandeau de Marly, Francis Marquette, Heckmann, Steïmann) already present in `person-index.json`

### Source Verification
All source URLs verified accessible (HTTP 200/301 responses)

### Duplicate Check
No duplicate translations found — each file covers distinct source material

### Notes
- Clone timeout workaround used: GitHub Contents API for all file operations
- `tag_concepts.py` exists in repo but not executed (no local clone available)

---
*Previous entries continue below*

## 2026-09-15 20:20 UTC — aetherforce-translation-qc

**Status:** ok

Checked the 5 newest translations (all 2026-09-15, Forge-authored): Simoneton radiovitality dossier, Blanche Merz hauts-lieux dossier, Enel Energeia reprints dossier, Simoneton-vs-biophotonics bench note, Merz high-places inter-rater bench note.

**Issues found & fixed (4):**
1. Bench-note frontmatter was thin (only name/description) — added translator, source_language, language, date_published, sources.
2. Factual error in bench note: "Alfred Bovis" → **André** Bovis (corpus record: André Bovis 1871–1947, confirmed across the other three dossiers).
3. research-index.json: 4 duplicate work ids re-emitted by the translation agent (andre-simoneton-radiovitalite ×2, jacques-ravatin ×2, shipov-torsion ×2, study-on-torsion-fields-de ×2) — merged keeping richer entries, 222→218. Added the 2 missing bench-note works (→220 effective).
4. person-index.json: 2 duplicate persons (blanche-merz/merz-blanche, andre-simoneton/simoneton-andre) — merged with union of works/cited_by/domains, 179→177.

**Verified:** 5 source URLs all resolve (editions-tredaniel, mrbienetre, psi-gamma, inexplore ×2). No untranslated passages — all FR/DE/ES quotes carry inline English translations. No new duplicate translation regrowth since the 12:20 UTC purge (filename-cluster scan of all 125 files: 3 clusters, all intentional translation+original pairs).

**Method note:** git clone hangs from this sandbox (known issue); entire run done via GitHub Contents API (one commit per file). Commits: 6611b62f, dd163f54, c01ec16f, 2ee488c9.

**Open:** root-cause fix for duplicate re-emission still belongs in the emitting translation agent (agent-75b8d29e) — content-hash/source-URL check before write.

## 2026-09-20 04:16 UTC — aetherforce-translation-qc
- QC'd 5 most recent translations (2026-09-18 batch: biodynamic-es, cesty-psychotroniky-cs, drbal-patent-cs, kozyrev-ru, kozyrev-fa). All well-formed, fully translated, no mojibake/interleave damage.
- Fixes: trimmed zerkoz.ru site boilerplate from kozyrev-ru (contact block, share/latest-promos, series index); added verified live source URLs to 4 files (cesty → fsoft.cz/rf/jcbp/casopis1/c1.htm found via Wayback CDX; drbal patent PDF; beee.es URL punctuation; iWell-Guard marked verified).
- DB: research-index 5 stub entries enriched (themes/concepts/key_claims/xrefs; biodynamic authors corrected goethe→Geier/Fritz/Steiner); merged 4 dup work ids sharing identical files (220→216); fixed 43 dangling author refs (15 alias-mapped, agent names removed from authors, 8 person stubs added); fixed 3 dangling crossrefs (file paths→work ids).
- person-index 202→215: +Pravdivtsev, Rejdák, Kafka, Geier, Fritz, Shevtsev, Astroya, Maglione, Laska, Orpanit, A.Pedro, J.Schang, Encyclopédie-de-Brocéliande; Drbal patent added to his works (was flagged "not yet in archive"); hecquet path typo fixed.
- Collision check passed: all pushes survived concurrent fleet activity (the za-tajemstvim probe was a false alarm — string is in the surviving file path, not a work id).
- Note: 18 person works_in_collection paths reference translation files not yet indexed in research-index (indexing gap, files exist).
- Clone timed out from this sandbox again (90s); entire run via Contents API. 10 pushes, all OK.


## 2026-10-07T08:05:00Z — aetherforce-translation-qc (08:00 UTC)
- Standing checks all clean (same-file dupes, unknown dates, dangling cross-refs, feed mojibake, feed dupes).
- Russian title-similarity hits = Cyrillic-stripping false positives (distinct works); Sitkowski pair left as distinct books.
- **Folded** bricage cross-convention dupe pair: `bricage-afscet-dowsing-protocol-fr-en` → `2026-10-04-bricage-dowsing-meta-analysis-fr` (same AFSCET 2025 dowsing-testing paper, excerpt-confirmed). Keeper cross-ref + person ref remapped.
- **+6 works** from Forge's Oct-7 batch (in feed, not DB): SENTERIS 2nd study (Varvoglis & Dullin, IMI), ČEPES Czech psychoenergetics, Risy NOTES 6 Young's-holes torsion experiments, Levent Aslan on Kozyrev ether/time (tr), CIA holographic-mind declass docs (ru), Korean OpenWiki cold fusion (ko).
- **+4 persons**: mario-varvoglis, eric-dullin, daniel-risy, levent-aslan.
- Fixed alan-de-gois-cesar ref (quasi→quase) and removed bricage stub file ref.
- Did NOT fold brazilian-scalar 09-03/09-11 pair — insufficient evidence (only 09-11 excerpt available, WO2013155580A1).
- Index sizes: 514 works, 431 persons. Commits c4a1a07fb (research-index), 79010072c (person-index). Collision re-check scheduled.
