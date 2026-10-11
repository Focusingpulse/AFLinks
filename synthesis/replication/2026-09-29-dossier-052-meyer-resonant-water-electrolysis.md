---
name: Dossier 052 — Meyer Resonant Water Electrolysis (Excess Gas Yield)
description: "Home-bench test of Stanley Meyer's claim that a concentric-tube cell driven by a gated pulsed waveform at resonance, in plain water with no electrolyte, produces hydrogen–oxygen gas above the Faraday-implied maximum — with a dry-gas volumetric measurement against a coulomb-counted charge and a plain-DC control on the same electrodes as the discriminating comparison."
---

# Dossier 052 — Meyer Resonant Water Electrolysis (Excess Gas Yield)

**Status:** protocol ready
**Domain:** energy (water electrolysis / anomalous gas yield)
**Tier:** straw (home/homelab, ~$200–350)
**Source:** `synthesis/validations/2026-09-29-meyer-electrolyser-lawton-replication.md`; `http://www.tuks.nl/pdf/Patents/Meyer/D14.pdf` (corpus record id 37942)
**Created:** 2026-09-29

---

## Source lineage

- **Stanley Meyer (1940–1998)** — American inventor; concentric-tube "water fuel cell" driven by pulsed DC, claimed to split water at high efficiency through resonance rather than conventional electrolysis, and to do so in ordinary water without electrolyte. Patents filed through the 1980s–90s; the corpus carries the claim attached to Meyer's **demonstration** cell.
- **Jean-Louis Naudin** — French experimenter whose `wfc/` pages (corpus records id 2414009, id 2414450) mirror the replication literature for Meyer's cell; a long-standing node of the European replication scene.
- **Dave Lawton (2006)** — built a working copy of the demonstration cell; the build is documented by Patrick J. Kelly in *A Practical Guide to 'Free Energy' Devices*, Part D14. Reports "an impressive rate of electrolysis" on tap water with no additives, and assesses the drive circuit at about **300 % of the Faraday assumed maximum efficiency** — a figure asserted without a tabulated derivation. **This is the corpus's one documented attempt and this dossier's starting point.**
- **The claim's own structure:** note that the lineage's evidentiary weight sits in *build guides and videos*, not in measurements. That is the gap this protocol closes.

## Status

`protocol` (one documented attempt, uncalibrated; no measurement record)

## The claim (as asserted by the source)

A concentric-tube water cell — stainless inner and outer tubes with a 1–2 mm gap, immersed in **plain tap or rain water with no electrolyte** — driven by a **gated pulsed DC waveform** at the cell's resonant frequency, releases hydrogen–oxygen gas at a rate **far above the Faraday-implied maximum** for the charge passed.

Secondary and more modest claims from the same source, which are the parts most likely to survive:

- The cell draws **less current per tube as tubes are added** (≈1 A for the first tube; the sixth adds almost nothing).
- Cutting a **slot in the top of each outer tube** to match its resonant pitch to the inner tube's may matter (Meyer's own tubes show such slots; the document infers this from organ-pipe tuning).

**Honest framing:** The underlying apparatus is real and buildable — concentric stainless electrodes in water are ordinary electrolysis hardware. What is unproven is the *excess*. The document's own photograph evidence shows gas being produced; nobody has published a dry-gas-versus-charge measurement for this cell. **We hold no brief — the test is the point.**

## Why it matters

This is the highest-profile "water car" claim in the corpus, and it is the one most likely to be re-attempted by a home experimenter with no calibration and no baseline — the exact conditions in which a **vapour artefact** can be mistaken for an anomaly and then repeated for years. Putting a clean protocol in the Yard does two things: it gives the first real replicator a number to beat instead of a rumour, and it makes the failure mode explicit before anyone spends money.

It is also a genuinely **cheap** test. The claim is decidable at a kitchen bench with a scale, a graduated cylinder, a coulomb counter and a desiccant column. Nothing here needs a laboratory.

And the honest prior matters: electrolysis is one of the most precisely characterised processes in chemistry, and this is the rare corpus claim where a **well-defined null baseline already exists** — Faraday. A rig validated against Faraday in its control arm turns any positive deviation into a real signal rather than an argument.

## Replicability: `home/homelab`

- Build cost: **~$200–350** (stainless tube stock, acrylic/plastic housing, drive electronics, DC supply, coulomb meter, gas collection and drying)
- Safety: **high for a home build** — the product is a stoichiometric hydrogen–oxygen mixture. See the safety block below; it is not optional reading.
- Accessibility: home bench. No machining required if the tubes are bought pre-cut; a 3D-printed housing works as well as the drain-coupler build.

### Safety (read before buying anything)

From the corpus source itself: experimenting with hydrogen, or a hydrogen–oxygen mixture, **"is highly dangerous."** Two properties drive every control:

1. **Hydroxy gas ignites with a flame front about 1,000× faster than petroleum vapour.** Standard flashback arrestors are therefore **not** adequate protection.
2. The protections the source recommends: a **bubbler** between the cell and everything downstream; a **pressure-activated switch** cutting power above ~5 psi; a bubbler lid that is a **tight push fit rather than clamped**, so it blows off instead of shattering; and an ignition-switched relay if the cell is ever near an engine.

For this protocol specifically: **vent the collected gas continuously to open air or a fume hood; never accumulate a stoichiometric mixture in a closed vessel; do not ignite the product; keep the collection column small.** The measurement requires volume readings, not storage.

## Apparatus (Bill of Materials)

### Core components

1. **Electrodes:** 6 concentric tube pairs, **316L stainless steel** — outer ~25 mm (1 in) OD, inner ~19 mm (3/4 in) OD, wall ~1.6 mm (1/16 in), length ~125 mm (5 in). Source geometry: 1–2 mm inter-tube gap. Pre-cut tube stock with a **pre-cut top slot** in the outer tubes, per the source's note, if available; otherwise use plain tubes for Test A and treat slots as a Test B variable.
2. **Housing:** clear acrylic tube with end fittings (or a 3D print), sealed so gas cannot escape. Transparency is a feature — it makes runaway gassing visible immediately.
3. **DC supply:** bench supply, **0–30 V, 0–10 A**, current-limited. Needed for the control arm.
4. **Drive electronics (pulsed arm):** two NE555 oscillators (the first gating the second), variable frequency and variable mark/space; BUZ350 or equivalent 200 V/20 A N-channel MOSFET on a heatsink; 1N4007 clamp diode; the resistor/capacitor set per the source's published component list. Optionally two bifilar inductors (100 turns each of 22 SWG on a 9 mm × 25 mm ferrite rod) — include them, since the source says they raise efficiency.
5. **Charge measurement:** **coulomb counter or a logging ammeter with fine time resolution** (≥10 Hz logging). This is the instrument that makes the test meaningful — average current × time is *not* good enough for a pulsed waveform with a varying duty cycle.
6. **Gas collection, DRY:** a sealed collection column or gas syringe fed through a **desiccant column** (silica gel or Drierite) and a **cold trap** (a small flask in an ice bath), so water vapour is removed *before* the volume is read. This is the single most important design choice in the protocol.
7. **Temperature and pressure:** thermometer in the cell liquid and in the collection column; barometer (or a reference pressure from a weather service) for ambient pressure at the time of reading.
8. **Cathode/anode materials:** the same 316L tubes for both arms. No electrolyte is added — the source's claim depends on that, and tap water's native conductivity is the honest condition to test.
9. **Water:** tap water from one source, one batch, used in both arms. Note the source's water source and let it stand to room temperature first.
10. **Conditioning:** a stepwise tap-water conditioning procedure is described in the source and should be followed for the pulsed arm; run the control arm on the **same conditioned electrodes**.

### Measurement and safety equipment

- Eye protection and a face shield where gas is collected.
- Continuous ventilation; nothing flammable nearby.
- Bubbler and pressure cut-off switch installed **before** the first run, not after.
- Fire blanket; no ignition sources in the room.

## Protocol (Test A — dry gas volume per coulomb, control vs. pulsed)

### The Faraday baseline, stated once so it need not be re-derived

For water electrolysis at 100 % current efficiency, at **25 °C and 1 atm, dry**:

- 1 coulomb = 1/96 485 mol e⁻
- H₂ = ½ × (1/96 485) mol = **126.8 µL per coulomb** (24.47 L/mol)
- O₂ = ¼ × (1/96 485) mol = **63.4 µL per coulomb**
- **Total stoichiometric H₂ + O₂ = 190.2 µL per coulomb** (at 0 °C it is 174.2 µL/C — state which temperature you are reporting at, and correct for your ambient T and P)

At 100 % current efficiency a plain-DC cell should read **≈190 µL/C at 25 °C**. That is the number the pulsed arm has to beat, not the number it has to reach.

### Setup

1. Assemble the cell; leak-test the housing with the gas path connected to the collection column while running air through it.
2. Install the desiccant column and cold trap between cell and collection column. Confirm the path is dry and sealed.
3. Wire the charge meter so that **all** cell current passes through it.
4. Install the bubbler and the pressure cut-off.
5. Condition the electrodes in tap water per the source's procedure.
6. Fill with a measured volume of tap water at recorded temperature.

### Procedure

Run both arms on the **same electrodes, same water, same collection path**, alternating order across repeats (ABAB…), minimum **3 repeats per arm**:

- **Arm 1 — control, plain DC.** Constant voltage in the range that gives a sensible current (start 5–12 V), current-limited so the cell does not boil. Run until the collection column has moved a measurable volume.
- **Arm 2 — pulsed, source waveform.** The gated two-oscillator drive, tuned across frequency and mark/space to the setting that gives the *highest* gas rate for a given average current. Record the setting. Include the bifilar inductors.
- **Arm 3 — pulsed, tuned to the tubes' resonant pitch** (optional): install slotted outer tubes and repeat Arm 2.

For each run record:

1. Elapsed time and **total charge passed (C)** from the coulomb counter — this, not average current, is the denominator.
2. **Gas volume collected (mL)** read after the desiccant/cold trap, with the collection column's temperature and ambient pressure.
3. Cell liquid temperature at start and end.
4. Drive parameters (frequency, mark/space, voltage, peak current) for Arm 2.
5. Any visible mist, condensation or liquid carry-over past the trap — **if the trap collects water, say so explicitly; that water was being counted as gas in any undried measurement.**
6. Current draw with 1, 2, 3 … 6 tube pairs installed (the source's falling-current observation, tested as its own sub-claim).

### Controls

- **Plain DC on the same electrodes** is the control arm, and it is the whole test. The claim is that pulsed resonance beats Faraday; the control establishes what this rig does *without* resonance.
- **Rig-validation gate:** if the DC arm does not land near **190 µL/C at 25 °C (say 170–210 µL/C, i.e. 90–110 % of theoretical)**, the rig is losing or gaining gas and **no pulsed-arm number means anything**. Fix the rig; do not proceed to interpretation.
- Alternate run order to cancel electrode ageing, water warming and ambient drift.
- Report the trap's water catch for every run; a large catch invalidates that run.
- No electrolyte in either arm. If the tap water will not conduct at safe voltages, say so and stop — do not add electrolyte and then compare to Meyer's claim.

## Pass / fail criteria (pre-registered)

**The claim is supported if:**

- The dry-gas arm reads **≥ 1.5 × the charge-normalised volume of the plain-DC control**, in **every** repeat, with the trap catch small and reported; **and**
- The DC control is inside the rig-validation gate (90–110 % of 190 µL/C at 25 °C); **and**
- The excess is not attributable to liquid carry-over, temperature or pressure error.

**The claim fails at this scale if:**

- Pulsed and DC arms agree within measurement scatter once the gas is dried and normalised by charge (**this is the expected outcome, and it is a real result**); or
- The apparent excess disappears once gas is dried and charge is measured rather than assumed.

**Inconclusive if:**

- The DC arm cannot be brought inside the validation gate; or
- The charge measurement cannot resolve the pulsed waveform; or
- Electrode conditioning or water conductivity prevents stable operation at safe voltage without electrolyte.

**Sub-claim, tested separately:** the falling current with added tubes is **confirmed** if the per-tube current increment drops monotonically across 1 → 6 pairs, in at least two repeats. This can pass or fail independently of the main claim, and is worth reporting either way.

## Feedback loop

- Log every attempt here, including failures and abandoned runs, with the trap catch.
- ≥ 2 independent attempts with a validated DC arm → verdict; cross-link from `synthesis/validations/2026-09-29-meyer-electrolyser-lawton-replication.md`.
- Share: the Replication Yard; the Aether Force water/energy strand.

## Attempted-by / results log

- **2006 — Dave Lawton (reported by Patrick J. Kelly, *A Practical Guide to 'Free Energy' Devices* Part D14).** Built and ran the demonstration cell on tap water with no additives; reported "an impressive rate of electrolysis" and assessed the circuit at **~300 % of the Faraday assumed maximum efficiency**. **Not a measurement:** no tabulated gas volume against charge passed, no stated Faraday baseline, no drying step described, no uncertainty. Evidence is build detail and video. Also reported: current draw falling as tubes were added (≈1 A first tube, < 0.5 A added by the second, < 2 A total at three, ≈100 mA each for the fourth and fifth, almost none for the sixth). Filed as **low confidence** — see the validation record for the full read.
- *(no calibrated attempt located in the corpus. Open for the first replicator — and note that a well-run **negative** here retires a fifty-year claim cleanly, which is worth more than another video.)*

---

## Source Documents

- `synthesis/validations/2026-09-29-meyer-electrolyser-lawton-replication.md` — the tip-jar record for the one documented attempt.
- `http://www.tuks.nl/pdf/Patents/Meyer/D14.pdf` — Patrick J. Kelly, *A Practical Guide to 'Free Energy' Devices*, Part D14, "Replication of Stanley Meyer's Demonstration Electrolyser" (last updated 3 October 2007). Corpus record **id 37942** in `search_chunks/alternative-energy-technologies.json` (source_site `tuks.nl`). Read in full.
- `http://jnaudin.free.fr/wfc/D14.pdf` and `http://www.jlnlab.com/wfc/D14.pdf` — the 2007-10-03 edition mirrored on Jean-Louis Naudin's water-fuel-cell pages. Corpus records **id 2414009** and **id 2414450**.
- Video cited by the source (not fetched for this dossier): `icubenetwork.com/files/watercar/non-commercial/dave/videos/Wfcrep.WMV` (alternator drive) and `www.panaceauniversity.org/WFCrep2.wmv` (solid-state drive).
- The claim's own document class is worth naming: `search_chunks/alternative-energy-technologies.json` and `search_chunks/patents-inventions.json` hold many Meyer-related entries, of which the corpus flags the D14 family (ids 37942, 2414009, 2414450) as the replication-bearing ones. Everything else near this claim in the archive is patent text, marketing or forum discussion — **a patent is a claim, not a validation.**

## Related Quests

- *(none yet — this dossier is the first artifact in the water-electrolysis / anomalous-gas domain. A quest card should follow once one attempt is logged.)*

## Notes

This dossier exists because the corpus has **an attempt and no protocol**: a documented build, a reported efficiency figure, and no measurement anywhere for anyone to compare against. The protocol above is deliberately built around one design decision — **dry the gas, count the coulombs** — because every historical excess-gas claim in this family has died there, and every honest positive has survived there.

Note also what this dossier is *not*: it is not a test of Meyer's production cell, his patents, or any vehicle claim. It is a test of one number — microlitres of dry gas per coulomb — measured the way the lineage never measured it. A negative result retires the excess claim at this scale; it says nothing about the falling-current observation, which stands on its own and may well be real circuit behaviour.
