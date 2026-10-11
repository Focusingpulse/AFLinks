---
name: Keppe Motor Matched-Load Efficiency Test
description: "The queue's first card whose claim is an EFFICIENCY claim on a conventional appliance, and its first whose discriminator is a matched-load comparison against a MODERN baseline. A Keppe-motor fan is certified at 28.5 W at 400 rpm where the manufacturer says ~500 conventional Brazilian ceiling fans average 130 W for the same airflow. Build the matched-airflow comparison yourself — and include a modern DC/BLDC fan, because if the Keppe fan lands in the same band, the 4.5x headline measures the age of the AC baseline, not a new energy source. Energy domain, ~$150-300, Power mirror (Electricity complement)."
---

# ⚡ Aetherforce — Power

**Guild:** Aetherforce — Power (complements Electricity)
**Quest Line:** ⚡ Aetherforce · Electricity complement
**Tier:** straw
**Domain:** energy (electric-motor efficiency — the queue's first efficiency claim on a conventional appliance, tested by matched load)
**Status:** proposed

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-09-27-keppe-motor-matched-load` · authored_at `2026-09-27` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural", "urban"],
  name: "Aetherforce — Power",
  desc: "A ceiling fan built around a 'resonant current' Keppe Motor was certified by INMETRO in Brazil at 28.5 watts at full speed. The manufacturer says the average of nearly 500 conventional Brazilian ceiling fans was 130 watts for the same airflow — a 4.5x difference, and the number the whole claim rests on. But those are two different kinds of number: one is a measurement of a single product, the other is a population average. Nobody has put the two fans in the same room at the same airflow. That is the experiment. Measure watts and airflow for three fans — the Keppe one, an ordinary AC one, and a modern DC one — then throttle the stronger fan down until the airflows match and read the watts there. The modern DC fan is the arm that decides it: brushless ceiling fans already draw 15-40 watts, so if the Keppe fan lands in that same band, the headline is measuring how old the baseline is, not a new energy source. Either way you will have measured something real about a claim nobody has checked. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "straw",
  quest: [
    "Keppe Motor Matched-Load Efficiency Test",
    "Pick a fixed measurement plane below the fan (record the distance) and a 3x3 grid across the downwash. For each of three fans — a Keppe-motor fan, a conventional AC ceiling fan, and a modern DC/BLDC ceiling fan — measure air velocity at all 9 points and the electrical watts with a TRUE-RMS plug-in power meter. First record each fan at full speed, then throttle the higher-airflow fan down until its airflow MATCHES the lower-airflow fan's, and read the watts at that matched point. Repeat on at least 3 separate days, logging room temperature and mains voltage each time. Measurable outcome: matched-airflow watts for each fan, and the Keppe fan's ratio against the conventional AC fan and against the modern DC fan. PASS: Keppe fan at <= 1/3 the AC fan's watts AND <= 50% of the modern DC fan's watts at matched airflow, in >= 2 of 3 sessions. FAIL: within +/-20% of the modern DC fan, or >= 50% of the conventional AC fan — the headline ratio is a baseline artifact, a complete result (Skeptic's Star). VOID: no Keppe motor obtainable — say so, do not substitute a different motor. ARTIFACT: the Keppe fan's lower watts track its lower airflow, or the gap vanishes at the same regulated voltage. Never open a powered fan; use the meter between the wall socket and the fan's own plug.",
    ["Science", "Engineering", "Measurement", "Energy"],
    "🔌"
  ],
  source_doc: "sources/2026-09-02-scout-b-multi-1.md#spanish-finds-entry-1 (scout find: 'Keppe Motor — Scalar Energy Resonance Motor'; practical_applicability buildable — 'INMETRO certified, 28.5W ceiling fan vs 130W conventional'; database work id keppe-motor-resonant)",
  source_url: "https://www.keppemotor.com/institucional/o-que-e-o-keppe-motor/",
  dossier: "living-library/synthesis/replication/2026-09-27-dossier-047-keppe-motor-matched-load.md",
  pass_fail: "PASS: the Keppe-motor fan delivers matched airflow at <= 1/3 of the conventional AC fan's watts AND <= 50% of the modern DC/BLDC fan's watts at matched airflow, reproduced in >= 2 of 3 sessions - the efficiency claim survives a matched-load test and is not explained by an obsolete control. FAIL: matched-airflow watts within +/-20% of the modern DC fan, or >= 50% of the conventional AC fan - the headline ratio is explained by the AC baseline being obsolete technology rather than a novel energy source; a complete result (Skeptic's Star). INCONCLUSIVE: airflow matching not achieved; fewer than 3 sessions; the power meter was not true-RMS; a bare motor was run without a fixed blade set. VOID: no Keppe motor could be obtained (the card cannot be run - do not substitute a different motor); the fan's speed or blades were altered internally; blade sets changed between sessions; the protocol was changed after the first session. ARTIFACT: the Keppe fan's lower watts track its lower airflow; the gap disappears at the same regulated voltage; the difference tracks room temperature; the airflow grid was moved between fans.",
  evidence: "Photo of each fan with its blade diameter + the marked measurement grid and its distance below the blades + the pre-registration sheet (distance, grid, thresholds, scoring rule, meter model) + the full log of watts and 9 velocity readings for every fan, speed and session + the matched-airflow calculation + the room-temperature and mains-voltage log + a photo of the power meter at the matched point for each fan + the Keppe fan's nameplate or certification marking if present + the void/artifact checks reported whether or not they void the run"
}
```

---

## Source Documentation

- **Primary (the archive find):** `living-library/sources/2026-09-02-scout-b-multi-1.md`, **§ Spanish Finds, entry 1** — *"Keppe Motor — Scalar Energy Resonance Motor (Spanish/Portuguese)"*, https://www.keppemotor.com/institucional/o-que-e-o-keppe-motor/ — Portuguese (Brazilian)/Spanish, Brazil (São Paulo), work type prototype/experimental. Scout flag: `Practical Applicability: Buildable (motor prototypes built, INMETRO certified, 28.5W ceiling fan vs 130W conventional)`; `Verification: INMETRO certified product; independent scientific validation not presented`.
- **Database mirror:** `living-library/database/research/research-index.json` → work id **`keppe-motor-resonant`** (*Motor Keppe: Tecnologia de Motores Ressonantes da Nova Física Desinvertida*), mirrored in `database/research/practical-applications.json` with `fields: [buildable, verified]`.
- **The claim in the source's own terms** (manufacturer's page, fetched 2026-09-27): a ceiling fan carrying a Keppe Motor was produced industrially in China in 2015; **INMETRO certified it in Brazil at 28.5 W consumption at maximum speed (400 rpm)**; the **average of nearly 500 conventional Brazilian ceiling-fan models was 130 W for the same airflow**; savings of *"up to 90%"* relative to equivalent motors. The motor is described as an **RC (*Corrente Ressonante*) motor** — neither AC nor DC — operating by electromechanical resonance and capturing what Tesla called scalar energy and Keppe calls **Essential Scalar Energy (E.E.E.)**.
- **The counter-context the card supplies itself:** modern **DC / brushless (BLDC)** ceiling fans already draw roughly **15–40 W**. The archive holds **no independent replication and no refutation** of the Keppe claim — a grep for "keppe" across `living-library/` returns only this scout find, the two database records, and `research-queue/corpus-docs.json`. That absence is why the card exists.
- **Replication Dossier:** `living-library/synthesis/replication/2026-09-27-dossier-047-keppe-motor-matched-load.md`
- **Vault:** https://focusingpulse.github.io/AFLinks — search "Keppe", "resonant motor", "scalar energy", "Tesla radiant"
- **Aetherforce Reference:** Search "Tesla", "scalar", or "resonant motor" on https://www.aetherforce.energy
- **Related cards:** 003 (Tesla Radiant Receiver — the queue's other Tesla-lineage energy card), 018 (Bladeless Tesla Turbine — static-to-electrical conversion), 041 (Spin-Weight Anomaly Test — the queue's other card whose source claim is already refuted), 024 (Spiral-Pipe Friction Test — the queue's other card that re-runs a *foundation* claim rather than a device claim)

---

## Rubric Justification

| Criterion | Assessment |
|-----------|------------|
| **Practical** | YES — Named apparatus (three fans, a true-RMS plug-in power meter, an anemometer, a fixed measurement grid) with a named procedure (full-speed reading → throttle the stronger fan to matched airflow → read watts there → repeat over ≥3 sessions) and a measurable outcome (**matched-airflow watts for each fan, and the Keppe fan's ratio against the conventional AC fan and against a modern DC fan**). Not pure theory. |
| **Replicable** | YES — Home, straw: **~$150–300** (Keppe motor/fan — the main risk; power meter ~$20; anemometer ~$25; the two comparison fans may already be on hand). No chemicals, no heat, no high voltage beyond ordinary household mains. The demanding requirement is **discipline** (true-RMS meter, matched airflow rather than matched rpm, the same room back-to-back). |
| **Relevant** | YES — Energy domain, squarely: a claim about how much electrical input a familiar appliance needs. It is also the queue's **first card whose claim is an efficiency claim rather than a novel energy source**, and its **first whose control is today's ordinary technology** rather than a shielded arm or a baseline scatter. |
| **Honest** | YES — the claim is framed as a claim and the card is a test, not an endorsement. Three things are stated in advance: the headline ratio compares **a certified measurement of one product against a population average of ~500 models**; a **conformity certificate is not an efficiency certificate**; and **the baseline may be obsolete AC technology**, which is why a modern DC fan is a *required* arm. The FAIL path is a complete result and a finding about the archive's own claim. Explicit VOID if the motor cannot be obtained, with an instruction **not** to substitute a different motor. |
| **Linked** | YES — a scout find, the primary manufacturer page, the database work id, a pre-registered replication dossier, and cross-links to four related cards. |

**Mirror choice, stated:** the card's lineage is explicitly **Tesla's scalar energy** — the manufacturer names it — and the device is an electric motor, so **Electricity** ("Radiant / Tesla / LMD") is the honest complement, and the family label is `Aetherforce — Power`, the label every energy-domain card in this queue carries. **Homesteading** ("Self-reliance / off-grid") was the closest alternative and was considered seriously, because the manufacturer pitches the motor for off-grid solar pumping and refrigeration without inverters; it was not chosen because the card tests the *efficiency claim* on an ordinary grid-connected appliance, not an off-grid system, and because the claim's own framing is Tesla-lineage. **Rocket** and **Oddball** were rejected: the card is not a novel-source claim and not a cross-field bridge.

---

## The honest framing (the spine of the card)

**The number everyone quotes is a ratio between two different kinds of number.** 28.5 W is a certified measurement of *one product at its maximum speed*. 130 W is the manufacturer's stated *average across nearly 500 conventional models*. Neither is wrong; they are simply not about the same thing, and no one has put the two in the same room at the same airflow. That is the whole experiment, and it is why the card is worth running: it converts a marketing comparison into a measurement.

**A certificate is a measurement of one thing; the claim is about a relation between two things.** INMETRO is Brazil's national metrology and standards institute, and the certificate records the product's own measured consumption. It does not certify the comparison, and it is not an efficiency rating against any other fan. This is the same shape of error the fleet keeps finding: *the instrument is not lying — it is answering the question it was built around, and that was a different question.*

**The modern DC fan is the arm that decides it.** Brushless ceiling fans already draw roughly 15–40 W. If the Keppe fan lands in that band at matched airflow, the 4.5× headline is measuring **how old the AC baseline is**, not a new energy source. If it lands *below* that band at matched airflow, the family has measured something genuinely interesting and the claim deserves a second, harder look. Either outcome is a real result; only one of them is the outcome the marketing implies.

**Airflow is a proxy, and the card says so.** A fan moving the same air with a different blade design is not doing the same work. The card compares **fans**, not motors in isolation, and states that plainly rather than dressing an airflow comparison up as a motor efficiency figure.

**Under-promise:** the card's most likely outcome is FAIL — the modern DC fan will probably absorb most of the headline gap. That is not a wasted run: it would be the first independent check of a claim the archive holds on the manufacturer's word alone, and it would file a real finding about the library's own holdings.

**Hard condition carried into the card:** the claim cannot be tested without a Keppe motor, and the card **explicitly forbids substituting a different motor**. If none can be obtained, the run is VOID and the card says so — a card that quietly swaps in an unrelated fan would be a fabricated result, not a replication.
