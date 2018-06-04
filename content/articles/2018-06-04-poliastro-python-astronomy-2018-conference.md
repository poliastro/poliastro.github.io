Title: poliastro at the Python in Astronomy 2018 conference
Date: 2018-06-04 20:30 CEST
Tags: pyastro18, poliastro, conferences
slug: 2018-06-04-poliastro-python-astronomy-2018-conference
lang: en
Author: Juan Luis Cano Rodríguez

A month ago I had the privilege to attend the **Python in Astronomy 2018 conference**, which gave me an unique perspective of the status of Python in the astronomical sciences and an opportunity to present poliastro to a very technical audience. I was planning to post a writeup somewhere, and as the Zen of Python says...

```
$ python -c "import this" | grep Now
Now is better than never.
```

So, let's do it! 🚀

# What was Python in Astronomy?

**Python in Astronomy** (from now on, **PyAstro18**) is best explained in [its website](http://openastronomy.org/pyastro/2018/):

> This conference aims to bring a wide variety of people who use, develop or teach people about Python packages in the context of all forms of Astronomy. The conference will include presentations, tutorials, unconference sessions, and sprints. As well as enhancing the community around astronomical uses of Python, the conference aims to improve collaboration and interoperability between Python packages, and share knowledge on Python packages and techniques. It will also provide training and educational materials for users and developers of Python astronomy packages.

![PyAstro 2018 introduction](/images/pyastro-intro.jpg)

This year it was celebrated at the [Center for Computational Astrophysics](https://www.simonsfoundation.org/flatiron/center-for-computational-astrophysics/), a research center committed to developing the research tools needed for modern astronomy as part the Flatiron Institute, in New York.

I had heard about the conference perhaps last year, but this was the first edition I actually applied to attend, and I was selected! Not only did the organization pay for transportation and accommodation of _all_ the attendees (including yours truly), but also they did a wonderful job gathering a **diverse audience**, which made me extremely happy!

PyAstro is not an ordinary conference, and many types of sessions happened:

* **Keynotes**: Classical talks addressed to all the attendees, about an important topic and given by a relevant member of the community.
* **Unconferences/Tutorials**: Sessions proposed by the attendees during the event itself. There were moments during the week when we were asked to suggest topics on a whiteboard, do a "pitch" about them (i.e. explain why we wanted to discuss about those topics) and then vote. The ones that were more interactive, or encouraged the attendees to code something, were called tutorials. There were also people taking notes of the discussions and they were all summarized at the end of each day.
* **Lightning talks**: 5 minutes talks about _any_ topic that can be a great opportunity for first time speakers or people that want to show something in an humorous way.
* **Hack projects**: One day was entirely devoted to _hacking_! This meant that people could do sprint on a particular software package, explore new libraries, discuss complicated things in person, or just advance with their personal projects. In the same way as unconferences, the conclusions were summarized and presented the following day.

The best thing is that _you can read_ most of the content we generated during the conference [in this index and the linked documents!](https://docs.google.com/document/d/1DLgH9D-Wm-zgeRdPecE1_VtKnugkYyHAc5imwAptktk/edit?usp=sharing) This includes the summaries of the unconference sessions, the lightning talks list, the participants directory, pictures and more. Great, isn't it?

![Unconference sessions](/images/pyastro-unconference.jpg)

# poliastro + PyAstro18 = 🚀

I wanted to make the most of PyAstro18 and participate as much as I could, so before arriving to New York I already had a rough idea of my main goals for the event, which were:

1. Spread the word about poliastro and reach out to potential users,
2. Make a decision about the API of ecliptic reference frames in Astropy, which affects poliastro (see [this lengthy issue](https://github.com/astropy/astropy/pull/6508)),
3. Share my concerns about high level, performant code in Python, in particular the performance of `astropy.units` (which in some parts of poliastro is a bottleneck, see [this commit](https://github.com/poliastro/poliastro/commit/ed931adb)), and
4. Get to know the Astropy developers (and the rest of the community) in person and have fun!

With this in mind, apart from my scheduled talk about poliastro ([repo](https://github.com/poliastro/pyastro18-talk/)), I gave a lightning talk titled "That messy conversation about reference frames" inspired in [this lengthy issue in astropy.coordinates that is not over yet](https://github.com/astropy/astropy/pull/6508) ([repo](https://github.com/Juanlu001/messy-frames-talk)) and I co-chaired an unconference session about Parallelization, Cython, Measuring Python Performance and Identifying bottlenecks.

## Personal summary

Luckily, **poliastro** attracted some attention and I got many interesting question from the attendees. The golden moment of the week was when [Abbie Stevens](https://github.com/abigailStev) wrote "Where are you sitting? Someone has a question about orbital mechanics!" 💗 Also, [Charlie Payne](https://twitter.com/coachxcpayne) announced that [he had used poliastro with high school students to examine the Europa Clipper mission](https://twitter.com/coachxcpayne/status/997322543852814336) 💖

For my **hack day project**, I decided to work on the performance of `astropy.units`, doing some profiling with common use cases to identify hot spots and hopefully try to address some of them. I must give a special Thank You here to [Erik Tollerud](https://github.com/eteq), which was super kind and supportive all the time and always happy to give guidance even though he was doing a dozen things at the same time. I also worked a lot with [Manodeep Sinha](https://github.com/manodeep/), our optimization expert and "general pedant about coding", who gave lots of useful and interesting suggestions to optimize the code. The conclusions can be read in [this issue](https://github.com/astropy/astropy/issues/7438) and can be sumarized to "why the heck is `isinstance` so slow?".

Regarding the decision on the **ecliptic frames**, at one point I sat with [Adrian Price-Whelan](https://github.com/adrn) and Erik and figured out that 12 or 24 ecliptic frames would be too many (unsurprisingly), and that we would have to find a compromise using factory methods and trying to make common frames visibly documented. A straightforward solution that works for us is already in place in poliastro, but I hope I have enough time to work on this [before Astropy 3.1 feature freeze](https://github.com/astropy/astropy/wiki/Release-Calendar) and reach consensus with the rest of the Astropy core developers (since not all of them were at PyAstro18).

And finally, I think I managed to **meet lots of new people** and had some fun :) I found myself excited to find other Spanish-speaking people (special mention to [Carlos Alberto Gómez González](https://github.com/carlgogo), with whom I had a couple of funny anecdotes) and in general I was glad to meet people I usually interact with on GitHub, in person.

![I, Juanlu](/images/pyastro-juanlu.jpg)

## Some final thoughts

* There was a great atmosphere during the event: everybody was participating, the venue was just awesome, there were people from many different countries... **10/10** for the organization, they did a great job. 
* I was already aware of the huge **infrastructure** that the Astropy community has been developing throughout the years, but watching how easy it is to create a Python package using their templates was amazing ([check out their cookiecutter template](https://github.com/astropy/package-template), which was finished during the event!). I think it's very important that non-programmers have easy ways to sort out documentation, continuous integration, testing... This applies not only for scientists, but also for engineers whose day to day job involves coding.
* I discovered thanks to Adrian that the field of **galactic dynamics** shares some common problem with astrodynamics/orbital mechanics (check out his package [gala](http://gala.adrian.pw/en/latest/)). Also, [Miguel de Val-Borro](https://github.com/migueldvb) shared that he is about to start working on a Python package for small bodies research called [sbpy](https://github.com/mommermi/sbpy) that will need orbital element handling and easy access to HORIZONS data. There are more collaboration opportunities than I expected, and I only wish I had more time to advance on common interfaces. 
* I think _I was among the few non-astronomers, and also among the few people working in a private company_. It was a weird feeling at the beginning, and gave me a different perspective about what the incentives for using open source are, what are the common problems in academia... I've been wondered how to bring the open source philosophy closer to the engineering world for years now, and this event was so important for me in that respect.
* After this event I really want to collaborate more and more with the community. I already have a plan to reduce the number of commitments in other areas and work more closely with the scientific community.

![Group picture at PyAstro18](/images/pyastro-group.jpg)

**Looking forward to see you all at PyAstro19!**

_Per Python ad astra!_

