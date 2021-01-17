---
title: "Street-Level Algorithms: A Theory at the Gaps Between Policy and Decisions"
date: 2021-01-17
tags: ['ai policy', 'politics']
categories: ['paper']
---
[Paper Link](https://hci.stanford.edu/publications/2019/streetlevelalgorithms/streetlevelalgorithms-chi2019.pdf)

By [Ali Alkhatib](https://ali-alkhatib.com/) and [Michael Bernstein](https://hci.stanford.edu/msb/)

### Paper Motivation

A major difficulty for algorithms is bridging the gap from where they were trained to to where they are going to be applied. Often that real-world scenario is quite different from that online environment where they were created.

### Paper Contribution

The authors of this paper draw on the theory of __street-level bureaucracies__, how humans such as police and judges interpret policies on the ground. The authors argue that __street-level algorithms__ can only refine themselves after a decision has been made. Bureaucrats on the other hand can reflect and make a response to a novel situation. Algorithms therefore experience a delay in response which can lead to illogical decisions.

The authors then make suggestions about designs for __street-level algorithms__ based on this theory.

### Background

Humans have continually reacted with surprise and frustration when algorithmic systems make decisions that they disagree with. Many researchers have taken different approaches aiming to alleviate that frustration and diminish surprises.
This paper argues that regardless of progress in other research directions such as fairness, accountability or transparency, algorithms will always encounter decisions that are __at the margin__. Even fair and transparent algorithms will make non-sensical decision when the data is quite different from its training data. [^1]

“Filling in the gaps“ or doing inference on novel data is not unique to algorithms. A __street-level bureaucrat__ is someone who directly interacts with people. They are tasked with making the bridge between legislature and the situation in front of them. These decisions turn __defined policies__ into the __effective policy__ that people experience. We have certain expectations about when we will a receive ticket based on how police officers enforce speeding law. In Michael Lipsky's book [Street Level Bureaucracy](https://www.amazon.com/Street-Level-Bureaucracy-Dilemmas-Individual/dp/0871545268) from 1983 he highlighted the important role of these street-level bureaucrats.

The authors argue that we could benefit from thinking about agents in technological systems as similar to street-level bureaucrats. The authors then pose the question, so why are people so upset by street-level algorithms and not street-level bureaucrats? [^2]

__Street-level algorithms__ fail where __street-level bureaucrats__ do not because algorithms can only refine themselves after making a decision and receiving feedback. Bureaucrats on the other hand have the ability to practice discretion. They understand their role in a system and the impact their decision might have.

### Case Studies

The authors focus on three case studies to show how this framework for thinking about algorithmic decisions can applied broadly.

###### Youtube's demonetization system

Youtube has many content policies that it enforces algorithmically. Machine Learning determines if content violates copyright and whether it violates their “advertiser-friendly content guidelines.“ If a video does not meet their guidelines it can not be monetized.Youtube began labeling videos uploaded by transgender users as “sexually explicit“ and therefore ineligible to be monetized. Based on testing users found that posts became ineligible for monetization if the title of the post included the word “transgender“ [^3].

The authors argue that since transgender people speaking in public about deeply personal aspects of their lives is new, the youtube algorithm was behind the curve. Since culture is constantly shifting having new data will not fix this problem. The algorithm will always be behind. When street-level algorithms mishandle situations users will find ways to circumvent them.

###### Management of workers in online labor markets

Crowd work - through platforms like Amazon Mechanical Turk - has become a source of income for many workers. Most tasks on crowd work platforms involve some sort of quality control. There have been examples of this quality control denying payment to workers who completed the task in good faith. The algorithms definition of success was too narrow.

With complex tasks it is quite difficult to define a precise and comprehensive success metric. The algorithm is unable to distinguish novel answers from wrong answers. Often the algorithm can only see if this work is similar to other work, not if the work meets the proper success criteria.

###### Bias in judicial bail recommendation systems

American Courts have turned to algorithmic systems to set the level of bail for a defendant. The goal of these systems is reduce jailing rates while having no increase in resulting crime rates [^4] Observers have shown that bail recommendation systems have perpetuated existing prejudices in the criminal justice system.

Our society insists on a right to trial because we recognize that everyone situation is unique and we cannot encode decisions from features. It is difficult for an algorithm to understand if a situation is novel or similar to what it has seen in the past. [^5]

### Design Implications

The authors argue that the same theme can be seen in all three of the case studies. An algorithm is unable to reflect on its decision criteria when presented with a novel situation.

The authors argue that there are some situations which algorithms should work in. It is key that we can accurately identify those situations. If the situation requires discretion and flexibility then currently it is not a good fit for an algorithm.

Another essential element is the ability to appeal and have recourse. Developing robust mechanism for recourse with street level algorithms is an important area for further research. Good recourse necessitates an understanding of how a decision was made and why it was a mistake. This requires the algorithm to explain why it made a certain decision.

## My Closing Thoughts

This paper stoked a lot of thoughts in me! I am not sure if that means it was a good paper or not though. I really appreciated the case studies in the paper as they provide concrete examples we can ground our thinking in. On the whole I think the framework the paper introduces is a helpful and reflective one, but I would probably have picked some different areas to think about.

Early in the paper, the authors say that street-level bureaucrats take defined policy and turn it into effective policy. But in the case of street-level algorithms the authors never discuss what the defined policy is! With street-level bureaucrats the defined policy is normally same piece of legislature. With street-level algorithms the defined policy is much harder to define and is inscrutable. It is the training data, the objective function and the algorithm. I think this lack of a clear defined policy is actually the more problematic part, not the fact that algorithms are not able to reflect.

This lack of defined policy is part of what makes recourse so hard. We do not even have a clear understanding of what the algorithm is supposed to be doing! In the youtube example, is the problem that the algorithm failed to translate the defined policy into a proper effective policy? I would imagine the real problem is that the defined policy is flawed. The training data probably has examples of videos with the word transgender in the title being labeled as sexually explicit. So the real problem is the defined policy being out of date. We face similar problems with laws and them becoming out of date. Because people enforce the laws though, this is less problematic. We do not need to follow the letter of the law but can have the same words mean something different over time. But overall, that does not seem like a good solution. It leads to debate about what the law actually means and leads to uneven enforcement. Just because it is what is happening right now does not mean it is something we should aim for.

I wish this paper had pushed us to think about what an ideal situation would look like rather than just thinking about how algorithms are missing out currently. Our current situation is clearly not ideal. Sitting here in 2021 seeing all the calls about how our criminal justice systems is broken it is difficult to have a positive feeling toward street-level bureaucrats. Street-level algorithms provide a world of new possibilities. Yes, there will be a lot of difficulties we have to figure out with them, and they will not work for a lot of use cases. But we actually have the ability to make policy that is consistent.

I mentioned this in a side note, but in this whole paper the authors are talking about generalization. But they did not frame it as such. They were trying to make the point that the problem of generalization is not unique to algorithms. Humans do it all the time and here is an example of it with literature discussing it. Lets use that framework to help us think about generalization in an algorithmic context.

In my head a really nice set up would be the following. We have an algorithm that is doing a task and when it encounters a novel example or when it has low confidence, it kicks out the decision to a human. Then a human can make a judgement on that situation. The authors seem to not really believe this type of solution is attainable.

The authors get at the following idea a couple of times in the paper, there are things algorithms are good at and there are things humans are good at. We should assign responsibility based on that. I appreciate this framing to some extent. One difficulty with it though is that what algorithms are good at is constantly changing.


[^1]: The authors do not mention generalizablility or robustness here. I will return to this later but I think they should have framed their argument differently. Rather than not bringing up generalizability, they should have stated that they believe an algorithm will never be fully generalizable. That is essentially what they end up arguing any ways.

[^2]: Is this even true? Are people that more upset about algorithms than people. I know that the media likes to cover algorithms more. But I know also that people have lots of problems with street-level bureaucrats.

[^3]: Is this really a problem of the algorithm not understanding the policy? This more seems like a situation of out of date policy.

[^4]: Is there anyone who has done a holistic look at these systems. I know there have been so high profile instances of them being biased but I would be really curious to see some other performance metrics.

[^5]: The authors of the paper seem confident we could not build algorithms that properly assess their own confidence. I am curious where this assertion comes from.