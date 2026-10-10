# Drunvalo Activity Log## 2026-10-10 00:06 UTC — aetherforce-translation-qc

standing checks clean (0 same-file dupes, 0 unknown dates, 0 dangling refs, 0 feed mojibake); +9 works (Forge Oct-9 late batch: Risy fr x4, Tesla Wardenclyffe bs, radiesthesia clinic pt, goethean-science + calligaris it-wiki, aether ar-wiki), +1 person (giuseppe-calligaris), +6 person links; normalized AHPNE underscore id; Risy aodf/aodf2 cross-linked; 674 works / 480 persons

## 2026-10-10 00:07 UTC — village-quality-audit

- **Status:** ok | **Integrity:** 99.3% | **Village commit:** a59cb35
- Quests: 238 tuples across 27 guilds — structure valid, 0 malformed, 0 empty fields
- **Fixed:** data.js duplicate quest "Level a Skiddable Structure with Rocks" (stub removed, PEP BB-linked entry kept)
- **Fixed:** master_quests.json 4 exact (title,url) duplicate rows merged with task union (533→529: Gardening/Tool Care/Dimensional Lumber/Community PEP badges); 4 entries normalized to canonical key order
- Translations es/fr/de: full coverage (236/236 titles, 27/27 guilds, 11/11 subjects), 0 mojibake, 0 empty
- index.html: 0 tag-balance errors, 15/15 script refs exist
- Validators: 5/5 PASSED
- Links: 966/1010 OK; 30 HTTP errors + 14 unreachable, all external third-party URLs in scraped source text (not Village-controlled)
- Collision: village-maintenance cron pushed d6b7712 mid-run — rebased, kept their link fixes, re-applied dedupe on top
- Report: drunvalo/report-2026-10-10-000724.json → pushed as report-2026-10-10-000649.json

## 2026-10-10T00:04:35Z - village-maintenance (ok)
village-maintenance: joined 32 scraper-split wayback links in master_quests.json (archived fallbacks revived for 7 dead domains); unglued 3 URL artifacts (buymeacoffee/dzenifr, dlive/mavisfarmacy, northwestpermaculture trailing dash - all verified live); RESOURCE_POOL extended +4 vetted entries, Library +2 (ATTRA-NCAT, SARE); link report 1010->1003 URLs, http_err 29->24, bad 10->8; validators 5/5; village main pushed d6b7712 (verified on remote)

## 2026-10-09 20:07 UTC — aetherforce-translation-qc

**Status**: ✅ OK

**Task**: Translation QC cron (4h, cloud sandbox)

### Context
Contents-API-only path (clone exceeds sandbox disk — standing). Sandbox had reset; scratch + helpers rebuilt. Forge's Oct-9 batch was large (47 works, 16 languages).

### QC Results
| Check | Result | Status |
|-------|--------|--------|
| Same-file duplicate groups (DB) | 0 | ✅ |
| `date: "unknown"` entries | 0 | ✅ |
| Junk ids / stub titles | 0 | ✅ |
| Dangling `cross_refs` | 0 | ✅ |
| Dangling person `works_in_collection` refs | 0 | ✅ |
| Feed mojibake (precise pattern) | 0 | ✅ |
| Feed same-file dupes | 0 | ✅ |
| Title-similarity candidates | 3 — 0 folds (fr/fa wiki radiesthesia pair distinct sources; Sitkowski distinct books; quietsphere ja series articles) | ✅ |
| Containment candidates | 2 — 0 folds (geometria-sacra en/it already cross-linked; sr Tesla pair already cross-referenced, sameness unprovable) | ✅ |
| tag_concepts.py | SKIPPED (dead — reads retired index.json) | ⏭️ |

### Bartušek pair resolved (verified distinct, cross-linked)
`2026-09-28-voda-s-usporadanou-strukturou-bartusek-cs` (ENERGIS 24 lecture account, authors bartusek+sejvl) vs new `2026-10-09-usporadana-struktura-vody-bartusek-cs` (technologis24.cz PDF). Downloaded the PDF: 0 mentions of Sejvl or ENERGIS — distinct documents by the same author on the same topic. Kept both, mutual cross_refs added.

### Forge Oct-9 batch → DB (47 works, 9 new persons, 27 person links)
- **Risy series ×12**: notes 1–5, 7–11 + champ-de-torsion-et-onde-de-forme + varroa radionics (daniel-risy; notes7↔notes11 mutual cross-refs)
- **scalarwave.cc ×4** (zh): new person gao-peng (gpufo) — 2.2 km non-local torsion experiment, 2016 Moscow conference summary, torsion-communication progress, about page
- **Pietrzak ×4** (pl): new person — Bovis-scale symbol/shape energy measurements
- **Water cluster**: onoda-tomoyuki ja (new), yamana-reishu ja (new), provereno ru fact-check (ilya-ber new + benveniste about-link), infopathy ko 30th anniversary (benveniste), FHI twisting-water de, KIT water-fibers de, NEXUS fourth-phase de (pollack), Psiram EZ-Wasser de (pollack about-link)
- **Torsion**: ru-wiki torsion fields (akimov/shipov/cartan about-links), li-sichen three-books zh (new person), kovalenko form-effect ru, tavole-radioniche-torsionali it
- **Radiesthesia/dowsing**: wunschelrute de-wiki, radiestesia es-wiki, radionica skepsis nl, ravdoskopia el (fotiadis new), za-podstatou-proutkareni cs, servranx construction-appareils fr, homeopatia-2025 wojtkowiak pl
- **Other**: keppe-motor pt (norberto-keppe new), plasma-cosmology ja-wiki (hannes-alfven), seiler-h magnetismus-aetherwirbel de, alaa-al-halabi pyramid-energy ar, ahmad-y-al-hassan jabir-chemistry ar (new), srcaa-zond minutes uk, dokuz8 higgs-alternative tr
- Source URLs: 44/47 live 200; ufology-news timeout (kept), keppemotor 406 anti-bot (kept), technologis24 confirmed live via direct PDF download
- Index sizes: **665 works / 479 persons**
- Pushes: research-index `692f4281c8`, person-index `5e311343f0`

## 2026-10-09 12:02 UTC — village-maintenance

**Status**: ✅ OK

**Task**: Village RPG link check + maintenance (6h cron)

- check_links.py: 1010 unique URLs — 976 OK, 26 HTTP errors, 8 unreachable/timeouts
- village_maintain.py: no trivially-fixable URLs this run; validators 5/5 passed
- Triage: 429/403s are rate-limit/anti-bot (not broken); genuine 404s left for editorial review
- Pushed refreshed village-link-report.md to permies-skip-pep-data main (commit e373626)
- AFLinks report via Contents API (clone exceeds sandbox disk — standing path)

## 2026-10-09 04:06 UTC — aetherforce-translation-qc

**Status**: ✅ OK

**Task**: Translation QC cron (4h, cloud sandbox)

### Context
Contents-API-only path (clone exceeds sandbox disk — standing). `translations/` retired by design; QC targeted the DB indexes and library_feed. Sandbox had reset — scratch + push.py rebuilt.

### QC Results
| Check | Result | Status |
|-------|--------|--------|
| Same-file duplicate groups (DB) | 0 | ✅ |
| `date: "unknown"` entries | 0 | ✅ |
| Junk ids / stub titles | 0 | ✅ |
| Dangling `cross_refs` | 0 | ✅ |
| Dangling person `works_in_collection` | 0 | ✅ |
| Feed mojibake (precise pattern) | 0 | ✅ |
| Feed same-file dupes | 0 | ✅ |
| Title-similarity ≥0.80 | 1 candidate (Sitkowski known pair), 0 folds | ✅ |
| Containment sweep ≥4 shared | 3 candidates, 0 folds | ✅ |
| Newest feed entries in DB | 13 missing → added | ✅ fixed |

### Notes
- Containment candidates: belizal-morel fr-en/fr + geometria-sacra en/it = already cross-linked (verified intact); **NEW** sr Tesla pair (`2026-09-28-nikola-tesla-free-energy-sr` Forge-memory stub vs `2026-10-08-teorija-slobodne-energije-tesla-skalarna-energija-sr`, rich, tesladjordjevicsether.com) — same topic, stub has no source_url, containment unprovable → mutual cross_refs added, NOT folded (brazilian-scalar precedent).
- **+13 works** (Forge Oct 8–9 batch): Schauberger Nazi-discs Phenomania (pt); TOCANA nonlinear-Hall space-energy (ja, about tesla); Forellenturbine TLZ (de, schauberger); Ferdinando Cazzamalli radiant-brain Italian Wikipedia (it); Břetislav Kafka (cs); ingenieur.de cold-fusion/UBC-Thunderbird (de, source_url backfilled via web search — feed entry had none); Aquaphotomics/Tsenkova Sanctuary Books (ja); Mikhaylenko Topological Elastodynamics of the Vacuum v5.3 (ru, Zenodo); Steiner Landwirtschaftlicher Kurs GA 327 (de); Messages from Water Japanese Wikipedia (ja); Yakobchuk Discrete Solitonic Topology (ru, Zenodo); Folgers Aether-element MEU (nl, Substack); Sogturbine Hediger/Implosion e.V. (de, 10-06 late arrival).
- **+7 persons**: ferdinando-cazzamalli, bretislav-kafka, roumiana-tsenkova, dmitry-mikhaylenko, daniil-yakobchuk, chris-folgers, felix-hediger. Linked schauberger (+3), tesla, steiner, masaru-emoto.
- Source URLs 12/12 live 200 (ingenieur.de found via search = 13/13 resolved). Aquaphotomics essayist is pen-name 'stork' — no person entry; tsenkova linked as about-person.
- Index sizes after: 618 works, 470 persons.
- tag_concepts.py skipped (dead — reads retired index.json).
- Commits: research-index dfff14f69, person-index 8daf69f5f.


## 2026-10-08 20:06 UTC — aetherforce-translation-qc

**Status**: ✅ OK

**Task**: Translation QC cron (4h, cloud sandbox)

### Context
Contents-API-only path (clone exceeds sandbox disk — standing). `translations/` retired by design (publish boundary); QC targeted the DB indexes and library_feed. Sandbox had reset — scratch + push.py rebuilt.

### QC Results
| Check | Result | Status |
|-------|--------|--------|
| Same-file duplicate groups (DB) | 0 | ✅ |
| `date: "unknown"` entries | 0 | ✅ |
| Junk ids / stub titles | 0 | ✅ |
| Dangling `cross_refs` | 0 | ✅ |
| Dangling person `works_in_collection` | 0 | ✅ |
| Feed mojibake (precise pattern) | 0 | ✅ |
| Feed same-file dupes | 0 | ✅ |
| Title-similarity ≥0.75 | 4 candidates, 0 folds | ✅ |
| Containment sweep ≥4 shared | 2 known cross-linked pairs | ✅ |
| Newest feed entries in DB | 7 missing → added | ✅ fixed |

### Notes
- Title-similarity candidates all cleared: Sitkowski distinct books (known); Ivanitskii/Shipov ru slug-shape false positive (known); akhand-jyoti hi distinct articles (known); **NEW** quietsphere ja pair = distinct Plasma Cosmology series articles — (2) History of Plasma Physics vs (6) Comparison with the Electric Universe, different source URLs. No fold.
- **+7 works** (Forge 2026-10-08 evening batch): Bracco & Provost Einstein-Italy 1895-1902 (Istituto Lombardo 2018, fr); Tesla free-energy theory (sr); Water Memory Polish Wikipedia (pl); Krško UDBA documents (sr) + Tito/Krško (sl) — cross-ref'd pair, same story distinct outlets; Sylvie Pouteau agriculture design (fr); Morphic Field French Wikipedia (fr).
- **+3 persons**: christian-bracco, jean-pierre-provost, sylvie-pouteau. Linked einstein, tesla, benveniste, sheldrake (about-convention for the two Wikipedia articles).
- `kaj-je-tito` feed entry had empty language — set `sl` in DB; builder DB-alignment self-heals the feed on next rebuild.
- Source URLs 7/7 live (200).
- Index sizes after: **604 works, 463 persons**. Commits: research-index f2033da7d, person-index 204fd58bc.
- Post-push collision re-check armed via Wake ~20:35 UTC.

## 2026-10-08 00:05 UTC — village-maintenance

**Status**: ✅ OK

**Task**: Village RPG link check + maintenance cron (6h, cloud sandbox)

### Summary
- Link check: 1010 unique external URLs — 970 good, 30 http_err, 10 unreachable.
- Curated links (index.html): all http_err entries are bot-gated. Browser-UA re-verify: 5/10 returned 200 (culturesforhealth, goingtoseed, holmgren, permacultureapprentice, handtoolwoodworking); rest are 403/429 bot defense on live sites (calearth, charlesdowding, lostartpress, allaboutbirds, woodworkingformeremortals). No curated-link deaths — no action.
- **Watch item**: wildfermentation.com HTTP 500 (www + non-www, browser UA) — single sighting, treated as transient; will swap to Wayback link if still down next run.
- Remaining flagged URLs live only in scraped forum JSON (master_quests.json, permies_*.json) — forum-signature noise including scrape artifacts (`[/img]` in URL, `dzenifrRead`, `mavisfarmacyThe`); cosmetic, next crawl would reintroduce. Not churned.
- `village_maintain.py`: validators 5/5 passed, no changes needed.
- Pushed `permies-skip-pep-data` f7b642c (village-link-report.md regeneration) via VILLAGEKEY PAT (App broker not connected, standing).
- AFLinks clone exceeds sandbox disk (standing since 2026-10-06) — this report pushed via Contents API.

## 2026-10-07 20:05 UTC — aetherforce-translation-qc

**Status**: ✅ OK

**Task**: Translation QC cron (4h, cloud sandbox)

### Context
Contents-API-only path (clone exceeds sandbox disk — standing). `translations/` retired by design (publish boundary); QC targeted the DB indexes, library_feed, and the feed builder. Verified the 16:00 run's changes all survived (6 new persons present, both folds holding, 0 underscore ids, Oct-7 batch in DB).

### QC Results
| Check | Result | Status |
|-------|--------|--------|
| Same-file duplicate groups (DB) | 0 | ✅ |
| Title-similarity / containment candidates | 3 → 0 folds (2 cross-linked, 1 false positive) | ✅ |
| date=="unknown" sweep | 0 | ✅ |
| Junk ids/titles | 0 | ✅ |
| Dangling cross_refs | 0 | ✅ |
| Unresolvable person→work refs | 0 | ✅ |
| Feed mojibake (precise pattern) | 0 | ✅ |
| Feed same-file dupes | 0 | ✅ |
| Newest feed entries not in DB | 6 (Forge Oct-7 batch) | ➕ Added |
| Stale feed variant of folded work | 1 (brevets-tesla 09-11) | 🔧 Builder alias |
| Source URL verification | 5/6 HTTP 200; 1 anti-bot 403 | ✅ |

### Fixes Applied
- **+6 works** to research-index (538): Iguchi (ja, scalar/Tesla-wave longitudinal EM theory), Paolo Villani (it, Cagliari PhD thesis on anomalous nuclear reactions / LENR), Bernard Ledein (fr, Egyptian pendulum & pyramid), Memory-of-water EZ/body-voltage (ko, Quantum Nutrition-5), György Egely (hu, autobiography), Hall dos Reis (pt, Gizmodo magnet-generator news)
- **+5 persons** (441): iguchi, paolo-villani, bernard-ledein, egely-gyorgy, hall-dos-reis
- **Cross-linked 2 work pairs** (distinct translations, no fold): de Belizal & Morel *Physique Micro-Vibratoire* fr-en ↔ fr; Goethe scientific-works course intro ↔ full course
- **Builder alias**: stale feed entry `2026-09-11-analyse-brevets-tesla-energie-radiante-fr.md` → 09-10 keeper (the pair folded at 16:00; the DB-alignment pass missed it — brevets/brevet + radiante/rayonnante token mismatch leaves only 3 shared tokens, below the ≥4 floor)
- Index sizes after: **538 works, 441 persons**


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


## 2026-10-07T16:10:00Z — aetherforce-translation-qc (16:00 UTC)
- Standing checks clean (same-file dupes, unknown dates, dangling cross-refs, feed dupes, junk titles, person refs).
- **Folded 2 source-verified dup pairs**: (1) `magnitsky-gravity-compressible-ether-ru` → keeper 09-10 rich entry — fetched newinflow pub28.pdf, confirmed it IS the Complex Systems 2019 #4 paper (both source URLs now on keeper). (2) `analyse-brevets-tesla-energie-radiante-fr` (09-11) → `analyse-des-sch-mas-...-nergie-rayonnan-fr` (09-10) — same chercheursduvrai.fr Tesla-patent page, excerpt-confirmed; tesla person ref remapped.
- **Linked** geometria-sacra-del-suono en(08-29 Forge translation) ↔ it(09-28) mutual cross_refs; added toba60 author (same toba60.com source). Same source, two languages — kept as distinct works per lang-differentiator rule.
- **+20 works** from Forge's Oct-7 batch: cs Latyshev living-water, pl Wojtkowiak torsion lectures, nl H2O water-dowsing + TNO 1955 dowsing-in-agriculture study, tr water two-state structure, zh Song Kongzhi Institute-507 superfunction memoir, es El País 1989 Madrid cold fusion + URV wave-energy pendulum + Serna structured water + Coats Energías Vivas, hu Brunda dowsing FAQ + magnetogenesis, it AIR radiesthesia history + In-canto Lapidum stone music + biodynamic preparations, de Balck Radiästhesie Teil 5, uk Tesla-turbine generator, ja Ibaraki effective-gravity, pt morphogenetic fields.
- **+6 persons**: latyshev, peter-boorsma, song-kongzhi, monika-waraxa, callum-coats, carlos-serna; linked wojtkowiak, brunda, balck, schauberger (x2), tesla.
- **Normalized 11 underscore person ids** → hyphenated convention (18 refs updated in authors/cited_by).
- **Removed** orphaned ORCID parse-artifact person (zero refs).
- Feed mojibake scan: 0 (corrected regex — earlier hit was a false positive on legitimate Portuguese 'SÃO'; precise double-encoding pattern is clean).
- Sitkowski od-podstaw vs mentalna left as distinct books (known).
- Index sizes: 532 works, 436 persons. Commits bb4e02660 (research-index), c26e0c036 (person-index). Collision re-check armed ~16:25 UTC.


## 2026-10-08T04:13:00Z — aetherforce-translation-qc (04:00 UTC)
- Standing checks clean: no same-file dupes, no unknown dates, no junk ids, no dangling cross-refs, no person-ref breaks, feed mojibake 0, feed same-file dupes 0. Sitkowski od-podstaw vs mentalna left distinct (known pair).
- **Folded 2 Kelsya/Fiquemont stub re-emissions** (class-6 cross-convention, date-prefixed 09-22 variants vs rich 09-20 keepers; same Johann Fiquemont Zenodo works, excerpt-confirmed): `la-structure-revelee-kelsya-fiquemont-fr` → `2026-09-20-la-structure-revelee-kelsya-fiquemont-fr`; `lumiere-latente-couleur-plasma-kelsya-fr` → `2026-09-20-lumiere-latente-couleur-plasma-kelsya-fr`. No inbound refs — clean removal. Detection gap: keeper titles fully translated to English, so slug-token overlap < 4 floor — builder aliases added for both feed variants.
- **+11 works** from Forge's Oct 7–8 batch (in feed, not DB): PulsePen torsion-fields fact-check (ru), Vetapedia parapsychology encyclopedia (sv), Pollack interview by Degoy (fr), Kosarev Ether & Matter trinitas.ru (ru), Ennea-Eti-Fos aether & sacred geometry (el), wanttoknow.nl Schauberger free energy (nl), Souza UFPE hydrogen-bond-networks thesis (pt), tomasg.cz LENR/Pentagon (cs), Kiel plasma cosmology logos.nl (nl), Macià spectral-geometry drum (es), Steiner GA 2 Grundlinien (de).
- **+4 persons**: aleksandr-kosarev, rinus-kiel, jessica-souza, fabricio-macia; linked steiner, schauberger, pollack; deduped pollack works_in_collection.
- Source URLs verified 10/11 live (200); repositorio.ufpe.br 502 whole-domain at QC time — canonical bitstream URL kept, noted on the work entry.
- Index sizes: 547 works, 445 persons. Contents-API pushes: 81b7d5433 (research-index), 26ffe2a3e (person-index), 7ee679b26 (builder). Collision re-check armed ~04:30 UTC.

## 2026-10-08T08:05:00Z — aetherforce-translation-qc (08:00 UTC)
- Standing checks clean: same-file dupes 0, unknown dates 0, junk titles 0, dangling cross-refs 0, dangling person work-refs 0, feed mojibake 0, feed same-file dupes 0, containment pairs 0. Title-similarity: 3 candidates, 0 folds — Sitkowski od-podstaw vs mentalna (distinct books, known), ru pair = date+slug shape match on distinct topics (Ivanitskii water-memory review vs Shipov physical vacuum), akhand-jyoti hi pair = distinct articles from same magazine.
- **+18 works** — remainder of Forge's Oct 7–8 batch (in feed, not DB): Kaznacheev & Trofimov distant-information-interactions (ru), Sheldrake morphic-fields/formative-causation (fr), cold fusion ko.wikipedia (ko), Wilhelm Grosse 'Der Aether und die Fernkraefte' 1898 e-rara (de), Storms 'Estudio de la Fusion en Frio' lenr-canr (es), Cunha ether-geometry base-12 (pt), Padligur radiesthetic bore-point report (de), legitim.ch Epstein-files cold-fusion piece (de), MHI ISS centrifuge facility (ja), yesilhaber LENR (tr), TU Delft dowsing-scientist (nl), Tesla FBI patents clubcurioso (es), PRIO/ENG8 industrial heat (pt), Benda psychotronics (it), CVUT/VSCHT psychoenergetic lab cs.wikipedia (cs), Lu Zuyin / Yan Xin Tsinghua external-qi (zh), Iberian regenerative-agriculture soil & water (es), Emoto water-memory eprudnik (pl).
- **+8 persons**: kaznacheev, trofimov, edmond-storms, wilhelm-grosse, renato-cunha, reiner-padligur, lu-zuyin, yan-xin. Linked sheldrake, benda, tesla, masaru-emoto to the new works (by-or-about convention); deduped 3 persons' works_in_collection (tesla had a doubled entry).
- Source URLs verified 18/18 live (200/206).
- synthesis_index.json absent from repo (builder script present, artifact not published) — standing staleness check no longer applicable; noted, not regenerated.
- Index sizes: 565 works, 453 persons. Contents-API pushes: 07e34bd0d (research-index), 8ff25aad7 (person-index). Collision re-check armed ~08:35 UTC.


## 2026-10-08T16:06:00Z — aetherforce-translation-qc (16:00 UTC)
- Standing checks clean: same-file dupes 0, unknown dates 0, junk ids 0, dangling cross-refs 0, dangling person work-refs 0, feed mojibake 0, feed same-file dupes 0, containment 0. Title-similarity: 4 candidates, 0 folds — Sitkowski od-podstaw vs mentalna (distinct books, known), geometria-sacra en/it and belizal-morel fr-en/fr pairs already cross-linked, **morphic-fields sheldrake pl (09-18) vs pl-en (09-20) pair cross-linked this run** (belizal/geometria-sacra precedent: same source, distinct-language renderings, containment unprovable with translations/ retired).
- **+32 works** — Forge's 2026-10-08 batch (in feed, not DB), 16 languages: Keely ether-generator inventor Biosfera Klub (sk — feed language empty, set Slovak from 'vynalezca' orthography), Schauberger Strahlturbine Austrian patent AT 117749 B rexresearch (de), Drbal pyramid razor-blade patent 91304 account (cs), Farghaly et al. radiesthesia sewing-worker ergonomics Int. Design Journal 2021 (ar), Sheldrake morphic-resonance interview Revista Fenix (pt), Memoire de l'eau fr.wikipedia (fr), Unruh-effect detection via Josephson ring Hiroshima U. Nazology (ja), qigong-as-information-tuning Sanwa (ja), plasma-cosmology series x2 quietsphere (ja), LENR news x4 (Forbes Japan hydrogen heater ja, Cool Fusion neutron/gamma PR Times ja, HYLENR pre-Series-A ko, Ekubo Tesla wireless-power demo ja), KAIST electric-double-layer (ko), torsion x6 (KPI metallographic SPS uk, uk.wikipedia torsion-field uk, scalarwave M.I.N.D device zh, scalarwave nonlocal transmission zh, scalarwave torsion-in-Japan zh, oborud DIY generator schematics ru, klimatyzacja.pl refrigeration pl), EZ-water teija (fr), water-memory Engelhart epochtimes.cz (cs) + Saliba cartadenoticias (pt) + acqua-informata Gastaldi (it), radiesthesia fa.wikipedia (fa), VRGS RR 3/2025 Wasserader (de), pyramida psychotronika glossary (cs), WaterQi vortex WUR thesis (nl), vibrational-medicine Factnameh fact-check (fa), al-Battat ether-basis-of-creation Al-Masra (ar).
- **+7 persons**: john-keely, serge-kernbach, zainab-farghaly, haidar-abduljabbar-al-battat, william-saliba, daniel-linder, quietsphere. Linked schauberger, sheldrake, karel-drbal, tesla, benveniste (x2), pollack, masaru-emoto (by-or-about convention).
- Source URLs 30/32 verified live (200; uk.wikipedia Cyrillic URL needed percent-encoding client-side — link itself fine). **farghaly entry had EMPTY source_url — backfilled DOI 10.21608/idj.2021.205077** (resolves 302 → idj.journals.ekb.eg/article_205077.html; IDJ vol 11 no 6, pp. 225–232). oborud.ogorodguru.ru timed out from sandbox (urllib + curl) — kept, noted as unverified-timeout, not confirmed dead.
- Feed-title quality: two slug-titled feed entries (al-battat ar, unruh nazology ja) given real titles in the DB — builder DB-alignment (same source_url) will rewrite feed titles on next rebuild; no builder patch needed. Keely feed title said 'cs' but source is Slovak — DB title corrected to sk.
- Index sizes: 597 works, 460 persons. Contents-API pushes below. Collision re-check armed ~16:35 UTC.
