---
name: Quest Card — Magnet Vortex Rotation Test: Does a Magnetic Field Twist a Suspended Body?
description: "Aetherforce-branded quest card testing the aether-vortex rotation claim — that the rotational component of a magnetic field exerts a twisting displacement on a suspended body, including a NON-magnetic one, and that a slight rotation persists after the current is switched off. The card hangs a light body on a nylon thread (a torsion pendulum) with a laser-and-mirror readout, drives a coil around it in both polarities, and measures the azimuthal deflection; the discriminators are a matched non-magnetic dummy, a sham coil, an air-current enclosure, and a logged ambient temperature. Energy domain (magnetism — the rotational component of a field); Power mirror (Electricity complement, 8th card)."
---

# ⚡ Aetherforce — Power

**Guild:** Aetherforce — Power
**Quest Line:** ⚡ Aetherforce · Electricity complement
**Tier:** straw
**Domain:** energy (magnetism — the rotational component of a magnetic field)
**Status:** proposed
**Created:** 2026-10-09

> **Authorship:** agent_id `agent-b73ac550-5671-471e-b3e1-721f948ea063` · agent_name `Tutor` · job `practicality-engine` · lineage `agent-b73ac550-5671-471e-b3e1-721f948ea063 -> practicality-engine -> 2026-10-09-magnet-vortex-rotation` · authored_at `2026-10-09` · *Authored by an AI agent. agent_id is the identity; the display name is for humans only.*

---

## Quest Card

```js
{
  type: "AETHER",
  biomes: ["suburb", "rural"],
  name: "Aetherforce — Power",
  desc: "A magnet's field lines look like they run straight from pole to pole. One account says that is the picture, not the thing: that the field line is really a thread of a swirling medium, that a magnet's motion is primarily a rotation, and that this rotation should twist a body hung so it can only turn — even a body that is not magnetic at all. The account is a Swiss physician's own experiment, self-published, and he says plainly that it needs re-checking: his first version would not reproduce reliably, and the second produced rotations of at most about 90 degrees that he admits could be artefacts of a field that is not quite uniform. What he also reports is the part worth testing: a slight rotation that stayed, in the same direction, for days after the current was switched off. This quest builds the instrument that can see it — a light body hung on a thin nylon thread with a laser and mirror to read its turning — measures the floor first (how much the pendulum drifts on its own, how much the coil's heat moves it, how much a draught moves it), and only then asks whether the field twists the body, whether the twist reverses with the field, and whether anything is left when the current is off. The ordinary outcome — that the turning is the coil's heat, or the draught, or the ordinary pull of a magnet on a magnet — is a complete result, and the card is built to reach it cleanly. ⚡ Aetherforce custom: does NOT count toward Permies badges (earn it here). Source: Aetherforce Knowledge Vault.",
  tier: "straw",
  quest: [
    "Magnet Vortex Rotation Test — Does a Magnetic Field Twist a Suspended Body?",
    "Hang a light non-magnetic body (a sand-filled glass bottle, about 400 g) on a thin nylon thread 1-3 m long so it can only rotate about the vertical axis, and read its turning with a small mirror on the thread and a laser pointer aimed at a screen at a measured distance. First measure the floor: with the coil off, record the rest position and the drift over 10 minutes; then with an identical sham coil carrying no current; then with the enclosure open. Now switch on a low-voltage coil around the body and record the laser spot's displacement and its direction, then reverse the coil polarity and record again. Repeat at least 10 times, alternating polarity, with the enclosure closed, logging the ambient temperature at every reading. Then switch off and record at fixed intervals for several days. Measurable outcome: the azimuthal deflection in millimetres of laser-spot movement at the recorded screen distance (converted to degrees), signed by direction (CW/CCW), for coil N-down, coil N-up, coil off (immediately and over days), the sham coil, the enclosure-open condition, and a matched non-magnetic dummy — each with the ambient temperature. Target: the deflection reverses sign with the coil polarity, the sham coil and the matched dummy show nothing comparable, the deflection does not track the temperature, and it survives with the enclosure closed. A deflection that sits inside the floor you measured first = the effect is not there at home scale, and that is the honest result the card expects.",
    ["Science", "Physics", "Engineering"],
    "🧲"
  ],
  source_doc: "translations/2026-10-09-magnetismus-und-aetherwirbel-seiler-de.md — full English translation of Hanspeter Seiler, Magnetismus und Aetherwirbel (NET-Journal 11(7/8), July/August 2006); scout record sources/2026-10-09-scout-b-langs-1.md (find #3) whose Practicality assessment flags it as reproducible",
  source_url: "https://focusingpulse.github.io/AFLinks",
  dossier: "living-library/synthesis/replication/2026-10-09-dossier-078-magnet-vortex-rotation.md",
  pass_fail: "PASS (claim supported at home scale): the deflection reverses sign with the coil polarity, AND the sham coil (no current) produces no comparable deflection, AND the deflection is reproducible across N >= 10 trials with the enclosure closed and does not track the ambient temperature, AND the current-off tendency is present over >= 3 days and differs from the no-coil baseline | REFUTED: the sham coil reproduces the deflection, OR the deflection tracks the ambient temperature, OR it disappears when the enclosure is closed, OR it does not reverse with polarity, OR the matched non-magnetic dummy reproduces the magnet-arm deflection | INCONCLUSIVE: the deflection is present but below the measured baseline drift, or the pendulum will not settle, or the readings scatter more than they separate | VOID: the thread is twisted or kinked at the start; the reading is taken before the pendulum settles; the laser spot is not on a fixed screen; the coil was driven from mains — a VOID is not a NULL",
  evidence: "Photo of the pre-registration sheet (the body and its mass, the thread length, the screen distance, the settle time, the scoring rule, N, the thermal log, the enclosure state) taken before the build + the raw laser-spot displacement readings in mm and degrees, signed by direction, for coil N-down, coil N-up, coil off, the sham coil, the enclosure-open condition, and the matched dummy + the 10-minute baseline drift with no current + the ambient-temperature log alongside every reading + photographs of the apparatus, the coil and its polarity (compass), the enclosure, and the matched dummy + the several-day current-off record + a one-paragraph verdict (supports / refutes / inconclusive) with the numbers and the floor comparison shown"
}
```

---

## Source Documentation

- **Primary (the archive translation):** `living-library/translations/2026-10-09-magnetismus-und-aetherwirbel-seiler-de.md` — the full English translation of **Hanspeter Seiler**, *Magnetismus und Aetherwirbel* (Magnetism and Aether Vortices), NET-Journal Vol. 11 No. 7/8, July/August 2006. Seiler (b. 1947, Chur) is a Swiss physician and vortex researcher; the article reports his 1993 magnet-in-water experiment and his 2006 torsion-pendulum series. Primary PDF: http://radialfeldhypothese.helmut-friedrich-krause.de/wp-content/uploads/2019/10/Seiler_Magnetismus-und-Aetherwirbel.pdf
- **The seed record:** `living-library/sources/2026-10-09-scout-b-langs-1.md` — Polyglot Scout B, 2026-10-09 (find #3). Its **Practicality assessment** is the filter, and it flags this record: *"describes a buildable apparatus (floating magnet, thermally shielded test body, current-pulse drive) and a stated control protocol; results are early-stage and explicitly call for replication."* ⚠ The record's own rights posture: the translation is **P0 — never publish**; the assessment is our own (P2).
- **The mainstream spine the card leans on:** the **Einstein–de Haas effect** (magnetising a ferromagnetic body rotates it — Einstein's own experiment) and the **Barnett effect** (rapid rotation magnetises a ferromagnetic body). Both are real, measured, and cited in the source itself; the card uses them as the ordinary mechanisms to exclude, not as the claim.
- **Replication Dossier:** `living-library/synthesis/replication/2026-10-09-dossier-078-magnet-vortex-rotation.md`
- **Vault:** https://focusingpulse.github.io/AFLinks — search "aether vortex", "Einstein-de Haas", "magnetism", "torsion", "Seiler"
- **Aetherforce Reference:** search "magnetism", "aether vortex", "Einstein-de Haas", or "radial field" on https://www.aetherforce.energy

---

## Rubric Justification

| Criterion | Assessment |
|-----------|------------|
| **Practical** | YES — a named apparatus (a torsion pendulum: a light body on a nylon thread, a low-voltage coil, a laser-and-mirror readout) with a named procedure (measure the floor, drive both polarities, log the temperature, run the controls) and a measurable outcome (the azimuthal deflection in degrees, signed by direction, per condition). Not pure theory. |
| **Replicable** | YES — home, ~$50-150; a nylon thread, a jar of sand, copper wire, a laser pointer, a mirror, a compass, insulating mat, a few magnets. No mains work, no lab. The source's own apparatus is described dimensionally. |
| **Relevant** | YES — Energy domain: the rotational component of a magnetic field, on the same axis as the queue's other non-conventional electromagnetism cards. It complements the Power guild, whose complement in the mirror map is the radiant / Tesla / LMD complement. |
| **Honest** | YES — framed as a TEST, not an endorsement. The card states plainly that the source is self-published and non-peer-reviewed, that the author himself calls for a critical re-examination, that his first experiment would not reproduce reliably, and that his rotations could be artefacts of a non-uniform field. It names the ordinary mechanisms (ordinary magnetic torque, the Einstein–de Haas effect, thermal drift, air currents, residual ferromagnetism) and requires the controls that separate them. Clean FAIL and VOID paths; the expected result is the null. |
| **Linked** | YES — the archive translation (with its scout record and card-eligible assessment), the primary PDF, the mainstream spine (Einstein–de Haas / Barnett), a pre-registered replication dossier, and the Vault + Aetherforce search pointers. |

**Mirror choice, stated:** the card's **domain is energy** (the rotation's next field), and its **guild complement is Power** — the Electricity guild, whose complement in the mirror map is *Radiant / Tesla / LMD*, i.e. non-conventional electromagnetism. This is its **8th card**. The alternative mirror was **Oddball** (*cross-field bridges / suppressed-science re-try candidates*), which is emptier (1 card) and is arguably a fit — the claim is a suppressed-science re-try that bridges magnetism and mechanics. Power was chosen instead for consistency with the queue's precedent: every prior non-conventional electromagnetism card (Scalar Field Detection, Mini Tesla Coil, Keppe Motor, Chiappini Antenna, Adams Motor, Bladeless Tesla Turbine) sits in the Electricity complement, and the card's endpoint is an electromagnetic effect. Under-promise noted: the card is emitted because the apparatus is buildable, the author asks for replication, and the endpoint is countable — not because the aether-vortex claim is believed.

---

## What makes it the queue's first of its kind

- **The first card on the Einstein–de Haas / Barnett lineage** — the coupling between magnetisation and macroscopic mechanical rotation. No prior card tests it.
- **The first card whose endpoint is a suspended body's rotation angle** — an azimuthal deflection of a torsion pendulum, rather than a weight (Spin-Weight Anomaly), a driven rotor's RPM (Adams Motor), an efficiency (Keppe Motor), or a field strength (EMF Bedroom Survey).
- **The first card whose claimed effect is claimed to persist with the drive removed** — Seiler's "constant slight CCW tendency … with the current switched off, and this over several days". Every prior card measures its effect with the apparatus running.
- **The first card that tests the same claimed effect on a NON-magnetic body** — the diamagnetic arm, which is the design's strongest discriminator: a sand-filled glass jar has no permanent magnetic moment, so if it turns the same way as the magnet, the ordinary magnetic-torque explanation is excluded.
- **The first card whose primary instrument is a torsion pendulum** — orders of magnitude more sensitive than a balance, and the first whose sensitivity is itself the principal hazard (it perceives air currents and thermal drift; the source says so).

---

## The honest framing (the spine of the card)

The card tests a claim, not a tradition. The aether-vortex lineage is not being asked to prove a mechanism — it is being asked what it says the field does to a suspended body, and the one part of that answer a family can establish at home is whether the body turns, which way, and whether anything is left when the current is off.

Four things the card keeps in front of the family:

1. **The source is self-published and asks to be re-checked.** Seiler's own closing line is *"a critical experimental and also theoretical re-examination of these promising results is now called for."* The card takes him at his word.
2. **The floor comes first.** A torsion pendulum perceives forces below any balance — which means it also perceives the coil's heat and the room's draughts. The card measures those first and refuses to call a deflection a result until it clears them.
3. **The ordinary mechanisms are named, not hidden.** The ordinary magnetic torque, the Einstein–de Haas effect, thermal drift, air currents and residual ferromagnetism are all written into the card, each with the control that separates it.
4. **A null is a complete result.** A deflection that sits inside the floor the family measured first means the effect is not there at home scale with this apparatus — a real, useful finding (Skeptic's Star), not a failed experiment.

**Under-promise, stated plainly:** the likely outcome is that the coil's heat and the room's draughts dominate, that the deflection either tracks the temperature or vanishes when the enclosure is closed, and that **nothing survives the controls.** That is the honest verdict, and the card is designed to reach it cleanly.

---

## Safety and rights notes

- **Safety: low.** The only electrical element is a low-voltage DC coil (a battery or a bench supply at a few volts) — **do not drive the coil from mains.** Keep the laser pointer below eye level and never point it at anyone. The pendulum is a hanging mass; hang it clear of walkways.
- **Rights posture:** the translation is a derivative work of a publicly posted self-published article and is **P0 — never publish.** The scout record and this card are our own analysis (**P2 — publishable**). The card **cites and links**; it reproduces only short attributed quotations.
