---
description: Progress report on the 10 blind-spot items (2026-09-14). Shared by Drunvalo to coordinate with the full fleet.
date: 2026-09-14
---

# Blind-Spots Progress Report — 2026-09-14

## Context
Chris surfaced a 10-item blind-spots list in the aetherforce chat. This file tracks status across all items and is the shared reference for cross-agent coordination.

---

## Items

| # | Item | Owner | Status | Notes |
|---|------|-------|--------|-------|
| 1 | Reactive QC — duplicates regrowing | Drunvalo | ✅ Done | `scripts/qc_pass.py` built; runs dedup, citation coverage, orphan refs, formatting drift. First run caught 1 real duplicate (PADRAK disclaimer, id 1499071). Clean since. |
| 2 | Index integrity beyond raw count | Drunvalo | ✅ Done | qc_pass.py checks shards for checksum validity, duplicate full-text (md5), orphaned person/translation refs |
| 3 | Large-file handling at scale | Drunvalo | ✅ Done | Radiesthesia batch 1: 59 unique PDFs (355MB) merged from Proton Drive share. Radiesthesia batch 2 (9 more folders, ~3.6GB) downloading and merging today. |
| 4 | Clickable `[1]` citations → source path | Open | ⬜ Todo | Citations currently print `[1] [https://...](...)` after each quote; needs sync across agents who emit citations |
| 5 | Unified fleet dashboard | Open | ⬜ Todo | family ledger lives on another account; needs cross-account aggregation story |
| 6 | Translation QC (unbiased reviewer) | Agent-75b8d29e? | ⬜ Todo | Reviewer agent or independent tool run per batch |
| 7 | Synthesis discoverability/tags | Drunvalo | ⬜ Todo | Tag synthesis outputs with concepts → link from person/research pages → searchable |
| 8 | Per-cycle quota tracking in status.json | Drunvalo | ⬜ Todo | Track credits consumed per cron cycle; no alerts, just bookkeeping |
| 9 | Cross-language concept formation mapping | Open | ⬜ Todo | Concepts form differently per language; map before translation to avoid loss |
| 10 | Provenance chain — checksums at each stage | Open | ⬜ Todo | Source → translation → synthesis → index → feed. Checksum at one step makes the chain auditable |

---

## Completed Work This Cycle

### 1. QC pass (`scripts/qc_pass.py`)
- Detects duplicates via md5 of stripped frontmatter + normalized whitespace
- Checks all `## N. Sources` numbered headers (bullet-list and blockquote refs)
- Checks orphaned `person-index.json` entries vs translation file references
- Catches formatting drift (missing translations under non-English quotes)

### 2. Radiesthesia archive — batch 1
- Source: Proton Drive share from Chris (E2E encrypted, fragment-key in URL)
- 9 folders extracted → 72 PDFs → md5-deduped → **59 unique (355MB)**
- Stored at: `books/radiesthesia/<author-slug>/`
- Provenance string: `"proton-drive-share-Physical-Radiesthesia (via Chris, 2026-09-14)"`
- Added `radiesthesia_books` (59 entries w/ md5, size, provenance) to `library_feed.json`
- Commit: `60cb3ba3d` — `radiesthesia archive: 59 source PDFs from Proton Drive share`

### 3. Synthesis English glosses
- All 5 synthesis files updated: blockquote translation pattern was already correct; added English glosses to **inline** French titles/phrases
- Files: instrumentation-of-the-invisible, french-form-wave-lineage, negative-green-carrier-thread, scalar-wave-convergence, geometric-foundations

---

## In Progress
- **Radiesthesia batch 2**: 9 remaining folders downloading (Christopher Hills – Supersensonics ~812MB, Dowsing Rod Science, Enel, Ibrahim Karim 176MB, Jacques Ravatin 661MB, Limited Design Technology 566MB, **Louis Turenne 1.5GB**, Misc Literature 377MB, Radiesthesia Images 284MB)
- Once complete: extract → md5-dedup → add to `books/radiesthesia/` → `radiesthesia_books` feed → commit & push

---

## Open Work (by item)
- **[4] Clickable citations**: Synthesis reports use `[1]` `[https://...](...)`. Other agents (especially source/translation emitters) should adopt the same pattern.
- **[5] Fleet dashboard**: Family ledger on other account. Options: (a) cross-account API integration, (b) shared repo ledger kept fresh by each agent, (c) lightweight HTTP endpoint from each agent's sandbox.
- **[6] Translation QC**: Reviewer agent (agent-75b8d29e) or separate QC run per batch. Goal: verify source fidelity, frontmatter completeness, and encoding before emit.
- **[7] Synthesis discoverability**: Open question — should the synthesis tag generator call `tag_concepts.py` on each emit? Also link synthesis from each person page and research concept page.
- **[8] Quota tracking**: Add `quota_consumed` to `status.json` per run. No alerts — just for bookkeeping and fallforward planning.
- **[9] Cross-language concepts**: Before translating, map concept keywords per language (e.g., "ondes de forme" ≠ "shape waves" ≠ "form waves"). Prevents missed conceptual links.
- **[10] Provenance chain**: Each stage writes checksums to `provenance.json`. Chain: srce_checksum → tl_checksum → syn_checksum → idx_entry → feed_entry. Audits show when a document was mutated where.

---

## How to contribute
This file is at `drunvalo/blind-spots-progress-2026-09-14.md`. Update whichever section you're working on, keep the table current as the shared source of truth.
