---
name: Quest Card — Coil-Geometry Water Treatment Test: Does the Winding Shape Change the Water?
description: "Aetherforce-branded quest card testing the Indonesian coil-geometry water-treatment claim — that water flowed through a coil-wrapped pipe comes out with a changed pH and electrical conductivity, and that the size of the change depends on the coil's WINDING GEOMETRY (toroid vs Rodin vs caduceus) at matched drive. The card builds four identical pipes (one plain, three coiled), calibrates the conductivity meter against a known standard first, and adds the two controls the source's own design omitted — a plain pipe (flow/degassing) and an unpowered coil (material). Water domain (water treatment — the treated water's own measured physical properties); Plumbing & Hot Water mirror (6th card)."
---

# ⚡ Aetherforce — Plumbing & Hot Water

**Guild:** Aetherforce — Plumbing & Hot Water
**Quest Line:** ⚡ Aetherforce · Plumbing & Hot Water complement
**Tier:** sand
**Domain:** water (water treatment — the treated water's own measured physical properties)
**Status:** proposed
**Created:** 2026-10-10

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-10-10-coil-geometry-water-treatment` · authored_at `2026-10-10` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural"],
  name: "Aetherforce — Plumbing & Hot Water",
  desc: "A pipe wrapped in wire is sold as a way to improve water: run the water through the coil, and it comes out 'structured', 'energised', 'living'. One university physics department in Indonesia tested this properly — three pipes, three different coil windings (a toroid, a Rodin coil, a caduceus coil), the same field on each — and measured what came out: pH, electrical conductivity, temperature. The water changed. And the three windings changed it by different amounts, which is the interesting part: if the shape of the winding matters, then the thing doing the work is the field's geometry, not just 'a magnet'. What the study could not see is the simplest explanation of all, because its comparison water never went through a pipe at all — and water moving through a pipe sheds carbon dioxide and rises in pH all by itself, with no field anywhere. This quest builds the four pipes the study should have had: one plain, three coiled, the same current through each, and a conductivity meter checked against a known standard before anything is measured. The plain pipe is the whole experiment. If water through a plain pipe changes as much as water through a coil, the field did nothing. If the three windings separate from each other and from the plain pipe, and it is not just the water getting warmer, then something real is happening and it is worth a second household. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "sand",
  quest: [
    "Coil-Geometry Water Treatment Test — Does the Winding Shape Change the Water?",
    "Build four identical pipe sections (same material, bore and length): one plain, and three wrapped with coils matched for turns and wire gauge — a toroid, a Rodin coil, and a caduceus coil. Feed any one coil at a time from the same low-voltage DC supply at the same measured current. First calibrate the conductivity meter against a known standard and record the standard's reading; if it does not read within tolerance, stop — the run is void. Then measure the standing water (no flow) for pH, conductivity and temperature. Run the plain pipe first, for a fixed flush time; then a coiled pipe with the coil connected but unpowered; then each of the three geometries powered, at the same current and flush time. Repeat at least 5 times, interleaving the arms within each run, and log the water temperature at every reading. Measurable outcome: pH, electrical conductivity (µS/cm) and water temperature for each arm, as mean and scatter across N >= 5 runs, plus the difference from the standing sample and from the PLAIN-PIPE arm, and the correlation of the conductivity change with water temperature. Target: the three geometries differ from each other and from the plain pipe, the unpowered coil shows nothing, and the change is present at matched temperature. A plain pipe that reproduces the change = the effect is degassing, not the field, and that is a complete result.",
    ["Science", "Chemistry", "Engineering"],
    "💧"
  ],
  source_doc: "translations/2026-10-10-em-field-water-physical-properties-plant-growth-purworini-id.md — full English translation of Fitri Purworini & Avin Ainur Fitrianingsih, Jurnal Neutrino Vol. 7 No. 2 (April 2015), Department of Physics, Universitas Islam Negeri Maulana Malik Ibrahim Malang; scout record sources/2026-10-10-scout-a-langs-2.md (find #9) whose Practicality assessment flags it as buildable/reproducible",
  source_url: "https://focusingpulse.github.io/AFLinks",
  dossier: "living-library/synthesis/replication/2026-10-10-dossier-079-coil-geometry-water.md",
  pass_fail: "PASS (claim supported at home scale): the treated water differs from the PLAIN-PIPE control in pH and/or conductivity, AND the three coil geometries differ from each other reproducibly, AND the unpowered coil shows no comparable change, AND the change is reproducible across N >= 5 runs, AND the change is not explained by the water temperature | REFUTED: the plain pipe reproduces the change (flow/degassing — the leading ordinary explanation), OR the unpowered coil reproduces it (coil material/former), OR the change tracks the water temperature (resistive heating), OR the three geometries are indistinguishable from each other (the geometry — the thing the card is about — does nothing) | INCONCLUSIVE: changes are present but sit inside the run-to-run scatter of the control arms | VOID: the conductivity meter was not calibrated against a known standard; the water source changed mid-run; the coils were not matched for turns or drive current; readings were taken before the fixed flush completed — a VOID is not a NULL",
  evidence: "Photo of the pre-registration sheet (pipe material and bore, each coil's geometry and turn count, the drive current, the flush time, the sample volume, the meters and their calibration state, the scoring rule, N, the run order) taken before the build + the conductivity-meter calibration record showing the standard's reading + the raw pH, conductivity and water-temperature readings for the standing sample, the plain pipe, the unpowered coil, and each of the three powered geometries + the N >= 5 interleaved repeat runs + photographs of the four pipes and the three windings, the drive circuit, and the meters + (optional) the matched-pot plant arm with the source's own null in mind + a one-paragraph verdict (supports / refutes / inconclusive) with the numbers and the plain-pipe comparison shown"
}
```

---

## Source Documentation

- **Primary (the archive translation):** `living-library/translations/2026-10-10-em-field-water-physical-properties-plant-growth-purworini-id.md` — the full English translation of **Fitri Purworini & Avin Ainur Fitrianingsih**, *"The Effect of Applying an Electromagnetic Field on the Physical Properties of Water and its Implications for Plant Growth Rate"*, **Jurnal Neutrino Vol. 7 No. 2, April 2015**, Department of Physics, Faculty of Science and Technology, Universitas Islam Negeri Maulana Malik Ibrahim Malang (Indonesia). Original: https://ejournal.uin-malang.ac.id/index.php/NEUTRINO/article/view/2988/4929
- **The seed record:** `living-library/sources/2026-10-10-scout-a-langs-2.md` — Polyglot Scout A, 2026-10-10 (file 2 of 2), **find #9**. Its **Practicality assessment** is the filter, and it flags this record: *"buildable/reproducible — the three coil-pipe geometries and the pre/post-test control design (groups A/B/C/D × 5 sub-samples) are fully specified; the measured water parameters are concrete and repeatable."* ⚠ The record's own rights posture: the translation is **P0 — never publish**; the assessment is our own (**P2**).
- **The source's reported numbers (as claims):** pH — PDAM 6.84 → toroid 7.49 / Rodin 7.48 / caduceus 7.42; conductivity — PDAM 1.86 → toroid 3.24 / Rodin 2.72 / caduceus 3.61 µmho/cm; temperature — PDAM 25.18 °C → treated ~27.1–27.7 °C; field strengths — toroid 18.97 mT, caduceus 18.76 mT, Rodin 18.20/18.68 mT. Plant arm — **no effect on chilli**; eggplant 0.933 cm/week under toroid-treated water. Statistics — pH `F = 30.374, Sig. = .000` (ANOVA/Duncan); conductivity `Prob>F = 0.0004`.
- **The archive's own counterweight, carried inside the card:** the reported baseline conductivity (1.86 µS/cm) is **~100× below typical municipal tap water**, so the absolute numbers cannot be trusted and a calibrated baseline is a hard entry condition; and the source's comparison water never passed through a pipe, so its design **cannot separate the field from the flow** — the plain-pipe arm is the card's addition.
- **Replication Dossier:** `living-library/synthesis/replication/2026-10-10-dossier-079-coil-geometry-water.md`
- **Vault:** https://focusingpulse.github.io/AFLinks — search "water structure", "electromagnetic water", "Rodin coil", "caduceus coil", "toroid", "magnetic water treatment"
- **Aetherforce Reference:** search "water vortex", "living water", "structured water", or "magnetic water" on https://www.aetherforce.energy

---

## Rubric Justification

| Criterion | Assessment |
|-----------|------------|
| **Practical** | YES — a named apparatus (four identical pipes; three matched coils in three named geometries; a low-voltage DC drive; a pH meter, a conductivity meter and a thermometer) with a named procedure (calibrate, baseline, plain pipe, unpowered coil, three powered geometries, N interleaved repeats) and a measurable outcome (pH, conductivity in µS/cm and water temperature per arm, with scatter and the plain-pipe comparison). Not pure theory. |
| **Replicable** | YES — home, ~$60-150. Pipe, magnet wire, a battery and resistor, a pH meter, a conductivity/TDS meter, a thermometer, and a calibration standard. No mains work, no lab. |
| **Relevant** | YES — Water domain: treating the water a household actually draws, measured on the water itself. It complements the Plumbing & Hot Water guild, whose complement in the mirror map is *Water vortex / living water*. |
| **Honest** | YES — framed as a TEST, not an endorsement. The card states plainly that the source's baseline conductivity is physically implausible for tap water, that its design omitted the plain-pipe control, and that the temperature rise is unexplained. It names the ordinary mechanisms (flow/degassing, coil material, resistive heating, meter scale, water-source drift) and requires the control that separates each. Clean FAIL and VOID paths; the expected result is a null. |
| **Linked** | YES — the archive translation (with its scout record and card-eligible assessment), the original journal article, the source's own numbers as claims, the archive's counterweight written into the card, a pre-registered replication dossier, and the Vault + Aetherforce search pointers. |

**Mirror choice, stated:** the card's **domain is water** (the rotation's next field), and its **guild complement is Plumbing & Hot Water** — *Water vortex / living water*, the guild that already holds the Wasserwirbler, the EZ-water card, the Piccardi P test, the MVP Vortex Motor and the electrolyzed-water fractions. This is its **6th card**. The alternative mirror was **Oddball** (*cross-field bridges / suppressed-science re-try candidates*), which is emptier (1 card) and is arguably a fit — the Rodin and caduceus windings come from the torsion/radionics instrument family and are here tested inside a mainstream physics department, which is a genuine cross-field bridge. Plumbing & Hot Water was chosen because the card's apparatus is an **inline device in a water line** and its endpoint is the water itself, which is that guild's whole subject. Under-promise noted: the card is emitted because the apparatus is cheap, the protocol is fully specified, and the endpoint is countable — **not** because the claim is believed.

---

## What makes it the queue's first of its kind

- **The first card whose independent variable is the coil WINDING GEOMETRY** — toroid vs Rodin vs caduceus at matched drive. Every prior electromagnetism-on-water card varies the field's *presence* or *strength* (the magnetized-irrigation card varies a passive magnet in or out); none varies its *shape*.
- **The first card resting on a mainstream university physics department's controlled study** with formal statistics (ANOVA in MATLAB and SPSS, Duncan follow-up). Prior cards rest on practitioner accounts, patents, or self-published reports.
- **The first card whose primary endpoint is the treated water's own measured physical properties** — pH, conductivity, temperature — rather than a downstream biological, device, or perceptual effect.
- **The first card whose key control is a plain pipe** — separating "flow alone" from "field". Flowing water through a pipe degasses CO₂ and raises pH by itself, so without this arm the effect is unassignable; the source's own design does not have it.
- **The first card that carries a required instrument calibration as a hard entry condition** — because the source's baseline reading (1.86 µS/cm) is ~100× below typical tap water, an uncalibrated meter is the single most likely explanation for the whole reported effect.

---

## The honest framing (the spine of the card)

The card tests a claim, not a tradition. The coil-treated-water lineage is not being asked to prove a mechanism — it is being asked whether the water that comes out of the pipe is measurably different from the water that went in, and whether the *shape of the winding* is what makes the difference.

Three things the card keeps in front of the family:

1. **The source is a real controlled study, and it reports its own null.** A university physics department ran the experiment with statistics and found **no effect on chilli plants**; only the eggplant arm moved. That honesty is why the card exists at all.
2. **The source's numbers contain a scale problem, and the card fixes it first.** A tap-water conductivity of 1.86 µS/cm is not tap water. The card's first act is to calibrate the meter against a known standard — because if the baseline is wrong, every difference computed from it is wrong too.
3. **The plain pipe is the whole experiment.** The source compared treated water to water that never entered a pipe. The card compares treated water to water that went through the *same pipe with no coil* — and that single arm decides whether the field did anything at all.

**Under-promise, stated plainly:** the likely outcome is that the **plain pipe reproduces most or all of the change**, that the conductivity shift partly tracks the water's temperature, and that the three geometries do not separate cleanly — i.e. that what the study measured was largely **flow and heat, not field geometry**. That is the honest verdict, and the card is designed to reach it cleanly.

---

## Rights posture

The translation is our own rendering of a publicly posted open-access journal article; the English rendering is a derivative work and is **P0 — never publish**. The scout record is our own analysis (**P2**). The card **cites and links**; it reproduces only short attributed quotations.
