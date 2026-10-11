---
name: Dossier 024 — Spiral-Pipe Friction Test
description: "Replication dossier for the 1952 Stuttgart Pöpel/Schauberger pipe claim: at high flow velocity a spirally-shaped pipe's resistance falls to zero and turns negative, and copper pipes resist water less than smooth glass. Home-replicable, gravity-fed, ~$40-100."
---

# Dossier 024 — The Spiral-Pipe Friction Test

**Status:** protocol
**Domain:** energy (flow resistance / energy loss)
**Tier:** straw (home/homelab-scale, ~$40–100)
**Created:** 2026-09-18
**Source docs:**
- `living-library/translations/2026-09-11-acqua-viva-viktor-schauberger-it.md` — Olof Alexandersson, *Living Water: Viktor Schauberger and the Secrets of Natural Energy* (Italian ed. *Acqua Viva*), ch. "The Last Years" / "Experiments at the Stuttgart Technical College" (lines 3831–3945)
- `living-library/translations/2026-09-09-schauberger-dynamic-hydroelectric-energy-es.md` (lines 136–174) — Spanish technical analysis of Schauberger's 1930 jet-turbine patent, restating the same Stuttgart finding

---

## The claim (as asserted by the sources)

In 1952, at the Stuttgart Technical College, Prof. Franz Pöpel and Viktor Schauberger ran flow-resistance tests on pipes of **different materials and different shapes**. Two linked claims came out of it:

1. **Material:** a smooth-walled **glass** tube showed **more** resistance to water than a **copper** tube of the same geometry — "it seemed that the material actually influenced friction."
2. **Shape (the extraordinary one):** in a pipe **configured as a spiral** (based on the shape of the kudu antelope's horn, following Schauberger's "cycloidal spiral space-curve"), at a relatively high flow rate **"the resistance dropped to zero and suddenly became a negative value."** The Spanish source states it flatly: "the friction in this pipe decreased with an increase in velocity and, at a certain point, the water flowed with **negative resistance**."

Pöpel's own summary of the spiral tube, quoted in the source: *"It seems that in this pipe the column of water frees itself from the walls of the pipe and oscillates freely, flowing through the tube."* The published chart shows three curves — friction in a straight glass tube (highest), a straight copper tube (middle), and a spiral copper tube (lowest, and turning negative at high flow).

**Honest status of the claim:** extraordinary and unreplicated in the modern literature. The 1952 measurements were made with 1950s instrumentation and the source itself reports only a chart, not a numerical table or error bars. Mainstream fluid mechanics actually predicts the **opposite** of claim 2 for ordinary spiral/coiled pipe: coils generate secondary (Dean) vortices that *increase* pressure drop over a straight pipe of equal length. So the mainstream and the claim point in opposite directions — which is what makes this a genuinely discriminating test rather than a rigged one.

**What "negative resistance" can and cannot mean.** A steady-state negative resistance would mean the pipe delivers more hydraulic energy than the head supplies — a perpetual-motion claim, and the dossier does not assume that. The three defensible readings of the 1952 result are: (a) a **measurement artifact** of the era's manometers and flow meters; (b) an **unsteady/resonance effect** — a transient or oscillatory condition that a steady-state head-loss measurement misreads; (c) a **real reduction in wall friction** in the spiral configuration, which has mainstream precedents in a different form (polymer drag reduction, riblet/shark-skin surfaces, and swirl-flow drag reduction). The test below discriminates between these readings by measuring **steady flow at fixed head**, where (b) can only show up as increased variance, not as a steady gain.

**Under-promise, stated plainly:** a home rig with a small head tank and a bucket-and-stopwatch flow measurement will not resolve a micro-watt effect. It **can** resolve a large one — a 20%+ flow difference at equal head, or a spiral tube that clearly beats straight. If the effect is real at the magnitude the 1952 chart implies, a family will see it. If it is not, the family will see parity, and that is the honest negative the archive wants.

## Why it matters

This is the **load-bearing experiment of the entire Schauberger vortex lineage**. Every downstream claim — the Wasserwirbler, the hyperbolic funnel, the jet turbine, the repulsine, "implosion" as an energy principle — rests on the assertion that **the shape of a conduit changes how water resists flow**. Dossiers 001, 004 and 008 all *cite* the Stuttgart pipe result as their supporting evidence; none has ever tested it directly. This dossier tests the foundation itself, and it is one of the few Schauberger claims that is cheap, safe, indoor/outdoor-anywhere, and highly measurable at home scale.

It is also a real education: a family that runs this learns head, flow rate, pressure drop, materials effects, and what a controlled comparison actually costs — core off-grid water-and-energy literacy.

## Replicability: `home`

- Build cost: **~$40–100** (copper tube ×2 lengths, glass tube, a few fittings, a head tank/tote, bucket, stopwatch, thermometer). The spiral tube is the fiddly part; a pre-coiled copper coil (available for solar/heat-exchanger use) gets you most of the way.
- Safety: **no mains, no chemicals, no heat.** This is gravity-fed water at household pressures. Only ordinary care needed: lift the tank safely, don't let a 200 L tote tip, keep the outlet clear.
- Accessibility: an afternoon for the tube arms; the wooden trough arm is a weekend project. Kids can hold the stopwatch and log the numbers.

## Apparatus (Bill of Materials)

- 1 **head tank** — a 20–60 L bucket or tote, or a large funnel on a stand, mounted so the water surface sits a **fixed, measured height** above the tube outlet (1.0–1.5 m is plenty; more head = more flow and a stronger signal)
- **Tube set (same inner diameter and same length across arms):**
  - **A — straight copper tube**, e.g. 8–10 mm ID × 50–100 cm
  - **B — spiral copper tube**, same ID and same developed length, coiled around a cylinder or, if you can, a cone — the closest cheap stand-in for the kudu-horn shape. A pre-coiled copper coil is ideal. Record the coil diameter and pitch.
  - **C — straight glass tube**, same ID and length (a glass tube is the material control; if unavailable, use a smooth rigid plastic tube, but real glass is the source's material)
- **Optional D — wooden conduits (the craft arm):** two troughs or bored wooden pipes of the same cross-section and length — one straight, one with a spiral groove cut or angled baffles set along its length. This is the arm that lands in the Dim Lumber Woodworking guild and tests the same claim with the material Schauberger actually worked in.
- A **mark on the tank** at the start water level, so every run starts from the same head
- **Bucket** of known volume (or weigh the water) + **stopwatch**
- **Thermometer** (water temperature — viscosity changes with temperature, and the source also claims vortex flow cools water; a measurable side-claim)
- **Phone camera** for evidence

## Protocol (steady flow at fixed head)

1. **Fill and mark.** Set the tank at a measured height above the outlet. Mark the starting level. Every run starts at that mark; refill to it between runs.
2. **One arm at a time**, same fittings, same outlet height, same tube length and ID. Change nothing but the tube.
3. **Run:** open the outlet (or just start the flow). Once flow is steady (2–3 s), collect the entire outflow in the bucket and time it. Record **volume / time = flow rate (L/min)**. Also record water temperature.
4. **Repeat each arm 3–5 times**, alternating arms (A, B, C, A, B, C, …) so drift, temperature, and tank level cancel out. Record every number — including the bad runs.
5. **Head-loss arm (optional but sharper):** if you can rig a vertical standpipe or a clear tube on the tube inlet, measure how high the water stands in it during flow. Height difference between arms at *the same flow rate* is the pressure-drop difference, in centimetres of water.
6. **Wood arm:** same procedure with troughs D (straight) and D' (spiral-grooved). Wood is rough and leaks; accept a coarser measurement and compare only wood-straight vs wood-spiral with the same method.
7. **Note the flow regime.** Estimate the flow speed (flow ÷ cross-section) and note whether you are in the slow (laminar-ish) or fast (turbulent) range. The claim is specifically about **high** flow — so if the effect exists, it should be *absent* at low flow and *appear* at high flow. A result that is flat across the whole range, or present equally at low and high flow, argues for artifact.

## Pass / fail criteria (pre-registered)

- **PASS (the shaping claim shows up):** spiral tube B sustains **≥20% higher flow than straight tube A at the same head**, as a mean of ≥3 alternating sessions, **and** the effect is *larger at higher head/flow than at lower*, **and** the wood arm (D vs D') agrees in direction. → The 1952 result replicates at home scale. Report the magnitude honestly; it will not be "negative resistance" unless you actually measure a spiral tube flowing faster than a frictionless straight duct of the same head, which you should state explicitly if you see it.
- **PASS (material claim):** copper A sustains ≥10% more flow than glass C at equal geometry, consistently. → The material-influences-friction claim replicates.
- **FAIL:** B and A within ±10% at all heads (and D/D' likewise). → The spiral-pipe friction anomaly does not reproduce at home scale; log it honestly. **Skeptic's Star** material. This is a real, valuable result: it would mean the foundation claim of the vortex lineage is not reproducible with simple apparatus.
- **INCONCLUSIVE:** run-to-run spread within one arm exceeds 15%, or leaks/temperature swings/tank-level drift dominate the signal.

Report both claims **separately**. A material result and a shape result are independent findings, and either can stand alone.

## What would change the verdict

- A modern, instrumented rerun (calibrated differential pressure transducer + electromagnetic flow meter) that reproduces the 1952 curve would move the claim out of "unreplicated" — that is the natural second-stage dossier. A home result should be read as a **screen**, not a hydraulic measurement.
- A clear null at home, repeated by several households, is strong evidence that the 1952 chart was an artifact — and that is worth publishing as loudly as a positive.

## Feedback loop

- Log every attempt (including failures and abandoned rigs) in the results log below.
- ≥2 independent attempts → update status to `replicated` / `refuted` / `inconclusive`; cross-link to the Schauberger death certificate and to dossiers 001, 004, 008.
- Share: Replication Yard, Permies post, Aetherforce energy / water strands.

## Results log

- *(none yet — open for the first replicator.)*
