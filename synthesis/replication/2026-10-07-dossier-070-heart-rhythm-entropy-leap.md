---
name: Dossier 070 — Heart-Rhythm Entropy Leap Test
description: "Replication dossier for the claim that the Shannon entropy of the heart's rhythm changes 'decisively, in leaps' and that those leaps correlate with a person's emotional, physical and mental state. Tests whether a cheap home pulse-waveform device gives a repeatable entropy reading, whether the daily series shows step changes rather than smooth drift, and whether any leap lands on a logged state-change day more often than chance. Health card (the information content of the heart's rhythm); home, ~$15-70; Natural Medicine mirror (health complement, 11th card)."
---

# Dossier 070 — The Heart-Rhythm Entropy Leap Test

**Status:** protocol
**Domain:** health (human physiology — the information content of the heart's rhythm, measured as the Shannon entropy of the pulse signal)
**Tier:** sand (home, ~$15–70)
**Created:** 2026-10-07
**Source doc:**
- `living-library/translations/2026-10-06-vizgyongyok-es-az-elet-ritmusa-bukki-hu.md` — the **full English translation** of Tamás Bükki, *Vízgyöngyök és az élet ritmusa* ("Water Pearls and the Rhythm of Life"), gajatri.hu, 25 March 2023 (Hungarian). Source: https://gajatri.hu/vizgyongyok-es-az-elet-ritmusa/. It reports the **Triangulum Foundation's one-year water-memory / homeopathy research project** (five physicians, a mathematician, a physicist, a physiology lecturer) and, in its "The heart's hidden secrets" section, the specific measurement claim this card tests.

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-10-07-heart-rhythm-entropy-leap` · authored_at `2026-10-07` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## The claim (as asserted by the source)

The source states the measurement claim directly, translated:

> "We can measure the heart's rhythm in many ways. We chose a simple device that can be given to people who use homeopathy, and at home, painlessly, in two minutes it is able to collect every essential piece of information about the heart's 'music,' while also making possible a sufficiently sensitive and accurate measurement. The chosen device is a simple pulse oximeter that clips onto the fingertip [Scan4all], which with the help of light flashes is able to record how the small vessels in the fingertip pulse. If we analyze the shape of the signal measured this way, and the patients perform the measurement daily over a longer period (in our case this was 10 weeks), then we can calculate how the deviation from the base rhythm changes. The amount of information in the 'music' sitting on the base rhythm as an energy wave, and its characteristic changes, can be determined; the Shannon entropy serves this purpose, for example. This concept was, incidentally, created by the science dealing with information to measure the information content of human language. Analyzing the measured data, we concluded that the information residing in the patients' heart tremors indeed sometimes changes decisively, in leaps, during a treatment. The change thus measurable appears to correlate with the changes observed in the patients' emotional, physical and mental states."

And the mechanism the project was built to support (stated as the project's conclusion, not as an established result):

> "it appears that water is able to carry and store information, and to transmit the characteristic vibration pattern of an active substance to the human organism even when not a single molecule of active substance is present in the given medicine."

**What is being tested, in one sentence:** does the **Shannon entropy of the pulse signal** — measured daily at home with a cheap device — (a) give a **repeatable** reading, (b) show **"leaps"** (decisive step changes) rather than smooth drift, and (c) land those leaps on **logged state-change days** more often than chance?

## Honest status of the claim

**The archive holds the claim and no home test of it.** A grep for `heart`, `pulse`, `entropy`, `HRV`, `oximeter` across `synthesis/quest-queue/` and `synthesis/replication/` returns **no card and no dossier** on the information content of the heart's rhythm. The queue's nearest health cards measure *water* (EZ water, water memory, form-field water-structure), *biofield* (Eeman, qi-water conductivity), *operator skill* (neutral pendulum, palm thermal control) or *light timing* — none measures a **physiological signal's information content**, and none uses a **computable information-theoretic endpoint**.

Five things the card must say out loud, because they are what a family is actually testing:

1. **The claim is a claim, not an established result.** The source is a one-year project run by a foundation with a homeopathy interest, reporting a *conclusion* ("we concluded that…") without publishing the underlying data or a control group. The card is a test, not an endorsement.
2. **This card tests the MEASUREMENT, not homeopathy.** No remedy is taken. The card asks only whether the heart-rhythm entropy measure behaves the way the source says it does. That keeps it clear of the child-facing health-claim rule: it issues no treatment claim and instructs no one to take anything.
3. **The endpoint is a number, and the likely result is a null.** The most likely outcome is that the entropy series drifts smoothly with no decisive leaps, or that any leaps land on state-change days no more often than chance. A clean null is a genuine finding about the method — it is exactly what the "Skeptic's Star" honours — and it is worth as much as a positive.
4. **The instrument check comes first.** "No difference" and "the instrument was not working" are different results and get filed identically if the Phase 0 check is skipped. If the cheap device cannot give a repeatable same-sitting reading, a no-leap result is **VOID, not a null**.
5. **A proxy is a proxy.** The source computes entropy on the **raw pulse waveform shape**. A chest-strap HRV monitor reports entropy on the **RR-interval series** instead — a related but not identical quantity. The card says which path was used and does not let a proxy result be reported as a waveform result.

**Under-promise, stated plainly:** the likely outcome is that the measure is either too noisy to be a usable instrument at home, or stable with no decisive leaps, and the honest verdict is *"the heart-rhythm entropy measure did not show the claimed leaps at home scale in this run."* A clear, replicating positive — a repeatable instrument, decisive leaps, **and** leaps landing on logged state-change days well above chance across a second 30-day series — would be genuinely interesting and would justify the taller follow-up (a pre-registered multi-person trial with a matched control series).

## Why it matters

- It is the queue's **first card whose endpoint is an information-theoretic quantity** — the Shannon entropy of a physiological signal. Every other health card scores a physical quantity (temperature, conductivity, a spin rate) or an operator's hit rate; none scores the *information content* of a body signal.
- It is the queue's **first card on the heart's rhythm as a measurable channel**, and the first to treat the pulse signal as carrying a message rather than as a rate.
- It is the queue's **first card sourced from the Triangulum water-memory / homeopathy research project**, and the first to test a claim whose mechanism (water memory) is **not** what is being measured — the card deliberately separates the measurable claim (entropy leaps) from the unmeasurable one (water carries information).
- It is the queue's **first card whose primary instrument check is test–retest reliability** — it asks whether the cheap device is an instrument at all before asking what it reads.
- It is a **Natural Medicine** card that is purely a measurement — no remedy, no treatment, no health claim — which is the honest way to engage a homeopathy-adjacent source under the child-facing rule.

## Replicability: `home`

- Build/obtain cost: **~$15–70.** Three paths, cheapest first:
  1. **Raw-PPG sensor + microcontroller** (~$15–30) — a MAX30102 breakout on an Arduino/Raspberry Pi streams the raw pulse waveform; a short script computes the entropy. The faithful path (waveform entropy).
  2. **USB pulse oximeter with a data stream** (~$30–40) — e.g. a Contec CMS50D+ class device that exports the waveform; entropy computed from the exported trace.
  3. **Chest-strap HRV monitor + an HRV app** (~$60–70) — a Polar H10-class strap with an app that reports an entropy metric on the RR intervals. **This is a proxy** (RR-interval entropy, not waveform entropy) and must be labelled as one.
- Safety: **low.** A fingertip optical sensor and a chest strap. No voltage beyond a USB port, no chemicals, no heat. Not a medical device and not a diagnostic; the card makes no health claim and the reading is not to be acted on.
- Accessibility: the test needs **30 consecutive days of a 2-minute morning measurement** and a state log. A family can run it at the kitchen table; a single person can run it alone. Two people can run it in parallel to check whether any leap pattern is person-specific.

## Apparatus (Bill of Materials)

- **A pulse-waveform source** — a MAX30102 + microcontroller (~$15–30), a USB pulse oximeter that exports the waveform (~$30–40), or a chest-strap HRV monitor + app (~$60–70; proxy path).
- **A computer** with a short entropy script (the dossier's analysis step; any language), or an HRV app that reports an entropy metric.
- **A log sheet** (paper or a spreadsheet) — one row per day: date, the entropy value, and a state score.
- **A state scale** — a simple 1–5 self-rating of sleep quality, mood and energy, written down *before* the day's entropy value is computed (so the state log cannot be fitted to the number).

## Protocol (pre-registered)

**Phase 0 — instrument check (mandatory).**
1. On one morning, take **three measurements back-to-back** (same sitting, ~2 min apart) and compute the entropy of each. Record the three values. **If the within-morning spread is comparable to the day-to-day spread you later see, the device is not a usable instrument and a no-leap result is VOID, not a null.** (Rule of thumb: the within-morning coefficient of variation should be clearly smaller than the between-day one; record both.)

**Phase 1 — baseline series.**
2. For **30 consecutive days**, take one measurement each morning, at the same time, in the same posture, before coffee or exercise. Compute the entropy value each day.
3. **Before** computing each day's value, write down the day's **state score** (sleep 1–5, mood 1–5, energy 1–5). The state log must be written before the number is known.

**Phase 2 — leap detection.**
4. Compute the **day-to-day absolute change** in entropy for all 29 transitions. Let *M* = the **median** of those 29 changes.
5. Define a **leap** as a day-to-day change larger than **3 × M**. Count the leaps. A leap is a **step change** (the value stays at the new level for ≥ 2 days), not a **spike-and-return** (a single day up and back) — record both counts separately.

**Phase 3 — leap–state correlation.**
6. Mark each day as a **state-change day** (any of the three state scores moved by ≥ 2 from the previous day) or a **steady day**.
7. Build the 2×2 table: leaps vs. state-change days. **The source predicts leaps land on state-change days more often than on steady days.**

**Phase 4 — replication (only if Phase 2 finds ≥ 3 leaps).**
8. Run a **second, independent 30-day series** on the same person and check whether the leap behaviour repeats (a similar leap count, and leaps again landing on state-change days above chance).

## Pass / fail (pre-registered)

- **PASS (instrument):** the Phase 0 within-morning CV is clearly smaller than the between-day CV — the device gives a repeatable reading and is usable as an instrument.
- **PASS (leaps exist):** the 30-day series contains **≥ 3 step-change leaps** (change > 3 × the median day-to-day change, sustained ≥ 2 days) — the series is not smooth drift.
- **PASS (leaps correlate):** leaps land on **state-change days** more often than on steady days (a 2×2 table with a Fisher exact test, one-tailed p < 0.05) — the source's correlation claim holds.
- **PASS (claim refuted — the expected, complete result):** the series shows **no decisive leaps** (0–2, indistinguishable from smooth drift), **or** leaps land on state-change days at chance — the heart-rhythm entropy measure does not show the claimed leaps at home scale (Skeptic's Star).
- **FAIL (void, not a null):** the Phase 0 instrument check fails — the cheap device cannot give a repeatable same-sitting reading — the instrument measures noise.
- **INCONCLUSIVE:** fewer than 30 days; the measurement time or posture was not held constant; the state log was written *after* the entropy value; a device or sensor was changed mid-series; the proxy path (RR-interval entropy) was used without recording it.
- **ARTIFACT:** the leap count tracks a **measurement-schedule change** (a different time of day, a different posture, a change in caffeine or exercise) rather than a state change; the leaps disappear when the measurement time is re-randomised; or the state log correlates with the entropy because both were written at the same moment with knowledge of the other.

## Evidence

- The Phase 0 three back-to-back readings, with their CV.
- The full 30-day table: date, entropy value, the three state scores, and the day-to-day change.
- The leap list: which days, the change size, and whether each was a step or a spike.
- The 2×2 leap-vs-state-change table with the test result.
- The second 30-day series if run.
- A one-paragraph verdict per series: **supports / refutes / inconclusive**, with the numbers.
- Post to the Village "Post to Permies" flow and file a record at `living-library/synthesis/validations/2026-10-07-heart-rhythm-entropy-leap-<attempt>.md`.

## Rights posture

The source translation is **our own** (P2 — publishable). The underlying Bükki article is a third-party work; the card **cites and links** it and reproduces only short attributed quotations. The card makes **no health claim** and instructs no treatment. Any harvested media transcript is **P0 — never publish**.
