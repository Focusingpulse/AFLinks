---
name: Dossier 018 — Bladeless Tesla Turbine Static Electricity Conversion
description: "Home/homelab-scale test of the modern bladeless Tesla turbine claim: compressed air + electrostatic charges generate usable electrical output (800V, 2.5A, 325Hz) while neutralizing static and improving air quality."
---

# Dossier 018 — Bladeless Tesla Turbine Static Electricity Conversion

**Status:** protocol ready
**Domain:** energy (static-to-electrical conversion)
**Tier:** straw (home/homelab-scale, ~$150-250)
**Source:** sources/2026-08-29-scout-b-es-fr-zh.md (item 3)
**Created:** 2026-09-14

---

## Source lineage

- **Nikola Tesla (1856–1943)** — Original bladeless turbine patent (US1061206, 1913): "Fluid propulsion" using boundary-layer drag on smooth disks.
- **Multi-institutional team (2026)** — Chung-Ang University (Korea), Kumoh National Institute of Technology (Korea), MIT (USA), National Taiwan University — Modern reformulation with electrostatic conversion.
- **Published in:** Nanowerk (Jan 2026), reported in 20minutos.es (Spanish news outlet, Jan 13, 2026).
- **Claim:** Bladeless Tesla turbine converts static electricity into useful energy: 800V, 2.5A, 325Hz output at 8,472 RPM with 300 m/s airflow from compressed air + electrostatic charges.

## Device-family watchlist (energy rotation, mid-cost tier)

- Bladeless Tesla turbine (this dossier — home/homelab ~$150-250).
- Tesla radiant receiver (dossier 003 — merged in game).
- Eeman biocircuit (dossier 002 — health domain).
- Vortex jet turbine (dossier 008 — proposed, higher tier).

## Status

`protocol` (draft; no attempts yet)

## The claim (as asserted by the source)

A bladeless Tesla turbine — using smooth disks and boundary-layer drag rather than blades — when fed with compressed air and electrostatic charges, generates usable electrical output: **800V, 2.5A, 325Hz** at **8,472 RPM** with **300 m/s airflow**. Secondary claims: neutralizes static electricity in the environment and improves air quality.

**Honest framing:** This is a *claim* from a 2026 multi-university study reported in Nanowerk. The original Tesla turbine (1913) is a real, patented device with documented performance in fluid propulsion. The electrostatic conversion claim is new and requires independent replication. We hold no brief — the test is the point.

## Why it matters

The bladeless Tesla turbine is a century-old design that never achieved mainstream adoption. If the electrostatic conversion claim replicates, it would represent a novel pathway for energy generation from compressed air and ambient static — potentially relevant for off-grid power, workshop energy, and air-quality management. A home-scale test would provide the first independent data point on this specific claim.

## Replicability: `home/homelab`

- Build cost: **~$150-250** (Tesla turbine disks + compressed air source + electrostatic generator + measurement gear)
- Safety: moderate (compressed air, high voltage, spinning disks — requires eye protection, ear protection, secure mounting)
- Accessibility: homelab bench (requires compressed air supply, basic machining or 3D printing for disks, multimeter, oscilloscope if available)

## Apparatus (Bill of Materials)

### Core components

1. **Bladeless Tesla turbine disks:** 5-10 smooth metal or acrylic disks, 5-10 cm diameter, 1-2 mm spacing (can be 3D-printed or machined)
2. **Compressed air source:** Shop compressor or portable air tank (regulated to 2-4 bar / 30-60 psi)
3. **Nozzle/jet:** Converging nozzle directing airflow tangentially onto disk edges
4. **Electrostatic generator:** Van de Graaff generator, Wimshurst machine, or high-voltage DC supply (10-50 kV range)
5. **Electrode:** Sharp-point electrode or wire mesh to inject charges into airflow
6. **Shaft and bearings:** Low-friction bearings for disk stack (high RPM expected)
7. **Electrical pickup:** Brushes or induction coil to collect generated voltage/current

### Measurement equipment

1. Multimeter (voltage, current)
2. Oscilloscope (if available) — to verify 325Hz claim
3. Tachometer (optical or magnetic) — to verify 8,472 RPM
4. Anemometer or flow meter — to verify 300 m/s airflow
5. Static electricity meter or electroscope — to measure ambient static before/after
6. Air quality sensor (optional) — particulate count or ionization level

### Safety equipment

- Eye protection (safety glasses)
- Ear protection (turbine may be loud at high RPM)
- Secure mounting (bench vise or heavy base)
- Insulated gloves for high-voltage handling

## Protocol (Test A — electrical output, controlled)

### Setup

1. Assemble the bladeless Tesla turbine: mount disks on shaft with proper spacing, install in housing with tangential air inlet.
2. Connect compressed air source to nozzle, aimed at disk edge.
3. Install electrostatic generator with electrode positioned to inject charges into the airflow (upstream of turbine).
4. Wire electrical pickup (brushes or induction coil) to multimeter/oscilloscope.
5. Secure all components firmly; verify no loose parts at expected RPM.

### Procedure

Run three configurations, 5 runs each, alternating order:

- **A — Compressed air only:** Air jet on disks, no electrostatic injection. Measure voltage, current, RPM, airflow.
- **B — Electrostatic only:** Electrostatic generator on, no airflow. Measure voltage, current, ambient static.
- **C — Combined:** Compressed air + electrostatic injection. Measure voltage, current, RPM, airflow, ambient static before/after.

For each run:
1. Start measurement logging (voltage, current, RPM).
2. Activate air and/or electrostatic source as per configuration.
3. Run for 60 seconds, recording steady-state values.
4. Stop, allow turbine to spin down, record ambient static.
5. Log all readings in table.

### Controls

- Same air pressure, same disk stack, same nozzle position for all runs.
- Alternate A/B/C order across runs to cancel drift (temperature, humidity, battery effects).
- The "air only" condition A is the baseline; B tests electrostatic alone; C tests the combined claim.
- Verify RPM and airflow match reported values (8,472 RPM, 300 m/s) before accepting electrical data.

## Pass / fail criteria (pre-registered)

**PASS (supports claim):**
- Configuration C produces **measurable electrical output** (voltage > 10V, current > 0.1A) while A and B produce negligible output.
- AND C output is **consistent across runs** (same order of magnitude, not random noise).
- AND RPM and airflow are in the reported range (±20% of 8,472 RPM, 300 m/s).

**FAIL (refutes claim):**
- C produces no measurable output beyond A or B (within noise).
- OR output is random/arbitrary, not correlated with air+electrostatic combination.
- OR RPM/airflow significantly below reported values, suggesting the claim requires specific conditions not achieved.

**INCONCLUSIVE:**
- Turbine fails to reach target RPM (mechanical issues).
- Electrostatic generator fails to inject charges (insufficient voltage, electrode placement).
- Measurement gear insufficient to detect claimed output (need oscilloscope for 325Hz verification).

## Feedback loop

- Log every attempt (including failures) here.
- ≥2 independent attempts → verdict; cross-link to energy-domain quest card when merged.
- Share: Permies (if relevant), the Replication Yard, Aetherforce Tesla/energy strand.

## Attempted-by / results log

- *(none yet — open for the first replicator.)*

---

## Source Documents

- sources/2026-08-29-scout-b-es-fr-zh.md (item 3: Turbina Tesla Sin Aspas)
- 20minutos.es article: https://computerhoday.20minutos.es/ciencia/energia-inalambrica-una-turbina-tesla-sin-aspas-es-capaz-convertir-electricidad-estatica-energia-util_6920492_0.html
- Nanowerk reference (Jan 2026)

## Related Quests

- dossier-003-tesla-radiant-receiver.md (energy domain, merged)
- dossier-008-vortex-jet-turbine.md (energy domain, proposed)

## Notes

This dossier tests the **electrostatic conversion** claim specifically. The original Tesla turbine's fluid-propulsion performance is well-documented; the novelty here is the claim of usable electrical output from combined air+static operation. A negative result is as valuable as a positive one — log it honestly.
