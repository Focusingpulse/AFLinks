# AFLinks Phase Roadmap — from the 2026-09-06 architecture debate

Source of truth for the phased build-out. Updates to this file should mirror
decisions in `living-library/synthesis/2026-09-06-architecture-debate-dossier.md`.

## Phase 1 — Data contract + phone wins ✅ (2026-09-06, committed b450cc5)

- [x] **Entity graph contract** — `archive-graph.json` (nodes: person/work/translation/concept; typed edges: authored_by, domain, translated, mentions, language; 453 edges). Conservative linking — exact url/title only, no fabricated edges.
- [x] **Curated-core bindings** — `living-library/database/curated-core-bindings.json` (62 bindings: work → persons/concepts/language/translations), fills the empty seam.
- [x] **Chunked phone search** — `search_chunks/<slug>.json` per meta-category (25 chunks) + `search_manifest.json`. `index.html?cat=X` deep links fetch only that chunk (16KB–4.7MB) instead of the 18MB full index. Default "search all" keeps full index; hero count honest from feed.
- [x] **Pattern-signal news** — paradigm-signal reports now appear in the What's New strip (wire existed, builder never emitted them).
- [x] **Key Dial verdicts** — "unexplored vein" badge when a paradigm lane spans many fields but the archive holds a thin slice of Aetherforce's output.

## Phase 2 — Pattern machinery (this month)

- [ ] **Wrong-Turn Death Certificates** — claim/status(died|suppressed|continued)/cause/late-confirmation per primary source. Priority: Epstein/Pons/LENR, Schauberger 1951 patent, Magnitsky.
- [ ] **Contradiction pass** — CONTRADICTS edges with quote + confidence on the testable cluster (Toulgoat ↔ TUO ↔ Besson).
- [ ] **Tokenized rarity-ranked search** — replace substring scan; rare cross-category co-occurrence ranking ("gravitational shielding × plasma" surfaces because the pair is rare). Also makes the DEFAULT search payload lean (drop the 18MB fetch).
- [ ] **Seeded Vesica** — "brightest seams" prefill from `connections.shared`.
- [ ] **Retrieval-grounding rules** — canonical `@id` + quote-citation contract in the feed so synthesists stop hallucinating archive contents.

## Phase 3 — This quarter

- [ ] **Re-try-now tags** — modern apparatus (micro-PIV, GPU CFD, nano-calorimetry) for died-untested claims.
- [ ] **JSON-LD headers** — schema.org ScholarlyArticle/Person per doc page (ingestible by external agents).
- [ ] **Bilingual bridge search surface** — translations frontmatter as the multilingual retrieval layer.
- [ ] **Curated-only tiny embeddings** (~150 works, <0.2MB uint8) — semantic recall on the gems, not the noise.
- [ ] **Timeline view** — only if a cheap date field materializes.

## Kill / defer hard

- Backend API / Postgres / vector DB — a moving existential dependency on a $0 static budget.
- Full 15k client-side embeddings — 23.6MB float32 is a phone killer.
- D3 force graph at archive scale — the microscope (≤30-node ego-graph) replaces it.
- Continuous full-corpus NLP entity extraction — the fleet already reads every doc with better judgment.