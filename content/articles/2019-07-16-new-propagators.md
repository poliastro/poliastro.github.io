Title: New propagators
Date: 2019-07-16 09:00
Category: GSOC
Tags: GSOC, GSOC19, poliastro, kepler
slug: 2019-07-16-new-propagators
lang: en
Author: Jorge Martínez Garrido


## What are propagators and why do we care about them?

One of the most common problems in astrodynamics and orbital mechanics is that
we want to know where a body will be at a given position along its orbit for a
given time. It is possible to integrate by hard the two-body equation and then
apply some boundary conditions. However, this last option is just insane and
would take several hours or days to be done by a human.

There is a better way to get the position as a function of time or `propagate` an
orbit. Johannes Kepler's contributions to the astrodynamics and orbital
mechanics field were really important and can be summarized here, in the
so-called Kepler's Laws:

* Planets' orbits follow an elliptical path around the Sun, which is located in one of the focus.
* Planets cover equal areas for given equal amounts of time.
* The square of the period is proportional to the cube of the semi-major axis.

Although Kepler applied previous laws to planets and they lead to good
approximations, they just can be applied when one of the masses is really small
compared to the other. Otherwise, the two masses will orbit around their common
center of mass, breaking this way the first law.

But one of the greatest relations that Kepler gave us was his famous Kepler's
Equation:

$$M = E - \sin(E)$$

This equation can be rewrited in the following form:
$$ M - M_{0} = n(t - t_{0}) = E - \sin(E) - E_{0} + \sin(E_{0}) $$

Where $$n = \sqrt{\frac{a^{3}}{\mu}}$$ is usually known as mean motion. Variables
M and E are respectively mean anomaly and eccentricity anomaly. This last one
can be realted to the true anomaly by:

$$ \cos(E) = \frac{e + \cos(\nu)}{1 + e\cos({\nu})} $$

Notice that given a certain amount of time, if we want to solve for the
position (solving for true anomaly) we must solve first for E and the previous
equation has not an analytical solution due to a sinusoidal function.

That fact makes this expression one of the most interesting topics in
astrodynamics: how to develop equivalent expressions, algorithms, procedures to
solve efficiently the Kepler's equation. Several algorithms have been raised
during the last years and now can be found in poliastro:

* mean_motion [already implemented]: propagates step by step and covers all geometric shapes.
* Kepler [already implemented]: propagates making use of universal formulation.
* mikkola [new]: applies a cubic approximation.
* markley [new]: fifth-order refinement of Mikkola's solution.
* pimienta [new]: 15th order polynomial approximation.
* gooding [new]: third-order polynomial approximation.
* danby [new]: fourth order convergence after initial guess.
* cowell [already implemented]: direct two-body equation integration.

### Which one is faster?

All the previous Kepler solvers are numerical methods. Numerical methods are
based on different mathematical concepts (derivatives, Taylor expansions...)
and sometimes they do not cover specific cases where singularities appear. For
these reason there is no such a great or perfect numerical method that works
well no matter the function to evaluate.

By having all this propagators, we are able now to compare which one is better
against different conditions: long time propagation, near equatorial orbits,
near parabolic orbits...

## Version 0.13

The release of poliastro 0.13 is getting closer and different checks need to be
done. This implies no more great features or implementations during the next
days until the version has been released. Some milestones where moved to version
0.14 due to their complexity, most of them related to frames. 

Is not rocket science, it is computer rocket science in fact! Modelling physical
concepts and implement them inside a computer is amazing but requires a good
approach and practices from the software engineering perspective, so all the
different algorithms work fast and be reusable.
