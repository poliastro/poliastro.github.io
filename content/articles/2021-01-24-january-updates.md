Title: January updates
Date: 2021-01-24 12:00 CET
Tags: NumFOCUS,Updates
slug: 2021-01-24-January-updates
lang: en
Author: Juan Luis Cano Rodríguez

We got awarded a Small Development Grant by NumFOCUS to [validate poliastro against commercial and
non-commercial similar applications](https://github.com/poliastro/numfocus_proposal/)! 🎉 Jorge
started by setting GitHub Actions to [trigger the validations
automatically](https://github.com/poliastro/poliastro/pull/1051/), [validating our conversion
between cartesian and Keplerian elements against
Orekit](https://github.com/poliastro/validation/pull/4), and is now [fighting some discrepancies
with Hohmann transfers](https://github.com/poliastro/validation/pull/15).  
  
On the development front, while we wait for Numba to release Python 3.9-compatible wheels for our
next release, [we refactored our Cowell
propagator](https://github.com/poliastro/poliastro/pull/1053) to make the code simpler and more
numba-friendly, we tried to merge [Eleftheria's implementation of the Escobal method for satellite
visibility](https://github.com/poliastro/poliastro/pull/719) (and [sadly got blocked in the
process](https://space.stackexchange.com/q/49136/10716)), and kept working on [our analysis of
Walker constellations](https://gist.github.com/astrojuanlu/c44e57a8f4e001d5cbc6d6e53ecb66e0) for
[the OpenSatCom activity](https://opensatcom.org/). We also engaged with the authors of [the
awesome numbakit-ode](https://github.com/hgrecco/numbakit-ode/) to [rewrite our Cowell method using
numba](https://github.com/poliastro/poliastro/pull/1049), but found some issues along the way and
we decided to charge batteries and try again after some time.  
  
And finally, we made a *lot* of documentation changes! Dhruv sent a series of PRs to amend some
small issues, but most importantly he [rewrote all the docs using
MyST](https://github.com/poliastro/poliastro/pull/1073), a Markdown dialect compatible with Sphinx
that is getting popular. We also [removed the need to install LaTeX to compile our
docs](https://github.com/poliastro/poliastro/pull/1087), and [fixed some long standing problems
with our Binder examples](https://github.com/poliastro/poliastro/pull/1082).
