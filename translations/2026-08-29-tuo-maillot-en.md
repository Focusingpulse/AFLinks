---
description: My (Forge's) English translation of François Maillot's TUO paper — 'De Maxwell et Einstein au champ de tension du vide Tv' (Wave-Universe Theory), the vacuum tension field as a geometric property of spacetime. Outer-ring / French physics. Translation metadata kept below.
---

> Translation metadata: title "Formalismes classiques et correspondance avec la TUO : De Maxwell et Einstein au champ de tension du vide Tᵥ / Classical Formalisms and Correspondence with the TUO: From Maxwell and Einstein to the Vacuum Tension Field Tᵥ" · source https://doi.org/10.5281/zenodo.17311741 · French · François Maillot (Théorie de l'Univers Onde, TUO) · Zenodo, 10 October 2025, DOI 10.5281/zenodo.17311742 · translated by Forge 2026-08-29 from the full 7-page manuscript PDF · status: claimed in progress · also stored in living-library translations/work/tuo-maillot/

# Classical Formalisms and Correspondence with the TUO: From Maxwell and Einstein to the Vacuum Tension Field Tᵥ

*François Maillot — Théorie de l'Univers Onde (TUO). DOI: 10.5281/zenodo.17311742. 10 October 2025. Translated from the French by Forge.*

## Abstract

This document presents the formal correspondence between the Wave-Universe Theory (TUO) and the classical mathematical formalisms of theoretical physics: electromagnetism (Maxwell), general relativity (Einstein), and field theory (covariant Lagrangian). Each section explicits the structural link between the classical operators, invariants, and tensors and their TUO equivalent, while insisting on the fundamental conceptual differences: the TUO does not introduce an additional gauge field, but a geometric property of the vacuum itself, the tension Tᵥ.

## 1. Fundamental Lagrangian of the TUO

### 1.1 Minimal form

In the TUO, the dynamics of the vacuum tension field Tᵥ is derived from a least-action principle analogous to that of scalar fields:

**L_TUO = ½ g^μν ∂_μTᵥ ∂_νTᵥ − V(Tᵥ)** (1)

where V(Tᵥ) is an effective potential describing the tension states of the vacuum (minima, transitions, saturation). This formulation allows obtaining the dynamical equations:

**□Tᵥ + dV/dTᵥ = 0** (2)

where □ = ∇^μ∇_μ is the covariant d'Alembert operator.

### 1.2 Conceptual difference with classical fields

- The field Tᵥ is not a force field, but a **state property of the vacuum**: it measures locally the geometric tension of the medium.
- Unlike a gauge field, Tᵥ possesses no gauge symmetry nor associated quanta (no gauge boson). It acts on the metric rather than through it.
- Its potential V(Tᵥ) encodes the memory and coherence of spacetime: the minima correspond to the stable phases of the vacuum (slowly expanding or accelerating universes).

## 2. Energy-momentum tensor of the field Tᵥ

Applying the classical definition of the energy-momentum tensor:

**T^(v)_μν = ∂_μTᵥ ∂_νTᵥ − g_μν L_TUO** (3)

one obtains the TUO–Einstein field equations:

**G_μν = 8πG (T^(m)_μν + T^(v)_μν)** (4)

where T^(m)_μν represents ordinary matter. The component T^(v)_μν replaces the cosmological constant Λg_μν: it is **dynamical and local**.

**Major difference:** T^(v)_μν depends on the gradients of Tᵥ, therefore on the spatial and temporal variations of the vacuum tension. This generates a variable expansion H(z), unlike the constant term Λ of general relativity.

## 3. Invariants: from Maxwell to the TUO

### 3.1 Classical electromagnetic invariants

Classical electromagnetism rests on two fundamental invariants:

**I₁ = F^μν F_μν = 2(B² − E²/c²), I₂ = F^μν F̃_μν = −4(E·B)** (5)

### 3.2 Vacuum tension invariant

The TUO introduces an analogous invariant based on the dynamics of the scalar field:

**I_Tv = g^μν ∂_μTᵥ ∂_νTᵥ − 2V(Tᵥ)** (6)

which can be seen as the "energetic" equivalent of the vacuum. It describes the ratio between the internal tension of the vacuum (gradient) and its cohesion potential.

**Fundamental difference:** the TUO invariant does not describe the propagation of a field, but the equilibrium structure of the vacuum. The local oscillations of Tᵥ are reorganizations of geometry itself, not waves in a pre-existing medium.

## 4. Correspondence of differential operators

Maxwell's equations use the divergence and curl operators:

**∇·E = ρ/ε₀, ∇×B − (1/c²)∂E/∂t = μ₀j** (7)

In the TUO, the local equation of state of the vacuum tension reads:

**∇Tᵥ = −g, ∇²Tᵥ − (1/c²_v)∂²Tᵥ/∂t² = S_T** (8)

where c_v is the relaxation speed of the tension field and S_T a source term. Thus, the operators are identical, but the **physical content changes**: Tᵥ does not obey a charge conservation, but a conservation of geometric equilibrium.

## 5. Covariant formulation

For integration in the relativistic framework, the TUO defines the scalar tension potential as a covariant quantity Tᵥ(x^μ) and its four-dimensional gradient:

**Φ_μ = ∂_μTᵥ, Φ² = g^μν Φ_μ Φ_ν** (9)

The TUO equations can then be formulated in action form:

**S_TUO = ∫ d⁴x √−g [ R/16πG + ½Φ² − V(Tᵥ) + L_m ]** (10)

**Difference of nature:** unlike the electromagnetic potential A_μ, Tᵥ is not a gauge vector but a scalar state density. Its variation modifies the metric and not the motion of charges.

## 6. Synthetic comparison

| Classical framework | TUO formulation | Conceptual difference |
|---------------------|-----------------|----------------------|
| Field F_μν (EM) | Scalar field Tᵥ | Geometric tension of the vacuum |
| Cosmological constant Λ | Dynamical tensor T^(v)_μν | Variable expansion of the vacuum |
| Invariant F^μνF_μν | Invariant I_Tv | Vacuum equilibrium, not force field |
| Potential A_μ | Covariant gradient Φ_μ = ∂_μTᵥ | Metric coupling, no gauge |

## 7. Enriched mathematical demonstrations

### 7.1 Variation of the action: field equation

Starting from the covariant action

**S = ∫ d⁴x √−g [ R/16πG + ½g^μν∂_μTᵥ∂_νTᵥ − V(Tᵥ) + L_m ]** (11)

The variation with respect to Tᵥ fixing δg_μν = 0 and neglecting the boundary term gives

**δS_Tv = ∫ d⁴x √−g [−∇^μ∇_μTᵥ − dV/dTᵥ] δTᵥ = 0** (12)

hence the Euler–Lagrange equation

**□Tᵥ + V′(Tᵥ) = 0, □ ≡ ∇^μ∇_μ** (13)

### 7.2 Metric variation: energy-momentum tensor of Tᵥ

Varying the action with respect to g_μν, one obtains

**T^(v)_μν = −(2/√−g) δ(√−g L_TUO)/δg^μν = ∂_μTᵥ∂_νTᵥ − g_μν[½g^αβ∂_αTᵥ∂_βTᵥ − V(Tᵥ)]** (14)

The gravitational variation provides the modified field equations

**G_μν = 8πG (T^(m)_μν + T^(v)_μν)** (15)

with ∇^μG_μν = 0 and therefore ∇^μ(T^(m)_μν + T^(v)_μν) = 0 (total conservation), leaving possible an exchange between matter and tension (effective source in the continuity equation).

### 7.3 FLRW reduction: Friedmann–TUO equations

For a flat FLRW metric, ds² = dt² − a²(t)dx², Tᵥ = Tᵥ(t) homogeneous and H = ȧ/a:

**H² = (8πG/3)(ρ_m + ρ_r + ρ_v), ρ_v = ½Ṫ²� + V(T�)** (16)
**Ḣ = −4πG(ρ_m + 4/3ρ_r + ρ_v + p_v), p_v = ½Ṫ²ᵥ − V(Tᵥ)** (17)

with the field equation T̈ᵥ + 3H Ṫᵥ + V′(Tᵥ) = 0. The effective state index w_v = p_v/ρ_v varies dynamically and allows regimes w_v ≈ −1 or w_v > −1, coherent with the needs for H(z).

### 7.4 Linear perturbations and stability

The perturbations δTᵥ satisfy

**δT̈ᵥ + 3H δṪᵥ + (k²/a² + V″(Tᵥ)) δTᵥ = S_metric** (18)

with an effective sound c²_v = 1. The stability conditions require V″(Tᵥ) ≥ 0 and positive energy ρ_v ≥ 0. These criteria fix the families of potentials V(Tᵥ) compatible with the CMB/BAO spectra.

### 7.5 Noether current and conservation

The symmetry Tᵥ → Tᵥ + const (if V depends only on the derivatives) induces a current J^μ = ∂^μTᵥ with ∇_μJ^μ = 0. For explicit potentials V(Tᵥ) this symmetry is broken (effective source), which corresponds to a **memory of the vacuum**.

### 7.6 Examples of potentials and dynamical regimes

- **Quadratic:** V = ½m²_v T²ᵥ.
- **Higgs-type:** V = λ(T²ᵥ − v²)².
- **Plateau:** V = V₀[1 − e^(−Tᵥ/μ)] or exponential V = V₀e^(−αTᵥ).

These families cover the cases necessary to reproduce the observables (CMB/BAO/SN) without cosmological constant.

## Calculation Appendices

**Appendix A. Variation of the action with boundary terms.** The scalar action coupled to gravitation; the scalar variation produces a surface term via integration by parts; imposing δTᵥ|∂M = 0 (or equivalent Dirichlet conditions) cancels the boundary term and the Euler–Lagrange equation follows: □Tᵥ + V′(Tᵥ) = 0. For the gravitational part, the variation of R also produces surface terms; one compensates them with the Gibbons–Hawking–York term S_GHY = (1/8πG)∫_∂M K √|h| d³x.

**Appendix B. Bianchi identities and energy exchange.** From the identities ∇^μG_μν = 0 follow the total conservation equations ∇^μ(T^(m)_μν + T^(v)_μν) = 0. One can define an exchange term Q_ν between matter and vacuum tension: ∇^μT^(m)_μν = Q_ν, ∇^μT^(v)_μν = −Q_ν. In the FLRW background, Q_ν = Qu_ν leads to the continuity equations ρ̇_m + 3Hρ_m = +Q and ρ̇_v + 3H(ρ_v + p_v) = −Q. The TUO authorizes Q ≠ 0 (memory/relaxation of the vacuum), subject to observational constraints.

**Appendix C. Linear scalar perturbations (Newton gauge).** In the gauge ds² = (1 + 2Ψ)dt² − a²(1 − 2Φ)dx², a canonical scalar satisfies δT̈ᵥ + 3HδṪᵥ + (k²/a² + V″(Tᵥ))δTᵥ = 4ṪᵥΨ̇ − 2V′(Tᵥ)Ψ. The anisotropy tensor of the canonical scalar is zero, so Φ = Ψ in the absence of anisotropy of the other fluids. The power spectrum of δTᵥ then feeds the CMB/BAO observables via the Boltzmann equations.

**Appendix D. Dimensional analysis and SI normalization.** In natural units c = ℏ = 1, [Tᵥ] = E, [V] = E⁴, [L] = E⁴. To relate to SI units (m, kg, s), one chooses a normalization factor κ_v such that, in an asymptotic galactic regime, |∇Tᵥ| ≃ GM/r² ⇒ κ_v ~ GM/(r²∇⟨uTᵥ⟩). This calibration (SPARC-type) then fixes the absolute scale for H(z) in the background equations.

**Appendix E. Stability and causality conditions.** No ghost: positive kinetic sign. No gradient instability: c²_s = (∂p_v/∂X)/(∂ρ_v/∂X) ≥ 0 with X = ½Ṫ²ᵥ (canonical scalar c²_s = 1). Mass stability: V″(Tᵥ) ≥ 0 around the background.

**Appendix F. Useful analytic regimes.** Quasi-de Sitter regime (quasi-constant tension): if Ṫ²ᵥ ≪ V and |V′| ≪ 3HṪᵥ, then w_v ≃ −1 and H² ≃ (8πG/3)V. Oscillating regime (quadratic potential): for V = ½m²_vT²ᵥ, Tᵥ oscillates at ω ≃ m_v; on average w_v → 0 (matter-like behavior); useful to modulate H(z) without Λ.

**Appendix G. Background equations in redshift.** With d/dt = −(1+z)H d/dz, one obtains equations ready for direct numerical integration and fitting to data (SN, BAO, CMB).

**Appendix H. SPARC link and local calibrations.** In the stationary galactic regime, g = −∇Tᵥ relates instantly the shape of Tᵥ(r) to the rotation curves. The same constant κ_v (Appendix D) must ensure the local (SPARC) and global (CMB/BAO) coherence — a strong constraint for the TUO.

## Conclusion

The integration of the field Tᵥ into the classical formalisms establishes a direct bridge between the vacuum physics of the TUO and the frameworks of Maxwell and Einstein. However, the essential difference remains: Tᵥ does not describe an interaction in spacetime, but the dynamical state of spacetime itself. The classical invariants, operators, and tensors become in this framework tools for expressing a more fundamental property: the universal tension of the vacuum, matrix of all physical structure.

## References
[1] J. C. Maxwell, A Dynamical Theory of the Electromagnetic Field. Phil. Trans. R. Soc. London, 155, 459–512 (1865).
[2] A. Einstein, Die Grundlage der allgemeinen Relativitätstheorie. Annalen der Physik, 49, 769–822 (1916).
[3] T. Kaluza, Zum Unitätsproblem der Physik. Sitzungsberichte der Preussischen Akademie der Wissenschaften, 966–973 (1921).
[4] F. Maillot, La constante fondamentale de la TUO: K, clef de la gravitation quantique universelle. Zenodo, DOI: 10.5281/zenodo.17243974 (2025).
[5] F. Maillot, De E = mc² à l'invariant vibratoire TUO: vers une gravitation quantique du vide condensé. Zenodo, DOI: 10.5281/zenodo.17243832 (2025).
[6] F. Maillot, Profondeur 5D de la Gravitation et Champ Fondamental B dans la TUO. Zenodo, DOI [to be completed] (2025).
[7] F. Maillot, Réduction du son cosmique par la fenêtre de tension du vide: un ajustement naturel de la constante de Hubble dans la TUO. Zenodo, DOI: 10.5281/zenodo.17218834 (2025).
[8] F. Maillot, Validation photonique de l'invariant harmonique de Maillot vers une universalité gravitationnelle. Zenodo, DOI: 10.5281/zenodo.17270975 (2025).
[9] F. Maillot, "Pont entre la théorie de Michaud et la TUO...", Zenodo, DOI: 10.5281/zenodo.17311742 (2025).
[10] CODATA 2022, Recommended Values of the Fundamental Physical Constants.
[11] Planck Collaboration, "Planck 2018 results. VI. Cosmological parameters", A&A, 641, A6 (2020).
[12] A. G. Riess et al., A Comprehensive Measurement of the Local Value of the Hubble Constant. ApJL, 934, L7 (2022).
[13] A. Michaud, "From Classical to Relativistic Mechanics via Maxwell", IJERD, 6(4), 1–10 (2013).
[14] P. Marmet, "Fundamental Nature of Relativistic Mass and Magnetic Fields", IFNA-ANS Journal (2003).
[15] Planck Collaboration, "Planck 2018 results. VI", A&A, 641, A6 (2020).
[16] DESI Collaboration, "Early 2025 Data Release: Updated BAO and Expansion Measurements", ApJ (2025).
[17] F. Lelli, S. McGaugh, J. Schombert, "SPARC: mass models for 175 disk galaxies...", AJ, 152, 157 (2016).

*DOI: 10.5281/zenodo.17311742. License: CC-BY 4.0. © François Maillot — All rights reserved.*

---

*Source: F. Maillot, "Formalismes classiques et correspondance avec la TUO", Zenodo, 10 October 2025, DOI 10.5281/zenodo.17311741 (record) / 17311742 (file). Complete translation from the 7-page manuscript PDF by Forge (translation-qc), 2026-08-29.*

## Translator's QC note (pending)
- Complete translation of the full 7-page manuscript: the Lagrangian formalism, the TUO–Einstein equations, the invariant correspondence (Maxwell → TUO), proofs A–H, and the reference list.
- Terminology: "champ de tension du vide" → "vacuum tension field" (Tᵥ); "Théorie de l'Univers Onde" → "Wave-Universe Theory (TUO)"; "propriété d'état du vide" → "state property of the vacuum"; "mémoire du vide" → "memory of the vacuum"; "invariant" kept; "condition de stabilité" → "stability condition"; "régime quasi-de Sitter" → "quasi-de Sitter regime"; "son effectif" → "effective sound".
- Cross-links: TUO's "vacuum tension as a geometric property, not a force" + "memory of the vacuum" + "tension replaces Λ as a dynamic field" maps directly onto the subtle-energy-layers / vibrational-spectrum thesis. Also connects to Burtin's Φκ (vacuum as active medium) and Benaros' Æther D. Strong authoring material.
- Reference [6] has a placeholder DOI in the original ("[À compléter]") — noted.
- No [pN] page markers in source (PDF preprint).