Title: New features after GSOC19
Date: 2019-08-20 22:00
Category: GSOC
Tags: GSOC, GSOC19, poliastro
slug: 2019-08-20-new-features-after-gsoc19
lang: en
Author: Jorge Martínez Garrido

GSOC 2019 Edition has almost finished. All along this last three months lots of
issues where solved, `poliastro 0.13` was raised, new features were applied and
of course, new issues and bugs appeared.

The objective of this post is just to collect all the implementations that have
been merged during this GSOC and also those that are still required to be done.

## ALREADY IMPLEMENTED

- [x] Lambert minor issues were fixed.
- [x] Lambert as Maneuver instances.
- [x] Docs and notebook on previous implementations.
- [x] Trail plotting option.
- [x] Fix minor issues on CI and tests.
- [x] New twobody propagators.
- [x] Maneuver fixes: Hohmann time to pericenter and units bug.
- [x] Atmospheric models: COESA62 and COESA76.

A detailed description and link to the code can be found in the following lines.

### Izzo Algorithm minor errors

Some errors appeared in the minimum transfer time for the Izzo algorithm. After
a little bit of debugging, Juanlu found that `time-of-flight equation that does
not need external computation of one of the terms`. I was asked to write some
unit tests.

<center>
**[Link to the corresponding pull request](https://github.com/poliastro/poliastro/pull/709)**
</center>

### Lambert becomes Maneuver

After the logic in Izzo's algorithm was fixed it was time to create a
`Maneuver.lambert(ss_origin, ss_final)`. Finally, a really simple and powerful
implementation was achieved!

```python
LAUNCH = Time.now()
ARRIVAL = LAUNCH + 600 * u.day

ss_earth = Orbit.from_body_ephem(Earth, epoch=LAUNCH)
ss_mars = Orbit.from_body_ephem(Mars, epoch=ARRIVAL)

man_lambert = Maneuver.lambert(ss_earth, ss_mars)
ss_trans, ss_target = ss_earth.apply_maneuver(man_lambert, intermediate=True)
```
<center>
**[Link to the corresponding pull request](https://github.com/poliastro/poliastro/pull/680)**
</center>

### Document Lambert's maneuver

It was necessary to update some of the Jupyter notebooks that made use of the
previous * raw* implementation of the algorithm.

<center>
**[Link to the corresponding pull request](https://github.com/poliastro/poliastro/pull/699)**
</center>

### Lambert's multirevolution example

After `#680` it was even easier to work with `Lambert transfers`. Therefore, I
decided to add some more documentation on the multi revolution problem. A
custom explanatory image was designed and finally merge in the following pull
request.

<center>
![]({static}/images/multi_lambert.png)
</center>

<center>
**[Link to the corresponding pull request](https://github.com/poliastro/poliastro/pull/725)**
</center>


### Add trail plotting option

To give a more *dynamical* perspective to the user when working with
`StaticOrbitPlotter()` instances this feature was proposed. Initial
implementation was not merged but improved by mentor Juanlu. Thank you so much
for your help!

<center>
![trail]({static}/images/faded_orbit.png)
</center>

<center>
**[Link to the corresponding pull request](https://github.com/poliastro/poliastro/pull/688)**
</center>

### Add ipywidgets to tox -e images

This is one of the minor issues that appear while coding. It was really easy to
solve.

<center>
**[Link to the corresponding pull request](https://github.com/poliastro/poliastro/pull/696)**
</center>

### Update tests to astropy 3.2

Some of the tests were coded by hard, meaning that they are subjected to
updates on NASA's JPL database. Therefore, when `astropy 3.2` was released it
was necessary to update some of them.

<center>
**[Link to the corresponding pull request](https://github.com/poliastro/poliastro/pull/700)**
</center>

### New powerful twobody propagators

While working with [#475](https://github.com/poliastro/poliastro/issues/475) I
decided to implement a new propagator to compare the solutions against the
available ones in **poliastro**. However, I became interested in Kepler's
problem and decided to collect and implement all possible algorithms I was able
to find. Following routines were added:

* `mikkola`:  https://doi.org/10.1007/BF01235850
* `markley`: https://doi.org/10.1007/BF00691917 (this is the previously called `kepler_improved`)
* `pimienta`: [link to the paper](https://www.researchgate.net/publication/288133262_Accurate_Kepler_equation_solver_without_transcendental_function_evaluations)
* `gooding`: https://doi.org/10.1007/BF01235540
* `danby`: https://doi.org/10.1007/BF00691917

<center>
**[Link to the corresponding pull request](https://github.com/poliastro/poliastro/pull/718)**
</center>

### Orbit method `change_attractor`

When retrieving orbits from external sources, such for example Jupyter's moons
by making use of `Orbit.from_sbdb` they were retrieved with an ICRS frame.
However, if a user wants to study their orbit around Jupyter it was necessary
to implement some `Orbit` method.

The `change_attractor` orbit solved this issue. It checked when and `Orbit` instance was under or out its attractor's SOI.

<center>
**[Link to the corresponding pull request](https://github.com/poliastro/poliastro/pull/729)**
</center>

### Hohmann time to pericenter

In all books, Hohmann maneuvers are explained from the PQW orbital frame, with
the satellite at an initial perfect circular orbit and `true anomaly` equal to
zero. This may not be the case in the real world, since the initial orbit may
be elliptical and the satellite could be in another position rather than at
periapsis. If this was the case, the orbit was propagated by force without
notifying the user and this time was not taken into account. 

Finally, this was solved by keeping the forced propagation and adding that
`time_to_anomaly` in the corresponding `Maneuver` instance.

<center>
**[Link to the corresponding pull request](https://github.com/poliastro/poliastro/pull/744)**
</center>

### Add atmospheric models

After [#694](https://github.com/poliastro/poliastro/issues/694) was opened, it
was necessary to implement a better atmospheric model instead of using the ISA
one. Some models such as COESA62, COESA76 were merged in the master code after
0.13 was released. However, previous models were not fully implemented and just
worked under 100km geometric altitude.

<center>
**[Link to the corresponding pull request](https://github.com/poliastro/poliastro/pull/738)**
</center>

### Reformat on atmospheres

After more research on the topic, I was finally able to implement COESA76 up to
1000km instead of 86km. A 4th order polynomial was used but this required
hard-coding lots of coefficients.

That was the reason behind the reformat of the `poliastro.atmosphere` module.
By making use of `astropy` generated `.dat` files it was possible to clean up
last implementations and make them more readable.

<center>
**[Link to the corresponding pull request](https://github.com/poliastro/poliastro/pull/756)**
</center>

## WHAT IS LEFT #TODO

Comparing my `Open Astronomy` proposal with the previous implementations following features are still required to be developed:

- [ ] SS and Earth-Moon barycenters are still required to be developed.
- [ ] New orbit creation such us `from_TLE`
- [ ] More plotting capabilities such us different attractors in the same figure or groundtracks.
- [ ] Verner78 ODE method may be implemented in Scipy following same idea for the [DOP853](https://github.com/scipy/scipy/pull/10173).

## My experience as GSOC student

During the last months, I have learned a lot of new things. Although most of them
are related to scientific content (astrodynamics in particular), others refer
to Python language such as packaging, docs, CI, version release...

**It was a great experience working during this summer with `poliastro` and
`Open Astronomy` people. Juanlu has been an amazing mentor, answering almost in
time all my questions. He understood that some topics were a little bit
complicated and required more time than expected to be studied and applied
to the code.**

A total of 5299 lines of code were added while 2620 were removed. But
contributions will not stop there! The Python package `poliastro` shows an
amazing future in computational astrodynamics and I want to be part of that
future. For sure I will keep opening issues, pull requests and learning lots of
things. Thank you all very much.

*Per Python ad astra!*
