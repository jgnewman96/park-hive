---
title: "The Hardware Lottery"
date: 2020-11-26T15:32:23-06:00
draft: false
tags: ['Policy', 'History']
categories: ['Papers']
---

By [Sara Hooker](https://www.sarahooker.me/)

[Paper Link](https://arxiv.org/abs/2009.06489)


## Paper Motivation

Through out history we have seen different research ideas win and lose. Why do some win and others lose? Do the superior ideas always win out?

## Paper Contribution

This paper introduces the term __hardware lottery__ to explain how some research ideas win out because they are best fit to the current state of hardware. It does not win out because the idea is superior to other research directionsThe author uses examples from early computer science research to show how the hardware lottery can delay research progress. The author believes recognizing hardware lotteries is more important as we start to make more niche hardware products.

### Background

Scientific progress is quite imperfect. It will head in wrong directions and be biased toward certain ideas. There will often be inertia to recognize new promising directions of research. For decades hardware, software and algorithms have been treated as separate research communities. We are now moving into a phase where all three of these will be more closely coupled together. This shift is larger due to the ways we have seen improvements in hardware making algorithms more powerful or even making new algorithms possible.

This closer collaboration has meant the creation of new hardware that is domain specific and very optimized for one use case. This specification can make it more costly to stray off the beaten path. There is a crucial paradox currently in machine learning research. Researchers will often ignore hardware despite the critical role it plays in their work.

Moore's law, which was true for a very long time, stated that every two years you could double the amount of transistors on a machine. This prevented the creation of specialized hardware because in two years general purpose hardware would be better than the specialized one. This meant that computers tended to be general purpose machines.

### The Hardware lottery

Successful breakthroughs in research are often distinguished from failures by multiple criteria aligning in a lucky way. Being too early can be the same as being wrong. The most well known example of the hardware lottery is the delayed adoption of the neural network. The algorithmic components of a neural net have been around since the 1960s. Deep neural networks were only accepted as a promising research direction in the 2010s. This gap is mostly due to hardware.Deep neural networks only took off when a different technology was re-purposed. Graphical processing units (GPUs) were introduced into computers to be used for video games. GPUs were then repurposed for training neural networks.

### Current Situation

We are currently seeing a swing back towards specialized hardware as we reach the end of Moore's law. There have been quite a few examples of hardware specifically being made for deep neural networks. TPUs are one example of this. This close collaboration between hardware and algorithms will make training and deployment of NN a lot easier.

The author uses the example of capsule networks for how the hardware lottery is impacting research today. Capsule networks are a new type of network that are quite different from CNNs. They are not optimized for GPUs though and therefore tough to currently train.

Hardware efforts general focus on optimizing algorithms that have already proven their worth and are known commodities.
It makes sense to bet heavily on specialized software if you believe future algorithms will look very similar to the ones today. Several labs are making this bet, focusing on bigger is better.

Biological intelligence differs enough from NN though, that we might believe we need to take a different approach in the future. Wile NN might be one way forward we should not make them the only one.

### How to not fall into a hardware lottery

1. We have to make it cheaper and less time consuming to try out novel techniques
2. Hardware for NN is ensured because NN have many commercial use cases. But how do we fund hardware for use cases that are not immediately commercially viable. There will be the chance that the hardware costs will never pay off.In that case we need investment from both public and private groups.
3. We should make it possible to benchmark systems when using different types of hardware. We need better profiling tools to understand how software and hardware should evolve together.

## My Closing Thoughts

Overall, I think this paper makes a compelling argument. Hardware specialization can make certain research directions more viable than others. It is difficult to have complete foresight about which research directions are the most promising. Specialized hardware could push the research community in certain directions which might be sub-optimal.

This paper is not actually about the hardware lottery. It really only has a couple of examples about a hardware lottery and is mostly focused on the present day situation. The hardware lottery is a theory of scientific progress. I would have really appreciated seeing more examples of the hardware lottery and seeing it also applied in fields outside of Computer Science.

The most compelling point in the paper is how monetary incentives led us to specialized hardware. Organizations do not want to invest in hardware that does not have a commercially viable use case. Neural Networks have already shown commercial use cases and so companies will build technology for them. This point really enforces the need for public investment in certain types of hardware. When we are pushing to develop a vaccine, a lot of that effort is subsidized by the government. It is possible that the vaccine does not ever work or a different company's vaccine ends up being better. The public investment is to make it worth companies time to invest in something that is not yet proven. If the thesis of this paper is correct, then it should be worthwhile to put more public investment for unproven hardware directions.




