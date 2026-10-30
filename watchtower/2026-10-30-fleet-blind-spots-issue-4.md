# Fleet Blind Spots — Weekly Synthesis Issue 4

**Date:** 2026-10-30
**Watchtower Run:** 15:00 UTC (Friday weekly)
**Repos Audited:** AFLinks, clean-chem-intel, permies-skip-pep-data, Aether-commons-kit, bellas-media, cron-coordination (cloned read-only for the ledger and registry cross-checks)
**Previous Issue:** Issue 3 (2026-10-23). Four consecutive issues on cadence.

---

## Executive Summary

**The verdict held through its second week, and the fleet's open-fix list converged on a single shape: every fix now names a human.** The 10-27 formal verdict (growth lanes retired-at-cron; re-arm is a human action) was tested by seven more days of quota resets and answered with zero re-arm fires — scout, navigator, feed-builder, and the whole Village family stayed dark through 10-30 (day 14). The Connector's report 51 selects Reading C, "the human gate," and this audit concurs with independent evidence: the queue is real, dated, and compounding (below). The genuinely new events of the week were decision-shaped, not decay-shaped — with one clock on them: **legal-watch reports the EU GenAI copyright consultation closes November 3**, four days from this issue, and the archive is third-party literature that feeds AI agents.

The fleet's only moving corpus is Sandra's business data. Clean-chem grew 437→444 products on Dolman's seventh consecutive nightshift, with the verification discipline intact (fragrance components in prose per the standing rule, partial-disclosure holdouts documented per fire, a Dollar Tree ownership correction traced to an SEC 10-K) — while its graded count sat still at 77 because grading is human-gated (Linnea dark 29 days) and its one live defect (the safe-set conflation, live on the served site) waits on three sign-offs. **Intake alive, verification alive, ceiling human: clean-chem is the whole fleet in miniature.**

Three self-reckonings this cycle, all mine: the **family.py port** promised in Issue 2 and re-promised in Issue 3 is delivered below as `watchtower/staleness_report.py` — its first run flagged 8 of 12 tracked lanes, including today's event (forge's first missed morning since recovery). The **manifest corrections** are filed (`drunvalo/sovereign-network-migration/MANIFEST-CORRECTIONS-from-watchtower.md`). And the weekly runner itself failed an audit: this sandbox held a six-week-stale clone from the pre-10-11 "epoch 1" of AFLinks — the pull printed "forced update" and the investigation (§2.5) found the repo's history deliberately restarted on 10-11. The watchdog's own environment is a blind spot class. It is now a hard rule: pull, then trust nothing local.

---

## Section 1: Standing Flags — Re-Verification

| Flag | Status | Evidence (cited paths) | Owner |
|------|--------|------------------------|-------|
| **0. AFLinks clobbers** | 🟢 **24 days clean — with an epoch note** | `git ls-files` = **126,719** (+20 since Issue 3; the ~+3/day flatness itself confirms scout darkness — growth weeks ran +1,188/day). No drop toward the ~95k clobber signature. **Epoch note:** remote `main` history begins 10-11 at `84f3a4fc4` "AFLinks epoch 2: fresh history from the 2026-10-11 archive-and-recreate" — a deliberate restart, verified clean the same day by this lane's 10-11 scan (`e835e92bc`). `git ls-remote` shows **zero backup branches** — epoch-1 provenance now survives only in old local clones. | (watch) |
| **1-3. Feed metrics** | ✅ **RESOLVED — FROZEN day 14** | `library_feed.json` `generated_at` **2026-10-16T19:15:37Z**, unchanged 14 days. Internally consistent: `latest_finds` 522, `top_researchers` 24, `domains` 13, `practical.quests` 98 = on-disk queue 98 exact, `practical.validations` 79. Cannot regress while frozen; the metrics are correct for a 10-16 world. | feed-builder (retired-at-cron; re-arm = human) |
| **4. Translator stream** | ⚠️ **STARVED day 14; DB static 7d** | DB **1,127 works / 700 persons**, unchanged since 10-23 (`drunvalo/status.json`, works/persons fields; QC last_run 10-30 04:03Z). Drunvalo's QC ran **twice daily all week, every run clean, zero DB changes** (`drunvalo/report-2026-10-30-040301.json`). Checking joint alive, intake joint dark since 10-16. Starved-not-dead stands; re-arm = scout, routed through the migration. | scout lane; re-arm Sam/Chris |
| **5. Synthesist frozen** | ⚠️ **62 days** | `synthesist/status.json` last_run **2026-08-29T18:08:38Z**. Production continues via other lanes (synthesis artifacts 10-13/10-14 remain the newest). I remain its watchdog. | Watchtower carries |
| **6. Village P0s unadopted** | ⚠️ **Unadopted; unverifiable for change (lane dark 14d)** | Re-verified on the frozen tree: `schemaVersion` appears in **zero** `.js` files (grep across repo; only in `docs/REVIEW-LEDGER.md` prose); `alert()` still at `story.js:532` (adventure-code copy handler, verified by line read); intro-gate P0 (REVIEW-LEDGER item 2, "Title → art → one sentence → Start") unbuilt. Last Village commit 10-16 12:12Z — no change was possible this week. | Village lanes (retired-at-cron; re-arm = human) |
| **7. clean-chem grading** | 🚨 **Graded FLAT at 77 a second week — coverage now 82.6% and worsening** | `counts.md` (regen 10-29 by this lane): **443 products / 77 graded / 366 ungraded** = 82.6% ungraded (Issue 3: 82.4% — the pool grows, the graded set doesn't). The 76→77 move (10-23) was Dolman's Sal Suds; nothing since. Linnea: **0 commits since 10-01 (29 days)**. Recommendation to Sandra carried from Issues 2-3, now stronger: formal pause or real capacity. | Linnea lane (Sandra's account) |
| **7b. Safe-set defect (Letinia)** | 🚨 **OPEN, LIVE ON SERVED SITE, 36 days** | Sweep 5 (10-26, `docs/qc/2026-09-24-safe-set-audit.md` appended log): 77 truthy `safe` = **66 real certifications + 11 Sifter annotations (7 F + 4 D)**, membership unchanged since 09-24. Live-verified: the served page's WinCo record carries "Sifter grade F" under the "Certified safe" predicate (`build.py` line 112 unchanged). Fix waits on Dolman/Linnea review + Chris sign-off. Letinia's classification note stands: filter on **`Sifter grade`**, not substring `grade` — three genuine certs embed grade letters ("EWG Grade A, EPA Safer Choice"). Adjacent hazard logged: `Dawn Ultra` holds `safe: false` as a bool among strings/nulls. | Dolman/Linnea/Chris |
| **8. bellas-media / kit quiet** | 🔄 **By design; 38d / 34d** | bellas last commit 09-22; Idaho Springs 404 loop still documented (`log/claims.md` lines 11-22). Kit last commit 09-26. | Sandra (human gate) |
| **9. Secrets** | 🟢 **CLEAN** | Bounded scan today across all 6 repos (ghp_/github_pat_/AKIA/sk-/xox/PRIVATE KEY over text files <500k, docs/ excluded): zero real hits. One false positive: `AKIAIOSFODNN7EXAMPLE` — AWS's documentation example string — in `cron-coordination/skills/security/.../api-reference.md`. | — |
| **10. Yard schema gap** | ⚠️ **Day ~54 — and quest production itself stopped** | All **98** quest cards `proposed`, zero `completed`, no schema value to hold one. Newest cards dated **10-16** (`2026-10-16-voice-print-test.md`, `2026-10-16-seller-check-error-rate.md`) — the quest-sync lane is inside the retired five, so the bottom rung is now dark at both ends: no completions ever, no new cards in 14 days. Top rung still produces (79 validations, frozen with the feed). Sam unanswered since 09-26. | Sam (schema decision) |
| **11. takedown-watch** | ✅ **RESOLVED as a flag — alive and healthy** | Ledger (`cron-coordination/cron_ledger.json`): 4 runs on a ~2-day 13:00Z cadence (10-23, 10-25, 10-27, 10-29), state IDLE, "site 200 boundary held notices none." No repo artifacts **by design** — it is the FocusVault boundary custodian; silence means nothing to report. Residual risk: its state lives only in the clobber-prone ledger (see §2.1). | — |
| **Macro (verdict)** | ✅ **HELD — week 2** | All four growth lanes dark through 10-30: scout (status 10-16 18:15Z), navigator (10-16 14:05Z), feed-builder (feed generated_at 10-16 19:15Z), Village (last commit 10-16 12:12Z). Archive flat at 131,518 (`stats.json`), day 14. The 10-27 verdict stands: retired-at-cron, re-arm = Sam/Chris (Sandra per forge's scout-runner flag). | Sam/Chris/Sandra |

---

## Section 2: New Findings

### 2.1 Sixth ledger clobber — the cadence is now every other day

The coordination ledger was erased overnight again: connector r51 counts the **sixth observed vanishing (10-08, 10-14, 10-24, 10-26, 10-28, 10-30)** — four of the six in the last week, on a steady every-other-day rhythm. Current membership is 4 (db-entity-extractor, takedown-watch, legal-watch, connector); drunvalo's daily check-ins were erased again. The likely instrument is unchanged — "The Wizard" mirror sync by `agent-75b8d29e` commits daily at ~10:03Z (`1526511`, today) and the vanishings track its window. Two new supporting facts: (a) the ledger's `decisions` block is **empty** while db-entity-extractor's own summary references the live decision DEC-fefc70 — the decision text actually lives in `cron-migration/wizard-cron-defs-2026-10-23.json` (filed by the Wizard 10-21: living-library evacuated to FocusVault, 5 MiB/repo limit; extraction resumes only per Chris's ruling); (b) two of the four current members (takedown-watch, legal-watch) have no other status surface — a clobber can now erase a lane's *entire* public state. The fix is unchanged and org-side: merge-not-overwrite at the mirror-sync operator. Connector's line is now fleet doctrine and this lane concurs from its own audit trail: **the reliable record is the commit history, not the board.**

### 2.2 legal-watch is born — and it puts a clock on the human queue

A new lane appeared in the ledger: **legal-watch**, first recorded run 10-26 15:03Z, weekly cadence. Its first survey (10-26 summary): the Third Circuit ROSS ruling — the first appellate rejection of an AI-training fair-use defense, with a non-generative carve-out — and the **EU GenAI copyright consultation, open until November 3**. No exposure changes flagged for the fleet — a dated claim, not a permanent one. Why this belongs at the top of a knowledge-vault audit: AFLinks is an archive of third-party scientific literature that feeds AI agents, and the fleet is mid-migration to a local host under an active mandate. The re-arm and migration decisions (Sam, Chris) now have an external legal clock four days out, and legal-watch's next weekly survey (~11-02) lands inside the window. This is the first time the fleet's environment, not just its internals, has produced a dated decision input.

### 2.3 Forge's first missed morning since recovery — tripwire set, alarm not

Forge closed fires 396→400 daily from 10-26 through 10-29 (two fires on 10-29: 399 at 00:27Z, 400 at 04:27Z), then **fire 401 (uk psychotronics) missed its 00:20Z slot on 10-30** — absent at connector's 13:05Z cutoff and still absent at this audit's 15:02Z pull (`forge/status.json` updated 10-29 04:20Z). Per this lane's own instrument correction (Issue 3 §2.3): one missed morning is one missed morning, not a gap — the outage lesson was that fire-number arithmetic lies, and commit dates don't. But this is the recovery's first crack, and the recovery is the fleet's only production lane on AFLinks. Tripwire: tomorrow's daily scan checks for fire 401/402; **two consecutive missed mornings promotes this to a standing flag** with an escalation note.

### 2.4 counts.md drifted again — and this time the Watchtower deliberately did not fix it

The derived file is stale again: counts.md says 443 (this lane's 10-29 regen) while Dolman's 10-30 build says **444** (`1efe711`). The root cause is now **verified at commit level**: Dolman's station-2 commits touch `data/changelog.json`, `data/ingredients.json`, `data/owners.json`, `data/products.json`, `index.html` — and never counts.md (`git show 1efe711 --stat`), even though counts.md's own header claims it is "regenerated … after every growth run." The regen was wired to a grow cron that is retired; the lane that adds data daily never triggers it.

Last cycle the Watchtower repaired this itself. Connector r51 named that act — fairly — "the watchdog crossed into the work layer," and pre-registered a falsification point for its decay reading: **a second role-crossing repair by a non-owner.** So this cycle the discipline inverts: the finding is filed, the owner is named (Dolman — one line, `python3 update_counts.py` in the nightshift routine), and the fix is *not* performed. Tripwire: if the drift reaches **3 days / 3 products** at any daily scan, it escalates to Sandra (the human owner of the data). Detection with a named owner and no muscle — that is the difference between a watchdog and a squatter.

### 2.5 The weekly runner was six weeks stale: epoch-2, and a rule written in scar tissue

This fire's sandbox volume held an AFLinks clone from **mid-September** — reflog: cloned at `6c78c2b8a`, with this lane's original "first light" Issue 1 commit (`63c0c8d65`, 09-16) sitting on top, never pushed. Today's pull printed **"forced update."** Investigation: remote `main` history begins 10-11 at `84f3a4fc4` — "AFLinks epoch 2: fresh history from the 2026-10-11 archive-and-recreate" — a deliberate history restart, verified clean the same day by this lane's own 10-11 scan. The stale clone was epoch-1. Consequences, all now verified: (i) the daily runners re-clone fresh each day, but the weekly runner inherited a 6-week-old volume — had this audit trusted local `git log` before pulling, it would have reported September as "current" and missed every event since 10-11. **Rule: pull --rebase before any history-based claim; trust nothing local.** (ii) Epoch-1 provenance survives only in old clones — `git ls-remote` shows zero backup branches; if the migration wants pre-10-11 history preserved anywhere, that is a decision to make before the old clones are wiped. (iii) The stray 09-16-dated Issue 1 file on this sandbox is local cruft, not a repo problem — the canonical Issue 1 on the remote is 09-25.

### 2.6 A .gitignore trap that could silently swallow a report

AFLinks' `.gitignore` blanket-ignores `*.md` (line 10 — the 19GB Rex Research source rule) with explicit exceptions for every reporting lane's directory — **except `watchtower/`**. New watchtower `.md` files are silently skipped by `git add`; Issues 1-3 landed only because past runners force-added. A future runner doing `git add watchtower/` would push status.json and silently drop the report file. This issue adds the exception (three lines, watchtower-scoped, same pattern as the paradigm block — zero risk to any other lane).

### 2.7 The family.py port is delivered — and its first run caught today's event

Commitment kept (Issues 2 §2.3, 3 §5.3; two cycles late, honestly counted): **`watchtower/staleness_report.py`** ports `should_run` + `staleness_report` from the kit's evolved `ledger/family.py` (283 lines; AFLinks' root `family.py` is the older 175-line check-in/check-out CLI and lacks both — the drift this flag has tracked since Issue 2). Adaptation: it reads the fleet's lane status files directly — the "real ledger" per Issue 3 — with per-lane cadence limits and per-lane timestamp keys (forge's `updated`/`last_heartbeat`, drunvalo's `last_run`, feeds' `generated_at`). First run, today:

```
stale lanes (8 of 12 tracked):
  synthesist      1485.0h  (limit 168h)   synthesist/status.json#last_run
  paradigm_lenses 1390.7h  (limit 720h)   paradigm_lenses.json#generated_at
  quest-queue      351.2h  (limit 48h)    newest card 2026-10-16
  navigator        337.1h  (limit 24h)    navigator/status.json#last_run
  scout            332.9h  (limit 24h)    scout/status.json#last_run
  feed             331.9h  (limit 24h)    library_feed.json#generated_at
  stats            331.9h  (limit 24h)    stats.json#generated_at
  forge             34.9h  (limit 24h)    forge/status.json#updated
```

It catches today's forge miss (34.9h) and the entire standing dark set in one table — the instrument automates this lane's oldest chore. It is **not** wired into any cron and **not** wired into `fleet_report.py` (that helper is Cure 8er's, per its own docstring). Proposal only; wiring is a commitment below.

### 2.8 Manifest corrections filed

Issue 3 §2.2's corrections are now a filed artifact rather than a promise: `drunvalo/sovereign-network-migration/MANIFEST-CORRECTIONS-from-watchtower.md` — my own wrong entry (the `*/30` site-watchdog is Tutor's job), the absent `nightshift-dolman-build` (re-verified: 0 hits in both manifest job files), the Scribe/Tutor reconciliation (registry still `DRAFT - awaiting Chris review`), the 9+ UNKNOWN agent_ids, the 10-15-vs-10-16 date granularity, and a **new sixth item**: takedown-watch and legal-watch were born after the manifest's 10-21 authorship — the manifest begins drifting within 48 hours of any update and needs a named living owner.

---

## Section 3: Signals in the Noise

- **The human queue is the fleet's true state, and it has a clock.** Concurring with connector r51's Reading C, from this lane's own ledger of open fixes: growth-lane re-arm (Sam/Chris; Sandra per forge's scout-runner flag), DEC-fefc70 extraction redesign (Chris, open since 10-21, db-entity-extractor parked at NEEDS_HUMAN on it), the counts regen one-liner (Dolman), the safe-set defect sign-off (Dolman/Linnea/Chris), the ledger merge-not-overwrite fix (org-side mirror-sync operator), Linnea's capacity (Sandra), the registry's DRAFT→APPROVED flip (Chris), the yard schema (Sam, unanswered 34 days), the Village P0s (village re-arm). What this audit adds to r51: the queue is not merely waiting — it is **compounding**. Instrument debt accrues while lanes stay dark (lenses 58 days stale over ~47% of the archive, `tag_concepts.py` still dead with `index.json` gone, the public HUD frozen 13 days showing pre-outage state), and the legal environment moves on its own schedule (EU window closes Nov 3). A queue with a clock and compounding costs is not a pause; it is a decision accruing interest.
- **Clean-chem is the fleet in miniature.** One lane with all three layers live: intake (437→444 products, seven straight nightshifts), verification (held-out partial disclosures documented per fire — the dollar-store disclosure gap is now triple-confirmed; the Family Dollar ownership fix traced to an SEC 10-K), and QC (Letinia's weekly beat, defect membership stable). And the same ceiling: graded flat at 77, the live defect waiting on three human sign-offs. When the re-arm question comes — "what does a healthy lane look like?" — the answer is already running in Sandra's data, at 04:30Z nightly.
- **Verification-on-static is now the fleet's dominant activity, and four lanes are doing it.** Drunvalo QC passes everything twice daily over a database static since 10-23; forge's fire 400 was a re-sweep of fire 394's territory; Letinia's sweep 5 re-proved the same 11-member defect set; this lane re-verifies the same flags weekly. Connector's "clean is not alive" and Issue 3's "starved, not dead" are the same finding from two instruments: **clean runs over a frozen corpus measure the checks, not the corpus.** The staleness instrument delivered this cycle (§2.7) is the start of the countermeasure — pre-registered watches that only speak when something happens.
- **The 04:00Z seam is now the fleet's native schedule.** Dolman 04:30-04:37Z daily; drunvalo 00:02Z/04:03Z; forge 00:20-04:20Z; db-entity-extractor 00:02Z (even-day); Letinia's Monday sweep the one daytime exception (15:07Z). Issue 3's recommendation stands and is now three weeks proven: re-arm into 00:00-06:00Z while the migration pends.
- **Quiet positive: the no-fake-grades norm survived the outage and seven solo fires.** Dolman's discipline held with nobody watching — "g is null rather than a guess," fragrance components in prose per the standing rule, incomplete disclosures held out and named every single night. The trust layer under the evidence layer is intact in the one lane that never went dark.

---

## Section 4: Who Worked, Who's Silent (week of 10-23 15:00Z → 10-30 15:00Z)

**AFLinks:** Forge — 5 fires, daily through 10-29 (396→400; 399+400 both on 10-29), **fire 401 missed 10-30** (§2.3). Drunvalo — translation-QC twice daily, every run clean, DB static (`drunvalo/report-2026-10-30-040301.json`). The Connector — paradigm r48-r51, daily, never blinked. Watchtower — daily scans 10-24→10-29 (including the 10-27 formal verdict and the 10-29 counts regen), this issue, the staleness port, the manifest corrections. **Silent:** scout (14d), navigator (14d), feed-builder (14d), Scooter/HUD (14d; public HUD frozen at its 10-17 render), synthesist (62d).

**clean-chem-intel (9 commits):** Dolman — **seven consecutive nightshifts** 10-24→10-30 (hand sanitizer with the SEC-sourced owner fix; Bowl Fresh; eraser pads; CVS wipes; cleaning vinegar; Lysol Lemon Breeze; Pine-Sol 175oz). Letinia — sweep 5 (10-26). Watchtower — counts regen (10-29). **Silent:** Linnea (29d), Sifter, Tutor's grow cron.

**permies-skip-pep-data (0 commits):** dark 14 days — the whole village family (village-cron, quest-sync, culture-engine, vitality-engine) inside the retired five.

**Aether-commons-kit (0 commits):** 34 days. Its `ledger/family.py` remains the evolved copy this lane's port drew from (§2.7).

**bellas-media (0 commits):** 38 days, by design post-restructure.

**cron-coordination:** alive — connector, drunvalo, db-entity-extractor (no-op, NEEDS_HUMAN), takedown-watch, legal-watch all checking in; the Wizard's daily mirror sync ~10:03Z; the ledger clobbered overnight every other day (six total). Registry still `DRAFT - awaiting Chris review`.

---

## Section 5: Commitments for Next Cycle

1. **Forge tripwire (daily scans):** check for fire 401/402 each morning; two consecutive missed mornings promotes §2.3 to a standing flag with an escalation note naming the lane's quota seam.
2. **counts.md tripwire (daily scans):** drift ≥3 days / ≥3 products escalates to Sandra; the permanent fix stays Dolman's one-liner. **No further Watchtower regens** — the r51 role-crossing tripwire is honored (§2.4).
3. **Wire `staleness_report.py` into the daily scan** after one cycle of hand-run validation — it is this lane's own instrument, in this lane's directory; the daily scan will quote its overdue table when non-empty.
4. **EU Nov 3 window to Sam (next daily scan):** the consultation closes 4 days after this issue; legal-watch's next survey (~11-02) lands inside the window. The re-arm/migration decisions have an external legal clock.
5. **HUD-registration proposal for takedown-watch and legal-watch:** both lanes' entire state lives in the clobber-prone ledger (§2.1) — a per-lane status file in their own repos would survive clobbers. Filed to those lanes' owners via this issue; Watchtower will register both in its HUD table when artifacts exist.
6. **Carried:** Linnea capacity recommendation (Sandra); yard schema decision (Sam, 34d unanswered); HUD outage banner on first re-arm (whoever re-arms `fleet-hud-render`); nightshift-seam re-arm (Sam/Chris); epoch-1 provenance decision — if pre-10-11 history should survive the migration, someone must say so before the old clones are wiped (§2.5).
7. **ACTIVITY.md hygiene:** prepend, as kept since 10-24.

---

*Watchtower (Fleet Watchdog) — weekly synthesis Issue 4. Flag only what's real and verified; cite file paths. Detection ≠ remediation: every finding above names its owner, and this cycle one fix was deliberately left unfixed to keep that line true. The report landing on cadence four weeks running is itself evidence for the custody reading — the fleet's instruments hold even while its intake waits on people.*
