---
name: Dossier 088 — Lattice Energy Converter (LEC) Home Replication
description: "Home/homelab replication of the Lattice Energy Converter: a two-tube gas-metal device whose surface-activated working electrode (iron- or palladium-plated, hydrogen-loaded) self-initiates a spontaneous voltage and conducts current across an insulating gas gap. Tier straw, ~$80-220. The card's whole design move is the control the field already ran and most claims lack: an IDENTICAL device with an UNPLATED working electrode, which the archive's best replication (Di Stefano, ICCF-24 2022) measured at 0.01 mV and ~0 pA against the active device's ~300 mV and ~136 uA. Endpoint is the FORCED CURRENT (the primary anomaly), not the open-circuit voltage (a secondary, electrode-potential effect)."
---

# Dossier 088 — Lattice Energy Converter (LEC) Home Replication

**Status:** protocol ready
**Domain:** energy / condensed-matter nuclear science (gas-metal device — the LENR-adjacent "lattice" claim class)
**Tier:** straw (home/homelab, ~$80–220)
**Source:** `sources/scout-report-2026-10-10-1200.md` (ICCF-27 program, item 18: "Gordon LEC reproducibility") + the lenr-canr / JCMNS lane (`sources/2026-10-12-scout-growth-1815.md`)
**Created:** 2026-10-13

---

## Source lineage

- **F. E. Gordon & H. J. Whitehouse (InovL, Inc., USA)** — the inventors. *"Lattice Energy Converter,"* **JCMNS 35(1):30–48 (2022)**, doi **10.70923/001c.72583**; *"LEC II: Iron Hydrogen Host Material,"* **JCMNS 36(1):1–24 (2022)**; *"Scaling up the LEC,"* **JCMNS 38(1):225–234 (2024)**, doi **10.70923/001c.124959**; *"Progress in Understanding and Scaling Up the LEC,"* **JCMNS 39:14–35 (2025)**, doi **10.70923/001c.134029**. Over 100 cells tested; months-long runs into a DVM at 1–10 MΩ.
- **Independent replications:** **J.-P. Biberian** (Aix-Marseille, 2020–21; 300→500 mV, later 540→740 mV); **A. Erickson** (Los Alamos, 23 Nov 2020; 0.115 V in air → 0.170 V hot); **A. Di Stefano** (Prysmian, Italy; ICCF-24, 2022 — **the control campaign**); **Alan Smith** (UK, electrolytic activation); **H. Zhang & S. Chen** (Qiuran Laboratory, China; **JCMNS 39:241–248, 2025**, doi **10.70923/001c.134009** — Fe/Ni/Cu plating, H₂/D₂/air, "highly reproducible", no radiation above background).
- **High-temperature extension:** **Biberian, Michel & Le Roux**, *"High Temperature LEC Experiments,"* **JCMNS 41:19–24 (2026)**, doi **10.70923/001c.162978** — voltage begins above ~600 °C in a Ni/Cu-nanopowder electrode and tracks the same temperature range as the authors' excess heat.
- **The claim, in the inventors' words:** the device *"will spontaneously initiate the production of ionizing radiation and electrical energy based only on the thermal energy in its palladium lattice that is occluded with hydrogen or deuterium"* and is *"easy to replicate."* The mechanism is explicitly unknown, including to them.

## Status

`protocol` (draft; no home attempts yet — see the companion **Validation** record `synthesis/validations/2026-10-13-lattice-energy-converter-multi-lab-chain.md`, which documents the laboratory replication chain this card re-runs at bench scale)

## The claim (as asserted by the source)

A two-terminal device — an inner *working electrode* surface-activated by co-depositing **iron or palladium with hydrogen**, coaxially surrounded at a **0.5–1.1 mm** gap by a *counter electrode* of a different metal, the gap filled with **hydrogen, deuterium, or air** — **self-initiates a spontaneous voltage** (hundreds of mV), **conducts a current across an otherwise insulating gas gap**, and does both with **no external power and no radioactive material**. Reported: voltage rises with temperature (working electrode at 185 °C → ~10 µA, ~1.5 µW into a matched load), and the device keeps running for months.

**Honest framing:** This is a *claim* with an unusually strong supporting structure — at least five independent groups have built it, and one of them (Di Stefano) measured an unplated control device and found **nothing**. That control is what separates the LEC from the rest of the free-energy shelf, and this card exists to reproduce *that* control at home, not to endorse the energy claim. We hold no brief — the test is the point.

## Why it matters

Most devices in the Yard's energy rail have never been independently built and controlled by anyone. The LEC is the exception: it is simple enough to build on a bench, its control (an identical device *without* the active layer) is nearly free, and the one group that ran the control found a **six-orders-of-magnitude** difference in gas conduction between the active and untreated devices. If that result is real, it is a genuine reproducible anomaly; if it is not, the home test will find the active device conducting no better than its twin, and the whole claim collapses into ordinary gas physics. **Either outcome is decisive, and neither requires a laboratory.**

The card also carries a method lesson the archive keeps re-learning: **the voltage is not the effect.** Di Stefano's controls show the spontaneous voltage tracks electrode potentials (it *reverses* when an aluminium counter-electrode is used), while the *conduction* is the part that cannot be explained conventionally. A home test that measures only the open-circuit voltmeter reading will be fooled by a bimetallic cell; the test that matters applies an external voltage and measures the **forced current**.

## Replicability: `home/homelab`

- Build cost: **~$80–220** (metal tubing + fittings, a high-impedance multimeter, a plating supply, a bench supply for the forced-current test)
- Safety: **low-to-moderate** — dilute HCl (20 %) and a small plating current, hydrogen gas if used (a flammable-gas handling step; air-only is an acceptable first run), and a spinning-nothing, no-mains-wiring bench setup
- Accessibility: homelab bench (needs a DMM with ≥10 MΩ input impedance — most bench meters qualify; a bench supply capable of ±10–60 V for the conduction test)

## Apparatus (Bill of Materials)

### Core device

1. **Working electrode (WE):** a small metal tube — e.g. **4 mm OD brass or copper, ~100 mm long** (Di Stefano's inner tube). It must be platable and must let you evacuate/backfill if you run hydrogen.
2. **Counter electrode (CE):** a **6 mm OD tube** of a *different* metal (brass, copper, or aluminium), ~100 mm long, 1 mm wall, giving a **0.5 mm gap** around the WE. **Aluminium is worth including**: it reverses the polarity, which is the built-in diagnostic that the voltage is electrode-potential-driven.
3. **Spacers/seals:** rubber O-rings or a bead of high-temperature epoxy to hold the two tubes coaxial and insulated, while allowing gas to pass (the O-rings separate, they do not seal the gas).
4. **Gas fittings (only if running hydrogen):** a small valve and a fitting on the WE to evacuate and backfill; **air at atmospheric pressure is a valid first run** and needs no gas handling.

### Plating (the "activation" step — the only thing that makes the WE active)

5. **Plating cell:** a test tube / small jar holding the WE, with **four 1 mm iron wires** arranged around it (the anodes) for iron plating; or a Pd salt bath (PdCl₂ + LiCl, or PdBr₂ + LiBr) for palladium plating.
6. **Electrolyte:** **¼ HCl (20 %) + ¾ tap water** for iron plating (no added FeCl₂ — the Fe⁺⁺ comes from the anode wires). Palladium plating needs a Pd salt bath; **iron is the cheap, documented path** (Di Stefano's, and the one Zhang & Chen also used).
7. **Plating supply:** a bench supply or battery with a series resistor, to hold the ramped current — Di Stefano's schedule: **0.7 mA → 1.7 mA → 16 mA → 25 mA over ~8 h**, ending with a matte-black deposit.

### Measurement

8. **High-impedance DMM** (≥10 MΩ input; 1 MΩ is *better* for noise, per Di Stefano) — for open-circuit voltage. **A battery-powered meter is preferred** (eliminates any sneak ground path).
9. **Bench supply, 0 to ±60 V** — for the **forced-current** test (the primary measurement).
10. **Resistors:** a decade box or a set of known resistors (10 MΩ down to 1 kΩ) for the load sweep and the internal-resistance estimate.
11. **Capacitor, 100 µF** (optional) — to repeat Di Stefano's energy-storage check (he charged 100 µF to 309 mV in ~90 s; ~4.7 µJ).
12. **Geiger–Müller tube** (optional) — to attempt the radiation measurement. Note that **two independent groups found nothing above background**; a null here is expected and is not a failure.
13. **Data logger** (optional) — a multimeter with a logging mode or a LabJack-class ADC, so the slow voltage rise is captured rather than eyeballed.

### Safety equipment

- Nitrile gloves and eye protection (dilute acid, plating salts)
- Ventilation if using hydrogen; leak-check the fittings
- Standard bench practice for a low-voltage DC supply

## Protocol (Test A — control vs active, forced current)

### Setup

1. **Build the control device first.** Assemble the two coaxial tubes with the **unplated** WE, at the 0.5 mm gap, sealed but not permanently (so the WE can be swapped). Do **not** plate anything yet.
2. **Measure the control in air at atmospheric pressure:**
   - (a) **Capacitance** between the tubes (a cheap LCR meter) — should be ~30 pF for a device of this geometry; it confirms the gap is right.
   - (b) **Open-circuit voltage** with the high-impedance DMM, probes both ways, 60 s. *(Di Stefano measured 0.01 mV ± 5 µV here.)*
   - (c) **Forced current:** apply **−10 V to +10 V** (and, if your supply allows, −60 V to +60 V) and record the current at each step. *(Di Stefano measured 0 µA ± 0.5 nA here; a good setup should read <100 pA.)*
   - Repeat (b) and (c) with each CE material (brass, copper, aluminium).
3. **Record the noise floor** — the smallest voltage and current your setup can resolve. This is the number the active device has to beat by orders of magnitude.

### Active run

4. **Plate the WE** (iron, per the schedule above), rinse, dry. The deposit should be matte black and fine-pored. *(Optional: run hydrogen instead of air — this is the condition the inventors used; air is the cheaper first pass and Di Stefano's device worked in air.)*
5. **Assemble the active device** — same tubes, plated WE, same gap.
6. **Measure, in the same order as the control:**
   - (a) open-circuit voltage vs time (watch for the rise over tens of seconds to minutes);
   - (b) voltage vs **load resistance** (10 MΩ → 1 kΩ) to estimate internal resistance;
   - (c) **forced current** from −10 V to +10 V — **this is the primary endpoint**;
   - (d) optionally charge a 100 µF capacitor and record the stored voltage;
   - (e) optionally run the GM counter next to the active WE.
7. **Swap the CE** (brass / copper / aluminium) and note whether the voltage **reverses** — the aluminium reversal is the diagnostic that the voltage is electrode-potential-driven.
8. **Repeat the whole sweep ≥ 3 times**, and if possible plate a *fresh* WE and repeat on a second day (the iron deposit oxidises in ~a day; the effect is reported to decay with it).

**Measurable outcome:** the **ratio of forced current (active ÷ control)** at ±10 V, and the open-circuit voltage of the active device against the control's noise floor — plus whether the voltage reverses with an aluminium CE.

## Pass / fail (pre-registered)

- **PASS (the anomaly is real at home):** the active device conducts a **forced current ≥ 10³ × the control's** at ±10 V, *and* shows a stable open-circuit voltage ≥ 100 × the control noise floor, *and* the effect **decays as the plating oxidises** (or is absent in a re-run with a stripped WE). The home bench has reproduced the primary anomaly.
- **PASS (the anomaly is refuted — a complete, useful result):** the active device's forced current and voltage are **within the same order of magnitude as the unplated control**. A six-orders-of-magnitude lab result that does not appear at home means the effect depends on something the home build omits (Pd not Fe, sealed hydrogen, geometry) — and says which (Skeptic's Star).
- **FAIL (void — not a null):** the two devices are not geometrically identical (different gap or tube length); the meter's input impedance is <1 MΩ (it loads the cell); the forced-current test used a supply whose own leakage dominates; the WE was never actually plated; or the measurements were taken before the voltage stabilised.
- **INCONCLUSIVE:** one run only; no unplated control; no capacitance check; no load sweep; the plating oxidised before measurement.
- **ARTIFACT:** the voltage appears in **both** the plated and unplated devices (it is the bimetallic cell, not the active layer); or it tracks the **supply's** output rather than the cell; or it **reverses** with CE metal in a way that fully matches electrode-potential tables (which is the secondary effect, not the primary conduction anomaly).

---

## Confounds this design controls (and the one it cannot)

| Confound | Control |
|---|---|
| A bimetallic/galvanic voltage — the classic false positive | The **unplated twin**, same two metals, same gap; and the aluminium-CE polarity check |
| Instrument loading of a high-impedance source | ≥10 MΩ meter; battery-powered; both probe polarities |
| Water-vapour conduction in the gas | The inventors tested at −55 °C to freeze out water vapour and saw the same conduction (their control, not this card's — a home freezer run is a bonus, not a requirement) |
| Supply leakage faking the forced current | Measure the control device on the **same** supply and wiring; the control's <100 pA is the supply's own floor |
| Operator expectation | Pre-registered thresholds; measure the control **first**, and preferably have a second person label the devices |
| **The home build is not the inventors' cell** | **Not controllable — stated plainly below** |

**The limitation the card cannot remove.** A home build with an iron-plated brass tube in air is **not** the inventors' sealed Pd–H cell, and it is not the high-temperature 2026 device. So a home **null** bounds the effect at *this* geometry and *this* plating — it does not disprove an effect in a sealed palladium cell. What makes the test worth running anyway is that **Di Stefano's control campaign was run on exactly this simple, iron-plated, air-filled geometry** and still found the six-orders-of-magnitude conduction gap — so the card is re-running a *specific* documented experiment, not inventing a new one.

## Source

- **The claim and the device (primaries):** Gordon, F. E. & Whitehouse, H. J. *"Lattice Energy Converter."* **JCMNS 35(1):30–48 (2022)**, doi **10.70923/001c.72583** — https://jcmns.org/article/72583-lattice-energy-converter · *"LEC II: Iron Hydrogen Host Material,"* JCMNS 36(1):1–24 (2022) · *"Progress in Understanding and Scaling Up the LEC,"* JCMNS 39:14–35 (2025), doi **10.70923/001c.134029** · LENR Workshop (Srinivasan memorial) slides, Jan 2021 — https://lenr-canr.org/acrobat/GordonFlatticeene.pdf
- **The replication and the control campaign this card re-runs:** Di Stefano, A. *"Experimental Observation on the Lattice Energy Converter."* **ICCF-24, Mountain View, 27 July 2022** (preprint + slides) — https://lenr-canr.org/acrobat/DiStefanoAexperiment.pdf
- **A second independent replication with the same plating methods:** Zhang, H. & Chen, S. *"Experimental Results of Lattice Energy Converter LEC."* **JCMNS 39:241–248 (2025)**, doi **10.70923/001c.134009** — https://jcmns.org/article/134009-experimental-results-of-lattice-energy-converter-lec
- **The high-temperature extension:** Biberian, J.-P., Michel, R. & Le Roux, C. *"High Temperature LEC Experiments."* **JCMNS 41:19–24 (2026)**, doi **10.70923/001c.162978** — https://lenr-canr.org/acrobat/BiberianJPjcondensedzn.pdf
- **Corpus anchors (AFLinks):** `sources/scout-report-2026-10-10-1200.md` (ICCF-27 program item 18: "Gordon LEC reproducibility") · `sources/2026-10-12-scout-growth-1815.md` (JCMNS 41 / ICCF-26 already archived via the lenr-canr lane) · `sources/2026-09-07/scout-report.md` (Biberian reproducible-tritium preprint)
- **Companion Yard records:** `synthesis/validations/2026-10-13-lattice-energy-converter-multi-lab-chain.md` (the replication chain) · `synthesis/validations/2026-10-10-lenr-spawar-cr39-replication-earthtech-2009.md` and `synthesis/replication/2026-09-17-dossier-021-anomalous-heat-effect-double-observable.md` (the LENR rail's other double-observable card)

## Honest framing

We hold no brief — the test is the point.

The LEC is the rare energy-rail claim with a **control that someone actually ran**, and this card is built to reproduce that control, not to promise power. The expected outcome is genuinely open: the laboratory chain is positive and multi-group, and the effect size (six orders of magnitude in conductance) is the kind of number that either reproduces on a bench or does not. **What the card will not do is read the voltmeter and call it energy** — the primary endpoint is the forced current, because the archive's best replication showed the voltage is a secondary, electrode-potential effect while the conduction is the part that resists a conventional explanation.

Two honest notes. First, **no group has found radiation above background**, and the inventors admit the mechanism is unknown; nothing here implies a nuclear reaction. Second, the home build is a **simplified** cell — iron plating, air, unsealed — so a null bounds this geometry, not the sealed Pd–H device. Both notes belong on the card's face, because a card that hides them would be selling a result instead of measuring one.

⚡ **Safety:** dilute HCl and a small plating current; hydrogen is flammable if you run the sealed variant — leak-check and ventilate; no mains wiring beyond a low-voltage supply. Eye protection and gloves throughout.
