---
name: Quest Card — Heart-Rhythm Entropy Leap Test
description: "Aetherforce-branded quest card testing the claim that the Shannon entropy of the heart's rhythm changes 'decisively, in leaps' and that those leaps track a person's emotional, physical and mental state. A family measures the entropy of the pulse signal each morning for 30 days with a cheap home device, checks the reading is repeatable, counts the leaps, and asks whether leaps land on logged state-change days more than chance. Health domain (the information content of the heart's rhythm); Natural Medicine mirror (health complement, 11th card)."
---

# ⚡ Aetherforce — Natural Medicine

**Guild:** Aetherforce — Natural Medicine
**Quest Line:** ⚡ Aetherforce · Natural Medicine complement
**Tier:** sand
**Domain:** health (human physiology — the information content of the heart's rhythm, measured as the Shannon entropy of the pulse signal)
**Status:** proposed
**Created:** 2026-10-07

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-10-07-heart-rhythm-entropy-leap` · authored_at `2026-10-07` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural", "urban"],
  name: "Aetherforce — Natural Medicine",
  desc: "Your heart does not beat like a metronome. Beat to beat the spacing shifts, and the pattern of those shifts carries information — how much is what a number called 'entropy' measures. A Hungarian research group spent a year asking whether that number is a signal you can read at home, and reported something strange: they said the information in the heart's rhythm sometimes changes 'decisively, in leaps,' and that the leaps line up with how a person is doing emotionally and physically. That is the claim this quest tests, and it is a claim, not a fact — the group reported a conclusion and never published the data or a control group, and the project it sits inside was built to argue for water memory, which is not what you are measuring here. You are testing the MEASUREMENT, and you take nothing. Get a cheap pulse-waveform device — a fingertip sensor, a USB pulse oximeter that exports its trace, or a chest strap with an app that reports an entropy number. First check the thing is an instrument at all: take three readings back to back one morning and see if they agree. Then measure once every morning for thirty days, writing down your sleep, mood and energy BEFORE you look at the number. Work out your typical day-to-day wiggle, call any jump bigger than three times that a 'leap,' and ask whether the leaps land on the days your state actually changed. If the readings are repeatable, the leaps are real, and they track your state, you have found something worth chasing. If the numbers wander randomly, or leap on days nothing changed, you have learned that this measure is not telling you what the source says it tells you — and that is a complete result, not a wasted month. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "sand",
  quest: [
    "Heart-Rhythm Entropy Leap Test",
    "FIRST prove the device is an instrument: one morning, take THREE readings back to back (same sitting, ~2 min apart) and compute the entropy of each. If the three readings scatter as much as the day-to-day values you later collect, the device is measuring noise and a no-leap result is VOID, not a null - record the three values and their spread. Then measure ONCE each morning for 30 consecutive days, at the same time, in the same posture, before coffee or exercise, and compute the day's entropy value. BEFORE you compute each day's number, write down a state score: sleep 1-5, mood 1-5, energy 1-5. Now analyse: compute the day-to-day change in entropy for all 29 transitions and take the MEDIAN change M. Call any change bigger than 3 x M a LEAP, and record whether it was a step (the value stayed at the new level for 2+ days) or a spike-and-return. Mark each day as a state-change day (any state score moved by 2+ from the day before) or a steady day. Measurable outcome: (a) the within-morning spread from Phase 0 versus the between-day spread - is the reading repeatable? (b) the COUNT of step-change leaps in the 30-day series; (c) the 2x2 table of leaps against state-change days, tested with a Fisher exact test. Target: a repeatable reading, at least 3 step-change leaps, AND leaps landing on state-change days above chance (one-tailed p < 0.05) = the claim survives; no leaps (0-2, indistinguishable from smooth drift), or leaps landing at chance = the measure does not show the claimed leaps at home scale (the expected, complete result). If Phase 2 finds 3+ leaps, repeat the whole 30-day series once to see whether the leap behaviour repeats.",
    ["Science", "Measurement", "Health"],
    "💓"
  ],
  source_doc: "translations/2026-10-06-vizgyongyok-es-az-elet-ritmusa-bukki-hu.md — Tamás Bükki, 'Vízgyöngyök és az élet ritmusa' (Water Pearls and the Rhythm of Life), gajatri.hu, 25 March 2023 (the Triangulum Foundation's one-year water-memory/homeopathy research project; the heart-rhythm Shannon-entropy measurement section)",
  source_url: "https://focusingpulse.github.io/AFLinks",
  dossier: "living-library/synthesis/replication/2026-10-07-dossier-070-heart-rhythm-entropy-leap.md",
  pass_fail: "PASS (instrument): the Phase 0 within-morning spread is clearly smaller than the between-day spread - the cheap device gives a repeatable reading and is usable as an instrument | PASS (leaps exist): the 30-day series contains >= 3 step-change leaps (change > 3 x the median day-to-day change, sustained >= 2 days) - the series is not smooth drift | PASS (leaps correlate): leaps land on state-change days more often than on steady days (2x2 table, Fisher exact, one-tailed p < 0.05) - the source's correlation claim holds | PASS (claim refuted - the expected, complete result): the series shows no decisive leaps (0-2, indistinguishable from smooth drift), or leaps land on state-change days at chance - the heart-rhythm entropy measure does not show the claimed leaps at home scale (Skeptic's Star) | FAIL (void, not a null): the Phase 0 instrument check fails - the cheap device cannot give a repeatable same-sitting reading - the instrument measures noise | INCONCLUSIVE: fewer than 30 days; the measurement time or posture was not held constant; the state log was written AFTER the entropy value; a device or sensor was changed mid-series; the proxy path (RR-interval entropy from a chest strap) was used without recording it | ARTIFACT: the leap count tracks a measurement-schedule change (a different time of day, a different posture, a change in caffeine or exercise) rather than a state change; the leaps disappear when the measurement time is re-randomised; or the state log correlates with the entropy because both were written at the same moment with knowledge of the other",
  evidence: "The Phase 0 three back-to-back readings with their spread + the full 30-day table: date, entropy value, the three state scores, and the day-to-day change + the leap list: which days, the change size, and whether each was a step or a spike + the 2x2 leap-vs-state-change table with the test result + the second 30-day series if run + a one-paragraph verdict (supports / refutes / inconclusive) with the numbers + the device and analysis path used (raw PPG waveform vs RR-interval proxy) recorded explicitly"
}
```

---

## Source Documentation

- **Primary (the claim):** `translations/2026-10-06-vizgyongyok-es-az-elet-ritmusa-bukki-hu.md` — the full English translation of Tamás Bükki, *Vízgyöngyök és az élet ritmusa* ("Water Pearls and the Rhythm of Life"), gajatri.hu, 25 March 2023 (Hungarian). It reports the **Triangulum Foundation's one-year water-memory / homeopathy research project** (five physicians, a mathematician, a physicist, a physiology lecturer). The measurement claim is quoted verbatim: *"The chosen device is a simple pulse oximeter that clips onto the fingertip… If we analyze the shape of the signal measured this way, and the patients perform the measurement daily over a longer period (in our case this was 10 weeks), then we can calculate how the deviation from the base rhythm changes. The amount of information in the 'music' sitting on the base rhythm as an energy wave, and its characteristic changes, can be determined; the Shannon entropy serves this purpose… Analyzing the measured data, we concluded that the information residing in the patients' heart tremors indeed sometimes changes decisively, in leaps, during a treatment. The change thus measurable appears to correlate with the changes observed in the patients' emotional, physical and mental states."*
- **Source URL:** https://gajatri.hu/vizgyongyok-es-az-elet-ritmusa/
- **The mechanism the project was built to support** (stated as the project's conclusion, **not** what this card measures): *"it appears that water is able to carry and store information, and to transmit the characteristic vibration pattern of an active substance to the human organism even when not a single molecule of active substance is present in the given medicine."* The card deliberately separates the **measurable** claim (entropy leaps) from the **unmeasurable** one (water carries information).
- **Cited within the source:** [Caligiuri, 2022] *Quantum (hyper)computation through universal quantum gates in water coherent domains*, J. Phys.: Conf. Ser. 2162, 013003; [Giudice, 2009] Del Giudice & Tedeschi, *Water and Autocatalysis in Living Matter*, Electromagn. Biol. Med. 28, 46–52; [MTA, 2017] the Hungarian Academy of Sciences' statement *Homeopathy: useful or harmful?* (the source quotes it as the position it argues against).
- **The instrument named in the source:** the "Scan4all" remote-diagnostic system (https://hello.emed4all.com/scn4all/). The card does **not** require it — the source itself says the measurement is made with "a simple pulse oximeter," and the card specifies a raw-PPG or chest-strap path instead.
- **Companion cards (health domain, different endpoints):** `synthesis/quest-queue/2026-09-11-ez-water-exclusion-zone.md` (009), `synthesis/quest-queue/2026-09-20-water-memory-imprint.md` (025), `synthesis/quest-queue/2026-09-28-egely-wheel-vital-force.md` (051), `synthesis/quest-queue/2026-09-30-form-field-water-structure.md` (058), `synthesis/quest-queue/2026-10-03-morning-light-timing.md` (064). **None measures the information content of a physiological signal, and none uses a computable information-theoretic endpoint.**
- **Replication Dossier:** `living-library/synthesis/replication/2026-10-07-dossier-070-heart-rhythm-entropy-leap.md`
- **Aetherforce Reference:** search "heart rhythm" / "Shannon entropy" / "water memory" / "structured water" on https://www.aetherforce.energy
- **Vault link:** https://focusingpulse.github.io/AFLinks

---

## Rubric Justification

- **Practical:** a named apparatus (a pulse-waveform device — a MAX30102 + microcontroller, a USB pulse oximeter that exports its trace, or a chest strap with an entropy-reporting app) with a named procedure (Phase 0 instrument check → 30 daily morning measurements → leap detection → leap–state correlation) and a measurable outcome (**the count of step-change leaps and the 2×2 leap-vs-state-change table, tested with a Fisher exact test, on top of a computable Shannon-entropy value**). Not pure theory.
- **Replicable:** home-scale (**~$15–70** — a MAX30102 breakout + microcontroller, a USB pulse oximeter, or a chest-strap HRV monitor), no lab, no chemicals, no treatment. A family can run it at the kitchen table; one person can run it alone.
- **Relevant:** maps to the Village **health** survival domain (the information content of the heart's rhythm) and complements the **Natural Medicine** guild (health / biofield).
- **Honest:** framed as a TEST, not an endorsement. The source is a one-year project by a foundation with a homeopathy interest, reporting a *conclusion* without publishing its data or a control group, and the card says so in the quest text. It tests the **measurement**, takes **no remedy**, and makes **no health claim** — which is the honest way to engage a homeopathy-adjacent source under the child-facing rule. The expected outcome is a **null**, and the card presents a positive as the surprise.
- **Linked:** source doc (the Bükki translation), dossier created with protocol + pass/fail, evidence protocol defined.

---

## What makes it the queue's first of its kind

- **The first card whose endpoint is an information-theoretic quantity** — the Shannon entropy of a physiological signal. Every other health card scores a physical quantity (temperature, conductivity, a spin rate) or an operator's hit rate; none scores the *information content* of a body signal.
- **The first card on the heart's rhythm as a measurable channel** — the first to treat the pulse signal as carrying a message rather than as a rate.
- **The first card sourced from the Triangulum water-memory / homeopathy research project**, and the first to test a claim whose **mechanism is not what is being measured** — the card deliberately separates the measurable claim (entropy leaps) from the unmeasurable one (water carries information).
- **The first card whose primary instrument check is test–retest reliability** — it asks whether the cheap device is an instrument at all before asking what it reads.
- **A Natural Medicine card that is purely a measurement** — no remedy, no treatment, no health claim.

---

## Honest Framing

This is a test, not an endorsement. The measurement claim is quoted here in the source's own words: *"Analyzing the measured data, we concluded that the information residing in the patients' heart tremors indeed sometimes changes decisively, in leaps, during a treatment. The change thus measurable appears to correlate with the changes observed in the patients' emotional, physical and mental states."* The source reports a **conclusion** from a one-year project run by a foundation with a homeopathy interest; it publishes **no data, no control group, and no pre-registration**, and the project it sits inside was built to argue for water memory — which is **not** what this card measures. The card turns the measurement claim into a scored test a family can run with a cheap device. The likely outcome is that the readings are too noisy to be an instrument, or stable with no decisive leaps, and that is a **complete and useful result** (Skeptic's Star), not a failure. The card makes **no health claim**, instructs **no treatment**, and is not a test of anything a family should act on before the result is in. It is a method test of a cited claim.

---

## Aetherforce Mirror Coverage

This card complements **Guild: Natural Medicine** (health / biofield) — its **11th** card, after the Eeman Biofield Test (2026-09-10), the Eeman Sleep Quality Test (2026-09-12), the Qi-Water Conductivity Test (2026-09-20), the Water Memory Imprint Test (2026-09-20), the Neutral Pendulum Discrimination Test (2026-09-22), the Wave-Water Stress-Recovery Test (2026-09-24), the Palm Thermal Control Test (2026-09-26), the Egely Wheel Vital-Force Test (2026-09-28), the Form-Field Water-Structure Test (2026-09-30) and the Morning Light Timing Test (2026-10-03).

**Mirrors filled: 25/26** (unchanged — no new guild filled; Textiles remains the only empty mirror, with no buildable fiber-resonance source in the archive).

---

## Dossier

- `living-library/synthesis/replication/2026-10-07-dossier-070-heart-rhythm-entropy-leap.md` — full protocol, apparatus, pass/fail, confounds and verdict rules.
