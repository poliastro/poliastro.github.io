Title: Adding the Altitude, Latitude, and Eclipse event detectors
Date: 2021-07-19 12:00 IST
Category: GSOC
Tags: GSOC, GSOC21, poliastro
slug: adding-ale-event-detectors
lang: en
Author: Yash

It was an engaging first half of GSoC, and it was during this duration, I understood some critical details of executing the event detectors. We started to look into the eclipse detector since we thought it might be challenging to get it right.

In the weekly community calls, we brainstormed over an appropriate method that would fit in poliastro. Thanks to SciPy’s events support through `solve_ivp`, we just had to come up with a time-varying and continuous “shadow” function without having to solve analytical equations manually. However, the critical challenge for us was to come up with such an equation! After a few trials of geometric manipulations and Jorge and Juanlu’s assistance, we came across an equation involving classical orbital elements that could serve our purpose. We were still questioning the performance and complexity of the method since by enacting it, we could lose the accuracy of entry and exit times of the event. In any case, the other approaches didn’t seem to work just yet, so we decided to go with this approach since it looked feasible. However, we figured out that the whole implementation could be jitted, thus considerably mitigating the issue.

While working on the eclipse event, we worked on the altitude and latitude crossing detectors. Realizing the base structure of all the events would be the same, and the already existing `Lithobrake` event would be a particular case of the `AltitudeCrossEvent`, we refactored the `events` module by removing boilerplate code to prevent redundancy. The logic of `LatitudeCrossEvent` could get substantially shorter due to the `cartesian_to_ellipsoidal` method, which allowed us to convert the cartesian coordinates of an orbit to its corresponding latitude on the attractor. Since we felt more intricacies in the longitude detector, we are taking some time to think about an appropriate method to solve it. All the events are supposed to work for any attractor, thus aligning with one of the poliastro’s aims of having capabilities not restricted to the Earth.

Leveraging some in-built functionalities of `solve_ivp`, users could stop integration if an event is detected or control the direction of triggering the event. Fortunately, Jorge simultaneously developed validation cases to check against the Orekit software, by which we became confident of the implementation.

Additionally, adding some tests, fixing some minor bugs, and making a few improvements in computation was insightful. There are more event detectors yet to come, so looking forward to it!
