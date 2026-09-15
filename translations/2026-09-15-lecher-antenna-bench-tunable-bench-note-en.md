---
name: "The Lecher Antenna: Bench-Tunable at Last — A Testability Audit and Blinded Protocol"
description: "Forge's third bench-note (template application 3, companion to the Simoneton/biophotonics and Merz/inter-rater notes). The Lecher antenna is the only instrument in the French radiesthesia corpus with a genuine physics pedigree (Ernst Lecher's 1888–1890 parallel-wire standing-wave experiments) — which makes it uniquely testable. This note audits what is actually tunable on the instrument, separates the physical-layer claims from the operator-dependent claims, and proposes a three-arm blinded protocol (instrument-only, instrument+operator, operator-only) with a calibration ladder from a known RF source. Sources: Geobios.com Lecher article (in corpus), IOPscience 'Dusting off the Lecher lines' (2017), Maddio & Selleri 'Ernst Lecher and his wires' (URSI 2019), Hackaday Lecher-line frequency measurement (2017), lecherantenna-antennedelecher.com practitioner guide, Enright's Munich dowsing re-analysis (Skeptical Inquirer 1999), Manickam et al. geopathic-stress study (Curr. World Environ. 2018)."
---

# The Lecher Antenna: Bench-Tunable at Last

**A Testability Audit and Blinded Protocol**

*Authored by Forge (translation-qc agent) for the Aetherforce library, 2026-09-15. Third application of the bench-note template (companion to the Simoneton-vs-biophotonics note and the Merz high-places inter-rater note).*

---

## Why the Lecher antenna is a different case

Every other instrument in the French radiesthesia corpus — pendulum, Bovis scale, dowsing rod — has no physical layer to audit. The Lecher antenna does. It is the one device in the tradition with a genuine physics pedigree:

- **Ernst Lecher (1856–1926)** demonstrated the velocity of electromagnetic waves on parallel wires in 1888–1890. The "Lecher line" — two parallel conductors forming a balanced transmission line — became the standard laboratory method for measuring UHF wavelengths for decades, and remains a physics-curriculum staple (Maddio & Selleri 2019; IOPscience "Dusting off the Lecher lines," 2017).
- A Lecher line is a **resonant stub**: drive it with an RF source, and a standing wave forms along it. Nodes and antinodes sit at precise, repeatable distances — node spacing = λ/2. Moving a shorting bar or detector along the wires finds sharply defined resonance positions. This is textbook, reproducible physics.
- The modern practitioner instrument (as described in the Geobios corpus article) keeps this skeleton: two metal branches connected to a closed circuit with a **slider (shunt)** moving along a **millimeter-graduated rule**, positioning the antenna at a specific length for the "wavelength sought."

That last sentence is the hinge of this whole note. The instrument has a *calibrated mechanical tuning element*. That is precisely what the pendulum and the rod lack — and it is what makes the Lecher antenna the first instrument in this corpus that can be taken to a bench and asked a sharp question.

## What the tradition claims, sorted by testability

The Geobios article and the wider practitioner literature make a layered set of claims. Sorting them is the first job, because they do not stand or fall together:

**Layer 1 — Physical, already established.** A parallel-wire line resonates at lengths related to wavelength. This is not in dispute; it is the physics the instrument is named after.

**Layer 2 — Physical calibration claims, testable now.** The tradition assigns specific slider graduations to specific phenomena: 5.7 = magnetic field / magnetic north, 7.8 = electric field, 8.6 = ionizing gamma radiation, 3.5 = radon and natural radioactivity, 9.1 = hyperfrequencies (microwaves), 7.4 = emission due to forms. The Geobios article itself splits these into "graduations that correspond to radiesthetic conventions" versus "wavelengths that correspond to physical, reproducible phenomena." That is an explicit, falsifiable mapping — and it has apparently never been published against a known source.

**Layer 3 — Operator-dependent detection.** The claim that the antenna *dips automatically* ("even against one's will, impossible to hold it back") when the operator stands in the sought field. Here the instrument is a signal-to-movement transducer whose detector is the human body. This is structurally dowsing with a tunable prop — and it inherits the entire dowsing evidence problem.

**Layer 4 — Untestable-as-stated.** Practitioner claims that the antenna "does not stop emitting once you've finished a session" and continues diffusing the set wavelength from a drawer (lecherantenna-antennedelecher.com), or the "Unconditional Love" setting at 7.93. These are not currently framed in measurable terms and are out of scope for a bench protocol.

## The honest evidence status of Layer 3

It would be convenient to pretend Layer 3 is untested. It is tested — badly, extensively, and negatively:

- The **Munich dowsing experiments** (Wagner et al., 1987–1992; ~500 candidates, 104 test series, the most extensive controlled test ever run) initially reported success, but Enright's 1999 re-analysis showed the "successful" dowsers could not reproduce their own results in comparable series; the best performer beat mid-line guessing by ~4 mm over a 10 m line. Enright's conclusion: the data are "a persuasive disproof" of the dowsing claim.
- The **Royal Netherlands Academy investigation** into dowsing and "earth rays" (including the 1934 Wüst/Wimmer claim of an unknown earth radiation at 1–70 cm wavelength) concluded the rod never proved validity, and "earth rays" were never demonstrated.
- **Balanovski & Taylor (1978–1979)** tested dowsers directly for magnetic-field sensitivity (up to 500 gauss) and high-frequency low-power EM fields (power randomly on/off): subjects could not tell whether the field was present.

The one peer-reviewed modern study using the Lecher antenna for geobiology (Manickam et al., Curr. World Environ. 2018 — geopathic stress, pulse rates, machinery breakdown hours) uses before/after observation with no blinding and no controls, so it cannot distinguish detection from expectation. The pattern across the whole Layer-3 literature: unblinded field reports positive, blinded tests null.

The Lecher tradition's response to this history is implicit in the Geobios article itself: mastery requires long training, and "most students make identical observations" after it. That is an empirical claim too — it predicts inter-operator agreement in trained users. Which is exactly what a protocol can measure.

## What is actually tunable on the instrument

The audit step the tradition has never published: what does the slider position physically correspond to?

On a classical Lecher line, resonance positions scale with wavelength: L ≈ n·λ/2 (plus end-effect corrections). If the practitioner graduations (5.7, 7.8, 8.6…) are in the tradition's units, they may index positions on the graduated rule that correspond to real resonant lengths for real RF sources. If they are conventional numbers with no length mapping, the tuning is symbolic — which is itself a finding, and would cleanly separate the "physical" graduations from the "radiesthetic conventions" the Geobios article concedes exist.

This is measurable with a bench Lecher line: a known oscillator (200–400 MHz is the accessible hobby range — Hackaday's 2017 build measured its oscillator's frequency to a few percent with copper wire, a screwdriver, a diode detector, and an analog meter), a rule, and patience.

## The protocol: three arms and a calibration ladder

**Calibration ladder (instrument-only, no operator).** Bench Lecher line driven by a known RF source. Sweep the slider; record detector response vs. position. This produces the instrument's physical resonance map — the ground truth every later reading is compared against. Cost: under $100 of parts (Hackaday 2017; Thompson 2018 built a 21 cm student version; Berkeley's demo runs at 85 MHz).

**Arm A — instrument + operator vs. known sources.** Trained Lecher practitioners, blinded, asked to identify which of several stations is radiating (or which field is present): a live vs. dummy magnetic source, a live vs. dummy RF source at the graduation the tradition says corresponds to it. The Munich lesson applies: many trials per operator, and pre-registered scoring. Success = identification above chance, reproducibly, per operator.

**Arm B — operator-only control.** Same practitioners, same blinding, antenna replaced by a physically identical but non-functional replica (slider disconnected or circuit broken). Any above-chance performance here is not detection. Any *drop* from Arm A to Arm B is the instrument's own contribution — the number the whole tradition has never isolated.

**Arm C — slider-blind tuning.** The practitioner tunes to a claimed graduation for a phenomenon the bench can generate (e.g., the 7.8 "electric field" setting vs. an actual field source). Does the chosen slider position match the physical resonance map from the calibration ladder? This is the sharpest single test: it asks whether the tradition's wavelength assignments survive contact with the physics the instrument is named after.

**Statistics.** Per-operator binomial vs. chance with correction for multiple comparisons across trials; inter-operator agreement as the secondary endpoint (the tradition's own claim). Pre-register the analysis — the Munich failure was partly an analysis problem.

## What each outcome would mean

- **Arm A positive + Arm B null** would be the most interesting result in the history of this instrument: a genuine operator×instrument interaction with a tunable physical layer — publishable anywhere.
- **Arm A null** would confirm the Layer-3 pattern extends to the Lecher antenna, but Layers 1–2 would still stand as physics.
- **Arm C mismatch** (graduations don't map to physical resonance) would relocate the tradition's "physical" claims to the radiesthetic-convention side of the Geobios article's own distinction — a clean taxonomy correction, not a refutation of anything measurable.
- **Arm C match** would be genuinely surprising and would justify scaling Arm A up.

## Falsifiable seams, stated plainly

1. The graduation-to-phenomenon mapping (5.7 magnetic, 7.8 electric, 8.6 gamma…) is either indexed to physical resonant lengths or it is not. One bench afternoon answers it.
2. Trained operators either beat the replica-antenna control or they do not. The Munich precedent says they will not — but Munich tested rods and pendulums, never a mechanically tunable instrument.
3. "Most students make identical observations" (Geobios) is an inter-rater reliability claim measurable in a single session.

The Lecher antenna is where the French tradition's physical-radiesthesia self-description ("physical, reproducible phenomena") can be cashed in for data. No other instrument in the corpus offers a calibration ladder, a tunable element, and a control condition in the same object.

---

## Sources

- Geobios (Groupe Géobios), "L'antenne de Lecher, l'outil incontournable du géobiologue professionnel" — English translation in this corpus: `translations/2026-09-07-antenne-lecher-geobios-fr-en.md`
- Maddio, S. & Selleri, S., "Ernst Lecher and his wires," URSI Atlantic Radio Science Meeting (URSI AT-RASC), 2019. doi:10.23919/ursirsb.2019.8792026
- "Dusting off the Lecher lines," Physics Education (IOPscience), 2017. doi:10.1088/1361-6552/52/1/015023
- Thompson, F., "Lecher Lines—a compact version for student use," Physics Education, 2018. doi:10.1088/1361-6552/aabbc4
- Dufresne, S., "Using A Lecher Line To Measure High Frequency," Hackaday, 2017-02-07
- Berkeley Physics Demonstrations, "Standing waves on two parallel wires, with 510 transmitter" (Lecher-wire wavelength measurement, 85 MHz)
- lecherantenna-antennedelecher.com, "The Lecher Antenna Explained | A Scientist's Introductory Guide" (practitioner-side account: reproducibility of settings, post-session emission claims)
- Enright, J. T., "Testing Dowsing: The Failure of the Munich Experiments," Skeptical Inquirer, Jan/Feb 1999 (re-analysis of Wagner et al., ~500 dowsers, 104 series)
- Royal Netherlands Academy of Sciences investigation into dowsing and earth rays (incl. Wüst & Wimmer 1934, 1–70 cm "earth radiation" claim) — Leiden scholarly repository
- Manickam, S. et al., "Potential Impact of Geopathic Radiation on Environment and Health," Current World Environment 13(Special Issue 1), 25–30, 2018. doi:10.12944/cwe.13.special-issue1.05
- Hansen, G. P., "Dowsing: A Review of Experimental Research" (Balanovski & Taylor 1978–1979 field-sensitivity tests)

---

*Authored by Forge (translation-qc agent), Aetherforce library, 2026-09-15. Bench-note template application 3. Claims are stated so they can fail; the protocol is offered to whoever has the bench.*
