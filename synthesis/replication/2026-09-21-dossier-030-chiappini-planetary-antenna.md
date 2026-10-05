---
name: Dossier 030 — Chiappini Planetary Antenna (D-Field VHF Antenna)
description: Replication dossier for testing the D-field "Planetary Antenna" claim — that a 49 cm VHF antenna built from electric-displacement (D) field theory matches or beats a conventional reference antenna in the 2 m amateur band — via a home-build with SWR and range endpoints. Home-replicable (~$15–30).
---

# Dossier 030 — Chiappini Planetary Antenna (D-Field VHF Antenna)

**Status:** protocol_ready
**Created:** 2026-09-21
**Primary source:** `translations/2026-09-18-planetary-antenna-d-field-chiappini-es.md` — "Antena Planetaria (Planetary Antenna)," a full ES→EN translation of Carlos Alejandro Chiappini's viXra preprint (viXra:2110.0093, 2021-10-17), with the complete construction guide and D-field theory appendix.
**Origin URL:** https://vixra.org/pdf/2110.0093v1.pdf (verified live 2026-09-21: HTTP 200, 687,183 bytes)
**Discovered by:** the practicality engine's energy-field scan, 2026-09-21 (translation surfaced by the Translation Curator, 2026-09-18; scout-flagged `buildable, reproducible` in `sources/2026-09-18-scout-a-langs-1.md` §6)
**Domain:** energy (radio / RF — off-grid communications)
**Tier:** sand
**Original guild:** Electricity (mirror complement — radiant / Tesla / LMD; the closest EM home in the Village guild list)

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-09-21-dossier-030-chiappini-planetary-antenna` · authored_at `2026-09-21` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## The Claim

Carlos Alejandro Chiappini (Argentina, amateur radio) claims that analyzing the
**electric displacement field D⃗** — the term Maxwell needed to make electrodynamics
complete, which he argues is omitted from standard teaching of propagation in vacuum —
yields a set of geometric constants (a length series `s1, s2, s3, …` derived from
`λ/2π`) that let a **very small antenna work well** in the 2 m amateur band
(144–148 MHz).

His device, the **"Planetary Antenna"** (nicknamed "El Protón" — the Proton), is a
single continuous wire shaped into **4 meridians and an equator**, like the wireframe
of a small planet. It mounts directly on a PL259 connector and radiates from a total
length of **49 cm**. The author explicitly rejects the quarter-wave reading: *"Ah, a
quarter wave! Absolutely not. The measurement comes from another method, based on the
analysis of the electric displacement vector."*

**A confound worth naming:** a quarter-wave in the 2 m band is λ/4 = 51.4 cm at
146 MHz, and ≈ 48.8 cm with a typical velocity factor of 0.95 — i.e. the 49 cm
radiating length is, numerically, essentially a quarter-wave. So a PASS on SWR would
**not by itself discriminate the D-field theory from ordinary quarter-wave resonance**.
The design's distinguishing feature is its *shape* (4 meridians + equator, a folded
spherical wireframe), not its length. A fair test therefore compares it against a
reference antenna of similar length, and treats a SWR PASS as evidence the antenna
*works*, not as evidence the *theory* is right.

**Reported performance (the author's own numbers, from Part 2 of the source):**

- Installed **5 m above ground**, connected to a **Baofeng UV-5R handheld at 1 W RF
  output**, the antenna achieves **~25 km range** in the middle of the city — the far
  station "knows that someone is modulating" but "understands very few words through
  the noise."
- At **5 W**, the far station at 25 km "understands the whole message, though a little
  noise accompanies the modulation."
- Within a **15 km** straight-line radius, the far station receives "very little noise";
  within **10 km**, "one can operate at 1 W with no noise."

**Honest status of the claim — stated up front:**

- **This is a single-author viXra preprint with 0 citations.** viXra is an unrefereed
  preprint server; the paper has not been peer-reviewed and the D-field theory
  underlying it is not accepted physics.
- **The author presents NO SWR data.** He says so explicitly: *"This document does not
  exhibit SWR measurements."* He had the SWR measured by "someone who works at a
  company, without my being present," and asks the builder to take charge of that
  themselves. This is unusually honest for the genre — and it means the central
  performance claim is **unverified**.
- **The author's own safety instruction is the test protocol:** *"Before testing the
  antenna on transmit, measure the SWR across the corresponding band… When the SWR
  approaches or exceeds 2, the equipment is in danger… If the SWR proves inadequate in
  every case, discard the antenna."*
- **The range numbers are anecdotal**, from a single operator in one city, with no
  controlled comparison against a reference antenna at the same power and location.
- **A null is a fine outcome:** if the antenna's SWR is poor or its range is no better
  than a stock rubber-duck or a reference quarter-wave ground-plane, the D-field
  design claim is retired honestly — and the builder has still learned antenna basics
  (resonance, SWR, polarization).

**Claimant:** Carlos Alejandro Chiappini (Argentina)
**Verification status:** unverified; no independent replication known to the archive; no SWR data published
**Mainstream position:** antenna design is well-understood from Maxwell's equations; a D-field-derived geometry that outperforms a conventional antenna of the same size would be a genuine anomaly. The reported range is plausible for a small 2 m antenna at 1 W with a good takeoff angle, so the claim is not extraordinary on its face — which is exactly why a controlled build-and-measure is worth doing.

---

## The Protocol — build it, measure SWR, compare range

The testable core: **if the D-field geometry does what the author claims, the antenna
should show acceptable SWR across 144–148 MHz and match or beat a reference antenna of
similar size at the same power and location.** If it doesn't, the claim is retired.

### Materials (~$15–30, assuming a 2 m handheld is already owned)

1. **63 cm of messenger wire** — the stiff wire from 75 Ω cable-TV coax (free, often
   found as offcuts). Cross-section and stiffness are what matter.
2. **1 male PL259 connector** (~$2–5).
3. **Twine + hot-glue** to fasten the wire crossings (or thin zip ties).
4. **Millimeter ruler** (a 50 cm steel rule is ideal) and **white electrical tape +
   fine black marker** for marking the segments.
5. **Pliers, long-nose pliers, soldering iron (35–45 W), 60/40 radio solder.**
6. **A 2 m handheld** (Baofeng UV-5R or any 144–148 MHz HT) — **1 W output preferred**
   for safety during testing.
7. **An SWR meter** for 2 m, or a **NanoVNA** (~$30–50) — this is the measurement
   instrument; without it the test cannot be run.
8. **A reference antenna** for comparison: the handheld's own stock rubber-duck, or a
   simple quarter-wave ground-plane.

### The build (from the source, Part 2)

1. **Mark the wire.** From one end: leave ~10 cm for the connector; then mark
   **4.1 cm** (half-meridian), **16.3 cm** (equator), **4.1 cm** (half-meridian), then
   three × **8.2 cm** (full meridians). Total radiating length **49 cm**.
2. **Bend the segments** into 4 meridians + 1 equator around a cylindrical form
   (~5.2 cm diameter) so the geometry is a wireframe sphere. Meridian planes are
   mutually perpendicular, and each meridian must advance in the equator's chosen
   direction ("coherently").
3. **Fit the PL259** with the south pole **8.3 mm** from the connector's start
   (`s3 = λ/(2π)³ ≈ 8.278 mm`).
4. **Tune.** If the geometry is imperfect, leave a short excess of wire past the south
   pole (start with ~1.5 cm) and trim **tenths of a millimeter at a time**, re-checking
   performance, to optimize resonance at the band center. The author never needed more
   than 9 mm of excess.

### Measurements (the endpoints)

1. **SWR sweep.** With a NanoVNA or SWR meter, sweep 140–150 MHz and record SWR at
   144.0, 145.0, 146.0, 147.0, 148.0 MHz, with the antenna in its final mounting
   position. **Record the environment** (height above ground, near walls/roof/chimney,
   indoors vs outdoors) — SWR depends on all of it.
2. **Reference comparison.** Measure the same SWR sweep for the reference antenna in
   the same position.
3. **Range test.** With a second station (a licensed operator, or a second HT with a
   known-good antenna), transmit at **1 W** on a simplex frequency and record the
   maximum distance at which the message is intelligible, for **both** the Planetary
   Antenna and the reference antenna, on the same day, same power, same locations.
   Repeat at least 3 times and average.
4. **Polarization/pattern check** (optional, if a field-strength meter is available):
   rotate the antenna and note the nulls.

### Controls and confounds (document all)

- **SWR is environment-dependent.** Measure in the final mounting position, and note
  everything nearby. Do not compare an antenna measured indoors against one measured
  outdoors.
- **Transmit safety.** Test on receive first. Only transmit once SWR < 2, and prefer
  1 W. A high-SWR transmit can damage the radio.
- **Licensing.** Transmitting on the amateur bands requires a license in most
  countries. Reception testing and SWR measurement with a VNA need no license. If
  unlicensed, do the SWR/geometry part and stop before transmitting.
- **Range is not a clean single variable.** Terrain, height, polarization, and the
  other station's antenna all matter. Comparing the two antennas **back to back on the
  same day from the same spots** is what makes the comparison meaningful.
- **Builder skill is a confound.** The author warns the geometry is sensitive to small
  errors; a sloppy build is not a fair test of the design. Note your build accuracy.

---

## Pass/Fail Criteria (pre-registered)

**PASS (supports the claim):**
- SWR **< 2.0** across at least 144–148 MHz in the final mounting position, AND
- Range at 1 W is **equal to or greater than** the reference antenna's range on the
  same day from the same locations (averaged over ≥ 3 runs), AND
- The result reproduces on a **second build** (the design, not one lucky wire)

**FAIL (refutes, for this family/bench):**
- SWR ≥ 2.0 across the band in every mounting position (the author's own discard
  criterion), OR
- Range at 1 W is clearly worse than the reference antenna's, OR
- Performance cannot be tuned into the band at all

**INCONCLUSIVE:**
- SWR acceptable but range comparison not run (e.g. unlicensed, or no second station)
- Fewer than 3 range runs, or conditions changed between the two antennas
- Build accuracy too poor to be a fair test of the design

**Honest note:** the most likely outcome for a careful home builder is **either a
modest PASS on SWR with an inconclusive range result, or a FAIL** — and both are
useful. A PASS on SWR plus a fair range comparison would be a real, if small, result
worth posting; a FAIL retires the D-field design claim honestly and still leaves the
builder fluent in SWR, resonance, and antenna mounting.

---

## What to Photograph/Record

1. **The build** — the marked wire before bending, the finished 4-meridian + equator
   shape on the PL259, close-ups of the crossings
2. **The mounting** — the antenna in its final position, with height and surroundings
   visible
3. **The SWR sweep** — screen photo of the NanoVNA or meter reading at each frequency
4. **The reference antenna** — same photos, same positions
5. **The range log** — date, time, power, frequency, both antennas, distances, and
   intelligibility (readable / partial / noise), for each run
6. **The build-accuracy note** — how closely the measurements were held

---

## Evidence Submission

Post to:
- Village "Post to Permies" quest evidence flow
- `living-library/synthesis/validations/` (markdown with photos, numbers, verdict)

Format:
```
Date: YYYY-MM-DD
Builder: [name]
Build accuracy: [measurements held to ±? mm]
Mounting: [height, indoors/outdoors, surroundings]
SWR @ 144/145/146/147/148 MHz: [values]
Reference antenna: [type] SWR @ same freqs: [values]
Range @ 1 W: [km] (Planetary) vs [km] (Reference), [n] runs
Verdict: [supports/refutes/inconclusive]
```
