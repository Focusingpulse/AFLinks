---
name: Torsion / Scalar — Reading Text Meaning with a Torsion-Field Detector (Gao, 2026)
description: The first record in this Yard's torsion/scalar family, filed the way the domain actually presents itself. A self-published preprint reports 19 independent sessions in which a Shkatov-lineage torsion detector gave a systematically higher "torsional contrast" to a certainly-false statement than to a certainly-true one — all 19 signs positive, mean +112.1 arbitrary units, p ≈ 2×10⁻⁶. Recorded with the reason it cannot be taken as evidence of the effect: the protocol cannot be blinded, and does not attempt to be.
---

# Validation — Torsimetry Reads a Truth Value (Gao, rxiv 2608.0099)

**Domain:** torsion fields / scalar waves — instrumental torsimetry and the informational-field claim
**Recorded:** 2026-09-25 (Replication Watch). **First record in this family in the Yard.**

## What was claimed

The **torsimetry** framework of **V. T. Shkatov**: that a torsion field — an informational field associated with rotation and spin, treated in that framework as an attribute of the physical vacuum — is instrumentally detectable as the *torsional contrast* (TC) of an object against the measuring instrument, in units of Torsi (1 Ts = 0.1 rad s⁻¹). Shkatov's stronger, prior claim: that the **semantic content of a text** carries its own informational structure and is measurable — that a torsion detector resolves the meaning of an assertion rather than the ink, paper or screen carrying it.

The hypothesis under test in this paper, in the author's words: *"that the meaning of a word or a sentence is a stable, objective attribute of the text, carried by its torsion field, and that a sufficiently sensitive detector of that field should be able to register it directly"* — with **no language model, no corpus and no GPU training**.

This matters to the Yard for its own reason: the framework's central problem is that **informational "phantoms" accumulate in the object–instrument–operator system** and smear successive readings. The paper's methodological core — Shkatov's **Method of Differential Test Assertions (MDTA-1)** — exists to cancel them by pairing assertions of opposite meaning. That is a real measurement-design problem, honestly named. The question this record has to answer is whether the design that follows actually closes it.

## Who ran it, when

**Peng Gao**, independent researcher, webmaster of a Chinese scalar-wave/torsion-field research network. **Preprint dated 24 August 2026**, posted at **rxiv.org (2608.0099)**. Not peer-reviewed; single author; no co-author, no institution, no funder.

Gao is not new to this line: he is the author of the 2016 viXra paper that used a wooden-frame torsion balance to claim detection of left- and right-handed torsion fields from a dual Tesla coil — the same paper whose own text records that **the frame rotated when a palm was held near a photograph of the frame, at a distance of ~8,000 km**. Same author, same framework, a decade apart.

- **Instrument:** a **GRG-001 torsion-field detector** (Shkatov lineage; earlier generations TSM-021, GRG-01M1/M2/M3, PZ-3D-M1, SADAF-08LC). Connected to a laptop by serial cable; its laser communicator aimed at the task text on a second screen. The unit came from Shkatov's estate, via his son.
- **Readout:** raw counts in **arbitrary units**, with the paper stating explicitly that there is **no absolute calibration to Torsi**.

## Method

Each session targets **one NBA basketball game**. Two statements about its total score are typed into the host program and displayed, with a photograph of the object, on a mirrored second screen:

- scan A: *"the total score will be **greater than** θ"*
- scan B: *"the total score will be **less than** θ"*

θ is chosen **above any physically realisable total** (541.5 to 765.5 across sessions), so A is **certainly false** and B is **certainly true**. Sampling is 4 readings per second, **60 samples per scan**, and the TC of a statement is the mean of its scan. The quantity of interest is

> ΔTC = TC(>θ) − TC(<θ)

`N = 19` independent sessions. The two scans form the MDTA differential pair.

## Result

**ΔTC was positive in all 19 sessions.**

- Mean **+112.1**; SD **38.2**; SEM **8.8**.
- Range **+36.5** (session 4) to **+173.7** (session 14).
- Under the null — a detector insensitive to the truth value of the assertion — each sign would be equally likely either way; 19 of 19 gives **p = 2⁻¹⁹ ≈ 2 × 10⁻⁶**.

The paper also reports, from Shkatov, that mirror-image swastika symbols yield TC of **−6 and +6**, that every letter of the Cyrillic alphabet carries a characteristic TC, and that the TC of the Bible is large-positive while books with "diabolical" connotations gave negative TC. It closes by proposing a **global torsion-field earthquake early-warning network** and describing MDTA as a torsion-based method of prediction.

## Confidence: low — and the reason is structural, not statistical

The arithmetic on the numbers given is fine. The problem is the design.

**The protocol cannot be blinded, and does not try.** The operator knows which statement is impossible — it is definitionally impossible — and the entire apparatus is arranged and attended by the person who also reads the result: the task text typed into the host program, the laser aimed at that text, the photograph of the object displayed alongside it, the session selection, the θ choice. 19 of 19 positive signs is exactly what one expects if the operator's expectation leaks into the measurement through any human-in-the-loop channel — and **there is no arm that separates that from a field effect**. Specifically absent: any sham pair (two statements of identical meaning), any pre-registration, any randomised θ or scan order, any second operator, any blinding of the analyst, any replication by another group.

Also absent, on the face of the record: independent replication; published data or code; a dose–response relation between ΔTC and any property of the assertion; and a null result anywhere in the series.

Context worth keeping alongside it: torsion fields are not recognised as a fundamental interaction; the instrument's output is in arbitrary units with no stated calibration; and the framework being confirmed rests largely on Shkatov's own unpublished technical reports, so the prior is not independently established either. **The honest reading is that this is a measurement of an operator–instrument pair, not of a text.**

## Source

- **Primary:** Gao, P. *"The torsion field detector can know the meaning of words and sentences without GPU training."* rxiv preprint **2608.0099v1**, dated **24 August 2026** — https://rxiv.org/pdf/2608.0099v1.pdf (read in full this run)
- **Prior in the same line by the same author:** Gao, P. *"Attempts to Detect the Torsion Field Nature of Scalar Wave Generated by Dual Tesla Coil System,"* viXra:1607.0130 (2016) — https://vixra.org/abs/1607.0130
- **Framework:** V. T. Shkatov, torsimetry — *Журнал Формирующихся Направлений Науки (ЖФНН)* 2(1), 2013 and 11(4), 2016; MDTA-1 technical report (Tomsk, unpublished); Shkatov, Zamsha, Krinker & Gorokhov, *"Роль глобального сознания в инструментальных исследованиях тонких полей,"* ЖФНН 15–16(5), 2017
- **Related, not read as evidence here:** Balerdi, E. *"A low-cost torsion balance experiment to detect repulsive gravitational anomalies in rotating superconductors,"* Zenodo, 6 June 2026 — https://doi.org/10.5281/zenodo.20574517 (a **proposed** experiment, no results; noted only because it is the other live torsion-balance protocol in the current literature)

## Honest framing

We hold no brief — the test is the point. This is the Yard's **first** record in the torsion/scalar family, and it is filed as the domain actually presents itself: a real instrument, a real date, a full data table, a stated statistic — and a central quantity that depends on a person who cannot be blinded. It is a **claim with a protocol**, not a demonstration.

The re-test that would mean something is cheap, needs no new apparatus, and is worth naming precisely: draw θ at random **after** both scans; randomise scan order by machine; have a second person enter the text; hold the analysis key with a third; add a **sham pair** of two statements of identical meaning as the null control; and pre-register the sign prediction. If a torsion detector can read meaning, that design should survive it. Nothing in this paper says it would not — it says nothing in this paper can tell.
