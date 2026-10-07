---
name: Quest Card — Dowsed-Ground Bioassay
description: "Aetherforce-branded quest card testing the earth-ray claim — that places where the dowsing rod deflects are 'irradiated' and harm what lives on them. The card plants matched pairs on dowsed and control spots, blind, and pools the paired difference across households. Community domain (the community's shared ground and its siting decisions; a distributed, multi-household blinded bioassay); Earthworks mirror (earth-energy / geobiology complement)."
---

# ⚡ Aetherforce — Earthworks

**Guild:** Aetherforce — Earthworks
**Quest Line:** ⚡ Aetherforce · Earthworks complement
**Tier:** sand
**Domain:** community (shared-infra knowledge — the community's shared ground and its siting decisions; a distributed, multi-household blinded bioassay)
**Status:** proposed
**Created:** 2026-10-07

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-10-07-dowsed-ground-bioassay` · authored_at `2026-10-07` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural"],
  name: "Aetherforce — Earthworks",
  desc: "In 1955 the Royal Netherlands Academy of Sciences published the most thorough controlled test of the dowsing rod ever run — nineteen dairy sheds, an experimental apiary, potato and flax plots, and the marketed 'shielding' boxes sold to protect them. Its question was not where the rod points but whether the places it points at change anything that lives there. On the stands the dowsers called 'irradiated', the cattle were no less healthy, the bees gathered no more honey, and the crops did no worse. That test has never been run at home scale. This quest runs it: your neighbourhood dowses its own ground, plants matched pairs on the dowsed spots and on control spots, blinds who tends which, and pools the results across households. You are testing a claim about the ground, not the dowser's honesty — and a clean null is the result the 1955 study predicts. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "sand",
  quest: [
    "Dowsed-Ground Bioassay",
    "Have a dowser mark every spot on your ground where the rod deflects. For each dowsed spot, pick a matched control spot the dowser says is clean (same soil, sun and water). A referee labels each pair A and B and keeps the key sealed, so the person who plants and tends them does not know which is which. Sow the same seeds in both and record germination %, height at 14 and 28 days, and any disease. Run at least three households, open all keys only after the last measurement, and pool the paired differences. Measurable outcome: the pooled mean paired difference (dowsed minus control) in germination and height, against a zero-effect null. Target: a dowsed-spot advantage at p<0.05 that repeats in a second sowing and holds across households = the claim survives at home scale; no difference = the 1955 null reproduced.",
    ["Science", "Observation", "Community"],
    "🌱"
  ],
  source_doc: "translations/2026-10-07-onderzoek-wichelroede-landbouw-tno-nl.md — 'Onderzoek naar de betekenis der wichelroede voor de landbouw' (Investigation into the Significance of the Dowsing Rod for Agriculture), werkgroep of the Koninklijke Nederlandse Akademie van Wetenschappen (KNAW), N.V. Noord-Hollandsche Uitgevers Maatschappij, Amsterdam, 1955; source PDF https://publications.tno.nl/publication/34611974/PqzSTl/1955-onderzoek-wichelroede.pdf",
  source_url: "https://focusingpulse.github.io/AFLinks",
  dossier: "living-library/synthesis/replication/2026-10-07-dossier-071-dowsed-ground-bioassay.md",
  pass_fail: "PASS (claim survives — surprising): the pooled mean paired difference favours the dowsed spots (higher germination and/or height) at p<0.05 on a paired test, AND the direction repeats in a second sowing, AND the effect holds across at least three households | PASS (claim refuted — the expected, complete result): the pooled mean paired difference is indistinguishable from zero — the 1955 null reproduced at home scale (Skeptic's Star) | FAIL: the blinding was broken (the tender knew which spot was which), the pairs were not matched (different soil, sun or water), or the dowsed/control assignment was not made by the dowser | VOID: the dowser could not produce a repeatable reading on a present source (Phase 0), or the key was opened before the final tally — a VOID is not a FAIL",
  evidence: "Photo of the pre-registration sheet (pairs, referee, key-holder, scoring rule, thresholds) taken before planting + the dowsed-spot map the dowser drew + the pairing sheet + a photo of each pair at germination and at every measurement point + the full log (each pair's A/B identity, germination counts, heights, disease notes) for both sowings + the recorded Phase 0 detector check + the pooled paired test with its calculation shown + a one-paragraph verdict per sowing (supports / refutes / inconclusive)"
}
```

---

## Source Documentation

- **Primary (the claim and the test):** `translations/2026-10-07-onderzoek-wichelroede-landbouw-tno-nl.md` — the **full English translation** (141 chunks, complete) of *Onderzoek naar de betekenis der wichelroede voor de landbouw* (Investigation into the Significance of the Dowsing Rod for Agriculture), the report of the working group for agricultural research on the dowsing-rod problem, **Royal Netherlands Academy of Sciences (KNAW)**, N.V. Noord-Hollandsche Uitgevers Maatschappij, Amsterdam, **1955**. Source PDF: https://publications.tno.nl/publication/34611974/PqzSTl/1955-onderzoek-wichelroede.pdf (34.4 MB scanned report, digitised by TNO). It carries the full design (19 Frisian dairy sheds, three professional dowsers, an experimental apiary at Tilburg, potato-eelworm and Fusarium-wilt plots, the shielding-apparatus cases), the blinding requirement, the results, and the working group's own conclusions.
- **Scout record:** `sources/2026-10-07-scout-a-langs-2.md` § Dutch, **find 7** (`practical_applicability: flag=false` — a study; the scout records it as "a *negative primary document* — the honest counterweight to the practitioner corpus, and a model of the double-blind protocol").
- **Companion cards (dowsing, different questions):** `synthesis/quest-queue/2026-09-23-blind-water-line-location.md` (dossier 035) — one operator locates a buried hose and names its flow direction, against ground truth and a non-dowser control. `synthesis/quest-queue/2026-10-01-blind-concordance-dowsing.md` (dossier 059) — do *several* operators agree with each other, and does the agreement land on the feature? `synthesis/quest-queue/2026-09-30-water-vein-gamma-anomaly.md` (dossier 057) — is there elevated ionising radiation over a claimed water-vein band? **All three score the operator or the zone's physical signature; none asks whether the zone changes anything that lives on it.**
- **Replication Dossier:** `living-library/synthesis/replication/2026-10-07-dossier-071-dowsed-ground-bioassay.md`
- **Vault:** https://focusingpulse.github.io/AFLinks — search "radiesthesia", "water veins", "geobiology", "dowsing"
- **Aetherforce Reference:** search "radiesthesia", "water veins", or "geobiology" on https://www.aetherforce.energy

---

## Rubric Justification

| Criterion | Assessment |
|-----------|------------|
| **Practical** | YES — a named apparatus (a dowsed-spot map, matched pairs, seeds, a referee, a sealed key) with a named procedure (dowse, pair, blind, sow, measure, pool) and a measurable outcome (the pooled paired difference in germination % and height, against a zero-effect null). Not pure theory. |
| **Replicable** | YES — home, sand-cheap: ~$0–20 for seeds, two matched plots or pots per pair, labels and a log sheet. No instrument, no mains work, no chemicals. The distributed design means one household's small N is not the experiment — the neighbourhood's pooled N is. |
| **Relevant** | YES — Community domain: the ground a neighbourhood shares and the siting decisions it makes on it (where to put the beds, the coop, the barn). It complements the Earthworks guild (earth energy / geobiology) — the same object class as the guild's earth-energy grid scan (card 021) and water-vein gamma anomaly (card 057). |
| **Honest** | YES — framed as a TEST, not an endorsement. The source is itself a **negative** study, so the expected outcome is a null and a positive is presented as the surprise. The card states plainly that it tests a claim about the ground, not the dowser's honesty, and it carries the source's own blinding requirement as a hard condition. Clean FAIL and VOID paths. |
| **Linked** | YES — the source translation (with the source PDF URL), the scout record, a pre-registered replication dossier, and cross-links to the three companion dowsing cards. |

**Mirror choice, stated:** the card's **domain is community** (the rotation's next field), and its **guild complement is Earthworks** — the claim under test is the **earth-ray** (*aardstralen*) claim, a geobiology claim, and Earthworks is the queue's earth-energy / geobiology complement. Earthworks is also among the thinner relevant mirrors (3 cards), so the card does not over-weight a full complement.

---

## What makes it the queue's first of its kind

- **The first card whose endpoint is a BIOLOGICAL EFFECT of a dowsed zone.** Every prior dowsing card scores the **operator** (035: location and flow direction; 059: concordance and repeatability; 029, 034, 044, 048) or a **physical signature of the zone** (057: ionising radiation). This one scores **the ground itself** — does a spot the dowser calls "irradiated" differ from a matched control in what grows on it?
- **The first card built to be run as a distributed, multi-household replication.** The Community guild's "neighbourhood replication node" made literal: each household runs its own matched pairs, and the neighbourhood pools the result. (046, Eclipse Pendulum Watch, is the queue's other distributed card, but it is a *simultaneous* measurement of a transient event; this one is a *pooled* measurement of a standing claim.)
- **The first card to carry the source's own blinding requirement as a hard condition** — the 1955 working group wrote it into the design: *"the assessment of the results must be done by persons who are unacquainted with whether or not the objects are irradiated."*
- **The queue's second card built on a published controlled NULL result** (after 059) — and the first whose null is about a **biological** endpoint rather than a detection endpoint.

---

## The honest framing (the spine of the card)

The card tests a claim, not a person. The dowser is not being asked to prove honesty — they are being asked to mark the ground, exactly as the 1955 working group asked three professional dowsers to mark nineteen sheds. What is scored is **the ground**: whether the spots they mark differ from matched control spots in what grows on them.

Three things the card keeps in front of the family:

1. **The source is a negative study.** The KNAW working group found no effect on livestock, bees or crops, and found that three professional dowsers gave "entirely different paths" and that one dowser's own two surveys ten months apart "showed no agreement". The card's expected result is that the null reproduces — and a positive is the surprise.
2. **A hose is not a vein, and a pot is not a field.** A pass shows a difference between a dowsed spot and a matched control spot in a home bioassay; it does not establish earth rays, aquifer location, or anything about a farm. The card says so plainly.
3. **The blinding is the experiment.** If the tender knows which spot is which, the test measures expectation. The referee, the sealed key, and the pre-registration sheet are the whole design — and the source itself named this as a hard condition.

**Under-promise, stated plainly:** the likely outcome is that the dowsed and control spots do not differ, and the honest verdict is *"a dowsed spot is not distinguishable from a matched control spot in what grows on it, at home scale, in this run."* A clean, replicating positive would be genuinely interesting and would justify the taller follow-up (a multi-site pre-registered trial with a second dowser and a soil-chemistry arm).
