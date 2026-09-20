---
name: Organizational Coherence Cosmology (DEBA) — A Complete Cosmology Without Postulates (fr→en)
description: "Full English translation of Michel Debailleul's 'DEBA - Une Cosmologie Complète sans postulat, Des réponses aux Anomalies' (Dec 23 2025, Zenodo record 18033125). Stochastic field theory in a pre-metric configuration space; bubble-universes emerge via organizational-coherence condensation from an atemporal, acausal primordial vacuum. Claims to explain dark matter (coherence gradients, no particle), dark energy, JWST early supermassive black holes (Type I coherence attractors), CMB Cold Spot + Axis of Evil (inter-bubble interfaces), and the Hubble tension (directional coherence gradient) without ad hoc hypotheses — with explicit falsifiability criteria. Author: geophysicist, Université Libre de Bruxelles. Translated from French by Translation Curator, 2026-09-20. 8/8 chunks, complete."
---

Organizational Coherence Cosmology:
    A Stochastic Field Theory of the Emergence of Bubble-Universes
                                                      Michel Debailleul
                                                   michel.debailleul@yahoo.fr
                                     Geophysicist, Université Libre de Bruxelles, Belgium

December 23, 2025

Abstract
          We present a cosmological framework (DEBA) founded on stochastic field theory in a
      pre-metric configuration space. Bubble-universes emerge through organizational coherence
      condensation from a primordial vacuum characterized by an atemporal, non-metric and
      acausal substrate. The framework provides quantitative predictions for dark matter, dark
      energy, early supermassive black holes, and CMB anomalies without ad hoc hypotheses.
      Physical laws and constants emerge locally within each bubble rather than being
      universal. We derive the DEBA master equation from functional Langevin dynamics,
      define the organizational flash as a stopping time, and compute instanton trajectories
      via large deviation theory. All predictions are falsifiable by current and future
      observations.


---


1     Introduction
Recent observations challenge the ΛCDM cosmological paradigm at several scales:
— CMB anomalies: The Cold Spot, the Axis of Evil (low-ℓ multipolar alignments), and the hemispheric
         asymmetry lack explanation within standard inflation [1].
— Early supermassive black holes: JWST observations of quasars at z > 7 with masses M ∼
         10⁹ M⊙ require implausible accretion scenarios or primordial seeds [2].
— Hubble tension: Measurements of H₀ diverge by more than 5σ depending on method and sky
         direction [3, 1].
— Large-scale structures: Massive early structures at the epoch of recombination exceed
         standard hierarchical formation timescales.
The ΛCDM model addresses these problems through parameter adjustments or by introducing new components
(variable dark energy, non-Gaussianity). We propose an alternative: these phenomena emerge
naturally from the dynamics of organizational coherence in configuration space.
The DEBA framework (Dynamique d'Émergence de Bulles Organisationnelles — Dynamics of the Emergence of
Organizational Bubbles) postulates that:
1. The primordial vacuum is an atemporal, non-metric, acausal configuration space (C, µ) with a finite
         measure µ(C) < ∞.
2. Bubble-universes emerge via a stochastic coherence condensation governed by a functional
         Langevin equation.
3. Physical laws, constants, and space-time emerge locally within each bubble.
4. Dark matter and dark energy are manifestations of inherited organizational coherence.
This paper derives the mathematical formalism, establishes the physical predictions, and specifies the
falsifiability criteria. The organizational structure is illustrated in Figure 1.

2     Mathematical Framework
2.1    Configuration space and coherence measure
  We define C as a measurable space of organizational configurations with a finite measure µ.
No metric, time parameter, or causal structure exists on C.

1
   The organizational field Φ : C × R+ → R depends on the configuration x ∈ C and an ordering
parameter τ ≥ 0 (which is not physical time).


---


2.2    DEBA master equation
   The field dynamics follow a functional stochastic differential equation:

                                      ∫
                                                    δV [Φ]             √
                       dΦ(x, τ) = −C   K(x, y)                dµ(y) dτ + 2D(x) dWτ (x)                               (1)
                                       C           δΦ(y, τ)

where:
    — K(x, y): non-local coherence kernel encoding correlations
    — V [Φ]: functional organizational potential
    — D(x) > 0: local diffusion intensity
    — Wτ (x): Wiener process indexed by τ and x
    — C > 0: coupling constant
    The organizational potential is:
                                                 ∫
                                                     λ 2      ²
                                         V [Φ] =       Φ − ϕ₀   − ϵΦ dµ                                              (2)
                                                  C 4

This bistable potential admits two stable states (Φ = ±ϕ₀) and allows phase transitions.

2.3    Local coherence and the organizational flash
   The local coherence at configuration x is:
                                                          (∫                            )
                                           s(x, τ) = σ             K(x, y)Φ(y, τ)dµ(y)                            (3)
                                                                C

where σ : ℝ → (0, 1) is a monotone sigmoid function.
    For a threshold Θ ∈ (0, 1), we define the coherent set:
                                                 BΘ (τ) = {x ∈ C | s(x, τ) ≥ Θ}                                   (4)

with organizational mass MΘ (τ) = µ(BΘ (τ)).
   The global resonance is:                     ∫∫
                                     R[Φ(·, τ)] = CR                   Φ(x, τ)Φ(y, τ)dµ(x)dµ(y)                  (5)
                                                            C       C
   Definition (Organizational Flash): The flash time is the stopping time:
                                τflash = inf {τ ≥ 0 | R[Φ(·, τ)] ≥ Rcrit and MΘ (τ) ≥ µmin }                       (6)
   At τflash, the emerging bubble-universe is:
                                                 U = {x ∈ C | s(x, τflash) ≥ scrit }                               (7)


---


2.4    Instanton trajectory and large deviations
    In the weak-noise limit D(x) → 0, Freidlin-Wentzell theory provides trajectory probabilities
via the action functional:
                                                                             ²
                                        1 T
                                         ∫ ∫            (∫          )
                                                   1                   δV
                                A[Φ] =                    ∂τ Φ + C K      dµ dµ dτ                                   (8)
                                        2 0 C D(x)                     δΦ
   Trajectories have asymptotic probability:
                                                       P[Φ] ≍ exp(−A[Φ])                                            (9)
   The instanton trajectory Φ∗ minimizes the action among all paths reaching the flash threshold:
                                                        A[Φ∗ ] = inf A[Φ]                                          (10)
                                                                         Φ∈E

where E is the set of trajectories satisfying Eq. (6).

2
                                           BAOBAB Schema – DEBA Cosmology
                                                        G ,Λ ,c     i   i i
                                                               Emergent time ti

Our                Bubbles:
                                                                                         F = {u1 , . . . , un }

FLASH                µ(A) > µcrit

A4

Attractors:              A3
                                 Coherence
                                 basins                                     τ ↗
                                                                                 A2

A1

PRIMORDIAL VACUUM (C, µ)
                                                     Atemporal • Acausal • Non-metric

Figure 1 – BAOBAB schema of DEBA cosmology. The primordial vacuum (C, µ) (bottom) is an atemporal,
acausal, non-metric configuration space. Organizational progression along the parameter τ (upward, not
physical time) forms coherence attractors Ai along the trunk. When the threshold µ(A) > µcrit is reached,
the organizational flash occurs, fragmenting into bubble-universes {ui } (upper branches). Each bubble
inherits a portion of Φflash determining its local constants (Gi , Λi , ci ) and its emergent internal time ti .
The Big Bang is the internal-physical description of this flash event.


---


3     Physical Emergence
3.1    Local laws and constants
    The flash condensation at τflash fixes the configuration Φ(x, τflash), determining:
                                                                  (i)
                                                               Geff = G[Φi ]                                         (11)
                                                                (i)
                                                               Λeff = L[Φi ]                                         (12)
                                                                (i)
                                                               ceff = C[Φi ]                                         (13)

via the functional maps G, L, C. Each bubble Ui possesses distinct local constants.

3.2    Emergent time
    Physical time emerges as an internal ordering within the bubble Ui :
                                                            dti = fi [Φi ] dτ                                        (14)

where fi > 0 depends on the local coherence structure. The Big Bang corresponds to the internal-physical
description of the flash event.

3.3    Dark matter
    Dark matter originates from the inherited coherence profile. The dark matter density field is:
                                                      ∫
                                          ΦDM (x) ∼      K(x, y)L(i) (y)dµ(y)                                        (15)
                                                                 C

where L(i) encodes the internal physical regime of bubble i.
    Dark matter is neither particle nor field but a gravitational manifestation of coherence gradients.
Its distribution depends exclusively on the portion of coherence inherited at emergence.

3.4    Dark energy
    Dark energy corresponds to the global persistence of coherence during expansion:
                                          ∫
                                     (i)
                                   Λeff ∼     g(s(x), s(y))L(i) (x)L(i) (y)dµ(x)dµ(y)                                (16)
                                                 C

3
where g(s(x), s(y)) quantifies the coherent interaction between regions of low coherence.
    Dark energy is not a true energy but a geometric consequence of the conservation of coherence
in an expanding space-time. Dark matter and dark energy are complementary manifestations
of the same coherence structure.

3.5    Black holes: Types I and II
    Type I (internal instability): When local coherence drops below the instability threshold:

s(x) < sinst =⇒ Type I Attractor                                      (17)

These correspond to early supermassive black holes forming from coherence pockets before
the establishment of the classical metric. This explains the JWST observations of quasars at z > 7.
     Type II (inter-bubble interface): At interfaces between bubbles:


---


Σ(x) = si (x)sj (x),   Σ(x) > Σcrit ,   ∇Σ(x) ≠ 0                             (18)

These persist as coherence-exchange memory between bubbles, generating CMB anomalies (Axis of
Evil, Cold Spot).

4     Observational Predictions
4.1    CMB signatures
    Inter-bubble interfaces (Type II) produce:
    — Cold Spot: Coherence deficit region, ∆T /T ∼ −10⁻⁴
    — Axis of Evil: Directional gradient ∇Σ(x) in low-ℓ multipoles
    — Hemispheric asymmetry: Coherence asymmetry between bubble hemispheres
    Prediction: These anomalies are correlated, not independent statistical fluctuations.

4.2    Early structures
   Type I attractors allow structure formation before standard hierarchical growth:
   — Massive galaxies at z ∼ 10 − 15
   — Supermassive black holes at z > 7 without super-Eddington accretion
   — Large voids at the epoch of recombination
   Prediction: The mass distribution of black holes shows a directional anisotropy correlated with
CMB anomalies.

4.3    Hubble tension
    If H₀ depends on the inherited coherence profile, directional variations appear:

H₀ (n̂) = H₀,mean + δH₀ (n̂)                                       (19)

where δH₀ is correlated with ∇Σ.
    Prediction: Measurements of H₀ show a systematic directional dependence aligned with the Axis of
Evil.

4.4    Dark sector
    Predictions for dark matter:
    — No particle detection (non-particle)
    — Fine structure in gravitational lensing maps
    — Correlation with CMB anomaly directions
    Predictions for dark energy:
    — Λeff varies with local coherence structure
    — The equation of state w deviates from −1 in regions of low coherence

4
5     Falsifiability
    DEBA is falsified if:
    1. CMB anomalies are statistically independent
    2. Increasing observational precision eliminates the correlated anomalies
    3. Early massive structures are explained without non-trivial initial conditions
    4. Particle dark matter is detected
    5. No directional dependence of H₀ correlated with CMB anomalies
    6. Black hole formation follows Eddington-limited accretion at all z

5.1    Comparative table

Observable               ΛCDM                      DEBA
                              Cold Spot      statistical fluke    Type II interface
                              Axis of Evil             unexplained                 ∇Σ(x)
                              SMBHs at z > 7      seed problem       Type I attractors
                              DM particle        WIMPs/axions            none (coherence)
                              H₀ tension         measurement error           directional ∇Σ

Table 1 – Observational comparison between the ΛCDM and DEBA frameworks.


---


6     Numerical Simulation
    DEBA is simulable via:
    1. Stochastic sampling of coherence distributions on C
    2. Percolation models at the µmin threshold
    3. Propagation of correlations in emergent space-time
    4. Joint multi-observable confrontation
    The Monte Carlo implementation of Eq. (1) on discretized C reproduces bubble emergence, flash
nucleation, and fragmentation into disjoint domains.

7     Discussion
   The DEBA framework differs fundamentally from ΛCDM:
   — No initial singularity: The primordial vacuum is atemporal; the temporal singularity is an artifact of
       the bubble's internal description.
   — No fine-tuning: Constants emerge from stochastic condensation, not from imposed boundary
       conditions.
   — Local physics: Laws and constants are not universal but specific to each bubble.
   — Finite structure: All physical quantities are bounded; infinities are excluded.
   DEBA provides a unified explanation for phenomena requiring separate ad hoc hypotheses in
ΛCDM. The framework is mathematically rigorous (derived from established stochastic field theory), conceptually
coherent (from configuration space to observables), and empirically testable.

8     Conclusion
    We have presented a complete cosmological framework based on organizational coherence in a
pre-physical configuration space. Bubble-universes emerge via stochastic condensation governed by a
functional Langevin equation. The organizational flash is rigorously defined as a stopping time,
with instanton trajectories minimizing action functionals.
    This framework naturally explains:

5
    — CMB anomalies (Cold Spot, Axis of Evil) as signatures of inter-bubble interfaces
    — Early supermassive black holes as Type I coherence attractors
    — Dark matter and dark energy as manifestations of inherited coherence
    — The Hubble tension as a directional coherence gradient effect
    All predictions are quantitative and falsifiable by current and near-future observations. DEBA
offers a rigorous alternative to ΛCDM, addressing its anomalies without ad hoc modifications.
    Future work includes: (1) detailed numerical simulation of bubble formation, (2) precise calculation of
the CMB power spectrum from DEBA dynamics, (3) quantitative comparison with Planck
and JWST data, (4) gravitational wave signatures from Type II interfaces.

Acknowledgments
    This work builds on fundamental stochastic field theory, large deviation theory, and
functional analysis. No external funding was received.


---


References
 [1] Planck Collaboration, Planck 2018 results. VII. Isotropy and statistics of the CMB, Astron. Astrophys. 641,
     A7 (2020).
 [2] Various authors, JWST observations of high-redshift quasars and galaxies, Nature, ApJ (2023-2024).
 [3] A. G. Riess et al., A Comprehensive Measurement of the Local Value of the Hubble Constant, Astrophys. J.
     Lett. 934, L7 (2022).

6


---

