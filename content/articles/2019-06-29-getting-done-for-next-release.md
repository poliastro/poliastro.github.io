Title: Getting done for next release
Date: 2019-06-29 07:00
Category: GSOC
Tags: GSOC, GSOC19, poliastro
slug: 2019-06-29-getting-done-for-next-release
lang: en
Author: Jorge Martínez Garrido

## Version 0.13 is getting closer

Version 0.13 is expected to be tagged in about a month. As any other release,
it includes new features such as a new method in the `Orbit` class called
`change_attractor` or the `trail` parameter in `StaticOrbitPlotter`. However,
this release will also include really important bug fixes such as:

* Minor issues related to Lambert's problem.
* Propagator's are supposed not to hang out anymore due to robust solutions and propagation methods.

Now that my final exams ended I am completely free to work in poliastro and
direct all my efforts to the software. I want to close issues
[#495](https://github.com/poliastro/poliastro/issues/495) and
[#475](https://github.com/poliastro/poliastro/issues/475)  in the next days since they are previously commented bugs.

### Propagator methods in the twobody problem

Kepler's equation (KE) allows us to solve either for the time at a given
position or the position for a known time. Although it is a very short
equation, there have been lots of numerical methods along with history since it
has not an analytical solution.

The most famous numerical method related to root finding is probably the so
called [Newton-Raphson
method](https://es.wikipedia.org/wiki/M%C3%A9todo_de_Newton). By making use of
the function derivative it is possible to reach with great accuracy and speed
the solution to the equation. Other methods also use higher order derivatives
to achieve a faster connvergence. Although the Newton-Raphson methods works
really well most of the cases, it is possible that sometimes the derivative at
some point of the evaluated function becomes zero, making to diverge the
numerical method.

Along the years, different approaches have been developed to solve this famous
equation: conversion to a third order polynomial, higher order derivatives
iterative methods, series expansion... Most of the different papers available
claim convergence regarding the speed of computation, somehting that is not
*fair* if we consider that CPUs computational power evolve as years pass.
Numerical methods should be compared fixing a relative error and number of
iterations. But remember: there is not a perfect numerical methods. While for
examples the *bisection* method always converges it does really slowly, on the
other hand, *Newton-Rapshon* based methods have a great rate convergence but
are subjected to zero derivative singularities.

After a huge research on the topic, the most interesting algorithms from my
point of view are the following ones:

* [Fukushima's work on KE](http://dx.doi.org/10.1007/BF00049384)
* [Solving the KE with SDG-CODE](https://doi.org/10.1051/0004-6361/201833563)

Both are universal, meaning that no matter the geometrical nature of the orbit
we can solve the KE. They claim low interations with huge numerical precission
onli limited by mantissa errors (floating point precission).

### Implementation of previous methods

As said before, there is no such a perfect numerical solver for the KE. I would
like to implement not only the previous cited ones, but also more of them and
compare their performance on the near-parabolic regime.

Fukushima's work also includes some Fortran77 codes and his research on the KE
topic is huge. It looks really promising. On the other hand, the SDG group at
UPM may be a really good contact source if I got stucked with the
implementation of the algorithm.

Last week I already added a new one that was called by me as
[*kepler_improved*](https://gist.github.com/jorgepiloto/8d572ea4bb50c9ffed93c56dfaa81160)
and although it is a non-iterative method it has a great accuracy. But after
some tests, I realized that it was diverging for eccentricities near 0.999. I
will contact with the [Julia Astro](https://juliaastro.github.io/) people to
compare the results.

Stay tuned!🚀 
