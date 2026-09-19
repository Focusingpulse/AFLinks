---
name: "Planetary Antenna — D-Field Antenna (Spanish)"
description: "Full translation of Carlos Alejandro Chiappini's viXra paper on the Planetary Antenna (El Proton) — a buildable 2m-band VHF antenna designed from electric displacement (D) field theory, with complete construction steps and theory appendix."
---

Planetary Antenna
Author: Carlos Alejandro Chiappini

Abstract

This document describes an antenna operating in the VHF amateur radio band, spanning 144 MHz to 148 MHz.

Although the geometric shape is reminiscent of the eggbeater antenna, the operating principle is different. The design of the planetary antenna is the result of taking full account of the physical laws referring to the field D⃗, called electric displacement. This makes it possible to achieve a small antenna that exhibits good performance.

The prototype began as a very low-cost experiment, intended to put to the test, in practice, the results of a theoretical development concerning the properties of the D⃗ field.

Probably very few radio amateurs will take an interest in the theoretical aspect of the design. That is no obstacle to their enjoying the construction of something new that works well.

Acknowledgments

I thank my brother Héctor Hugo Chiappini for stimulating, since my childhood, my fascination with physics and with radiocommunications. Added to this is his gift of radio equipment and materials, which I am now putting to use. To this is added the moral support, indispensable for continuing.

I thank the people of the Radio Club Quilmes for placing at my disposal technical knowledge, hands-on practice with equipment and instruments, patience to teach me what was necessary, offering constant and inexhaustible help. I also thank them for the excellence of the preparatory course for the amateur radio license, which in addition to teaching rules and knowledge manages to kindle enthusiasm, love, and responsibility in the practice of amateur radio.

I thank the colleagues who, giving me their best, resemble my brother closely and know how to earn the marvelous title of friends.

I thank my father, Carlo Chiappini, for devoting much time and much patience to my education in childhood and youth, in the ethical, social, community, family, musical, and intellectual aspects. Though he has passed away, he left his spirit present.

I thank every woman who has bettered some stage of my life, in whatever role fell to her. They are like the air, which cannot be seen with the eyes. We perceive it by an aroma, by the caress of a breeze, by the force of the wind, or simply because, were it missing, it would be impossible to keep breathing.

1
Planetary Antenna
        The Proton

Part 1 — Presentation, photographs, and materials


---


(1-a) What will we cover?
     Subject: Compact antenna
     Band: 144 MHz to 148 MHz (the Argentine 2m amateur radio band)
     Type: Made up of meridians and an equator (hence the name "planetary")
     Task: To recount the origin and present the design
     Contents of the document: Description, measurements, a guide for home construction, and an appendix devoted to the physical laws that gave rise to the design

Why is "The Proton" the preferred name among my close group of colleagues? Three days after the first trial I sent a photo of the antenna to LU7DTC, Ariel Visciglio, a colleague at the Radio Club Quilmes. The immediate reply was "haha, it looks like a proton." It was a lighthearted, hilarious moment, which lives on in the antenna's familiar name.

(1-b) Photographs

2
The radiating wire is continuous, with no cuts. It has simply been shaped to form 4 meridians and the equator, in resemblance to the geometry of a planet. One pair of meridians lies in one plane, and the other pair in a plane perpendicular to the first. The antenna mounts directly onto a PL259-type connector, because its 52 mm diameter allows this.

3
Are the photographs enough to build the antenna? The answer is no, and I guarantee that answer. I add the following. By reading the instructions minutely and calmly, it is also possible to build it poorly. Before carrying out each step we need to understand how, why, and in what manner to do it. Can a structure this simple be very sensitive to small errors? Yes, I attest to it.

(1-c) Necessary materials

63 cm of messenger wire — the kind we see attached to the 75 Ω coaxial cable used by cable-TV companies, since it has suitable cross-section and stiffness. That coaxial cable is abundant, abandoned in the street.

1 male PL259 connector

Something to fasten the crossing points of the wire structure. In my case I used twine and a glue gun with silicon sticks.

A millimeter-graduated ruler to mark on the wire the segments corresponding to meridians, half-meridians, and the equator. I used a steel ruler 50 cm long.

Something to make visible marks on the wire delimiting the segments, so they can be shaped without error. In my case I used white electrical tape, and on it I made each mark with a thin-tipped indelible black marker.

Pliers

Long-nose pliers (the kind with long, thin arms)

Electrician's pliers (normal arms)

4
     Electric soldering iron (between 35 and 45 watts is fine)
     Radio solder (60/40 is sufficient quality for this task)

Part 2 — Construction

AVOID RISK


---


This document does not exhibit SWR measurements. Before testing the antenna on
        transmit, measure the SWR across the corresponding band (144 MHz to 148 MHz in the
        case of the amateur band). When the SWR approaches or exceeds 2, the equipment is in
        danger, and the advisable course is not to test on transmit. Reception testing can be
        done, taking great care to avoid accidentally keying the transmitter. Remember that
        the SWR value depends on nearly everything: on where the antenna is when you take
        the measurement, on everything in the surroundings, on being near or far from
        walls, roofs, chimneys, on being inside a building or outside, on pointing the
        antenna up, down, tilted, and on everything you can add to the list. Test in
        different situations and conditions. If the SWR proves inadequate in every case,
        discard the antenna.

In my case the risk is minimized because I set the equipment to 1 W of RF output. Even if
the output power were totally reflected (SWR too high), 1 W is not enough to damage the
equipment's components. I use a Baofeng UV-5R handheld, a cheap set compared with more
elaborate ones. The SWR measurement was made by someone who works at a company, without
my being present. That is why I prefer that you take charge of this matter personally, if
you build the antenna. But how can I decide to build it without performance data or SWR
data? I have personally verified the performance. On transmit it is good. The antenna
installed 5 m above ground, connected to the Baofeng UV-5R at 1 W RF output, achieves,
in the middle of the city, 25 km of range. In the 1 W case, the other station (25 km away
in a straight line) knows that someone is modulating, understands very few words through
the noise, without understanding the complete message. With 5 W they understand the whole
message, though a little noise accompanies the modulation. Within a 15 km straight-line
radius the other station receives very little noise, and less and less as the distance
shrinks. Within a 10 km straight-line radius one can operate at 1 W with no noise.
Antennas with excessive SWR usually perform very poorly. This gives grounds to trust the
measurements made by the man at the company, which yielded reassuring results.

(2-a) Preparing the wire

5
The total radiating length is 49 cm. Ah, a quarter wave! Absolutely not. The
measurement comes from another method, based on the analysis of the electric displacement
vector. At the end of the document there is an appendix explaining it.

In the previous image we see a violet zone, symbolizing an omitted part. The omission
makes it possible to show the 49 cm region in more detail. There are also marks made with
white electrical tape, seen better in the following image.

The first mark indicates 4.1 cm, the measure of a half-meridian.

The second indicates 8.2 cm, the measure of a full meridian.


---


The third indicates 16.3 cm, the measure of the equator.
After marking the ruler, the next step is to mark the wire. To work comfortably, we take
63 cm of wire. The connector will go on one of the ends. So we place the first mark 10 cm
from that end, leaving a generous segment that makes fitting the connector easy.

The second mark sits 4.1 cm (41 mm) from the first and indicates a half-meridian.
The third sits 16.3 cm (163 mm) from the second, indicating the equator's measure.
The fourth sits 4.1 cm from the third, indicating a half-meridian.
The fifth sits 8.2 cm (82 mm) from the third, indicating a full meridian.
The sixth sits 8.2 cm from the fifth (full meridian).
The seventh sits 8.2 cm from the sixth (full meridian).
After the seventh we leave an excess of wire, because we may need it to
optimize resonance at the center of the band. In theory the excess would be
unnecessary if every detail of the construction came out perfect. In practice
imperfection is very likely, and a small excess after the fourth meridian can
compensate for errors. If the excess is needed, it is best to give all the
meridians their normal measure. The fourth ends at the south pole, where it must
arrive at normal measure and be fastened at the point where the normal-measure
mark is. The excess will emerge from the south pole, as a plant's stem emerges
from the soil. The inclination of the little piece of excess wire is important.
We can bring it near the connector's neck or move it away. By varying the length
and the inclination of the excess we will seek to optimize performance.

6
The greatest excess I ever needed was 9 millimeters, but I always leave more and then trim it
little by little, checking how performance improves. Once, when I managed to respect the spherical
geometry and the measurements well, an excess of less than a millimeter was sufficient. In pure
theory the excess is unnecessary and harmful, because the theory is formulated assuming the
measurements and the shape are absolutely perfect. In practice, the wire's cross-section is not
zero, and that makes geometric perfection impossible. Hand construction adds another share of
imperfection. For that reason, a small excess can optimize performance.

(2-b) Construction steps

Step A: Make a half-meridian

The segment from the wire's end to the first mark is left for fitting the
connector later. Between the first and second marks there are 4.1 cm. With
those 4.1 cm we make half of meridian 1, that is, a quarter of a circle. What
would the diameter of the full circle be? It would be 5.2 cm. To make the task
easier we can use as an aid some cylindrical object 5 cm in diameter, serving
as a form for bending the wire into the required shape. The closer everything
comes to perfection, the less excess we will need and the better the antenna
will work.

Step B: Make the equator

The segment from the second mark to the third measures 16.3 cm and is used for
the equator.

7


---


7
I will describe my way of proceeding. I hold the connector segment vertical, with its
end pointing down, as the figure indicates. The half-meridian stays above that segment.
The equator starts at the highest point of the half-meridian, makes a full circle, and
returns to the starting point. The arrows in the drawing indicate the direction chosen
for going around the circle. Let us remember it well, because the set of four meridians
must be coherent with that direction. You may choose either direction you wish for the
equator, provided you then build the meridians coherently. When we describe the
construction of the last three meridians we will explain the coherence.

Step C: The other half of the first meridian

The equator begins and ends at the same point, and that is the point where we will
begin the second half of the first meridian.

Step D: Make meridian 2

8
Meridian 2 begins at the point where meridian 1 ends. That point is, in the
drawing, the north pole of our little planet.

Meridian 1 lies in a plane perpendicular to the plane of the equator. Meridian
2 lies in a plane perpendicular to the plane of meridian 1 and perpendicular to
the plane of the equator. Let us imagine an ant walking along the equator. If
the walk starts at meridian 1, the shortest path to meridian 2 is achieved in
the direction indicated by the equator's arrows. This is the guide for building
the meridians coherently with the equator. Each meridian we build must move away
from the previous one following the direction we chose for building the equator.

To build meridian 2 we use the wire segment between the fourth and fifth
marks. That segment measures 8.2 cm. To shape the wire we can use the same
cylindrical object as before.

Step E: Make meridians 3 and 4

This time we will not repeat the figures. The verbal description is sufficient.

Meridian 3 runs from the south pole to the north pole. Its plane is
perpendicular to the plane of the equator and to the plane of meridian 2. It
moves away from meridian 2 in the direction indicated by the equator's arrows.
To build it we use the wire segment between the fifth and sixth marks. That
segment measures 8.2 cm.

Meridian 4 runs from the north pole to the south pole. Its plane is
perpendicular to the plane of the equator and to the plane of meridian 3. It
moves away from meridian 3 in the direction indicated by the equator's arrows.
To build it we use the wire segment between the sixth and seventh marks. That
segment measures 8.2 cm. In theory we should cut the wire at the seventh mark,
where meridian 4 ends. In practice, remember to leave some excess.

We can shape meridians 3 and 4 using the cylindrical object mentioned before.

Step F: Fit the PL259 connector

The proper separation between the south pole and the connector's starting point
is 8.3 mm. The appendix explains this detail.

9


---


Step G: Find the best tuning for the center of the band. The excess may or may not be
necessary. If you have achieved measurements and geometry without errors, or with minimal
errors, you will not need to leave an excess and can cut the wire exactly at the south
pole. Otherwise, leave an excess and then reduce it little by little, millimeter by
millimeter. How much excess should we start with? As I related at the start of the
document, I have never needed more than 9 millimeters of excess. And as you can see in the
photographs, my manual skill is not great. Start with a centimeter and a half of excess if
your manual skill does not exceed mine. If it does, start with less, to minimize the
number of performance tests you will make before optimizing the tuning. Every millimeter
you trim calls for a test. As stated at the beginning of the document, the position of the
excess is also very important and requires checking performance. I suggest trimming
millimeter by millimeter, though in fact it is enough to trim a few tenths of a
millimeter, one or two at times, to change performance. A truly good tuning requires
great patience, trimming tenths of a millimeter and seeking, with great delicacy, the
optimum position of the excess.

I have surely not managed to document all the details I learned building several
protons. I suppose I have documented the basics, so that you can add your own good
judgment and skill until you obtain the expected result.

Part 3 — Appendix

(3-a) Separation between the south pole and the connector

My criterion in the proton's design is to use measures from the s series (s1, s2, etc.).
The measure s3 is 8.3 mm, acceptable as the separation between the south pole and the
connector.
                                        λ
                               s3 = ---------- = 8.278 mm ≈ 8.3 mm                (1)
                                      (2π)³

(3-b) Before the proton

For a long time, even before I held an amateur radio license, I had been interested in
the analysis of the electric displacement vector, symbolized D⃗. James Clerk Maxwell,
illustrious scientist of electrodynamics, needed in his research to recognize the
relevance of electric displacement in order to formulate the theory in a complete,
coherent, and consistent form. Without including D⃗ and minutely analyzing its
properties, that formulation would have been impossible.

It always struck me as inexplicable (and suspicious) that the teaching of
electromagnetic propagation, in classrooms and in the literature, omits an adequate
analysis of the D⃗ field when the wave propagates in vacuum.

That way of teaching never satisfied me, and when I had the chance, I devoted time and
effort to the analysis of the D⃗ field in the simplest case of propagation in vacuum.
That analysis yielded theorems that no one had taught me in classrooms and that the
literature does not contain. No literature, of any era and from any source, contains
them. Those


---


10
theorems lead from Maxwell's equations to topics of advanced physics, with the corresponding
mathematical formulations and concrete results. There appears, directly, a branch of physics
that is taught neither in classrooms nor in the literature.

The theorems concerning electromagnetic propagation in vacuum contain a relevant term,
equal to the wavelength λ divided by 2π. The wave equation taught in classrooms contains
the inverse of that term, called the propagation constant k, equal to 2π divided by λ. Let
us look at the electric wave equation, in its complete form, for the simplest case of
propagation in vacuum.

D = D̂ e^{i(ωt − kx)}                                        (2)
In classrooms the complete form is not taught. The following incomplete form is taught.

E = Ê sin(ωt − kx)                                        (3)
In the complete form, the polarization of the vacuum is evident whenever an
electromagnetic wave propagates in that medium, of whatever frequency and power. The
faintest, lowest-frequency wave that can exist is likewise accompanied by the
polarization of the vacuum. This detail is not contemplated in public teaching. Without
including it, it is impossible to understand and properly formulate fundamental phenomena.
You can find an analysis of these phenomena in the document titled "James Clerk Maxwell:
Forbidden Knowledge," available at the following links.

http://www.vixra.org/abs/1711.0313
http://www.monografias.com/docs115/james-clerk-maxwell-conocimiento-prohibido/
james-clerk-maxwell-conocimiento-prohibido.shtml
The second link is very long and therefore spans two lines, but it must be used without an
intervening break.

In all developments based on the complete form, the term s1 given by the following
formula is relevant.
                                                         λ
                                                 s1 = ------                         (4)
                                                        2π

The development shows that, in vacuum, the simplest electromagnetic wave consists of a
set of cylinders constituted exclusively of electromagnetic field. The length of the
individual cylinder equals λ and the diameter equals s1. This term is relevant from the
simplest wave propagating in vacuum up to the constitution of elementary particles, such
as the electron, the proton, the neutron, and their respective antiparticles. It is the
term that everything analyzed has in common. It is impossible to suppress the itch to
build some antenna based on the measure s1. Thus began my activity of building
experimental antennas and testing them.


---


11
The photograph shows some designs predating the proton. Starting from the top, the
first antenna is a tube with a wire inside. The tube's length is s, the same as the length
of the conductor inside. From the start it showed very good performance, with an
in-city range of 18 km at 5 W and good reception quality for the other station.

The second antenna down is the result of learning in practice that s is the universal key
at every level, from the largest to the smallest. I set out to start with an antenna of
measure s1, because it appears immediately in the mathematical development. The smaller
measures are not evident at first sight. To find them we need to go over the whole
development, with the intention of understanding in much greater detail why s1 is the
diameter of the elementary radiation cylinder in vacuum. In the cylinder there are two
resonant measures: one is λ and the other is s1. The measure λ resonates with the E⃗ and
B⃗ fields. The measure λ/2π resonates with the polarization of the vacuum and, for that
reason, resonates directly with space. In relativistic terms, it is correct to say it
resonates with spacetime.

Do the electrodynamic laws permit dividing by 2π only once, or do they permit doing it
more times — perhaps infinitely many times — always obtaining good performance? Answering
this question in purely mathematical form is a task beyond my abilities. So I decided to
build antennas following that order, that is, dividing λ by 2π more than once.

Dividing λ twice by 2π is dividing by (2π)². That is why my second experiment was to
build antennas of measure s2, given by the following formula.
                                                   λ
                                           s2 = -----------                    (5)
                                                (2π)²
Starting from the top, the second antenna seen in the photograph is a cube with edge
equal to s2. As happens with the proton, the radiating element has no cuts and runs along
the edges, as it runs along the meridians and the equator in the proton. In the cubic
antenna the radiating wire is not connected directly to the equipment. There is an
intermediate transducer, but the similarities with the proton are many and essential. On
a night with favorable propagation, the cubic antenna at 1 W was heard at 34 km in a
straight line, very noisily.


---


12
At 5 W there was

12
background noise, but the modulation was fully understood. The QSO took place between my
QTH in Quilmes and a recreation ground on Route 5, on the border between Ezeiza and
Esteban Echeverría. The colleague on the other end had his Ringo antenna installed 50
centimeters above ground, beside his car. This practical experience answered that question
I am incapable of answering in purely mathematical form. The measure s2, applied to a
suitable geometry, offers the same performance as the measure s1. And that performance is
not inferior to that of traditional antennas.

The transducer is a sheathed wire of measure s1, wound on a size-8 iron rod of measure s2.
It is the same wire we use in the proton. Those measures resonate at the band-center
frequency, 146 MHz. What is the advantage of using such a transducer? The SWR stays very
low across the whole band, and the energy transfer through the transducer is very good.
Remember that at 1 W, the cubic antenna's emission was received 34 km away in a straight
line.

Dividing by 2π more times we obtain the measures s3, s4, s5, and so on. Judging by what
happened with s2, one understands that all of them, used in a suitable geometry, yield good
performance. In theory one can imagine a set of infinitely many antennas: one of measure
s1, another of measure s2, another of s3, and all the others up to sn, with n → ∞. That
set of infinitely many antennas, placed one after another, is equivalent to an antenna
slightly longer than the measure s1. The sum is not large, because each antenna is 2π
times shorter than the previous one. For 146 MHz, the first measures 32.7 cm, the second
5.2 cm, the third 8.3 mm, the fourth 1.31 mm, the fifth 2.1 tenths of a millimeter, and so
each antenna contributes less to the total length. In mathematics we say the series is
convergent, that is, it ends up giving a definite finite value. That value is computed
with the following formula.
                     s1 + s2 + s3 + s4 + s5 + (…) = Σ_{i=1}^{i=n} λ/(2π)^i  with n → ∞ = λ/(2π − 1)      (6)

For 146 MHz formula (6) gives 38.85 cm — that is, 6.15 cm more than s1. The antenna at the
bottom of the photograph has measure sn, that is, it measures 38.85 cm. Its performance is
slightly better than the s1 tube.


---


The third antenna from the top is a tube of measure s2 — that is, 5.2 cm — with a coil of
very low inductance attached to the end. Zero inductance would be optimal, but that cannot
be achieved in practice. So we settle for the lowest inductance we can manage. Let us
review a basic concept. When the inductance is very high, a small current circulating in the
coil produces an intense magnetic field. When the inductance is very low, a very large
current circulating in the coil produces a weak magnetic field.

Now let us remember that all electrodynamic phenomena are reversible. Alternating current
belongs to electrodynamics. Radio frequency is alternating current that, instead of
operating at 50 Hz, operates at a much higher frequency. This means radio frequency is of
the electrodynamic type and its phenomena are reversible. The coil produces an alternating
magnetic field when alternating current circulates through it. This is reversible: that
is, the coil delivers current to a load connected across its ends when an alternating
magnetic field is present in the surroundings. In this type of antenna, the radiation
concentrates more at the tube's end than elsewhere. This means the RF magnetic field is
intense there. A low-inductance coil attached to that end will deliver good current to a
load. If the load is the radiating wire inside the tube, we obtain

13
positive feedback and increase the antenna's performance. This antenna achieves the same
performance as the 32.7 cm tube and as the cubic antenna with 5.2 cm edges. The
low-inductance coil is tuned to the band-center frequency.

(3-c) How did the proton idea arise?

All the antennas predating the proton worked well, but geometrically they do not have a
very symmetrical design. Is a symmetrical design good for anything? In principle, yes,
because with more symmetry we achieve more omnidirectivity. And in vector terms, the best
symmetry minimizes reactive power, maximizing active power. In radio vocabulary, this
means minimizing SWR.

It is impossible to trace all the edges of a cube with one uncut wire without overlapping.
A theorem of topology shows that, without cuts or overlaps, we can trace at most 9 of the 12
edges the cube has. Although this produces no global asymmetry, it causes partial
asymmetries in the emission. Is there any shape that produces neither global asymmetry nor
partial asymmetries? Meditating on it, we convince ourselves of the following. To achieve
that we need spherical symmetry. Instead of edges we will have meridians and an equator.
How many meridians? If we want the meridians and the equator to lie in mutually
perpendicular planes, like orthogonal Cartesian coordinates, we will use 4 meridians. In
electromagnetism, mutually perpendicular planes minimize harmful interactions. That is how
we arrive at the proton's shape.


---


The measure s1 is indispensable, because it appears in all the essential equations
referring to the D⃗ field. The first version of the proton had no equator. For that reason
I distributed the measure s1 among the 4 meridians. That gave good performance when I built
it, but it did not outperform the 38.85 cm tube. This result sows doubts, because the 4
meridians have more geometric symmetry than the tube. Why don't they perform better? I
spent nearly two years testing the equatorless proton, sometimes making it a bit oval,
other times a bit flatter than the perfect sphere, and so on. None of those attempts
outperformed the 38.85 cm tube.

After two years I reasoned that the RF energy from the equipment travels through the
meridians one by one. It enters the first, then the second, then the third, then the
fourth. So, in net terms, the energy follows an equatorial forward path. That is
virtually equivalent to a current running around the equator. What would happen if,
instead of using 32.7 cm of wire, we used more, so as to also build the equator and have
RF circulating in it? Logically, the RF must run around the equator in the same direction
as the energy's movement through the meridians. That is why the construction steps
emphasize that detail.

Adding the equator, the wire used will measure more than 32.7 cm. How much more? The
equator uses as much wire as two meridians, because the geometry is spherical. One
meridian takes 8.2 cm of wire. Double is 16.4 cm. In total we will use 32.7 cm + 16.4 cm
= 49.1 cm. This is very close to the 49 cm used in ordinary quarter-wave antennas. In
mathematical terms, the wavelength in vacuum for 146 MHz is 2.053 m, and a quarter of that
length is 51.32 cm, not 49 cm. It is said that the atmosphere does not behave like
vacuum, and that is why the radiating element must be 5 percent shorter than the
wavelength in vacuum. I wanted to find the theoretical origin of that rule, and nobody
knows it, nor could I find literature explaining it. It is an empirical rule.


---


14
So I decided to apply to the radiating wire the same theorems that determine the
properties of the elementary radiation cylinder and the properties of particles. Those
theorems contain a dimensionless term, symbolized γ, whose value equals the electron
charge qe divided by the charge Qo corresponding to a half-cycle of the elementary
radiation cylinder.
                                         √
                             qe    −3 + 13
                        γ = ------ = ---------- = 0.302775637731994646…             (7)
                             Qo        2

Working out the elementary energy balance we arrive, for a full wave, at a radiating wire
length 4.58 percent shorter than the wavelength in vacuum. This has nothing to do with
the atmosphere's behavior. It relates to the displacement wave D that forms inside the
radiating wire. The energy Wm of this wave's magnetic field belongs to the oscillatory
motion of the particles. If this energy were radiated, oscillation would be impossible
and there would be no radio frequency. The energy of this oscillation is given by the
following formula.
                                                ( 1 · qe/Qo )²
                                       Wm = ------------------ WTX                    (8)
                                               2
Wm → oscillation energy of the particles
WTX → energy delivered by the transmitter

Doing the calculations, the following results.

radiating length for a full wave = 1.96 m                        (9)

radiating length for 1/4 wave = 48.97 cm                        (10)

This matches the 49 cm of the empirical quarter-wave rule very well. And it comes very
close to the 49.1 cm of the perfectly spherical geometry mentioned earlier.
Consequently it comes very close to the energy balance given by the laws of physics. But
something close is not exact. If we want precision, we need a radiating wire whose total
length equals 48.97 cm, the value given by the laws of physics. This value corresponds to
the physical separation between a node and the nearest crest of the wave established
inside the radiating wire. To the extent we depart from those 48.97 cm, performance
decreases. If the total must be 48.97 cm and we use 32.7 cm for the meridians, how much
wire is left for the equator?

equator length = 48.97 cm − 32.7 cm = 16.27 cm                    (11)
That is why the construction steps allot 16.3 cm to the equator, instead of the 16.4 cm
measured by the equator of the perfect sphere. The proton departs very slightly from
spherical geometry, to optimize resonance at the center of the band.

(3-d) A useful criterion in experimental development


---


Every time a radio amateur saw one of the experimental antennas, they immediately asked
the following: Did you measure the SWR? How much SWR does it have? My answer was that I
had not measured it. So it went for three years. Those years would have been more than
enough to save up the money a

15
SWR meter costs. I never did it, because for studying new antennas, SWR measurement is a
mental prison. A well-directed design can give, in the precariousness of the first
attempts, an unacceptable SWR value. That does not mean we should abandon the study of
that design. It only means we need to revisit details to improve it. The obsession with
obtaining SWR values near 1 can undermine the freedom to try something interesting.

When I built the proton as the steps of this document indicate, its performance far
exceeded what was obtained with the 38.85 cm tube. To verify that this result was not
chance, I built more protons in the same form, and all performed to the same level.
Evidently I had arrived at a stable design, which always gives the same result when the
same construction standards are respected. And that result outperforms all the previous
ones. The laws of physics are fulfilled in the proton's design. After three years of
effort, I accepted the proton with equator as an adequate design. I then installed it on
the roof of my house, 5 m above ground. The coaxial feedline measures 45 m long. It is a
low-loss cable, but 45 m produces significant attenuation. That is no obstacle to
obtaining good reports when working repeaters and direct, always using 1 W.

After quite a few months of simply using the proton to chat with colleagues, the design's
stability stood proven. I then asked a friend who works at a radio laboratory to measure
the proton's SWR. They are encouraging measurements. I do not include them in this
document, so that you take your own before connecting the antenna to your equipment. That
serves to prevent risks.

—————————————————————————————

I am Carlos Alejandro Chiappini, sole author of the design of the Planetary Antenna,
familiarly called The Proton. I hold an amateur radio license issued by ENACOM in
Argentina, with callsign LW9DDD. My email is lw9ddd@gmail.com. My cell phone is
1151537099 and it has no WhatsApp. Always QRV. 73!

16


---

