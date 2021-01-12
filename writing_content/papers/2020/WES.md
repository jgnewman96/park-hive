---
title: "WES: Agent-based User Interaction Simulation on Real Infrastructure"
date: 2020-09-06T11:31:51-07:00
draft: False
tags: ['Design']
categories: ['Papers']
---

[By Facebook Research](https://arxiv.org/abs/2004.05363)

### Papers Motivation

Large distributed software systems with many users interacting are difficult to fully test. There are large numbers of edge cases which are difficult to identify ahead of time. Lots of bugs arise from complex interactions between users and the software that only occur at scale.

### Papers Contribution

This paper outlines the general principles of web enabled simulations (WES). The development of Facebook's WW simulation is used to guide a discussion of WES in general. WES takes a different approach to software testing by focusing on user behavior rather than system behavior.

### Background
A web enabled simulation (WES) simulates the behavior of users on a software problem. WES simulations build on recent developments in reinforcement learning. Each user is modeled as an agent playing a game on the software platform. A multi-agent approach is taken where each bot simulates a user. The bot's behavior can be encapsulated in rules or via machine learning

The goal of a WES is similar to other software testing systems, to find and fix issues with the software. This environment is isolated from the production environment. This type of software testing can test bugs and features in a way that is not possible of other approaches. Facebook's WW tests what happens when users try to break the community standards. It allows Facebook to test their response to bad actors.

### Testing new Software Changes
**Scenario**: We want to understand the end user behavioral response to new privacy restrictions before they go into place. We use a WES to run simulations with the new policy and compare it to the old policy or slightly different policies.

WES facilities __Automated Mechanism Design__. If the new policy has a parameter we are trying to optimize, we can run many simulations with different values for that parameter.

Normal testing is focused on one user and their individual actions. This limits the ability to test features or bugs resulting from a communities actions. These __social bugs__ require a new form of testing: __Social Testing__. WES systems are well suited to social testing. Social Testing allows developers to test levels of abstraction higher than previously possible

### Facebook's WW
WW is an environment built at Facebook to test the reliability, integrity and privacy of their platforms.  Bots in WW only interact with FB's backend code and do not interact with the GUI at all. WW bots are trained using reinforcement learning. A bot takes an action in the environment and then the state, with an accompanying reward is returned to them. The bot then decides on another action aiming to maximize the received reward.

An example of how WW is used is to simulate scamming. For this simulation multiple bots are needed, The scammer and the target. The scamming bot is trying to find a target and scam them. Target bots follow a rule based system hopefully modeling what targets look like in the real world. The platform is measured in its ability to impede scammers from finding suitable targets

### Applications of WW

Currently WW is being used to test FB's ability to deal with bad actors. If bots find ways to post bad content or break other parts of FB's platforms then developers can stop real bad actors from taking a similar path in the future. WW does an automated search for mechanisms that impede bad actors.

WW can also be used to test certain metrics at scale. WW provides a final full ecosystem which allows testing of key platform metrics before a change is rolled out to users.

### Open Problems and Challenges

- How to better train bots to act like real users or bad actors?
    - We need realistic social interaction. Is a fitness function able to express this?
- How do we search the mechanism space to find optimal design?

## My Closing Thoughts

- Reading a paper every week with [Tushar](https://tusharc.dev/) has opened my eyes to all the different stages of research. Different papers take different approaches and convey different depths of information. A paper which is at the beginning of a research agenda, has a very different style than a paper building on a known field. This paper is a very early paper in its space. It proposes the idea of a WES with some further questions. I often can be critical of papers like this because it feels like there is so much more for them to contribute. But that can come in later papers. It is a losing battle to expect everything from one paper.

- One part of this paper I struggled with is how tied it is to a specific company. It seemed to go against the open source nature of research. Developing a WES seems very difficult and Facebook is only able to do so because they have an immense amount of resources. It would be difficult for anyone other than people at a company like Facebook to extend this research further. They also did not open source any of the code that went into developing WW. If WW was an open source platform that external parties could interact with, so much more could be learned about Facebook. How do certain design decisions that Facebook makes drive outcomes and what are the other possibilities?

- It is interesting that this paper focused so much on integrity. In my head there are so many questions that WW could answer that seem more exciting than integrity. I imagine that the team developing WW had to find a first use case to prove their direction is worthwhile. They were successful with integrity and will now build it for other use cases.
