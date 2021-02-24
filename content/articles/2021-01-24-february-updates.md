Title: February updates
Date: 2021-02-24 21:00 CET
Tags: NumFOCUS,Updates
slug: 2021-02-24-February-updates
lang: en
Author: Juan Luis Cano Rodríguez

poliastro [finally landed support for Python 3.9](https://github.com/poliastro/poliastro/pull/1027),
thanks to the fine folks of numba! [Their release candidate already works with the newest Python
release](https://numba.discourse.group/t/numba-0-53-0-and-llvmlite-0-36-0-release-candidates/504?u=astrojuanlu),
and we've been told that [the stable release is around the
corner](https://twitter.com/numba_jit/status/1363868866984751107). This means that the next stable
release of poliastro will also support it 🚀

On the validation side, Jorge has been working on more enhancements, and we have finally confirmed
that our 3D impulsive maneuvers give the same result as GMAT and Orekit! You can read the full
details [in this blog
post](https://blog.poliastro.space/blog/2021/02/17/2021-02-17-validation-of-3dmaneuvers/).

And finally, we have made some small improvements on the development side, by [fixing some
continuous integration small failures](https://twitter.com/numba_jit/status/1363868866984751107),
[reducing the number of warnings in our tests](https://github.com/poliastro/poliastro/pull/1092),
and [other small fixes](https://github.com/poliastro/poliastro/pull/1094). Thanks Yash, Dhruv, zkl2,
and Souhit!
