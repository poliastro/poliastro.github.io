Title: GSOC-19 starts! 
Date: 2019-05-10 11:00
Category: GSOC
Tags: GSOC, GSOC19, poliastro
slug: 2019-05-10-poliastro-gsoc-jorge
lang: en
Author: Jorge Martínez Garrido

## From my first pull request to GSOC student

Hi, my name is Jorge, and I am one of the selected students for this GSOC
edition at poliastro under the OpenAstronomy organization. I started working on
poliastro project after Juanlu came to my university to give a talk about Open
Source software in engineering. 

After forking poliastro, I decided to improve API Docs, which gave me an
overview on how the project was built and how the different modules talked
among them. I had no idea on how Git and GitHub worked and therefore,
when finished with the docs my first pull request was quite massive...

But after that I started feeling more confortable with GitHub and Sphinx, the
tool used nowadays in poliastro for building documentation. Then, I decided to
work on a porkchop plotter.

I spent the week after taking my final exams with the porkchop plotter. Reading
lots of blogs, posts and others on how to plot contours in Python, vectorize
functions... But finally, I was able to code the plotting utility and it was
included in poliastro.

## GSOC acceptance and first ideas

After being accepted at GSOC I have received a lot of emails, comming either
from Google, OpenAstronomy and poliastro. We need to regulary meet our tutors
or at least be in contact with them, so everyone knows how things are evolving.

Yesterday I talked with Juanlu about the main goals for this Summer of Code.
My objective during the first weeks of coding phase will be the development of
a propagation algorithm capable of working with all possible orbits, no matter
their eccentricity.

This would be amazing, since no integrators would be needed for near parabolic
orbits where numerical methods start failing. The algorithm that we expect to
solve for this is the one developed by Gauss.

## My plans for this summer in poliastro

Previous algorithm is just one of many utilities I am expected to code
all along this summer.  Although most of them are related
to numerical methods and inegrators, others dealt with:

* Plotting utilities such us a groundtrack plotter.
* Orbit determination and TLE retreival from Celestrack.
* Atmospheric models.
* Rendezvous maneuvers and low-thrust guidance.

At this moment, there are two main important core issues that I would like to
solve before first GSOC evaluation:

* Gauss propagator for any kind of orbit.
* Solar-system and Earth-Moon barycenters implementations.

I am still thinking how to approach the second one and this will need another
talk with Juanlu, for sure. But for the moment, I will focus on my final exams.

Can't wait to start the coding phase!

