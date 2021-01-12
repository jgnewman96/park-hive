---
title: "What is Ai Literacy? Competencies and Design Considerations"
date: 2020-08-24T14:37:40-07:00
draft: False
tags: ['Design', 'Software Engineering']
categories: ['Papers']
---

[By Duri Long and Brian Magerko](https://static1.squarespace.com/static/53c69580e4b08011fc2337bf/t/5e2893e4a9d342214836e832/1579717605435/CHI+2020+AI+Literacy+Paper-Camera+Ready.pdf)

### Paper Motivation

Artificial Intelligence is increasingly integrated into user-facing technology but public understanding is limited. We need more research investigating what users need to effectively interact with AI and how to design learner centered AI technologies that increase user understanding.

### Paper Contribution

This paper formally defines AI literacy based on other existing research. The authors synthesize interdisciplinary research into a set of core competencies. They also make design suggestions for creating learner centered AI

## Background

End-users often lack the most fundamental understanding that they are interacting with AI. Researchers are beginning to address public misconceptions through inspecting how people make sense of AI.This paper takes a slightly different direction by identifying skills necessary in a future where AI transforms every aspect of our lives.

There has been lots of recent work on how to foster a better understanding of AI in groups with non-technical backgrounds and for people at a younger age.The “AI for K-12“ working has identified five big ideas to help teach each grade band what it needs to know about AI

1. Computers perceive the world through sensors
2. Agents maintain models/representations of the world and use them for reasoning
3. Computers can learn from data [^1]
4. Making agents interact with humans is a substantial challenge for AI developers
5. Applications can impact society in both positive and negative ways

While AI has existed as a field for over sixty years, most of the research on AI education for non-technical learners has been published in the last two years. The authors wanted to draw on more than just this recent work. They conducted an exploratory review of literature across multiple fields.

## What is AI Literacy?
The term literacy originally refers to the ability to express ourselves using written language. Literacy has the historically context of broadening access to knowledge and providing people with the ability to share and communicate.Literacy has come to be a term used to mean competency in a certain topic to effectively communicate: digital literacy, computational literacy, data literacy etc...

{{< quote >}}
We define AI literacy as a set of competencies that enables individuals to critically evaluate AI technologies; communicate and collaborate effectively with AI; and use AI as a tool online, at home, and in the workplace.

{{< /quote >}}

## Methodology
The authors conducted an exploratory review of interdisciplinary literature in order to define AI literacy competencies and design considerations for developers.

There search was guided by two questions
1. What do AI experts think people need to know about AI?
2. What existing misconceptions do non-technical learners have?

In the paper the authors describe in more detail how they searched for literature. [^2]


## Conceptual Framework

The authors divide their competencies and design consideration into five overarching themes. For each theme the authors listed some competencies and some design considerations.

1. What is AI?

- **Competency 1**: The ability to recognize AI
- **Competency 2**: The ability to reason about what it means to be intelligent
- **Competency 3**: Understanding that AI is interdisciplinary
- **Competency 4**: Understanding the difference between narrow and general AI

2. What can AI do?

- **Competency 5**: Understanding AI's current strengths and weaknesses. What domains does it excel in and what domains does it struggle in?
- **Competency 6**: Individuals should plan and think about what AI will look like in the future.

3. How does AI work?

- **Competency 7**: Understanding representations and how information is represented to a computer
- **Competency 8**: Understand how systems make a decision
- **Design Consideration 1**:  Information about the AI system, its state and what it is perceiving should be communicated to users
- **Competency 9**: Understand the different steps in training a Machine Learning system (e.g. model selection, training, testing and prediction)
- **Competency 10**: Understand humans role in creating AI
- **Design Consideration 2**: Simulate the agents algorithm with the individual. Put the individual in the place of the algorithm
- **Competency 11**: Basic Data Literacy
- **Competency 12**: Understand that learning happens from data
- **Competency 13**: Be critical interpreting data
- **Design Consideration 3**: Contextualize Data &rarr; How was data created and what is it used for?
- **Competency 14**: Robotic Agents can take action in the world
- **Competency 15**: Understanding how sensors communicate information to agents

4. How should AI be used?

- **Competency 16**: Identify and describe key ethical issues surrounding AI

5. How do people perceive AI?

- **Design Consideration 4**: Promote transparency in all parts of AI design
- **Design Consideration 5**: Unveil the inner mechanisms of the system to a user gradually
- **Competency 17**: Understand that agents are programmability
- **Design Consideration 6**: Provide opportunities for users to design and program
- **Design Consideration 7**: Consider individuals‘ competencies when designing an AI system
- **Design Consideration 8**: Encourage learners to be critical consumers of AI
- **Design Consideration 9**: Consider that end users might have different values and backgrounds
- **Design Consideration 10**: Provide support for parents teaching kids about AI
- **Design Consideration 11**: Design AI learning that fosters social interaction and collaboration
- **Design Consideration 12**: Consider leveraging learners interests, e.g. music or art to teach them about AI in a specific context
- **Design Consideration 13**: Acknowledge users preconceptions or biases that might come from media
- **Design Consideration 14**: Introduce perspective about AI that are not as popular in the media
- **Design Consideration 15**: Lower barriers to entry


## My Closing Thoughts

I am quite conflicted about this paper. Or not conflicted but disappointed. This paper had so much promise and aligns with a lot of my personal values about AI. It asks a really important question and surfaces some good ideas. But the paper was quite tough to read and the finally product felt more like a list then an actual framework. While a list is valuable and a good reference, a framework is often a lot more powerful.

A lot of AI research has focused on how can the AI community make AI better. Those are important questions but this paper takes a slightly different approach. It focuses on how to make the public better consumers of AI. I know personally being AI literate is quite powerful and love the attempt to define what it actually means to be AI literate.

I was hoping the paper would provide a framework rather than just a list of items. To me a framework gives a more hierarchical way of thinking about AI Literacy and maybe defines different levels of AI literacy. Here would be a quick stab from me at a framework. In order to understand AI you must understand there are four different parts that compromise AI.
1. A task
2. Data related to the task
3. An Optimization problem
4. An Algorithm related to all three of the above

Within each of these parts there are different depths to your understanding. As part of the task it is important to know what tasks AI is good at or bad at. Why can certain tasks be easily automated and others cannot. We can also assign some of their competencies to the data part. This kind of hierarchical framework makes it easier to focus on just one small section rather than a long laundry list.

Having this framework rather than the laundry list is important because it makes gaining AI Literacy more approachable. If you tell someone here is a list of 16 competencies you need, that seems like they will never be able to understand AI. But breaking it down into a couple of different parts makes it a lot more approachable.

I would LOVE LOVE LOVE to see future work where the authors of the paper used this research to design curriculum our courses and then got to iterate on their list and make it tighter.

When I was talking through this paper with [Tushar ](https://tusharc.dev/) one thing we discussed was how not all research has to do anything. While I might have wished for this paper to have done something slightly different, it provides an exciting jumping over point for future research. Taking this list of ideas and putting it into a teaching framework is a job for another paper potentially.


[^1]: Why is this only computers and not all agents? Humans also learn from data!

[^2]: While seeing the authors put down all of their search terms seemed kind of trite it was interesting to see them describe their search in granularity. It would be interesting to do a replication of this paper and see if you found similar sources or different ones.
