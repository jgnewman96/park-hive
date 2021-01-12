---
title: "Studying_simple_systems"
date: 2019-11-04T16:10:10-08:00
draft: true
tags: 
categories: ['Research']
---



This is a combination of a lot of different things coming together into one project 

we have to put our assumptions first and make an actual judgement 

we want to study complex systems and try to not reduce the complexity 

we want to open ourselves up to be wrong and be corrected and iterate

We want to be able to understand things slightly better, it is not about having a complete and full understanding but just a partially improved understand 

So i think reading either the notes I took on Michael Jordans talk or the article I sent you earlier might help conceptualize some of what I am going to say, but not sure its necessary. At a high level though, if you havent noticed I am very interested in working on a project with you. I have always found that a learn a ton working with you and I think it is really fun to work together. I also think it would be really good to keep working together even after I leave Nielsen We could just work on kaggle competitions or problems involving data, but I think both of us are more interested in larger research questions. We are interested in questions of HCI and systems. We want to understand how systems function and how does technology interact with humans. While working on data problems is fun and enlightening they are often very narrow in scope. Also that is what I imagine we will both be doing in our day job, so maybe not as good to take on in our side projects
Obviosuly because these questions are larger and more nebulous, they are a lot harder to answer. Just working on a data problem is a lot more straightforward and easy for us to work on, but just because something is hard does not mean we should not do it.
While yes most research happens in academic settings. I truly believe there is no reason that you and I cannot do research while both working for a company, Yes it might be slow because we cannot devote enough time, but I think it can be done. Also research does not have to follow traditional methods. Like we do not have to write a research paper. Research is not defined by what the output is. It is defined by the approach and the process.
But how do we answer these larger questions about systems. A lot of HCI research involves running human subject studies. THis allows us to examine how people actually interact with this systems and what their outcomes are. We cannot really run human subject studies because we do not have the resources. Well actually we probably could use Mturk if we wanted to, but thats a question for another time.
I have been thinking about that gelman blog post that you sent me earlier today. It was so simple yet it shined so much light and showed so much. Maybe it did that because it was so simple. I was thinking about how can you use very simple systems to try and answer larger questions
So that was a lot of motivation and how I reached this line of thinking, but let me get down to the bread and butter.
What we are actually interested in is these larger systems and how humans interact with them. How can we gain information about them and make inference. Ideally we could just observe them, but that is really hard, But what about simulating approximations of them and using that to guide our answers. Research does not have to fully answer a question, it just needs to provide evidence and then follow up research can provide more evidence. One paper does not have to do everything.
So what I am saying is lets begin by designing a very simple system with agents in it. Lets observe outcomes with certain assumptions, and then slightly tweak those assumptions and see how outcomes change. Lets start out by making this as simple as possible. Agents in this system are as simple as possible and their actions are as simple as possible.
This is still kind of nebulous so lets ground it in one of the questions you said you were interested in
one thing you said you were interested in was
How do we build tools for content moderation and fact checking at scale?
so lets build a system that does this, (in a second you will see this connect to data generating process)
Lets imagine we have actors, that both produce content and consume content

For content produced it can either be legitimate or not legitimate

for contain consumed individuals can either believe it, or not believe it

We can parameterize all of these with different values.

Lets than run the system and see how disinformation spreads?

maybe we introduce content moderation in the form of some real content also getting filtered out, or maybe content moderation has impacts on how people consume content? We can really add any constraints or changes that we want

we can then run the system and see how the output changes

Do you see how this connects to thinking about the data generating process for a data science process?

we could also use a similar approach for your question of

What is the extent of filter bubbles on Reddit? How much does self-selecting subreddits limit the information you are exposed to?

We can model this in behavior in reddit with agents

I think the key will be to start out as simple as possible and with very well defined use cases

Let me know your thoughts on all of this. TBH it seems pretty doable to me and SO SO interesting.

If we ever wanted to actually write a research paper or anything we would have to do read the related literature and everything, but just from a baseline this seems to me to be a super feasible thing we could do to try and answer some questions we are interested in.

