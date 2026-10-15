---
name: Quest Card — Does a Passive Device Cut Your Freezer's Power Bill? The Cold-Storage Energy Test
description: "Aetherforce-branded quest card testing the one applied, quantitative claim in the torsion-field literature that is measurable in a kitchen: that a passive, unpowered torsion-wave polarizer installed in a refrigeration device cut average drive power consumption by 13.5% and shortened the cooling and freezing time of a 20 dm3 bucket of water by about 37%, while changing the structure of the frost and the ice. The card carries the source's own null (the internal coefficient of performance stayed at ~2.5 regardless of the polarizers) and its own admitted hole (the thermal load was never determined and the ambient temperature 'was not regulated') as the design's primary controls, adds the matched inert control and the blinding the source lacked, and states plainly that the source's device is proprietary so the card tests the CLASS claim, not the product. Source: Henryk Pacocha (P.P.H.U. TORST) & Waldemar Targanski (Gdansk University of Technology, Department of Thermal Engineering), 'Zagadkowe fale torsyjne a oszczednosci w chlodnictwie', Technika Chlodnicza i Klimatyzacja 2006 no. 9 (pl->EN 4 chunks, complete). Food domain (cold storage — keeping food cold on the least energy); Food Prep mirror (food-preservation complement), 4th card."
---

# ⚡ Aetherforce — Food Prep

**Guild:** Aetherforce — Food Prep
**Quest Line:** ⚡ Aetherforce · Food Prep complement
**Tier:** sand
**Domain:** food (cold storage — keeping food cold on the least energy)
**Status:** proposed
**Created:** 2026-10-15

**Source:** Aetherforce Knowledge Vault — [focusingpulse.github.io/AFLinks](https://focusingpulse.github.io/AFLinks) · on Aetherforce: search "torsion field" / "Schauberger" / "water structure" — [aetherforce.energy](https://www.aetherforce.energy)

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-10-15-cold-storage-energy` · authored_at `2026-10-15` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Read this first — what this card can and cannot test

The source's device is **proprietary**. P.P.H.U. TORST publishes no dimensions, materials or schematic for its HPT® polarizers and says the *"type and manner of use of this technology is developed individually."* **This card therefore cannot test the HPT® product, and does not claim to.** It tests the **class claim the source itself makes** — that a passive, unpowered device placed in a refrigeration appliance changes the appliance's energy use and the freezing behaviour of water. A null here refutes the class; it does not by itself refute the specific product. That asymmetry is written into the pass/fail and is not hidden.

**Safety.** A household freezer and a plug-in energy meter are ordinary appliances. Do not defeat a thermostat, do not bypass a door switch, do not run a freezer with the door blocked open, and do not put anything into a freezer that is not food-safe. If the freezer is the household's only one, run the card in a season when its contents can be kept elsewhere — **do not risk the food to run a test.**

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural", "urban"],
  name: "Aetherforce — Food Prep",
  desc: "A Polish refrigeration journal published a study from the Department of Thermal Engineering at Gdańsk University of Technology: a passive, unpowered device — no battery, no wire to the wall — was installed inside a refrigeration chamber, and the compressor's average drive power dropped by 13.5%. In a second experiment, the same kind of device was put in a working cold store and a 20-litre bucket of water froze about 37% faster. The paper is twenty years old and nobody has ever reproduced it. Here is the part that makes it a real experiment rather than a sales sheet: the same paper reports that the machine's own efficiency did not change at all — the internal coefficient of performance sat at about 2.5 with the device and without it — and the authors admit they never measured the chamber's thermal load and that the room temperature 'was not regulated'. A 13.5% saving with no change in efficiency has to come from somewhere, and the likeliest somewhere is the room. So you will measure the room. You will run your own freezer for sixteen days, alternating a passive device against a matched inert object of the same mass and the same metal, with the swap done by someone who does not tell you which arm is running, and you will normalise every day's kilowatt-hours to that day's logged room temperature. If the device arm really uses less energy at the same room temperature, you will have found the first independent confirmation of any part of this claim. If the two arms land on top of each other, you will have measured a null on your own bench and retired the whole family of 'put a passive object in your appliance' claims. Both are worth having, and the second is what the evidence predicts. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "sand",
  quest: [
    "Does a Passive Device Cut Your Freezer's Power Bill? — The Cold-Storage Energy Test",
    "Build the device: 30 turns of 1.5 mm² insulated copper wire wound into a 15 cm coil, taped to the inside wall of your freezer. Build the control: the SAME LENGTH of the SAME WIRE, unwound into a straight bundle, of the SAME MASS — weigh both on a kitchen scale and record the grams. Plug a cumulative-kWh energy meter into the freezer's socket, and put a thermometer or data logger in the room (not in the freezer). FIRST prove the freezer is quiet enough to test: run two 24-hour days with NO device at all and compare the two kWh figures. If two identical days differ by more than the effect you are chasing, STOP — the honest result is 'this freezer is too noisy for this card', and that is a result. Then fix everything that moves the number: same thermostat setting, same weighed contents, same door-opening rule (log every opening), fully defrosted before day 1 and no defrost during the run. Run EIGHT 24-hour periods alternating device and matched control (A-B-A-B-A-B-A-B), with a second person swapping the device without telling you which arm is running, recording the arm on a sealed sheet. Each period log: cumulative kWh, mean room temperature, door-opening count, and the fraction of the day the compressor was audibly running. Each period also freeze one identical 1-litre bottle of water from +15 °C to 0 °C in the same position and time it, and photograph the evaporator frost and the ice in the condensate tray. Repeat the whole 8-period set in a second week, re-randomising the order. Measurable outcome: kWh per 24 h NORMALISED to the logged mean room temperature (regress each period's kWh on its ambient and compare the arms at a common ambient), plus the 1-litre freezing time per arm. PASS: the device arm's normalised kWh is at least 10% lower than the matched control's in BOTH weeks with the blinding held and the instrument check passed — the first independent confirmation of any part of this claim. PASS (the expected, ordinary result): the two arms agree within the meter's resolution and the between-day scatter in both weeks — a passive object of this kind does nothing measurable to a freezer, and the source's 13.5% was the unregulated room temperature and the frost state, not a field (Skeptic's Star). FAIL: the arms differ but the CONTROL arm uses less, or the difference appears one week and reverses the next. ARTIFACT: the kWh figure tracks the room temperature, the door-opening count, the frost state or the week rather than the arm. Report the source's own 13.5% and 37% figures beside yours so the two can be compared directly.",
    ["Science", "Measurement", "Food Preservation"],
    "❄️"
  ],
  verify: "This is a test of an APPLIED, QUANTITATIVE claim, not of the torsion-field mechanism, and the card says so first. The mechanism the source invokes — torsion fields as the spin polarisation of the physical vacuum, acting on matter by changing the properties of water — has no accepted physical basis; the Russian Academy of Sciences dismissed the torsion programme in the 1990s, and the claim-status record this card sits beside (synthesis/claim-status-records/soviet-torsion-psychotronics-1960s.json) carries status 'suppressed' with grounds [dismissal, funding-cutoff, institutional-death]. What is testable is what the source actually measured, quoted: 'During operation with the thermostat, an average driving-power consumption lower by 13.5% was recorded in the case of the installed polarizers (series 1 and 3)' and 'a shortening of both the cooling and the freezing time of the water was found — on average by about 37%'. The card carries the source's OWN two admissions as its primary controls, quoted verbatim: 'During the tests, the thermal load of the refrigeration chamber was not determined. There is therefore no possibility of determining the coefficient of cooling performance. The internal coefficient of cooling performance ... remained at a similar level (about 2.5 in the case of operation with the thermostat) — regardless of the presence of the polarizers', and 'The ambient temperature of the chamber (which affects the thermal load) was similar for all measurement series, but not identical. It was not regulated.' Read together these are the paper's own null: a 13.5% power saving with an unchanged coefficient of performance, in a room whose temperature was never controlled. Three further limits are stated and not hidden. (1) AUTHOR CONFLICT: the first author is P.P.H.U. TORST, the firm that manufactures the polarizers under test. (2) NO BLINDING, NO RANDOMISATION, NO REPLICATION: the four series are not randomised, the operator knew the configuration, and no second laboratory has attempted it in twenty years. (3) THE DEVICE IS PROPRIETARY: no dimensions, materials or schematic are published, so this card tests the class claim (a passive unpowered object changes an appliance's energy use) and NOT the HPT® product — a null here refutes the class, not the product, and the card says so in its own quest text. The ordinary rival explanation is strong and is the expected result: a freezer's power draw is dominated by its thermal load, which is set by ambient temperature, door openings, load and the frost layer; frost is self-reinforcing (a thicker layer insulates the evaporator and lengthens every later compressor run); and any device that happens to leave less frost will show a lower power figure with no field involved. That is why the primary endpoint is ambient-NORMALISED energy, why the control is a matched inert object of the same mass and metal, and why the arm order is blinded. The expected result is the ordinary one, and the ordinary one is a complete result.",
  source_doc: "living-library/translations/2026-09-30-zagadkowe-fale-torsyjne-chlodnictwo-pacocha-targanski-pl.md (Henryk Pacocha & Waldemar Targański, 'Zagadkowe fale torsyjne a oszczędności w chłodnictwie' / 'Mysterious torsion waves and savings in refrigeration', Technika Chłodnicza i Klimatyzacja 2006 no. 9, source https://www.tchik.com.pl/archiwum/2006/9/fale_torsyjne.pdf, pl->EN 4 chunks, complete) + living-library/translations/2026-10-08-zagadkowe-fale-torsyjne-chlodnictwo-pl.md (same study republished on klimatyzacja.pl, pl->EN 7 chunks, complete)",
  source_url: "https://www.tchik.com.pl/archiwum/2006/9/fale_torsyjne.pdf",
  dossier: "living-library/synthesis/replication/2026-10-15-dossier-095-cold-storage-energy.md",
  pass_fail: "PASS (the claim survives): the device arm's ambient-normalised kWh per 24 h is >= 10% lower than the matched inert control's in BOTH weeks, with the instrument check passed and the blinding held, and the 1-litre freezing time is shorter in the device arm in both weeks — the first independent confirmation of any part of this claim | PASS (the rival is sufficient — the expected, ordinary result): the two arms' ambient-normalised kWh agree within the meter resolution and the between-day scatter in both weeks, with the instrument check passed — a passive unpowered object of this kind does nothing measurable to a freezer, and the source's 13.5% was the unregulated room temperature and the frost state rather than a field (Skeptic's Star) | FAIL: the arms differ but NOT in the pre-registered direction (the matched inert control uses less), or the difference appears in one week and reverses in the other | INCONCLUSIVE: the instrument check failed (two no-device days differed by more than the target effect); the room temperature moved more than 3 K within a period; the freezer contents or the door-opening count differed materially between arms; the blinding was broken; fewer than 8 periods in either week; the meter's resolution is coarser than the effect sought | ARTIFACT: the kWh figure tracks room temperature, door-opening count, frost state or the week rather than the arm; the frost photographs differ because the defrost state differed; the operator's expectation is visible in the arm order",
  evidence: "Photos of the built coil and the matched inert control on a kitchen scale showing equal mass + the pre-registration sheet (thermostat setting, weighed contents, door rule, defrost rule, predicted direction, criteria, operator name) photographed before period 1 + the instrument-check log (two no-device days, kWh, ambient) + the sealed arm-order sheets for both weeks + the 16 period logs (cumulative kWh, mean room temperature, door-opening count, compressor duty cycle) + the 1-litre freezing-time trace per arm + the evaporator-frost and condensate-ice photographs per period + the ambient-normalised comparison table with the source's own 13.5% and 37% figures shown alongside for direct comparison + the void/artifact checks reported whether or not they void the run"
}
```

---

## Source Document
- **ID**: `translations/2026-09-30-zagadkowe-fale-torsyjne-chlodnictwo-pacocha-targanski-pl.md`
- **Authors**: Henryk Pacocha (P.P.H.U. TORST) & Waldemar Targański (Gdańsk University of Technology, Department of Thermal Engineering)
- **Published**: *Technika Chłodnicza i Klimatyzacja* 2006 no. 9 — https://www.tchik.com.pl/archiwum/2006/9/fale_torsyjne.pdf
- **Claim (quoted)**: *"During operation with the thermostat, an average driving-power consumption lower by 13.5% was recorded in the case of the installed polarizers (series 1 and 3)."* · *"After the polarizers were installed in the chamber … a shortening of both the cooling and the freezing time of the water was found — on average by about 37%."*
- **The source's own null (quoted)**: *"The internal coefficient of cooling performance … remained at a similar level (about 2.5 in the case of operation with the thermostat) — regardless of the presence of the polarizers."*
- **The source's own admitted hole (quoted)**: *"During the tests, the thermal load of the refrigeration chamber was not determined. There is therefore no possibility of determining the coefficient of cooling performance."* · *"The ambient temperature of the chamber (which affects the thermal load) was similar for all measurement series, but not identical. It was not regulated."*
- **Vault link**: https://focusingpulse.github.io/AFLinks

## Dossier
- **Path**: `living-library/synthesis/replication/2026-10-15-dossier-095-cold-storage-energy.md`
- **Status**: protocol (no replication attempts yet)
- **Cost**: ~$25–60 (a plug-in cumulative-kWh energy meter, two matched 1 L bottles, a room thermometer, ~$10 of copper wire)
- **Time**: 8 × 24 h periods, run twice (16 days of freezer logging)

## Pass/Fail Criteria
- **PASS (supports the claim)**: device arm's ambient-normalised kWh ≥ 10% lower than the matched inert control's in **both** weeks, instrument check passed, blinding held, and the 1 L freezing time shorter in the device arm in both weeks.
- **PASS (refutes the class claim — the expected result)**: the two arms agree within the meter resolution and the between-day scatter, in both weeks, with the instrument check passed. A passive unpowered object of this kind does nothing measurable to a freezer.
- **FAIL**: the arms differ but the control arm uses less, or the difference reverses between weeks.
- **INCONCLUSIVE**: instrument check failed; room temperature moved > 3 K within a period; contents or door-opening count differed between arms; blinding broken; fewer than 8 periods; meter resolution coarser than the effect.

## Relationship to the queue's other Food Prep cards (stated, not hidden)

This is the **4th Food Prep card**, and the mirror already carries a cold-storage card:

| | `2026-09-26-cold-machine-vortex-cooling.md` (dossier 043) | This card (dossier 095) |
|---|---|---|
| What is under test | a **vortex cooling machine** the family builds | a **passive device with no power supply** placed in the family's **existing freezer** |
| Independent variable | the vortex arm vs a matched straight arm | the passive device vs a **matched inert object of the same mass and metal** |
| Primary endpoint | the temperature the machine can reach | the **energy the appliance draws** (ambient-normalised kWh) |
| Source | a source that debunks its own headline claim | a source whose own COP measurement contradicts its headline claim |

The two share a domain (cold storage) and nothing else — one asks *can a buildable machine cool?*, the other asks *does a passive object make an existing appliance cheaper to run?* The other two Food Prep cards are the **egg-shaped fermentation vessel** (vessel geometry) and **pyramid storage desiccation** (form effect on drying).

## What makes this the queue's first of its kind

- The first card whose **primary endpoint is the ENERGY a household appliance draws** — every prior card measures a temperature, a count, a position, a weight, a trace or a perception.
- The first whose **independent variable is a device with no power supply at all** — no battery, no mains, no drive.
- The first whose **control is a matched inert object of the same mass and the same metal** (the wire itself, unwound) rather than a different apparatus, a shielded arm or a baseline scatter.
- The first that carries **the source's own internal contradiction as the design's central control** — a 13.5% power saving reported alongside an unchanged coefficient of performance, which is the paper's own null and the reason the endpoint is ambient-normalised energy.
- The first on the **torsion-field-applied-to-refrigeration** lineage, and the first whose source is a **manufacturer and a university department of thermal engineering** rather than a practitioner, a fringe academy or a lone inventor.
- The first whose **apparatus problem is stated in the quest text** — the source's device is proprietary, so the card tests the class claim and says plainly that a null refutes the class and not the product.
