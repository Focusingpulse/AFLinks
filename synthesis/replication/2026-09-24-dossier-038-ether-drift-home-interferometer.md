---
name: Dossier 038 — Ether-Drift Anisotropy (Home Michelson Interferometer)
description: "Home/homelab-scale test of the ether-drift claim: a laser Michelson interferometer with ~1 m arms, rotated through eight positions, looking for the 180°-periodic fringe modulation the classical ether hypothesis predicts. Reaches claims of the large kind (≳25 km/s) and says plainly that it cannot reach the modern cavity bounds. The ether rail's first dossier."
---

# Dossier 038 — The Ether-Drift Anisotropy Test

**Status:** protocol ready
**Domain:** ether / vacuum (optical anisotropy — the archive's largest pillar, previously unrepresented in the Yard)
**Tier:** sand (homelab bench, ~$250–500; an afternoon to build and align, an evening to run)
**Source:** `synthesis/2026-09-21-verification-rail-methodology.md` §3.2 (Daneš 1985, Czech psychotronika rail); `synthesis/2026-09-17-verification-turn.md` §4; `synthesis/2026-09-24-ether-drift-danes-1985-czech.md` (companion validation record)
**Created:** 2026-09-24

> **Authorship:** agent_id `agent-6791a657-6924-416e-8d80-fe2efb532fad` · agent_name `Navigator` · job `replication-seeder` · lineage `agent-6791a657-6924-416e-8d80-fe2efb532fad -> replication-seeder -> 2026-09-24-dossier-038-ether-drift-home-interferometer` · authored_at `2026-09-24` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Source lineage

- **Michelson & Morley (1887)** — the founding experiment: a rotating interferometer, arms at right angles, looking for a fringe shift as the apparatus turns through the putative ether. Reported null; historically the expected signal was ~**0.4 fringe** at an assumed 30 km/s drift.
- **Dayton Miller (1921–1933)** — the persistent non-null: repeated observations at Mount Wilson reporting a positive, seasonally varying drift of a few km/s. Never reproduced by another group at that scale.
- **Kennedy–Thorndike (1932), Brillet–Hall (1979), and the modern optical-resonator era** — each successive generation tightened the null. Cryogenic cavity experiments (2000s–2010s) bound any anisotropy around **10⁻¹⁷**, roughly *eight orders of magnitude* below anything a home instrument can see.
- **Josef Daneš (1985, Czechoslovakia)** — *Za tajemstvím éteru*: Michelson–Morley-type experiments run inside the **radio-amateur movement**, with **drift claimed as detected**. 192 pp, reviewed by Joachim and Prosek; full English translation in the corpus (2026-09-18). Magnitude, arm length and controls are **not established** in the corpus reading available to this lane — see the companion validation record.
- **The Russian etherodynamics school** — Atsyukovsky's collected works landed complete in the archive (vixri.ru, 2,222/2,222, 2026-09-23); the corpus also holds GPS/geostationary-satellite drift claims and a 1974 Stuttgart ether-wind item. Same claim family, large-magnitude form.
- **The claim under test here:** the vacuum is a medium; motion through it produces a **directional anisotropy** in the propagation of light, detectable by a rotating interferometer as a fringe modulation with a **180° period in rotation angle**.

## Status

`protocol ready` (no attempts yet; the instrument is buildable, not built)

## The claim (as asserted by the source)

That a laboratory on Earth is **moving through a medium**, and that the motion shows up as an orientation-dependent difference in the round-trip light time along two perpendicular arms. On the classical (ether) reading the fringe difference between the two orientations is

```
ΔN(θ) ≈ (2L / λ) · (v/c)² · cos 2θ
```

with `L` the arm length, `λ` the wavelength, `v` the drift speed, `θ` the rotation angle. At `L = 1 m`, `λ = 650 nm` that is:

| Assumed drift speed | Predicted fringe amplitude |
|---|---|
| 30 km/s (Earth's orbital motion) | **0.031 fringe** |
| 100 km/s | **0.34 fringe** |
| 300 km/s (typical galactic-frame figure) | **3.1 fringe** |
| 370 km/s (CMB-frame motion) | **4.7 fringe** |

The modern consensus measured null; the corpus's non-null reports (Miller's few km/s, Daneš's claimed detection, the etherodynamics school's larger figures) are of the **large** kind. That is the whole reason a kitchen-table test is worth running: **a home instrument cannot see a tiny drift, but it can see a large one — and the claims in this archive are large.**

**Honest framing:** We hold no brief — the test is the point. The mainstream expectation is **null**, and this dossier pre-registers that expectation alongside the claim. A positive result here would not by itself overturn a century of cavity experiments; it would be a home-scale anomaly in the *same class* as Miller's and Daneš's, and would need a laboratory before it meant anything. A negative result would not "disprove the ether" — it would close the *classic large-drift form* of the claim, at a stated sensitivity, and say nothing about any effect below that. Both outcomes are publishable numbers.

## Why it matters

- **It is the archive's biggest pillar with no practical entry.** `Challenges to the Standard Model` holds 64,634 documents and `Aether, Light & Electricity` 1,893; the ether-drift lane was *completed* by the scouts on 2026-09-23 (vixri.ru 2,222/2,222) and had **zero** Yard records before this dossier. The corpus's own rail names "*Daneš's ether drift: independent replication with modern interferometry*" as an open rung.
- **It is the cleanest falsifiable core of an enormous doctrine.** Whatever the ether school claims about cosmology, the operational prediction is one number on one rotating table.
- **It teaches the sensitivity ladder honestly.** This is the archive's best example of a test that is *discriminating* rather than merely controlled: it separates large-drift claims from small ones, and it teaches a reader to ask *what magnitude a claimed effect would have to have for my instrument to see it.*
- **The apparatus is reusable.** A working 1 m interferometer is a general-purpose instrument: it measures thermal expansion, vibration, refractive index of air, and the wavelength of a laser.

## Replicability: `home/homelab`

- Build cost: **~$250–500** (optics dominate; the rotation stage is cheap)
- Time: one afternoon to build and align, one evening to run a full rotation series
- Skill: comfortable laser/optics alignment; patience for thermal settling
- Safety: **low-voltage laser, moderate eye risk** — a 1–5 mW class-3R beam must never be viewed directly or via a mirror; align with the beam below eye level, wear laser goggles matched to 650 nm, and box the beam path

## Apparatus (Bill of Materials)

### Core optics
1. **Laser module** — 650 nm, 1–5 mW, collimated diode module (a second 532 nm module is the wavelength-discrimination control). ~$10–25 each
2. **Beamsplitter** — 50/50 non-polarising cube, 20 mm, mounted. ~$30–60
3. **Mirrors** — two front-surface (dielectric or enhanced-aluminium) flats, λ/8–λ/10, on kinematic mounts. ~$40–100 the pair
4. **Beam expander + screen** — 10× microscope objective or a f=50 mm lens, plus a white card or ground-glass screen to project fringes. ~$15–30
5. **Baseplate** — 600 × 400 mm aluminium tooling plate or 18 mm MDF (aluminium strongly preferred for thermal stability), drilled for the mounts. ~$40–80

### Motion and reference
6. **Rotation stage** — lazy-susan bearing with **eight mechanical detents 45° apart**, or a stepper + index mark, mounted under the baseplate so the *whole interferometer* turns as one rigid body. ~$25–50
7. **Reference line and azimuth marks** — tape on the floor or bench marking the lab frame (used by the 90° control below)
8. **Tilt/level indicator** — a small spirit level or a phone inclinometer, logged per position (the null test for platform wobble)

### Detection
9. **Fringe detection** — USB webcam pointed at the projected fringe pattern (analysis by FFT/phase fit), **or** a photodiode + Arduino counting fringe crossings. ~$20–40
10. **Thermometer** — ambient + near-baseplate, logged with every reading. ~$10

### Enclosure and safety
11. **Blackout cloth / foam drape** — encloses the whole beam path against air currents, draughts and room light
12. **Laser goggles** (650 nm), beam-stop or beam dump, tape and card baffles
13. **Notebook or logger** — the pre-registered analysis script must be written *before* the rotation runs

## Protocol

### A. Build and align
1. Assemble the Michelson interferometer on the baseplate: arms of **equal length, L ≈ 1.0 m**, mirrors at the far ends, beamsplitter at the corner.
2. Expand the output beam and project the fringes onto the screen; adjust for **fringe visibility > 0.5** (clear dark/bright contrast).
3. Enclose the whole path. Clamp the baseplate to the rotation stage so nothing shifts when the stage turns — **verify by rotating 360° with the laser on: the fringe pattern must return to the same position and visibility at every detent.**

### B. Noise floor first (do not skip this)
4. With the apparatus stationary, log fringe position for **≥ 30 minutes**. Compute σ.
   - σ ≤ **0.02 fringe** → proceed.
   - σ between 0.02 and 0.05 fringe → usable but state it; the reach is reduced (see thresholds).
   - σ > **0.05 fringe** → **stop and fix the instrument** (thermal drift, air currents, mount flex, table vibration). An apparatus that cannot hold 0.05 fringe cannot test a 30 km/s claim, and reporting otherwise is how a null becomes an artefact.

### C. Rotation series
5. One **series** = 8 detents × 5 min dwell, recording mean fringe position at each detent. Rotate **clockwise for even series, counter-clockwise for odd series** — this cancels any artefact tied to the rotation mechanism's own direction.
6. Run **≥ 8 series** across at least two sessions on different days (the classical prediction also has a diurnal and annual modulation; a single evening cannot see it).
7. Log, per series: date/time, ambient temperature, baseplate temperature, tilt reading, and the room-frame azimuth of the zero detent.

### D. The discriminating control — apparatus turned 90° in the room
8. Move/rotate the entire apparatus so its zero detent points **90° away from the first configuration**, re-align to visibility > 0.5, and run **4 more series**.
9. Fit every series with the same pre-registered model: `fringe(θ) = a + b·cos(2θ + φ)`.
   - A **real** anisotropy is a property of the lab's motion through the medium: its phase **φ, expressed against the room**, should be **unchanged** when the apparatus is turned 90° in the room.
   - A **mechanical** artefact (mount flex, platform tilt, a mirror that shifts at a detent) is a property of the apparatus: its phase locks to the **apparatus frame** and therefore rotates 90° with it.
   This is the single most useful measurement in the protocol. Without it, a positive result is uninterpretable.

### E. Wavelength control (optional, if the 532 nm module is fitted)
10. Repeat two series at 532 nm. A genuine anisotropy scales as `1/λ` — **~1.22× larger** at 532 nm than at 650 nm. Most mechanical artefacts do not scale with wavelength at all.

## Pass / fail criteria (pre-registered)

**PASS — supports a large-drift claim:**
- Fitted amplitude **≥ 0.05 fringe** (≈ 38 km/s-equivalent at L = 1 m, λ = 650 nm; ≈ 25 km/s if the noise floor is 0.02), **and**
- the 180°-periodic modulation reproduces across **≥ 8 series** with a stable phase, **and**
- the phase does **not** rotate with the apparatus in step D (it tracks the room), **and**
- amplitude scales with `1/λ` in step E if that control was run.

**FAIL — no large drift at the stated sensitivity:**
- Fitted amplitude **< 0.02 fringe** with consistent phase across series → no anisotropy at the ≳ **25 km/s** level (state the exact reach from the measured noise floor). This closes the classic Michelson–Morley form of the claim and the archive's large-magnitude non-null reports. It says nothing about smaller effects.

**INCONCLUSIVE:**
- Noise floor **> 0.05 fringe**, or visibility lost, or the fringe pattern does not return to the same position at every detent (the stage is flexing the instrument).
- Modulation present but **phase-locked to the apparatus** in step D → an apparatus artefact; report it as such and do not file it as an anomaly.

## What this test cannot do (stated so a null cannot be over-read)

- It reaches **≈ 10⁻⁸** in `(v/c)²` terms. The best modern cryogenic optical-resonator experiments reach **≈ 10⁻¹⁷** — about **eight orders of magnitude** further down. A null here therefore constrains nothing that those experiments have not already constrained far more tightly.
- Its value is therefore (a) **public and reproducible** adjudication of the *large* claims the archive actually holds, (b) a **worked lesson in sensitivity** for every other dossier in the Yard, and (c) a **reusable instrument**.
- A null result is **not** evidence against any ether model that predicts a smaller effect, and not evidence against any model whose observable is not optical anisotropy.

## Feedback loop

- Log every attempt here, including failed builds, alignment failures and unusable noise floors.
- **≥ 2 independent attempts → verdict**; cross-link to a quest card (proposed; the Tutor lane authors cards) when one exists.
- Share: the Replication Yard; the Aether Force ether/energy strand; amateur optics and radio-amateur groups (Daneš's own lineage — the radio amateurs are the natural replicators, and an RF variant of the same test is a legitimate second protocol).

## Source documents

- `synthesis/2026-09-21-verification-rail-methodology.md` §3.2 + ref [6] — the Czech rail and the open interferometric rung.
- `synthesis/2026-09-17-verification-turn.md` §4 — verification culture's two poles; why a public test beats a sealed one.
- `paradigm/2026-09-22-1989-is-now-a-dossier-not-a-legend.md` Thread 4 — the ether-drift corpus completing (vixri.ru 2,222/2,222; Atsyukovsky; 1974 Stuttgart ether-wind item).
- `synthesis/validations/2026-09-24-ether-drift-danes-1985-czech.md` — the companion validation record (this dossier's reason to exist).
- `library_feed.json` → `latest_translations` — the Daneš translation's own index entry (date, languages, file). Primary `translations/2026-09-18-za-tajemstvim-eteru-behind-the-mystery-of-ether-cs.md` is **cited but not carried by this repo's tree**; no number in this dossier is taken from it.

## Related

- **Dossier 032 — Bovis scale calibration** (`R = UB(×2 dial) / UB(standard dial)`): the same family of question — *does the instrument track the world, or the document?* Here the dial is the interferometer and the swapped scale is the apparatus frame.
- **Dossier 005 / 026 / 029 — blind geopathic mapping, water dowsing, psi-track dowsing**: the other "does the instrument see anything at all" tests in the Yard.
- **Dossier 016 — wood acoustic resonance**: the Yard's other physics-measurement bench test.

## Notes

- **Build the analyser before the experiment.** The pre-registered fit (`a + b·cos 2θ`) and the noise-floor rule are what make this a test rather than a demonstration; write the script and fix the thresholds first, then build.
- **The 90° control is not optional.** Every historical non-null MM report that failed to replicate is suspected of exactly the artefact this control catches.
- **A negative result is a result.** Log it with the measured sensitivity — "no anisotropy at ≥ 25 km/s, 8 series, 90° control clean, 532 nm consistent" is a finished experiment, and the first one the archive has ever published on its largest doctrine.
