Title: Summarizing GSoC 2021
Date: 2021-08-22 12:00 IST
Category: GSOC
Tags: GSOC, GSOC21, poliastro
slug: conclusion-gsoc21
lang: en
Author: Yash

This page describes the work done during Google Summer of Code 2021 with [poliastro](https://github.com/poliastro/poliastro). I added some space event detectors under the `twobody` problem by implementing raw orbital mechanics algorithms (inside `poliastro.core`) accelerated by the `numba.jit()` decorator (in the `nopython` compilation mode, as was customary in `poliastro`). It uses the `events` parameter from `scipy.integrate.solve_ivp` for tracking events and numerical integration. The required condition is checked at each time instance for an event occurence.

The validation cases for the events were developed against the [`orekit`](https://www.orekit.org/) software, using the [Orekit Python Wrapper](https://gitlab.orekit.org/orekit-labs/python-wrapper), and some additional tests were added for investigating edge-cases. The user guide for the added events and some plotting results using `poliastro`’s plotting capabilities, can be found [here](https://docs.poliastro.space/en/latest/examples/Detecting%20Events.html).

## Added events (so far…)

- Altitude Crossing [#1254](https://github.com/poliastro/poliastro/pull/1254).
    - The already existing `LithobrakeEvent` was made to inherit this event.
- Latitude Crossing [#1268](https://github.com/poliastro/poliastro/pull/1268).
- Eclipse (penumbra and umbra) Event [#1246](https://github.com/poliastro/poliastro/pull/1246).
    - Thanks to `numba`'s function optimization capabilities for accelerating some calculations in the developed analytical "shadow" function!
- Nodal Crossing [#1293](https://github.com/poliastro/poliastro/pull/1293).

These events could be used for orbits around any solar system body, and are not restricted to the Earth, since they do not leverage any earth-specific properties.

The template structure to use the events is given below:

```py
event_1 = <Event>(<args>, direction=0, terminal=True)
.
.
.
events = [event_1, event_2, …, event_n]
r, v = cowell(
	attractor.k,
	orbit.r,
	orbit.v,
	tofs,
	events=events,
	f=func_twobody
)
```
where the argument `f`, which defaults to keplerian-only forces, can be modified to include, for example, atmospheric perturbations for more rigorous orbit analyses.

## Other work (bug fixes, additional patches)
- We observed some general and events-related bugs, one of which was related to orbit propagation termination during event tracking:
    - Issue: [#1285](https://github.com/poliastro/poliastro/issues/1285)
    - PR: [#1288](https://github.com/poliastro/poliastro/pull/1288)

- Some examples of additional and/or supporting patches include:

    - Marginal newton iteration speed enhancement for eccentric and hyperbolic anomaly calculation (https://github.com/poliastro/poliastro/pull/1247).
    - Adding tests:
        - [#1255](https://github.com/poliastro/poliastro/pull/1255)
        - [#1272](https://github.com/poliastro/poliastro/pull/1272)

    - Completing work on removing some test warnings [#1235](https://github.com/poliastro/poliastro/pull/1235)


I have also included the progress journey in the following blog posts:

- [Introduction blog](https://www.poliastro.space/blog/2021/06/06/poliastro-gsoc-yash/)
- [Second blog](https://www.poliastro.space/blog/2021/07/19/adding-ale-event-detectors/)

## What is left to do?

Apart from the above, implementing some events is currently work-in-progress, on which I would continue to work:

- Line-of-sight (LOS) event [#1258](https://github.com/poliastro/poliastro/pull/1258).
    - An edge-case, when the satellite hits the attractor (`LithobrakeEvent`) while tracking for a LOS, is under inspection.
- Satellite visibility with respect to a ground station [#1299](https://github.com/poliastro/poliastro/pull/1299).
    - Slight event time mismatches with the corresponding `orekit`'s `ElevationDetector` are being investigated.
- Satellite view event [#1298](https://github.com/poliastro/poliastro/pull/1298).
    - The addition of a reliable test example to check the added implementation is pending.
- Satellite-satellite collision detection.

## Acknowledgments

I am very grateful to and sincerely thank my mentors, Juan Luis Cano Rodríguez and Jorge Martínez, for critically reviewing pull requests, assisting in making event API decisions, and for help in implementing the event validation cases.