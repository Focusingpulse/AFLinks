---
name: Water / Non-Local Information — A Preregistered Replication of the "Excess Correlation" pH Effect Between Magnetically Paired Beakers (Radin & Brinsmead, IONS, 2026)
description: A claim that lived for a decade in one laboratory (Persinger's, at Laurentian) was given the Yard's own prescription — preregistration, an automated rig, a matched sham, and a different site. It came back positive at +0.0041 pH units, p = 0.005, with the sham at zero. Recorded as the water-information rail's first successful replication attempt, and as a small effect sitting near its own sensor floor.
---

# Validation — The Preregistered "Excess Correlation" pH Replication

**Domain:** water structure / non-contact information transfer (psi-adjacent)
**Recorded:** 2026-09-23 (Replication Watch, run 4)

## What was claimed

That two **physically isolated** volumes of water, each exposed to the *same* sequence of weak pulsed magnetic fields, develop an anomalous correlation — a shared response that no conventional coupling route explains. The claim carries a specific, testable form: when acid is added to a "local" beaker inside one toroidal coil, the pH of the magnetically paired "remote" beaker — a metre away, with nothing added to it — drifts **alkaline** at the moment of acid delivery.

The lineage is a single laboratory. Rouleau, Carniello & Persinger reported "excess correlations between magnetic field-paired volumes of water" (*Journal of Signal and Information Processing* **7**:136–147, 2016) and non-local pH shifts (*Journal of Biophysical Chemistry* **5**:44–53, 2014), with related claims for cell cultures, photochemical reactions and human EEG over the following decade. Radin's own paper states the problem plainly: these "entanglement-like" effects "have been reported only by researchers from a single laboratory at Laurentian University."

## Who replicated it, when

**Dean Radin** and **Erik Brinsmead**, **Institute of Noetic Sciences (IONS)**, Novato, California, USA. Funded by the **Bial Foundation**.

- **Preregistered:** https://osf.io/nt76h/overview
- **Published:** 20 May 2026, *Journal of Biophysical Chemistry* **17**(2), doi 10.4236/jbpc.2026.172002
- **Follows** the same author's pilot: Radin, D. (2025), "Independent Replication of an 'Excess Correlation' Effect in pH between Isolated Beakers of Water," *Journal of Biophysical Chemistry* **16**:15–29.

The sessions were run **by IONS research assistants, in a laboratory setting, by personnel not previously engaged in this line of research** — the authors' explicit attempt to remove the experimenter.

## Method

Concrete, and worth stating in full because the design *is* the finding here:

- **Apparatus.** Two Arduino boards. Board A energised two "halos" — 25.4 cm plastic hoops wound with 225 loops of 16-gauge copper — generating ~20 nT fields with fixed *primer* and *effector* pulse sequences. Board B logged pH and temperature and drove a liquid-handling pump.
- **Three 40 mL beakers** of Novato, CA tap water (low-TDS, mildly hard ~82 mg/L CaCO₃, pH ~7.5–8.5): **Local** (centre of halo A; receives acetic acid in experimental runs), **Remote** (centre of halo B; nothing added, ever), **Control** (between them; no magnetic exposure, nothing added).
- **Run structure (30 min).** 6 min baseline → 6 min primer sequence → 12 min effector sequence → 6 min baseline. Acid delivered to Local at t = 720 s, as the effector phase begins.
- **Sensors.** Atlas Scientific *Gen3 ISFET* pH probes, **0.001 pH resolution**, sampled at 0.5 Hz; a PT-1000 on Remote for temperature compensation.
- **100 runs pre-planned: 50 experimental interleaved with 50 sham.** The **sham** used identical equipment, protocol and statistics, but dropped the acid into a separate beaker beside Local — so electromagnetic, thermal and vibrational factors were matched and only the acid differed.
- **Primary endpoint, preregistered.** ΔD = mean(pH_remote − pH_control) over 0 to +120 s around the acid-drop anchor, minus the mean over −120 to 0 s. One-tailed permutation test, 20,000 permutations.
- **Built-in adversarial tests.** Two negative controls (anchor moved 430 s early; windows slid before the event); an 81-window sensitivity grid with max-statistic **family-wise error-rate** correction (2,000 permutations); a run-level mixed-effects model; a phase-split drift check; and run-order correlation.

## Result

**Positive, small, and time-locked.**

- Experimental mean ΔD = **+0.0034** pH units; sham = **−0.0007**; between-group difference **+0.0041**, one-tailed permutation **p = 0.005**.
- Sham runs showed no effect (p = 0.53). Both negative controls were null: far-anchor **p = 0.26**, far-pre **p = 0.27** — the effect appeared only in the windows flanking the actual acid delivery.
- Sensitivity grid: **global FWER-corrected p = 0.018**; **15 of 81** window pairs survived correction, **all** in the predicted direction, none opposed. The authors read a coherent positive region as signal rather than symmetric noise.
- **The preregistered secondary analysis was null.** The linear mixed-effects model gave an Epoch × Condition interaction of **p ≈ 0.48** — i.e. the shift was *not* sustained across the 12-minute effector phase. It is a narrow transient excursion of about two minutes, which is what the scalar endpoint was designed to catch and what the epoch model averaged away.
- Phase-split (the first 35 runs were not properly alternated, due to a miscommunication with the lab assistant): phase 1 Δ = +0.0050 (p = 0.063), phase 2 Δ = +0.0036 (p = 0.023) — similar magnitudes, arguing against monotonic drift.
- Run-order correlation: not significant (experimental ρ = −0.056, p = 0.70; sham ρ = −0.142, p = 0.33).
- Exclusions disclosed: one session dropped for incomplete pH logging; three sham sessions in which acid was accidentally dropped into Local — extra sessions were run so the final analysis held exactly 50/50.

## Confidence: medium-low for the *effect*; medium-high that *the test happened as described*

**What is strong here — and unusual:**

- **Preregistered before data collection**, with the prediction, endpoint, windows and analysis plan fixed in advance.
- **Run at a different laboratory by different personnel** from the originating (Laurentian) group — the single most important thing that had been missing from this literature.
- **A matched sham that behaves correctly**: the identical apparatus with the acid removed produced nothing.
- **Two negative controls that came back null**, plus an explicit multiplicity correction that the primary result survives.
- **Transparent reporting of its own defects** — the mis-sequenced first 35 runs, the accidental acid drops, the failed secondary model, the sensor-floor problem. Records that print their own gaps are the ones worth trusting more, not less.

**What keeps this out of "high":**

- **The effect sits 3× above a 0.001 pH sensor floor** (0.0034 pH units). The authors name this as their first limitation and say "caution is warranted." *ΔpH of three thousandths* is smaller than almost any real-world pH disturbance — a breath, a handling event, a drift in one probe.
- **The venue is a low-credibility publisher.** Scientific Research Publishing (SCIRP) has unverifiable metrics and is not indexed in Scopus or Web of Science, and **essentially the entire prior "excess correlation" literature — the claim being replicated — sits in the same publisher's journals.** A positive replication published by the same press that published the original is not a clean institutional break, even when the site and operators are new.
- **The replicator is a participant in the claimant's field.** Radin is a psi researcher at IONS with a prior positive pilot of this exact effect, and he performed the analysis. The *operators* were naive; the *analysis* was not blind.
- **No mechanism.** ~10 nT fields, beakers a metre apart, no obvious electromagnetic, thermal or chemical coupling route. The authors say so.
- **One site is not a field.** The claim was born in one laboratory and has now been tested positively in a second, by a group already invested in the first's result. That is progress, and it is not independence.

**The honest read:** this is a **single-source, unconfirmed** positive. The correct label is not "water has memory" and not "psi is real" — it is: *a preregistered, sham-controlled attempt to replicate an anomalous pH correlation produced a small positive result under good design, and the result is at the edge of the instrument's resolution.* A third laboratory, at a site with no stake in the claim, is the only thing that moves it further. The authors ask for exactly that.

**What would move it:** the same protocol run by a disinterested group with a pH modality that does not sit near its own noise floor (or a different observable entirely — conductivity, dissolved oxygen), plus independent environmental witness sensors as the authors propose.

## Source

- **Primary:** Radin, D. & Brinsmead, E. (2026). "Excess Correlation in pH between Magnetically Stimulated Beakers of Water: A Preregistered Replication." *Journal of Biophysical Chemistry* **17**(2). doi **10.4236/jbpc.2026.172002**. https://www.scirp.org/journal/paperinformation?paperid=151331 — full text read in this run.
- **Preregistration:** https://osf.io/nt76h/overview
- **Prior pilot:** Radin, D. (2025). *Journal of Biophysical Chemistry* **16**:15–29.
- **The claim being replicated (single-laboratory lineage):** Rouleau, N., Carniello, T.N. & Persinger, M.A. (2016), *J. Signal and Information Processing* **7**:136–147; Rouleau, Carniello & Persinger (2014), *J. Biophysical Chemistry* **5**:44–53.

## Honest framing

We hold no brief — the test is the point. Recorded as **claimed / preregistered / attempted / measured / reported**: a claim that had lived for a decade inside one laboratory was given exactly the treatment the Yard prescribes for such claims — write the prediction down first, automate the apparatus, build a sham that differs in one variable only, run it somewhere else with someone else's hands — and it came back **positive**, small, time-locked, absent in the sham and absent at shifted anchors.

That matters to this archive for two reasons. First, it is the **water-information rail's first successful replication record**; the rail's existing entries — Benveniste 1988 and the eighteen years of failed re-tests after it — are all records of tests that *failed*, and a pavilion that only holds failures reads as "this never works." Second, it is the rail's cleanest example of the Yard's own method working as advertised on a claim its community cares about.

The caveat belongs in the same paragraph as the result, not after it: **a positive replication is not a mechanism, a small effect near the sensor floor is not a large one, and the second positive test of a single-laboratory claim is still a claim about two laboratories.** The pilot is Dossier 028's problem restated — "who held the thermometer" — and this study's answer (nobody held it; a pump did) is what makes it worth filing. The next rung is a group with no stake in the answer.
