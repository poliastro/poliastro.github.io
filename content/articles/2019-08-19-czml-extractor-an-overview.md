Title: CZML Extractor: An overview
Date: 2019-08-19 15:00
Category: GSCOC
Tags: GSOC, GSOC19, poliastro
slug: 2019-08-19-czml-extractor-an-overview.md
lang: en
Author: Eleftheria Chatziargyriou

As the proverb says "all good things must come to an end". Unfortunately, it's time
to bid adieu to the summer and have a look on what has been accomplished so far.

The CZML Extractor
------------------
This was undoubtedly the main and most time-consuming part of the project. The extractor
allows users to easily convert orbital data to CZML. You can find an overview of the
extractor's usage in the [User Guide](https://docs.poliastro.space/en/stable/user_guide.html)
or take a look in the more in-depth 
[Jupyter notebook tutorial](https://github.com/Sedictious/poliastro/blob/2c4355e50207470b18f31d8405ddc1f2c53c574b/docs/source/examples/CZML%20Tutorial.ipynb)


The Cesium Application
-----------------------
Since we need more parameters to accurately represent the data, we also need a
specific application to parse said parameters. For this reason, I worked on a 
Cesium application that allows you to easily visualize the data. At this moment, 
there are two separate applications: 
[one](https://github.com/poliastro/cesium-app/tree/master/application) that runs remotely 
and [one](https://github.com/poliastro/cesium-app/tree/master/Sandcastle) you can
copy-paste directly into Cesium [Sandcastle](https://cesiumjs.org/Cesium/Build/Apps/Sandcastle/).
I have added the instructions on how to run it in the [repo](https://github.com/poliastro/cesium-app),
where you can also find a few examples to get you started.

CZML3
-----
As I've mentioned in previous posts, the CZML packets were internally represented
by nested dictionaries. This complicated the code and made it generally uglier for 
many reasons (need for a "default" packet, need to specify the path of every parameter
that was being added etc...). Fortunately, my mentor Juanlu came up with a great 
[library](https://github.com/poliastro/czml3) that made the process exponentially easier and
allowed us to get rid of many unecessary parts of the older code. Over time, I added most of 
the basic Cesium properties that were needed for the extractor (though I hope to eventually
go back to it and turn it into a fully fledged library!)


Git log
-------
Those are my PRs which were merged into poliastro's core (excluding the commits made to czml3 or the app)

- [#601 Adds basic CZML Extractor](https://github.com/poliastro/poliastro/pull/601)
- [#603 Added some tests for CZML Extractor](https://github.com/poliastro/poliastro/pull/634)
- [#661 Create custom CZML packets](https://github.com/poliastro/poliastro/pull/661)
- [#674 Add ground stations](https://github.com/poliastro/poliastro/pull/674)
- [#711 Use czml3 for the czml extractor](https://github.com/poliastro/poliastro/pull/711)
- [#717 Additional orbit properties](https://github.com/poliastro/poliastro/pull/717)
- [#720 Add SpheroidLocation class](https://github.com/poliastro/poliastro/pull/720)
- [#721 Add 2D Scene support](https://github.com/poliastro/poliastro/pull/721)
- [#730 Add updated IAU values for body radii](https://github.com/poliastro/poliastro/pull/730)
- [#735 Update rotational elements](https://github.com/poliastro/poliastro/pull/735)
- [#737 SpheroidLocation accepts poliastro bodies instead of spheroid parameters](https://github.com/poliastro/poliastro/pull/737)
- [#739 Add ground track plotting](https://github.com/poliastro/poliastro/pull/739)
- [#743 Allow groundtrack lead/trail time](https://github.com/poliastro/poliastro/pull/743)
- [#746 Add angular speed and rotational period](https://github.com/poliastro/poliastro/pull/746)
- [#753 Add initial CZML notebook tutorial](https://github.com/poliastro/poliastro/pull/753)
- [#755 Add additional parameters for groundtracks](https://github.com/poliastro/poliastro/pull/755)

There is still a pending PR that will add pass tracking (finally). I'm currently trying to test the 
added functionality to ensure it is as bug-free as possible.

Special thanks
--------------
I'd like to thank everyone in the Open Atronomy community. I'd also like to give a special
thanks to my mentor, Juanlu, who helped make the whole GSoC experience even greater than I initially
expected: he helped me get the proper background, gave helpful feedback and was very supportive
and an all-around amazing person!

What's next
-----------
I had a wonderful time and I'm certainly planning to go back and polish the project as well as add
any extra functionalities. Who knows, maybe there are many more contributions yet to come 😉

If you're interested in this project, or poliastro in general, you can attend the 
[Open Source CubeSat Workshop](https://indico.oscw.space/event/3/) where we'll be running a 
[workshop](https://indico.oscw.space/event/3/contributions/78/). Hope to see you there!
