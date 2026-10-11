---
name: Neutral Pendulum Discrimination Test
description: "Test the claim that a neutral pendulum, tuned by string length to a target's vibrational quality, produces a felt pull only when the tuned quality is present. Blind hit rate against a computed chance baseline, with an open positive-control arm and a sham block. The first card from the video lane."
---

# ⚡ Aetherforce — Natural Medicine

**Guild:** Aetherforce — Natural Medicine
**Quest Line:** ⚡ Aetherforce · Natural Medicine complement
**Tier:** sand
**Domain:** health (vibrational testing as a measurement skill)
**Status:** proposed

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-09-22-neutral-pendulum-discrimination` · authored_at `2026-09-22` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural", "urban"],
  name: "Aetherforce — Natural Medicine",
  desc: "A neutral pendulum on a string is said to be an extension of your own energy field — tune the string length to a quality and you feel a pull when that quality is present, nothing when it isn't. The instructor says it himself: an external skeptic will never believe it whether your hand is rock still or not. So test it blind. Learn the pull on known batteries, then let someone else code 40 containers you can't see and score your hits against chance. If the pull discriminates, you have a measurement skill; if it doesn't, you have retired a claim honestly. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "sand",
  quest: [
    "Neutral Pendulum Discrimination Test",
    "Tune a neutral pendulum's string length to a battery's positive pole until you feel the pull. Then run two arms: 20 OPEN trials where you know each battery's polarity (the positive control — can you produce the signal at all?), then 40 BLIND trials where a second person flips a coin, hides each battery in an opaque container, and codes it without you seeing. Report pull or no-pull in writing before each container is opened, unblind only after the last number, and score hits against a 50% chance baseline with a binomial test. Add a 10-trial sham block of empty containers to catch false positives. Target: open arm >=16/20 AND blind arm >=27/40 at p<0.05 AND sham false positives <=2/10 — or an honest refutation of the claim at home scale.",
    ["Science", "Health", "Community"],
    "🪢"
  ],
  source_doc: "sources/video/2026-09-21-biogeometry-neutral-pendulum-testing (video record — Vesica Institute, 'Learning to Test with the Neutral Pendulum')",
  source_url: "https://focusingpulse.github.io/AFLinks",
  dossier: "living-library/synthesis/replication/2026-09-22-dossier-034-neutral-pendulum-discrimination.md",
  pass_fail: "PASS: open arm >=16/20 (80%) AND blind arm >=27/40 (67.5%) with binomial p<0.05 one-tailed (chance 0.5) AND sham false-positive rate <=2/10, and the direction repeats in a second run. FAIL: open arm >=16/20 (operator demonstrably can produce the signal open) AND blind hit rate within chance (16-24/40, p>0.05). INCONCLUSIVE: open arm <16/20 (operator cannot produce the signal even open - the blind arm is uninformative, NOT a refutation), the key was opened before the final tally, the calibration string length changed mid-run, N was not pre-registered, or sham false positives exceed 20%.",
  evidence: "Photo of the pre-registration sheet (trial counts, thresholds, chance model, scoring rule, key-holder) + the calibration string length recorded + the sealed key photographed sealed + the written pull/no-pull report for every trial, timestamped before unblinding + the full hit/miss tally with the binomial calculation shown + the sham block results reported separately + the unblinding sheet"
}
```

---

## Source Documentation

- **Primary (the claim):** `living-library/sources/video/2026-09-21-biogeometry-neutral-pendulum-testing.md` — the video record for *"Learning to Test with the Neutral Pendulum with Dr. Robert J. Gilbert"* (Vesica Institute, https://www.youtube.com/watch?v=rklULOn8p0w), harvested 2026-09-21. The record carries the transcript (**P0 — never publish**) and the termbase (**P2 — publishable**). This card summarises the claim; it does not reproduce the transcript.
- **The source's own hard condition:** the record's practicality assessment states the video *"states plainly that 'an external skeptic will never believe it whether your hand is rock still or not' — so an unblinded card would be exactly the kind of unfalsifiable claim the engine's honesty rubric forbids. Framed as a blind protocol, it is a legitimate card."* **Blinding is carried into the card as a hard condition, not an option.**
- **Terminology caution carried from the record:** *vibrational radiesthesia* (physical, instrument-based) and *mental dowsing* (programmed, mental) are used as **opposed** practices. The card tests the physical method only; collapsing the two destroys the source's argument.
- **Replication Dossier:** `living-library/synthesis/replication/2026-09-22-dossier-034-neutral-pendulum-discrimination.md`
- **Vault:** https://focusingpulse.github.io/AFLinks — search "radiesthesia" or "pendulum"
- **Aetherforce Reference:** Search "radiesthesia", "pendulum", or "biofield" on https://www.aetherforce.energy
- **Related dossiers:** 029 (Psi-Track Dowsing — the *thought-leaves-a-track* arm; sender/receiver design, different claim), 022 (Qi-Water Conductivity — a physical instrument on a subtle-energy claim), 017 (Orgone Accumulator To-T — the other home subtle-energy measurement card)

---

## Rubric Justification

| Criterion | Assessment |
|-----------|------------|
| **Practical** | YES — Named apparatus (neutral pendulum, tuned by string length) with a named procedure (calibrate open, test blind) and a measurable outcome (blind hit rate against a computed 50% chance baseline, plus a sham false-positive rate). Not pure theory. |
| **Replicable** | YES — Home, sand-cheap: ~$10–20 for a pendulum, a few batteries, an opaque container, and a coin. No mains power, no chemicals, no purchased instrument. One evening to run. |
| **Relevant** | YES — Health domain (vibrational testing as a measurement skill); fills the **Natural Medicine** mirror (subtle energy / biofield). A family that can measure — or honestly fail to measure — a subtle-energy claim has a skill the rest of the survival-mode health content depends on. |
| **Honest** | YES — The card carries the source's own hard condition (blinding) as a requirement, states that the mechanism is unfalsifiable and only the effect is testable, adds an **open positive-control arm** so a null blind result is not misread as a refutation, adds a **sham block** to catch expectation-driven pulls, pre-registers N and the chance model, and reports every trial. A null is a **complete, valuable result** (Skeptic's Star). |
| **Linked** | YES — Real source (video-record slug + channel attribution), dossier 034 created first, Vault + Aetherforce links provided. |

**Why this card and not another.** The health field's seed candidates were structured/EZ water and subtle-energy rest tools — and those are already carded (022 Qi-Water Conductivity, 028 Water Memory Imprint, 006 Eeman Animal Calm, 012 Eeman Sleep Quality, 017 Orgone To-T). What the health field had never carried is a **measurement-skill** card: not a device and not a treatment, but the question of whether a family member can learn an instrument-based discrimination and have it survive blinding. The video lane was wired on 2026-09-21 specifically to feed this engine, and its first record already carries a qualifying assessment — this is that card.

**Why it is not a duplicate of dossier 029.** Card 029 (Psi-Track Dowsing) tests whether an **intense thought leaves a track in space** that a blind dowser can follow to a hidden object — a **sender/receiver** design with three roles. This card tests whether a **tuned instrument discriminates a known physical property** (battery polarity) with **no sender at all** — a single-operator blind discrimination design. Different claim, different apparatus, different protocol. **The overlap is the pendulum and the blinding discipline, and it is stated, not hidden.** The engine permits multiple cards per domain (Natural Medicine carries four, Plumbing four, Gardening three).

**Why the open arm is not optional.** The signal is operator-reported. If the operator cannot produce it even when they know the answer, a blind null tells you nothing about the claim — it only tells you this operator has not learned the method. Without the open arm, a null blind result would be filed as a refutation when it is actually an **unattempted test**. The open arm is the control that makes the blind arm interpretable, and it is the reason this card is a real experiment rather than a demonstration.

**Why the sham block is not optional.** The operator expects a pull. An empty container tests whether they report one anyway. Without the sham block, a positive blind result could be an expectation artifact, and a null could be a ceiling effect. Both arms need the sham.

---

## Aetherforce Mirror Coverage

This card fills **Guild 19: Natural Medicine** (complement domain "subtle energy / biofield") as its **fifth** card, after Eeman Biofield (merged), Eeman Sleep Quality (012), Qi-Water Conductivity (022), and Water Memory Imprint (028). It is assigned to Natural Medicine because the domain is health and the complement domain is the biofield — the mirror whose subject this is. The queue already carries multiple cards per mirror by design (Plumbing & Hot Water four, Gardening three).

**Updated coverage: 25/26** (unchanged — Textiles remains the only empty mirror, and no buildable fiber-resonance source exists in the archive; re-scan #9 this run, same terms, found nothing new).

---

## Family Check-in

```
Member: practicality-engine
Run: 2026-09-22 22:00 UTC
Budget: gate passed (gear overdrive; watchdog flagged practicality-engine stale — expected lag after the cron re-create, see note)
Field: health (rotation honored — previous field shelter, 2026-09-22 14:00 UTC)
Card: 3 of 3 daily
Status: emitted
Watchdog note: the stale flag is the expected lag after the cron was re-created to add the
  literal check-in step (id db128f38-853e-4a1a-a8c5-78564c1ab108, empty run history until
  first fire). Not a prompt gap.
```

---

*Generated by the Engine of Practicality — 2026-09-22*
