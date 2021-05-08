Title: April updates
Date: 2021-05-08 21:00 CET
Tags: NumFOCUS,Updates
slug: april-updates
lang: en
Author: Juan Luis Cano Rodríguez

The first (and hopefully) only **beta of poliastro 0.15** is out! 🎉
It took us a bit longer to get this release out,
but we are happy that poliastro 0.15 is now around the corner.
We will soon write detailed release notes and a proper announcement for it,
and in the meanwhile you can read [the preliminary poliastro 0.15 changelog](https://docs.poliastro.space/en/latest/changelog.html).

Juan Luis revamped our website a bit,
by [adjusting our domain names](https://github.com/poliastro/poliastro.github.io/issues/2)
and [improving the navigation bar](https://github.com/poliastro/poliastro.github.io/pull/74)
([twice](https://github.com/poliastro/poliastro.github.io/pull/77)).
Besides, he has finished the reorganization of our docs
following [the Diátaxis Framework by Daniele Procida](https://diataxis.fr/),
[prepared for the upcoming Sphinx 4.0 release](https://github.com/poliastro/poliastro/pull/1188),
and [updated our installation and contribution instructions](https://github.com/poliastro/poliastro/pull/1206/).

Jorge has finished [validating our planetary transformations against GMAT and Orekit](https://github.com/poliastro/validation/pull/24),
which required reaching out to the Orekit developers
and [adjusting one outdated constant in poliastro](https://github.com/poliastro/poliastro/pull/1193).
This wraps up the work we started with our first [NumFOCUS Small Development Grant](https://numfocus.org/programs/small-development-grants),
and we will be also sending a report and an announcement very soon!

Finally, Dhruv and Abdul have made some small fixes and cleanups,
and Yash has started moving many parts of poliastro computation to our core API
to make them faster,
like our [maneuver computations](https://github.com/poliastro/poliastro/pull/1136)
and our [spheroid arithmetic](https://github.com/poliastro/poliastro/pull/1136).
We have more pull requests like this in the pipeline,
which we will start reviewing soon
now that the `0.15.x` branch has been created.
