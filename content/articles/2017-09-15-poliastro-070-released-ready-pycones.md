Title: poliastro 0.7.0 released and ready for PyConES!
Date: 2017-09-15 11:00 CEST
Tags: SOCIS, poliastro, releases, PyConES
slug: 2017-09-15-poliastro-070-released-ready-pycones
lang: en
Author: Juan Luis Cano Rodríguez

It fills us with astronomical joy to announce the release of **poliastro 0.7.0**! 🚀

For the newcomers, poliastro is a pure Python library that allows you to simulate and analyze interplanetary orbits in a Jupyter notebook in an interactive and easy way, [used by people from all around the world](http://docs.poliastro.space/en/v0.7.0/index.html#success-stories). Sounds interesting? Read on!

This release is the biggest one since the creation of the project in terms of code changes and new features, and on behalf of the poliastro development team I would like to deeply thank the European Space Agency for the SOCIS grant that made it possible. Besides, I would like to officially welcome Antonio Hidalgo to the team, since in reward for his amazing work during SOCIS he gained write access to the repository. ¡Bienvenido Antonio!

As always, the easiest way to get poliastro in any platform is using `conda`:

```
conda install poliastro --channel conda-forge
```

Additionally, installation using `pip` is now better supported and `numba` is no longer optional (see below).

# Release highlights

## New NEOS package

As you have been reading in this blog during the summer, Antonio implemented a new `poliastro.neos` package which reads public asteroid and comet data from NASA JPL and loads it as poliastro `Orbit` objects. Using it is as simple as

```
from poliastro.neos import neows
apophis_orbit = neows.orbit_from_name('apophis')
```

And you can get nice plots like this one:

![Ganymed, Eros and an Amor asteroid](http://docs.poliastro.space/en/v0.7.0/_images/examples_Using_NEOS_package_7_1.png)

To know more about how to handle NEOS in poliastro check out [the corresponding Jupyter notebook](http://docs.poliastro.space/en/v0.7.0/examples/Using%20NEOS%20package.html)!

## Astropy for body ephemerides

We now rely directly on Astropy to manage the Solar System ephemerides for us. It ships an approximate model that does not require downloading files from the JPL, so now getting the osculating orbit of a body is as simple as:

```
>>> Orbit.from_body_ephem(Earth, epoch=time.Time("2015-05-09 10:43"))
1 x 1 AU x 23.4 deg orbit around Sun (☉)
```

In case we need more precise results, we can tell Astropy to download a better model:

```
>>> from astropy.coordinates import solar_system_ephemeris
>>> solar_system_ephemeris.set("jpl")
Downloading http://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/de430.bsp
|==========>-------------------------------|  23M/119M (19.54%) ETA    59s22ss23
```

## Coordinate frame transformations

In this release we took the issue of coordinate frames very seriously, namely because the REST APIs we are using to retrieve the orbits of NEOs use an _heliocentric ecliptic frame_ that is different from [ICRS](http://aa.usno.navy.mil/faq/docs/ICRS_doc.php), the standard frame assumed in poliastro.

As a result, we are working hard with the Astropy core devs (see [this lengthy pull request](https://github.com/astropy/astropy/pull/6508) by Juanlu) to properly define ecliptic coordinates and their transformations to other reference frames. You can have a sneak peek of this work by using the new `poliastro.frames` module:

```
from astropy.coordinates import (
    ICRS, CartesianRepresentation, CartesianDifferential)
from poliastro.neos import neows
from poliastro.frames import HeliocentricEclipticJ2000

florence = neows.orbit_from_name("Florence")

florence_heclip = HeliocentricEclipticJ2000(
    x=florence.r[0], y=florence.r[1], z=florence.r[2],
    d_x=florence.v[0], d_y=florence.v[1], d_z=florence.v[2],
    representation=CartesianRepresentation,
    differential_cls=CartesianDifferential,
    obstime=EPOCH
)

florence_icrs = florence_heclip.transform_to(ICRS)
```

This way you can mix orbits expressed in different frames as it is done here!

![Florence asteroid in the inner Solar System](http://docs.poliastro.space/en/v0.7.0/_images/examples_Catch_that_asteroid!_26_1.png)

For details on how this is done, check out the [Jupyter notebook that studies the orbit of the Florence asteroid](http://docs.poliastro.space/en/v0.7.0/examples/Catch%20that%20asteroid!.html).

## And many more!

There were so many changes in this release that describing them in full would take us a while. We recommend interested readers to check the [full release notes of poliastro 0.7.0](http://docs.poliastro.space/en/v0.7.0/changelog.html#poliastro-0-7-0-2017-09-15) in the official documentation.

This release arrived just in time to PyConES 2017, the Spanish Python Conference. [Our talk on poliastro and NEOS](https://2017.es.pycon.org/es/schedule/atrapa-ese-asteroide-con-poliastro/) (Spanish) was accepted, so we hope the public will enjoy our little Python library. See you there!

If you use poliastro and are happy with it, please send us a little paragraph to contact@poliastro.space and we will publish it under [our Success Stories section](http://docs.poliastro.space/en/v0.7.0/index.html#success-stories)!

As a last note, we would like to invite you to our [community chat](https://riot.im/app/#/room/#poliastro:matrix.org) so you can share your impressions on the library, ask questions, or just say "Thank you! 💙"

# Getting involved

Our focus now for the 0.8 release will be to improve the plotting capabilities. [Having proper 3D plotting functions is now the oldest poliastro issue](https://github.com/poliastro/poliastro/issues/22), and we think the library is now mature enough to accept the challenge. Several tasks will have to be worked on first:

* Add propagation to a certain date https://github.com/poliastro/poliastro/issues/236
* Add a method to sample an osculating orbit https://github.com/poliastro/poliastro/issues/237
* Refactor plotting to store all the orbits
* Add the ability to change the plotting plane a posteriori

Some of these are no easy tasks, so we will need your help!

If you are a beginner but still want to lend a hand, thank you again! Here you have [a list of issues that we have identified as "easy"](https://github.com/poliastro/poliastro/issues?q=is%3Aissue+is%3Aopen+label%3Aeasy) in case you need a place to start.

You are more than welcome to contribute to poliastro and even the tiniest help will be highly appreciated. This includes not only code, but also documentation, ideas, testing, blog articles showcasing poliastro... Anything! Please relax and read the [Contribution Guidelines](https://github.com/poliastro/poliastro/blob/master/CONTRIBUTING.rst) and drop by our chat so we can guide you in using git, GitHub and everything.

Before you leave, let me add a very important **impostor syndrome disclaimer** (from [here](https://github.com/adriennefriend/imposter-syndrome-disclaimer#how-to-contribute)):

> I want your help. No really, I do.
> 
> There might be a little voice inside that tells you you're not ready;
> that you need to do one more tutorial, or learn another framework, or
> write a few more blog posts before you can help me with this project.
> 
> I assure you, that's not the case.

If you have read this far, I hope to have you on board very soon :)

_Per Python ad astra!_

