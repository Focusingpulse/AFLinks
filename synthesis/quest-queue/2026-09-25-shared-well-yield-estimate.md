---
name: Shared Well Yield Estimate Test
description: "Test whether a sensitive person can estimate the YIELD (flow rate) of a hidden water source — the number that decides whether a shared well is worth digging — blind, against a measured ground truth (bucket + stopwatch) and a non-dowser control. Community/shared-infra card; ~$10–40; Community mirror."
---

# ⚡ Aetherforce — Community

**Guild:** Aetherforce — Community
**Quest Line:** ⚡ Aetherforce · Community complement
**Tier:** sand
**Domain:** community (shared-infra knowledge — sizing a shared water source)
**Status:** proposed

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-09-25-shared-well-yield-estimate` · authored_at `2026-09-25` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural"],
  name: "Aetherforce — Community",
  desc: "Finding the water is only half the decision — the other half is how much it gives. The dowsing tradition claims a sensitive person can put a number on a source's yield, and it even names the method. Test it with a tap, a jug and a stopwatch: a referee sets the flow out of sight, you write down your estimate in litres per minute, then the truth gets measured. Do it blind across a range of flows, on two days, with a non-dowser guessing alongside you. You get a rank correlation between what you said and what was true — a number that says whether your estimates carried any information at all. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "sand",
  quest: [
    "Shared Well Yield Estimate Test",
    "Set up a tap or valved hose whose flow a referee can change out of your sight and hearing (a lidded bucket or a corner works). First run the calibration arm: estimate the flow of a tap you can watch, whose true rate the referee has just measured and told you — if you can't produce a signal on a known flow, stop and record it as inconclusive, because the blind arm can't tell you anything. Then run 16 blind trials across two days: the referee sets one of four pre-registered rates (1, 2, 4, 8 L/min) from a shuffled list, you write your estimate in L/min before anything is revealed, and the referee then measures the truth with a jug and a stopwatch. Include 4 water-off trials you are not told about, and have a non-dowser estimate on the same trials as the control. Measurable outcome: Spearman rank correlation between your estimates and the true flows >= 0.6, with >=60% of estimates within +/-25% of truth and clearly better than the control, repeated in a second session — or an honest null at home scale. If you have your own spring, well or cistern, run the real-source arm too: estimate its yield blind, then measure it the same day.",
    ["Science", "Measurement", "Community"],
    "🔢"
  ],
  source_doc: "sources/2026-09-25-scout-a-langs-1#find-1 (Saevarius manual, Ch. IX–X, Fr. Padey net-production method) + sources/2026-09-22-scout-a-langs-2#find-11 (UCR field record, 'Determinación del caudal que puede aportar el pozo')",
  source_url: "https://hdl.handle.net/10669/90757",
  dossier: "living-library/synthesis/replication/2026-09-25-dossier-040-shared-well-yield-estimate.md",
  pass_fail: "PASS: blind Spearman rank correlation rho >= 0.6 between estimates and true flows AND >=60% of estimates within +/-25% of the true flow AND clearly better than the non-dowser control on both, repeated in a second session. FAIL: rho <= 0.2 (the estimates carry essentially no information about the flow) OR the operator is not better than the control - an honest negative (Skeptic's Star). INCONCLUSIVE: the operator cannot produce a signal on the visible, known flow (the calibration arm) - the blind arm is then uninformative, NOT a refutation; the flow was visible or audible; the key was opened before the final tally; N was not pre-registered; or the operator answers confidently on the water-off trials.",
  evidence: "Photo of the pre-registration sheet (flow set, trial count, thresholds, scoring rule, key-holder) + the sealed key photographed sealed + every trial's written estimate, timestamped before the truth was measured + the referee's measured true flow for every trial + the water-off trials reported separately + the control operator's estimates reported separately + the rank correlation and the percentage-within-25% calculation shown + the second-session repeat + (if run) the real-source arm's estimate and its measured yield"
}
```

---

## Source Documentation

- **Primary (the field record):** Mario Enrique Arias Salguero, *"El arte del Zahorí, las creencias del Rabdomante y la sensibilidad del Radiestesista en la búsqueda del agua subterránea"*, Universidad de Costa Rica, 2020 — https://hdl.handle.net/10669/90757 (**fetched and read 2026-09-25**). A geophysicist's field survey of the practice: the two schools (physical — the instrument as a radiation receiver; mental/psychic — the whole action inside the operator, the instrument merely amplifying an imperceptible neuromuscular movement), the instruments (pendulum, L-rods, Y-rod, biotensor), the training exercises (coded envelopes; "7 of 10 correct indicates you have begun to develop sensitivity"), the flow-direction method, the **depth by counting** (*"the groundwater is between 0 and 10 m"* … *"twenty-one metres, twenty-two metres…"*), and the section heading **"Determinación del caudal que puede aportar el pozo"** — determining the flow rate the well can supply — which the document states uses the same counting procedure. The same document records **Hans Dieter Betz** (Munich, 1995), head of the German GTZ arid-zone water program, **pairing dowsers with vertical electrical soundings** in Africa and Asia. **The author writes plainly that no comparative technical studies have been published to verify the results** — the gap this card fills.
- **Primary (the named method):** Dr. E. Saevarius, *Manual Teórico e Prático de Radiestesia*, Editora Pensamento, São Paulo — https://epage.pub/doc/manual-radiestesia-yl0m28642r (**front matter and table of contents fetched and verified live 2026-09-25**; 308 pages). Ch. IX *"Busca de uma corrente d'água — Método de Fr. Padey"* and Ch. X *"Cálculo de produção líquida de uma corrente d'água subterrânea (Método de Fr. Padey)"* — the tradition names the yield claim *net production* and attributes the method to Fr. Padey. **The body of Ch. X was not reached before the fetch limit**; the method is cited by its named chapter, not by its text.
- **Scout entries:** `sources/2026-09-25-scout-a-langs-1.md` (find 1) and `sources/2026-09-22-scout-a-langs-2.md` (find 11).
- **Replication Dossier:** `living-library/synthesis/replication/2026-09-25-dossier-040-shared-well-yield-estimate.md`
- **Vault:** https://focusingpulse.github.io/AFLinks — search "radiesthesia", "water divining", "Fr. Padey"
- **Aetherforce Reference:** Search "radiesthesia", "water divining", or "geobiology" on https://www.aetherforce.energy
- **Related dossiers:** 035 (Blind Water-Line Location — *where* the line is and *which way* it flows; this card is its quantitative follow-up), 005 (Blind Geopathic Mapping — map-vs-map, no ground truth), 029 (Psi-Track Dowsing — a *mental* target), 034 (Neutral Pendulum — a tuned instrument on a known physical property), 022 (Qi-Water Conductivity — the only other instrument-on-water endpoint)

---

## Rubric Justification

| Criterion | Assessment |
|-----------|------------|
| **Practical** | YES — Named apparatus (a settable tap or valved hose, a measuring jug, a stopwatch, a pendulum) with a named procedure (calibrate, blind, estimate, measure, compare) and a measurable outcome (rank correlation between estimates and true flows; percentage of estimates within ±25%). Not pure theory. |
| **Replicable** | YES — Home, sand-cheap: ~$10–40 for a valved hose, a jug, a stopwatch, and a pendulum. No mains work, no chemicals, no purchased instrument. Two short sessions. |
| **Relevant** | YES — Community domain: sizing a shared water source is the village-scale shared-infrastructure decision that follows the siting question, and the estimate is a shared, teachable, mutual-aid skill. Fills the **Community** mirror (the community-domain complement). |
| **Honest** | YES — Claim framed as contested and pseudoscientific; the mechanism (a "subtle matter") is unfalsifiable and the card tests only the effect; both sources are proponent documents; **the UCR source itself states no comparative verification studies exist**; and the card states plainly that **a tap is not a vein** — a pass shows the operator can estimate a hidden *pipe* flow, not an aquifer's yield. Clean FAIL path. |
| **Linked** | YES — Two source docs (the UCR field record read this run; the Saevarius manual's TOC verified this run) plus two scout entries, a pre-registered replication dossier, and cross-links to five related cards. |

**Mirror choice, stated:** the card's **domain is community** (the rotation's next field) and its **guild complement is Community** — the community-domain mirror, whose theme is shared measurement capacity for neighborhood decisions. **Earthworks** was the alternative (the object is an underground water measurement, the same class as card 021 and 035); it was not chosen because it already carries two cards and this one's subject is the *community's* decision about a shared source, not the earth structure itself. The domain/mirror split is deliberate and consistent with card 035, which is community-domain with an Earthworks mirror.

---

## The honest framing (the spine of the card)

**The claim is a claim.** The radiesthesia tradition asserts that a sensitive person can put a number on a water source's yield — the Saevarius manual names the method *net production* and attributes it to Fr. Padey; the UCR field record documents the procedure. **This card tests that claim; it does not endorse it.**

**The source says the verification does not exist.** The UCR author — a geophysicist who works with electrical soundings and proton-magnetic-resonance equipment — writes plainly that the practice has no uniformity, that most practitioners are self-taught empirics who do not know which of the two schools they are using, and that **no comparative technical studies have been published that allow the results to be verified.** That is the gap a family bench can close, at its own scale, with a tap and a jug.

**The design that makes it a measurement.** Three things do the work:

1. **The calibration arm is a positive control, not a warm-up.** The operator first estimates a flow they can *see* and whose true rate they have just been told. If they cannot produce a signal there, the blind arm is **uninformative, not a refutation** — and the card says so.
2. **The endpoint is a number, so the scoring is a correlation.** A hit rate asks *did you get it right?*; a rank correlation asks *did your answers carry any information at all?* A guesser can pass a hit-rate test by luck on a small N; a guesser cannot manufacture a rank correlation. That is why ρ ≥ 0.6 is the primary endpoint and the ±25% band is secondary.
3. **The non-dowser control is the design, not an extra.** Without it, a rank correlation cannot be told from a rig that leaks the answer — a hum, a vibration, a wet sound the referee did not think of.

**The central limitation, stated up front: a tap is not a vein.** A hose has no aquifer, no rock strata, no recharge, and no seasonal drawdown. A **pass** shows only that this operator, on this tap, on these days, produced estimates that tracked a hidden pipe's flow better than a non-dowser's guesses. It does **not** show that anyone can size a real well. The optional real-source arm — estimate your own spring, well or cistern blind, then measure it — is the arm that touches the actual community decision, and it is reported separately, never pooled with the hose trials.

**A null is the likely outcome and is a complete result.** If the estimates carry no information about the flow, the quantitative claim is retired honestly at home scale, with the archive's own sources cited — and the family has learned the difference between a number that *sounds* precise and a number that *is*.

**Safety and honesty:** this is a test of a phenomenon, **not** advice to rely on dowsing to size a real well or to decide a community's water investment. Never substitute a dowsing protocol for a hydrogeological survey or a licensed driller.

---

## Relationship to the rest of the queue

This card is the **quantitative follow-up to card 035** (Blind Water-Line Location). 035 tests *detection* — can the operator mark the line and name the flow direction? Its own honest framing names depth and yield as **not tested**. This card tests the harder claim: can the operator put a *number* on the flow? Same tradition, same instrument, same rig family (a hidden flowing-water line) — different claim, different endpoint, and the overlap is stated here rather than hidden.

It is also the **first card in the queue whose endpoint is a continuous number scored by correlation** rather than a hit rate against a chance baseline — a genuinely different measurement design, and the reason it is worth a card of its own rather than a paragraph appended to 035.
