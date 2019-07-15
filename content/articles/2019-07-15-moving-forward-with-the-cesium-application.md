Title: Moving forward with the Cesium application
Date: 2019-07-15 17:50
Category: GSCOC
Tags: GSOC, GSOC19, poliastro
slug: 2019-07-15-moving-forward-with-the-cesium-application
lang: en
Author: Eleftheria Chatziargyriou

I feel like in the last couple of weeks I got to work a little in several aspects
of the project. While this didn't allow me to focus on a single feature, it allowed
me to make progress in various different areas.

Bug resolving and 2D mode
--------------------------

First and foremost, I got rid of a particularly frustrating bug in the application.
Certain javascript events (such as the one that allows the inertial view), where tied 
to a single ``Viewer`` and thus wouldn't trigger when the ``Viewer`` was destroyed 
(which is the case when, for example, loading the data from the file). I also made a 
few minor changes in the code and introduced the option to set the Viewer mode to 2D.
This isn't any useful as of now, but it will be with the new feature I'm planning to 
introduce, which brings me to...

Groundtrack plotting
--------------------

Cesium allows users to define animated polyline paths, allowing us to visualize an orbit's 
groundtrack. What is even more exciting, is that Cesium automatically projects the path when
on 2D scene mode, allowing us to see the orbit's groundtrack even on orthographic projection.

I have most of the work laid out and I'm planning to open a pull request next week. Cesium
has a problem when dealing with particularly long paths and in that case the path needs to be 
broken down and dynamically loaded.

Satellite pass predictor
------------------------

I made an initial commit for the pass predictor based on Escobal's paper and I also started
working on a helper class to work on the Ellipsoidal coordinate system (altough technically,
the class is restricted to spheroids, since they are easier to work with and planetary bodies
can be accurately approximated by them). It offers methods for converting coordinates from the 
ellipsoidal to the Cartesian system and vice versa and determining whether a point is visible to
the ``SpheroidLocation``. Additionally, it is also equiped with a few other helpful math functions
(e.g. determining the plane tangential to the point on the spheroid).

Next steps
----------

In the next couple of weeks, I'm planning to finally finish the pass predictor and at least complete
the first commit of the groundtrack plotter.
