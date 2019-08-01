Title: Ground track plotting and Ellipsoids
Date: 2019-08-01 15:00
Category: GSCOC
Tags: GSOC, GSOC19, poliastro
slug: 2019-08-01-ground-track-plotting-and-ellipsoids.md
lang: en
Author: Eleftheria Chatziargyriou

The second evaluation period has come to the end and with the end of the
program drawing ever closer, I'm happy to announce that most work on 
the additional deliverables has been complete!

CZML3
-----
I've added polylines and points (along with myriad of other dependent 
properties/types). These also marked the release of 
[v0.1.3](https://pypi.org/project/czml3/#description)!

Ground Track Plotting
---------------------
Having added the necessary CZML properties, I finally managed to add
the ground track plotter. It allows to draw both a static path and
an animated one. The coolest feature is that it automatically calculates
the path's orthographic projection, allowing you to see the satellite in
2D mode. I was also toying with the idea of allowing the users to export
gif images directly from the application, which would mean no longer relying
on external screen capturing software to create and share projects.

Speroid Location
----------------
I refactored the class and got it merged which makes it technically possible
to determine an orbit's pass given the spheroid location. I'm ashamed to admit,
the pass predictor is the only area I haven't make any tangible progress in in 
the last  couple of weeks, so that definetely remains one of my main goals.

Ellipsoids, ellipsoids, ellipsoids...
-------------------------------------
The bug that has bugging me the most has been finally resolved! The cesium 
application now correctly renders any arbitrary ellipsoid. My last task is 
to create the rotation matrix given the attractor's average rotational velocity,
converting the system into ICRF.

What's Next?
------------

- Start working on some Jupyter notebook tutorials

- Hopefully be down with the closed-form pass peredictor

- Use ICRF frames in the app
