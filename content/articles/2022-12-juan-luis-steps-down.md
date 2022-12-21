Title: Juan Luis steps down as maintainer of the project
Date: 2022-12-21 19:00 CET
Tags: poliastro
slug: juan-luis-steps-down
lang: en
Author: Juan Luis Cano Rodríguez

Today is [Volunteer Responsibility Amnesty Day](https://www.volunteeramnestyday.net/),
and with a heavy heart I, [Juan Luis](https://github.com/astrojuanlu/), would like to announce
that I am stepping down as maintainer of poliastro, almost a decade after creating the project.

Some of you might find this surprising, some others may have seen this coming for some time.
This is a continuation of my decision to
[step down as co-maintainer of `astropy.coordinates`](https://github.com/astropy/astropy.github.com/pull/452#issuecomment-961131035)
a year ago, and a realization of the fact that
I have been spending less and less time in poliastro in the past months.

Before getting into details about why stepping down now,
I would like to comfort existing users by saying that I spoke to
[Jorge Martínez](https://github.com/jorgepiloto/),
co-maintainer since he started as a Google Summer of Code Student in 2018-2019,
and he accepted taking over the maintenance of the project.
The pace will still be slow for a while until Jorge finds a good work-life balance
and sorts out his own personal circumstances.
On a personal note, Jorge is one of the kindest and most brilliant people I have ever met,
and I am sure the project is in good hands.

When I evolved poliastro beyond a disorganized collection of MATLAB and FORTRAN scripts
glued together with Python, I wanted to prove several things:
that a pure-Python package could be "fast enough" for most use cases;
that it was possible to define a friendly, yet rigorous API
that would lower the barrier of entry for Astrodynamics;
that making the effort of maintaining the code over an extended period of time
and resisting the urge of abandoning it would attract users;
and that we could collectively rescue decades of scientific progress
from the oblivion of paywalled journals and obscure PDFs
and turn it into well tested, carefully validated, reasonably documented, open source code.
From this point of view, I think poliastro has been a great success:
it's been used by [the creators of STK](https://github.com/AnalyticalGraphicsInc/STKCodeExamples/blob/466c139/StkAutomation/Python/Scenario_Analysis/Lifetime%20Analysis/RunLifetimeAnalysis.ipynb#L30),
[IBM Space Tech](https://github.com/IBM/spacetech-ssa),
[Satellogic](https://github.com/satellogic/orbit-predictor/blob/686af07/orbit_predictor/keplerian.py#L24),
[the Libre Space Foundation](https://gitlab.com/librespacefoundation/polaris/vinvelivaanilai),
and many other relevant companies in the space sector.
In fact, I would say that my biggest achievement with poliastro is that 
many people's first contact with GitHub was to open an issue in our repository.
All of this wouldn't have been possible without a supportive community,
funding from various entities (the European Space Agency, Google Summer of Code, and NumFOCUS),
and our dear students over the years.
I'm incredibly proud and thankful of all the things we have achieved together over the past decade.

And yet, I feel it is the moment to step down as the maintainer of the project and focus on other things.
There are numerous reasons for my decision, and it is something I have meditated for a very long time.

To start, it has been very difficult to find a consistent audience for poliastro.
When I presented the project at PyCon, PyData, and SciPy events,
everybody told me that poliastro was really cool (we put a lot of effort into those plots!)
but we never met people with the skills, time, and motivation to contribute
(some of them had the skills but no time, and viceversa).
The one time I presented it at an industry conference
I felt tiny compared to bigger projects like Orekit, let alone commercial ones,
and didn't get much feedback.
And finally, when I reached out to the few alive scientists that had worked on astrodynamics
projects that were within our reach, I got very little help
(the one exception being David A. Vallado, who always replied promptly to my emails
and showed genuine excitement and encouragement and to whom I am deeply thankful).
It has always been too much astrodynamics for software engineers,
and too much software engineering for astrodynamicists.
This is not new of open source computational science projects,
with the difference that I was not working in academia,
and most of the time I didn't even have direct connection with people using it for real projects.
The icing in the cake, sadly, were space companies that told me they were using poliastro,
but when I asked them for a brief testimonial, they never replied.

For people as privileged as myself, that can afford to spend afternoons and weekends writing code for free,
the currency for volunteering work is sometimes very intangible: a bit of recognition can go a long way.
At the same time, I know I could have been much more persistent, reached out to industry actors directly,
established more clear ways to contribute to the project,
secured a business model that didn't rely on grants. I don't want to somehow convey that
I tried everything I could think of: in fact, there are so many ideas that could make
poliastro more sustainable. This is very good news: it means that someone else can try them out!

At the technical level, poliastro is now more mature and it has started to hit several bottlenecks:
the performance of `astropy.units`, the complexity of `astropy.coordinates`,
the limitations of `numba`, the overhead of `numpy` for small arrays,
and the lack of maintainers for `scipy.integrate`, to name a few.
There are various unfinished prototypes that try to move past these bottlenecks:
[a (hopefully) faster units package](https://github.com/astrojuanlu/fastunits/),
[a proof of concept of a simpler coordinate frames implementation](https://github.com/astrojuanlu/astropy/commit/f7873c5a),
[an attempt of replacing small arrays by tuples](https://github.com/pleiszenburg/bulk_propagate/blob/master/test_notation.ipynb),
[conversations with a numba-accelerated ODE integration library](https://github.com/hgrecco/numbakit-ode/).
But at this point, experiments and proofs of concept are no longer enough:
for poliastro to keep moving forward it is essential to keep pushing these ideas
and contribute to the upstream dependencies, which requires patience, dedication, time, and focus.

Finally, I found it extremely hard to reconcile my ardent passion for space
with the reality of the space industry. When I was younger, inspired by the wonderful works of Carl Sagan
and ideas behind the Moon Treaty, I thought that space exploration would help humanity achieve world peace,
and that we would venture the Solar System in a peaceful, cooperative way.
In addition, I truly believed that space observation would help us tackle the climate emergency,
humanity's most important and pressing problem.
What we got instead was the militarization of space with the creation of the US Space Force,
the rolling of the Artemis Accords aligned with the US interests,
a new space race of bored tech billionaires,
fervent adoration towards Elon Musk despite being the most toxic CEO of our times,
[the US military being the main customer of space observation companies](https://joemorrison.substack.com/p/the-commercial-satellite-imagery),
and in general a reek of long-termism and tech solutionism I can't stand anymore.
I got exhausted of the space industry and I don't plan to go back,
which made my involvement in poliastro even more meaningless.

Despite these bittersweet lines, I am incredibly thankful of having spent the past decade
developing poliastro, learning from the broader open source community,
and working with kind and passionate human beings
(I especially miss my Argentinian colleagues from Satellogic so very much).
I am looking forward to spending the next decade applying these learnings to
accelerate the [Solidarity Economy](https://solidarityeconomyprinciples.org/)
and working towards a sustainable, regenerative future.

_Per Python ad astra!_

