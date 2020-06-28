Title: What we've been working on these days!
Date: 2020-06-27 09:00 CEST
Tags: GSOC,GSOC20,Google,poliastro
slug: 2020-06-28-What-we'-ve-been-working-on-these-days!
lang: en
Author: Meuge

Hey, folks! I hope everyone is okay out there. Today, I am going to explain a little bit about **Repeat ground track orbits**, and the value that lies behind. 
Orbits with repeating ground tracks play a significant role in space engineering. Ground tracks that repeat according to any pattern have meaningful applications in remote sensing missions, reconnaissance missions, and numerous rendezvous and docking opportunities with an orbiting spacecraft. Since they overfly the same points on the planet’s surface every repeat cycle, such as those studying gravity, the atmosphere, or the movement of the polar ice cap.

![mind-blown](https://media.giphy.com/media/OK27wINdQS5YQ/giphy.gif)

So as you might imagine, this is amazing. In one way, the data we consume relies on these orbits. As mentioned before, Repeat ground track (RGT) orbits allows a satellite to reobserve the same area after a repeat cycle. 
![repeat-ground-track](https://www.iceye.com/hs-fs/hubfs/new-pages-website-2019/Img%20(no%20adding)/Sat%20Data%20-%20constellation.gif?width=450&name=Sat%20Data%20-%20constellation.gif)

# So how do we do it?

RGT is usually specified by an integer number of days *N* and an integer number of orbits *K* in the repeat cycle. So after acknowledging how the user wants the repeat ground track orbit. We calculate the mean semimajor axis,*a*, required for a repeating ground track orbit using an algorithm devised by Carl Wagner. And we iterate on *a* until we find the desired approximation. For further information, refer to *Fundamentals of Astrodynamics and Applications, 4th ed* by David A. Vallado. 

This algorithm starts with the following initial guess for the required mean semimajor axis:

$$a_{o}= \mu^\frac{1}{3}[(\frac{R}{D})\omega_{b}]^{-\frac{2}{3}}$$

And iteratively improves the semi-major axis with the following update:

$$a_{i+1}= \mu^\frac{1}{3}[(\frac{R}{D})\omega_{b}]^{-\frac{2}{3}}[1-\frac{3}{2}J_{2}(\frac{r_{bq}}{a_{i}})^2(1-\frac{3}{2}\sin(i)^2)]^\frac{2}{3}[1+J_{2}(\frac{r_{bq}}{a_{i}})^2(\frac{3}{2}\frac{R}{D}\cos(i)-\frac{3}{4}(5\cos(i)^2-1))]^\frac{2}{3}$$

Where:
$$R$$ = Integer number of orbits
$$D$$ = Integer number of days
$$J_{2}$$ = Second gravity coefficient
$$\omega_{b}$$ = Inertial rotation rate of the Body
$$r_{qb}$$ = Equatorial radius of the Body
$$i$$ = Orbital inclination
$$\mu$$ = Gravitational constant of the Body

So do you know any satellite mission that has a repeat ground track orbit? There are just a bunch of them!. Just to mention, ICESat (Ice, Cloud, and land Elevation Satellite), was a satellite mission for measuring ice sheet mass balance, cloud and aerosol heights, as well as land topography and vegetation characteristics. If you visit, [National Snow & Ice Data center](https://nsidc.org/data/icesat/data.html), you may find some datasets coming from the different versions of ICESat.

# Join us on SciPy US sprint!

**Poliastro** has registered on **SciPy US**, and we'll have a sprint on 11th and 12th July, in tandem with **SciPy** sprint. So make a time slot for yourself on the agenda, and get ready! If you have any ideas about what you want to work on, or stuff that you want us to pay attention to, feel free to write to us! These are some of the [suggestions](https://github.com/poliastro/poliastro/wiki/SciPy-2020-Sprint) we came up with.

That would be all for today, folks. ;) 
![bye](https://media.giphy.com/media/79ZFYdMsStRYI/giphy.gif)