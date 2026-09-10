---
name: Dossier 008 — Vortex Jet Turbine Energy Test
description: "Home-scale test of the Schauberger/Herbrand dynamic-energy claim: a jet-shaped intake with spiral vortex induction extracts more power from flowing water than the altitude-head formula predicts."
---

# Dossier 008 — Vortex Jet Turbine Energy Test

**Status:** protocol ready
**Domain:** energy (water-power)
**Tier:** straw (home/homelab-scale, ~$120-200)
**Source:** translations/2026-09-09-schauberger-dynamic-hydroelectric-energy-es.md
**Created:** 2026-09-10

---

## The Claim

Two linked claims from the source document (Spanish technical analysis of Schauberger's 1930 Jet Turbine patent No. 117,749 and Ludwig Herbrand's Rheinfelden measurements, translated from giurfa.com/schauberger.pdf):

1. **Schauberger (patent 117,749, 1930):** a jet tube with screw-shaped ribs inducing a longitudinal vortex feeds a cone turbine with corkscrew blades. The ribs "promote a rotation which, according to actual observations, increases the velocity of the water jet and the efficiency of the machine." Supporting observation: the 1952 Stuttgart Pöbel/Schauberger pipe experiments, where spiral (kudu-horn) pipes showed friction *decreasing* with velocity.
2. **Herbrand (Rheinfelden, mid-1930s):** a generator with 50 m³/s flow and 1 m head reportedly delivered as much energy as one with 250 m³/s and 12 m head — attributed to the dynamic energy of fast-flowing water rather than pressure head. The document claims kinetic power scales with v² (E_kin = m/2 · v²), so raising velocity (via jet narrowing + vortex) multiplies output far beyond what head-based engineering extracts.

**The testable core:** At a *fixed* altitude head and flow rate, does adding (a) a jet-shaped restriction and (b) spiral vortex induction to a simple water turbine setup increase electrical output measurably compared to a straight-pipe control? If yes, by how much — and does it exceed the trivial gain explainable by the Venturi speed-up alone?

---

## Protocol

### Materials (home/homelab-scale, ~$120-200)

1. Water source with repeatable head: reservoir on a stand (e.g. 200 L tote) with **1 m drop** to the turbine, OR a garden hose/pump recirculating loop with fixed flow (a recirculating loop with a pump is the cleaner control — same flow every run)
2. Micro hydro generator/turbine: small 5-12V DC water turbine generator wheel (widely available, ~$20-40)
3. **Control intake:** straight PVC pipe, 3-4 cm diameter, ~1 m length
4. **Jet intake:** same pipe with a funnel/jet restriction at the outlet end (reducing to ~1-1.5 cm) aimed at the turbine wheel
5. **Vortex induction:** spiral ribs or an inserted spiral guide (wire coil / 3D-printed helix / angled vanes) inside the jet section, aligned to induce rotation in the flow direction
6. Multimeter (V, A) — two if possible
7. Power resistor bank (e.g. 10-50 Ω) as a fixed load
8. Bucket + stopwatch (to measure flow rate in L/s)
9. Thermometer (water temp — the source claims vortex flow cools water; a measurable side-claim)
10. Camera (phone) for evidence

### Setup

1. Fix the reservoir height (1 m head) and record it
2. Mount the turbine wheel so the jet hits the same spot in every configuration
3. Wire the generator to the fixed resistor load; connect multimeter(s) to log voltage (and current if a second meter is available)

### Procedure

Run three configurations, same head, ~5 runs each, alternating order to cancel drift:

- **A — Control:** straight pipe, no restriction, no ribs
- **B — Jet only:** restriction/funnel outlet, no spiral ribs
- **C — Jet + vortex:** restriction WITH spiral ribs/vanes

For each run:
1. Open the valve fully; let flow stabilize 10 s
2. Record voltage (and current) across the load for 60 s (note the average)
3. Measure flow rate: timed bucket fill at the outlet (L/s)
4. Measure water temperature at inlet and outlet

Compute electrical power P = V·I (or V²/R). Compute the conventional kinetic power available at the measured flow and jet velocity: P_kin = ½ · ṁ · v², using measured flow and the outlet velocity (from jet diameter and flow).

### Controls

- Same head, same valve position every run; verify flow rate is consistent within each config
- Alternate A/B/C order across runs (drift, temperature, battery effects)
- The jet-only condition B is the critical control: any C-over-B gain beyond measurement noise is the *vortex* effect; B-over-A is just the Venturi/jet effect
- Note: a jet raises velocity by *reducing* the effective flow area — check whether flow rate drops; if flow drops a lot, the comparison must be on total power, not velocity alone

## Pass/Fail Criteria

**PASS (supports claim):**
- Config C electrical output exceeds config A (straight pipe) by a clear margin (>15% average across runs, beyond run-to-run spread)
- AND C exceeds B (jet-only control) by >10% — isolating the vortex-ribs effect claimed in the patent
- AND flow rate did not drop enough to explain the gain (total power up, not just velocity)

**FAIL (refutes claim):**
- C ≈ B (within noise) — the spiral ribs add nothing; the patent's efficiency claim is not supported at home scale
- OR total power in B/C is *lower* than A (restriction throttles more than it gains)

**INCONCLUSIVE:**
- Flow varies >10% between runs, head not constant, or generator output too small/noisy to measure (<0.5 W)

---

## Evidence to Collect

1. Photo of all three intake configurations
2. Video of at least one run per configuration (wheel + multimeter visible)
3. Voltage/current readings per run (table)
4. Timed flow-rate measurements per config
5. Inlet/outlet water temperature per config (tests the cooling side-claim)
6. Head measurement photo (reservoir height)

---

## Honest Framing

This is a test of the CLAIM, not an endorsement. The Herbrand/Rheinfelden story is a single second-hand account from the 1930s, never independently verified; Schauberger's jet turbine was patented but not reliably documented in operation. The physics framing in the source (velocity-squared scaling) is real — E_kin = ½ṁv² is standard — but mainstream hydro engineering already accounts for it; the claim under test is whether vortex induction extracts *additional* usable power at fixed head and flow. A home rig cannot replicate Rheinfelden-scale claims; it can only test the mechanism's direction. If C ≈ B, the vortex-rib claim is weakened for home scale. If C > B consistently, that is a genuine anomaly worth escalating to a bigger rig.

Patent ≠ proof. A negative result is as valuable as a positive one — log it either way.

---

## Source Documents

- translations/2026-09-09-schauberger-dynamic-hydroelectric-energy-es.md (full translation: patent 117,749 text, Herbrand account, Pöbel/Stuttgart pipe experiments)
- living-library/synthesis/death-certificates/schauberger-vortex-repulsine-1951.json (the Repulsine wrong-turn record — this dossier tests the *turbine* line, not the Repulsine)

---

## Related Quests

- dossier-001-wasserwirbler.md (Schauberger vortex, household scale, water domain)
- dossier-004-hyperbolic-funnel-vortex.md (funnel vortex for aeration — this dossier tests power extraction, a different outcome variable)
- dossier-003-tesla-radiant-receiver.md (energy domain)

---

## Notes

The Repulsine (the classic Rocket-guild seed candidate) is lab-tier and not home-replicable — this dossier deliberately tests the *home-testable* member of the same Schauberger implosion family. Complements the **Rocket** guild (free energy / implosion) as its Aetherforce mirror.
