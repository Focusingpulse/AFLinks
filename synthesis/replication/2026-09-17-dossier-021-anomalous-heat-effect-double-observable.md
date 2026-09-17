---
name: Dossier 021 — The Anomalous Heat Effect (LENR): A Double-Observable Replication Protocol
description: A replication dossier for the metal–hydrogen "anomalous heat effect" claim (Fleischmann–Pons lineage). Built on the corpus's central discrimination — heat claims and nuclear-product claims are different observables and require different instruments. Lab tier; specifies a checklist-gated calorimetry arm and a nuclear-product arm, so that any heat result is interpretable rather than a fourth decade of ambiguity.
---

# Dossier 021 — The Anomalous Heat Effect (LENR)

**Status:** protocol ready
**Domain:** energy (LENR / anomalous heat effect)
**Tier:** lab (above straw/sand — requires a calorimetry bench and gas-loading hardware; not home-replicable as stated)
**Source:** `paradigm/2026-09-13-positive-at-nucleus-negative-at-calorimeter.md`; `sources/2026-09-13-scout-report-1200.md`; `sources/scout-report-2026-09-16-1200.md`; `translations/2026-09-03-prometheus-lenr-reactor-it.md`
**Created:** 2026-09-17

---

## Source lineage

- **Fleischmann & Pons (1989)** — founding claim: electrolysis of D₂O on palladium produces excess heat. The origin of the anomalous heat effect (AHE) program.
- **The replication wars (1989–2010s)** — decades of excess-heat reports, each with contested calorimetry; the field's central controversies were fought over the calorimeter. `synthesis/2026-09-01-rotational-ether-vortex-torsion-lenr.md` traces the corpus's vortex/torsion reading of this lineage.
- **Project Callisto (2015–2024)** — >100 contributors, >40 formal and modified Fleischmann–Pons replications, released 2026-09-08. **Null at the calorimeter**, with prosaic explanations identified for most prior positives. Recorded in this Yard as `synthesis/validations/2026-09-17-lenr-callisto-null-campaign.md`.
- **Nature 2025 / Nature Communications 2026 (Berlinguette group, UBC)** — electrochemical loading enhances D–D fusion *rates* (~15% in the 2025 result), with direct neutron detection. Positive at the nucleus, with no net-energy claim by the authors.
- **JJAP 2025 (Yamauchi et al.)** — He-3 detected in Ni–Cu nanocomposites by NRA/TDS. Positive nuclear product.
- **Scientific Reports 2024** — >10,000× background neutron emission during acoustic cavitation of deuterated titanium powder in mineral oil. Positive nuclear product.
- **Scientific Reports 2026 (Alpha Ring International)** — proton–LaB₆ glow-discharge calorimetry showing integrated gain >1 under specific conditions, with tungsten-cathode controls that did not show it. In this Yard as `synthesis/validations/2026-09-16-lenr-lab6-glow-discharge-excess-heat.md`.
- **Hylenr Technologies (ICCF-27, 2026)** — 32-element signatures claimed in a hydrogen-loaded Ni–Pd lattice. **Watch only:** press and conference presentation, no peer-reviewed paper, no independent replication. A claim, not a validation.

## Status

`protocol` (draft; no attempts yet under this protocol)

## The claim (as asserted by the source)

A metal–hydrogen system — Pd/D, Ni–Cu/H, Ti/D — driven out of equilibrium by electrolysis, gas loading, glow discharge or acoustic cavitation can:

**A. release more thermal energy than is supplied to it** (the energy claim), and/or
**B. host nuclear reactions at rates far above bare-nucleus expectations** (the nuclear claim), evidenced by neutrons, helium, or transmutation products.

**Honest framing — the corpus's own selection (paradigm report 12):** these are **two claims with two observables**, and the field's historical error was conflating them into one banner.

- The **energy** claim is tested by **calorimetry**.
- The **nuclear** claim is tested by **particle detection and isotopic analysis**.

They are compatible: a 15% enhancement of a fusion rate that is itself negligible for power purposes produces detectable products and negligible heat. "LENR is real" was a blending move that collapsed the two; selection keeps them separate. We hold no brief — the test is the point.

## Why it matters

This is the single highest-stakes discrimination in the corpus. The Yard currently holds two LENR validations and no LENR protocol, which means a reader sees *findings* about this claim without ever seeing *what a fair test of it looks like*. This dossier supplies that. It also encodes a general rule the Yard should carry into every heat-anomaly entry: **match the observable to the claim.** A heat claim needs calorimetry that survives a prosaic-explanation checklist; a nuclear claim needs products detected by standard methods. Conflating them is how four decades were spent confusing the record.

## Replicability: `lab` (not home)

This is honestly above the Yard's straw/sand tiers. The discrimination is cheap in principle and expensive in practice, because the *checklist* — not the apparatus — is what makes a heat result interpretable.

- **Cost (order-of-magnitude estimates, not vendor quotes):** isothermal or Seebeck calorimeter ~$500–2,000; electrolysis cell and electrodes ~$100–300; D₂O and Pd stock ~$200–600; neutron detection is the expensive arm (a He-3 tube and moderator run into the thousands; some university labs will run samples). A calorimetry-only first rung may be reachable under ~$3,000; the nuclear arm is realistically institutional.
- **Safety:** moderate to high — deuterium gas handling, DC power in a wet cell, and (in the cavitation variant) sonication of metal powders. Follow institutional lab practice; this dossier is not a safety document.
- **Accessibility:** bench lab with temperature control, a way to log electrical input and thermal output simultaneously, and — for a credible result — someone other than the experimenter to hold the analysis key.

## Apparatus (Bill of Materials)

### Arm A — heat (the interpretable first rung)

1. **Cell:** sealed electrolysis cell with a Pd (or Pd-alloy) cathode and Pt anode; or a gas-loading chamber with temperature and pressure logging.
2. **Calorimeter:** isothermal (heat-flow) or Seebeck-type, calibrated against a resistive heater of known dissipation — the calibration is the instrument.
3. **Power measurement:** four-wire DC input measurement (voltage across and current through the cell) — not supply-side readings.
4. **Temperature logging:** redundant sensors (≥2, independently calibrated), logged at fixed intervals, with the sensor identities blinded to the analyst.
5. **Cathode mass and composition:** recorded before and after, by an independent party, on a balance adequate to the claimed mass-loss scale.
6. **Gas handling:** recombination accounting — the cell's evolved gas must be measured or catalytically recombined; unaccounted recombination is a known false-positive source.
7. **Humidity and ambient logging:** room temperature, humidity, and barometric pressure at the calorimeter.

### Arm B — products (the interpretation arm)

1. **Neutron detection:** He-3 proportional counter (or BF₃) with moderator, plus a background run of equal duration — or access to a facility that will run a sample.
2. **Isotopic analysis:** SIMS or NRA/TDS on the cathode before and after, for deuterium loading ratio and for He-3, tritium, or transmutation products.
3. **Gamma spectroscopy:** to test for the gamma signature a fusion claim would generally predict, and to check the background trend claimed in the orgonomic/cavitation corners of the corpus.

## Protocol (Arm A — heat, checklist-gated)

### Setup

1. Calibrate the calorimeter by resistive heating at three power levels; record the instrument's response function and its drift over hours.
2. Install the cell, seal it, and run a **blank electrolysis** at the intended current with a non-absorbing cathode (e.g. Pt or Ni) for the full intended duration. This establishes the cell's own thermal and chemical behaviour.
3. Log everything — input power, thermal output, ambient, cathode mass, evolved gas — at fixed intervals for the entire run.

### Procedure

1. Run the **blank** (control cathode), then the **Pd/D₂O** condition, alternating order across at least three replicate runs each.
2. For each run, compute the integrated energy balance (thermal output ÷ electrical input) using the calibrated response function — never the raw sensor readings.
3. At the end of each run, have an independent party weigh the cathode and analyse the evolved gas before any energy figure is interpreted.

### Controls (pre-registered — the Callisto checklist)

Before a positive heat result may be read as anomalous, **all** of the following must be closed and documented:

1. **Isothermal control** — the calorimeter was calibrated and the run was isothermal, not simply "well insulated."
2. **Recombination accounting** — evolved H₂/D₂ was measured or recombined, and its chemical energy is included in the input.
3. **Sensor validation** — sensors were independently calibrated and their identities blinded to the analyst.
4. **Hydriding enthalpy** — the loading energy (and any hydride phase change) is accounted for in the balance.
5. **Power-accounting** — four-wire measurement at the cell, with all lead and contact losses accounted for.
6. **Contamination** — cathode provenance checked for prior loading or impurities that could store chemical energy.
7. **Blank** — the non-absorbing-cathode blank was run at the same power and duration.

## Pass / fail criteria (pre-registered)

**PASS (supports the energy claim):**
- Integrated energy balance **> 1.0 beyond the calibrated uncertainty**, in replicate runs, **with all seven checklist items closed and documented**, **and** with the effect absent from the blank.

**FAIL (refutes the energy claim under these conditions):**
- Balance = 1.0 within uncertainty, or
- Any unclosed checklist item fully accounts for the apparent excess, or
- The effect appears in the blank.

**INCONCLUSIVE:**
- Balance > 1.0 but one or more checklist items are open — this is the honest verdict for most of the historical record, and it must not be reported as a pass.
- Calibration instability, sensor drift, or a run shorter than the cell's thermal time constant.

**Arm B (products), reported separately:** a positive neutron or He-3 result under the protocol is a **nuclear** finding. It does not confirm the energy claim, and must be recorded under its own heading.

## What the corpus already found (so a replicator is not starting blind)

- **Callisto:** >40 replications, null at the calorimeter, with prosaic explanations for most prior positives.
- **Alpha Ring 2026:** excess heat in a proton–LaB₆ glow discharge under specific conditions, with an independent-material control (tungsten) that did not show it; every author is affiliated with the company that built the system (disclosed competing interest); no nuclear signature reported.
- **Nature 2025/2026:** fusion-rate enhancement with neutron detection, with the authors themselves framing it as tabletop fusion research, not energy production.
- **JJAP 2025:** He-3 in Ni–Cu nanocomposites.
- **Sci Rep 2024:** cavitation neutrons.
- **Hylenr:** an unreplicated claim.

The honest expectation under the checklist above is a **null heat result** unless every item is closed. The value of running it anyway is that the nuclear arm and the heat arm can then be read against each other in a single, pre-registered frame — which is what the field has never done.

## Feedback loop

- Log every attempt here, including negative and inconclusive ones — the negative is the result.
- ≥2 independent attempts with closed checklists → verdict. Cross-link to the Callisto validation and to the nuclear-product validations.
- Share with the Aether Force LENR strand and the Replication Yard; a null is as publishable in this Yard as a positive.

## Attempted-by / results log

- *(none yet — open for the first replicator.)*

---

## Source Documents

- `paradigm/2026-09-13-positive-at-nucleus-negative-at-calorimeter.md` — the two-observable selection, Callisto's scope, the positive nuclear-product results.
- `sources/2026-09-13-scout-report-1200.md` — Callisto discovery and the prosaic-explanation list.
- `sources/scout-report-2026-09-16-1200.md` — verified-source table (Nature Communications 2026, Callisto, Brillouin, ENG8) and the upgrade ledger.
- `sources/scout-report-2026-09-15.md` — source-status table (Nature 2025 verified; Callisto domain-down note).
- `synthesis/validations/2026-09-17-lenr-callisto-null-campaign.md` — this run's tip-jar record for Callisto.
- `synthesis/validations/2026-09-16-lenr-lab6-glow-discharge-excess-heat.md` — Alpha Ring.
- `synthesis/validations/2026-09-16-lenr-he3-nanocomposite-nuclear-signature.md` — JJAP He-3.
- `callisto_report_entries.json` — chapter catalog for the Callisto report suite (`07-replications.pdf`, `08-novel-experiments.pdf`, `09-conclusions.pdf`).
- `translations/2026-09-03-prometheus-lenr-reactor-it.md` — the corpus's Italian LENR reactor thread (context).

## Related Quests

- `synthesis/replication/2026-09-14-dossier-017-orgone-accumulator-tot.md` — the other long-running temperature-anomaly claim that never got a matched-control test; the same "match the observable to the claim" discipline applies.

## Notes

This dossier tests the **claim**, not a particular device, and its primary product is a **checklist** rather than an apparatus. The discrimination it encodes — heat claims need calorimetry that survives the checklist; nuclear claims need products — is the corpus's own correction to forty years of argument, and it should be inherited by every future heat-anomaly dossier regardless of which device is proposed. A negative result is as valuable as a positive one — log it honestly.