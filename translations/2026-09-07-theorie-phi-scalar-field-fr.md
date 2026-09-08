---
title: "Rigorous Study of a Light Scalar Field Coupled to Matter in Galaxies: Application to Rotation Curves"
original_title: "Étude rigoureuse d'un champ scalaire léger couplé à la matière dans les galaxies : application aux courbes de rotation"
source_url: "https://doi.org/10.5281/zenodo.17311741"
source_language: fr
language: en
translator: Forge (translation-qc)
date: 2026-09-07
source_site: Zenodo
tags: [scalar field, galactic rotation curves, dark matter alternative, MOND, SPARC, Klein-Gordon, Yukawa, baryonic density, Fabien Toulgoat, cosmology, gravitational theory]
---

# Rigorous Study of a Light Scalar Field Coupled to Matter in Galaxies: Application to Rotation Curves

**Author:** Fabien TOULGOAT (fabientoulgoat@hotmail.com)
**DOI:** 10.5281/zenodo.17311741

## Abstract

Galactic rotation curves present significant deviations from Newtonian predictions based on visible matter. This work proposes an alternative model based on a light scalar field Φ, coupled to baryonic density, capable of locally modifying the effective gravitation. The model is developed within a rigorous theoretical framework, with quantitative testable predictions on SPARC data. The field parameters (mass m ~ 10⁻²⁷ eV/c² and coupling constant α ~ G) are physically motivated and lead to observable effects at the galactic scale. This approach offers a testable and falsifiable alternative to the dark matter paradigm and MOND theories.

## Table of Contents

1. Introduction
2. Theoretical model and dimensional analysis
3. Klein-Gordon equation coupled to baryonic density
4. Solution for the potential Φ via Green's function
5. Modification of the gravitational force and rotational velocity
6. Modeling the galactic density
7. Fitting methodology on SPARC data
8. Numerical implementation and parameter estimation
9. Consistency tests and observational constraints
10. Distinctive predictions and comparisons
11. Discussion and perspectives
12. Conclusion
13. References and technical appendices

---

## 1. Introduction

The observed galactic rotation curves reveal a major discrepancy with the predictions of Newtonian gravity applied to visible matter. This anomaly, discovered by Vera Rubin and Kent Ford in the 1970s, suggests either the existence of non-baryonic dark matter, or a modification of gravity at galactic scales.

This work explores a third path: the hypothesis of a light scalar field Φ, coupled directly to baryonic matter, capable of generating an additional gravitational force with finite range. Unlike MOND approaches that modify dynamics for low accelerations, or dark matter models that postulate exotic particles, our model proposes an explicit physical mechanism based on a fundamental field.

The objective is to develop a rigorous theoretical framework, mathematically coherent, and empirically testable to quantitatively explain galactic rotation curves without recourse to non-baryonic dark matter.

---

## 2. Theoretical model and dimensional analysis

### 2.1 Lagrangian of the system

The model is based on a real scalar field Φ coupled to gravity and matter. The total Lagrangian reads:

ℒ = (1/16πG)R - (1/2)gμν∂μΦ∂νΦ - (1/2)m²Φ² + αΦρ + ℒmatter

where:

- R is the Ricci scalar
- m is the effective mass of the scalar field
- α is the field-matter coupling constant
- ρ is the baryonic matter density

### 2.2 Complete dimensional analysis

Dimensional coherence imposes the following constraints:

Fundamental dimensions:
- [Φ] = L²T⁻² (dimension of a gravitational potential)
- [m] = M (mass, expressed in units eV/c²)
- [α] = L⁴M⁻¹T⁻² (so that [αΦρ] = L⁻¹T⁻² like the Lagrangian density)
- [ρ] = ML⁻³ (standard mass density)

The coupling term αΦρ has the dimension of a Lagrangian density, ensuring the coherence of the model.

### 2.3 Physical motivation for the coupling

The linear coupling αΦρ represents the simplest interaction between the scalar field and ordinary matter. This type of coupling appears naturally in several theoretical contexts:

- Scalar-tensor theories (generalization of Brans-Dicke)
- Quintessence models with matter coupling
- Effective theories of modified gravity
- Models with compactified extra dimensions

---

## 3. Klein-Gordon equation coupled to baryonic density

### 3.1 Derivation of the field equation

Variation of the Lagrangian with respect to the field Φ yields the modified Klein-Gordon equation:

□Φ - m²Φ = -αρ

where □ = gμν∇μ∇ν is the covariant d'Alembert operator.

### 3.2 Quasi-static approximation

For quasi-static galactic systems and in the weak-field limit, the equation reduces to:

(∇² - m²)Φ(r) = -αρ(r)

This inhomogeneous Helmholtz equation governs the distribution of the scalar field in a galaxy.

### 3.3 Properties of the equation

The equation exhibits several important characteristics:

- Finite range: The term -m²Φ imposes a characteristic length λ = 1/m
- Linearity: Superposition principle applicable
- Local source: The field responds directly to baryonic density
- Exponential decay: Natural suppression at large distances

---

## 4. Solution for the potential Φ via Green's function

### 4.1 Yukawa Green's function

The general solution of the equation (∇² - m²)Φ = -αρ is expressed as a Green's integral:

Φ(r) = α ∫ GY(|r - r'|) ρ(r') d³r'

where GY(r) = e^(-mr)/(4πr) is the Yukawa Green's function in three dimensions.

### 4.2 Explicit solution

In spherical coordinates, for a matter distribution ρ(r'), the scalar field at point r reads:

Φ(r) = (α/4π) ∫ [e^(-m|r-r'|) / |r-r'|] ρ(r') d³r'

### 4.3 Asymptotic properties

The solution exhibits the following limiting behaviors:

- r → 0: Φ(r) ~ α∫ρ(r')d³r'/(4πr) (Newtonian behavior)
- r ≫ 1/m: Φ(r) ~ e^(-mr)/r (exponential decay)
- m → 0: Recovery of the Coulomb potential (1/r)

---

## 5. Modification of the gravitational force and rotational velocity

### 5.1 Effective gravitational force

The scalar field modifies the equation of motion for test particles. The total acceleration reads:

a = -∇(ΦN + Φ)

where ΦN is the Newtonian gravitational potential and Φ is the scalar field contribution.

### 5.2 Circular rotation velocity

For stable circular motion, the equilibrium between centripetal force and effective gravitational force gives:

vrot²(r) = r d/dr [ΦN(r) + Φ(r)]

### 5.3 Decomposition of contributions

The velocity can be decomposed into distinct contributions:

vrot²(r) = vNewton²(r) + vscalar²(r)

where:

- vNewton²(r) = GMenc(r)/r
- vscalar²(r) = r dΦ/dr

---

## 6. Modeling the galactic density

### 6.1 Disk density profile

The baryonic matter density is modeled by a standard exponential profile:

ρdisk(r,z) = ρ₀ exp(-r/Rd) exp(-|z|/zd)

where Rd is the scale radius of the disk and zd its characteristic height.

### 6.2 Bulge component (optional)

For galaxies with a significant central bulge, a spherical component is added:

ρbulge(r) = ρb (r/Rb)^(-γ) exp[-(r/Rb)^(1/n)]

### 6.3 Total baryonic mass

The total baryonic mass interior to radius r is expressed as:

Mbar(r) = 2πρ₀Rd²zd [1 - (1 + r/Rd)exp(-r/Rd)]

### 6.4 Observational parameters

The density profile parameters are constrained by:

- Photometry in I, K bands (stellar mass tracers)
- HI kinematics (neutral gas, total mass tracer)
- Mass-to-light ratio Υ⋆
- Gas fraction fgas = Mgas/Mbar

---

## 7. Fitting methodology on SPARC data

### 7.1 SPARC database

The SPARC database (Spitzer Photometry and Accurate Rotation Curves) provides high-quality rotation curves for 175 spiral and irregular galaxies, with:

- Spitzer photometry in the 3.6 μm band (optimal tracer of M⋆)
- High-resolution HI kinematics
- Quantified observational uncertainties
- Wide range of morphological types and masses

### 7.2 Likelihood function

The fitting of parameters m and α is performed by maximum likelihood, equivalent to minimizing χ²:

χ²(m,α) = Σᵢ [(vobs,i - vtheo,i(m,α))² / σᵢ²]

where the sum runs over all data points from all galaxies considered.

### 7.3 Fitting strategy

The optimization follows a hierarchical approach:

1. Individual fitting: Determination of optimal (m,α) for each galaxy
2. Correlation analysis: Search for relations m(M⋆), α(morphological type)
3. Global fitting: Universal parameters over the entire sample
4. Cross-validation: Testing on independent subsamples

### 7.4 Comparisons with alternative models

The comparative evaluation includes:

- Pure Newtonian model: Baryonic matter only
- Standard ΛCDM: NFW dark matter profile
- MOND: Bekenstein-Milgrom formulation
- Hybrid models: Dark matter + gravitational modifications

### 7.5 Galaxy selection criteria

To ensure the robustness of the analysis, we apply the following criteria:

- Photometric quality: S/N > 10 in the 3.6 μm band
- Radial extent: Rmax > 2Rd
- Kinematic resolution: > 10 independent points
- Inclination: 30° < i < 80° (avoid face-on and edge-on)

---

## 8. Numerical implementation and parameter estimation

### 8.1 Preliminary physical estimates

The expected orders of magnitude for the parameters are determined by dimensional analysis and observational constraints:

Scalar field mass: m ~ 10⁻²⁷ eV/c²
- Compton wavelength: λ = ħ/(mc) ~ 1 kpc
- Consistent with the scale of observed galactic effects

Coupling constant: α ~ G ~ 6.67×10⁻¹¹ m³ kg⁻¹ s⁻²
- Natural gravitational order of magnitude
- Ensures observable effects without violating local constraints

### 8.2 Numerical computation algorithm

The numerical implementation proceeds through the following steps:

```python
import numpy as np
from scipy.optimize import minimize
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Physical constants
G = 6.67430e-11  # m³ kg⁻¹ s⁻²
c = 299792458    # m/s
eV_to_kg = 1.782661907e-36  # Conversion eV/c² → kg
kpc_to_m = 3.0857e19        # Conversion kpc → m
solar_mass = 1.9885e30       # kg

def compute_scalar_field(r, m, alpha, rho_0, R_d, max_radius=5):
    """Computation of the scalar field by Yukawa integration"""
    def integrand(r_prime):
        if r_prime == 0:
            return 0
        distance = abs(r - r_prime)
        if distance < 1e-6:
            distance = 1e-6
        rho_prime = rho_0 * np.exp(-r_prime / R_d)
        yukawa_kernel = np.exp(-m * distance) / (4 * np.pi * distance)
        volume_element = 4 * np.pi * r_prime**2
        return alpha * yukawa_kernel * rho_prime * volume_element

    phi, error = quad(integrand, 0, max_radius * R_d, epsabs=1e-10, epsrel=1e-8)
    return phi

def compute_rotation_curve(radii, m, alpha, rho_0, R_d, M_total):
    """Computation of the complete rotation curve"""
    velocities = []
    for r in radii:
        M_enc = M_total * (1 - (1 + r/R_d) * np.exp(-r/R_d))
        v_newton_sq = G * M_enc / r if r > 0 else 0
        if r > 0:
            dr = r * 1e-4
            phi_plus = compute_scalar_field(r + dr, m, alpha, rho_0, R_d)
            phi_minus = compute_scalar_field(r - dr, m, alpha, rho_0, R_d)
            dphi_dr = (phi_plus - phi_minus) / (2 * dr)
            v_scalar_contrib = r * dphi_dr
        else:
            v_scalar_contrib = 0
        v_total_sq = v_newton_sq + v_scalar_contrib
        if v_total_sq >= 0:
            velocities.append(np.sqrt(v_total_sq))
        else:
            velocities.append(0)
    return np.array(velocities)

def fit_galaxy_parameters(galaxy_data, initial_guess=None):
    """Fitting of parameters m and alpha by χ² minimization"""
    radii = galaxy_data['radii']
    v_obs = galaxy_data['velocities']
    errors = galaxy_data['errors']
    rho_0 = galaxy_data['rho_0']
    R_d = galaxy_data['R_d']
    M_total = galaxy_data['M_total']

    def chi_squared(params):
        m, alpha = params
        if m <= 0 or alpha <= 0:
            return 1e10
        try:
            v_theory = compute_rotation_curve(radii, m, alpha, rho_0, R_d, M_total)
            chi2 = np.sum(((v_obs - v_theory) / errors)**2)
            return chi2
        except:
            return 1e10

    if initial_guess is None:
        m_init = 1e-27 * eV_to_kg
        alpha_init = G
        initial_guess = [m_init, alpha_init]

    bounds = [(1e-30, 1e-20), (1e-15, 1e-5)]
    result = minimize(chi_squared, initial_guess, method='L-BFGS-B',
                     bounds=bounds, options={'ftol': 1e-12, 'gtol': 1e-8})
    return result
```

---

*Translation metadata: source https://doi.org/10.5281/zenodo.17311741 · French · Zenodo, published 2025 · scalar field model for galactic rotation curves by Fabien Toulgoat · translated by Forge 2026-09-07 · cosmology / gravitational theory*
