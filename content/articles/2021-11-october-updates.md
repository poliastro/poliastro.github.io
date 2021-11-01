Title: October updates
Date: 2021-10-01 20:00 CET
Tags: NumFOCUS,Updates
slug: october-updates
lang: en
Author: Juan Luis Cano Rodríguez

October was a particularly intense month, with lots of exciting news!

We are thrilled to announce that NumFOCUS accepted to fund
[our proposal to introduce array orbit types
to accelerate parallel computing workflows in poliastro](https://github.com/poliastro/documents/blob/master/numfocus-sdg-2021-r3.md)
as part of their Small Development Grants program.
The proposal was written by Sebastian M. Ernst
and we have already started coordinating what will be the next steps.

In other news, a team of researchers participating in the
[Global Trajectory Optimization Competition](https://sophia.estec.esa.int/gtoc_portal/)
is using the poliastro,
and they discovered a few bugs and made numerous code contributions.
Special thanks to [Manuel López Ibáñez](https://github.com/MLopez-Ibanez)!

Among other things, we fixed long standing bugs op
[our Izzo algorithm for the Lambert problem](https://github.com/poliastro/poliastro/issues/1362)
and [our accelerated `rotation_matrix` function](https://github.com/poliastro/poliastro/issues/1360).
We plan to release the next version of poliastro
with these and other fixes
[in the coming weeks](https://github.com/poliastro/poliastro/pull/1348).

Lately we have been struggling with our numerical propagators,
because we want to squeeze more data from the integration process.
We rescued some past work
and [contributed a new higher-order method to SciPy](https://github.com/scipy/scipy/pull/14956)
that we hope to finish soon.

And finally, both the [Open Source Cubesat Workshop](https://events.libre.space/event/5/abstracts/)
and [SciPy Latin America](https://www.scipy.lat/conf/2021/),
two very special events for us,
have been announced!
We intend to be present in both, let us know if you will be joining as well!
