Title: Impulsive 3D maneuvers have been validated!
Date: 2021-02-17 09:30
Category: NumFOCUS grants
Tags: NumFOCUS, maneuvers, orekit, GMAT
slug: 2021-02-17-validation-of-3dmaneuvers
lang: en
Author: Jorge Martínez Garrido

As part of the NumFOCUS small development grants, the
[poliastro/validation](https://github.com/poliastro/validation) repository has
increased its activity in order to reach its main goal: validate poliastro's
most complex features against similar software.

One of those features are impulsive maneuvers (Hohmann and Bi-elliptic) when
applied to non-equatorial orbits. The absence of numerical results in literature
and similar sources, made impossible to test associated pieces of code to
impulsive maneuvers for orbits with inclination and spacecraft not placed in
periapsis. However, this situation has changed, as they are now validated
against Orekit and GMAT.

![Bi-elliptic transfer in GMAT]({static}/images/poliastro_bielliptic.png)
![Bi-elliptic transfer in GMAT]({static}/images/gmat_bielliptic.png)

You can see corresponding pull-request for [Hohmann
validation](https://github.com/poliastro/validation/pull/18) and [Bi-elliptic
validation](https://github.com/poliastro/validation/pull/20). Not only that, a
continuous integration tool has been setup. This ensures that if any bug is
introduced within main poliastro source code, we can detect it and fix it
without any problem.

One interesting thing is that code making use of poliastro API is shorter than
that one based in Orekit or GMAT. This is important from the point of view of
readable code and simplicity. However, let us not forget that both Orekit and
GMAT provide amazing capabilities, so this might be a reason behind more lines
of code when using their APIs.

In addition to previous implementations, having a look at other similar software
has given us some ideas about future features of poliastro. For example, we
thought about the possibility of expanding our events detectors in order to
locate in time special situations such us when spacecraft will be under umbra
(eclipse) or when it will be visible over the horizon for a particular
topocentric location.

The idea is now to keep validating more code, in this case the one associated
with planetary reference frames and their conversions between them. This is a
major topic within the actual state of poliastro, as it is not easy at all to
check if conversions are properly performed.

Stay tuned for more about the validation work we are carrying out!
