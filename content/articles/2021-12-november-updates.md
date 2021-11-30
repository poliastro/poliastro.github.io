Title: November updates
Date: 2021-12-01 00:00 CET
Tags: NumFOCUS,Updates
slug: november-updates
lang: en
Author: Juan Luis Cano Rodríguez

We have released the first beta of poliastro 0.16!
[Highlights include](https://docs.poliastro.space/en/latest/changelog.html)
new events detectors written by Yash as part of GSOC 2021,
a new `.plot_maneuver` method, and many performance improvements.
We expect to release 0.16.0 in the first days of December,
and users are encouraged to test their code with the beta.

During this month we have made some small improvements to the library
and the development workflow. In particular, we have added
a continuous integration check that ensures that `poliastro.core`
depends only on NumPy and numba. For the next release we want to
keep working on the consistency and quality of the code and do some cleanups.

We discussed the possibility of adding new APIs to interface with TLE data,
which will enable a whole new range of use cases
related to commercial terrestrial satellites.
Hopefully we will be able to present a prototype in the upcoming
[Open Source Cubesat Workshop 2021](https://events.libre.space/event/5/).
