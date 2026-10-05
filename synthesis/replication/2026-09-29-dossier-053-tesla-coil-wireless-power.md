---
name: Dossier 053 — Mini Tesla Coil Wireless Power Transfer Test
description: "Replication dossier for the Tesla-coil wireless-power claim: a resonant coil lights an unconnected lamp through the field, and Tesla's larger vision was power transmission at distance through the aether. The card builds the miniature coil from an Arabic build guide and measures how received power falls off with distance — near-field inductive coupling (steep falloff, a few coil-heights) vs far-field radiation (shallow falloff, many coil-heights). Energy card; home, ~$50–150. The queue's first wireless-power-transfer card."
---

# Dossier 053 — The Mini Tesla Coil Wireless Power Transfer Test

**Status:** protocol
**Domain:** energy (wireless power transfer — near-field vs far-field)
**Tier:** sand (home, ~$50–150)
**Created:** 2026-09-29
**Source docs:**
- `living-library/translations/2026-09-28-mini-tesla-coil-wireless-power-ar.md` — the **full English translation** of Khaled Hamidi's Arabic build guide *ملف تسلا مصغر: نقل الطاقة لاسلكيا* (Mini Tesla Coil: Wireless Energy Transfer, September 2023). Source page: https://khaledhamidi.com/ar/writing/tesla/ — the guide gives a complete construction procedure (24 V DC primary, 2000-turn secondary, foil toroid) and states the near-field / far-field distinction in its own words.
- `living-library/sources/2026-08-30-scout-a-it-pt-ar.md` — **find 10** (Khaled Hamidi mini Tesla coil guide; `buildable, reproducible`; "Safe miniature design. Practical demonstration of Tesla's wireless energy vision.").
- `living-library/sources/2026-08-26-scout-b-de-ru-it.md` — **Teslas Verschollene Erfindungen** (German; Tesla's spark-gap oscillator, Tesla coil, Earth-resonance frequencies 6.8 Hz / 11.78 Hz / 150 kHz, Wardenclyffe; "Tesla coil and spark-gap oscillator are reproducible; wireless power transmission at scale was never demonstrated").
- `living-library/sources/2026-08-27-scout-b-fr-sr-ja.md` — Tesla's wireless-power vision connected to modern wireless power transfer (WPT) and electric-field resonant WPT (ERWPT, UNIST Korea) — the modern comparator.

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-09-29-tesla-coil-wireless-power` · authored_at `2026-09-29` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## The claim (as asserted by the source)

The source's own framing, translated:

> "In this guide we will build a miniature, safe model of this coil, to see in practice how the idea of 'power transmission through the aether' turns from a dream in Tesla's mind into an experiment you can carry out on your table."

> "An oscillating electromagnetic field around the secondary coil, enough to light fluorescent/neon bulbs nearby without a wired connection, as a clear example of part of the energy being transferred through the field rather than through a wire. A practical demonstration of the idea that energy can 'live' in the field, not only in the wire — which is the essence of what Tesla was trying to prove practically, on much larger scales."

The source then does something most free-energy material does not — **it separates the two regimes itself**:

> "**Near-Field Coupling:** … the near fields (the strong magnetic field around the coil) are used to transfer energy to other nearby resonant circuits tuned to the same frequency (such as a receiving loop or a nearby neon lamp). Here a considerable portion of the power is transferred with reasonable efficiency over short distances — the same principle used today in resonant wireless charging (Resonant Inductive Coupling). **Far-Field Radiation:** at certain frequencies and special designs, a Tesla coil can radiate part of its energy as an electromagnetic wave into far space … But the efficiency of this mode, especially at the low frequencies Tesla sought for transmitting power over continental distances, is very weak in practice due to losses and attenuation."

**What is being tested, in one sentence:** does a home Tesla coil transfer usable power to an *unconnected* receiver through the field, and does the received power fall off like a **near field** (steep, a few coil-heights) or like a **radiated wave** (shallow, many coil-heights)?

## Honest status of the claim

**The archive holds the claim and no home test of it.** A grep for `wireless power`, `Tesla coil`, `resonant inductive`, and `power transfer` across `living-library/synthesis/` returns no card and no dossier — the queue has no wireless-power-transfer card of any kind. Its energy cards test a **radiant-energy receiver** (003), a **bladeless turbine's static-electricity conversion** (018), a **planetary RF antenna** (030), a **motor's matched-load efficiency** (047), a **vortex motor** (031) and a **vortex jet turbine** (008). **None measures how power falls off with distance through the field** — the one endpoint that separates Tesla's near-field demonstration from his transmission-at-distance claim.

Three things the card must say out loud, because they are what a family is actually testing:

1. **The near-field result is not the claim.** That a resonant coil lights a nearby bulb is textbook resonant inductive coupling — the same physics as a phone's wireless charger (the source names this comparator itself). **A card that only shows "the bulb lights" proves nothing new.** The card is about the *falloff*, not the lighting.
2. **The falloff law is the discriminator.** A magnetic near field from a small coil falls off roughly as **1/r³** (dipole) or steeper; a radiated electromagnetic wave falls off as **1/r**. Measuring received power at a series of distances and fitting the exponent is what tells the two apart — and it is the only honest way to ask whether "power through the aether" reaches beyond the near field.
3. **The source concedes the far-field result in advance.** It states plainly that far-field transmission "is very weak in practice due to losses and attenuation" at the low frequencies Tesla sought. **So the default expectation is near-field coupling, and a far-field result would be the surprise that justifies a second round.** The card is a test, not an endorsement.

**Under-promise, stated plainly:** the likely outcome is that received power falls off steeply and reception stops within a few coil-heights — i.e. the honest verdict is *"the coil transfers power by resonant inductive coupling over short distances, and does not transmit usable power at distance."* That is a complete, useful result (it tells a family that a Tesla coil is a near-field device, and that modern wireless charging is the same physics). A far-field result would be genuinely surprising and would require independent replication.

## Why it matters

- It is the queue's **first wireless-power-transfer card** — every prior energy card measures a device's *output* (voltage, current, efficiency) at the device; this one measures the **spatial falloff of power through the field**, a different physical question.
- It is the **first card whose endpoint is a fitted falloff exponent** — a measurement *curve*, not a single reading. It teaches the transferable lesson: **when a claim is about transmission at a distance, the distance is the independent variable and the falloff law is the result.**
- It is the **first card that tests Tesla's own thesis** (power through the field, not the wire) rather than a later device built on it — and the source hands the card its own honest comparator (resonant inductive coupling = modern wireless charging).
- It is genuinely **family-scale**: a safe 24 V build, an afternoon of winding, and a ruler. It is the smallest bet in the queue's energy set and the one a child can help wind.

## Replicability: `home`

- Build/obtain cost: **~$50–150** — a 24 V DC supply (~$10–20), magnet wire for the 2000-turn secondary (~$10–20), a plastic tube former (~$0–5), a primary coil + capacitor + spark gap (~$10–30), aluminium foil and a paper ball for the toroid (~$0–5), a receiver coil + a neon/fluorescent bulb or a small lamp + a multimeter (~$15–40), and a tape measure.
- Safety: **low-voltage input, but not zero hazard.** The primary runs at 24 V DC (safe); the **secondary reaches ~2500 V at low current** — a painful shock, and a burn risk. **Adult supervision required; never touch the secondary or the toroid while powered.** The spark gap produces ozone and broadband RF interference (keep it away from medical devices and radios). Run it on a bench, not on a floor a child can reach.
- Accessibility: one afternoon to wind and assemble, one session to measure. The winding is the slow part.

## Apparatus (Bill of Materials)

- **A 24 V DC supply** — the safe miniature design the source specifies.
- **A primary circuit** — a capacitor, a spark gap, and a primary coil (few turns of heavier wire).
- **A secondary coil** — **2000 turns** of thin insulated copper wire on an insulating plastic tube; lower end to the circuit's negative pole, upper end to the toroid.
- **A top capacitor (toroid)** — a paper ball covered in aluminium foil, connected to the secondary's top.
- **A receiver** — a small coil (few turns) with a capacitor, **tuned to the coil's resonant frequency**, feeding a load: a neon/fluorescent bulb, or a small lamp, or a rectifier + a resistor of known value read by a multimeter.
- **A tape measure** and a **log sheet** — distance, orientation, and received reading, pre-registered.

## Protocol (distance-falloff test, pre-registered)

**Phase 1 — build and pre-register.**
1. Build the coil per the source's procedure (24 V primary, 2000-turn secondary, foil toroid). Photograph it.
2. Determine the coil's **resonant frequency** (from the secondary's inductance and distributed capacitance, or by tuning the receiver until the bulb is brightest at a fixed short distance). Record it. **Tune the receiver to that frequency — an untuned receiver makes the run inconclusive.**
3. Write the **pre-registration sheet** before measuring: the distances to be tested, the axis and the radial directions, the receiver's orientation, the load, the number of repeats, and the falloff exponents that would count as near-field vs far-field. Photograph it.

**Phase 2 — measure the falloff.**
4. Place the receiver at a fixed short distance where the load clearly responds. Record the baseline reading with the coil **off**.
5. Power the coil. Record the received reading at each pre-registered distance **along the coil's axis**, then **radially** from the coil's side. At each distance, record the reading with the coil on and off.
6. Repeat the whole series at least **three times**, re-randomising the order, and have a second person read the meter where the load is a bulb judged by eye.
7. Record the coil's input power (24 V × measured current) so the received/input ratio can be reported.

**Phase 3 — score.**
8. Plot received power (or load voltage) against distance on a log–log axis. Fit the exponent.
9. Score the pre-registered endpoint: **the fitted falloff exponent** and the **distance at which reception stops**.

## Pass / fail (pre-registered)

- **PASS (near-field coupling — the source's own honest reading):** received power falls off **steeply (exponent ≤ −2)** and reception stops within **a few coil-heights** — the coil transfers power by resonant inductive coupling over short distances, the same principle as modern wireless charging, and does **not** transmit usable power at distance. Reported as the expected result, not a failure.
- **PASS (far-field / aether transmission — a surprising result):** measurable received power at **≥ 10 coil-heights** with a **shallow falloff (exponent ≥ −1)** — supports Tesla's transmission-at-distance claim; **requires a second independent replication before any conclusion.**
- **FAIL:** no measurable power transfer to an unconnected receiver at any distance — the coil sparks but does not transfer power through the field.
- **INCONCLUSIVE:** the receiver was not tuned to the coil's resonant frequency; distances or orientations were not recorded; input power was not recorded; fewer than three repeats were run.
- **ARTIFACT:** the receiver lights from **capacitive (electric-field) coupling** to the coil rather than the magnetic near field — separate by re-orienting and shielding the receiver and re-measuring; or the "receiver" is connected by a wire; or the reading tracks the coil's spark rate rather than distance.

## Evidence

Photo of the built coil + the **pre-registration sheet** (resonant frequency, distances, axis/radial directions, receiver orientation, load, repeats, thresholds) + the coil's resonant frequency and how it was found + the input power (24 V × current) + the received-reading table for every distance in both directions, coil on and off + the log–log plot with the fitted exponent + the distance at which reception stopped + the three repeats + the void/artifact checks reported whether or not they void the run.

## Confounds (named in advance)

- **Capacitive vs inductive coupling — the central confound.** A nearby receiver can light from the coil's **electric** field (capacitive) as well as its **magnetic** near field. The card separates them by re-orienting and shielding the receiver and re-measuring; a result that survives re-orientation is the magnetic near field.
- **Resonance is required.** An untuned receiver measures nothing meaningful. The receiver must be tuned to the coil's resonant frequency or the run is void.
- **The spark gap is a broadband RF source.** The coil radiates interference as well as a near field; keep measurement distances well-defined and the environment fixed.
- **Orientation matters.** A near field is directional; record and hold the receiver's orientation.
- **Input power drifts.** The 24 V supply and the spark gap can drift; record input power at each repeat.
- **The reading is operator-judged where the load is a bulb.** Use a second reader and keep the distance labels keyed by someone other than the reader.
- **One session is a sample of one.** Repeat on a second day before concluding anything.

## Verdict rules

Steep falloff (≤ −2) and reception stopping within a few coil-heights → **near-field coupling** (the expected, complete result; the coil is a short-range device). Shallow falloff (≥ −1) with reception at ≥ 10 coil-heights → **far-field / transmission-at-distance** (surprising; needs independent replication). No transfer at any distance → **refutes the coarse claim**. Untuned receiver, unrecorded distances, or a single session → **inconclusive, not a refutation**.
