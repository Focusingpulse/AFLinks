---
name: Replication Dossier 079 — Coil-Geometry Water Treatment Test
description: "Pre-registered replication protocol for the Indonesian coil-geometry water-treatment claim (Purworini & Fitrianingsih, Jurnal Neutrino 7(2), April 2015): does flowing water through a coil-wrapped pipe change the water's pH and electrical conductivity, and does the size of the change depend on the coil's WINDING GEOMETRY (toroid vs Rodin vs caduceus) at matched drive? Home tier, ~$60-150. Includes the plain-pipe and unpowered-coil controls the source's own design omitted, and the required conductivity-meter calibration the source's implausible baseline forces."
---

# Replication Dossier 079 — Coil-Geometry Water Treatment Test

**Quest:** Coil-Geometry Water Treatment Test — Does the Winding Shape Change the Water?
**Status:** protocol
**Domain:** water (water treatment — the treated water's own measured physical properties)
**Tier:** sand (home, ~$60-150)
**Created:** 2026-10-10

**Source docs:**
- `living-library/translations/2026-10-10-em-field-water-physical-properties-plant-growth-purworini-id.md` — the full English translation of **Fitri Purworini & Avin Ainur Fitrianingsih**, *"The Effect of Applying an Electromagnetic Field on the Physical Properties of Water and its Implications for Plant Growth Rate"*, **Jurnal Neutrino Vol. 7 No. 2, April 2015** (Department of Physics, Universitas Islam Negeri Maulana Malik Ibrahim Malang, Indonesia). Original: https://ejournal.uin-malang.ac.id/index.php/NEUTRINO/article/view/2988/4929
- `living-library/sources/2026-10-10-scout-a-langs-2.md` — Polyglot Scout A, 2026-10-10 (file 2 of 2), **find #9**. Its **Practicality assessment** is the filter, and it flags this record: *"buildable/reproducible — the three coil-pipe geometries and the pre/post-test control design (groups A/B/C/D × 5 sub-samples) are fully specified; the measured water parameters are concrete and repeatable."*

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-10-10-dossier-079-coil-geometry-water` · authored_at `2026-10-10` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## The claim (as asserted by the source)

The study's own abstract states the result directly:

> "The results showed an average pH value of PDAM water of 6.84, toroidal-pipe-treated water 7.49, Rodin pipe 7.48 and caduceus pipe 7.42. … The average electrical conductivity of toroidal-pipe-treated water was 3.24 μmho/cm, Rodin pipe 2.72 μmho/cm, caduceus pipe 3.61 μmho/cm, and for PDAM water the electrical conductivity value was 1.86 μmho/cm."

And the mechanism the authors offer:

> "In relation to magnetic field strength, the toroidal pipe produces a magnetic field strength of 18.97 mT. The magnetic field in the toroidal pipe is the largest compared with the other pipes. The magnitude of that field strength can affect the pH of the treated water so that it can improve water quality."

Reported field strengths: **toroid 18.97 mT · caduceus 18.76 mT · Rodin 18.20 mT (one side) / 18.68 mT (other side)**.

**What is being tested, in one sentence:** does water that has flowed through a coil-wrapped pipe come out with a different **pH and electrical conductivity** than water that flowed through the same pipe with no coil — and does the size of that difference depend on the coil's **winding geometry**?

## Honest status of the claim

**This source is unusual in the queue and its status is genuinely mixed.** It is a **mainstream university physics department's controlled study**, published with formal statistics (ANOVA in MATLAB and SPSS, with a Duncan follow-up test; the pH effect is `F = 30.374, Sig. = .000` and the conductivity effect `Prob>F = 0.0004`), and it reports its own **null** alongside its positive: *"The application of an electromagnetic field did not affect the growth rate of chilli plants watered with the treated water."* Only the eggplant arm moved (0.933 cm/week under toroid-treated water).

Against that, three things must be said plainly, and the card carries all three:

1. **The baseline conductivity is physically implausible.** The reported PDAM (municipal tap water) conductivity is **1.86 µmho/cm = 1.86 µS/cm**. Real municipal tap water is typically **200–800 µS/cm** — roughly **100–400× higher**. A reading of 1.86 µS/cm is closer to deionised water than to tap water. Either the instrument was mis-scaled, the units are wrong, or the sample was not what it was said to be. **Consequence: the absolute numbers cannot be trusted, and the family must establish its own baseline with a calibrated meter before any comparison means anything.** This is a hard entry condition, not a footnote.
2. **The source's control omitted the obvious alternative.** The untreated comparison was PDAM water that had *not* been flowed through a pipe at all. So the design cannot separate "the field" from "**flowing through a pipe**" — and flowing water through a pipe degasses CO₂ and re-equilibrates with air, which **raises pH** on its own. A plain pipe with no coil is the control that separates them, and the source does not have it. The card adds it.
3. **Temperature is a confound and is also an unexplained result.** The treated water ran ~1.6–2.6 °C warmer than the untreated sample (25.18 °C untreated; treated inlets/outlets 26.80–27.74 °C). Conductivity is temperature-dependent at roughly **2 %/°C**, so ~2 °C explains only ~4 % of the reported rise — **not** the 46–94 % reported. But the temperature rise itself is unexplained and must be logged, because a coil carrying current is a heat source.

**The ordinary mechanisms that must be excluded before the claim is interesting:**

| Ordinary mechanism | What it predicts | The control that separates it |
|---|---|---|
| **Flow / degassing / aeration** | pH rises because CO₂ leaves the water as it moves and contacts air — nothing to do with any field | the **plain pipe** (identical pipe, identical flow rate, no coil) |
| **Coil material / galvanic contact** | the wire, former, or pipe metal leaches ions, raising conductivity | the **unpowered coil** (identical coil, no current) and a blank run with the same pipe |
| **Resistive heating** | the coil warms the water; conductivity and pH both drift with temperature | the **ambient and water temperature log at every reading**, and a run at matched temperature |
| **Instrument scale / calibration error** | the reported change is an artefact of an uncalibrated or mis-scaled meter | **calibrate the conductivity meter against a known standard** and report the standard's reading before any sample |
| **Water-source drift** | the mains water itself changed between runs | draw all samples from one batch, or run all arms on the same day, interleaved |

**So the honest position is:** the claim is measurable, the apparatus is cheap and buildable, the source is a real controlled study — and the source's own numbers contain a scale problem and a missing control that a family can fix in an afternoon. **The card's first job is to establish a trustworthy baseline**, not to chase the effect.

| | Ordinary (the change is an artefact) | Claim supported at home scale |
|---|---|---|
| **Plain pipe (no coil)** | reproduces the pH/conductivity change | no change vs the standing sample |
| **Unpowered coil** | reproduces the change | no change |
| **Temperature** | the change tracks the water temperature | the change is present at matched temperature |
| **Three geometries** | all three are indistinguishable from each other | toroid / Rodin / caduceus differ from each other, reproducibly |
| **Repeat runs** | scatter exceeds the difference | the difference exceeds the scatter |

## Why it matters

- It is the queue's **first card whose independent variable is the coil WINDING GEOMETRY** — toroid vs Rodin vs caduceus at matched drive. Every prior electromagnetism-on-water card varies the field's *presence* or *strength*; none varies its *shape*.
- It is the queue's **first card resting on a mainstream university physics department's controlled study** with formal statistics — prior cards rest on practitioner accounts, patents, or self-published reports.
- It is the queue's **first card whose primary endpoint is the treated water's own measured physical properties** (pH, conductivity, temperature) rather than a downstream biological, device, or perceptual effect.
- It is the queue's **first card whose key control is a plain pipe** — separating "flow alone" from "field" — a control the source's own design omitted.
- It is the queue's **first card that carries a required instrument calibration as a hard entry condition**, because the source's baseline reading is physically implausible for the water it claims to have used.

## Replicability: `home`

- Build/obtain cost: **~$60-150** — four identical pipe sections (~$10), magnet wire for three coils (~$15-25), a low-voltage DC supply or battery + resistor (~$15-30), a digital pH meter (~$15-25), a conductivity/TDS meter (~$15-30), a thermometer (~$5), and a conductivity calibration standard (~$10). No mains work, no lab.
- Safety: **low.** Low-voltage DC only. Do not drive the coils from mains. Do not drink the treated samples (the conductivity rise, if real, means dissolved material).
- Accessibility: any home with a tap and a table.

## Apparatus (Bill of Materials)

- **Four identical pipe sections** — same material, same bore, same length (e.g. 20 cm of ½″ PVC or PE). One is the **plain pipe** (control); three carry coils.
- **Three coils, matched for turns and wire gauge** — wound around the three pipe sections in three geometries: a **toroid** (wire wound as a closed ring around the pipe axis), a **Rodin coil** (the published Rodin winding — a star/torus pattern), and a **caduceus coil** (two counter-rotating helices crossing on opposite sides of the pipe). The source's own field readings were toroid 18.97 mT, caduceus 18.76 mT, Rodin 18.20/18.68 mT — so the three are close in strength, which is what makes the geometry comparison meaningful.
- **A matched drive** — one low-voltage DC supply (or battery + resistor) feeding any one coil at a time, at a **measured, identical current** for every arm.
- **A digital pH meter** and a **conductivity / TDS meter** — the two primary instruments.
- **A conductivity calibration standard** (or a freshly mixed KCl standard) — mandatory; see the hard condition below.
- **A thermometer** — measure the water temperature at every reading.
- **A stopwatch** — a fixed flush time per sample.
- **Sample jars** — identical, rinsed with the sample before filling.

## Protocol (pre-registered)

1. **Pre-register, before measuring.** Write down: the pipe material and bore, the coil geometry of each arm and its turn count, the drive current, the flush time, the sample volume, the meters used and their calibration state, the scoring rule, N runs, and the run order. Photograph the sheet.
2. **Calibrate the conductivity meter against a known standard** and record the standard's reading. If the meter cannot read the standard within its stated tolerance, the run is VOID — the source's own baseline is ~100× below typical tap water, so an uncalibrated meter is the single most likely explanation for the whole effect.
3. **Establish the baseline.** Fill a jar with the standing water (no flow) and measure pH, conductivity and temperature. This is the reference.
4. **Run the plain-pipe control FIRST.** Flow water through the pipe with **no coil** for the fixed flush time; measure pH, conductivity and temperature. This is the arm that catches degassing — the effect the source's design could not see.
5. **Run the unpowered-coil control.** Flow water through a coil-wrapped pipe with the coil **connected but no current**; measure. This catches the coil material and former.
6. **Run each geometry, powered.** Flow through the toroid, the Rodin and the caduceus pipes in turn, at the **same current and the same flush time**; measure pH, conductivity and temperature for each.
7. **Repeat N ≥ 5 times**, interleaving the arms within each run so that the water source and the room temperature are shared across arms. Log the water temperature at every reading.
8. **Optional secondary arm (the source's own plant result).** Water matched pots of a fast crop with the plain-pipe water and the toroid-pipe water and compare height growth. The source found **no** chilli effect and a modest eggplant effect (0.933 cm/week); a null here is the expected result and is a complete one.
9. **Compute.** For each arm: pH, conductivity and temperature, as the mean and scatter across N runs; the difference from the standing baseline and from the **plain-pipe** arm; and the correlation of the conductivity change with the water temperature.
10. **Post.** Photo of the pre-registration sheet, the four pipes and the three windings, the meters and the calibration record, the raw readings, and a one-paragraph verdict.

## Pass / fail (pre-registered)

- **PASS (claim supported at home scale):** the treated water differs from the **plain-pipe** control in pH and/or conductivity, AND the **three geometries differ from each other** reproducibly, AND the **unpowered coil** shows no comparable change, AND the change is reproducible across N ≥ 5 runs, AND the change is **not explained by the water temperature**.
- **REFUTED:** the **plain pipe reproduces the change** (flow/degassing — the leading ordinary explanation), OR the **unpowered coil reproduces it** (material/former), OR the change **tracks the water temperature**, OR the **three geometries are indistinguishable from each other** (i.e. the geometry — the thing the card is about — does nothing).
- **INCONCLUSIVE:** changes are present but sit inside the run-to-run scatter of the control arms.
- **VOID:** the conductivity meter was not calibrated against a standard; the water source changed mid-run; the coils were not matched for turns or drive current; readings were taken before the fixed flush completed. A VOID is not a NULL.

## Independent-variable discipline

The one variable is **the coil's winding geometry** — with the drive current, the pipe, the flow time and the water held fixed. The **plain pipe** is the control that catches flow alone; the **unpowered coil** catches the coil material; the **temperature log** catches resistive heating; the **interleaved run order** catches a drifting water source. If the three geometries come out the same, the card has answered its question: the geometry — the thing the source's headline rests on — does nothing.

## What a result would mean

- **Plain pipe flat, unpowered coil flat, geometries differ, temperature uncorrelated** → the effect is real at home scale and is not the ordinary mechanisms. The honest follow-up is a blinded run (the operator does not know which pipe is which) and a second household.
- **Plain pipe reproduces the change** → the effect is degassing, not the field. A complete and useful result — and the one the source's missing control left open.
- **Change tracks temperature** → resistive heating. Also complete.
- **No change above scatter at all** → the claim does not reproduce at home scale with this apparatus. A complete result (Skeptic's Star), and the honest one the card expects.

## Rights posture

The translation is our own rendering of a publicly posted journal article; the English rendering is a derivative work and is **P0 — never publish**. The scout record is our own analysis (**P2**). The card **cites and links**; it reproduces only short attributed quotations.
