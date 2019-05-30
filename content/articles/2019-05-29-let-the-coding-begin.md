Title: Let the coding begin
Date: 2019-05-29 23:30
Category: GSCOC
Tags: GSOC, GSOC19, poliastro
slug: 2019-05-29-let-the-coding-begin
lang: en
Author: Eleftheria Chatziargyriou

Let the coding begin
====================

So the bonding period is over, which means that the coding phase has officially begun.
I've already worked on some of the key features I'd like to add since my examination
period is around the corner. Hopefully, this won't slow me down and I'll keep up with 
the workload.

The work so far
===============

I've worked on the main part of the project, which was to connect poliastro to the
visualization capabilities offered by the Cesium API. There is already the possibility
of adding orbits and defining custom attractors, along with various visual customizations.
As exciting as this is, there are still way more things that could be added to give life to the
project, rendering it more useful and interesting.

Communications satellites
=========================

In the past days, I became increasingly interested in adding communication satellites
and visualizing their line of sight. I added a bit of extra code to define ground
stations anywhere on the surface of the attractor.

With the attractor defined, we need to calculate the time the satellite is visible
to the ground station. My initial approach was pretty straight-forward:

- Take N sample points of the trajectory.

- Emit a ray from said point to the ground station.

- If the ray intersects the ellipsoid at any point other than the ground station discard
it, otherwise conclude that the satellite is visible to the station at the given
time stamp.

Despite working fine, this approach posed two main problems: The calculated pass is
dependent on the number of sample points and the algorithm itself isn't really efficient.

What I thought next was to define the plane that is tangential to the ellipse at the coordinates
of the ground station. After that, we could easily find the point where the plane and the trajectory
(granted it has constant eccentricity) intersect. Now we'd have the exact point where the satellite
became visible, but we still needed the respective timestamp. This was the point I became stuck and
had to ask my mentor for ideas on how to move on. Unfortunately, the answer is that there is no single
closed formula that can be used to easily calculate the starting and ending epochs. The problem needs
to be reformulated mathematically and solved by known iterative approximation methods.

What's next
===========

By the end of the first phase, I'm planning to have a more-or-less working pass predictor integrated
into poliastro. I'd also like to work some more on documentation, by adding a few tutorials to make
the project more accessible to regular users.
