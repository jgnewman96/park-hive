---
title: "A Fair Algorithm is not Sufficient"
date: 2020-07-19T10:52:00-05:00
draft: False
tags: ['Reflections', 'Machine Learning']
categories: ['Research']
---

For the past two weeks, I have been working through __Me & White Supremacy__, Layla Saed's month long interrogation of white supremacy. I am reading the book, journaling each day and then meeting with a group of co-workers weekly to discuss our experience. While journaling, I noticed my tendency to gravitate toward simple solutions. The chapters about tone policing and cultural appropriation were quite challenged.  I was looking for specific guidelines about what my behavior should look like. A checklist to tell me when something was or was not cultural appropriation. Explicit guidance that I could always follow.

This is both an unfair and doomed proposition. It is unfair because my actions and behavior are my own responsibility. Asking someone else to inform me of the correct way to act in all situations is unsustainable. Each situation comes with its own intricacies and complications. Just following a checklist will not be sufficient. There will be situations where the checklist leads me astray. Instead it is important for me to process the context in realtime and evaluate the situation in front me.

The real problem with relying on check lists is that it offloads the decision making process. When I use a checklist I am no longer grappling with difficult questions. The checklist is doing all the work.

Asserting myself, versus taking a back seat in a conversation is heavily dependent on who else is in their room. Making an appropriate decision is dependent on understanding other individuals‘ histories and our group dynamic as a whole. If I make that decision using a checklist I am processing information in a different way. Using the checklist means I am more concerned with my actions being perceived as the right ones, rather than having an understanding of the situation. I can say "look I went through the checklist therefore my actions are defensible".

These reflections reminded me of Rhonda V Magee's messages about radical complexity. At a [meditation retreat](/writing/talks/mindfulness/med_social_rhonda/) I attended earlier this year, she talked about how the world is radically complex. But we have not been taught to hold that radical complexity and examine it. We have been taught to simplify it. To simplify situations so we can run them through a checklist and then make a decision. But this simplification will always lead mean missing part of the full picture. It deludes us that what matters is making the correct decision and not also what goes into that decision

***

After reading this [article](https://www.nature.com/articles/d41586-020-02003-2) by Pratyusha Kalluri I am reflecting on how the AI community might be following into a similar trap with “Fair AI“.

Fair AI research is focused on evaluating algorithms for systematic bias. Is the error rate different for different populations? Does the algorithm use certain protected traits such as race or gender to make a decision? Research about fairness in AI systems has exploded in the past few years. I do not want to downplay the importance of this work. Lots of researchers are asking very important questions that need to be asked. But I do wonder if this work is deluding both people inside and outside of the AI community.

Is it important that we use algorithms which are fair by these definitions? Yes! But does having a supposedly fair algorithm mean it is safe to use? No. Algorithms passing these specific tests are only a small part of the picture. We should refrain from and be skeptical of any checklist that people can use to determine if an algorithm is useful.

This view of fairness comes from us wanting to move past radical complexity. We tend to gravitate towards simple solutions for difficult problems. While it might be a necessary condition that our algorithm passes certain checks, it is not sufficient. When AI is implemented it will always be part of a larger system. We must interrogate AI in that larger framework.

***
We can use a case study to help ground our thinking. Here is a [NY Times article](https://www.nytimes.com/2020/06/24/technology/facial-recognition-arrest.html) about an instance where AI usage went terribly wrong. It led to a man being arrested for a crime that he did not commit. While it is easy to read this article and call for “Fair AI“, a fair algorithm would not have solved all of the problems here.

The article mentions that research has shown algorithms are less accurate for black individuals than for white ones because of bias in training data. But even if that were not the case, and the algorithm had passed the fairness check, AI still would have been misused in this context. Similarly there is a quote in the article suggesting that the problems would be solved if law enforcement bought the good facial recognition algorithms rather than the bad ones.

The real problems is that the people using the technology have minimal understanding of it. The company that contracts with the police department has no transparency and did not develop the algorithms. The  police officers who were using the output of the algorithm knew nothing about it. They did not have insight into how often it is wrong. When people using the output of an algorithm know nothing about it, the algorithm is more likely to be misused. The people who develop technology are responsible for overseeing how it is used.

***

Even if an algorithm is fair and the people using it know a lot about it, it might still be a bad idea to deploy the algorithm. It is possible that it will be used to surveil or damage certain populations. Successful development and deployment of AI depends on asking questions not specific to algorithms. It is essential to be asking questions about the system that the algorithm is operating in as well as the algorithm itself.

- Who is developing this technology?
    - What is their background?
    - Where other voices involved?
- What is driving the development of this technology?
    - What funded this work?
    - What principles were leading the development?
- Where will this technology be implemented?
    - Were the use cases clearly specified by the developer?
    - Are the developers part of the implementation of the algorithm or only the development of it?
- How will this technology be used and who will be in charge of maintaining it?
    - Is the output of the system feed into another system?
    - Who acts on the output of the system?
    - How much knowledge do the people that are using the system have about the development of the systems?

***

- When we ask these questions about the larger system rather than just the algorithm, we have a better chance of uncovering problems with AI adoption.  The current approach to fairness focuses too much on the internals of the algorithm. The AI community must proactively ask questions outside the scope of the algorithm.

If we look at some characteristics of the larger AI community we can notice dangerous trends.

- Who is developing Artificial Intelligence?
    - The Elite! Wealthy people either at large organizations or academic institutions. The field is not diverse and is mostly white and male.
- What is driving the development of this technology?
    - Profit! People are developing AI for the benefit of large organizations. Rarely is AI being developed because of the ways it could help people. The focus is on automation. Not how the automation could unlock opportunities for people.
- How will this technology be used and who will be in charge of maintaining it?
    - The technology is often being implemented by people who have very little knowledge of it. They often do not know how it works and the potential dangers.

If AI researchers truly want to see AI be a force for good they need to start working with communities and pushing themselves to do more difficult things. They need to be more aware of larger societal structures and recognize that you have a responsibility for how your technology is going to be used. While research on algorithmic fairness is important, it will never be enough. Adoption of AI in a harmonious and beneficial way is dependent on large contextual questions about complex systems.

