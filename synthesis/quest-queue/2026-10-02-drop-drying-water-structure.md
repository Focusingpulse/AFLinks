---
name: Quest Card — Drop-Drying Water-Structure Discrimination Test
description: "Aetherforce-branded quest card testing the Ruth Kübler micro-optical drop-drying method — the perceptual method the whole 'water revitalisation' market implicitly appeals to. A drop of water dried on a clean glass slide leaves a residue whose structure (hatching, crossing lines, a bluish welling core, edge density) is claimed to change in specific ways after vortexing, magnet treatment, or mineral contact. The card tests the one thing the source never tested: can a BLIND rater tell treated water from untreated water by its dried drop, and can they tell vortexed from magnetised? Water domain; Greywater & Willow mirror (water-structure complement)."
---

# ⚡ Aetherforce — Water

**Guild:** Aetherforce — Water
**Quest Line:** ⚡ Aetherforce · Greywater & Willow complement
**Tier:** sand
**Domain:** water (water structure — a claimed change in the dried-drop residue of water after vortexing / magnet / mineral treatment; a blinded perceptual discrimination test)
**Status:** proposed
**Created:** 2026-10-02

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-10-02-drop-drying-water-structure` · authored_at `2026-10-02` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural", "urban"],
  name: "Aetherforce — Water",
  desc: "Put a single drop of water on a clean glass slide, let it dry in the air, and look at the residue under a cheap microscope. That is the whole method — and it is the method the entire 'water revitalisation' market quietly stands on. In a cooperative report from the University of Stuttgart's aerospace structures institute and the Pythagoras-Kepler-School, water that had been vortexed, stood on a magnet, or wrapped in a mineral cuff was claimed to dry into visibly different patterns: vortexing erased the hatching and crossing lines and strengthened a bluish core; magnets densified the whole structure; minerals reordered it. But every one of those slides was prepared and read by someone who already knew which water was which. This quest does the one thing the report never did — it blinds the reader. Code the slides, hand them to three people who never saw the preparation, and ask two forced-choice questions: treated or untreated, and vortexed or magnetised. Score the answers against chance. If blind raters can read the treatment off the dried drop, you have found a cheap home water test the archive has never validated; if they cannot, you have shown that the pattern is a story told by the person who already knew the answer — and that is a complete result, not a failure. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "sand",
  quest: [
    "Drop-Drying Water-Structure Discrimination Test",
    "Clean glass microscope slides with soft paper and a microfibre cloth (dust shows in the dark field), align them north-south, and put a FIXED-volume drop on each with a sterile syringe. Let the drops dry in the air at 19-25 C and 50-70% humidity. FIRST prove the method can see anything at all: dry a known-different pair (distilled vs hard tap water) and have a blind rater sort them - if that fails, the whole run is void, not a null. Then draw ONE batch of water and split it four ways: (A) vortexed through a vortexer for a fixed time, (B) 30 mL stood on a permanent magnet for 30 min, (C) untreated control, (D) sham - poured and waited identically but not treated. Dry 5+ slides per arm, photograph each under identical lighting and magnification, and have a second person code the images. Three raters, working alone and blind, answer two forced-choice questions per image: treated or untreated, and vortexed or magnetised. Measurable outcome: each rater's accuracy against chance (50% on a 2-way choice), pooled, repeated on a second day. Target: treated-vs-untreated AND vortexed-vs-magnetised both at 1.5x chance or better, replicating across raters and sessions = the claim survives; both at chance = the dried-drop pattern carries no readable treatment signature (the expected, complete result).",
    ["Science", "Observation", "Water"],
    "💧"
  ],
  source_doc: "translations/2026-09-30-mikrooptische-wasserverwirbelung-trocknungsstrukturen-de.md — Berthold Heusel, 'Mikrooptische Untersuchungen zur Auswirkung von Wasserverwirbelung auf Trocknungsstrukturen des Wassers', cooperative project report of the Institut für Statik und Dynamik (ISD), University of Stuttgart, with the PKS (Pythagoras-Kepler-Schule, Lauffen/Bad Ischl)",
  source_url: "https://focusingpulse.github.io/AFLinks",
  dossier: "living-library/synthesis/replication/2026-10-02-dossier-061-drop-drying-water-structure.md",
  pass_fail: "PASS (claim survives - surprising): blind raters distinguish treated from untreated AND vortexed from magnetised, each at >= 1.5x chance, replicating across raters and in a second session - the report's 'different kinds of change' claim survives and needs the taller follow-up | PASS (claim refuted - the expected, complete result): both questions score at chance (within the binomial noise band) in >= 2 of 3 sessions - the dried-drop pattern does not carry a treatment signature a blind rater can read (Skeptic's Star) | FAIL (void, not a null): the method cannot separate the known-different instrument-check pair - the run measures nothing | INCONCLUSIVE: fewer than 3 raters; one session; the rater saw the preparation or the key; slides not coded; drop volume not fixed; room conditions outside 19-25 C / 50-70% RH; lighting or magnification differed between slides; fewer than 5 slides per arm | ARTIFACT: the discrimination tracks dust or slide cleanliness rather than the treatment; the rater can read drop size; the discrimination tracks drying order or tray position; the rater's expectation (unblinded); or the sham arm (D) is distinguished from the control (C) - handling alone produces the signal",
  evidence: "Photo of the setup (slides, syringe, microscope, magnet, vortexer) + the pre-registration sheet (arms, drop volume, drying conditions, N, raters, questions, thresholds) photographed before any slide dried + the instrument-check result (the known-different pair, sorted blind) + the coded slide images (whole drop at 4x + detail at 10x) + the rater score sheets (Q1 and Q2, per rater) + the accuracy table against chance + the recorded temperature and humidity + the second-session repeat + the void/artifact checks reported whether or not they void the run"
}
```

---

## Source Documentation

- **Primary (the claim and the method):** `translations/2026-09-30-mikrooptische-wasserverwirbelung-trocknungsstrukturen-de.md` — Berthold Heusel M.A., *Mikrooptische Untersuchungen zur Auswirkung von Wasserverwirbelung auf Trocknungsstrukturen des Wassers* (Micro-optical investigations into the effect of water vortexing on the drying structures of water) — a cooperative project report of the **Institut für Statik und Dynamik der Luft- und Raumfahrtkonstruktionen (ISD), University of Stuttgart** (Prof. Dr.-Ing. Bernd Kröplin) with the **PKS (Pythagoras-Kepler-Schule, Lauffen/Bad Ischl)**, de→EN, 6/6 chunks. It gives the **full working technique** (slide cleaning, N–S alignment, syringe-applied drops, 19–25 °C / 50–70 % RH, dark-field or phase-contrast microscopy at 4×/10×/20×), the three treatment arms and their claimed signatures, and the report's own call for verification.
- **Source PDF:** https://www.frohkost.ch/mediafiles/PDF/Diverse%20Geraete/Wassergeraete/Mikrooptische_Untersuchungen_Auswirkung_von_Wasserverwirbelung.pdf
- **Scout record:** `sources/2026-09-29-scout-a-langs-2.md` § German, **find 7** (`practical_applicability: flag=true, fields [reproducible, conceptual]`; note: "the method is fully stated … Cheap, repeatable protocol"). Also recorded at `sources/2026-09-16-scout-a-de-fr-ja.md` find 1. ⚠ The scout notes the findings are "phenomenological (structure comparison), not quantitative; the document itself frames them as 'first tests'" — the card carries that caveat.
- **Method origin (cited by the report, not held in the archive):** the micro-optical drop-drying method of the Stuttgart artist **Ruth Kübler**, used by the ISD to investigate physical and biophysical influences on water.
- **Companion cards (water structure, different endpoints):** `synthesis/quest-queue/2026-09-30-form-field-water-structure.md` (dossier 058) — a **light-scattering** measurement of a paper cylinder's form effect on water. `synthesis/quest-queue/2026-09-11-ez-water-exclusion-zone.md` (dossier 009) — an exclusion-zone observation. `synthesis/quest-queue/2026-09-25-water-memory-persistence.md` (dossier 042) — a thermal-history memory. **None uses a dried-drop pattern, and none scores a blind observer.**
- **Companion card (perceptual discrimination, different object):** `synthesis/quest-queue/2026-09-22-neutral-pendulum-discrimination.md` (dossier 034) — a blind pendulum discrimination of water samples. That card tests a *dowser's instrument*; this one tests a *microscope image*. Both score a blind observer against chance.
- **Replication Dossier:** `living-library/synthesis/replication/2026-10-02-dossier-061-drop-drying-water-structure.md`
- **Aetherforce Reference:** search "water structure" / "Schauberger" / "vortex water" on https://www.aetherforce.energy
- **Vault link:** https://focusingpulse.github.io/AFLinks

---

## Rubric Justification

- **Practical:** a named apparatus (glass slides, a syringe, a microscope, a vortexer, a magnet) with a measurable outcome (**a blind rater's forced-choice discrimination accuracy against chance**, for treated-vs-untreated and vortexed-vs-magnetised) and a specific multi-rater protocol. Not pure theory.
- **Replicable:** home-scale (**~$40–200** — a USB microscope, slides, a syringe, a magnet, a vortexer), no lab, no chemicals, family-safe. The report's own method is fully stated.
- **Relevant:** maps to the Village **water** survival domain (water structure — a cheap home way to ask whether a water device does anything visible) and complements the **Greywater & Willow** guild (water structure / vortex).
- **Honest:** framed as a TEST, not an endorsement. The source is a **cooperative project report, not peer-reviewed**, it is **unblinded**, and it explicitly calls for verification — the card says all three. The expected outcome is a null, and a positive is presented as the surprise.
- **Linked:** source doc (translation + source PDF), scout record, dossier created with protocol + pass/fail, evidence protocol defined.

---

## What makes it the queue's first of its kind

- **The first drop-drying / micro-optical water-structure card.** The method the whole "water revitalisation" market implicitly appeals to has never been tested in this queue.
- **The first card whose endpoint is a blinded visual-pattern discrimination.** Every prior perceptual card (013 Kolisko, 034 neutral pendulum, 045 palm thermal) scores a *sorting* or a *sensation*; this one scores **whether a treatment can be read off an image at all** — the perceptual analogue of the dowsing cards' forced-choice scoring, applied to water rather than to a hidden target.
- **The first card that tests whether three treatments are distinguishable from one another** (vortex vs. magnet vs. control) rather than whether one treatment beats a baseline. The report's specific claim is that the changes are "of a different kind" — a **discriminability** claim, and the card scores it as one.
- **The design choice that is the whole card:** the report's images were prepared and read by an operator who already knew which water was which. The card's fix is the arm the source lacked — **blinding**: coded slides, raters who never see the preparation, and a forced-choice score against chance. It also adds the **sham arm (D)** the report lacked (poured and waited identically but not treated), so handling alone cannot produce the signal, and the **instrument check** (a known-different pair), so a no-difference result is not read as a null when the method could not have seen a difference.

---

## Honest Framing

This is a test, not an endorsement. The report is a **cooperative project report of a university institute and a Schauberger school**, not a peer-reviewed study; its findings are **phenomenological** ("structure comparison") and it frames them itself as "first tests" that "would … have to be verified on a series of similar waters." Every slide in it was prepared and read **unblinded**. The card keeps that honesty: the likely outcome is that blind raters score at chance, because the dried-drop pattern is moved more by dust, humidity, drop size and slide cleanliness than by any of these treatments — and that is a **complete and useful result** (Skeptic's Star), not a failure. A discrimination rate above chance, replicating across raters and sessions, would be genuinely surprising and would justify the taller follow-up: a series of waters, a pre-registered feature checklist, and an instrumented image metric. The card is a method test of a cited claim; it makes **no health claim** and is **not** a water-safety test — it is never a substitute for a real water analysis before you drink.

---

## Aetherforce Mirror Coverage

This card complements **Guild 14: Greywater & Willow** (water structure / vortex) — its **3rd** card, after the Hyperbolic Funnel Vortex (2026-09-09) and the Contour Swale Rain-Retention Test (2026-09-23).

**Mirrors filled: 25/26** (unchanged — no new guild filled; Textiles remains the only empty mirror, with no buildable fiber-resonance source in the archive).

---

## Dossier

- `living-library/synthesis/replication/2026-10-02-dossier-061-drop-drying-water-structure.md` — full protocol, apparatus, pass/fail, confounds and verdict rules.
