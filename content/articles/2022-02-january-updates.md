Title: December updates
Date: 2021-02-01 16:00 CET
Tags: NumFOCUS,Updates
slug: january-updates
lang: en
Author: Juan Luis Cano Rodríguez

This January we have spent a lot of time discussing Sebastian proposal
to [add a new `OrbitArray` object](https://github.com/poliastro/poliastro/pull/1445)
in line with our Small Development Grant.
We are now all in the same page and the implementation is progressing nicely!

Apart from that, our contributors have been working on a number of things:

- After the release of numba 0.55, Juan Luis
  [added support for Python 3.10](https://github.com/poliastro/poliastro/pull/1441)
  and dropped 3.7.
- Jorge has [fixed some long-standing problems with the Lambert
  API](https://github.com/poliastro/poliastro/pull/1450)
  by unifying the two algorithms included in the libary, removing an unnecessary iteration,
  and documenting everything in depth.
- Yash [addressed a pickling error with bodies](https://github.com/poliastro/poliastro/pull/1443)
  that was discovered after using poliastro in multiprocessing workloads,
  [unified the computation of vector norms](https://github.com/poliastro/poliastro/pull/1442),
  and [fixed a propagation error](https://github.com/poliastro/poliastro/pull/1444)
  that was affecting highly eccentric orbits.
- Kevin, a new contributor, added
  [the propagation algorithm he developed](https://github.com/poliastro/poliastro/pull/1439)
  as part of his Masters thesis, and
  contributed several functions related to the
  [Circular Restricted Three Body Problem](https://github.com/poliastro/poliastro/pull/1451).

In the coming weeks, Juan Luis will work with the Libre Space Foundation to prepare
Google Summer of Code 2022 and keep working with Sebastian on `OrbitArray` objects.
