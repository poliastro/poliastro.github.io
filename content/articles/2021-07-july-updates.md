Title: July updates
Date: 2021-07-18 17:00 CET
Tags: NumFOCUS,Updates
slug: july-updates
lang: en
Author: Juan Luis Cano Rodríguez

This month [the poliastro repository](https://github.com/poliastro/poliastro/)
has crossed ⭐️ 500 GitHub stars ⭐️, thanks everyone for believing in the
project!

Juan Luis [released version
0.15.2](https://docs.poliastro.space/en/v0.15.2/changelog.html) with [a fix for
newer astroquery versions](https://github.com/poliastro/poliastro/pull/1228),
as well as compatibility with Plotly 5.0, which allows users to install all the
required JupyterLab extensions without Node.js. This will make the installation
process much easier!

Yash and Jorge had a very productive month: after a lot of discussion in our
weekly community calls and several rounds of code reviews, [we finally have
eclipse event detection
merged!](https://github.com/poliastro/poliastro/pull/1246)
Yash has passed the first Google Summer of Code evaluation with
flying colors and will publish an entry in our blog soon. The work Jorge did
[on our validation
infrastructure](https://github.com/poliastro/validation/pull/33) as part of the
NumFOCUS Small Development Grant has proven to be extremely useful.
In addition, Yash has also added [latitude crossing
detection](https://github.com/poliastro/poliastro/pull/1268),
[accelerated some Earth atmosphere
calculations](https://github.com/poliastro/poliastro/pull/1280), and done some
other minor improvements, while Jorge has added [some developer documentation
on how we handle Orekit](https://github.com/poliastro/validation/pull/31) in our
validation infrastructure, done a lot of reviews for Yash, and [validated our
latitude crossing detection](https://github.com/poliastro/validation/pull/32)
against Orekit.

Finally, Javier Tegedor [accelerated some thrust
functions](https://github.com/poliastro/poliastro/pull/1250), making the slowest
tests 40 % faster!
