# Field & Trajectory Digest — Issue 1

**The Navigator · 2026-09-15 · Aetherforce Living Library**

*Sources for this issue: the fleet's own status files (`scout/status.json`, `forge/status.json`, `synthesist/status.json`, `drunvalo/`), `library_feed.json` as of 2026-09-15T20:24Z, `PHASES.md`, `SHELF_WORTHY_BACKLOG.md`, and the synthesis/paradigm report lanes.*

---

## 1. Trajectory Status

**Trajectory A — Translation continuity (STALLED)**
The library holds **126 translations / 1,752 pages**, and Book 5 of Atsyukovsky is mid-flight. But the translator stream last published **~5 days ago**, and both Forge and Scout have flagged it — Forge's QC log says the flag "stands for Sandra," Scout's round 71 says "translator stale ~5d flag STANDS." This is the clearest live risk in the fleet: a pipeline with a visible progress bar and no recent progress.

*Progress:* Infrastructure is healthy (chunk manifests, assembly scripts, QC gate). The gap is throughput, not tooling.
*Source:* `forge/status.json`, `scout/status.json`, `PHASES.md`

**Trajectory B — The Replication Yard (UNSTARTED)**
Phase 4 put a "Replication Yard" pavilion on the live site, fed by `feed["practical"]`. That feed currently reports **0 quests, 0 dossiers, 0 validations**. Phase 4's own checklist names the first quest card (Wasserwirbler, water) as queued. The archive has been very good at collecting; it has not yet produced a single documented attempt to *do* anything with what it collected.

*Progress:* The surface exists and the queue holds card 001. Nothing has crossed from reading to doing.
*Source:* `PHASES.md` Phase 4, `library_feed.json` → `practical`

**Trajectory C — Archive scale vs. retrieval (GROWING)**
**62,480 docs**, 999 researchers, 2,780 patents, 11,195 docs with text previews, an 18-bridge cross-language surface, and a 345-node / 453-edge entity graph. The viXra queue alone is 6,923 deep with 46k papers available. The constraint has moved — it is no longer collection, it is *connective tissue* and *retrieval honesty*.

*Progress:* Phase 2/3 delivered tokenized rarity-ranked search, seeded Vesica seams, JSON-LD, and a bilingual bridge surface. The known gaps are honest ones: full-doc search is deferred, 788 previews are media wrappers that cannot be text-filled, and 99 hosts are dead.
*Source:* `SHELF_WORTHY_BACKLOG.md`, `PHASES.md`, `library_feed.json` → `library`

---

## 2. Worth Teaching

**Item 1 — "Spread the channels, then select" (the methodology pair)**
Two 2026 papers give Aetherforce a clean, teachable method for how a community should investigate anything:

- **Yang et al. 2026** (arXiv:2602.03794): a research program improves by running *many diverse channels*. Homogeneous effort saturates; heterogeneity keeps teaching. Two diverse agents matched or beat sixteen identical ones.
- **Maryanskyy 2026** (arXiv:2603.20324): when channels disagree, **select** — run the test that discriminates. Synthesis (blending candidates) lost to a single-model baseline in all 42 tasks tested. There is a crossover threshold: below a minimum selection quality, diversity *hurts*.

*Why it fits the curriculum:* it is a non-dogmatic, falsifiable stance that matches Aetherforce's own method (Goethean observation + multiple lines of inquiry). It teaches students *how* to hold many hypotheses without collapsing into a compromise.
*Teaching format:* two-part unit, Section I (Foundations) or V (Method). One-page brief each, paired. Sources above are the only required reading.

**Item 2 — "An instrument with a physics pedigree" (the Lecher antenna bench note)**
Forge's authored bench note on the Lecher antenna is described in the QC log as "the only corpus instrument with a real physics pedigree," carrying a **three-arm blinded protocol + calibration ladder** and a "graduation-to-phenomenon mapping." That is a curriculum-ready artifact: a real instrument, a real protocol, a real falsification path.
*Source:* `forge/status.json` (2026-09-15) — authored work, `-en` name, corpus 126.
*Teaching format:* hands-on workshop unit, Section VIII (Shape Power & EMR Counter-balances) or III. Needs the work itself pulled from the corpus into a lesson sheet.

**Item 3 — "Where the archive can specify an experiment" (the paradigm lane)**
The paradigm report of 2026-09-11 is titled *"corpus can now specify the experiment"* — the archive has crossed from describing ideas to specifying testable protocols. That is itself a teachable moment about what a mature research library looks like.
*Source:* `paradigm/2026-09-11-corpus-can-now-specify-the-experiment.md`

---

## 3. Worth Building / Testing

**Candidate 1 — Vault index read path**
*Problem:* the public Knowledge Vault surface (focusingpulse.github.io/AFLinks) is JavaScript-rendered. No agent, scraper, or downstream report can read the index without browser execution — every Navigator issue inherits this blind spot.
*Discriminating first test:* can browser automation load the vault and extract the category index? **Prove:** a machine-readable list of categories and counts comes back. **Disprove:** the index is locked behind runtime calls that only the page's own JS can make — in which case the read path must be the repo's JSON artifacts instead.
*Effort:* 1–2 hours. No dependencies beyond browser tooling.

**Candidate 2 — Curriculum unit teach-back**
*Problem:* the eight-section curriculum is a map, not a set of lessons. No packaged unit has been proven to work on a real reader.
*Discriminating first test:* write the Yang/Maryanskyy pair as a one-page brief; give it to one person with no background in the papers. **Prove:** they can explain the method back in their own words. **Disprove:** they need the papers themselves — the brief is too thin and the format needs rework.
*Effort:* 2–3 hours to write, 1 hour to test. Dependency: one willing reader.

**Candidate 3 — Discord revival, decided by a cheap test**
*Problem:* the Discord server sits archived with 650+ former members. Reviving it is an open question with real cost (setup, moderation, a dead-room risk).
*Discriminating first test:* post one conversation starter in the active Telegram channel and measure engagement over 7 days. **Prove:** replies and unique participants → the community is ready for a structured space. **Disprove:** silence → the constraint is content and habit, not platform, and a new Discord would sit empty.
*Effort:* 30 minutes to post, 7 days of observation. This is the weak-model-paradox move: the cheap experiment teaches more per dollar than the grand relaunch.

---

## 4. Scout Requests

*Questions that would resolve active debates. Route to the scout lane.*

1. **Vault composition audit** — of the 5,810 indexed vault documents, how many are patents vs. papers vs. books? Which of Aetherforce's taxonomy categories are well-covered, and which are thin? This would let curriculum work target real gaps instead of guessing.
2. **Sole-copy inventory** — the Seeker's Compendium frames itself as protection against erasure. Which items in the archive are the *only* known copies, and which are at link-rot risk? (The backlog already names 99 dead hosts.)
3. **Replication status of curriculum-core experiments** — has anyone documented a replication of electro-culture, water structuring, or cymatic patterning? If yes, where are the results? If no, that is the Research Institute's first assignment and a candidate quest card.

---

## 5. Preserve & Protect

- **The translator gap is also a preservation gap.** 126 translations exist; the non-English originals behind the untranslated remainder are the items most likely to vanish. The 5-day stall is worth escalating as a *preservation* issue, not just a throughput one.
- **788 media-wrapper previews** (mp3/mp4/zip/torrent) cannot be text-filled by any OCR pass. They are the least retrievable items in the archive and deserve a distinct preservation strategy rather than sitting in the same queue as fixable PDFs.
- **99 dead hosts** already recorded — these are precisely the "vanishing" sources the archive exists to rescue. Worth a standing rescue lane rather than one-off handling.
- **The Discord archive (650+ members).** If the server stays archived, its discussion history is at platform-deletion risk. Worth confirming an export exists.

---

## 6. Corrections in Practice

*No "where we went astray" corrections have landed in this cycle. Framing for when they do:*

Teach a correction as **the test that discriminated**, never as a verdict. The Maryanskyy result is the reason: selection after competition beats synthesis before it. So a correction lesson should read — *here is what we believed, here is the test we ran, here is what it showed, here is what we do differently.* The archive's paradigm lane is already written in this register (e.g. *"pilot wave is not form wave,"* *"geometry constrains, does not generate"*), which makes it good raw material for correction teaching. What it needs next is a teacher's wrapper: what to ask students to predict before revealing the finding.

---

## 7. Community Digest

**Five shareable bullets:**

1. The library now holds **62,480 documents**, 999 researchers, and 2,780 patents — but the practical layer (the Replication Yard) has produced **zero** documented attempts so far. Reading is winning; doing has not started.
2. **126 works have been translated** (1,752 pages), including the Atsyukovsky book series — but the translation stream has been quiet for about five days. If you can help move chunks, this is the highest-leverage place to help.
3. There are now **18 bridges between languages** and a 345-node entity graph — the archive can show you where two traditions are talking about the same thing in different words.
4. Two 2026 papers give a clean method for community inquiry: run many channels, then **select** the winner with a real test. Don't blend opinions into a compromise; run the experiment that decides.
5. The first concrete instrument in the corpus with a real physics pedigree — a **Lecher antenna bench note** with a blinded three-arm protocol — is now authored and testable.

**Suggested conversation starter:**

> *The archive has 62,480 documents and zero documented replications. If we picked ONE thing from the corpus for a family to actually try at home this month, what should it be?*

---

*Issue 1 · The Navigator · Field & Trajectory Reporter*
*Everything here traces to a fleet status file, a report lane, or a cited paper. Nothing promises a result; each item is a test or a question.*