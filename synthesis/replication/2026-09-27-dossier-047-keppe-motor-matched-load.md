---
name: Dossier 047 — Keppe Motor Matched-Load Efficiency Test
description: "Replication dossier for the Keppe Motor claim: a resonant-current (RC) motor fan consumes 28.5 W at 400 rpm where the average of ~500 conventional Brazilian ceiling fans consumes 130 W for the same airflow. Home-replicable, ~$150-300. The queue's first card whose claim is an EFFICIENCY claim on a conventional appliance rather than a novel energy source, and its first whose discriminator is a matched-load comparison against a modern baseline."
---

# Dossier 047 — The Keppe Motor Matched-Load Efficiency Test

**Status:** protocol
**Domain:** energy (electric-motor efficiency — the queue's first efficiency claim on a conventional appliance)
**Tier:** straw (home-scale, ~$150–300)
**Created:** 2026-09-27
**Source docs:**
- `living-library/sources/2026-09-02-scout-b-multi-1.md` — **§ Spanish Finds, entry 1**: *"Keppe Motor — Scalar Energy Resonance Motor (Spanish/Portuguese)"*, https://www.keppemotor.com/institucional/o-que-e-o-keppe-motor/ — Portuguese (Brazilian)/Spanish, Brazil (São Paulo), work type prototype/experimental. Scout flag: `Practical Applicability: Buildable (motor prototypes built, INMETRO certified, 28.5W ceiling fan vs 130W conventional)`; `Verification: INMETRO certified product; independent scientific validation not presented`.
- `living-library/database/research/research-index.json` → work id **`keppe-motor-resonant`** (*Motor Keppe: Tecnologia de Motores Ressonantes da Nova Física Desinvertida*), mirrored in `database/research/practical-applications.json` with `fields: [buildable, verified]`.
- **Primary source, fetched 2026-09-27** (the manufacturer's own page, same URL): *"Um ventilador de teto embarcando Keppe Motor foi produzido industrialmente na China em 2015. O INMETRO certificou este produto no Brasil com 28,5W de consumo na máxima velocidade (400rpm). A média dos quase 500 modelos de ventiladores de teto convencionais utilizados no Brasil era de 130W para o mesmo fluxo de ar."* The same page claims savings of *"até 90% de economia de energia em relação aos motores equivalentes"* and pitches the motor for off-grid solar pumping/refrigeration without inverters.

---

## The claim (as asserted by the source)

That the **Keppe Motor** — a "resonant current" (RC, *Corrente Ressonante*) motor, distinguished by its inventors from both AC and DC motors — operates by **electromechanical resonance** and thereby "captures part of the energy Nikola Tesla called scalar energy, and Keppe calls Essential Scalar Energy (E.E.E.)". The concrete, numeric form of the claim:

- A ceiling fan built around a Keppe Motor, **industrially produced in China in 2015**, was **certified by INMETRO in Brazil at 28.5 W consumption at maximum speed (400 rpm)**.
- The **average of nearly 500 conventional ceiling-fan models used in Brazil was 130 W for the same airflow**.
- Up to **90 % savings** "relative to equivalent motors."

**What is being tested, in one sentence:** does a Keppe-motor fan deliver **the same airflow** as a conventional ceiling fan while consuming **substantially less electrical power** — and does it also beat a **modern DC/BLDC** ceiling fan, or is the headline ratio simply a comparison against obsolete AC technology?

## Honest status of the claim

**The archive holds the claim and no independent test of it.** A grep for "keppe" across `living-library/` returns only the scout find, the two database records, and `research-queue/corpus-docs.json` — there is **no replication, no refutation, and no independent measurement** in the library. That absence is the reason this card exists.

Three things the card must say out loud, because they are what a family is actually testing:

1. **The headline ratio is a comparison against a population average, not a matched measurement.** 28.5 W is a *certified measurement of one product*. 130 W is the manufacturer's stated *average across ~500 conventional models*. Those are two different kinds of number. A ratio built from them is a marketing comparison until someone measures both fans at the same airflow — which is precisely what this card does.
2. **A conformity certificate is not an efficiency certificate.** INMETRO is Brazil's national metrology/standards institute; the certificate records the product's own measured consumption at its maximum speed. It does not certify the comparison, and it does not certify the motor against any other product. **A certificate is a measurement of one thing; the claim is about a relation between two things.**
3. **The baseline may be obsolete technology rather than a novel energy source.** Modern **DC / brushless (BLDC)** ceiling fans already draw roughly 15–40 W. If a Keppe-motor fan lands in that same band at matched airflow, then the 4.5× headline measures **the age of the AC baseline**, not a new energy source. This is the single most informative arm of the test and it is why a modern DC fan is a required comparison, not an optional one.

**Not tested by this card:** the theoretical claim (resonant current drawing "essential scalar energy" from the vacuum) and the STEM motor-generator claim. Both are deferred to the instrument tier.

**Under-promise, stated plainly:** this card can establish, for one household, **whether the efficiency claim survives a matched-load comparison against a modern fan**. A FAIL is a complete and valuable result — it would say the headline number is a baseline artifact, which is a finding about the archive's own holdings, not merely about one product.

## Why it matters

- It is the queue's **first card whose claim is an efficiency claim on a conventional appliance** — every prior energy card (Tesla radiant receiver, vortex jet turbine, bladeless Tesla turbine, spiral-pipe friction, Chiappini antenna, sealed-box electrostatic thrust, spin-weight anomaly) tests a claim about a **novel energy source**. This one tests a claim about **how much input a familiar device needs**.
- It is the queue's **first card whose discriminator is a matched-load comparison against a modern baseline** — the control is not a shielded arm or a baseline scatter, it is *today's ordinary technology*.
- It teaches the transferable lesson the whole library keeps relearning: **a ratio between two numbers is only as good as the two numbers being about the same thing.** The measurement's object must match the claim's object.
- It links a **commercially produced, standards-certified product** to the archive's Tesla/scalar-energy lineage — the first card in the queue built on a product that a family can simply buy.

## Replicability: `home`

- Build/obtain cost: **~$150–300** — a Keppe-motor fan or motor unit (availability is the card's main risk; see VOID), a plug-in power meter (~$20, **true-RMS required**), an anemometer (~$25), a tape measure. A conventional AC ceiling fan and a modern DC/BLDC ceiling fan may already be on hand.
- Safety: **mains electricity at the fan.** Wire nothing yourself; use a plug-in meter between the wall socket and the fan's own plug. No chemicals, no heat, no high voltage beyond ordinary household mains. Do not open the fan housing while powered.
- Accessibility: an afternoon, three sessions on different days.

## Apparatus (Bill of Materials)

- **Keppe-motor fan (the claim under test)** — a ceiling fan or fan unit carrying a Keppe Motor. If only a bare motor is obtainable, it must be run with a **fixed, recorded blade set**; a bare motor with no load cannot be compared to a fan.
- **Conventional AC ceiling fan (the claim's own baseline)** — an ordinary single-phase induction ceiling fan of comparable blade diameter.
- **Modern DC / BLDC ceiling fan (the modern baseline — required)** — the arm that decides whether the claim is a novel source or an obsolete baseline.
- **Plug-in power meter** — **true-RMS**, reading **watts** (not just VA). A non-true-RMS meter misreads induction-motor loads badly and would corrupt the whole comparison. Record the model.
- **Anemometer** — vane or hot-wire, to measure air velocity at defined points.
- **Tape measure + a marked measurement plane** — a fixed grid of points (e.g. a 3×3 grid across the fan's downwash at a fixed distance below the blades).
- **Thermometer + a note of mains voltage** — for the confound log.
- **Log sheet** — pre-registered columns: date, time, fan, blade diameter, speed setting, watts, the 9 velocity readings, mean velocity, computed airflow, room temperature, mains voltage.

## Protocol (matched-load, three arms, pre-registered)

**Phase 1 — build the airflow measurement (one session).**
1. Choose a measurement plane at a fixed distance below the fan (record the distance). Mark a 3×3 grid. Measure air velocity at all 9 points at the fan's maximum speed, three times, and compute the mean. **Record the method and the distance** — airflow numbers are meaningless without them.
2. State plainly in the log that **airflow is a proxy for mechanical output**, not a torque measurement: a fan's electrical-to-airflow ratio also depends on blade design. The card compares fans, not motors in isolation, and says so.

**Phase 2 — the three arms (≥3 sessions on different days).**
3. For each fan, measure **watts and airflow at maximum speed**. Then **throttle the higher-airflow fan down until its airflow matches the lower-airflow fan's**, and record its watts at that matched point. *(Throttle the stronger fan down to the weaker fan — never the reverse.)*
4. Record the **matched-airflow watts** for all three fans. This is the comparison the claim actually requires.
5. Repeat on **at least 3 separate days** at different times, and log room temperature and mains voltage each time.

**Phase 3 — score.**
6. Compare the Keppe fan's matched-airflow watts against **(a)** the conventional AC fan's and **(b)** the modern DC fan's. The modern-DC comparison is the decisive one.

## Pass / fail (pre-registered)

- **PASS:** the Keppe-motor fan delivers matched airflow at **≤ 1/3** of the conventional AC fan's watts **AND ≤ 50 %** of the modern DC/BLDC fan's watts at matched airflow, reproduced in **≥ 2 of 3 sessions** — the efficiency claim survives a matched-load test against a modern baseline and is not explained by an obsolete control.
- **FAIL:** the Keppe-motor fan's matched-airflow watts are **within ±20 % of the modern DC fan's**, or **≥ 50 % of the conventional AC fan's** — the headline ratio is explained by the AC baseline being obsolete technology, not by a novel energy source. **A complete result** (Skeptic's Star), and a finding about the archive's own claim.
- **INCONCLUSIVE:** airflow matching was not achieved (fan diameters differ too much for the flows to overlap); fewer than 3 sessions; the power meter was not true-RMS; a bare motor was run without a fixed blade set.
- **VOID:** **no Keppe motor could be obtained** — the card cannot be run, and says so rather than substituting a different motor; the fan's speed or blades were altered internally; the same fan was measured on different blade sets between sessions; the protocol was changed after the first session.
- **ARTIFACT:** the Keppe fan's lower watts track its **lower airflow** (it simply moves less air — check the matched point, not the max-speed point); the difference disappears when both fans are run from the **same regulated voltage**; the difference tracks **room temperature** (BLDC and induction motors both drift); the airflow grid was moved between fans.

## Evidence

Photo of each fan with its blade diameter and of the marked measurement grid + the **pre-registration sheet** (measurement distance, grid, thresholds, scoring rule, meter model) + the full log of watts and the 9 velocity readings for every fan, every speed, every session + the matched-airflow calculation + the room-temperature and mains-voltage log + a photo of the power meter reading at the matched point for each fan + the Keppe fan's certification/nameplate if it carries one + the void/artifact checks reported whether or not they void the run.

## Confounds (named in advance)

- **Airflow is not mechanical power.** A fan moving the same air with a different blade design is not doing the same work. State the proxy; do not present airflow as efficiency.
- **Blade diameter and speed.** A small fan at high rpm and a large fan at low rpm can match airflow with very different watts. Record diameter and speed; match airflow, not rpm.
- **Meter quality.** A non-true-RMS meter misreads induction-motor loads. Require true-RMS and record the model; a bad meter here is not a small error.
- **Mains voltage.** Motor power tracks voltage. Log it; if it varies more than a few percent between sessions, treat the comparison as confounded.
- **Temperature.** Both motor types drift with ambient and with winding temperature. Run the three fans in the same session, back to back, in the same room.
- **The baseline's provenance.** The 130 W figure is an average across ~500 models, not a measurement of the family's own conventional fan. **Measure your own conventional fan** — that is the point.

## Verdict rules

≥2 of 3 sessions showing the Keppe fan at ≤1/3 the AC fan's watts **and** ≤50 % of the modern DC fan's watts at matched airflow → **supports**. Within ±20 % of the modern DC fan → **refutes at home scale** (the headline ratio is a baseline artifact). Mixed or unmatched → **inconclusive**. No Keppe motor obtainable → **void, stated as such**.
