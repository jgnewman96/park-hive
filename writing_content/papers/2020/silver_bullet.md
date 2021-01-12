---
title: "No Silver Bullet - Essence and Accident in Software Engineering"
date: 2020-01-29T11:48:28-08:00
draft: false
tags: ['Software Engineering']
categories: ['Papers']
---

[By Fredrick P Brooks](http://worrydream.com/refs/Brooks-NoSilverBullet.pdf)


## Summary

This paper was published in 1986 examining the difficulties of creating software. Brooks argues that there is no silver bullet to make software development a lot easier. The main things that are making software development hard are part of the essence of software development. Rather than aiming for a silver bullet that will greatly improve software development we should be making smaller iterative improvements.

Brooks argues that Moore's Law and a two fold increase in productivity each year is a fools goal for software. Software development is much more complex. Most of the largest gains in software development have already been gained. From here on out it will be smaller iterative improvements that take more time.

Brooks divides the difficulties of software development into two categories. This two category framework can actually be applied to the difficulties of any task.

1. Essence &rarr; difficulties inherent in the process
2. Accidents &rarr; difficulties that exist today but which are not inherent.

The difficulties that make up the essence of software development are how do we build something so complex. The difficulties are the specification of the design, getting concepts to work with each other and the testing of the construction. Syntactical errors are nothing relative to the difficulty of actually creating software. These are difficulties that will always exist because they are the essence of software development.

Brooks discusses four different parts of the essence

1. Complexity
    No two parts of a code base are the same. If they were it would be modularized and turned into one thing. Redundancy or repetition often makes it easier for us to understand things. The number of possible states in a program grows exponentially. This complexity is a key part of software systems and so we cannot just abstract this complexity away.

2. Conformity
    - The complexity of a software system is not explained by some underlying principle. The complexities are often driven by various complex human needs interacting with each other. There is not some underlying mechanism which if we understood, we would then understand the complexity software.

3. Changeability
    - Software is constantly changing and has changing requirements. This is dissimilar from most other manufactured products. With physical things, rather than changing them, they are often just superseded by a new model. While this can be an advantage of software it also adds lots of difficulties.

4. Invisibility
    - Software cannot be represented in the physical space. When we manufacture other goods we can represent them in physical space. We can make a diagram or a prototype. This makes it easier for humans to reason about it. While we could make a flow diagram for software it is nothing like being able to represent the full complexity  software in physical space.

* * *

#### Previous Breakthroughs

The previous solutions that made software development easier solved accident difficulties rather than essential difficulties.

- High Level Languages allowed us to think in layers of abstraction. They get us closer to thinking in terms that humans can understand but it does not get rid of the inherent complexity in reasoning about software. No matter the language we are using, the complexity of software will always be there. There is now just less work turning our thoughts into something the machine can understand.

- Time-sharing is actually a concept I had not heard of before. This is because this break through was so much before my time that I cannot imagine computing without it. Time-sharing means that multiple users can access the same resource at a time. This means there is less waiting time to use a resource and shortens the systems response time which makes it easier to develop.

- Unified Programming Environments such as unix allow us to use multiple programs together rather than having to use them all separately. They make it much easier for different parts to interact.

* * *

#### Proposals for Future Fixes

Brooks next discusses some proposals for future fixes and explains while they might be helpful none of them are silver bullets.

- **The language ADA**. I have actually never even heard of this language so clearly it did not end up being a silver bullet. Brooks argues that while this language might help make programming easier, it is no silver bullet. Each step we go higher in languages will be less of a gain than the step before it. Higher level languages are solving accidental difficulties and not essential difficulties.

- **Object Oriented Programming** is another fix that allows the designer to express an idea in a more native form. While this also will improve software development it will not be an enormous gain.

- **Artificial Intelligence** while a promising idea, is not going to solve all of our software development problems. Creating the data necessary for AI to create programs is quite difficult and we have not seen any promise of AI being able to do anything nearly as complicated as this. Brooks believes AI will be helpful by being supplemental to the coder and providing advice to them. There is too much heterogeneity in coding tasks for us to create an AI anytime soon that will be able to do software development for us.

- **Automatic Programming** is really just a higher level language. We still need to provide information for the program to be created. The information we are providing is just at a higher level.

- **Graphical or visual programming** is not a realistic goal because software is too difficult to visualize. While some parts of software can be broken down into a flow chart, this visualization will not be able to encompass everything. Generally, when programmers code, they do not make flow charts before hand but only afterwards forcing their program into an abstraction that is not well suited.

- **Program verification** will ease the testing load of the program but it will not be able to get rid of it. For very few programs are we actually able to verify that their behavior is correct. Testing is instead about providing evidence and we will still always want to do testing on our own.

- **Environments and tools** will help make programming easier in language specific contexts bu do not solve the inherent problem of programming. These returns will continue to be marginal and each continued return will be less and less.

- **More powerful work stations** might be helpful in speeding up the computation time but the most time intensive part of any developers day is thinking. A more powerful work station does not help with that.

* * *

#### Areas to Focus on

While Brooks has argued that there will not be a breakthrough that makes software development a lot easier, there will be steady progress over time. He highlights some areas that should lead to steady progress in our ability to develop software.

- When we can, we should **buy and not build**. We do not have to build everything from scratch but rather can re-use other things that people have built. This is a key part of being a software engineer. Recognizing when there are commonalities between tasks and being able to use other code.

- **Refining requirements through rapid prototyping** is the best way to build good software. The hardest part of any software project is defining the scope and specs. Clients often do not know what they want or need until after they interact with it. The best way to deal with these challenges is to put prototypes in front of clients and get there feedback.

- We should **grow rather than build software**. Software grows slowly piece by piece over time. Looking at how plants grow in nature is a better metaphor than how humans build. Humans build with a ton of planning and then rote execution. Growing is not completely planned out but rather changes based on the environment around it.

- It is critical we cultivate an environment that promotes **great designers**. We should recognize we have an active role to play in inspiring people to be creative. We can teach good design, but it is much harder to teach great design. A lot of the most incredible software was developed by individuals in isolation because there ideas were not molded to what had come before them. Too much of the business world is focused on making managers and rewards managers a lot more than great designers. We want to develop a culture that rewards and promotes great design.

## Thoughts

- I understand why this is such a seminal piece and in a lot of ways feels very ahead of it's time. I am very oblivious to what the state of computing was in 1986 but so much of what Brooks argues still rings true today. This is just further confirmation about the essential complexities in software design. Brooks is able to pick apart what parts of software design are always going to be challenges.

- It often seems like our society has such a focus on making progress that we do not take a step back and think about where it is possible to make progress. Brooks identifies areas in software development we will struggle to make progress on because they are inherent difficulties. By taking the approach that Brooks does, we would be able to find what are the areas that make the most sense for us to invest our time in. We should take this approach with almost all things. People are constantly calling for quick fixes that can make large differences. This view probably over states the impact of any fix. It would be really good practice for me to examine something in more detail and find what are the accidental difficulties and what are the essential difficulties. I might try to do this with a different environment or task at some point.

- I was really interested in Brooks advise to buy and not build because it comes up constantly in my day to day. When I use a python library, I am using something that someone else built rather than creating something completely from scratch. We also see this all the time with Software as a Service or the Cloud being such a huge business now. Rather than building our own version from scratch we buy it from someone else. I have been struggling with this for a bit because so many places are trying to sell their own Machine Learning Platform. I am tempted to maybe follow Brooks' advise but I have also not really seen a platform that fits any of my use cases.

- An idea that Brooks hints at but does not discuss in depth because it is outside his scope is why humans struggle so much with the complexity of software. Software is so different from the physical world that we interact with on a daily basis. We are used to thinking about concepts in the physical world and interaction in our day-to-day. Due to software being so different from our day-to-day we cannot reason about it. But just because humans are not able to reason about software does not mean that will be the case for all forms of intelligence. While artificial intelligence is still very far away from being able to reason about software, I do believe there is some form of intelligence that could create much more beautiful and impressive software than humans.

- The way Brooks is taking about making improvements reminds me of the 80-20 law. For the first 80 percent gain it takes 20 percent of the effort and then the last 20 percent gain comes with 80 percent of the effort. Essentially the beginning gains we make are the easiest and then each gain after that is harder and harder. This is true in so many places not just the software world. Even when it seems like there was some large break through that made a huge gain often that break through comes from a lot of unseen work over time. This really enforces why Moore's Law is do different. I cannot think of many other examples of where progress was similar to Moore's Law. I would be interested to explore what makes Moore's Law so unique and how it has sustained progress in that way.