---
name: "Radioactive Decay — Does Rotation Touch the Nucleus? The Tomsk Independent-Expert Replication (Melnik & Mokeev, Siberian Physical-Technical Institute)"
description: "An Am-241 source with a Pu-239 admixture — two isotopes resolved in one alpha spectrum, each serving as the other's internal control — was counted while a steel vessel of liquid spun on the same vertical axis at 8,000 rpm, then counted again after the motor stopped. The Tomsk group, framing the work explicitly as an independent-expert replication of earlier rotation experiments, report that rotation alters the alpha-decay distribution (multiplet structure; Am intensity falls while Pu rises; one-way ANOVA Fisher F=98 against a critical 3.85) and that a metastable after-effect persists once the motor is off. Filed LOW: a single self-described institute outside the metrology traceability chain, with the strong counter-ledger from JRC Geel sitting beside it."
---

# Validation — The Tomsk Rotation Effect on Alpha Decay (Melnik & Mokeev)

**Domain:** nuclear decay as a field detector (the "non-electromagnetic field of rotating objects" — the torsion lineage)
**Recorded:** 2026-10-15 (Replication Seeder)

## What was claimed

The torsion lineage's strongest testable form of its central claim: if radioactive decay rates report the state of the surrounding field, then **engineering the field locally — with a rotating mass — should move the decay rate on command.** The Tomsk group's report is framed explicitly as an **independent-expert replication of earlier rotation experiments**, i.e. it is a *replication record by its own account*, not an original discovery claim.

## Who tested it, when, and where

**I. A. Melnik** and **D. Yu. Mokeev**, at the **Siberian Physical-Technical Institute** (Tomsk). Published via **trinitas.ru** (document 02311025), the self-publishing channel of the Russian "Academy of Trinitarianism." Companion theoretical papers by the same group and by Kholodov & Goryachev sit alongside it in the same channel.

## Method — what they actually did

The design is disarmingly simple and contains one genuinely good control:

- **Source:** **americium-241** with a **plutonium-239** admixture.
- **Detector:** a **GaAs semiconductor detector** resolving the **5485.6 keV (Am)** and **5155 keV (Pu)** alpha peaks **simultaneously** — so the two isotopes are measured in the *same* spectrum, on the *same* detector, at the *same* moment, and **each serves as the other's internal control.**
- **Manipulation:** an **asynchronous motor spins a steel vessel of liquid at 8,000 rpm** on the same vertical axis as source and detector.
- **Then:** the motor is **switched off**, and counting continues — testing for a metastable after-effect.
- **Analysis:** histograms of the full set of relative samples; **one-way analysis of variance**.

## Reported result

> "Constructing the histogram of the full set of relative samples showed convincingly that rotation acts on the alpha decay of the atomic nucleus; the alpha-particle distribution becomes multiplet-structured, the americium intensity falls while the plutonium isotope's rises… One-way analysis of variance of these distributions gave a **Fisher coefficient F=98** (critical value 3.85)."

The group also reports the field's properties as **chiral polarization** (clockwise ≠ counterclockwise), **memory** (a metastable state that relaxes slowly after the motor stops), and a dependence on the internal state of the rotating object.

## Confidence: LOW

- **Single laboratory**, and one outside the interlaboratory traceability chain — a self-described institute of the Academy of Trinitarianism, self-publishing through trinitas.ru.
- **The statistic cannot carry the claim alone.** **F=98** speaks to a difference between two sample sets; by itself it **cannot exclude systematic coupling between the motor state and the detector** — vibration, EMI, and temperature all change when an 8,000 rpm motor stops.
- **The "metastable after-effect" is exactly the shape an instrumental thermal relaxation would take.** That is not a refutation; it is the rival explanation that the described design does not exclude.
- **No mechanism** is proposed for the claimed multiplet structure of the alpha spectrum, and **no metrology laboratory has replicated the rotation effect.**

## Counter-ledger (it must sit beside the record)

The decay-constant question has one of the strongest skeptical ledgers in the archive, at the highest instrumental level:

- **Pommé et al. (JRC Geel)** — *"Is decay constant?"*, *Appl. Radiat. Isot.* **134** (2018) 6–12 — examined **twelve independent long-term decay datasets** across α, β⁻, β⁺ and EC nuclides, at every frequency from 0.08 to 20 yr⁻¹, and found **no common oscillations** beyond small annual effects that track the **instruments themselves** (their fitted amplitudes stay below 3σ; their keyword list, unusually, includes "Cognitive bias").
- **Norman et al.** answered **Jenkins–Fischbach**'s Earth–Sun-distance correlation in the *same journal* (*Astropart. Phys.* **31**, 2009) with a 22-nuclide reanalysis.

So the honest state of this lane: **every positive has a paired null of equal instrumental quality**, and the Tomsk result is the rotation leg of that pattern.

## Why it is a replication, and why the internal control matters

Two reasons this record exists rather than being waved away as one more torsion claim:

1. **It is explicitly a replication.** The report positions itself as an independent-expert re-test of earlier rotation experiments, which places it squarely inside this Yard's definition.
2. **The Am/Pu internal control is a real design idea.** Two isotopes in one spectrum, on one detector, moving in *opposite* directions (Am down, Pu up) rule out every drift that would move the whole spectrum together — gain drift, temperature, dead-time. The remaining confounds (vibration and EMI coupling to the motor state) are real, but the design has already excluded the easy ones. That is more than most of its genre manages, and it is precisely why a **clean null** on this rig would be informative.

## Source

- **Corpus:** `synthesis/2026-10-13-decay-inconstant-constant-field-detector.md` §5 ("Tomsk: Rotation Touches the Nucleus") and abstract — carries the Russian text, translation, the F=98 statistic, and the skeptical ledger quoted above.
- **Primary (external, cited by the corpus synthesis):** Melnik, I. A. & Mokeev, D. Yu., "Study of the Remote Influence of Rotation on the Decay Rate of Alpha-Radioactive Sources," trinitas.ru **02311025** — https://www.trinitas.ru/rus/doc/0231/004a/02311025.htm
- **Related in this Yard (torsion / decay rail):**
  - `synthesis/validations/2026-10-03-torsind-pugach-temporal-effects.md`
  - `synthesis/validations/2026-10-09-torsion-vortex-em-jiang-2026.md`
  - `synthesis/validations/2026-10-10-torsion-materials-nanu-triple-negative.md`
  - `synthesis/validations/2026-09-25-torsion-torsimetry-text-meaning-gao.md`

## Honest framing

We hold no brief — the test is the point. **Recorded as attempted / reported:** a Tomsk group, calling its own work a replication, spun a mass beside an Am/Pu source and reported a statistically large change in the alpha distribution with an opposite sign for the two isotopes. Filed **LOW** — single-lab, outside traceability, with the after-effect indistinguishable from thermal relaxation on the described evidence.

**Not home-testable.** This is a lab experiment: it needs a sealed alpha source and a semiconductor spectrometer, and it is not a candidate for the Replication Yard's straw tier. The decisive experiment is named in the corpus and has never been run: a **pre-registered, blinded, multi-laboratory decay dataset** — one source type (Am-241, for continuity with both the Tomsk and the Tsinghua qi experiments), counted simultaneously by metrology-chain ionisation chambers *and* semiconductor spectrometers at three or more sites, with full environmental telemetry published alongside the counts and the frequency list fixed in advance. The cost is trivial by big-science standards; the obstacle is that no program's survival depends on the answer.
