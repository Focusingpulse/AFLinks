---
name: Dossier 062 — Blinded Manual Muscle Testing (Applied Kinesiology) Reliability
description: "Home-scale test of the applied-kinesiology diagnostic claim: that a manual muscle test weakens under a substance the subject is sensitive to, so a trained tester's hand reads physiology. Protocol blinds the tester to a concealed key and forbids mid-run exclusions. Two-person, ~$0, one afternoon. The claim's own literature reports ~90% open-label concordance and 35% (below chance) blinded — the design difference is the claim."
---

# Dossier 062 — Blinded Manual Muscle Testing (Applied Kinesiology) Reliability

**Status:** protocol ready
**Domain:** biofield (operator-channel diagnostics — manual muscle testing)
**Tier:** straw (home-scale, two people, ~$0)
**Source:** forge/ACTIVITY.md 2026-10-02 20:20Z (QC dossier FAL-es-263-1, ES→EN)
**Created:** 2026-10-03

---

## Source lineage

- **George Goodheart (1918–2008)** — chiropractor; founded Applied Kinesiology (1964): the manual muscle test as a diagnostic channel for organ/organ-system function via neurolymphatic and neurovascular reflexes.
- **Schmitt (1998)** — open-label study correlating AK muscle testing against serum immunoglobulin levels for food allergies: **~90.5% concordance** (corpus QC: "open-label with KA-mediated subject selection").
- **Staehle (2005)** — double-blind test-retest of muscle testing: **35%, below chance**, with **28% of the sample excluded pre-test by an adaptive rule**.
- **AQuAS / RedETS (2024)** — Catalan state health-technology assessment: 9-database search, **no systematic review or RCT of diagnostic accuracy**, signed conclusion **"no existe evidencia confiable."** (Companion UETS-Madrid 2024 Seitai HTA reaches the harsher construct-level verdict.)
- **Claim under test:** that a muscle holds or gives way as a function of a substance the subject is sensitive to, read by a practitioner's hand — i.e. that the operator is a valid measurement instrument.

## Device-family watchlist (biofield / operator-channel rotation, lowest-cost tier)

- Blinded manual muscle testing (this dossier — ~$0).
- Damanhur "selfica" devices, blind-operator HRV session (validation `2026-10-03-damanhur-selfica-measurement-campaigns.md`).
- UAH rheotome biomagnetic-pair test (validation `2026-09-24-biomagnetic-pair-uah-2016-rheotome-placebo.md`).

## Status

`protocol` (draft; no documented home attempts yet — the two cited studies are laboratory/institutional, not home)

## The claim (as asserted by the source)

That **manual muscle testing is a valid diagnostic channel**: a limb tested against a practitioner's controlled pressure **weakens** when the subject is exposed to a substance to which they are sensitive (allergen, food, toxin), and holds otherwise. On the strong form, the practitioner's hand recovers physiological information that laboratory testing otherwise requires bloodwork to obtain.

**Honest framing:** the two published results **diverge by design**. The open-label study found ~90%; the blinded study found below chance. That divergence is not scientific noise to be averaged — it is the diagnostic itself, because in both cases the one variable that changed was whether the tester knew the answer. We hold no brief — the test is the point.

## Why it matters

This is the operator-channel family's **diagnostic** claim — not a device, not a distant effect, but "a trained person's hand is an instrument." It is the cheapest possible test of the family's central question: **does the operator need to know the answer?** If a blinded tester still reads the concealed sample above chance, that is a result no physical theory currently accommodates and the strongest single home datum in the family. If the blinded tester lands at chance, the claim's own founding result (the open-label 90%) is revealed as a property of the open design. Either outcome is decisive, and unlike almost every other card in this Yard, it needs **no apparatus at all**.

## Replicability: `home`

- Build cost: **~$0** (two people; optionally a few test substances and a divider).
- Safety: low (no electricity, no chemicals beyond ordinary foods/odours; if using known allergens, use sealed containers only — **do not open a food to which anyone present is actually allergic**).
- Accessibility: any two people; requires the willingness to follow a concealment protocol and score honestly.

## Apparatus (Bill of Materials)

### Core

1. **Two people:** an **Operator** (does the muscle testing) and a **Handler** (prepares the concealed key and records the results). A third person may score, but is not required.
2. **Test substances:** 6–10 small identical sealed containers. Use strong, distinct, *safe* aromatics (e.g. peppermint, vanilla, coffee, a metal coin, an empty control) rather than real allergens. At least **two containers must be inert** (empty or water) so the key is not trivially "all are active."
3. **A concealed key:** a written list, sealed in an envelope, mapping container ID → contents. The **Operator may not see it** until the session ends.
4. **A divider or screen** (optional) so the Handler can present the container without revealing which one it is.

### Records

1. Paper scoring sheet: trial number, container ID, Operator's call (strong / weak), pre-registered hypothesis for that ID.
2. A calculator (or phone) for the binomial check at the end.

### Safety

- Sealed containers only; no opened allergen.
- Stop if anyone becomes uncomfortable; this is a zero-stakes reliability test, not a diagnosis.

## Protocol (single blinded block)

### Setup

1. **Fix the outcome in advance.** Define exactly one binary observable: **the Operator calls each presented container as "active" or "inert"** based solely on the muscle response. Nothing else counts.
2. **Choose the substance set and the active/inert mix BEFORE any trial.** Write the key. **Commit to the sample size before starting: 30 trials minimum** (each container presented multiple times in randomised order).
3. The Handler shuffles container order with a randomiser; the Operator cannot see the key or the container contents.

### Procedure

For each trial:
1. Handler presents one sealed container (behind the divider if used) — **without saying anything about it.**
2. Subject holds or is exposed to the container in the standard AK manner; Operator performs the muscle test and **calls "active" or "inert."**
3. Handler records the call against the hidden key.
4. **No exclusions.** If the Operator is unsure, the call still stands — the unsure calls are data. **A trial may not be dropped after the fact.**
5. Repeat until the pre-registered N is reached. Do **not** stop early on a good or bad streak.

### Controls (the whole point of the card)

- **Blinding:** the Operator never sees the key, never learns correctness mid-session, and receives no feedback that could let them infer the key from the Handler's behaviour. This is what the 2005 study did and the 1998 study did not.
- **Non-adaptive exclusion:** the corpus records that the 2005 study dropped 28% of its sample pre-test under an adaptive rule. **This protocol forbids that**, and the report must state how many trials were scored vs. discarded (target: 0 discarded).
- **Inert arm:** at least two inert containers are present every block, so "always call active" cannot score.
- **Order randomisation** per block, to cancel any drift in the Operator's technique across the session.

## Pass / fail criteria (pre-registered)

**PASS (supports claim):**
- Operator's correct calls are **significantly above chance** (e.g. ≥20/30 with the inert arm preventing a constant guess; report the binomial p and the confidence interval).
- AND the result holds **within the blinded block** (it is a blinded result by construction).
- AND 0 trials were discarded.

**FAIL (refutes the operator-channel reading):**
- Correct calls are **at or below chance** (≈50% with a balanced active/inert mix).
- OR the result depends on retaining/dropping specific trials after seeing the key.

**INCONCLUSIVE:**
- The Operator cannot reliably produce a distinct strong/weak response at all (technique issue, test substance too weak).
- Contamination: the Operator infers the key from the containers (smell, weight, sound) — check by re-running with a blind Handler-to-Operator audio barrier and identical, odour-masked containers.

## Feedback loop

- Log every block (including nulls) here.
- ≥2 independent two-person attempts → verdict; cross-link to the biofield rail and the AK validation `2026-10-03-applied-kinesiology-mmt-schmitt-staehle.md`.
- Share: the Replication Yard; relevant AK/skeptic forums **both** — the design is neutral on purpose, so it is publishable by either side.

## Attempted-by / results log

- *(none yet — open for the first replicator. This is a ~$0, one-afternoon test and it needs no equipment.)*

---

## Source Documents

- `forge/ACTIVITY.md` 2026-10-02 20:20Z — translation-QC dossier **FAL-es-263-1** (ES→EN), the two Spanish state HTAs on life-force techniques; names AQuAS/RedETS 2024, UETS-Madrid 2024, Schmitt 1998, Staehle 2005; primary PDFs "fetched in full from conprueba.es"; cheapest unrun named: *"a blinded MMT reliability replication with non-adaptive exclusions — 30 years stale."*
- Prior in this Yard: `synthesis/validations/2026-10-03-applied-kinesiology-mmt-schmitt-staehle.md`; `synthesis/validations/2026-09-24-biomagnetic-pair-uah-2016-rheotome-placebo.md`.
- Primaries (cited, not read from this sandbox): Schmitt (1998); Staehle (2005); AQuAS/RedETS (2024); UETS-Madrid (2024).

## Related Quests

- *(no quest card yet — this dossier is the protocol; if no home attempt is logged after the next few seeder runs, open a quest card at `synthesis/quest-queue/` so the rail has a demand-side entry.)*
- Adjacent: Damanhur selfica blind-operator session (same family, same "does the operator need to know" question).

## Notes

This dossier tests the **operator-channel claim at its most favourable and cheapest site** — a trained hand on a live subject, no apparatus. It deliberately does **not** test whether the practitioner can *help* a subject; it tests whether the muscle response carries information the tester did not already supply. A negative here is the cleanest possible statement of the family's recurring result; a positive is the strongest possible home datum, and it would need its own follow-up (repeat with independent pairs, odour-masked containers, and a pre-registered key). Log it honestly either way.
