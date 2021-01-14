---
title: "Bayesian Methods for Hackers: Prologue and Chapter 1"
date: 2020-04-15T18:08:51-05:00
draft: false
tags: ['machine learning', 'Statistics']
categories: ['Textbooks']
katex: true
---

[Bayesian Methods for Hackers](https://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/) is an online textbook created by Cam Davidson Pilon. The book focuses on bridging the gap from theory to practice. The author argues that textbooks often focus on theory to the point where they become inaccessible. By focusing on accessability these methods become avaliable to anyone.

## Notes

The first chapter begins with an outline of how to think in a bayesian frameworks. Bayesian methods are our process of updating beliefs after seeing new evidence. Rather than making a definitive decision these methods express their uncertainty. In the frequentist world, a probability is the long term probability of an outcome. In the bayesian world, a probability measures our confidence in a belief. As N goes to infinity then bayesian inference and frequentist inference become the same thing. Bayesian inference excels when we are dealing with small N.

The chapter contains a quote from Andrew Gelman which I found very interesting. He argues that we actually never have large N size. If we have a large N we should look at segments of our data to answer more interesting questions. If we are looking at a national data, as our data gets larger we are then able to look at trends by state or city.

What is the probability of A given X can be notated as P(A | X). This can be a combination of our prior and our evidence. Bayes rule can be expressed as the following.

$$P(A | X) = \frac{P(X | A) P(A)}{P(X)}$$

In the rest of the first chapter the author goes through some examples of how bayesian thinking works and talks through a couple of different probability distributions. I have found that having a key grasp on the different probability distributions is really important. I have dedicated this [page]({{< ref  "/writing/textbooks/prob_distr.md"  >}}) to probability distributions. I will continue to add to it whenever I encounter new distributions.

Probability distributions can be used to model values that we are interested in. In the textbook the author looks at a couple of different examples. The classic example is using a Bernoulli distribution to model a coin flip or a binomial distribution to model a series of coin flips. The parameters of these probability distributions are hidden from us. We want to use the data to help infer what those parameters are. If we learn the parameters of the probability distribution we will then be able to make inferences.

At the end of the chapter the author provides an example of using [Pymc3](https://docs.pymc.io/) to solve a problem. The author has data about his number of text messages every day. He wants to answer whether or not there was a change in his texting behavior during this period. He specifies a model for his texting behavior and then fits it using pymc3. This model shows that there likely was some change in his texting behavior because the parameter for the probability distribution likely changes.

## Thoughts

The example that the author used towards the end of the chapter is very interesting but left me wanting a lot. The author made the whole process look easy & simple. We specify a model and boom here is an answer. There are a lot of key parts of the modeling process that the author leaves out. We have to compare this model to other possible models. Is this model the one that best explains your behavior? How would we compare this model to one where we believed there were two changes to your texting behavior?

Our results and model are directly a result of the questions we ask. The best model is determined by how much it helps us answer the question swe are interested in. The question the author asked was did my texting behavior change? I guess to answer this question, the model he proposes works well. A much more interesting question would be, how can we understand my texting behavior. Rather than assuming there was only one change we could compare different models with different numbers of changes.

Another question I like to ask myself is the following "If I had to solve this problem in a different way, how would I do it?". Two compelling approaches came forward to me. With all of these approaches the number of clusters is a parameter.

- We could try clustering the data forcing clusters to be continuos over time. We would want to maximize within cluster similarity and minimize between cluster similarity. This would allow us to cluster our days into different segments of behavior.
- Another option would be to compare averages. Look at the average before a day cut-off and after a day cut-off. Find the day cut-off which maximizes that difference. Then keep repeating this process until we get the desired number of clusters.


Two more existential thoughts:

1. Is anything actually distributed by a probability function? Maybe as N reaches infinity, but for sample sizes we care about the probability distribution is always an approximation. This means that there is no true value for a parameter only our best guess given what we know.

2. I could see the following counter argument to a bayesian line of thinking. "Real life consists of decisions. While it might be nice to express your uncertainty, we have to make a decision. Why not incorporate that decision into the statistics, rather than off loading it to someone else." This line of thinking is problematic for a couple of reasons. Uncertainty is a big part in assessing the trade-offs in a decision. Expressing uncertainty and being transparent allows individuals to make their own decisions and assessments rather than forcing it upon them. We should always lean towards being more transparent and giving people as much information as possible. This gives them the power to make an educated decision rather than being opaque and showing them a decision based on arbitrary guidelines. The idea that 5% significance should apply to all situations is completely ridiculous.

