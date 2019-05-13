Title: The beginning of GSoC 
Date: 2019-05-13 20:30
Category: GSCO19
Tags: GSOC19, poliastro
slug: 2019-05-10-poliastro-gsoc-eleftheria
lang: en

Hello everyone, I'm Eleftheria and this summer I'll be working with poliastro 
under Open Astronomy as part of GSoC 2019. I'm hoping this blog will prove to 
be interesting to those who are interested in poliastro or simply a source of 
inspiration to those looking for a way to get their feet wet with open source.

The beginning of a journey
==========================

After forking poliastro, I immediately dived in and tried to make sense of the
codebase. Fortunately, poliastro is extensively 
[documented](https://docs.poliastro.space/en/stable/) so the learning curve wasn't
as steep as I expected. After getting familiar with the project structure, I started
browsing the open issues to find ways to make myself useful. What caught my attention
was the ongoing process of adding visualization features to poliastro, which would 
make the library more accessible to professionals and beginners alike.


It should be noted that poliastro does provide a way to easily create both 
[2D](https://docs.poliastro.space/en/stable/examples/Catch%20that%20asteroid!.html?highlight=plot)
and  [3D](https://docs.poliastro.space/en/stable/examples/Plotting%20in%203D.html) plots.
However, while matplotlib and plotly excell at data visualization, neither of them
are really suitable for this particular task. 

Cesium to the rescue
====================

One of the project ideas was to create an application who could extract orbitary data with
the help of poliastro and visualize it with Cesium. While I've heared of Cesium before,
as it is arguably one of the most well-known javascript libraries (and is also open source!), 
I didn't know just how extensive its functionality is.


I immediately started looking at similar projects both for inspiration and in order to get 
a sense of what can be achieved on the tecnhical side. I was pleasantly surprised by a large
selection of [demos](https://cesiumjs.org/demos/), 
[some](https://cesiumjs.org/demos/OrbitalPredictor/) of which were particulary relevant to
poliastro.

Summer is coming
================

So what is there to be done during the summer? Well, fortunately far more that I initially 
expected. I currently have a working, albeit basic version of the project which allows the users 
to define earth-based sattelites and visualize their trajectories, but when it comes to additional
features, sky's the limit. 

Some of the features I plan to tackle first are:

* Add communication satellites and ground stations and visualize their line of sight.

* Add a groundtrack plotter capabilities (hopefully following Jorge's work) that will also work
with Cesium's 2D view

* Implement planetary orbits 

I'm really excited to start working on the project and hope for an exciting and productive summer!
