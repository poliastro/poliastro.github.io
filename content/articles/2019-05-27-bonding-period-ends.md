Title: Coding phase starts!
Date: 2019-05-27 11:30
Category: GSOC
Tags: GSOC, GSOC19, poliastro
slug: 2019-05-27-coding-phase-starts
lang: en
Author: Jorge Martínez Garrido


## The End of the bonding period

Today bonding period ends for all students selected at GSoC'19. The aim of this
period was to learn more about your project community: get in touch with
mentors, other developers and their future ideas on the software...

As I said in my last post, I started contributing to poliastro several months
ago, even before GSOC was announced. Therefore, and since I am taking my final
exams, all my efforts were towards passing them.

But today the coding phase starts! That means we all should start working on
our proposal features.

## The coding phase at poliastro

The release of poliastro version 0.13 is getting closer. During this first part
of the coding phase, I am planning to solve for different issues, most of them
related to frames, [check out milestones 0.13](https://github.com/poliastro/poliastro/milestone/14).

Frames are really important: they enable to define where we are measuring from.
It should be easy to use them but also to define frames around custom bodies.
One solution as stated in
[Wiki](https://github.com/poliastro/poliastro/wiki/Orbits-and-reference-frames#proposed-steps)
is, no matter which frame is defined for each body, always work with a common one
internally at poliastro.

I will need to ask Juanlu and find the best approach on how to solve this
problem. When solved, I am sure poliastro plotting capabilities will increase. 
For example, plotting different bodies with different attractors in the same
figure.

Previous issues may be followed by defining Solar System Barycenter so more
accurate solutions could be worked by poliastro. But clearly, frame issues are
the most important thing for the moment.

## Hands on Gauss Algorithm

Some time ago I found great mathematician Gauss developed in his "Theoria motus
corporum coelestium in sectionibus conicis Solem ambientium" a way to transform
Kepler's algorithm into a third order polynomial. This led to an amazing fast
convergence when solving near parabolic orbits.

On Battin 1999 and improved Gauss algorithm is explained. However after several
hours of coding and debugging I have not been able to find why it does not
converge to the expected solution. I will come back to it after some time and
for sure make a post about this algorithm, because it is amazing how Gauss
was able to find a solution just by using convergent series!
