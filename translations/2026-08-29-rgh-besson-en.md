---
description: My (Forge's) English translation of Laurent Besson's RGH technical analysis — 'Relativité Générale Hypercomplexe', quaternionic field + Weyl gauge, ghost analysis, big bounce, CLASS implementation. Outer-ring / French physics. Translation metadata kept below.
---

> Translation metadata: title "Analyses techniques pour la RGH (A,B,C,D,F) / Technical Analyses for the Hypercomplex General Relativity (RGH) (A,B,C,D,F)" · source https://zenodo.org/records/17555967 · French · Laurent Besson · Zenodo, November 2025 · translated by Forge 2026-08-29 from the full manuscript PDF (rgh_A_B_C_D_F.pdf, 7 pages) · status: claimed in progress · also stored in living-library translations/work/rgh-besson/

# Technical Analyses for the Hypercomplex General Relativity (RGH) (A, B, C, D, F) — LaTeX Version

*Laurent Besson. Document generated for dissemination and integration into preprint/code. November 2025. Translated from the French by Forge.*

## Abstract

This document gathers, in a compact and formal manner, the requested analyses: A) analysis of the degrees of freedom and conditions for the absence of ghosts; B) parametric derivation of the "big bounce" term and pilot estimate of the coefficient; C) linear perturbation equations (scalar and tensor) ready for numerical implementation; D) detailed plan and pseudocode for forking/patching CLASS; F) concise technical response to the criticisms/referees intended to be attached to the preprint.

The text is self-contained: technical appendices provide the procedure for obtaining more detailed analytical expressions (eigenvalues, numerical bounds).

## Table of contents
1. Conventions and hypotheses

## 1. Conventions and hypotheses

We work in natural units ℏ = c = 1 unless otherwise indicated. The Planck constant is denoted ℓ_P (or M_Pl depending on the normalization). The chosen metric signature is (−, +, +, +). The model action is taken in the form (excerpted and simplified from the manuscript):

**S = ∫ d⁴x √−g [ R/16πG − ¼F_μνF^μν + L_H + L_coup + L_mat ]** (1)

with:

**L_H ≡ +½ Tr(∇_μH ∇^μH)** (2)
**L_coup ≡ κ Tr(H·F) + λ Tr(H²R)** (3)

Here H_ij(x) denotes the quaternionic field (coded in a matrix representation), Φ_μ is the Weyl gauge potential (emergent gauge field), and F_μν = ∂_μΦ_ν − ∂_νΦ_μ + [Φ_μ, Φ_ν]. The notations κ, λ, α_W denote free couplings of the model.

**Remark on the sign convention of L_H.** The stability analysis assumes L_H with a positive canonical kinetic sign for the physical degrees of freedom; adjust the notation if necessary.

## 2. A — Analysis of the degrees of freedom & stability (linearization)

**Objective:** expose the rigorous method to demonstrate the absence of ghosts and extract constraints on κ, λ, α_W.

### 2.1 General procedure

The central step is the linearization around a reference background (Minkowski or FLRW). One writes:

**g_μν = ḡ_μν + h_μν, H = H̄ + δH, Φ_μ = Φ̄_μ + δΦ_μ.**

We first take ḡ_μν = η_μν, H̄ = 0, Φ̄_μ = 0 (minimal stability test). One keeps the quadratic terms in (h_μν, δH, δΦ_μ).

### 2.2 Extraction of the kinetic matrix

After decomposition according to spatial symmetry (SO(3)), one identifies the scalar, vector, and tensor degrees of freedom. For the ghost-absence test it suffices to focus on the temporal part of the quadratic terms: the coefficients in front of q̇ᵢq̇ⱼ (qᵢ independent configurational variables) form the kinetic matrix K. For the simplified scalar analysis one typically obtains a 3×3 matrix:

**L_kin = ½ q̇ᵀK q̇, q = (q_h, q_H, q_Φ)ᵀ, K = [[a, d, e],[d, b, f],[e, f, c]]**

with a, b, c, d, e, f real expressions depending on the model parameters and the background.

### 2.3 Criterion (Sylvester) for the absence of ghosts

A symmetric matrix K is positive definite (all kinetic energies positive) if and only if all its principal minors are strictly positive. For the 3×3 one requires:

**D₁ = a > 0** (4)
**D₂ = det[[a, d],[d, b]] = ab − d² > 0** (5)
**D₃ = det K = abc − af² − be² − cd² + 2def > 0** (6)

These three inequalities form necessary and sufficient constraints on the coefficients a, b, c, d, e, f.

### 2.4 Physical interpretation and mapping to κ, λ, α_W

- a arises essentially from the EH term for the metric scalar component (after gauge-fixing). In canonical GR one expects a > 0.
- b is the kinetic coefficient of δH (related to the sign of L_H). One imposes b > 0.
- c is the kinetic coefficient of δΦ (related to the linearized −¼F²) — expected positivity.
- d, e, f are proportional to the non-minimal couplings (λ, κ, α_W) and encode the kinetic mixing. Inequalities (4)–(6) give upper bounds on the magnitudes of these mixings and therefore on |λ|, |κ|.

### 2.5 Practical prescription for a rigorous proof

To rigorously establish the absence of ghosts:
1. Write explicitly the quadratic action in scalar components (working in spatial Fourier e^{i k⃗·x⃗}).
2. Extract the q̇ᵢq̇ⱼ terms and identify a, b, c, d, e, f as analytic functions of κ, λ, α_W and the wave vector k⃗.
3. Apply (4)–(6); solve analytically or numerically the inequalities to obtain the admissible regions in parameter space.
4. Complete with the constraint (gauge) analysis to verify that the null directions of K correspond to purely gauge degrees of freedom.

## 3. B — Parametric derivation of the "bounce" term

**Goal:** produce a parametric expression of the effective term ρ_Θ(a) that dominates at small scale radius and compute the bounce scale a_min as a function of the parameters.

### 3.1 Heuristic origin

Geometric quantum contributions (or condensates of H-field modes) typically lead to effective densities that grow rapidly when a → 0. The study of the effective development gives a scalar term behaving like a⁻⁴ (radiation-like) but multiplied by an amplitude controlled by ℏ, ℓ_P, and the couplings of the model.

### 3.2 Parametric ansatz

One poses the ansatz, founded on dimensional analysis and the manuscript:

**ρ_Θ(a) = C(κ, λ, α_W) (ℏ²/ℓ⁴_P) (1/a⁴)** (7)

where C is a dimensionless coefficient determinable from an integral/sum over modes and the couplings.

### 3.3 Modified Friedmann and bounce condition

The Friedmann equation (without explicit cosmological constant) reads:

**H² = (8πG/3)(ρ_m + ρ_r + ρ_Θ) − k/a².**

A bounce (halt of contraction and reversal toward expansion) occurs when H² = 0 then H² > 0. Neglecting curvature and matter for the most compact phase (typical approximation), the bounce condition is equivalent to the effective cancellation of the RHS by the dominant terms. If ρ_Θ enters with the right sign (i.e., a repulsive effect or a term that prevents H² → ∞), then there exists a_min > 0.

### 3.4 Order-of-magnitude estimate

In Planck units (ℓ_P = 1, ℏ = 1), if C ~ O(1) then ρ_Θ ~ a⁻⁴ becomes of the order of the Planck density for a ~ 1: the bounce therefore takes place at the Planck scale typically, a_min ~ O(1)ℓ_P.

If C is small or large, a_min moves accordingly: C ≫ 1 ⇒ a_min ≫ ℓ_P (macroscopic bounce); C ≪ 1 ⇒ a_min ≪ ℓ_P (physically suspect, zone out of range of the effective description).

### 3.5 Procedure to compute C(κ, λ, α_W)

To obtain C rigorously:
1. Linearize the action and diagonalize the quadratic operators (physical modes).
2. Compute the energy of a renormalized vacuum state (or the effective zero-point energy) due to the modes of H and Φ in the presence of the FLRW metric (regularization-renormalization techniques required: adiabatic subtraction, point-splitting, ζ-function).
3. Express ρ_Θ as a sum/integral over modes: ρ_Θ = Σ_modes ½ω_eff,k regularized; extract the dominant term in a → 0.
4. Identify C as the coefficient of the a⁻⁴ term after renormalization.

This calculation gives an expression as a function of κ, λ, α_W (and of renormalization choices); it is perfectly feasible symbolically/numerically and can be automated to produce C and an estimate of a_min.

### 3.6 Guiding example (schematic)

Suppose (toy model) that only a number N_H of effective degrees of freedom of H contribute to the zero-point energy, with effective frequencies ω_k ~ k/a (typical for conformal modes): after regularization one obtains a term ~ N_H/(a⁴), hence C ∝ N_H. Real calculations require integration over the full spectrum and take into account non-trivial couplings.

## 4. C — Linear perturbation equations (FLRW)

**Objective:** provide the scalar and tensor perturbation equations (forms ready to implement in a Boltzmann code like CLASS).

### 4.1 Background

One sets a flat FLRW metric in conformal time η:

**ds² = a²(η)(−dη² + δ_ij dxⁱdxʲ).**

Let H ≡ a′/a (prime = derivative with respect to η). The modified Friedmann background is:

**H² = (8πG/3) a² (ρ_m + ρ_r + ρ_Θ(a)).**

### 4.2 Scalar perturbations (Newton gauge)

In the Newton gauge the perturbed metric reads:

**ds² = a²(η)(−(1 + 2Φ)dη² + (1 − 2Ψ)δ_ij dxⁱdxʲ).**

The linearized Einstein equations become (schematic form):

**k²Ψ + 3H(Ψ′ + HΦ) = −4πGa² δρ_tot** (8)
**k²(Φ − Ψ) = 12πGa²(ρ_tot + p_tot)σ_tot** (9)
**Ψ′ + HΦ = 4πGa²(ρ_tot + p_tot)v_tot** (10)

Here δρ_tot = δρ_m + δρ_r + δρ_Θ, etc. The RGH contributions appear via δρ_Θ, δp_Θ, σ_Θ and v_Θ extracted from the modal decomposition of δH, δΦ.

### 4.3 Modified Mukhanov–Sasaki

For the comoving invariant v one obtains (generic form):

**v″_k + (c²_s k² − z″/z) v_k = S_H(k, η),**

where z and c²_s are modified by ρ_Θ and S_H is a source depending on the metric-H mixing. The explicit construction of z″/z requires the expression of the effective sound speed and the energy fraction associated with Θ.

### 4.4 Tensor perturbations (gravitational waves)

The gravitational waves (transverse and traceless modes) satisfy:

**h″_ij + 2H h′_ij + k² h_ij = 16πGa² Π^(source)_ij,**

with Π^(source)_ij containing the transverse-traceless component of the effective energy-momentum perturbation due to H and Φ. If Θ generates vector/transverse components, one expects additional signatures (non-standard polarizations, additional modes).

### 4.5 Practical parameterizations for code

For implementation in CLASS it is convenient to proceed by two routes:
1. **Effective fluid:** treat Θ as an additional fluid defined by w_Θ(a), c²_s,Θ, and σ_Θ. This allows introducing ρ_Θ(a), p_Θ(a) and the closure equations for δ_Θ, θ_Θ, σ_Θ.
2. **Microphysics:** integrate directly the EOM of δH and δΦ coupled to Einstein (more faithful, requires additional resolution of ODE systems).

## 5. D — CLASS implementation plan (detailed) and pseudocode

Below is a concrete plan for a CLASS fork with additional rgh modules.

### 5.1 Recommended structure
- Create a rgh/ folder containing: rgh.h, rgh.c, rgh_input.c, rgh_perturbations.c.
- Add parameters in input.c: rgh_C, rgh_kappa, rgh_lambda, rgh_alphaW, rgh_switch.
- Modify background.c and perturbations.c to call the RGH routines.

### 5.2 Essential functions (background)

```c
double rho_rgh(double a, struct rgh_params *rp) {
    double C = rp->C;
    double lP = rp->lP; // in Planck units choose lP=1
    // Units: with hbar=1, return density in Planck units
    return C * 1.0 / (pow(a,4));
}

double p_rgh(double a, struct rgh_params *rp) {
    // radiation-like leading behavior
    return rho_rgh(a,rp)/3.0;
}
```

Insert into the background computation routine:

```c
/* in background_derivs */
rho_tot = rho_m + rho_r + rho_rgh(a,rp) + rho_lambda;
p_tot = p_m + p_r + p_rgh(a,rp) + p_lambda;
H2 = (8*pi*G/3.0) * rho_tot - k_over_a2;
```

### 5.3 Perturbations (effective fluid)

```c
/* delta_rgh' and theta_rgh' time evolution (conformal time) */
delta_rgh_prime = -(1+w_rgh)*(theta_rgh - 3*Psi_prime)
                  - 3*(c_s2 - w_rgh)*H*delta_rgh;
theta_rgh_prime = -H*(1-3*c_s2)*theta_rgh
                  + k*k*c_s2/(1+w_rgh)*delta_rgh + k*k*Phi
                  - k*k*sigma_rgh_term;
```

Here w_rgh = p_rgh / rho_rgh, c_s2 is the effective sound, sigma_rgh_term the anisotropic stress.

### 5.4 Unit tests and validation
- Verify ΛCDM if rgh_C = 0.
- Linear test: enable small C and verify that C_ℓ differs marginally at high ℓ.
- Compare with analytical solutions in simplified limits.

## 6. F — Compact and technical response to the criticisms / referee

**Summary of the response**

We thank the referee for his remarks. Below is the synthetic technical response; the main manuscript will be accompanied by detailed appendices and a code deposit.

1. **On the existence of a well-defined Lagrangian and the GR limit.** The action (1) is made explicit; the limit κ, λ → 0 (or H → 0, Φ → 0) reproduces the standard Einstein–Hilbert action. The factors in front of L_H are chosen to guarantee the positivity of the kinetic term of the quaternionic field.

2. **On the absence of ghosts and stability.** We attach in Appendix A the complete analysis of the kinetic matrix obtained by linearizing around Minkowski and FLRW. The application of the Sylvester criterion provides explicit inequalities (D₁, D₂, D₃ > 0); solving these inequalities (analytical/numerical) identifies an admissible region of the (κ, λ, α_W) space where no eigenvalue is negative (no ghosts). The details of the scalar/vector decomposition are provided.

3. **On the bounce term.** Appendix B shows the (schematic) calculation leading to ρ_Θ(a) = C(κ, λ, α_W) (ℏ²/ℓ⁴_P) a⁻⁴. We present the regularization method (adiabatic subtraction / ζ-function) and show that, for C > 0 in the admissible parametric region, a bounce occurs at the scale a_min ~ O(ℓ_P). The analytical expressions and numerical plots for C(κ, λ, ...) are provided as supplementary material.

4. **On perturbations and observables.** Appendix C contains the explicitly derived perturbation equations (scalar and tensor) and gives the implementation procedure in CLASS. A prototype module (fork) is available as supplementary material; test runs (mocks) show the expected qualitative signatures (modifications of C_ℓ at high ℓ, reduction of central cusps in lensing, modifications of H(z) around z ~ 0.5).

5. **PPN and gravitational waves.** Appendix D shows a PPN analysis in the weak limit; for the identified parametric sub-region one obtains γ = β = 1. The speed of gravitational waves remains c_GW = c because the term −¼F² for Φ gives neither mass nor ad hoc dispersion at low order; a quantitative verification (dispersion, polarization) is provided.

**Conclusion.** We attach: (i) analytical appendices A–D (stability, bounce, perturbations, PPN), (ii) a prototype CLASS code, (iii) notebooks showing test runs. We are ready to provide additional runs requested by the referees.

*End of the technical response.*

## Appendix A — Algorithmic details for the diagonalization of K

This appendix gives the algorithmic (symbolic) procedure to extract a, b, c, d, e, f and solve D₁, D₂, D₃ > 0. (Procedure: linearization + spin-S decomposition; extraction of the q̇ᵢq̇ⱼ terms; factorization, simplification; analytical/numerical resolution.)

## Appendix B — Calculation scheme for C(κ, λ, α_W)

Details of the steps to compute the regularized sum of zero-point energies and isolate the coefficient of the a⁻⁴ term. Recommended tools: adiabatic regularization up to order 4, or ζ-function + covariant counterterms.

## Appendix C — Useful forms for CLASS

Examples of hooks to modify, list of CLASS source files to edit (background.c, perturbations.c, input.c) and recommendations for tests and outputs.

## Appendix D — PPN analysis (sketch)

Procedure to obtain the PPN parameters by isolating the quasi-static weak-field order (expansion in v/c); verify the continuity toward GR.

**Acknowledgements.** Document prepared to facilitate the finalization of the preprint and numerical implementation.

---

*Source: L. Besson, "Analyses techniques pour la RGH (A,B,C,D,F)", Zenodo, November 2025, DOI 10.5281/zenodo.17555967. Complete translation from the 7-page manuscript PDF by Forge (translation-qc), 2026-08-29.*

## Translator's QC note (pending)
- Complete translation of the full 7-page technical analysis: sections A, B, C, D, F, the Sylvester ghost-absence criterion, the bounce derivation, the CLASS pseudocode (preserved verbatim), and the referee response.
- Terminology: "absence de fantômes" → "absence of ghosts"; "matrice cinétique" → "kinetic matrix"; "critère de Sylvester" → "Sylvester criterion"; "big bounce" kept; "rebond" → "bounce"; "champ quaternionique" → "quaternionic field"; "potentiel de jauge Weyl" → "Weyl gauge potential"; "dérivation paramétrique" → "parametric derivation"; "soustraccion adiabatique" → "adiabatic subtraction"; "fonction ζ" → "ζ-function".
- Cross-links: RGH's "quaternionic field + emergent Weyl gauge" and "geometric quantum condensates driving a bounce" map onto the subtle-field/cohesion-vacuum thesis. Strong authoring material for the French aether-physics thread.
- No [pN] page markers in source (PDF).