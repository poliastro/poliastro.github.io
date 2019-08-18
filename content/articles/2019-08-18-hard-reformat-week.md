Title: Hard reformat week
Date: 2019-08-18 17:30
Category: GSOC
Tags: GSOC, GSOC19, poliastro, atmosphere, bodies
slug: 2019-08-16-hard-reformat-week
lang: en
Author: Jorge Martínez Garrido

## Reformat on poliastro.atmosphere

After implementing the `COESA62` and `COESA76` models in
[#738](https://github.com/poliastro/poliastro/pull/738) I was not completly
happy because of lots of data and coefficients at the beginning of each script.
Therefore and after asking Juanlu, it was finally decided to move all those
numbers to text files under the `*.dat` extension.

Furthermore, I decided not only to do that but also to completely reformat the
`poliastro.atmosphere` module:

* `base.py`: holds different mother classes for atmospheric models.
* `coesa62.py`: U.S Standard Atmosphere 1962 model.
* `coesa76.py`: U.S Standard Atmosphere 1976 model.
* `util.py`: contains atmospheric utilities.

Documentation was also added together with a notebook to better see not only how
these objects work but their differences in output results. In the following
image properties for COESA76 against geometrical altitude are plotted:

![COESA76]({static}/images/atm76.png)

## Reformat on poliastro.bodies

While working on the previous module, Eleftheria completed
[#746](https://github.com/poliastro/poliastro/pull/746) and was merged. This
allowed me to start working on Sun-synchronous orbits for any Solar System body
since sidereal times were added. However, a small bug was introduced, since
inheritance was not properly structured. Taking advantage of this, Juanlu
decided to reformat `poliastro.bodies`, `poliastro.coordinates` and
`poliastro.frames`. 

Previous changes can be checked at
[#763](https://github.com/poliastro/poliastro/pull/763). Since this is a
"critical" issue, I am redirecting all my efforts towards it to check and
adapt different modules and tests that depend on previous ones.

## Last evaluations and code submissions

Previous issue and associated ones may lead to a delay for SS0 orbits to be
merged. Any work produced after August 26th will not be taken into account,
however, it does not mean to stop contributing to `poliastro`.

Lots of things still need to be done for the 0.14 version such as:

* Pass `frames` in `StaticOrbitPlotter`.
* Properly define SS barycenter and EM barycenter.
* Test cases against Orekit, GMAT...
* Implement new orbit creation methods.

Most of them require deep analysis since, again, they are critical issues.

But even if GSOC ends I will be still contributing to `poliastro` for sure. It
is not only the number of thigns I have learned since I enjoyed the project but
the people involved in it.
