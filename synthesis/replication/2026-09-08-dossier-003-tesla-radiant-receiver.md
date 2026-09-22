---
name: replication dossier 003 — Tesla radiant energy receiver
description: Replication dossier for Tesla's radiant energy receiver (US patent 685,957 apparatus — elevated insulated plate, capacitor, ground). Home-replicable (~$30-50). Testable by charge-accumulation measurement vs shielded control. Status: protocol.
---

# Replication Dossier 003 — The Tesla Radiant Energy Receiver

## Source lineage

- **Nikola Tesla** — US Patent 685,957 "Apparatus for the Utilization of Radiant Energy" (1901) and 685,958 "Method of Utilizing Radiant Energy" (1901): an insulated conducting plate elevated in open air, connected through a capacitor to ground; the environment deposits charge on the plate, the capacitor accumulates it, a load can draw it.
- **Peter A. Lindemann** — *The Free Energy Secrets of Cold Electricity* (2000) + 2006 lecture — the compilation the archive's translation is built from.
- **Archive source doc:** `living-library/translations/2026-09-03-tesla-patents-radiant-energy-fr.md` (FR→EN analysis of Tesla's radiant-energy patent schematics; honest compiler disclaimer included: "no single patent provides a step-by-step assembly guide").
- Scout context: `living-library/sources/2026-08-26-scout-a-fr-es-zh.md` Find 2 (French analysis of Tesla's radiant energy patents with practical assembly guidance).
- Rotates into the ENERGY domain of the Engine of Practicality (energy → water → food → shelter → health → community). Mirrors Village guild **Homesteading** (self-reliance / off-grid energy) in the Aetherforce quest-mirror layer.

## Status

`protocol` (draft; no attempts yet)

## The claim (as asserted by the tradition)

Tesla's patents assert that an elevated, insulated conductor exposed to the open air accumulates charge from the environment ("radiant energy"), day and night, and that this charge can be collected in a capacitor and used to do work. Tesla claimed continuous charging regardless of visible source.

**Honest framing:** this is a *claim* from 1901, and known 2026 physics already predicts SOME charge collection by any elevated insulated conductor: the atmospheric potential gradient (~100 V/m near the ground), RF rectification at contact junctions, and triboelectric effects. The dossier does not test "is atmospheric electricity real" — it tests ONE measurable facet: **how much charge does the home-built receiver actually collect, and is it above a shielded control?** The open question the tradition cares about (magnitude and source) is exactly what the numbers will speak to. We hold no brief — the test is the point.

**Under-promise, stated plainly:** even if collection is confirmed, expected magnitude at home scale is micro-watts (½CV² for realistic voltages and capacitances) — enough to move a meter, NOT enough to power a household. The claim under test is *measurable collection*, not *usable power*.

## Why it matters

This is the founding document of the entire "ambient energy harvesting" lineage — every free-energy forum thread descends from patent 685,957. Families will keep encountering this claim. A $30 controlled test (receiver vs shielded control) would be the archive's first clean home-scale data point on the lineage, and it doubles as a real lesson in atmospheric electricity, grounding, and honest measurement — core self-reliance energy literacy.

## Replicability: `home`

- Build cost: **~$30-50** (aluminum plate or ~10 m insulated wire, wooden/fiberglass pole, film capacitor, ground rod or cold-water-pipe ground, DMM with 10 MΩ input)
- Safety: **no mains connection anywhere.** The elevated conductor is a lightning attractant — **disconnect and ground the antenna whenever storms are near or unattended.** Never run during thunderstorms. This is a fair-weather instrument.
- Accessibility: an afternoon with hand tools; kids can hold jobs (pole, plate, table-scribe)

## Apparatus (Bill of Materials)

- 1 aluminum or galvanized steel plate, ~30×30 cm (or a 5-10 m horizontal wire antenna as the collector)
- 1 wooden or fiberglass pole, 3-5 m (NO metal pole; it must insulate)
- Insulated wire for the downlead (~10 m) + strong insulators (ceramic/plastic) at the plate
- 1 low-leakage film capacitor, 10-100 nF (polypropylene; NOT electrolytic — leakage ruins the test)
- 1 ground connection (ground rod preferred; clamp to a metal water pipe as fallback)
- 1 digital multimeter, 10 MΩ input impedance (most DMMs; check the spec sheet)
- Optional: a neon bulb or small LED across the cap for a visible tick
- 1 roll of heavy aluminum foil (for the control shield)

## Protocol (Test A — charge accumulation vs shielded control)

1. Mount the plate atop the pole at 3-5 m, on insulating supports, in the open (away from trees and buildings if possible). Run the insulated downlead to the capacitor's high terminal; capacitor's other terminal to ground.
2. DMM across the capacitor (10 MΩ bleeds continuously — that's fine, it IS the load; record it).
3. **Session:** measure voltage at 0, 5, 10, 15 min. Note weather, sky condition, time of day.
4. Run 5+ sessions across varied conditions: morning / midday / after dark; clear / overcast / (never storm).
5. **Control (same session, alternating):** wrap the plate in foil connected to ground (a Faraday shield). Same measurement schedule. The control should read ~0; any control reading is your noise floor.
6. Log every number in a table: date, time, sky, wind, V at each interval, control V.

## Pass / fail criteria (pre-registered)

- **Receiver accumulates charge consistently above the shielded control** (≥10× control noise, same direction ≥4/5 sessions) → the apparatus measurably collects ambient charge at home scale. Verdict: *collection confirmed; mechanism unresolved* (atmospheric gradient vs RF vs Tesla's "radiant" claim — the numbers constrain which). Then compute stored energy (½CV²) and report honest micro-watt scale.
- **No accumulation above control** → the 1901 receiver does not replicate at home scale under fair conditions; log honestly (Skeptic's Star material) and cross-link to the radiant-energy death-cert line when written.
- Either outcome is a win for the archive: the founding claim of the free-energy lineage gets its first clean home data point.

## Feedback loop

- Log every attempt (including failures) here.
- ≥2 independent attempts → verdict; cross-link to the energy-domain quest card when merged.
- Share: Permies post, Replication Yard, Aetherforce energy strand.

## Attempted-by / results log

- *(none yet — open for the first replicator.)*
