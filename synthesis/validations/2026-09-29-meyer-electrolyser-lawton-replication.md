---
name: Meyer Electrolyser — Dave Lawton's Documented Replication of the Demonstration Cell (2006)
description: Dave Lawton built and ran a copy of Stanley Meyer's demonstration electrolyser — six concentric 316L stainless tube pairs in tap water with no electrolyte, driven by a gated pulsed waveform — and the write-up by Patrick J. Kelly reports a high rate of gas production and assesses the circuit at about 300% of the Faraday-implied maximum. A documented build with video evidence and no calibrated gas-versus-charge measurement.
---

# Validation — Lawton's Replication of Stanley Meyer's Demonstration Electrolyser

**Domain:** water electrolysis / anomalous gas yield (pulsed electrolysis)
**Recorded:** 2026-09-29 (Replication Seeder)

## What was claimed

**Stanley Meyer** claimed that a concentric-tube water cell driven by **pulsed DC at resonance**, using ordinary water with **no electrolyte**, produces a hydrogen–oxygen ("hydroxy") gas mixture at a rate far above what Faraday's law allows for the charge passed — and that this is a resonance phenomenon rather than ordinary electrolysis. The claim in the corpus is attached to Meyer's *demonstration* electrolyser (his bench cell), not to his production cell or to the vehicle.

## Who replicated it, when

**Dave Lawton** built and ran a copy of the demonstration cell. The build and its results are documented by **Patrick J. Kelly** in *A Practical Guide to 'Free Energy' Devices*, **Part D14 — "Replication of Stanley Meyer's Demonstration Electrolyser"** (first version 10 June 2006; last updated **3 October 2007**).

Video evidence is cited in the document: a video of Lawton's replication of the demonstration electrolyser, and a second video of the same cell running on the solid-state circuit rather than the alternator.

Note the shape of the source honestly: this is a **replication guide written by a third party describing a replicator's build**, published in a practical-compendium series — not a measurement paper by the replicator. It is a real named attempt with real construction detail; it is not a laboratory report.

## Method

**Cell.** Six pairs of concentric seamless **316L stainless-steel tubes**: outer tube 1 in diameter, inner tube 3/4 in, wall thickness 1/16 in, **5 in long** (the document notes Meyer's own tubes were about three times that length), giving an inter-tube gap of **1–2 mm**. Inner tubes are centred at each end by four rubber strips. The housing is made from two standard 4 in plastic drain coupler fittings solvent-cemented to each end of a cut acrylic tube — deliberately transparent, so the electrolysis can be watched. Electrical connection is by stainless bolts tapped into the tubes and run through the base, sealed with a bonding agent.

**Fuel.** Tap water or rainwater, **with no additives whatsoever**.

**Drive (two equivalent routes).**

1. *Alternator:* the field coil is switched on and off by an FET pulsed from a 555 timer, producing a composite waveform. The stator winding outputs are wired **positive pulses to two of the outer tubes, negative pulses to all six inner tubes** — the document says this is "copied directly from Stan Meyer's circuit diagram," and notes it is not obvious why Meyer drew it that way, since one would expect all six outer tubes in parallel.
2. *All solid-state:* two NE555 oscillators — the first with large capacitors producing slow pulses, **gating the second, higher-frequency oscillator on and off** — each with variable pulse rate and variable mark/space, output reduced by a 220 Ω / 820 Ω divider into a current-amplifying transistor driving a **BUZ350 MOSFET** (22 A rating), with a 1N4007 clamp protecting the drain. The document states the solid-state circuit alone produces about the same gas rate, and draws less current because no alternator drive motor has to be powered.

**Stated improvement:** two **bifilar-wound inductors** (100 turns each of 22 SWG / 21 AWG enamelled copper, wound side by side on a 9 mm × 25 mm ferrite rod or a toroid), introduced after the original build, which the document says raise operating efficiency further because "the inductors used by Stanley Meyer form a very important role[] in raising the operating efficiency still higher."

**Conditioning.** The document treats conditioning of the electrode tubes in tap water as "a very important part of the cell build," with a stated procedure (no resistance on the negative side of the supply during conditioning).

## Result

- **"An impressive rate of electrolysis using just tap water or rainwater with no additives whatsoever."** The document's photographs show the cell visibly filling with gas within seconds of switch-on.
- **The circuits "have been assessed as operating at about 300% of the Faraday assumed maximum efficiency."**
- **Current draw falls as tubes are added**, which the document presents as the interesting observation: about **1 A** with one tube installed; the second tube adds **less than 0.5 A**; the total is **under 2 A** at three tubes; the fourth and fifth add about **100 mA each**; the sixth "causes almost no increase in current at all." The document reads this as evidence the efficiency could be raised further with many more tubes, and suggests the tubes could be bundled.

## Confidence: low

The claim here is the **excess-gas** claim, and this record does not support it at any strength above "reported." Specifically:

1. **The ~300 % figure is asserted, not derived.** The document does not tabulate gas volume against charge passed, does not state the Faraday baseline it is comparing against, and does not show the arithmetic. A number that appears once, without a calculation attached, is a report.
2. **No calorimetry, no volumetric measurement, no uncertainty.** Nothing in the document allows a reader to reproduce the *number* — only the *build*.
3. **The boring explanation is not excluded, and must be named.** Apparent excess gas in pulsed electrolysis is the standard place where measurement goes wrong: water vapour and entrained mist carried off with the gas inflate apparent gas volume, and pulsed drive heats the liquid. **Measuring gas dry, at a known temperature and pressure, with a stated Faraday baseline for a stoichiometric H2/O2 mix, is the first thing any serious measurement must do — and it is exactly what this document does not do.**
4. **No independent measurement of this cell has been located in the corpus.** The evidence is one replicator's build plus video, reported by a third party.
5. A **positive** reading remains possible and is not dismissed: the falling current with added tubes is a real, reproducible-looking observation about the cell's electrical behaviour, and it is the kind of number that would survive a proper measurement either way.

## Safety — this is the least safe artifact in the Yard

The source document itself opens by stating that experimenting with hydrogen, or with a hydrogen–oxygen mixture, **"is highly dangerous and you do so entirely at your own risk."** It records two facts that matter more than any efficiency claim:

- Hydroxy gas ignites with a flame front roughly **1,000 times faster** than petroleum vapour, so **standard flashback arrestors do not work**.
- The protections it recommends are a **bubbler** between cell and any engine, a **pressure-activated switch** cutting power above about 5 psi, a tight push-fit (not clamped) bubbler lid so it can blow off, and — in a vehicle — an ignition-switched relay so the cell cannot run with the engine off.

Anyone contemplating this build should read those lines as the load-bearing part of the document, not the efficiency figure.

## Source

- `http://www.tuks.nl/pdf/Patents/Meyer/D14.pdf` — Patrick J. Kelly, *A Practical Guide to 'Free Energy' Devices*, Part D14, "Replication of Stanley Meyer's Demonstration Electrolyser," last updated 3rd October 2007. Read in full from the corpus copy (`pdftotext`); indexed in `search_chunks/alternative-energy-technologies.json` as record **id 37942** (source_site `tuks.nl`, the 2006-06-10 version).
- Mirrors in the corpus, which is how this document entered the archive twice: `http://jnaudin.free.fr/wfc/D14.pdf` and `http://www.jlnlab.com/wfc/D14.pdf` — records **id 2414009** and **id 2414450** in `search_chunks/alternative-energy-technologies.json`, source_site `jnaudin_free_fr` (the 2007-10-03 edition). Jean-Louis Naudin's `wfc/` directory is itself a long-running replication site for Meyer's cell.
- The referenced video of Lawton's replication was hosted at `icubenetwork.com/files/watercar/non-commercial/dave/videos/Wfcrep.WMV`; the non-alternator video at `www.panaceauniversity.org/WFCrep2.wmv`. Both are cited in the document; neither was fetched for this record.

## Related Yard artifacts

- `synthesis/replication/2026-09-29-dossier-052-meyer-resonant-water-electrolysis.md` — the protocol this record's claim needs. The dossier's results log opens with this Lawton entry.

## Honest framing

We hold no brief — the test is the point.
