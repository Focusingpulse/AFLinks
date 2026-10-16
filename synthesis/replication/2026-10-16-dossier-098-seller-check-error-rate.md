---
name: Replication Dossier 098 — Install-and-Re-Check Test
description: "Pre-registered replication protocol for the check a seller uses to demonstrate a field-neutralising device — the before/after pendulum reading (the Finnish 'earth-radiation estimi', Yle 2019). The card measures the demonstration's OWN false-positive rate first (how often 'it went quiet' happens with nothing installed), then compares nothing / the device / a matched decoy blind. Source: translations/2026-10-16-maasateilyn-estin-tyottomat-kaavi-yle-fi.md. Tests the seller's verification method ONLY; it makes no claim about whether earth radiation exists and no health claim of any kind."
---

# Replication Dossier 098 — Install-and-Re-Check Test

**Quest:** Does the Check Know Its Own Error Rate? — The Install-and-Re-Check Test
**Status:** protocol
**Domain:** community (shared-infra knowledge — how a household checks a device it is offered, before it buys)
**Tier:** sand (home, **~$0–30** — a pendulum or a pair of rods, eight identical posts, two copper coils, sand)
**Created:** 2026-10-16

**Source docs:**
- `living-library/translations/2026-10-16-maasateilyn-estin-tyottomat-kaavi-yle-fi.md` — **Veli-Pekka Hämäläinen**, *"Työttömät pantiin kokoamaan 'maasäteilyn estimiä' — valtiokin rahoittaa erikoista keksintöä, jonka tiede totesi huuhaaksi jo 1980-luvulla"* (The unemployed were set to assembling an 'earth-radiation detector' — even the state funds a strange invention that science dismissed as nonsense back in the 1980s), **Yle** (Finnish national broadcaster), 21 January 2019, https://yle.fi/a/3-10603767, fi→EN 3 chunks, complete. **This is the source of the demonstration protocol the card tests, and of the counter-evidence that decides the design.**
- `living-library/translations/2026-10-16-vesisuoni-water-vein-finnish-wikipedia-fi.md` — *Vesisuoni* (Water vein), Finnish Wikipedia, https://fi.wikipedia.org/wiki/Vesisuoni — the encyclopedic counter-integrity account; carries the **Helsinki Kaisaniemi** experiment (Matti Wäre, hydrological office: several dozen dowsers mapped the area's water veins and **all of them were different**) and the **1985 University of Oulu** study (prof. Onni Kari-Koskinen: dowsers marked vein locations driving one road, and **the return-trip marks did not coincide with the outward marks**).
- `living-library/sources/2026-10-16-scout-b-langs-2.md` — Polyglot Scout B, run 2026-10-16, **find #12** (the Yle feature; `practical_applicability: FALSE — conceptual/journalistic`) and **find #11** (the Finnish Wikipedia article). Both URLs probed HTTP 200 that run.
- **Counter-integrity companion already held by the archive:** the University of Oulu **1976–1983** `maasäteilyraportti` (the report the Yle feature summarises). The card cites the Yle summary of it and does not re-analyse it.

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-10-16-dossier-098-seller-check-error-rate` · authored_at `2026-10-16` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## The claim under test

The Yle feature describes a device — the **"earth-radiation estimi"** (detector/neutraliser) built by **Risto Skottman** of Siilinjärvi, Finland: **a set of four plastic posts** placed in the corners of a room, claimed to cut off the harmful "earth radiation" (maasäteily) arising from the crossing points of underground water veins. The seller does **not** disclose what is inside the posts; the source records the traditional construction as **"copper plates or coils"**.

**The claim is not the card's subject. The seller's CHECK is.** The source records the demonstration in full:

> *"In his hand he holds a pendulum, which swings gently at the end of a thin chain. Above the living-room table the pendulum begins to spin more strongly in a circle. At this spot, according to Skottman, lies the crossing point of the water veins that cause earth radiation."*
> *"When Skottman has placed the plastic posts in the corners of the room, he walks with his pendulum again to the supposed crossing point of the water veins. This time the pendulum no longer moves. In Skottman's view, that means the harmful earth radiation has been removed."*

So the seller's verification method is a **three-step, single-operator, before/after reading with the same instrument**:

1. find the spot (the instrument reads **present**);
2. install the device;
3. re-read the same spot (the instrument reads **absent**) — and call that "removed".

**That method is what this card tests.** It is a **signal-cessation** endpoint: the seller's evidence for the device working is the *disappearance* of his own reading.

## Why the check's own error rate is the thing to measure

A signal-cessation check has a failure mode that no amount of careful reading can remove: **the instrument's reading can go quiet on its own.** If the operator's reading drifts, or is intermittent, or responds to expectation, then "it went quiet after I installed it" and "it went quiet because my reading is not stable" are **the same observation**.

The source supplies the finding that makes this concrete, from the **University of Oulu 1976–1983** study, which the Yle feature summarises:

> *"In the experiments it was noticed, among other things, that the earth-radiation seekers were not able to find the same earth-radiation points on different occasions, nor a flowing water vein beneath the ground. A radiation researcher who worked by drawing lots achieved equally good results. Likewise, the S-equalizer that protects against earth radiation worked only when the test subject could see whether it was on or not."*

and the Finnish Wikipedia's **1985 Oulu** study:

> *"In the study a certain road was driven and the places of the veins found by the dowsers were marked. The same was repeated on the return journey, and the veins found on the return journey were not in the same places as the veins of the outward journey."*

**The same operator, re-walking the same ground minutes later, did not reproduce their own reading.** That is precisely the condition the seller's check depends on and never measures.

**So the card's primary endpoint is the check's own false-positive rate**: with **nothing installed at all**, how often does the operator's re-reading report that the signal has gone quiet? If that rate is high, the seller's demonstration cannot distinguish a device from an empty room.

## What the card is NOT

- **Not a test of whether earth radiation exists.** That question has its own literature and its own cards; this card does not touch it.
- **Not a health claim.** No participant reports symptoms, sleep, pain or wellbeing. The only thing recorded is the operator's instrument reading and their confidence in it.
- **Not a test of the seller, the company, or the Finnish authorities.** The card tests a *method*.
- **Not a claim that the device does nothing.** The card's design can return "the check survives" — that is a stated PASS path.

## The rival explanations the design must separate

| explanation | prediction in this design |
|---|---|
| **The device works** (the seller's claim) | the "gone quiet" rate is **high for the device**, **low for nothing**, **low for the decoy** |
| **The reading is unstable** (the Oulu 1985 finding) | the "gone quiet" rate with **nothing installed** is **not lower** than with the device — the check is uninformative |
| **The operator's expectation** (the S-equalizer finding) | the rate tracks what the operator **believes** is in the room, so a **matched decoy** produces the same rate as the device |
| **Drift / time** | the calls cluster in time rather than in condition — visible as a run of "quiet" calls regardless of what was set |

The **matched decoy** is the arm that separates "the device works" from "the operator expects it to". It is the arm nobody runs, and it is the reason the card needs eight posts rather than four.

## Protocol (pre-registered)

**1. Pre-register, in writing, before the first reading.** Photograph a sheet carrying: the room; the spot-finding rule; the reading rule in the operator's own words; the three conditions; the trial count; the randomisation method; the sealed list; the scoring rule; the pass/fail thresholds; the operator's name; the coder's name; the instrument. **The thresholds may not change after any data exists.**

**2. Apparatus.**
- **The instrument:** the operator's own pendulum or rod pair — whatever they would use to run the check.
- **The device set (D):** four identical posts, ~30–50 cm, each containing a **copper coil** — the traditional construction the source names (*"traditionally those who believe in earth radiation have removed the radiation, for example, with copper plates or coils"*). **The card tests the class claim, not the seller's product**, whose contents are undisclosed.
- **The decoy set (X):** four posts **identical in size, colour and external appearance**, filled with **sand** to match the coil's mass.
- **The nothing condition (N):** no posts at all.
- *If the household already owns a field-neutralising device of any kind, it may be used as set D; the decoy must still be built to match it.*

**3. People.** An **operator** (the person who would install the device — ideally the person who believes in it, because that is who runs the demonstration in real life) and a **coder** (who sets the condition, never reads, and records the truth). The operator must not see the coder set the condition.

**4. Locate the spot.** The operator walks the room with the instrument and marks the **one spot where the reading is strongest** — tape it to the floor and photograph it. **Do not move it for the rest of the run.** *If no spot can be found anywhere in the home, stop: that is a VOID, not a null.*

**5. The reading rule (fixed before trial 1).** Write down, in the operator's own words, what counts as "the reading is present" and "the reading has gone quiet" at the taped spot — e.g. *"the pendulum rotates steadily"* vs *"the pendulum hangs still or only sways"*. **The rule may not be changed after trial 1.**

**6. The trial.** For each trial:
   - the operator **leaves the room**;
   - the coder sets the condition at random from the sealed list (N, D or X), out of the operator's sight, and clears it afterwards;
   - the operator **re-enters**, walks to the taped spot, and calls **"still reads"** or **"gone quiet"**;
   - the operator states **confidence 0–10**;
   - the coder records the truth and the call.

**7. Trial count and order.** **At least 20 trials per condition** (≥60 total). The order is drawn from a **sealed randomised list** prepared before trial 1. The coder does not deviate from the list.

**8. Second day.** Repeat the whole series on a **second day with a fresh sealed list**. A result that does not reproduce is not a result.

**9. Primary endpoint.** The **"gone quiet" rate in the NOTHING condition (N)** — *the check's own false-positive rate.*

**10. Secondary endpoints.** The "gone quiet" rate in **D** and in **X**; the **D-minus-N** and **D-minus-X** differences; the operator's mean confidence per condition; and whether the calls cluster in **time** rather than in condition.

**11. Chance model.** For a three-condition blind design the naive chance rate is 1/3, but the operator's calling bias is what matters: **compute the empirical baseline by re-scoring the recorded calls against 1,000 shuffled condition orders** drawn from the same condition mix, and report the observed rates' percentiles. Do not assume uniformity.

## Pass/fail

- **PASS (the check is uninformative — the expected, ordinary result):** the **"gone quiet" rate in N is not distinguishable from the rates in D and X** (all three inside the central band of the shuffled baseline; the D-minus-N and D-minus-X differences are within the noise floor). **The seller's check reports success about as often with nothing installed as with the device, so it cannot tell a device from an empty post.** This is a complete result and earns the **Skeptic's Star**.
- **PASS (the check survives — surprising):** the **D rate is significantly higher than BOTH the N rate and the X rate**, beyond the shuffled baseline's 95th percentile, **and reproduces on the second day**. A positive would mean the operator's own check discriminates the device from a matched decoy under blinding — which no published account of this device class has shown.
- **FAIL:** the operator knew the condition on any trial; the coder also read; the taped spot was moved or re-located; fewer than 20 trials per condition; the reading rule or thresholds were changed after data existed; the operator saw the condition being set.
- **VOID (not a null):** no spot could be located in the home at all; the operator changed instrument mid-run; the room was materially altered mid-run (furniture moved, a wall opened); the operator dropped out mid-series.
- **ARTIFACT:** the calls track the operator's **confidence** rather than the condition; the calls **cluster in time** (a run of "quiet" calls spanning several conditions); the operator reports that they inferred the condition from the coder's behaviour (sound, timing, footsteps).

## Evidence

Photo of the pre-registration sheet (room, spot-finding rule, reading rule, three conditions, trial count, randomisation, scoring rule, thresholds, operator, coder, instrument) taken before trial 1 + the room plan with the taped spot marked and photographed + photos of the device set and the matched decoy set side by side (showing they are externally identical) + the sealed randomised list photographed **sealed** and then **opened** after the series + the full trial log (trial number, condition set, operator's call, confidence 0–10, time of day, any deviation) + the three "gone quiet" rates with the 1,000-shuffle baseline histogram and the observed percentiles stated + the D-minus-N and D-minus-X differences + the time-clustering plot + the second-day series and its rates + a one-paragraph verdict (the check is uninformative / the check survives / inconclusive) with the numbers and the trial counts shown.

## Honesty notes (carried into the card)

1. **The seller's own position, quoted, belongs in the card.** The Kaavi project leader, Tapani Tirkkonen, told Yle: *"There are many who have received help from this. If it is only because one's own head believes [that the estimi removes earth radiation], it does not bother me at all."* A device whose seller does not need it to work is exactly the case where the buyer's own check has to be trustworthy.
2. **The patent office's own position, quoted, belongs in the card.** Yle records the patent engineer Olli-Pekka Sievänen: *"If it is known that the invention does not work, the patent is not granted. But if the matter remains unclear and the other conditions of the application are met, it often leads to a situation where the patent is granted. A patent does not guarantee that the invention works exactly as the inventor presents."* **A patent number is not evidence that a device works**, and the card says so.
3. **The university group's own conclusion, quoted, belongs in the card.** *"Non-functioning devices that do not remove non-existent earth radiation are amulets, objects whose protective effect is based on belief, the University of Oulu research group summarized as its final conclusion."*
4. **The card is not a health card and must not become one.** No symptom, sleep, pain or wellbeing measure appears anywhere in the protocol, the endpoints, the pass/fail or the evidence list. If a family wants to test whether a device changes how they feel, that is a different card with a different (and stricter) standard.
5. **The card is not an accusation.** It tests a method, not a company or a country. The same method is used by sellers and by well-meaning practitioners everywhere, and the card's own PASS path allows the check to survive.
6. **The expected result is the ordinary one.** The Oulu 1985 finding is that the same operator did not reproduce their own reading on the same road minutes later. On that evidence the most likely outcome is that the N rate is not lower than the D rate.

## Why this is a Community Living card

Its **domain is community** (the rotation's next field) and its **guild complement is Community Living** — *"Group coherence / radionics — group-field experiments; shared subtle-energy"* — the **emptiest community-adjacent mirror in the queue**, carrying one card (the Kolisko group steigbild). The fit is the *shared subtle-energy* half of that seed: the device is a **shared subtle-energy device installed in a shared dwelling**, and the check is run by **the group that shares it** — one member operating, one coding — because the claim is about the household, not about the operator alone. The engine's own rule is to fill the emptiest mirror, and the alternative community-adjacent mirrors are far fuller (Community 11, Earthworks 7, Nest 5).
