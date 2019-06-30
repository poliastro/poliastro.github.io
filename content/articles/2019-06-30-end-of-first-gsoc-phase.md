Title: End of first GSoC phase 
Date: 2019-06-30 11:30
Category: GSCOC
Tags: GSOC, GSOC19, poliastro
slug: 2019-06-30-end-of-first-gsoc-phase
lang: en
Author: Eleftheria Chatziargyriou

So the first phase of GSoC is over and with it, it's time to reflect what
has been achieved in the last couple of months.

CZML3
=====

As I mentioned in the 
[last blogpost](https://blog.poliastro.space/2019/06/13/2019-06-13-communication-satellites-and-refactoring/)
this is a very useful [library](https://github.com/poliastro/czml3) created by juanlu. After a
few patches, the library now supports most CZML properties and - as far as I can tell - this is 
the only currently mantained Python library for creating CZML packets.

CZML Extractor
==============

This is the first feature I've started to work on and while it is still far from complete,
I'm happy to say that it is now usable. 

At first, the czml document was represented by a nested dictionary and then converted to 
valid JSON format. This worked ok and I did write a function which made manipulating the
dictionary a tad more intuitive, but it was overall a very ad hoc solution and made the
code hard to follow. What I attempted to do was to completely refactor the extractor
to rely on czml3 (you can find the related PR [here](https://github.com/poliastro/poliastro/pull/711)).

Merging the PR and getting everything *just* right gave me far more trouble than I would've expected
and there are still a few more things that need to be adressed. Part of the problem was that czml3
doesn't support Python 3.5 (since it doesn't have any way to implement ordered dictionaries without 
relying on external libaries or creating your own data structure), so a simple Import Error could 
cause the whole thing to fail. On the flipside, I learned the importance of exhaustive testing and
paying attention to versioning.

Cesium application
==================

Of course, the custom data isn't really useful in and of itself so I also created an 
[application](https://github.com/poliastro/cesium-app) (which you can run both locally and on
[Sandcastle](https://cesiumjs.org/Cesium/Build/Apps/Sandcastle/)) to visualize the data. 

What's next?
============

As I mentioned before, one of the features I was meaning to add was the determination of a satellite's pass.
The difficulty lies in solving the problem efficiently and most of the solutions I've thought of or read were either
too slow or too inaccurate and often making earth-specific assumptions which wouldn't help with the general case.

However, my mentor recently pointed my to a very interesting [paper](https://arc.aiaa.org/doi/abs/10.2514/3.2057) which
I'm currently going through and trying to thing of the next step.

GSoC has been a great experience so far and I'm looking forward to the next coding phase!
