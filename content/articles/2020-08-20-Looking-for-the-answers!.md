Title: Looking for the answers!
Date: 2020-08-20 12:00 CEST
Tags: GSOC,GSOC20,Google,poliastro
slug: 2020-08-20-Looking-for-the-answers!
lang: en
Author: Meuge

Hey, folks! The last weeks were really exciting getting done an algorithm for ground-track orbit. After long days trying to find the perfect approach for Poliastro, we decided to give it a go bringing to life this [paper]([https://www.researchgate.net/publication/287869810_Daily_repeat-groundtrack_Mars_orbits)

![wow](https://media.giphy.com/media/gZBYbXHtVcYKs/giphy.gif)

# But everything it's not what it seems

Well, we thought it will be quite straightforward but much too learn still I have , right Master Yoda?  

![do-or-do-not](https://media.giphy.com/media/pvDp7Ewpzt0o8/giphy.gif)

So I am not gonna lie to you folks, it wasn't that easy, but as Rocky says, "Every champion was once a contender who refused to give up". So now you are gonna know how we solve it. Game on!  First things first, we needed to apply numerical analysis in order to obtain the roots of the equation, because given the complexity of the function, there was no other way around. 

![oh-no](https://media.giphy.com/media/xT5LMLMPdRh2VRNVLi/giphy.gif)

So we had to come up with a method which would be computationally efficient and optimal for this kind of problem. That's how LMS, Linear Mean Square, appeared on our door. We used VSSLMS, which is an enhanced LMS version that improves the convergence rate and mean-square error. You might recognize it as one of the main competitors to performance and accuracy of the Kalman Filter, but with the need for less computational power and easier maintenance. What's great about this algorithm is the capability of achieving the solution without the necessity of finding a bracket, since we have no idea which might be the right interval where the answer lies, in this case, we refer to the semi-major axis to acquire a ground-track orbit.
Another point of difficulty when trying to model the solution, it's each orbit's particularities. Such as $ecc=0$ or having an orbit with a critical angle or even $inc=0$.
Currently, the [PR]([https://github.com/poliastro/poliastro/pull/1002](https://github.com/poliastro/poliastro/pull/1002)) is its last stages of review so let's hope to have this feature soon. 

![yay](https://media1.tenor.com/images/b5c9fa0621cba99bbc1b5ee2f62802c2/tenor.gif?itemid=15917936)

I hope everything is fine at your end. See you soon 🚀