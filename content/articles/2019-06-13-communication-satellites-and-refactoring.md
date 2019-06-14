Title: Communication satellites and refactoring 
Date: 2019-06-13 21:00
Category: GSCOC
Tags: GSOC, GSOC19, poliastro
slug: 2019-06-13-communication-satellites-and-refactoring
lang: en
Author: Eleftheria Chatziargyriou

Those couple of weeks were spent mainly on setting future milestones
and improving the quality of the code. In a way, Tom Cargill's famous
aphorism came to my mind:

> The first 90 percent of the code accounts for the first 90 percent 
of the development time. The remaining 10 percent of the code accounts
for the other 90 percent of the development time.

Writing stuff that "just works" is relatively easy. But when programming,
you always have to keep track of myriad variables including but not limited
to: maintanability, integration and readability. 

CZML3
=====

My mentor, Juanlu, wrote a fully-fledged [library](https://github.com/poliastro/czml3)
for composing czml packets. While it's still in the early stages of development,
I  would urge anyone interested to check it out. I'm currently trying to refactor
the czml core, so it utilizes the library instead of the current approach (packets
are represented as a nested dictionary which is then converted to JSON).

Changes to the javascript application
=====================================

* Added camera controls for easier navigation (only rotation left to be added)

* Added a file browser, so that any czml data file can be added directly from the
browser. This was one of my top priorities since before that, the only way to import
the files was by copy-pasting.

* Wrote a README explaining how to run the application. Once I'm done with the basic 
refactoring, I'll also start adding documentation  and tutorials about writing czml 
packets.

Communication satellites
========================

As mentioned in the last blogpost, I started working on visualizing ground stations
and communication satellites. This opened up a whole new can of worms. For example,
early in the process, we decided that it would be better for groundstation's coordinates
to be expressed on the ellipsoidal coordinate system. However, this seemed to result in
accuracy errors where a given point would be slightly off the ellipsoid, which would in
turn give inaccurate results on the visibility predictor. Some of the code is merged and 
at least a PR containing the basic implementation is pending, but I'll get back to it
after refactoring the core.
