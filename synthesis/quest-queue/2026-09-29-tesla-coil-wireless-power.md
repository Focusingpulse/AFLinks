---
name: Mini Tesla Coil Wireless Power Transfer Test
description: "Test whether a home Tesla coil transfers usable power to an UNCONNECTED receiver through the field, and whether the received power falls off like a near field (steep, a few coil-heights) or a radiated wave (shallow, many coil-heights) — the one measurement that separates Tesla's near-field demonstration from his transmission-at-distance claim. Energy card; home, ~$50–150; Power mirror (Electricity complement). The queue's first wireless-power-transfer card, and its first whose endpoint is a fitted falloff exponent."
---

# ⚡ Aetherforce — Power

**Guild:** Aetherforce — Power (complements Electricity)
**Quest Line:** ⚡ Aetherforce · Electricity complement
**Tier:** sand
**Domain:** energy (wireless power transfer — near-field vs far-field)
**Status:** proposed

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-09-29-tesla-coil-wireless-power` · authored_at `2026-09-29` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural"],
  name: "Aetherforce — Power",
  desc: "Tesla's whole thesis was that energy can live in the field, not only in the wire. A miniature Tesla coil proves the easy half of that on the table: a nearby bulb lights with no wire attached. What it does NOT prove is the half Tesla actually cared about — power that reaches across distance. This card builds the coil and then measures the part nobody measures: how the received power falls off as you carry the receiver away. A near field drops off steeply and dies within a few coil-heights; a radiated wave drops off gently and keeps going. Fit the falloff and you have your answer. The source itself says the far-field mode is 'very weak in practice' — so a steep falloff is the expected result, and a shallow one would be the surprise. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "sand",
  quest: [
    "Mini Tesla Coil Wireless Power Transfer Test",
    "Build the miniature coil (24 V DC primary, a 2000-turn secondary on a plastic tube, a foil toroid) and tune a small receiver coil to the coil's resonant frequency. Then carry the receiver away from the coil along the axis and radially, recording the received power (a bulb's brightness, or a rectified voltage across a known load) at each pre-registered distance with the coil on and off. Repeat three times, re-randomising the order. Measurable outcome: plot received power against distance on a log-log axis and fit the falloff exponent - an exponent of -2 or steeper with reception stopping within a few coil-heights means near-field inductive coupling (the coil is a short-range device); an exponent of -1 or shallower with reception at ten coil-heights or more supports Tesla's transmission-at-distance claim and needs a second independent replication. An untuned receiver voids the run.",
    ["Science", "Physics", "Measurement"],
    "🗼"
  ],
  source_doc: "translations/2026-09-28-mini-tesla-coil-wireless-power-ar.md (Khaled Hamidi, 'Mini Tesla Coil: Wireless Energy Transfer', 2023) + sources/2026-08-30-scout-a-it-pt-ar.md#find-10",
  source_url: "https://khaledhamidi.com/ar/writing/tesla/",
  dossier: "living-library/synthesis/replication/2026-09-29-dossier-053-tesla-coil-wireless-power.md",
  pass_fail: "PASS (near-field coupling, the source's own honest reading): received power falls off steeply (fitted exponent <= -2) and reception stops within a few coil-heights - the coil transfers power by resonant inductive coupling over short distances, the same principle as modern wireless charging, and does NOT transmit usable power at distance. PASS (far-field / transmission-at-distance - a surprising result): measurable received power at >= 10 coil-heights with a shallow falloff (exponent >= -1) - supports Tesla's transmission claim; requires a second independent replication before any conclusion. FAIL: no measurable power transfer to an unconnected receiver at any distance. INCONCLUSIVE: the receiver was not tuned to the coil's resonant frequency; distances or orientations were not recorded; input power was not recorded; fewer than three repeats. ARTIFACT: the receiver lights from capacitive (electric-field) coupling rather than the magnetic near field (separate by re-orienting and shielding, then re-measure); the 'receiver' is connected by a wire; or the reading tracks the coil's spark rate rather than distance.",
  evidence: "Photo of the built coil + the pre-registration sheet (resonant frequency, distances, axis/radial directions, receiver orientation, load, repeats, thresholds) + the coil's resonant frequency and how it was found + the input power (24 V x current) + the received-reading table for every distance in both directions, coil on and off + the log-log plot with the fitted exponent + the distance at which reception stopped + the three repeats + the void and artifact checks reported whether or not they void the run"
}
```

---

## Source Documentation

- **Primary (the claim and the build):** Khaled Hamidi, *ملف تسلا مصغر: نقل الطاقة لاسلكيا* (Mini Tesla Coil: Wireless Energy Transfer), September 2023 — https://khaledhamidi.com/ar/writing/tesla/ (**full English translation in the library and read this run**: `translations/2026-09-28-mini-tesla-coil-wireless-power-ar.md`). The guide gives a complete construction procedure — a 24 V DC primary with a capacitor and spark gap, a **2000-turn** secondary on an insulating tube, and a foil toroid top — and states the near-field / far-field distinction in its own words: near-field coupling transfers "a considerable portion of the power … with reasonable efficiency over short distances — the same principle used today in resonant wireless charging," while far-field radiation "is very weak in practice due to losses and attenuation" at the low frequencies Tesla sought.
- **Scout entries:** `sources/2026-08-30-scout-a-it-pt-ar.md` (find 10 — the build guide; `buildable, reproducible`; "Safe miniature design. Practical demonstration of Tesla's wireless energy vision."); `sources/2026-08-26-scout-b-de-ru-it.md` (**Teslas Verschollene Erfindungen** — Tesla's spark-gap oscillator, Tesla coil, Earth-resonance frequencies 6.8 Hz / 11.78 Hz / 150 kHz, Wardenclyffe; the scout's own note: "Tesla coil and spark-gap oscillator are reproducible; wireless power transmission at scale was never demonstrated"); `sources/2026-08-27-scout-b-fr-sr-ja.md` (Tesla's wireless-power vision connected to modern WPT and electric-field resonant WPT, UNIST Korea — the modern comparator).
- **Replication Dossier:** `living-library/synthesis/replication/2026-09-29-dossier-053-tesla-coil-wireless-power.md`
- **Vault:** https://focusingpulse.github.io/AFLinks — search "Tesla coil", "wireless power", "resonance", "Wardenclyffe"
- **Aetherforce Reference:** Search "Tesla coil", "wireless power transmission", or "resonance" on https://www.aetherforce.energy
- **Related dossiers:** 003 (Tesla Radiant Receiver — the same inventor, a *receiver* claim; this card is about the *transmitter's* field), 030 (Chiappini Planetary Antenna — the same RF/field family, a *communications* claim), 018 (Bladeless Tesla Turbine — the same inventor's fluid device, a static-electricity claim), 047 (Keppe Motor Matched-Load — the queue's other *comparative* energy measurement)

---

## Rubric Justification

| Criterion | Assessment |
|-----------|------------|
| **Practical** | YES — Named apparatus (a 24 V primary, a 2000-turn secondary, a foil toroid, a tuned receiver coil and load) with a named procedure (build, tune, carry the receiver away, record at pre-registered distances, fit the falloff) and a measurable outcome (the fitted falloff exponent and the distance at which reception stops). Not pure theory. |
| **Replicable** | YES — Home, ~$50–150: a 24 V supply, magnet wire, a plastic tube, a capacitor and spark gap, foil, a receiver coil, a bulb or a multimeter, and a tape measure. No mains work, no purchased instrument beyond a multimeter. One afternoon to wind and assemble, one session to measure. |
| **Relevant** | YES — Energy domain: wireless power transfer is the foundational off-grid-energy claim of the Tesla/Aetherforce lineage. Fills the **Power** mirror (the Electricity complement). |
| **Honest** | YES — The claim is framed as a claim; the source itself separates near-field (works, = modern wireless charging) from far-field (weak) and concedes the far-field result in advance. The card's endpoint is the *falloff*, not the lighting, and it names the capacitive-coupling confound. Clean FAIL path and a clean "the coil is a near-field device" path. |
| **Linked** | YES — One primary build guide read this run, three scout entries, a pre-registered replication dossier, a Vault search pointer, and cross-links to four related cards. |

**Mirror choice, stated:** the card's **domain is energy** (the rotation's next field) and its **guild complement is Power** — the Electricity mirror, whose theme is electrical generation and transmission. **Electricity** was the alternative label (the queue's other Tesla cards — 003 and 018 — sit there); **Power** was chosen because this card's subject is the *transmission* of electrical energy through space, not its generation at a device — the same domain/mirror split the queue already uses for card 047 (Keppe motor, energy domain, Power mirror).

---

## The honest framing (the spine of the card)

**The claim is a claim.** The source says a Tesla coil demonstrates that "energy can 'live' in the field, not only in the wire," and connects it to Tesla's vision of power transmission at distance. **This card tests that claim; it does not endorse it.**

**The easy half is not the claim.** That a resonant coil lights a nearby unconnected bulb is textbook **resonant inductive coupling** — the physics of a phone's wireless charger, which the source names as its own comparator. **A card that only shows "the bulb lights" proves nothing.** The claim that matters is the *distance* half: does the field carry usable power beyond the near field?

**The design that makes it a measurement.** Three things do the work:

1. **Distance is the independent variable.** The card carries the receiver away in pre-registered steps and records received power at each — a *curve*, not a single reading. The fitted exponent is the result.
2. **The falloff law is the discriminator.** A magnetic near field from a small coil falls off roughly as **1/r³** (dipole) or steeper; a radiated electromagnetic wave falls off as **1/r**. Nothing else in the measurement separates "near-field device" from "transmitter" as cleanly.
3. **The receiver must be tuned, and the confound is named.** An untuned receiver measures nothing, and a receiver can light from the coil's **electric** field (capacitive) as well as its **magnetic** near field — so the card re-orients and shields the receiver and re-measures, and voids the run if the receiver was not tuned.

**The likely result is near-field coupling, and that is a complete result.** If received power falls off steeply and reception stops within a few coil-heights, the honest verdict is *"the coil is a short-range device; the same physics runs your phone's wireless charger, and the field does not carry usable power at distance."* That retires the transmission-at-distance claim while leaving the demonstration standing, and it is exactly the answer a family needs before spending on a "free energy" build.

**The central limitation, stated up front: one coil is one coil.** The falloff depends on the coil's geometry, its resonant frequency, the receiver's tuning and the room. A result here speaks for *this* coil in *this* room, and the card requires repeats on a second day before any conclusion.

**Safety and honesty:** this is a bench experiment, **not** a power source. The primary runs at 24 V (safe); the **secondary reaches ~2500 V at low current** — a painful shock and a burn risk. **Adult supervision required; never touch the secondary or the toroid while powered.** The spark gap produces ozone and broadband RF interference — keep it away from medical devices and radios. Never connect a home-built coil to mains wiring.

---

## Relationship to the rest of the queue

This card is the **transmission counterpart to card 003** (Tesla Radiant Receiver). 003 tests whether a *receiver* draws power from the environment; this card tests whether a *transmitter's* field carries power across distance. Same inventor, opposite end of the same question — and the overlap is stated here rather than hidden.

It is also the **first card in the queue whose endpoint is a fitted falloff exponent** — a measurement curve rather than a single reading — and the **first wireless-power-transfer card** of any kind. Every prior energy card measures a device's output at the device (voltage, current, efficiency); this one measures the *spatial decay of power through the field*, which is the only honest way to ask whether "power through the aether" reaches beyond the near field.
