---
name: Dossier 059 — Scalar-Wave Overunity Energy-Balance Test
description: "Replication dossier for Konstantin Meyl's scalar-wave claim — that a low-voltage Tesla-replica kit yields over-unity efficiency (500–1000% claimed by the vendor; ~10 in his JSE paper) via scalar waves travelling at 1.5c. Home/homelab-buildable, ~$150–400 for a function generator or DDS, two coils and plates, and a two-channel power measurement. The endpoint is an energy balance, not a light: does more electrical power leave the receiver than enters the transmitter, measured at the same instant, with the error sources catalogued? Instrumented once at the IGF in 2001 (45%, no overunity) — the decisive two-channel sweep has never been published."
---

# Dossier 059 — The Scalar-Wave Overunity Energy-Balance Test

**Status:** protocol
**Domain:** energy (resonant wireless power transfer — the scalar-wave / over-unity claim)
**Tier:** straw (home/homelab, ~$150–400; needs a signal source, a two-channel measurement, and patience)
**Source:** forge/ACTIVITY.md — QC dossier **FAL-de-207-1/-2/-3**, "the Meyl scalar-wave apparatus + the complete German skeptic spine" (Forge memory commit 851def5; claims fe2b921 → 49c4046)
**Created:** 2026-10-01

> **Authorship:** agent_id `agent-6791a657-6924-416e-8d80-fe2efb532fad` · agent_name `Mr Navigator` · job `replication-seeder` · lineage `agent-6791a657-6924-416e-8d80-fe2efb532fad -> replication-seeder -> 2026-10-01-dossier-059-scalar-wave-overunity` · authored_at `2026-10-01` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Source lineage

- **Nikola Tesla (1856–1943)** — the wireless energy-transmission arrangement Meyl's kit is a "replica" of: an oscillator driving two elevated terminals coupled by a single long conductor, with Tesla's own reported observations of resonance and of effects that did not yield to conventional radio interpretation.
- **Konstantin Meyl (b. 1942), Germany** — professor of electrical engineering; the modern reformulation. Extends Maxwell's field theory with *potential vortices* (electric-field vortices) said to propagate as longitudinal "scalar" waves, decoupled from Hertzian transverse waves. Published as **Meyl, K., "Scalar Waves: Theory and Experiments," *Journal of Scientific Exploration* 15(2) (2001)** — claims (1) wireless electrical-energy transmission, (2) reaction of receiver to transmitter, (3) **free energy with an over-unity effect of about 10**, (4) transmission of scalar waves at **1.5× the speed of light**, (5) **inefficiency of a Faraday cage** at shielding scalar waves. Sells the **Experimental-Kit** demonstration set; the vendor documentation states *"Efficiencies of approximate 500% are measured"* and cites a 6 July 2000 control measurement at the **Technical University of Clausthal** averaging **1000%**, with received power at the middle pancake coil reported as ten times the transmitted power.
- **H. Weidner, E. Zentgraf, T. Senkel, T. Junker, P. Winkels — Institut für Gravitationsforschung (IGF), Waldaschaff, September 2001** — the instrumented replication. Reproduced the effects, then measured both sides: **19 mW in, 8.5 mW out, 45% efficiency, "Ein Overunity-Effekt wurde nicht beobachtet."** Resonance at **5.35 ± 0.1 MHz** against a circuit length of **18.8 m** (a vacuum half-wave would need 22.2 m); the report's working hypothesis is a **Lecher line** carrying ordinary transverse waves. See `synthesis/validations/2026-10-01-scalar-wave-overunity-igf-weidner-2001.md`.
- **Bruhn, TU-Darmstadt** — the theoretical counter-case: every solution of Meyl's *own* fundamental field equation together with his scalar-wave condition is **stationary**, i.e. moving scalar waves cannot exist inside his own system. Carried here as lineage, **not** as evidence about the experiment.
- **PLoS ONE 2021** — the genre's one peer-reviewed instrumented detection: a gamma spectrometer finding **thorium and uranium inside** "scalar energy" pendants. A different product line; recorded because it is what a rigorous instrument said when pointed at this market.

## Device-family watchlist (energy rotation, homelab tier)

- Scalar-wave / over-unity resonant kit (**this dossier** — homelab, ~$150–400).
- Water-vortex over-unity motor (dossier 031 — the rail's other energy-balance card, <50 €).
- Mini Tesla coil, near-field versus far-field falloff (dossier 053 — wireless power *without* an over-unity claim).
- Tesla radiant-energy receiver (dossier 003 — charge accumulation against a shielded control).
- Keppe motor, matched-load input power (dossiers 043, 047 — motor efficiency, not over-unity).

## Status

`protocol` (draft; no attempts yet)

## The claim (as asserted by the source)

A low-voltage replica of Tesla's wireless-transmission arrangement, driven by a function generator rather than a spark gap, draws a small amount of electrical power at the transmitter and delivers **more** electrical power at the receiver. The excess is attributed to **scalar waves** — longitudinal potential-vortex waves that pass through Faraday cages and travel at 1.5c — and is quantified: **500–1000%** in the vendor's documentation, **~10** in Meyl's peer-reviewed paper.

**In one sentence:** more power comes out of the receiver than goes into the transmitter, and the deficit is not an accounting error.

**Honest framing:** This is a claim from a professor of electrical engineering, published in a peer-reviewed journal and sold as a reproducible kit with documented experiments. The core arithmetic of the claim — η > 1 — is the single most consequential thing a bench can test, and it is the one thing the world's instrumented laboratories have not published a full sweep of in twenty-five years. We hold no brief — the test is the point.

## Why it matters

- **It is the rail's cleanest falsifiable.** Every other claim in this corpus needs an interpretation to dispute; this one needs a **power meter and two channels**. If η > 1 is real, it is the largest result in the archive. If it is not, the archive has a template for how the entire over-unity genre fails, at the bench, in an afternoon.
- **The Yard has no card of any kind on the scalar rail.** Dossier 053 measures falloff, dossier 003 measures charge accumulation, dossiers 043/047 measure motor efficiency. **None measures an energy balance on a device that claims to break one.** This is the hole.
- **The archive already holds both halves of the argument as documents** — Meyl's JSE paper and the IGF's instrumented refutation — and the QC layer has already assembled the German skeptic spine around them. The Yard's job is to turn that into a measurement a home experimenter can run.
- **It is the first electromedicine card whose endpoint is unambiguous.** No blinding is needed, no subjective rating, no surrogate marker: the endpoint is a ratio, and the ratio is either above 1 or it is not.
- **Its cost is the point.** The vendor's own documentation states that the kit was designed *so that it is reproduced as often as possible*, and the report we hold notes the decisive measurement is *"already written."* That is an invitation, not a research programme.

## Replicability: `homelab`

- **Build/obtain cost: ~$150–400.** A DDS signal generator (1–30 MHz, adjustable amplitude) **$30–120**; two spiral/pancake windings on plates (or a kit) **$40–150**; a sphere or ball terminal (metal spheres, or salvaged doorknobs) **$10–30**; interconnecting wire, **≈19 m** to reproduce the reported geometry; a **two-channel oscilloscope** (the cost driver — a used 100 MHz two-channel scope is $150–250, and a two-channel USB scope $60–150 is adequate here); current probes or a small non-inductive shunt; two matched LEDs and a resistor decade box for the calibrated output comparison; a dummy load (5 Ω and 50 Ω).
- **Safety: low-to-moderate, with three real rules.** (1) The kit is low-voltage by design (2–4 V), but a resonant tank with sphere terminals can develop **high RF potentials** — do not touch the terminals while driving, and keep fingers and instruments off the coils during a run. (2) Any mains-powered scope or generator is a mains-earth path; **use one isolation transformer or run from battery/USB power** so the measurement equipment does not become part of the circuit being measured. (3) RF burns and eye injury are not the hazards here; **self-deception is** — this is the card where a wrong probe placement manufactures a result, and the protocol is built against that, not against the device.
- **Accessibility:** an evening to build the two stages, an evening to calibrate, then roughly an hour per session. Three sessions on three days.

## Apparatus (Bill of Materials)

- **A signal source — DDS function generator**, sine output, **1–30 MHz**, adjustable amplitude, with a known output impedance. Record the output impedance on the label; every power calculation depends on it.
- **Two spiral (pancake) windings on flat plates** — the transmitter and receiver, as in the kit's geometry. A commercial spiral coil pair is acceptable and cheaper than winding accurately.
- **Sphere terminals** — one small metal sphere per stage, mounted on the coil lead. **Record the diameter**; the sphere capacitance is the reason the resonance sits where it does.
- **Interconnecting conductor, ≈19 m** of wire between the two stages (to reproduce the reported circuit length) — and a second, variable length (10–25 m) for the line-length sweep.
- **A two-channel oscilloscope** (or two RF power meters), **with two matched probes**. Both channels must be shown to read the same amplitude and phase on a common test signal before any measurement is trusted.
- **A non-inductive current shunt** (e.g. 0.1–1 Ω, low inductance) for measuring current without a probe's phase error; and **×10 low-capacitance probes** for voltage.
- **A dummy load** — 5 Ω and 50 Ω power resistors, plus a **resistor decade box** for matching the load to whatever the circuit wants.
- **Two matched LEDs plus a calibrated DC reference** — the IGF's output-comparison method, used *only* as a cross-check on a real power measurement, never as the primary endpoint.
- **A Faraday cage** — a metal box or mesh large enough to enclose the receiver, for the shielding sub-claim.
- **A thermometer and a notebook** — for ambient temperature and every reading; the notebook is the instrument that catches most of the artifacts.

## Protocol (energy balance, pre-registered)

**Phase 1 — calibrate the instruments before touching the claim.**

1. **Write the pre-registration sheet before running anything:** the source, its output impedance and amplitude setting; the coil geometry and sphere diameters; the conductor length; the frequency range to be swept; the load; the criteria below; and the two-channel method to be used. Photograph it.
2. **Cross-calibrate the two channels.** Drive both probes from the **same** signal and confirm they agree on amplitude and phase across the band. **A probe-dependent error is indistinguishable from an over-unity result**, and this step is what excludes it.
3. **Establish the noise and pickup floor.** With the transmitter running but the receiver **disconnected from any load**, measure the induced voltage on the receiver channel with the probe in its measurement position, then with the probe's ground moved to a **star point at the source**. Record both. Any difference is pickup entering the measurement loop, not power leaving the device.
4. **Establish the source's true output.** Terminate the source into the dummy load and confirm that the power it actually delivers equals the power the instrument's own display implies. **Do this before believing any ratio computed from that display.**

**Phase 2 — reproduce the demonstration, blind to nothing, and record exactly what is seen.**

5. **Run the vendor's own demonstration first** and photograph it: the receiver's lamp/LED lit, the resonance found, the amplitude setting. **The point of this step is honesty — the claim says something striking happens on the bench, and it usually does.** Record it as observed.
6. **Then measure the resonance.** Sweep frequency and find the current maximum in the interconnecting conductor. **Record the frequency.** (The 2001 report found **5.35 ± 0.1 MHz** against 18.8 m of conductor.) Note where the maxima and minima fall along the conductor — that pattern is the first thing that tells you whether you are looking at a resonant line or something else.

**Phase 3 — the energy balance.**

7. **Instrument both sides at the same instant.** Transmitter: voltage across, and current through, the driven coil (current via the shunt, not a clamp probe). Receiver: voltage across, and current through, the **load** — not the open-circuit terminal voltage. The instantaneous product on each side is the power. **No ratio is computed from a DC voltage reading across a load resistor, and none from an instrument's internal display.**
8. **Sweep the load.** Take the ratio at several load values (matching the source, matching the line's characteristic impedance, and a decade box sweep). **The vendor's own method infers over-unity from a receiver DC voltage exceeding the transmitter's** — that comparison is between two different impedances and produces a false ratio by construction. **The load sweep is what exposes it.** Record η against load.
9. **Sweep the conductor length** (10–25 m) at fixed drive and record where the resonance moves. If the resonance tracks the conductor length as a transmission line predicts, that is the Lecher-line hypothesis confirming itself and there is no anomaly to explain.
10. **Cross-check the output with the LED method.** Match two LEDs against a DC-fed twin and record the inferred output power. **Report it beside the two-channel figure and label which is which.** If the LED method and the two-channel method disagree, the disagreement is the finding.
11. **Have someone else set the drive amplitude and frequency** (from a randomised list of 6 settings, three resonant and three off-resonance) so the measurer does not know which setting is which. Score all six.

**Phase 4 — the shielding sub-claim, as a separate question.**

12. **Run the receiver inside the Faraday cage** at resonance and record η again. The claim is that a cage does **not** shield the transfer — so a cage that *does* attenuate it argues against the scalar account and for ordinary coupling. **Report the attenuation in dB**, not as a verdict.

**Phase 5 — repeat.**

13. **Repeat the whole set on at least 3 separate days**, re-running the channel cross-calibration each day. An over-unity result that appears on one day and not another is an artifact of that day's setup, and the archive wants to see the three days.

## Pass / fail (pre-registered)

- **PASS (the claim survives — extraordinary, needs the fullest follow-up):** **η > 1 repeatably at resonance, in ≥ 2 of 3 sessions**, with (a) both channels cross-calibrated the same day, (b) the load swept and the ratio surviving the sweep, (c) the LED cross-check agreeing with the two-channel figure, and (d) the result confirmed by a **second, independent method** — a calorimetric measurement of the load, or a calibrated RF power meter. Report as an extraordinary result requiring a second builder before anything is concluded.
- **PASS (the claim is refuted — the expected, complete result):** **η < 1 at every load and every session**, the resonance frequency tracking the conductor length, and the transfer attenuating inside the Faraday cage. Reported as the expected result, not a failure (**Skeptic's Star**).
- **FAIL:** η > 1 appears only in the load-sweep arms where the load impedance differs from the source's — i.e. the effect is real *in the measurement* and is an impedance-mismatch artifact, not power gain.
- **INCONCLUSIVE:** only one side instrumented; output power inferred only from LED brightness; no channel cross-calibration; no load sweep; no pre-registration; or the resonance was never located.
- **ARTIFACT:** the ratio tracks the **probe position, probe ground, or cable routing** rather than the device; the receiver "output" is measured open-circuit at the sphere terminal rather than across the load; the current is measured with a clamp probe whose phase is unverified; a **second signal generator, oscillator, or USB hub** is the real source; the reading is taken while the hand or an instrument body is near the coil; the receiver channel is picking up the transmitter **radiatively** (confirmed by moving the receiver away without changing the wiring — if the ratio follows the pickup, it is pickup).

## Evidence

Photo of the built two stages with a ruler showing coil diameter, sphere diameter and conductor length + the pre-registration sheet (source, impedance, sweep range, load, criteria) photographed before the first trial + the two-channel cross-calibration record on a common signal + the pickup-floor record (probe at the load versus probe grounded at the source) + the source's true-output check into the dummy load + the vendor demonstration photograph + the frequency sweep with the resonance marked and the conductor-length sweep + the full load sweep with η per load + the LED cross-check beside the two-channel figures + the Faraday-cage attenuation in dB + the blinded six-setting scoring sheet + the per-session channel re-calibration + the artifact/void checks reported whether or not they void the run.

## Confounds (named in advance)

- **The vendor's own inferred method is the first confound.** Over-unity is asserted from a receiver **DC voltage** exceeding the transmitter's, across a rectifier and a load resistor. That compares two different impedances and squares a voltage ratio; it produces apparent gain from ordinary mismatching. **The whole protocol is built to bypass it.**
- **LED nonlinearity and the eye.** LED brightness is not linear in power, and "the LEDs looked the same brightness" is a human judgement. **Use the LED method as a cross-check with a DC-fed twin, never as the endpoint.**
- **Probe and ground topology.** A two-channel measurement of a resonant RF circuit is where a result is manufactured or destroyed. **Cross-calibrate the channels, use a shunt for current, and re-run with the probe ground moved to a star point at the source.** A ratio that changes when the probe lead is rerouted is a measurement-loop artifact.
- **Radiative pickup.** At 5 MHz a receiver coil will pick up the transmitter without any conductor at all. **Move the receiver and see whether the ratio follows.** If it does, the transfer is ordinary coupling.
- **A second oscillator in the room.** USB hubs, switchers, monitors and fluorescent ballasts all radiate in this band. **Turn the rig off and confirm the receiver channel goes quiet.**
- **Earth loops.** Mains-powered instruments add a ground path that can carry real current between the two stages. **Run the source from battery or USB, or isolate.**
- **DC rectification on the measurement channel.** A probe or meter that rectifies will report a DC voltage on an AC node and invite the arithmetic that produced the original claim. **Check every meter's AC/DC behaviour on a known sine before trusting it.**
- **Load impedance versus source impedance.** A matched-load measurement and a mismatched one give different ratios for a device with no gain at all. **This is why the load sweep is mandatory, not optional.**

## Verdict rules

η > 1 repeatably at resonance in ≥ 2 of 3 sessions, surviving the load sweep, agreeing with the LED cross-check and confirmed by a second measurement method → **the claim survives** (extraordinary; needs a second, independent builder before it means anything). η < 1 at every load and session, with the resonance tracking conductor length and the Faraday cage attenuating the transfer → **the claim is refuted at the bench** — the expected, complete result. η > 1 only in the mismatched-load arms → **the apparent gain is an impedance-mismatch artifact, not power gain.** One channel instrumented, LED-only output, no cross-calibration, or no load sweep → **inconclusive, not a refutation.** A ratio that moves with the probe lead's routing or that persists with the transmitter off → **artifact; re-instrument before scoring.**
