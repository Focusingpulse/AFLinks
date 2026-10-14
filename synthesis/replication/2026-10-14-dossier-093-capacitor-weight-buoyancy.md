---
name: Replication Dossier 093 — Buoyancy-Controlled Capacitor Weight Test
description: "Pre-registered replication protocol for the one quantitative modern measurement the electrogravitics revival owns — the 1996 Honda R&D report of a 62 g oil-immersed capacitor losing weight when energised (0.29 ± 0.17 g at 18 kV DC; 0.88 ± 0.63 g at 8 kV AC pulses; max single 1.92 g) — run with the buoyancy systematic the archive itself names and quantifies ('a third of its 62 g is already cancelled before any voltage is applied. A 1.92 g change is a 9.6% change in that buoyant force') removed rather than ignored. Source: synthesis/claim-status-records/brown-electrogravitics-1923-2011.json (status: died) and its retry_now item (2)."
---

# Replication Dossier 093 — Buoyancy-Controlled Capacitor Weight Test

**Quest:** Does a Charged Capacitor Get Lighter? — The Buoyancy-Controlled Weight Test
**Status:** protocol
**Domain:** energy (a claimed coupling between an imposed electric field and a body's weight)
**Tier:** straw (home/homelab, **~$150–400** — a 0.001 g scale, a current-limited high-voltage module, a capacitor, insulating oil, and (optionally) a density-matched bath)
**Created:** 2026-10-14

**Source doc:**
- `living-library/synthesis/claim-status-records/brown-electrogravitics-1923-2011.json` — **status: died**. The record's `lineage` carries the Honda measurement and its numbers; its `contradictions` and `mechanism_note` carry the buoyancy systematic and the E² inversion; its `retry_now` item (2) names **this test** as the unrun one. The record cites **doc:1520046** (Takaaki Musha, *Explanation of Dynamical Biefeld-Brown Effect from the Standpoint of ZPF Field*, 2008, with the Natural Philosophy Wiki's own sourced assessment of the paper) as the document carrying both the Honda numbers and the buoyancy arithmetic.
- **Primary investigation, cited for the mechanism verdict:** **doc:4327** — ONR File 24-185, Willoughby M. Cady, *An Investigation Relative to T. T. Brown*, 15 September 1952.
- **The 1956 industry report, cited for the k-theory the anomaly was meant to serve:** **doc:3563** — *Electro-Gravitics Systems*, Report GRG-013/56, Gravity Research Group, Aviation Studies (International) Ltd., 25 February 1956.
- **Brown's own 1929 statement of the law, cited for the claim's shape:** **doc:4325** — *How I Control Gravitation*, Science & Invention, August 1929, with the complete British Patent 300,311 text.
- **Scout record:** none — this came from the claim-status corpus (`synthesis/claim-status-records/`), which is the engine's named first input for retry candidates.

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-10-14-dossier-093-capacitor-weight-buoyancy` · authored_at `2026-10-14` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## The claim under test (the revival's own best number)

The Biefeld–Brown lineage's central claim is that a charged condenser couples to gravitation — that an imposed electric field changes a body's **weight**, not merely that it pushes air. Brown stated it in 1929 as a law of mutual unidirectional force proportional to the potential difference; the 1955–56 notebooks widened it into separable gravitational and inertial mass (doc:4325, doc:4330).

The mechanism question was settled in 1952 — Cady's ONR investigation concluded that *"All the well documented effects disclosed by Mr. Brown appear to be explained as caused by ionization of the air or oil in which the apparatus is immersed"* and that the thrust *"has its origin in the well-known phenomenon of the electric wind"* (doc:4327). Modern vacuum tests agree: the thrust vanishes with the air.

**What survived that verdict is one measurement, and it is the reason this card exists.** In 1996 the Honda R&D Institute reported that a **62 g dielectric-glass capacitor immersed in insulating oil loses weight when energised** (doc:1520046):

> "They reported ΔW = 0.29 ± 0.17 g for DC and ΔW′ = 0.88 ± 0.63 g for AC pulses at 50 Hz, with a maximum single reduction of 1.92 g, about 3% of the capacitor's weight."

This is the only quantitative modern measurement the revival owns, and every later zero-point-field explanation (Musha 2008) is built to rescue it. It is also the measurement that has **never been replicated with the systematic its own assessor names**.

## The rival explanation, in the archive's own words

The wiki assessment carried with Musha's paper performs the arithmetic the paper omits, and it names the mundane candidate precisely (doc:1520046):

> "the capacitor's volume of 22.7 cm³ immersed in oil of density around 880 kg/m³ displaces about 20 g, so **a third of its 62 g is already cancelled before any voltage is applied. A 1.92 g change is a 9.6% change in that buoyant force**"

and adds the second mechanism:

> "insulating oil in a strong non-uniform field is a **dielectrophoretic pump** whose flow would be strongest in the pulsed case — *That ordering matches the data where the E² law does not*"

**The rival claim, in one sentence:** the weight change is a **fluid effect** — a change in buoyant force and/or a dielectrophoretic circulation of the oil — and it should therefore appear only where there is a fluid to displace and a field gradient to stir it.

## Why this card exists — the gap both sides leave open

The revival's own assessor states the test and states that it has not been run:

> "**Run it in vacuum or in a matched-density bath, with the oil's flow field instrumented, and the anomaly either survives or becomes a flow measurement.**"

That is the whole card. Note what the two claims predict about the **same manipulation**:

| | If the claim is real (field ↔ weight coupling) | If the rival is right (fluid effect) |
|---|---|---|
| **Weight change in oil** | present | present (buoyancy + circulation) |
| **Weight change in a density-matched bath** (buoyancy nulled, fluid retained) | **present** — buoyancy was never the mechanism | **absent** — the buoyant term is what was being read |
| **Scaling with voltage** | ∝ V² (field-squared), the law the ZPF rescue requires | follows the fluid's motion, not V² |
| **Ordering of DC vs pulsed** | DC (higher field) ≥ pulsed | pulsed ≥ DC — "that ordering matches the data where the E² law does not" |

The two rows in bold are the discriminator, and neither has been measured. The archive's own arithmetic already says the honest expectation: a claimed 3% rest-mass effect sits **twenty orders of magnitude** below the field scale at which vacuum nonlinearities would enter (the Honda field is 1.8×10⁷ V/m against a Schwinger field of 1.32×10¹⁸ V/m — "The gap is twenty orders of magnitude", doc:1520046). And the reported effect is itself **within about two standard deviations of zero** at DC (0.29 ± 0.17 g).

**This card does not re-litigate the mechanism.** It measures the one number the revival rests on, with the confound the archive names removed — and either the anomaly survives, or it becomes a flow measurement.

## Apparatus

1. **The article.** A capacitor of known mass and **known displaced volume** — the second matters more than the first. Record: dry mass (g), external volume (cm³, by water displacement), dielectric material.
2. **A 0.001 g balance.** The claimed effect at DC is 0.29 g and the buoyant term is ~20 g; a 0.001 g resolution is required to see either. The balance must be **level, draught-shielded, and warmed up**; record a null run (article on the pan, unpowered, 10 readings) to establish the noise floor **before** any voltage is applied.
3. **A current-limited high-voltage module** (commercial, enclosed, with a bleed resistor). **Start at the lowest voltage the module offers and step up** (e.g. 1 → 3 → 6 kV). The confound test works at any voltage; the claim's magnitude does not need 18 kV to be tested, it needs the *scaling*.
4. **The three media.**
   - **Air** — the no-fluid condition. *Note the confound:* in air a charged asymmetric article can produce ion wind, which is a real force (the sibling card `2026-09-23-sealed-box-electrostatic-thrust.md` tests exactly that). Air is therefore **not** a clean "no fluid" control for a force claim; it is reported, but the discriminator below does not rest on it.
   - **Insulating oil** — the Honda condition (buoyancy ≈ 20 g on the 62 g article; dielectrophoretic circulation possible).
   - **A density-matched bath** — the archive's own condition. A bath tuned so the article's average density matches the liquid's nulls the buoyant term while keeping a fluid present. Sodium polytungstate solutions reach ρ ≈ 1.0–3.1 g/cm³; a saturated zinc-chloride or similar dense solution is the cheap alternative. **Record the bath density and the article's displaced volume** so the residual buoyancy is a computed number, not an assumption.
5. **A flow tracer.** A few grains of fine inert tracer (or a dye thread) in the oil, filmed during the pulsed condition, so "the oil circulates" is an observation and not an inference.
6. **A power/voltage record.** The applied voltage at the terminals, and the module's current limit, logged per trial.

## Protocol (pre-register before trial 1)

1. **Write the pre-registration sheet first** and photograph it: article mass, displaced volume, balance model and resolution, the three media with their measured densities, the voltage steps, the trial count, the order scheme, the operator's name.
2. **Null run.** Article on the pan, unpowered, 10 readings per medium. Record the mean and the standard deviation. **This is the noise floor the whole card is judged against** — a claimed effect smaller than it is not a result.
3. **Buoyancy calibration.** Weigh the article in air, then fully immersed in each medium, unpowered. The difference is the buoyant force. Record it. It should be ≈ 20 g in oil; if it is not, the immersion or the volume is wrong and the run stops here.
4. **The sweep.** For each medium, and for each voltage step: 10 alternating cycles of **uncharged → charged → discharged**, recording the balance reading at each state. Randomise or alternate the order. **Discharge fully between trials** (bleed resistor, then a shorting wand) — a residual charge is a carry-over.
5. **DC and pulsed arms.** Run both — the archive's own tell is that the **pulsed** case is where the ordering matches the fluid explanation and not the E² law. Use the same peak voltage in both arms.
6. **Flow film.** In the oil and bath conditions, film the tracer during the pulsed arm.
7. **Three sessions on different days.** A single session is one measurement, not a result.
8. **Analysis.** For each medium and voltage: the mean charged-minus-uncharged mass change, with its standard deviation, against the null run's noise floor. Then: does the change scale as V²? Does it survive in the density-matched bath? Does the DC/pulsed ordering follow the field or the fluid?

## Pass / fail (pre-registered)

- **PASS — the claim survives (field ↔ weight coupling).** A charged-minus-uncharged mass change that (a) exceeds the null-run noise floor, (b) **appears in the density-matched bath as well as in oil** (i.e. it is not the buoyant term), (c) scales as V² across at least three voltage steps, and (d) reproduces in all three sessions. **This would be the first controlled confirmation in thirty years, and it would be a major result.**
- **PASS — the rival is sufficient (the expected result).** The mass change appears in oil, is **absent or negligible in the density-matched bath**, does not scale as V², and the pulsed ordering follows the tracer's motion. The anomaly becomes a **flow measurement** — which is exactly the outcome the archive's own assessor predicts. **(Skeptic's Star.)**
- **PASS — neither.** No mass change above the noise floor in any medium at any voltage. The Honda result does not reproduce at all; the revival's one quantitative measurement is withdrawn.
- **FAIL:** no null run; no buoyancy calibration; the balance's resolution coarser than 0.001 g; the article's displaced volume unmeasured; the medium's density unmeasured; fewer than 10 cycles per condition; fewer than 3 sessions; the article charged during the uncharged readings; no discharge between trials; the voltage unrecorded.
- **VOID:** the article's dielectric changed or was damaged mid-run; the bath's density drifted; the balance was moved or re-levelled mid-run; the operator changed the protocol mid-run. **A VOID is not a NULL.**

## Honest status of the claim

1. **The mechanism is dead and this card does not revive it.** Cady's 1952 ONR investigation attributed the thrust to ion wind and measured the discriminating tests (cardboard over the outboard wire cut thrust from ~7 g to ~1 g; polarity reversal cut it 7.5 → 3 g) (doc:4327). The modern vacuum tests agree.
2. **The effect is real and this card does not deny it either.** A charged asymmetric capacitor pushes in air — Cady measured it to 7 g in 1952, NASA and ASU measured it in air, and MIT flew a solid-state ionic-wind aircraft in 2018. **The effect survived; the mechanism died.** This card is about the one *weight* measurement, which is a different claim from the thrust.
3. **The revival's number is weak on its own terms.** 0.29 ± 0.17 g at DC is ~1.7σ from zero; the AC/DC ratio runs **opposite** to the field-squared expectation its own rescue theory requires (0.198 predicted, 3.03 measured); and the claimed effect is twenty orders of magnitude below the field scale where the proposed mechanism could act. None of that is a measurement of the confound — it is an argument *about* it.
4. **The confound is quantified by the archive itself and has never been removed.** A third of the article's mass is cancelled by buoyancy before any voltage is applied, and a 1.92 g change is 9.6% of that buoyant force. **No document in the corpus reports the Honda measurement run in a density-matched bath or in vacuum.**
5. **The archive holds no prosecution-side primary document for the mainstream verdict.** There is no NASA or ARL vacuum-test report in the vault and no peer-reviewed ion-wind paper; the resolution is cited from external sources and labelled as such in the record. The card therefore rests on the **Honda number as the revival states it** and on **the archive's own arithmetic**, not on a verdict document it does not hold.

## What would change the verdict

- A **positive** result in the density-matched bath, scaling as V², in three sessions → the record's `retry_now` item (2) is answered in the claim's favour and the lineage graduates from `died` to a live replication programme.
- A **negative** result (oil-only, non-V², tracer-ordered) → the Honda anomaly is formally reclassified as a fluid measurement and the record's contradictions list gains its resolution.
- **Either way the card is worth running**, because the number is the revival's only quantitative result and the confound is arithmetic the archive has already published.
