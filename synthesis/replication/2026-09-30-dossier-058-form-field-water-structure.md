---
name: Dossier 058 — Form-Field Water-Structure Test
description: "Replication dossier for the claim that a hollow paper cylinder changes the light-scattering structure of water held inside it — a 2012 Russian light-scattering experiment (Kovalenko & Shutov, esrae.ru) that attributes the change to a 'stationary torsion field' from spin polarisation in the form. Four arms: the cylinder, a paired control cuvette, a paper-present control beside the cylinder, and an instrument check on a known-different water pair. Home-replicable with a laser pointer and a photodiode, ~$30-80. Health card (drinking-water quality — the source's claimed mechanism for the form effect's health benefit); Natural Medicine mirror."
---

# Dossier 058 — The Form-Field Water-Structure Test

**Status:** protocol
**Domain:** health (drinking-water quality — the water you drink, held in a form; the source's claimed mechanism for the form effect's health benefit)
**Tier:** sand (home, ~$30–80 for a laser pointer, a photodiode, a cuvette and a protractor arm)
**Created:** 2026-09-30
**Source docs:**
- `living-library/translations/2026-09-30-vliyanie-formy-na-strukturu-vody-kovalenko-shutov-ru.md` — Kovalenko V. F. & Shutov S. V., *Влияние формы на структуру воды* (The influence of form on the structure of water) (ru→EN, 17/17 chunks), source https://s.esrae.ru/biofbe/pdf/2012/2/894.pdf — the claim, the full apparatus specification, the measured numbers, and the source's own mechanism.
- `living-library/sources/2026-09-30-scout-a-langs-2.md` § Russian, **find 13** — the scout record (`practical_applicability: flag=true, fields [buildable, reproducible, conceptual]`; the note that "the apparatus is simple and the measurement is physical; the torsion-field interpretation is the contested part").
- `living-library/synthesis/claim-status-records/soviet-torsion-psychotronics-1960s.json` — the torsion-field lineage this claim belongs to (`status: suppressed`; the record's own `retry_now` names tabletop verification as the next step).

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-09-30-form-field-water-structure` · authored_at `2026-09-30` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## The claim (as asserted by the source)

The source's own opening, quoted:

> "It is known [1-4] that bodies of certain geometric forms (pyramid, cylinder, cone, etc.) and proportions possess a property, called the form effect, of creating inside and outside themselves a field of a non-electromagnetic, non-electric, non-magnetic nature (according to [5-7], a torsion field) and, by means of it, of exerting a broad spectrum of influences both on the surrounding environment and on human health. The best known and most widely practised manifestation of this effect in alternative medicine is the health-giving and protective influence of pyramids on the organism [8, 9]. It is assumed that the form field correlates the physical, chemical and biological processes of the organism when there are failures in their normal course. However, the mechanism of this correction has not been established."

The source's stated aim — the experiment exists to explain the health mechanism, not to demonstrate a device:

> "With the aim of clarifying this mechanism, the present work investigates the influence of a cylindrical form on the structural properties of water, which is a common component of all living and non-living objects. On the basis of the data obtained, a possible mechanism of the form effect is proposed."

The source's proposed mechanism, quoted:

> "The proposed mechanism of the field's influence on the structural properties of water consists in the reorientation of the spins of the tetravalent oxygen atoms of clusters that do not correspond to the spin configuration of the field, which, on the one hand, causes the destruction of clusters, and on the other, the formation of new clusters with an ordered spin orientation of the cluster oxygen atoms corresponding to the direction of the field's action."

The source's own health link, quoted:

> "It is assumed that the health-giving influence of form on a sick organism is due to the informational aspect of the structuredness of water and consists in its restructuring within the organism into a spin-ordered state, which ensures the transition of its various systems to normal functioning that eliminates pathology."

**What is being tested, in one sentence:** does a hollow paper cylinder change the light-scattering structure of water held inside it, relative to a paired control cuvette of the same water measured at the same moment — and does the *direction* of any change follow the water's initial state as the source predicts?

## The measurement (the source's own numbers, carried into the card)

The source's apparatus is fully specified and is why this is a home card:

| Element | Source specification |
|---|---|
| Form | hollow cylinder, open ends, **A4 writing paper, H = 297 mm, D = 35 mm** (single layer; 2- and 4-layer variants; a D = 120 mm cylinder for the orientation study) |
| Sample vessel | glass cuvette, **internal D 8 mm, wall 0.75 mm, H 90 mm** |
| Sample positions | along the cylinder axis at **0.1H, 0.3H, 0.5H, 0.7H, 0.9H** (positions 1–5) |
| Light source | **semiconductor laser, λ = 0.65 µm, beam 3 mm, power < 1 mW — a laser pointer** |
| Measurement | scattering indicatrix **I(θ)**, forward half-plane, **4° ≤ θ ≤ 90°, step 2°** |
| Temperature | T = 300 K |
| Holding time | **t_v = 30 min** (main series) |
| Cluster classes | super-large r > 2.5 µm; large 0.95–2.5 µm; medium 0.4–0.95 µm; small r < 0.4 µm |
| Control | a second cuvette of the same water, "located at a distance of several metres from the cylinder" |

The source's headline result (Table 1), reproduced exactly:

| Initial stage | Control IΣ (rel. units) | After 30 min in the cylinder | Source's figure |
|---|---|---|---|
| I — [H₂O] = [(H₂O)₆] | 20555 | 13310 | **65 %** |
| II — [H₂O] > [(H₂O)₆] | 12514 | 17546 | **140 %** |
| III — [H₂O] >> [(H₂O)₆] | 10700 | 15750 | **147 %** |

The source's own reading of its three numbers, quoted:

> "the influence of the form on the structure of water of stage I manifested itself in a decrease in the degree of polydispersity, which led to a decrease in the total concentration of clusters by ~ 35% … which is the cause of the decrease in NΣ and **the approach of the structure to stage III**."

> "The influence of the form on the structure of water of stage III led to an increase in the concentration of clusters of all sizes present in the initial sample … which increased their total concentration by ~ 47% and **brought the structure, in terms of the ensemble and sizes of clusters, closer to stage I**."

## Honest status of the claim

**The archive holds the claim and no home test of it.** A grep for `scatter`, `form field`, `эффект формы` and `torsion` across `living-library/synthesis/quest-queue/` and `living-library/synthesis/replication/` returns **no card and no dossier** on light scattering from water. The queue's form cards test **space** (011 form waves) and **objects** (027, 033, 050 — pyramids on blades, food, a capacitor); **none tests a form's effect on water.** The queue's water cards measure vortex devices (001, 004, 031), the EZ layer (009), conductivity (022), retention (037), composition (054) — **none measures water's optical/cluster structure.**

Five things the card must say out loud:

1. **The source's three numbers all move toward the same value, and that is the whole problem.** Stage I falls 20555 → 13310; stage II rises 12514 → 17546; stage III rises 10700 → 15750. **Every arm converges on ≈ 15,000.** The source reads this convergence as evidence *for* the form ("the approach of the structure to stage III", "closer to stage I"). But **convergence toward a common value is also exactly what a formless relaxation looks like** — water settling, temperature equilibrating, aggregates dissociating, or plain measurement noise regressing to the mean. The source's data cannot tell those apart, because of point 2.
2. **The source's percentages are computed against the control's INITIAL value, not the control's final value.** Stage I's "65 %" is 13310 ÷ 20555 — the treated sample's *end* value over the *control's start* value. **If the control water also drifted during the same 30 minutes, the source's figure conflates the form's action with the water's own settling.** The card's primary metric is therefore **R = IΣ(treated, final) ÷ IΣ(control, final)**, both measured at the same moment — which cancels any drift the two cuvettes share. This is the one methodological fix the card exists to make.
3. **A sign-flip is the claim, and a sign-flip is also what regression to the mean produces.** The source's prediction is that the *direction* of the change depends on the initial state. That is a genuinely falsifiable prediction — and it is also the signature of an instrument with noise. **The paired control is what separates them:** if R is repeatably ≠ 1, the form did something the control did not; if R ≈ 1, the convergence was the water's own.
4. **The source's own control is weak, and the card says so.** The control cuvette sat "several metres away" — inside the room, in the same air, but also **potentially inside the claimed field**, since the source's own claim is that the form acts "inside and outside" itself. The card adds **arm C (a paper-present control beside the cylinder at the same height)** so that "the paper is in the room" is separated from "the water is enclosed by the form".
5. **A scattering measurement that has not been shown to resolve a known difference is not a measurement.** Water scatters very weakly. **The instrument check (arm D — a known-different water pair) is mandatory:** if the method cannot separate two waters that are known to differ (e.g. distilled vs. tap, or tap vs. tap + a trace of milk), then a no-change result is **void, not a null** — "no difference" and "the instrument could not have seen a difference" are different results and get filed identically if the check is skipped.

**Under-promise, stated plainly:** the likely outcome is that R ≈ 1 — the treated and control cuvettes drift together over 30 minutes, and the source's headline percentages turn out to be the water's own convergence read against a control that was drifting too. **That is a complete, useful result** — it files the first home test of a 2012 claim the archive has held untested, and it retries a torsion-field lineage the archive already marks `suppressed`. A repeatable R ≠ 1 in the pre-registered direction would be genuinely surprising and would justify the taller follow-up (the layer and position series, which the source reports as non-uniform).

## Why it matters

- It is the queue's **first card on the form effect applied to water** — the form cards so far act on space (011) and objects (027, 033, 050); none acts on water.
- It is the queue's **first card whose endpoint is a light-scattering measurement** — an optical, physical quantity (cluster size, concentration, polydispersity) rather than a dowsing response, a temperature or a germination count.
- It is the queue's **first card whose source reports a sign-flipping, initial-state-dependent response** — the direction is the claim, so the card must pre-classify the sample before it can be falsified at all.
- It is the queue's **first card that retries the torsion-field lineage** via `soviet-torsion-psychotronics-1960s.json` — the record whose own `retry_now` asks for tabletop verification, delivered here as a household-scale version of one of its named experiments.
- It carries a **checkable number from the source** (the 65 %/140 %/147 % table) that a family can compare its own R against, so even a null leaves a documented replication attempt in the record.
- It is genuinely **home-scale**: a laser pointer, a glass cuvette, a sheet of paper, a photodiode and a protractor.

## Replicability: `home`

- Build/obtain cost: **~$30–80** — a red laser pointer (λ ≈ 650 nm, < 1 mW; **note the source's 0.65 µm is 650 nm, so an ordinary red pointer is the correct source**), a glass cuvette or a small flat-sided glass vial (a 10 mm spectrophotometer cuvette is ideal and cheap; a square glass jar works), a sheet of A4 paper and glue, a photodiode or light-dependent resistor with a multimeter (or a phone camera in manual mode as the detector), a protractor and a cardboard arm to swing the detector, a dark cloth or a dark room.
- Safety: **low, with one real rule.** A laser pointer is a Class 2/3R device: **never look into the beam, never point it at anyone, and keep the beam below eye level and enclosed by the dark cloth.** Do not use a laser above 1 mW. The water is ordinary drinking water; there are no chemicals and no mains wiring. **The real hazard is over-reading a null as a health verdict** — the card is a physics test of a cited claim, not a health assessment, and the card says so.
- Accessibility: an afternoon to build the cylinder, the cuvette holder and the detector arm; about an hour per session; three sessions on three days.

## Apparatus (Bill of Materials)

- **A red laser pointer** — λ ≈ 650 nm, output < 1 mW, beam ≈ 3 mm. Record the class and the wavelength on the label.
- **A glass cuvette** — a 10 mm path-length spectrophotometer cuvette (square, flat sides) is the closest match to the source's 8 mm cylindrical cuvette and is far easier to align; a small square glass jar is an acceptable substitute. **Use the same vessel for every arm.**
- **A sheet of A4 paper and glue** — to make the cylinder (H = 297 mm, D = 35 mm, open ends). Make one single-layer cylinder; the 2- and 4-layer variants are the optional extension.
- **A photodiode or light-dependent resistor + multimeter** — the detector. A phone camera in manual mode (fixed ISO and shutter) is an acceptable substitute; record which you used.
- **A protractor and a cardboard arm** — to swing the detector around the cuvette in known angular steps. Mark 4°, 10°, 20°, 30°, 45°, 60°, 90° at minimum.
- **A dark cloth or a dark room** — the measurement cannot be made in daylight.
- **A thermometer and a timer** — for the room temperature and the holding time.
- **A notebook** — for the pre-registration sheet and every reading.

## Protocol (four-arm light-scattering test, pre-registered)

**Phase 1 — instrument check and noise floor.**
1. **Write the pre-registration sheet before running anything:** the laser and detector used, the vessel, the angles measured, the holding time, the number of sessions, the classification rule (step 5) and the criteria below. Photograph it.
2. **Establish the method's noise floor.** Fill the cuvette with the session's water and take **10 repeated readings at a fixed angle (e.g. 20°)** without moving anything. Record the mean and the standard deviation. **This SD is the noise floor** against which every arm is scored.
3. **Run the instrument check (arm D).** Measure the same fixed angle on a **known-different pair** — distilled water versus tap water, or tap water versus tap water with one drop of milk in a litre. **If the method cannot separate the pair by clearly more than the noise floor, the method cannot see a structural difference and the run is void — not a null.**

**Phase 2 — prepare the sample and classify it.**
4. **Draw one batch of water** (the same source for the whole session — the source used a spring; tap water is fine, but use the same tap all three sessions). Split it into **three identical cuvettes**.
5. **Measure the baseline indicatrix of each cuvette** (the same angles, the same detector, the same room temperature) and compute the **baseline integral intensity IΣ** (the sum of the readings across angles, in arbitrary but consistent units). **Classify the batch by its baseline IΣ against the range you have observed:** a **low-cluster** sample (low IΣ, few small clusters) or a **high-cluster** sample (high IΣ, many small clusters). **Write the predicted direction on the sheet before any holding:** low-cluster → the source predicts an **increase** (R > 1); high-cluster → the source predicts a **decrease** (R < 1). This pre-registration is the card — without it the sign-flip claim cannot be falsified.

**Phase 3 — hold, blind.**
6. **Arm A — inside the cylinder.** Place cuvette A on the axis of the paper cylinder at **0.9H** (the source's position 5, where the single-layer effect was largest) on a small stand so it does not touch the paper.
7. **Arm B — the paired control.** Place cuvette B **several metres away**, same height, same room, uncovered. (This is the source's own control.)
8. **Arm C — the paper-present control.** Place cuvette C **beside the cylinder at the same height, outside it** — same paper in the same room, but not enclosed. (This is the card's addition; it separates "the form" from "the paper".)
9. **Have someone else code the three cuvettes** (A/B/C → 1/2/3 in a shuffled order) so the measurer does not know which is which. Record the code sheet separately.
10. **Hold for 30 minutes**, then measure all three cuvettes at the same angles, in the same session, at the same room temperature.

**Phase 4 — score.**
11. **Compute IΣ for each cuvette at the end of the hold.** The primary metric is **R = IΣ(A, final) ÷ IΣ(B, final)** — treated over paired control, both at the same moment. Report **R_C = IΣ(A, final) ÷ IΣ(C, final)** as the secondary metric.
12. **Also compute the source's own metric** (IΣ(A, final) ÷ IΣ(B, baseline)) so the family can compare directly against the source's 65 %/140 %/147 % table. **Report both, and label which is which.**
13. **Repeat the whole set on at least 3 separate days**, with a fresh batch each day, and record the classification and the predicted direction each time.

## Pass / fail (pre-registered)

- **PASS (the claim survives — surprising, needs follow-up):** **R** differs from 1 by more than the noise floor, **in the pre-registered direction for the sample's class**, in **≥ 2 of 3 sessions**, with the instrument check (arm D) passing. Report as a surprising result needing the layer and position series before any conclusion.
- **PASS (the claim is refuted — the expected, complete result):** **R ≈ 1** (within the noise floor) in ≥ 2 of 3 sessions — the treated cuvette and the paired control drift together, and the source's headline percentages are the water's own convergence read against a control that was drifting too. Reported as the expected result, not a failure (Skeptic's Star).
- **FAIL:** R differs from 1 but **not in the pre-registered direction** for the sample's class — the change is real but it is not structure-dependent as the source claims.
- **INCONCLUSIVE:** the instrument check (arm D) did not separate the known-different pair; the baseline could not be classified; fewer than 3 sessions; the arms were not measured in the same session; the room temperature changed by more than a degree between the baseline and the final reading; or the control cuvette sat within a metre of the cylinder.
- **ARTIFACT:** R tracks the **room temperature**, the **time of day**, or the water's own aging rather than the arm; the treated and control cuvettes drift in the **same direction** (a common attractor, not a form effect); the reading follows the **operator's expectation** (unblinded); the reading follows the cuvette's **position in the room** rather than its enclosure; or the "control" cuvette was itself disturbed (moved, warmed, or handled).

## Evidence

Photo of the built cylinder, cuvette holder and detector arm with a ruler showing H = 297 mm and D = 35 mm + the pre-registration sheet (laser, detector, angles, holding time, classification rule, predicted direction, criteria) photographed before the first trial + the noise-floor log (10 readings → mean and SD) + the instrument-check log on the known-different pair + the baseline indicatrix per cuvette + the code sheet and the shuffled order + the final indicatrix per cuvette with the room temperature + the R and R_C tables with the source's own metric shown separately for comparison + the session classification and predicted direction for each of the ≥ 3 days + the void/artifact checks reported whether or not they void the run.

## Confounds (named in advance)

- **Convergence toward a common value — the central confound.** The source's three stages (20555, 12514, 10700) all move toward ≈ 15,000. **A form field and a formless relaxation look identical in that data.** The paired control measured **at the same moment** is the only thing that separates them; that is why R uses the control's *final* value, not its initial one.
- **Regression to the mean.** A sign-flipping response is the claim **and** the signature of a noisy instrument. Pre-classifying the sample and pre-registering the direction is what makes the sign-flip a test rather than a post-hoc story.
- **The water's own aging.** The source reports that its source water changed over **weeks** ("with the passage of time, reckoned in weeks, the ensemble of clusters … decreased"). **Use one batch per session, split across the arms, and never carry water between sessions.**
- **Temperature.** Scattering and cluster populations are temperature-sensitive. **Record the room temperature at every reading and reject a session whose temperature moved more than a degree between baseline and final.**
- **The control's position.** The source's control sat "several metres away" — possibly inside the claimed field, since the source claims the form acts outside itself too. **Arm C (paper present, water not enclosed) is the card's answer**, and the card asks whether arm B and arm C agree.
- **The detector.** A phone camera's auto-exposure will silently normalise the very difference being measured. **Use manual mode with fixed settings, or a photodiode with a multimeter.**
- **The vessel.** A cylindrical cuvette and a square one scatter differently. **Use the same vessel for every arm and every session.**
- **The health over-read.** A null does not mean a form cannot affect health, and a positive does not mean it can. **This card tests one physical link in the source's proposed chain — form → water structure — and says so.**

## Verdict rules

R ≠ 1 repeatably, in the pre-registered direction, with the instrument check passing → **the claim survives** (surprising; needs the layer and position series). R ≈ 1 in ≥ 2 of 3 sessions → **the claim is refuted at home** (the expected, complete result — the source's percentages are the water's own convergence against a drifting control). R ≠ 1 but in the wrong direction → **the change is real but not structure-dependent as claimed.** Instrument check failed, baseline unclassifiable, fewer than 3 sessions, or the arms not run in the same session → **inconclusive, not a refutation.**
