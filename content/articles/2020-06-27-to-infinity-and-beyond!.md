Title: To Infinity and Beyond!
Date: 2020-06-27 21:45 CEST
Tags: GSOC,GSOC20,Google,poliastro
slug: 2020-06-27-to-infinity-and-beyond!
lang: en
Author: Meuge

Hey folks! It's been a while, but here I am to keep you posted about what we've been up to these last days. 

![news](https://media.giphy.com/media/3o84sJXOIrnjvlwnF6/giphy.gif)

# What have we been up to?

We began the coding period with a video call with the mentors, as you might already know, **JuanLu** and **Jorge**. We got to know each other a little better, and we started to design what was ahead of our path.

![future](https://media.giphy.com/media/KZocN3LfuqktW/giphy.gif)

But, before dropping any line of code, we first had to think about what would be the best way to integrate the new features to **Poliastro community** in order to capture the desired requirements from an end-user perspective. After some deliberation, we came up with the idea of adding two new objects. 

![Spock](https://media.giphy.com/media/sBl8Fowq0ErFC/giphy.gif)

By now, I hope to have your attention as well as Spock's. So we created *EarthSatellite* and *Spacecraft*. Both of them would be vital to develop what's coming next for **Poliastro**. Did someone say **TLE**?. 

![Surprise](https://media.giphy.com/media/LPNNFDYNTgP3q1jcAK/giphy.gif)

 Still, you might want to check out EarthSatellite propagation considering J2's perturbation and the atmospheric drag. Sounds superb, right? In order to use it you might want to try:
 ```python
    from poliastro.earth.atmosphere import COESA76
    from poliastro.bodies import Earth
    from poliastro.earth import EarthSatellite
    from astropy import units as u
    from poliastro.twobody.orbit import Orbit
    from poliastro.earth.enums import EarthGravity
    from poliastro.spacecraft import Spacecraft


    tof = 1.0 * u.min 
    ss0 = Orbit.from_classical( Earth, 1000 * u.km, 0.75 * u.one,  63.4 * u.deg, 0 *u.deg, 270 * u.deg, 80 * u.deg)
    C_D = 2.2 * u.one  # dimentionless drag coefficient
    A = ((np.pi / 4.0) * (u.m ** 2)).to(u.km ** 2)
    m = 100 * u.kg 
    spacecraft = Spacecraft(A, C_D, m) #we create the spacecraft
    earth_satellite = EarthSatellite(ss0, spacecraft)
    orbit_with_atmosphere_and_J2 = earth_satellite.propagate(tof=tof, gravity=EarthGravity.J2, atmosphere=COESA76())
 ```

Nevertheless, this API is subject to changes, so before diving in, verify the documentation:)
See you in the next post, and stay safe :)
![Infinity](https://media.giphy.com/media/wPXW2MLFCTNF6/giphy.gif)
 
 
 

  
  
  
  
  
  