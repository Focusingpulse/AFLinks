---
name: Dossier 043 — Cold Machine Vortex-Cooling Test
description: "Replication dossier for the Schauberger 'cold machine' (冷机) cooling claim: water forced into an inward-spiral vortex through a curved tube, then jetted through a fine orifice, cools — and the vortex shape itself contributes cooling beyond plain evaporation. Home-replicable, gravity-fed, ~$40-120."
---

# Dossier 043 — The Cold Machine Vortex-Cooling Test

**Status:** protocol
**Domain:** food (cold storage — preserving food without grid power or fuel)
**Tier:** straw (home/homelab-scale, ~$40–120)
**Created:** 2026-09-26
**Source docs:**
- `living-library/translations/2026-09-26-water-based-cold-machine-zh.md` — full EN translation of *百年神秘「水基冷机」* (The Century-Old Mysterious Water-Based Cold Machine), tech-works.cn, source material by E Yusong (鄂雨松). Carries the six-step working principle, the vortex-tube + micro-orifice construction, and — unusually — the article's own list of the claim's fatal flaws.
- `living-library/sources/2026-08-26-scout-a-fr-es-zh.md` find 4 — the scout entry that flagged the source `conceptual [buildable]`.
- Lineage context: `living-library/synthesis/claim-status-records/schauberger-vortex-repulsine-1951.json` (the Schauberger vortex/implosion claim record, `retry_now` pointing at dossiers 001 and 004).

---

## The claim (as asserted by the source)

The "cold machine" is a sealed water loop — annular array of **vortex tubes**, an egg-shaped shell, **1 mm micro-jet orifices**, a reversed turbine, a central water collector, an external radiator. The article's own step-by-step:

1. **Vortex tubes.** Clean water is distributed from the central collector into specially curved "antelope-horn" tubes; inside them the flow is forced into **inward spiral vortices**, producing "fluid self-focusing of energy and a drastic reduction in flow resistance."
2. **Micro-orifice injection.** The high-speed vortex flow jets out through ~1 mm nozzles; velocity spikes, pressure plummets, and the water undergoes **adiabatic expansion plus a liquid-to-gas phase change**, absorbing heat and forming a cold source.
3. **Atmospheric heat replenishment** — the machine's interior stays cold, so ambient heat flows in.
4. **Water strikes the reversed turbine** → mechanical/electrical output.
5. **Vapour condenses in the radiator and returns** — a sealed loop.
6. A biomimetic vortex-ring field for propulsion.

The article then states the headline claim in one sentence: *"a natural power device that uses water as its circulating medium, creates low temperature through vortex spiraling plus micro-orifice phase change, harvests the atmosphere's greenhouse waste heat and converts it into power and electricity, simultaneously cools the atmosphere, and runs in a sealed perpetual loop."*

**The source's own honesty — and this is why the card exists.** The article does not hide the problem. It devotes a section to "the hard flaws that keep the cold machine outside modern science today" and lists them plainly:

- *"It crosses the red line of conservation of energy"* — the "one unit in, ten units out" framing *"violates classical physics, is perpetual-motion fantasy, and cannot stand at present."*
- *"It violates the second law of thermodynamics."*
- *"Its core concepts lack formal scientific support"* — negative friction, pipes crossing and auto-generating electricity, self-rotation in resonance with the cosmic electric field: *"no mathematical models and no repeatable experiments."*
- Engineering materials and control technology cannot keep up.
- Disciplinary walls divide it.

And its own summary of what is actually reproducible: *"the fluid effects, the cooling structures, and the water-cycle logic of the cold machine can be partially reproduced; but complete high-power output, crewed flight, and self-sustaining energy circulation have never received formal scientific verification or engineering realization."*

**So the card tests the part the source itself says is reproducible — the cooling — and ignores the part it says is false — the energy.**

### Splitting the cooling claim into its two halves

The cooling claim is really two claims, and they are not equally extraordinary:

| Half | Status | Testable at home? |
|---|---|---|
| **A. Flash evaporation at the orifice cools water.** Water jetted through a fine orifice into a low-pressure chamber evaporates; evaporation absorbs latent heat; the remaining water and the chamber cool. | **Ordinary physics.** This is how every evaporative cooler, swamp cooler and spray pond works. | Yes — but it is not the claim worth testing; it passes trivially. |
| **B. The vortex shape itself contributes cooling** — Schauberger's "spontaneous cooling" from inward-spiral flow, the "drastic reduction in flow resistance" step. | **Extraordinary and unreplicated.** Mainstream fluid mechanics predicts the *opposite* sign: a coiled tube generates secondary (Dean) vortices that **increase** viscous dissipation, so the water should come out slightly *warmer* than from a straight tube of equal developed length. | Yes — and this is the discriminating test. |

**The card tests B, not A.** A rig that only asks "does it get cold?" measures evaporation and proves nothing about the vortex. The comparison must be **vortex arm vs straight arm at the same orifice and the same flow**, where evaporation is present in both arms and cancels.

### Honest status of the claim

Unreplicated, and the source's own over-unity framing is false. The cooling half is a mix of ordinary physics (evaporation) and an extraordinary sub-claim (vortex-contributed cooling) that has never been isolated with modern instrumentation — the Schauberger claim record's own `late_confirmation` field says exactly this: *"No mainstream physics program has tested Schauberger's vortex claims with calibrated instrumentation."*

**Under-promise, stated plainly:** a home rig with a bucket, a copper coil and kitchen thermometers will not resolve a micro-degree effect. It **can** resolve a large one — a 0.5–1 °C arm-to-arm difference at matched flow, consistent across sessions. If the effect is real at the magnitude the lineage implies, a family will see it. If it is not, the family will see **parity**, and parity is the honest negative the archive wants: it would mean the cold machine's cooling is ordinary evaporative cooling wearing a vortex costume.

## Why it matters

This is the **cooling half of the entire Schauberger vortex lineage**, and it is the half that has never been isolated. Dossier 001 (Wasserwirbler) measures a temperature differential across a hyperbolic funnel — but with **no orifice** and **no straight-arm control**, so its temperature endpoint cannot separate vortex from geometry from ambient. Dossier 024 (spiral pipe) measures **flow and head**, with temperature only as a noted side-claim. **No card in the queue isolates the vortex's contribution to cooling against a matched straight-arm control** — and that is the single comparison the "cold machine" claim lives or dies on.

It is also a real education: a family that runs this learns latent heat, flash evaporation, flow matching, and what a controlled comparison actually costs — core off-grid food-and-energy literacy. And the practical outcome is a genuine homesteading capability: **a cold store that runs on gravity and water, with no fuel and no grid.**

## Replicability: `home`

- Build cost: **~$40–120** (a head tank/tote, two copper tubes of equal ID and developed length, a pre-coiled copper coil, fittings, two 1 mm orifice caps/nozzles, a small insulated cooler box, three 0.1 °C thermometers, a bucket and a stopwatch).
- Safety: **no mains, no chemicals, no combustion, no heat.** This is gravity-fed water at household pressures. Ordinary care only: lift the tank safely, don't let a full tote tip, keep the spray chamber's lid vented so pressure cannot build, and keep the outlet clear.
- Accessibility: an afternoon to build the two arms; the four alternating sessions are the measurement. Kids can hold the stopwatch, read the thermometers and log the numbers.

## Apparatus (Bill of Materials)

- **1 head tank** — a 20–60 L bucket or tote, mounted so the water surface sits a **fixed, measured height** above the orifice (1.0–1.5 m gives a usable jet; more head = finer spray and a stronger signal). Mark the start level.
- **Tube set (same inner diameter and same *developed* length across arms — this is what makes the comparison fair):**
  - **A — vortex arm:** copper tube, 8–10 mm ID × 60–80 cm developed length, **coiled** around a cylinder (a pre-coiled copper coil is ideal). Record coil diameter and pitch.
  - **B — straight arm:** straight copper tube, **same ID and same developed length** (60–80 cm).
  - **C — vortex-no-orifice arm (optional, sharper):** the same coil as A but with an **open end** instead of the orifice. This isolates the vortex *alone*, with no flash evaporation at all.
- **Orifice:** a 1 mm drilled cap or a fine nozzle fitted to the end of arms A and B. **The same orifice is used on both arms** — this is the control that makes the test discriminating.
- **Insulation:** wrap **both** tube arms in the same insulation. The coil has a larger surface area than the straight tube, so an uninsulated coil exchanges more heat with the room — a confound that would masquerade as a vortex effect.
- **Spray chamber (the cold store):** a small insulated box (5–10 L cooler) with a vented lid, holding a **sealed 500 mL water jar** (the thing being cooled) and a thermometer. The jar is the food-storage analogue; a family can put a real item in it later.
- **Thermometers:** three, 0.1 °C resolution — **inlet water**, **chamber air**, **jar water** — plus an **ambient** reading.
- **Flow control:** a small valve or clamp on each arm so flow can be matched between arms.
- **Bucket** of known volume + **stopwatch** (flow rate), and a **phone camera** for evidence.

## Protocol (matched-flow, alternating arms)

1. **Fill and settle.** Fill the tank to the mark and let the water sit until it is at ambient temperature (an hour is plenty). Record ambient.
2. **One arm at a time**, alternating **A, B, A, B, …** so drift, tank level and room temperature cancel out. Change nothing but the tube.
3. **Match the flow.** With the valve, set each arm to the same flow rate — target e.g. **1.0 L/min, matched within ±10 %**. Measure flow with the bucket and stopwatch *at the start and the end of every run*; an unmatched flow invalidates the session (see VOID).
4. **Run 30 minutes.** Log **inlet water temp, chamber air temp, jar temp, ambient temp and flow rate** at **t = 0, 5, 10, 20 and 30 min**.
5. **Repeat.** Four alternating sessions per arm (A,B,A,B,A,B,A,B). Record every number, including the bad runs.
6. **Optional arm C** (vortex, no orifice): run it the same way. If the vortex claim is real, C should show cooling with **no** evaporation present — the cleanest possible signal. If C is flat while A and B both cool, the cooling is evaporation and nothing else.
7. **Note the spray.** Photograph the spray pattern of each arm. A swirl at the orifice can atomize the jet more finely, which increases evaporation — a **real** mechanism, but not the claimed one. Note it if you see it.

## Pass / fail criteria (pre-registered)

- **PASS (the vortex contributes cooling):** at matched flow (±10 %), the **vortex arm A is ≥0.5 °C colder than the straight arm B** in the chamber at t = 30 min, with the **same sign in ≥3 of 4 sessions**, and the difference survives both arms being insulated identically with ambient logged and stable. → The cold machine's cooling claim has a vortex component beyond evaporation. Report the magnitude honestly.
- **PASS (cleaner, if arm C is run):** arm C (vortex, no orifice) cools measurably below ambient. → The vortex alone produces cooling with no evaporation present. This is the strong form of the claim.
- **FAIL:** A and B within **±0.3 °C** at t = 30 min in ≥3 of 4 sessions at matched flow. → **The vortex shape contributes no cooling beyond the orifice's evaporation; the cold machine's cooling is ordinary evaporative cooling.** A complete and valuable result — **Skeptic's Star**. It would mean the cooling half of the vortex lineage is not reproducible with simple apparatus.
- **INCONCLUSIVE:** run-to-run spread within one arm exceeds 0.5 °C, or flow cannot be held steady, or ambient swings dominate.
- **VOID:** flow cannot be matched within ±10 %, or ambient swings more than 2 °C during a session, or the chamber leaks so freely that both arms simply track ambient. Report the resolution achieved and the control required, **not** a verdict. A rig that cannot hold its controls has not tested anything.
- **ARTIFACT (must be ruled out before any PASS is claimed):** the A–B difference tracks the **coil's larger surface area** (test: insulate both arms identically and re-run), or disappears when both arms' water is brought to the same temperature before the orifice, or is fully explained by a **finer spray** from the swirl (photograph the sprays; a visibly finer mist on arm A is the alternate mechanism, not the claimed one).

Report the **practical outcome** (does the chamber hold below ambient, and by how much) **separately** from the **claim outcome** (is A colder than B). The first is a homesteading capability and will almost certainly be positive — evaporation works. The second is the claim, and it is the one that can fail.

## What would change the verdict

- A modern instrumented rerun (calibrated thermocouples, a mass-flow-matched pump, and a droplet-size measurement at the orifice) that isolates the vortex term would move the claim out of "unreplicated." A home result should be read as a **screen**, not a calorimetric measurement.
- A clear null at home, repeated by several households, is strong evidence that the "spontaneous vortex cooling" is an artifact of evaporation and measurement — worth publishing as loudly as a positive.
- A positive result on arm C (vortex, no orifice) would be the first isolated modern observation of the Schauberger cooling claim, and would justify a second-stage instrumented dossier.

## Feedback loop

- Log every attempt (including failures and abandoned rigs) in the results log below.
- ≥2 independent attempts → update status to `replicated` / `refuted` / `inconclusive`; cross-link to the Schauberger claim record (`schauberger-vortex-repulsine-1951`) and to dossiers 001, 004, 024.
- Share: Replication Yard, Permies post, Aetherforce energy / water strands.

## Results log

- *(none yet — open for the first replicator.)*
