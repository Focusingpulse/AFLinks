---
name: Sealed-Box Electrostatic Thrust Test
description: "Test whether an asymmetric electrostatic-pressure device produces thrust that survives inside a sealed enclosure — the discriminating prediction that separates a claimed new force from ion wind. A balsa lifter calibrates the box. Energy/propulsion card; ~$120–180; Rocket mirror. Adult-only, lethal-voltage gate."
---

# ⚡ Aetherforce — Propulsion

**Guild:** Aetherforce — Propulsion
**Quest Line:** ⚡ Aetherforce · Rocket complement
**Tier:** straw
**Domain:** energy (electrostatic propulsion — propellantless thrust)
**Status:** proposed
**Created:** 2026-09-23

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-09-23-sealed-box-electrostatic-thrust` · authored_at `2026-09-23` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## ⚠ Safety gate — read this before the quest

The apparatus runs at **10–50 kV**. It can kill. **Adults only. No children in the room. Never work alone. One hand in the pocket. Insulated probe and discharge wand. Power off and discharge before any touch. Switch on from a distance. Keep the whole apparatus inside the closed box while energised. Keep the current-limiting resistor in circuit. No pacemakers, no heart conditions, no water on the floor.** If any of those cannot be met, **do not run this card** — the refusal is the correct outcome, and it is recorded as one.

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural"],
  name: "Aetherforce — Propulsion",
  desc: "Two engineers — one of them the lead of NASA's electrostatics laboratory — say an asymmetric electrostatic device makes thrust that is not ion wind, and they demonstrate the contrast with a balsa lifter in a sealed plastic box on a scale. That box is the whole experiment: a closed box closes the momentum budget, so a thrust made by pushing air out of the system must vanish inside it. Build both devices — the lifter that is supposed to read flat, and the blade-geometry article that is supposed to read non-flat — and put them in the same box on the same scale. The lifter is not a warm-up; it is the control that proves the box is doing its job. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "straw",
  quest: [
    "Sealed-Box Electrostatic Thrust Test",
    "Build two articles: (A) a balsa lifter — aluminium-foil plate 3–4 cm wide, corona wire 0.2–0.4 mm, on a light frame; (B) a single-stage electrostatic-pressure article in the blade geometry — one electrode carrying a proximal conductive face close to a flat opposing plate and a distal face further away, joined by a conductive web, the two held apart by a NON-conductive brace. Power both from a current-limited, enclosed 10–50 kV supply. Put a 0.01 g scale under the rig. First run the OPEN arm: device on the stand, powered off vs on, 10 alternating cycles, for both articles — this proves the rig can see a thrust at all. Then run the SEALED arm: device and stand inside a clear plastic box with a lid, the BOX on the scale, power fed through a slack flexible lead with a service loop so it cannot push or pull, 10 alternating cycles, for both articles. Run a mass-matched dummy on the same lead as the lead-artifact control. Repeat with each device flipped 180° and with polarity reversed — the claim predicts the reading reverses on flip; ion wind does not. Repeat the whole thing in three sessions on different days. Measurable outcome: delta-mass in grams (powered off minus powered on) for each article in each arm, against the dummy's delta and against the lifter control's sealed reading. Target: blade article delta >= 0.5 g (>=5 mN) sealed, at least 10x the dummy, with the lifter control flat (|delta| <= 0.1 g) and the reading reversing on flip, in all three sessions — or the honest negative: the blade article flat in the box while the lifter shows clear thrust in the open arm.",
    ["Science", "Engineering", "Energy"],
    "⚡"
  ],
  source_doc: "sources/2026-09-14-deep-dive-morning-a#find-2 (Exodus/Buhler New Force) + translations/2026-09-22-shipov-institute-vacuum-physics-experiments-ru (Brown asymmetric capacitor construction) + sources/2026-09-17-patent-watch#1 (US 12,715,620, Biefeld-Brown thrust claim)",
  source_url: "https://patents.google.com/patent/WO2020159603A2/en",
  dossier: "living-library/synthesis/replication/2026-09-23-dossier-036-sealed-box-electrostatic-thrust.md",
  pass_fail: "PASS: blade article delta-mass in the sealed box >= 0.5 g (>=5 mN), at least 10x the mass-matched dummy's reading, with the balsa lifter control flat in the same box (|delta| <= 0.1 g) and the reading reversing on device flip - repeated in three separate sessions. FAIL: blade article flat in the sealed box (within 2x the dummy's noise) while the lifter shows a clear thrust in the open arm - the force is momentum exchange with the external air and the claim does not survive at home scale (honest negative, Skeptic's Star). INCONCLUSIVE: the lifter control does NOT read flat in the sealed box (the enclosure is invalid - a leak, a stiff lead, a draught), the scale cannot resolve the claimed force, the device arcs at the working voltage, the dummy reads comparably to the device, the key was opened before the tally, or N was not pre-registered.",
  evidence: "Photo of the pre-registration sheet (cycle counts, thresholds, scoring rule, key-holder) + photos of both articles with a ruler in frame + the open-arm table for both articles (10 alternating cycles each, powered off vs on) + the sealed-arm table for both articles + the dummy's readings + the flip and polarity-reversal readings + the lifter control's sealed reading shown explicitly + a photo of the closed box on the scale with the lead entering + the full tally with the arithmetic shown + all three session dates. A video of one powered cycle per arm is strongly preferred, with the scale display and the box in the same frame."
}
```

---

## Source Documentation

- **Primary (the device class):** WO2020159603A2, *"System and method for generating forces using asymmetrical electrostatic pressure"*, inventors **Andrew Neil Aurigema** and **Charles Raymond Buhler**, priority 2018-11-19, published 2020-08-06, status **Ceased** — https://patents.google.com/patent/WO2020159603A2/en (**fetched and read 2026-09-23**). The patent states that the invention *"does not require the use of an ion wind to generate the force"*, derives the force from electrostatic pressure (½ε₀E²), notes the effect is *"about five orders of magnitude less"* than the Coulomb attraction inside the same device, and says the reduction-to-practice tests *"were generally performed within an enclosed box to nullify ion wind effects."* Its worked geometry is the **blade configuration** (proximal + distal conductive faces joined by a conductive web, opposing a flat plate, held apart by a non-conductive brace).
- **Primary (the 2026 claim and the demonstration):** Brian Wang, *"Exodus Propulsion and the Exodus Force aka Electrostatic Pressure Force"*, NextBigFuture, 2026-03-31 — https://www.nextbigfuture.com/2026/03/exodus-propulsion-and-the-electrostatic-pressure-force.html (**fetched and read 2026-09-23**). Reports ~2,000 vacuum-chamber tests, **5–10 mN** on ~30–40 g articles, thrust *"perpendicular to the expected ion wind direction, reverses cleanly when the device is flipped, and remains present inside a sealed enclosure"*, persistence after power-off, and **no independent replication**. It also records the claimants' own control demonstration: *"a balsa lifter placed inside a sealed plastic box on a scale, powered up, lifts internally while the scale reads flat. That is conservation of momentum. That is what ion wind looks like."*
- **Archive source (construction numbers):** `translations/2026-09-22-shipov-institute-vacuum-physics-experiments-ru.md` — the Institute of Vacuum Physics *Experiments* page (RU→EN, 2026-09-22): *"Brown's asymmetric capacitor is a capacitor construction in which one plate is made of foil 3–4 cm wide and the other a wire 0.2–0.4 millimetres thick. A voltage of 35–50 thousand volts is applied to the plates. When the voltage is applied, the whole construction takes off, overcoming the force of its own weight."*
- **Archive source (the claim is live in the patent record):** `sources/2026-09-17-patent-watch.md` find 1 — **US 12,715,620**, granted 2026-08-25, claiming thrust *"via Biefeld-Brown electrogravitic effect"* inside a zero-point-energy / gravity-nullification claim. A granted patent is not evidence the effect works.
- **Archive source (the status report):** `sources/2026-09-14-deep-dive-morning-a.md` find 2.
- **Replication Dossier:** `living-library/synthesis/replication/2026-09-23-dossier-036-sealed-box-electrostatic-thrust.md`
- **Vault:** https://focusingpulse.github.io/AFLinks — search "Biefeld-Brown", "asymmetric capacitor", "electrogravitics", "Townsend Brown", "lifter"
- **Aetherforce Reference:** Search "electrogravitics", "Townsend Brown", or "Biefeld-Brown" on https://www.aetherforce.energy
- **Related dossiers:** 002 (Tesla Radiant Receiver — the other ambient-field card), 008 (Vortex Jet Turbine — the other Rocket-mirror card), 018 (Bladeless Tesla Turbine — the other anomalous energy-conversion card)

---

## Rubric Justification

| Criterion | Assessment |
|-----------|------------|
| **Practical** | YES — Named apparatus (two articles, a current-limited HV supply, a 0.01 g scale, a clear box) with a named procedure (open arm, sealed arm, dummy control, flip and polarity reversal, three sessions) and a numeric outcome (delta-mass in grams for each article in each arm, against two controls). Not pure theory. |
| **Replicable** | YES — Home/homelab, ~$120–180. Every component is a commodity item; the blade geometry is a foil-and-brace build; nothing needs a machine shop. **Gated: adults only, lethal-voltage preconditions listed in the card.** |
| **Relevant** | YES — Energy domain: propellantless electrostatic thrust is the extreme end of "off-grid without relying on big anything," and the card's real product is a measurement skill (how to close a momentum budget on a bench). Complements the Rocket guild — the mirror for exotic propulsion — which holds one card. |
| **Honest** | YES — The claim is framed as a claim: unreplicated, un-peer-reviewed, patent-status *Ceased*, with the EmDrive precedent named and the ARL's own "not understood" line quoted from inside the patent. The card's limitation (it cannot reproduce Buhler's specific articles, only the discriminating prediction on the closest home-buildable member of the class) is stated in the card and the dossier. Clean FAIL path. |
| **Linked** | YES — Three archive source docs plus two primary documents fetched and read this run, a pre-registered replication dossier, and cross-links to three related cards. |

**Mirror choice, stated:** the card's **domain is energy** (the rotation's next field), and its **guild complement is Rocket** — the mirror the engine's own map defines as "free energy / implosion," i.e. exotic propulsion and energy, which already holds the Vortex Jet Turbine card. Rocket is the emptiest relevant mirror (1 card); stacking a fourth card on the Electricity mirror would over-weight one complement, and an electrostatic thruster is propulsion before it is wiring.

---

## The honest framing (the spine of the card)

- **The box is the experiment, not the packaging.** A sealed enclosure closes the momentum budget. A force made by pushing air out of the system cannot move the scale inside a closed box — the device's pull on the box cancels the air's push on the box. A force that is not momentum exchange can. **The test needs no theory of the mechanism; it needs only that the box be closed.**
- **The lifter is the control, not a warm-up.** The claimants themselves put a balsa lifter in a sealed box on a scale as the picture of the ion-wind result. If our lifter does **not** read flat in our box, our box is leaking momentum or our lead is transmitting force, and **the whole test is invalid.** That is the enclosure calibrating itself.
- **Credential is not evidence.** One claimant leads NASA's electrostatics laboratory and is incoming president of the Electrostatic Society of America. That is a reason to take the claim seriously and to test it properly. It is not a reason to believe it.
- **A patent is a claim, not a result.** WO2020159603A2 describes a claimed invention; its status is **Ceased**. The examiner's witness affidavits the claimant calls "equivalent to peer review" are not controlled measurements.
- **The nearest precedent failed.** The EmDrive lineage did not survive independent testing, and the source itself places this work in that lineage. That is the base rate, and the card says so.
- **The claimed force is small, and the card states its own resolution.** 5–10 mN is 0.5–1 g-force on a 30–40 g article; a 0.01 g scale resolves 0.098 mN, so the claim sits at 50–100 counts. If the bench cannot resolve it, the honest verdict is INCONCLUSIVE, not FAIL.
- **A null is the likely outcome and is a complete result.** The mainstream account predicts it. Producing it with a pre-registered protocol, a control, and three sessions would be the first home-scale independent data point on a live 2026 claim — and it earns the Skeptic's Star.
- **This card cannot reproduce Buhler's own device.** The patent describes a class of geometries and no source we hold fully dimensions the tested articles. The card tests the discriminating prediction on the closest home-buildable member of the class. That is a real limitation and it is written down, not hidden.
