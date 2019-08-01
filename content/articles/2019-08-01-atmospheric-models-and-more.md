Title: Atmospheric models and more!
Date: 2019-08-01 21:00
Category: GSOC
Tags: GSOC, GSOC19, poliastro, twobody
slug: 2019-08-01-atmospheric-models-and-more
lang: en
Author: Jorge Martínez Garrido

## Tasks for this last period...

While checking the stability of the 0.13, GSOC continues and new bugs,
implementations, and others need to be solved for the 0.14. Most of them are
related to:

* New frame modeling, implementation, and testing.
* New plotting capabilities, such us two attractors in the same plot.
* New orbit creation methods.
* Start using non-dimensional units.
* Different bug solving.

Issues related to frames are the most tricky ones since working with them is
not so intuitive. Plotting capabilities are directly related to frames and
therefore no major improvements are done in this field without solving something
in the previous one.

## New atmospheric models

I have been trying to model and implement some famous atmospheric models for
poliastro. Drag is one of the main perturbations for LEO orbits. By making use
of Cowell's formulation we can integrate the acceleration caused by this force
which is directly proportional to air density. This implies that having a good
atmospheric model is critical since it determines the drag force.

Different models have been published along the years:

* U.S Standard Atmosphere 1962 and 1976
* Jacchia-Roberts 1971 and 1977
* Russian Ghost models 
* NRLMSISE-00

Each model assumes different atmospheric conditions and factors that affect the
temperature distribution, pressure and density among others. While U.S Standard
Atmospheres take the value of the gravity at 45[deg] latitude, Jacchia solves
it no matter the location in the globe. Furthermore, it also includes solar
radiation flux.

## Pericenter and units bug in poliastro.maneuver

Two different issues were found in the `poliastro.maneuver` module: one related
with the units and others with a time of flight of maneuvers.

On one hand, the issue related to the time to pericenter was that
poliastro propagated internally the orbit for both **Hohmann** and **Bielliptic** when
not at pericenter to solve for those maneuvers. The time it took the orbit for
being at pericenter was not taken into account and the user was not warned. This
problem was finally solved by adding this time in the Maneuver instance.

On the other hand, some strange behavior of `astropy.units` were causing that
conversions among units internally inside this module were not correct in some
cases. By forcing their simplification this was solved.
