---
name: Wave Universe Theory (TUO): From the Electromagnetic Origin of the Vacuum to the Covariant…
description: "Translation document. https://doi.org/10.5281/zenodo.17311741"
---

- **description:** English translation of François Maillot's "Théorie de l'Univers Onde (TUO)" — two-part paper establishing vacuum tension field theory as a unified approach to gravitation and cosmology. Translated from French with full provenance.
- **source_language:** French
- **geographic_origin:** France
- **author:** François Maillot
- **work_type:** theoretical
- **practical_applicability:** conceptual
- **source_url:** https://doi.org/10.5281/zenodo.17311741
- **archive_files:** archives/2026-08-26-tuo-formalism-fr.pdf, archives/2026-08-26-tuo-confined-em-fr.pdf
- **host:** Zenodo (CERN)
- **host_stability:** stable — Zenodo, CC licensing, persistent DOI
- **translated_date:** 2026-08-26

# Wave Universe Theory (TUO): From the Electromagnetic Origin of the Vacuum to the Covariant Reformulation of Gravity and Cosmology

**Author:** François Maillot
**Date:** October 10, 2025
**DOI:** 10.5281/zenodo.17311742 (v1.1)
**Host:** Zenodo (CERN European Organization for Nuclear Research)
**Original language:** French

---

## Provenance

- **Source language:** French
- **Geographic origin:** France (researcher based in France; published via CERN's Zenodo)
- **Researcher:** François Maillot — independent researcher, author of multiple TUO-related papers on Zenodo (2025)
- **Work type:** Theoretical — full mathematical framework with covariant Lagrangian, field equations, cosmological applications
- **Practical applicability:** Conceptual — no experimental verification claimed; provides theoretical framework. The SPARC calibration proposal (Part II, §5.5) is a concrete observational anchor but untested.
- **Host:** Zenodo (CERN), stable infrastructure with persistent DOI
- **Related researchers referenced:** André Michaud (electron model), de Broglie, Marmet, Maxwell, Einstein, Kaluza

---

## Part I: Classical Formalisms and Correspondence with the TUO — From Maxwell and Einstein to the Vacuum Tension Field Tv

### Abstract

This document presents the formal correspondence between the Wave Universe Theory (TUO) and the classical mathematical formalisms of theoretical physics: electromagnetism (Maxwell), general relativity (Einstein), and field theory (covariant Lagrangian). Each section explicates the structural link between classical operators, invariants, and tensors and their TUO equivalent, while emphasizing the fundamental conceptual differences: the TUO does not introduce an additional gauge field, but a geometric property of the vacuum itself — the tension Tv.

### 1. Fundamental Lagrangian of the TUO

#### 1.1 Minimal Form

In the TUO, the dynamics of the vacuum tension field Tv are derived from a principle of least action analogous to that of scalar fields:

**L_TUO = ½ g^μν ∂_μ T_v ∂_ν T_v − V(T_v)**

where V(T_v) is an effective potential describing the tension states of the vacuum (minima, transitions, saturation). This formulation yields the dynamical equations:

**□T_v + dV/dT_v = 0**

where □ = ∇_μ ∇^μ is the covariant d'Alembert operator.

#### 1.2 Conceptual Difference with Classical Fields

- The field T_v is **not a force field**, but a **state property of the vacuum**: it locally measures the geometric tension of the medium.
- Unlike a gauge field, T_v possesses no gauge symmetry and no associated quanta (no gauge boson). It acts on the metric rather than through it.
- Its potential V(T_v) encodes the **memory and coherence** of spacetime: minima correspond to stable phases of the vacuum (universe in slow or accelerated expansion).

### 2. Energy-Momentum Tensor of the T_v Field

Applying the classical definition of the energy-momentum tensor:

**T^(v)_μν = ∂_μ T_v ∂_ν T_v − g_μν L_TUO**

one obtains the TUO–Einstein field equations:

**G_μν = 8πG [T^(m)_μν + T^(v)_μν]**

where T^(m)_μν represents ordinary matter. The component T^(v)_μν **replaces the cosmological constant Λg_μν**: it is dynamic and local.

**Major difference:** T^(v)_μν depends on gradients of T_v, therefore on spatial and temporal variations of vacuum tension. This generates a **variable expansion H(z)**, unlike the constant Λ term of general relativity.

### 3. Invariants: From Maxwell to the TUO

#### 3.1 Classical Electromagnetic Invariants

Classical electromagnetism rests on two fundamental invariants:
- I₁ = F_μν F^μν = 2(B² − E²/c²)
- I₂ = F_μν F̃^μν = −4(E · B)

#### 3.2 Vacuum Tension Invariant

The TUO introduces an analogous invariant based on the dynamics of the scalar field:

**I_Tv = g^μν ∂_μ T_v ∂_ν T_v − 2V(T_v)**

which can be seen as the "energetic" equivalent of the vacuum. It describes the ratio between the internal tension of the vacuum (gradient) and its cohesion potential.

**Fundamental difference:** The TUO invariant does not describe the propagation of a field, but the **equilibrium structure of the vacuum**. Local oscillations of T_v are reorganizations of geometry itself, not waves in a preexisting medium.

### 4. Correspondence of Differential Operators

Maxwell's equations use divergence and curl operators. In the TUO, the local state equation of vacuum tension is written:

**∇T_v = −g**

**∇²T_v − (1/c_v²)(∂²T_v/∂t²) = S_T**

where c_v is the relaxation speed of the tension field and S_T is a source term. Thus, the operators are identical, but the physical content changes: T_v does not obey charge conservation, but **geometric equilibrium conservation**.

### 5. Covariant Formulation

For integration into the relativistic framework, the TUO defines the scalar tension potential as a covariant quantity T_v(x^μ) and its four-dimensional gradient:

**Φ_μ = ∂_μ T_v,  Φ² = g^μν Φ_μ Φ_ν**

The TUO equations can then be formulated as an action:

**S_TUO = ∫ d⁴x √(−g) [R/(16πG) + ½Φ² − V(T_v) + L_m]**

**Difference in nature:** Unlike the electromagnetic potential A_μ, T_v is not a gauge vector but a **scalar state density**. Its variation modifies the metric, not the motion of charges.

### 6. Synthetic Comparison

| Classical Framework | TUO Formulation | Conceptual Difference |
|---|---|---|
| Field F_μν (EM) | Scalar field T_v | Geometric tension of vacuum |
| Cosmological constant Λ | Dynamic tensor T^(v)_μν | Variable expansion of vacuum |
| Invariant F_μν F^μν | Invariant I_Tv | Equilibrium of vacuum, not force field |
| Potential A_μ | Covariant gradient Φ_μ = ∂_μ T_v | Metric coupling, no gauge |

### 7. Enriched Mathematical Demonstrations

#### 7.1 Action Variation: Field Equation

Starting from the covariant action, variation with respect to T_v (fixing δg^μν = 0, neglecting boundary terms) yields the Euler–Lagrange equation:

**□T_v + V'(T_v) = 0**

#### 7.2 Metric Variation: Energy-Momentum Tensor of T_v

Varying the action with respect to g^μν gives the modified field equations:

**G_μν = 8πG [T^(m)_μν + T^(v)_μν]**

with ∇_μ G^μν = 0 and therefore ∇_μ [T^(m)_μν + T^(v)_μν] = 0 (total conservation), allowing exchange between matter and tension (effective source in the continuity equation).

#### 7.3 FLRW Reduction: Friedmann–TUO Equations

For a flat FLRW metric, ds² = dt² − a²(t)dx², with T_v = T_v(t) homogeneous and H = ȧ/a:

**H² = (8πG/3)(ρ_m + ρ_r + ρ_v)**

**Ḣ = −4πG(ρ_m + ⁴⁄₃ρ_r + ρ_v + p_v)**

where:
- ρ_v = ½ Ṫ_v² + V(T_v)
- p_v = ½ Ṫ_v² − V(T_v)

The effective equation-of-state index w_v = p_v/ρ_v varies dynamically and allows regimes with w_v ≈ −1 or w_v > −1, consistent with the needs for H(z).

#### 7.4 Linear Perturbations and Stability

Perturbations δT_v satisfy:

**δT̈_v + 3H δṪ_v + (k²/a² + V''(T_v))δT_v = S_métrique**

with an effective sound speed c²_v = 1. Stability conditions require V''(T_v) ≥ 0 and positive energy ρ_v ≥ 0. These criteria fix the families of potentials V(T_v) compatible with CMB/BAO spectra.

#### 7.5 Noether Current and Conservation

The symmetry T_v → T_v + const (if V depends only on derivatives) induces a current J^μ = ∂^μ T_v with ∇_μ J^μ = 0. For explicit potentials V(T_v), this symmetry is broken (effective source), corresponding to a **memory of the vacuum**.

#### 7.6 Example Potentials and Dynamical Regimes

- **Quadratic:** V = ½ m²_v T_v²
- **Higgs-type:** V = λ(T_v² − v²)²
- **Plateau:** V = V₀[1 − e^(−T_v/μ)] or exponential V = V₀ e^(−αT_v)

These families cover the cases necessary to reproduce observables (CMB/BAO/SN) without a cosmological constant.

---

## Part II: From Confined Electromagnetic Field to Cosmic Vacuum Tension — A Bridge Between Michaud's Theory and the TUO

### Abstract

We show that the work of André Michaud (2013), based on the magnetic contribution to electron mass, offers a coherent microphysical basis for the oscillatory structure of the vacuum tension field (T_v) postulated by the Wave Universe Theory (TUO). By linking the internal electromagnetic dynamics of particles to the cosmic tension of the vacuum, the TUO extends Michaud's vision toward a total unification of gravitation, electromagnetism, and cosmology.

### 1. Introduction

André Michaud's work, particularly *From Classical to Relativistic Mechanics via Maxwell* (IJERD, 2013), proposes a direct integration of Newton's and Maxwell's equations, based on the hypothesis that a particle's mass originates from its internal electromagnetic field. By combining ideas from de Broglie, Marmet, and Maxwell, Michaud shows that the electron can be understood as a **confined electromagnetic oscillation**, and that its mass derives from this internal dynamics.

The Wave Universe Theory (TUO), developed by François Maillot, follows the same lineage but at the cosmological scale. It describes the structure of the universe as the result of vacuum tension (T_v), a universal electromagnetic field whose gradients explain gravitation, galactic rotation, and cosmological expansion.

### 2. Recap of Michaud's Equations

In his model, Michaud introduces the notion of **magnetic mass** M, defined from the magnetic field of a moving electron:

**M = μ₀e²v² / (8πr_e²c²)**

The rest magnetic mass is then:

**M₀ = μ₀e² / (8πr_e²) = ½m_e**

where r_e is the classical electron radius. Michaud shows that **half the electron's mass comes from its internal magnetic field**, the other half from its electric component.

The electron is thus an **LC oscillator**:

**E(t) = E_E cos(ωt) + E_B sin(ωt)**

where E_E and E_B represent alternating electric and magnetic energies. This internal oscillation constitutes the basis of relativistic structure and links classical mechanics to relativity through the dynamics of the electromagnetic field.

### 3. Correspondence with the TUO

| Michaud's Concept | TUO Formulation | Interpretation |
|---|---|---|
| Internal LC oscillation | Local oscillation of T_v field | Confined EM polarization |
| Magnetic mass | Magnetic component of T_v | Magnetic polarity of condensed vacuum |
| Confined photon energy | Local condensation of T_v | Birth of a stable node (particle) |
| E ↔ B transition | Phase switch T_v+ ↔ T_v− | Fundamental vacuum symmetry |
| Relativity from Maxwell | Emergent relativity from ∇T_v | Geometric dynamics of vacuum |

### 4. Cosmological Extension

Michaud establishes that mass energy is a consequence of internal electromagnetic equilibrium. The TUO extends this idea to the universal scale:

**ρ_Tv(r,t) = ½(ε₀E² + B²/μ₀)**

which relates the vacuum energy density to the tension T_v. The gradient of T_v then becomes the direct cause of gravitation:

**g = −∇T_v**

Thus, relativistic dynamics and gravitational effects derive from a single fundamental electromagnetic principle. The vacuum is no longer a mere substrate, but an **active medium whose tension structures matter, galaxies, and expansion**.

### 5. From Local Magnetic Mass to Cosmological Dynamics: ∇T_v and H(z)

#### 5.1 Micro → Macro Transition Principle

Starting from Michaud's micro decomposition (magnetic mass + electric mass), one performs a **coarse-graining** (ensemble averaging) to obtain a cosmic field quantity. The local vacuum tension energy is:

**u_Tv(x,t) = ½(ε₀E² + B²/μ₀) = u_E + u_B**

identical to the EM energy density. Michaud's role is to fix the internal partition u_B/u_Tv via the LC oscillation: in stationary time average, ⟨u_E⟩ = ⟨u_B⟩ (equipartition). At finite velocity, the effective magnetic contribution grows (magnetic mass).

At the macro scale, the vacuum tension is posited as a scalar field proportional to the averaged EM energy:

**T_v(x,t) = κ_v ⟨u_Tv(x,t)⟩_C**

where κ_v is a normalization coupling and ⟨·⟩_C denotes cosmological cell averaging (coarse-graining over a comoving volume).

#### 5.2 Local Gravitation as Tension Gradient

In the TUO, gravitational acceleration relates to the tension gradient:

**g(x,t) = −∇T_v(x,t)**

**Link to Michaud:** The magnetic mass increases u_B for given dynamic regimes, which reinforces ∇T_v around baryonic condensations, and explains **galactic rotation curves without dark matter** (in the TUO–SPARC version).

#### 5.3 From Background T_v to H(z)

Defining the homogeneous component T̄_v(t) = ⟨T_v⟩_Hubble and the fluctuation δT_v = T_v − T̄_v, in a FLRW universe at first order:

**H²(t) = (8πG/3)[ρ_b + ρ_r + αT̄_v(t) + βṪ_v²(t)]**

with α, β coupling constants (TUO). The evolution of T̄_v obeys an effective continuity equation from the averaged LC oscillation:

**dṪ̄_v + 3H(1 + w_v)T̄_v = S(t)**

where w_v is the effective equation-of-state index of the tension background, and S is a source term (micro → macro transfer, e.g., EM phase transitions of the primordial plasma). The symmetric LC scheme suggests w_v ≈ −1 on average (negative pressure), with deviations δw_v when u_B/u_E departs from equipartition (dynamic phases), which the magnetic mass quantifies locally.

**Practical minimal closure** in redshift:

**dT̄_v/dz = [3(1 + w_v)T̄_v − S(z)/H(z)] / (1 + z)**

**H²(z) = H₀²[Ω_b(1+z)³ + Ω_r(1+z)⁴ + αT̄_v(z) + βṪ_v²(z)]**

**Role of Michaud:** The microphysical determination of T̄_v(z) requires estimating ⟨u_B(z)⟩ and ⟨u_E(z)⟩ (LC partition), constrained by EM processes of the plasma and baryonic condensations. The magnetic mass provides a micro observer of the u_B/u_E bias, hence of w_v(z) and S(z).

#### 5.4 Proposition (Micro → Macro Bridge)

**Proposition:** If the average magnetic fraction f_B(z) ≡ ⟨u_B/u_Tv⟩ can be written f_B(z) = ½ + δ_B(z), and if δ_B is related to the effective magnetic mass of charge carriers in the plasma (à la Michaud), then there exists a constant κ_v such that:

**T̄_v(z) = κ_v ⟨u_Tv(z)⟩_C ∝ κ_v mc²f_B(z)**

which closes the Friedmann equation **without postulating a cosmological constant**, via the EM micro-partition.

**Corollary:** Rapid variations of δ_B(z) around decoupling (CMB) introduce modulations of T̄_v(z) and thus of H(z), capable of encoding acoustic oscillations in the TUO version of the spectrum (link with BAO/CMB work).

#### 5.5 Calibration and Units

T_v is in TUO arbitrary units. To relate T_v to SI units, choose κ_v such that in the stationary Newtonian regime of a test galaxy, ‖∇T_v‖ ≈ GM/r² at r = r_asym (SPARC calibration). The same κ_v fixes the absolute scale of T̄_v in the Friedmann equations.

### 6. Conclusion

André Michaud's equations demonstrate that mass and relativity can emerge from an internal electromagnetic field oscillating between electric and magnetic components. The Wave Universe Theory (TUO) extends this logic to the cosmological scale, identifying vacuum tension T_v as the universal generalization of this confined field.

Thus, the link between the microphysics of the electron and the macrostructure of the universe is unified: **mass, gravitation, and expansion proceed from a single vibratory essence of the vacuum.**

### References

1. A. Michaud, *From Classical to Relativistic Mechanics via Maxwell*. IJERD, 6(4), 1–10 (2013). — Central reference: electron mass from confined EM field.
2. J. C. Maxwell, *A Dynamical Theory of the Electromagnetic Field*. Phil. Trans. Royal Society, 155, 459–512 (1865).
3. A. Einstein, *Die Grundlage der allgemeinen Relativitätstheorie*. Annalen der Physik, 49, 769–822 (1916).
4. T. Kaluza, *Zum Unitätsproblem der Physik*. Sitzungsberichte Preuss. Akad. Wiss., 966–973 (1921). — Historical reference on 5th dimension for Gravity-EM unification.
5. F. Maillot, *The fundamental constant of the TUO: K, key to universal quantum gravitation*. Zenodo, DOI: 10.5281/zenodo.17243974 (2025).
6. F. Maillot, *From E = mc² to the TUO vibrational invariant: toward quantum gravitation of condensed vacuum*. Zenodo, DOI: 10.5281/zenodo.17243832 (2025).
7. F. Maillot, *5D Depth of Gravitation and Fundamental Field B in the TUO*. Zenodo (2025).
8. F. Maillot, *Reduction of cosmic sound by the vacuum tension window: A natural adjustment of the Hubble constant in the TUO*. Zenodo, DOI: 10.5281/zenodo.17218834 (2025).
9. F. Maillot, *Photonic validation of the Maillot harmonic invariant toward gravitational universality*. Zenodo, DOI: 10.5281/zenodo.17270975 (2025).
10. CODATA 2022, Recommended Values of the Fundamental Physical Constants.
11. Planck Collaboration, *Planck 2018 results. VI. Cosmological parameters*, A&A, 641, A6 (2020).
12. A. G. Riess et al., *A Comprehensive Measurement of the Local Value of the Hubble Constant*.

---

## Translator's Notes

**Significance:** This is a rare French-language contribution to aether/vacuum theory that engages seriously with the mathematical formalism of general relativity and cosmology. Rather than proposing a new force or particle, Maillot introduces a **scalar vacuum tension field** (T_v) that replaces the cosmological constant with a dynamic, local term. The key conceptual move is treating vacuum tension as a **geometric state property** rather than a gauge field — it modifies the metric directly rather than acting through it.

**The Michaud bridge (Part II)** is the more speculative component: it proposes that the electron's mass arises from internal EM oscillation (LC model), and that coarse-graining this microphysics yields the cosmic vacuum tension. The claim that galactic rotation curves can be explained without dark matter via ∇T_v is the most testable assertion, with SPARC calibration proposed as an anchor.

**Relation to the Living Library's focal entity (The Force of Aether):** TUO provides a modern mathematical formalization of the aether concept — vacuum tension as a scalar field with covariant Lagrangian, replacing Λ with a dynamic term. It connects to the Atsyukovsky etherodynamics tradition (Russian) and the broader aether theory landscape, but from a French perspective with stronger engagement with standard GR formalism.

**Limitations:** No experimental verification is claimed. The theory is internally consistent mathematically but requires observational calibration (SPARC) to be distinguished from ΛCDM. The Michaud electron model is not mainstream physics.
