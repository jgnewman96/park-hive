---
title: "Bayesian Methods for Hackers: Chapter 2"
date: 2020-04-21T16:38:35-05:00
draft: false
tags: ['machine learning' , 'Statistics']
categories: ['TextBooks']
katex: true
---

## Notes

The chapter explains the syntax of pymc3 and how to turn different concepts into pymc3 code. It outlines the difference between a stochastic variable and determinstic variable

- A stochastic variable is random. This means even if all the information about the variable is known, we do not know what its value is. Drawing a value from a distribution is a stochastic variable.
- A deterministic variable can be determined from its parameters. Some examples of deterministic variables below
    - 4
    - 4 + 4

There is one tricky piece here. 4 + poisson(4) would be a stochastic variable but the following is a stochastic variable followed by a deterministic one.

- x = poisson(4) : stochastic
- 4 + x : deterministic

* * *

The author outlines a process for thinking about modeling when using Bayesian Inference. We should think about our model in the following process.

How is my data generated?

1. What is the best random variable to describe my data?
2. What do we need to know for that distribution?
3. How can we calculate what we need to know for that distribution?

This process helps us tell a narrative about our data. There is a story about where our data is coming from and how it is generated. This narrative is desirable because humans understand stories intuitively. It provides a way to explain our data to other people.

This process also makes it trivial to sample / generate data. Once we have created our data generating process we can plug in different parameters and then generate data.

The author then runs through three different examples using this modeling approach and pymc3. Some of my thoughts about these examples can be seen below.


## Thoughts

- Examples are such a powerful way to learn.  Referencing an examples makes it easy to extend an approach to more complicated problems. I really appreciate this book's approach of using examples.

- The author of the book repeatedly bashes frequentist approaches. Before the beginning of the A / B testing example he bashes significance testing. I kind of hate this rhetoric. It does not explore why people like frequentist approaches and what the benefits of a bayesian approach are. In this particular example the frequentist approach is actually very similar to the bayesian approach. The frequentist approach just assumes normality and does not make the assumptions it is using clear. Rather than bashing frequentist approaches the author should highlight how the bayesian approach is more flexible and makes our assumptions more evident.

- In the last example, the author argues that plots should be used to assess goodness of fit for a model. I agree that plots can often add more information then just a metric, but the example that the author uses is poor. Separation plots are difficult to understand and do not add much information. For a logistic problem I would have provided a different plot. We could create a plot that has for each class the predicted probability as a function of the variable. We can then overlay on top of this the true results. This gives us a better sense of when we are predicting the wrong class and where the model has higher confidence.



