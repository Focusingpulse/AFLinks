---
name: Geometric Resonance — A Pre-Registered Self-Replication Returns Null on Prime-Ratio Frequency Pairing (Sutton, 2026)
description: A self-published apparatus reported that prime-integer frequency ratios produce stronger, sharper, more coherent interference than composite ratios. The same author then ran a pre-registered 1,200-trial replication with pure sine waves and got null on seven of eight metrics, diagnosing the original effect as an odd-harmonic artefact of square waves — and withdrew the claim. A negative result, honestly reported, on the frequency-and-geometry rail.
---

# Validation — Prime-Ratio Frequency Pairing: The Author's Own Replication Returns Null

**Domain:** geometric resonance / frequency-ratio effects (the "integer and shape matter" family)
**Recorded:** 2026-10-02 (Replication Watch)

## What was claimed

That **frequency pairs whose ratio is prime-integer produce measurably stronger and more coherent interference patterns than pairs whose ratio is composite** — i.e. that the *arithmetic* structure of a frequency ratio, and not merely its value, changes the physical outcome in an analog wave circuit. The apparatus was framed as a **"torsion ring" PCB** with twelve radial analog cells, driven by GreenPAK-generated **square-wave frequency dividers**, and the reported effects (Sutton, *Prime Wave Theory — V3 Experimental Results*, Zenodo, doi 10.5281/zenodo.20637347) were:

| Metric | Claimed effect (prime ratios) | Reported significance |
|---|---|---|
| Amplitude (Vpp) | **+28 %** | significant |
| Sharpness (spectral power ratio) | **+18 %** | significant |
| Coherence (cross-correlation) | **+22 %** | significant |

The theoretical companion is *Prime Resonance Theory: From Factorisation to Frequency* (Zenodo, doi 10.5281/zenodo.20541350). This is the archive's **geometric/frequency-resonance rail** — the family of claims that integer ratio and geometry, rather than magnitude alone, govern a resonant outcome. The rail previously had **zero** validation records.

## Who replicated it, when

**Adrian "Tusk" Sutton** (Tusk Innovations), the **original author** — i.e. this is a **self-replication**, the strongest available form of a claim-holder testing their own result. The corrigendum is dated **19 September 2026**; the v1 preprint and the replication both date to 2026.

**Provenance, stated plainly because it bears on how the record should be weighted:** the work is a **single-author self-published Zenodo preprint**, not peer-reviewed. The corrigendum's own acknowledgements state that the replication "was designed with input from **Grok (xAI)** for experimental methodology review, and executed with **Nagaπ (OpenClaw)** for automation and analysis," with a project member listed as "Nagaπ, Co-Prime Mate." The archive's own QC layer has flagged AI-generated *citation* layers before (the AFSCET hallucinated bibliography, the Hecquet/Benhadid Zenodo genre); this document is **not** of that kind — it has a pre-registration, a stated sample size, a decision tree, raw data paths, and firmware — but its authorship is unusual and it is filed accordingly.

## Method, as reported

The replication — **"Plan C"** — was designed as a **pre-registered falsification test** of the V3 claims, and the methodological upgrades are the point of the record:

1. **Pure sine waves replace square waves.** Two **AD9833 DDS modules** (THD < −60 dBc) replaced the GreenPAK square-wave dividers — removing the odd-harmonic comb that was the suspected confound.
2. **Shared master clock.** Both DDS modules driven from a **single 25 MHz TCXO**, so the frequency ratios are exact, not crystal-tolerance approximations.
3. **Pre-registered analysis plan** — primary hypothesis, test pairs, sample size, exclusion rules and decision tree fixed **before** data collection.
4. **Blinded, randomised pair ordering** — 30 test pairs (8 prime:prime, 9 composite:composite, 6 prime:composite, 3 non-coprime controls, 4 irrational controls) in randomised order across **5 complete blocks**.
5. **Automated capture** — Python-controlled Arduino + **Rigol DS1054Z** over SCPI, removing operator bias.
6. **Scale and correction** — **1,200 trials, 8 metrics**, Bonferroni-corrected α = **0.00625**.

## Result, as reported

**Seven of eight metrics returned null**, including all three V3 headline metrics:

| Metric | PP mean | CC mean | p | Cohen's d | Significant? |
|---|---|---|---|---|---|
| RSP (dB) | −28.82 | −28.97 | 0.70 | 0.03 | No |
| Crest factor | 1.544 | 1.551 | 0.56 | −0.05 | No |
| **Spectral flatness** | **0.0045** | **0.0036** | **0.0003** | **0.28** | **Yes** (survives correction) |
| Envelope regularity | 0.291 | 0.293 | 0.71 | −0.03 | No |
| Cross-correlation peak | 0.874 | 0.872 | 0.43 | 0.06 | No |
| Phase coherence | 0.802 | 0.798 | 0.34 | 0.07 | No |
| Vpp | 0.445 | 0.454 | 0.40 | −0.07 | No |
| Vrms | 0.360 | 0.360 | 0.98 | −0.002 | No |

- **The one surviving metric is not claimed as a win.** Spectral flatness was significant (p = 0.0003, d = 0.28) but was **not** a pre-registered primary metric, and the author attributes it to **hardware limitations**: channel crosstalk of −7 to +8.5 dB in the resistive summing network (so CH1 and CH2 were not independent), an erratic DDS B output (0.14–0.68 V vs DDS A's 0.62–0.66 V), and no buffer amplifiers. He asks for independent replication on properly isolated hardware before it is interpreted.
- **Sanity checks passed** — non-coprime control pairs (e.g. 9:6) matched their reduced forms (3:2) as expected (p > 0.17); irrational ratios (√2, φ, e/2, π/2) showed no significant difference from either stratum; no block-order effects.
- **Diagnosis:** the V3 result is attributed to the **odd-harmonic content of square waves**. A prime:prime pair has harmonic series sharing no common frequency below their product, giving many distinct spectral peaks; a composite:composite pair shares harmonics at lower order, which overlap and partially cancel. **This is a mathematical property of harmonic combs and coprimality, not a physical property of the medium.**
- **The claim is withdrawn.** "The original V3 claims should be considered unreliable"; the headline effects "should not be cited as evidence."

**The author's own boundary on the null, worth keeping:** the framework is "not falsified in domains where it was not tested." Plan C tested a **passive, linear** circuit — a resistive summer whose transfer function depends on frequency, not on the arithmetic of ratios. Domains where boundary conditions enforce integer quantisation — **acoustic cavities, vibrating strings, crystal lattices, EM resonant cavities** — were explicitly **not** tested. That is the correct place to draw the line, and it is drawn by the claimant, not by a critic.

## Confidence: medium-high that the document exists and reports this; low as independent evidence

**For it.**

1. **A pre-registered replication that refuted the author's own prior result and was published anyway** is the single most valuable artefact type in this Yard. It is the "publish the part of the positive that failed" rule carried out on itself.
2. **The method is stated in enough detail to be attacked and rebuilt** — DDS part numbers, clock, capture instrument, pair counts, block structure, correction method, data paths (`pre-registration.md`, `scripts/results/runs/`, firmware, circuit design all named).
3. **The apparatus's own limitations are disclosed by the author**, and the one surviving metric is explicitly *not* promoted. That is the opposite of the failure mode the Yard usually catches.
4. **The diagnosis is mechanistic and checkable**: remove the odd harmonics and the effect disappears.

**Against it.**

1. **Single author, self-published, not peer-reviewed, AI-assisted**, with an unusual authorship record. Filed as **single-source, unconfirmed.**
2. **The apparatus is a passive resistive summing network, not a resonant system.** The "torsion ring" is a PCB layout; the measurement is of an electrical sum of two oscillators. So this is a test of **linear superposition of pure tones** — not a test of any acoustic, geometric or cavity resonance claim. The archive's actual frequency/geometry claims (Helmholtz cavities, Chladni figures, spiral-pipe resonance) are untouched by it.
3. **No independent party has repeated Plan C.** Every number here is the author's.
4. **The one "significant" metric is, by the author's own account, likely an instrument artefact** — which means the honest summary is stronger than "7/8 null": **on this apparatus, with these channels, no ratio-class effect was demonstrated at all.**

## Source

- **Primary (the replication + corrigendum):** Sutton, A. *"Experimental Evidence for Prime-Ratio Superiority in a Physical Torsion Resonator Network."* **Zenodo**, v1→v2 preprint, published 2026-09-19 — https://zenodo.org/records/22843244 — doi **10.5281/zenodo.22843244**. Corrigendum file: `CORRIGENDUM.md` (8.8 kB) on the same record.
- **The original claim (withdrawn):** Sutton, A. *"Prime Wave Theory — V3 Experimental Results."* Zenodo — doi **10.5281/zenodo.20637347**.
- **Theory companion:** Sutton, A. *"Prime Resonance Theory: From Factorisation to Frequency."* Zenodo — doi **10.5281/zenodo.20541350**.
- **Code and data:** repository `nagapi2357-ui/Prime_Maxel-v3` (GitHub).
- **Prior in this Yard:** none — this rail had **0 validations** before this record. Adjacent but distinct: `2026-09-25-torsion-torsimetry-text-meaning-gao.md` (torsion as a *measurement instrument* claim, different question); `2026-10-01-scalar-wave-overunity-igf-weidner-2001.md` (Meyl's scalar/over-unity kit, resonance attributed to a Lecher line — the same "harmonic/resonant-line explains it" shape as this null).

## Honest framing

We hold no brief — the test is the point. **Recorded as attempted / measured / reported, and the negative is the content:** a claimant built an apparatus, reported a striking effect, then **pre-registered a replication that failed to reproduce it, found the artefact, and withdrew the claim in public.**

That is the cleanest thing that can happen on this rail, and the Yard should file it as a **model of how a null should be reported** — not "we saw nothing," but "we saw something, we worked out what it actually was (the square wave's odd-harmonic comb), and we removed it." The transferable lesson is the one the archive keeps needing: **when a frequency-ratio effect shows up, ask first what the *signal source* is putting into the spectrum.** A confound that is a mathematical property of the waveform is not a property of the medium, the geometry, or the ratio.

And the boundary the author himself draws is the honest one: **this null does not touch the archive's actual acoustic-cavity and geometric-resonance claims.** A passive resistive summer is not a cavity. If anything, the record makes the real test *cheaper to specify* — a Plan-C-shaped protocol (pre-registration, pure-tone sources, harmonic content verified, blinded ordering, corrected multi-metric analysis) is exactly the rig a Chladni-plate or Helmholtz-cavity claim would need.
