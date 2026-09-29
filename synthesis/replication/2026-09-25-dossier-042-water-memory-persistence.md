---
name: Dossier 042 — Water Memory Persistence Test
description: "Replication dossier for the claim that water activated by a rapid thermal transition holds a non-equilibrium clathrate-cavity state that relaxes over a CALCULABLE time — about 10 days at 20 C for the deficit state, about 4 minutes for the excess state (Vysotskii & Kornilova, Vestnik MGU, 2004). Home-replicable, ~$60-150, a 14-day protocol. The water field's first card whose endpoint is a TIME CONSTANT, and its first card built on a calculated prediction rather than a device claim."
---

# Dossier 042 — The Water Memory Persistence Test

**Status:** protocol
**Domain:** water (the time dimension of water's state — how long a thermal-history memory persists) / Homesteading mirror
**Tier:** straw (home-scale, ~$60–150; a 14-day protocol)
**Created:** 2026-09-25

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-09-25-dossier-042-water-memory-persistence` · authored_at `2026-09-25` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

**Source docs (AFLinks Vault):**

- `sources/2026-09-25-scout-a-langs-2.md` find 7 — the scout entry that flagged this paper, `practical_applicability: conceptual-to-buildable`, and named it the T2 ("testable, apparently untested") category: *"the storage-duration calculation is a falsifiable prediction."*
- **Primary document:** В.И. Высоцкий, А.А. Корнилова, *«Физические основы долговременной памяти воды»* (Physical foundations of long-term memory of water), **Вестник Московского университета, Серия 3, Физика. Астрономия, 2004** — https://cyberleninka.ru/article/n/fizicheskie-osnovy-dolgovremennoy-pamyati-vody — **fetched and read in full this run.** V.I. Vysotskii (Kiev National University, solid-state physics dept.) and A.A. Kornilova (Moscow State University).

**Honest note on doc-id verification:** the AFLinks Vault repo is not present in this sandbox, so no `doc:<id>` was verified against the live index this run. Sources are cited by repo path (scout slug) plus the primary URL, which the quest-card schema explicitly allows (`source_doc: "doc:<id> or translation slug"`). Stated, not papered over.

---

## The claim (as asserted by the source)

**Water has a long-term "memory": a non-equilibrium state of its clathrate cavity structure, set by a rapid thermal transition, which relaxes back to equilibrium over a calculable time.**

The paper's stated contribution is explicit and unusual: *«Впервые вычислена длительность хранения информации»* — **"for the first time, the storage duration of the information is calculated."** Most of the water-memory literature asserts an effect and stops; this paper puts a lifetime on it. That is what makes it testable.

**The model, in the paper's own terms.** Water is treated as Pauling's clathrate model: a hydrogen-bonded framework of pentagonal dodecahedra (each ~2.6 Å inscribed radius, 20 water molecules at the vertices, 12 pentagonal faces) enclosing microcavities whose ~2.5 Å windows are slightly narrower than a water molecule (~2.76 Å). The framework holds 20–30 % of the molecules at room temperature. Cavity occupancy follows a Boltzmann distribution and rises with temperature:

| Water temperature | Fraction of cavities filled |
|---|---|
| 4 °C | 18 % |
| 36.6 °C | 38 % |
| 55 °C | ~50 % |

**The mechanism of "memory."** A molecule entering or leaving a cavity must deform (its outer size must shrink by ΔR ≈ 0.26 Å), which costs ΔEм ≈ **1.1 eV** — far above thermal energy (k_BT ≈ 0.025 eV at room temperature). So the spontaneous transition is strongly suppressed and the relaxation time is enormous. The paper computes it:

**τ1w — the deficit state (empty cavities filling back up; produced by *rapid heating* of the whole water):**

| T | 1 °C | 10 °C | **20 °C** | 30 °C | 36.6 °C | 40 °C | 50 °C | 60 °C | 70 °C | 90 °C |
|---|---|---|---|---|---|---|---|---|---|---|
| τ1w | 300 d | 49 d | **10 d** | 58 h | 24 h | 15 h | 4.4 h | 1.3 h | 27 min | 3 min |

**τ2w — the excess state (filled cavities emptying; produced by *rapid cooling*):**

| T | 1 °C | 10 °C | **20 °C** | 30 °C | 36.6 °C | 40 °C | 50 °C | 60 °C | 70 °C | 90 °C |
|---|---|---|---|---|---|---|---|---|---|---|
| τ2w | 30 min | 14 min | **4 min** | 1.5 min | 45 s | 30 s | 12 s | 4 s | 1.5 s | 0.3 s |

**The predicted property change (the part a family can measure):**

- **Rapidly-heated water** → *«избыток как аморфной воды, так и количества незаполненных микропустот»* — an excess of both amorphous water and empty cavities → **lower bulk density** (*«меньшую объемную плотность»*) and **lower viscosity** (*«ее вязкость будет значительно меньше»*).
- **Rapidly-cooled water** (or long-compressed water, or mountain-spring water) → a deficit of amorphous water and filled cavities → **higher density and viscosity**.

**The asymmetry is the signature.** The paper predicts the two directions decay on wildly different timescales at the same temperature — **~10 days for the deficit state, ~4 minutes for the excess state at 20 °C.** A real clathrate effect should show that asymmetry; a temperature artifact cannot produce it.

**Activation methods the paper names:** heating/cooling, **magnetic fields**, **ultrasound**, and **all-round compression** — all described as ways to drive the cavity population away from its equilibrium value. (The card uses the thermal route because it is the one a home can control precisely.)

**Claimants:** V.I. Vysotskii & A.A. Kornilova (Kiev National University / Moscow State University), *Vestnik Moskovskogo Universiteta*, Ser. 3, 2004.
**Verification status:** **unreplicated** — a model calculation with stated parameters; no independent replication of the storage-duration figure is known, and none was found this run.
**Mainstream position:** the clathrate/Pauling model of water is a real minority model (Pauling 1959); "water memory" as a phenomenon is contested, and the mechanism here is a model estimate, not a measurement.

---

## Honest status of the claim — stated up front

1. **This is a calculation, not a measurement.** The paper derives the storage duration from a model. Its two key parameters (ΔEм ≈ 1.1 eV forward, ≈ 0.9 eV reverse) are *«определены нами исходя из модельных расчетов»* — determined from model calculations — and the authors write plainly that if those parameters are refined, *«соответствующие значения τ1w и τ2w могут существенно изменяться»* — **the resulting times may change substantially.** The card is therefore testing a *model's* prediction, and it says so.
2. **The paper is about pure water and excludes dissolved impurities** (*«относятся к чистой воде и не рассматривают влияние растворенных примесей»*), including iron ions and microparticles, which the authors note can produce *other* effects.
3. **The medical aspect is "extremely weakly studied"** — the authors' own words (*«медицинский аспект действия активированной воды изучен крайне слабо»*). **This card makes no health claim of any kind.** It measures two physical properties of water.
4. **"Water memory" as a field is contested** (Benveniste 1988, Montagnier 2009, Emoto). This card does not test "water memory" in general. It tests **one specific, quantified prediction** from one physics-journal paper: that a thermal-history state exists, changes density and viscosity, and relaxes with a stated time constant and a stated temperature dependence.
5. **The predicted effect is small, and a home test may only see its direction and its time course**, not its absolute magnitude. The card states the resolution it needs and treats a rig that cannot resolve the effect as VOID rather than as a refutation.

---

## The protocol — one thermal history, one pycnometer, one time course

The testable core: **if a rapid thermal transition leaves water in a state that changes its density, then water given a rapid thermal history should differ measurably in density from water of the same batch given a slow thermal history — and the difference should decay with a time constant near the paper's prediction (≈10 days at 20 °C for the deficit state), not persist indefinitely and not vanish at once.**

### Materials (~$60–150)

1. **A precision scale, 0.001 g (1 mg) resolution** (~$20–35). The predicted density change is roughly 0.5–0.6 % (see below), so 1 mg on a 25 mL sample (≈ 0.00004 g/mL) is comfortably sufficient — this is a case where the cheap instrument is enough, and the card says why.
2. **A 25 mL pycnometer** (specific-gravity bottle with a capillary stopper) (~$10–20), or a 25 mL volumetric flask with a ground stopper. The pycnometer is preferred: the capillary stopper fixes the volume exactly at the fill temperature.
3. **A thermometer reading to 0.1 °C** (~$10–15).
4. **A temperature-controlled water bath** — a large basin with an aquarium heater and a circulation pump, or a sous-vide circulator (~$20–40). **This is the card's critical instrument** (see "the crux").
5. **Sealed glass jars** (one per arm, ~250 mL) with airtight lids (~$10).
6. **An ice bath / refrigerator** for the 4 °C chill.
7. **Optional: a flow cup** (Ford cup #4 or equivalent, ~$10–15) for the viscosity arm.

### Design — the parts that make it a measurement

1. **All arms come from ONE boiled batch.** Boiling drives out dissolved CO₂/O₂, and degassing itself changes density and viscosity. So **every arm is boiled identically** — the only difference between arms is the *thermal history after boiling*. This is the paper's own definition of "ordinary water": *«Такая вода получается после длительного кипячения и медленного остывания или после очень длительного отстаивания»* — obtained after long boiling and slow cooling, or very long standing.
2. **Arm A — Equilibrated control.** Boil 10 min, cool slowly (insulated, ~2 h) to 20 °C, hold. This is the paper's equilibrium state.
3. **Arm B — Rapid-heat activated (deficit state).** From Arm A's equilibrated water, chill to 4 °C for ≥ 2 h (so it reaches the 4 °C equilibrium occupancy of 18 %), then **warm the whole volume rapidly to 20 °C** in the bath and measure immediately. Predicted: **lower density and lower viscosity than Arm A**, relaxing over ≈ 10 days at 20 °C.
4. **Arm C — Rapid-cool activated (excess state), optional.** Water held at ~50 °C (equilibrium occupancy ~50 %) **cooled rapidly** to 20 °C in an ice bath, measured within 60 s. Predicted: **higher density and viscosity**, vanishing within ~4 minutes at 20 °C. **This arm is the asymmetry test** — and its 4-minute decay may be shorter than a measurement cycle, in which case that is a *resolution limit*, not a refutation, and is reported as such.
5. **The comparison is thermal-history versus thermal-history, not "special water" versus tap water.** Both arms are the same water, boiled the same way, measured the same way. Only the post-boil thermal path differs.
6. **Primary endpoint: density by pycnometer.** Chosen deliberately: water's density near 20 °C changes only ~0.02 %/°C, roughly **100× less temperature-sensitive than viscosity** (~2.5 %/°C). Since temperature is the card's main enemy, the least temperature-sensitive endpoint is the primary one. Weigh the filled pycnometer at 20.0 °C, subtract the empty mass, divide by the certified volume.
7. **Secondary endpoint: efflux time through a fixed orifice** (viscosity proxy), at the same controlled temperature. Reported, but **not** used for the verdict, because a 0.5 °C arm-to-arm difference produces ~1.2 % in efflux time — comparable to the predicted effect. Stated, not hidden.
8. **Temperature control is the crux.** Every measurement at **20.0 ± 0.1 °C**, every sample equilibrated in the bath for 10 minutes before weighing, **arms interleaved** (A, B, A, B, …) so slow drift cancels. A 0.5 °C difference between arms would produce ~0.01 % in density (below the predicted 0.5 %) but ~1.2 % in viscosity (at the predicted effect) — which is exactly why density is primary.
9. **The time course.** Arm B versus Arm A at t = 0, 1, 2, 4, 7, 10, 14 days. Arm C (if run) at t = 0, 2, 5, 10, 20, 40 min.
10. **The assay's own validity check.** **Arm A must stay flat** — within its own repeat scatter — across the 14 days. If Arm A drifts as much as Arm B, the thermal or instrument control is inadequate and **the run is VOID, not a refutation.** An assay that cannot hold its own control still cannot test the claim.
11. **Storage.** All arms in the same dark, stable place; the storage temperature logged daily (the predicted time constant changes steeply with temperature — 10 d at 20 °C, 58 h at 30 °C — so the storage temperature is part of the result, not a footnote).
12. **Optional extension — the temperature dependence.** Split Arm B; store half at 20 °C and half at 30 °C. The paper predicts the 30 °C half relaxes ~4× faster (10 d → 58 h). This is a **differential** prediction and is the strongest form of the test, because instrument drift affects both halves equally.
13. **Pre-register** the arm order, the number of repeats, the timepoints, the thresholds, and the scoring rule before the first weighing.

### Endpoints

- **Primary — the density difference at t = 0.** Δρ = ρ(Arm A) − ρ(Arm B), in g/mL, against the pooled repeat scatter.
- **Primary — the relaxation time constant.** The time for Δρ to fall to 1/e of its t = 0 value, fitted across the 14-day series, compared to the paper's ≈ 10 days at 20 °C.
- **Secondary — the asymmetry.** Whether Arm C's excess vanishes within minutes while Arm B's deficit persists for days.
- **Secondary — the temperature dependence** (if the extension is run): the ratio of the 30 °C to the 20 °C time constants, against the predicted ~4×.
- **Control — Arm A's flatness.** The control's own drift across 14 days, which sets the verdict's floor.

### Pre-registered pass/fail

- **PASS:** Δρ at t = 0 is **≥ 3× the pooled repeat scatter**, of the **same sign in ≥ 4 of 5 independent runs**, converging to Arm A with a time constant **within ~2× of the paper's 10 days at 20 °C (i.e. 5–20 days)**; and, if Arm C is run, **Arm C's excess vanishes within minutes** (the predicted asymmetry).
- **FAIL:** Δρ at t = 0 is **within the pooled repeat scatter in ≥ 4 of 5 runs** → no measurable thermal-history memory in water at home scale. A complete result; earns the Skeptic's Star.
- **VOID:** Arm A drifts as much as Arm B across the 14 days; or the bath cannot hold 20.0 ± 0.1 °C; or the pycnometer repeat scatter exceeds the predicted effect size. **Report the resolution achieved and the control required, not a verdict.** An instrument that cannot see the effect has not tested it.
- **ARTIFACT:** Δρ tracks the sample temperature difference between arms rather than the thermal history, or disappears when both arms are brought to exactly the same temperature before weighing → the reading is the temperature confound, and the card records it as such.

---

## Why it matters — and what makes it a different card

**It fills the water field's missing dimension.** Every water card in the queue is about water's **structure** (001 Wasserwirbler, 004 hyperbolic funnel, 009 EZ water, 019 Dodonov vortex, 031 MVP vortex motor), its **vitality** (025 Piccardi P, 028 water memory imprint), or its **quantity and path** (037 contour swale). **None of them tests water's *time* dimension** — how long a state persists — and **none has a time constant as its endpoint.**

**It is the queue's first water card built on a *calculated* prediction.** The source's headline contribution is a number — the first calculated storage duration in the water-memory literature. A number can be tested; an assertion cannot. The card tests the number.

**The asymmetry is a real discriminating prediction.** The paper says the deficit state lives ~10 days at 20 °C and the excess state ~4 minutes. That is not a decoration: a temperature artifact, a dissolved-gas difference, or a container effect cannot produce a 3,600× asymmetry between two arms of the same water. A family that sees B persist and C vanish has seen the model's signature.

**The honest limits are the card's spine.** The paper is a model, not a measurement; its parameters are estimates the authors say may change substantially; it is about pure water; its medical claims are its own admitted weak point and this card makes none. What remains is a clean physical question a kitchen can ask.

**Safety:** boiling water and glassware. Use heat-safe containers, vent the lids during the boil, handle the bath with care. Nothing here is hazardous; the only real risk is a scald.

---

## Replicability: `home`

- Build cost: **~$60–150** (a 1 mg scale, a pycnometer, a 0.1 °C thermometer, a temperature-controlled bath, sealed jars).
- Time: 14 days of daily measurements, ~15 minutes each.
- Accessibility: a kitchen, a scale, a bath, and a written table.
- The one demanding requirement is **temperature control to ±0.1 °C** — which is why density (not viscosity) is the primary endpoint.

## Apparatus (Bill of Materials)

- A 0.001 g precision scale.
- A 25 mL pycnometer (or volumetric flask with stopper).
- A 0.1 °C thermometer.
- A temperature-controlled water bath (aquarium heater + pump, or sous-vide circulator).
- Sealed glass jars (one per arm).
- An ice bath / refrigerator.
- Optional: a flow cup for the viscosity arm.

## What a result means (and what it does not)

- A **pass** means: this kitchen, on this water, found a density difference between two thermal histories that decayed with a time constant near the paper's prediction, and (if run) the predicted asymmetry. It would be the **first home replication of a calculated water-memory lifetime** — and the first thing to do with it is hunt for the confounds, because a temperature difference between arms is the obvious way to manufacture one. A pass is a reason to look harder, not a reason to believe.
- A **fail** means: at home scale, the thermal-history difference is below the pycnometer's resolution. That is a complete, honest outcome, and it is the expected one for a model whose parameters the authors themselves flag as provisional.
- Either way the confounds must be named in the report: **the sample temperature difference between arms**, **dissolved gas**, **microbial growth over 14 days**, **the pycnometer's fill repeatability**, and **the fact that a home pycnometer cannot separate a 0.5 % bulk-density change from a 0.5 % volume error.**

## Cross-links

- **Dossier 028** (Water Memory Imprint) — the *imprinting* claim (a field writes information into water); this dossier is the *persistence* claim (how long any such state lasts). Different question, same field.
- **Dossier 009** (EZ Water Exclusion Zone) — water's *structure* at a hydrophilic interface; this is water's *bulk state* after a thermal history.
- **Dossier 025** (Piccardi Cosmic Precipitation) — the other card that tests a water-property claim against an external variable (there, cosmic; here, thermal history).
- **Dossier 037** (Contour Swale Rain-Retention) — water's quantity and path, the other half of the water field.
- **Claim status record:** none directly — the clathrate model is a minority mainstream model, not a suppressed lineage.
