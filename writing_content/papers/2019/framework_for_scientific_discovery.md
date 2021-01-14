---
title: 'Scientific discovery in a model-centric framework: Reproducibility, innovation, and epistemic diversity'
date: 2019-09-29
draft: false
tags: ['Statistics']
categories: ['Papers']
---

[By Devezer B, Nardin LG, Baumgaertner B, Buzbas EO](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0216125)

## Summary

This paper creates a model of how scientific researchers make progress towards the truth. By examining this process under different conditions the authors were able to identify what characteristics help lead scientists towards the truth. This work was motivated by understanding the role that reproducibility has in the research process. Through experiments with different conditions the authors were able to reach some conclusions about how reproducibility and other characteristics affect a communities ability to find the truth. 

The authors experiment had the following set-up:

* There is data that was generated from a certain process with a certain amount of noise
* There is infinitely many scientists and one of them is selected at random to propose a hypothesis for how the data was generated.
* If that hypothesis or model, is more likely than the current hypothesis it replaces the current hypothesis.
* This process of scientists trying to find the truth can be modeled using a Markov chain.

This experiment allowed the authors to test how varying different characteristics such as, how the scientists make hypothesis, or how much noise is in the data generating processing, affects the following outcomes:

1. How quickly does the group of scientists find the correct model?
2. How much time do the scientists have the correct model as the global hypothesis?

The authors found the following results:

* Even if our results are reproducible that does not mean that we have found the truth
* Having a population of scientists with heterogeneous research approaches performs better than a homogenous population
* It is more important to have innovative research early on in the research process. Later, we want research that is focused on refining the current hypothesis

## Thoughts

* The core argument of this paper can be boiled down to the following observation, having reproducible results is different from finding the truth. In this paper we update our hypothesis by comparing it to another hypothesis. In the setting from the paper, it is quite clear how just because something is reproducible does not mean it is the global truth. But in real world settings this is often quite hazy. What does it mean for something to be locally true versus globally true?'
* I see a lot of parallels in this paper to the idea of local optimum and global optimum in optimization. If we are focused too narrowly we can end up at a local optimum and not a global optimum. The equivalent would be if we are focused too much on reproducibility we will similar only reach local results. I am not sure how well this parallel holds though. I do not imagine research as one large optimization problem with local optimum and one global optimum. I see research as using small narrow truths to help us build one larger truth.
* I personally prefer thinking about research results in a Bayesian perspective. Each piece of research is just a piece of evidence helping us update our beliefs. With any piece of research we have never fully proofed anything but we have provided some evidence that a certain direction might be correct. When we reproduce that result we have provided even more evidence. When we are unable to reproduce that result we have provided some evidence that direction might be incorrect. If we view research in this way then no piece of research is proving a definitive truth. Rather research is proving evidence in favor of a certain view point which is helping us update our opinions. This mindset about research leads to a great understanding of the limitations of each piece of research and how different pieces of research interact with each other.  
* Research often gets boiled down to the paper where it was published. But research is so much more than just one paper that was published at a certain time. As the authors get at in this paper, research is a process of gradually trying to get closer and closer to the truth. Thinking of research in terms of papers rather than the greater process of trying to understand the truth, can lead to dangerous practices. Each experiment, paper, blog post is in a dialogue with all of the other research before and after it. I love this intiative called [ML Retrospectives](https://thegradient.pub/introducing-retrospectives/)  being rolled out at NeurIPS 2019. This initiative specifically calls out that research is a lot more that just papers. Research is a never ending dialogue and there should be other dialogues for discussion, communication and sharing.