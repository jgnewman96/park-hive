---
title: "ODSC Keynotes"
date: 2019-10-31T08:22:50-07:00
draft: false
tags: ['Machine Learning']
categories: ['Talks']
---

## AI Lifecycle Model Management: Monitoring for Risk, Bias and Fairness

Talk given by [Sepideh Seifzadeh](https://community.ibm.com/community/user/people/sepideh-seifzadeh1)

The first keynote was about how can we as data scientists monitor for risk, bias and fairness. The speaker motivated the tech by saying that AI and data regulation is coming. There is more data being collected, Machine Learning capabilities have increased and the cost of storage is now a lot lower.

The speaker highlighted how we do not have defined mechanisms in place to handle when their are problems with AI. When AI makes a mistake who do we blame? Who is liable if a self driving car hurts someone. She then referenced the [COMPAS](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing) example of Machine Learning having higher false positive rates of a black defendant re-committing a crime.

The rest of the talk was focused on what can we do to better handle all of these difficulties. The speaker highlighted a lot of different tools IBM has developed to help with this process.

### My thoughts

Wow, I struggled with this talk a ton. It really felt like a sales pitch and not a talk dissecting the issues. Here are a couple of larger thoughts though.

The speaker said regulation for machine learning is coming and that is how she motivated the talk. I struggled with this motivation a lot. For me all of the things she talked about are not issues because there is going to be regulation, but rather because they are fundamental questions about how we use technology. It was kind of hard for me that the motivation was that regulation is coming. I also think using that motivation leads to a very different approach. Rather than getting at the fundamental questions and trying to answer them, we are worried about some body having rules for how we have to act. Would it be good for there to be some regulation or some principles established around all of this? Yes, 100% yes. But focusing on regulation and that us a motivation is fairly troubling to me.

It is interesting to see how aggressively IBM is moving into this space. I do not know much about IBM as a company but it seems like they are really trying to market themselves as place that cares about fairness and transparency and helping data scientists achieve that. To me having data scientists that work in accountable and transparent ways is not just about tools but about a shift in the way we think. Tools can obviously make that whole process easier though. It will be interesting to see how this space continues to develop. I personally believe a start up is probably better equipped to make good offerings in this space rather than IBM.

## AI and Security, Lessons, Challenges and Future Directions

Talk given by [Dawn Song](https://people.eecs.berkeley.edu/~dawnsong/) Professor at Berekely and founder of [Oasis labs](https://www.oasislabs.com/)

This talk was motivated about all of the advancements we have made with Deep Learning. Deep Learning is now in use in personal assistants and other places all through out our lives. As deep learning has grown as a field so has the security attacks aganist automated systems. The speaker referenced the [Mirai botnet](https://www.csoonline.com/article/3258748/the-mirai-botnet-explained-how-teen-scammers-and-cctv-cameras-almost-brought-down-the-internet.html) attack and how the growth in technology use makes us more susceptible to attackers.

From now on we should always know that there will be bad attackers. We should always assume that there will be someone who wants to abuse technology and use it for their own purposes. As we automate more systems that makes it easier for attackers to have power. When something is not automated, it is harder for an attacker to gain control or have as large of an impact.

The speaker highlighted there are two main ways to attack:

1. An integrity attack &rarr; cause a system to produce incorrect or specific outcomes
2. a confidentiality attack &rarr; Get sensitive information

When we build systems, we need to make them secure. The speaker than used the example of self driving cars. There has been [research](https://www.csoonline.com/article/3258748/the-mirai-botnet-explained-how-teen-scammers-and-cctv-cameras-almost-brought-down-the-internet.html) that shows how easy it is to make a self-driving car think a stop sign is actually something different. Dawn showed a video of how you could convince a car that a stop sign is actually a speed limit sign.

She then presented [another example](https://arxiv.org/pdf/1709.08693.pdf) of tricking a visual question answering system. The input is an image and question and then the system generates an answer. By simply adding noise to the image, the researchers were able to change the answer to the question.

These were both examples of integrity attacks. But there has also been research about confidentiality attacks. We need to build systems that maintain different privacy and were users have control over their data.

Differential privacy is defined at the following:

- We add one extra point to our data set, for example we add John's data point
- An algorithm is differentially private if the output of the algorithm is the same with and without John's data point.
- If John's data point changed the output of the algorithm a lot, then it is not differentially private.

There was a [morning paper write up](https://blog.acolyer.org/2019/09/23/the-secret-sharer/) about memorization in NLP systems and how we can extract secrets from training data.

There are lots of challenges to deploy algorithms which are differentially private. It can be hard to make these algorithms usable by non-experts and for them to integrate with our existing environments.

Oasis labs, is a company that has been putting together lots of different tools to help companies build secure systems.

There are many important questions about security still to answer and it is a large challenge that requires community effort.

### My thoughts

AI and ML is really just a tool. Anyone who talks about how great AI and ML is, is oversimplifying everything. Its a tool that can be used for both good and bad.

One big key though, that when something is automated you are giving more power to the system. By giving power to the system you are reducing friction to a bad actor. A bad actor is no able to more easily take control. Tech in general is something that reduces friction and makes it easier to accomplish things. By making it easier to accomplish tasks it also makes it easier for bad actors to inflict more damage.

This kind of work about the weaknesses in ML systems is so important. It highlights how these systems are not intelligent but just doing complicated pattern recognition.

To me this kind of work should but a large doubt in the mind of a lot of researchers. This work should not only motivate you to think about security, but recognize the limitations of our current approaches. If our current approaches can be fooled so easily, are these even the right approaches. Can we even call these systems intelligent?

While it is important for some people to be focusing on the security of the current systems we develop there should also be other researchers looking at this and saying, WOW &rarr; we need a totally different approach.

## Getting Specific About Algorithmic Bias

Talk given by [Rachel Thomas](https://www.linkedin.com/in/rachel-thomas-942a7923) founding director of the Center for Applied Data Ethics at USF and founder of fast.ai

Rachel began her talk by using the [Gender Shades](http://gendershades.org/) example of image classification doing much worse with african-american faces, specifically african-american women. Furthermore, amazon's facial recognition algorithm matched 28 members ofr congress to mugshots of criminals. The rate of incidence was much higher for congressman of color.

Rachel than talked about how bias or fairness are too abstract concepts. We need a more structure way to think about these things. She calls out the paper called [*A framework for understanding unintended consequences of machine learning*](https://arxiv.org/pdf/1901.10002.pdf) by Harini Suresh and John Guttag.

The face recognition example above is something called representation bias. Identifying the specific bias gives us a better way to conceptualize how we deal with bias. This was an example of representation bias because the training sets the algorithm used had more white men in them. It was also an example of evaluation bias. The bench mark data sets that were used to evaluate performance also had more light skinned men.

Now that we understand what type of bias is present we can do a better job getting rid of that bias. We can create more representative data sets which have more people of color in them.

* * *

The next example she used is the compass algorithm which had a false positive rate twice as high for black defendants. It had a false positive rate of 40 percent predicting that black defendants would re-offend when they did not. It was possible to get the same performance as the compass algorithm using a linear classifier with only three variables. Using more complex algorithms does not always increase performance that much but often decreases transparency and understanding.

Even though race was not an input into the compass algorithm, the algorithm found it as a latent variable. We have to be careful of this when we use complex algorithms.

When we implement machine learning systems we also have to be very careful about feedback loops. A feedback loop happens when the machine learning system impacts the next round of data that you see. The most intuitive example of this is a recommendation system. The recommendation system predict what content people would want to see and then shows that to them. But then we are using the content that people view to train the recommendation system. The recommendation system is then impacting what content people look at.

Another example of bias we have to be careful about is historical bias. Getting more data would not have mitigated the compass algorithm bias. The algorithm was biased because we have historically incarcerated higher numbers of black people. This is a historical and cultural bias that is ingrained in our systems that if we continue to use data naively will continue to be a part of our society. This highlights the necessity of working closely with domain experts. We have to work with the people who intricately know how these systems work. We should also involve the people who will actually be impacted by these systems into the design process.

* * * 

The third case study Rachel discussed was online ad delivery. Latanya Sweeney, a professor at Harvard wrote a [research paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2208240) about how the ads shown when you google certain names are different. When you googled a name associated with african-americans the add asked if you wanted to do a background check and see if they had been arrested. If you googled a more neutral sounding name, even for someone who had actually been arrested, it showed a more neutral ad.

The company responded by saying that they were allowing people to post both and then doing A/B testing. They would show the add that gets people to click on it more.

This example show cases how we have to be more carefully about what we optimize and the impacts it could have.

* * *

The fourth example Rachel referenced is a [paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5540263/) by Sendhil Mullainathon and Ziad Obermeyer looking at a system that predicted the likelihood of a stroke. The system that was implemented found that the following things where most predictive of if you were you going to have a stroke

1. have you previously had a stroke?
2. do you have cardiovascular disease
3. have you had an accidental injury?
4. Do you have a benign breast lump?
5. Have you had a colonoscopy?

The first two make sense as being predictive but why would the last three be predictive? It is because we are not actually measuring if someone has had a stroke. We are measuring if you had a stroke and then went to the hospital and reported. The last three predictive variables are measures of how much you use healthcare. This is an example of measurement bias in action.

* * *

We see historical bias all throughout society. Here are just three examples that are related to racial historical bias:

* When doctors are shown identical files for black and white patients they are less likely to give helpful recommendations to black patients
* If you apply to an apartment on craigslist with a name that is thought to be associated with being an african-american you are less likely to get a response
* When bargaining for a car, black people are offered higher prices on average

This might lead you to ask why does algorithmic bias matter, humans are biased too. Algorithmic bias is even more important than human bias because machine learning amplifies bias. We use machine learning differently than how humans are used. Machine learning is used at scale to do many things at once. It is much easier to appeal to a human being than to appeal to an algorithm. Also people are more likely to assume algorithms are fair. We recognize that humans are subjective, but we are less likely to see that in an automated system.

* * *
So know that we understand a lot more structurally about bias and fairness, how can we work towards a solution.

One good place to start is to analyze a project and find all the different biases and how they could be in that project. There are lots of different frameworks to try and do this but Rachel provided some questions she thinks are important to ask.

* Should we even build this? Sometimes the answer is just not to build something
* What bias are there in the data? All data is biased and it is important to recognize that
* Can the code and data be audited? Is it open source?
* What are the error rates for different subgroups?
* How accurate would a very simple alternative be?
* How do we handle appeals or mistakes?
* How diverse is the team that built it?



### My thoughts

This was one of the best talks I have ever seen. Rachel Thomas is such a good speaker and she created such a great talk. She did such a good job of having examples and depth but also driving home high level concepts. She also made the talk understandable to everyone.

I want to in the next coming weeks do what she suggested and examine a project and look at all the potential bias or fairness issues.
 

