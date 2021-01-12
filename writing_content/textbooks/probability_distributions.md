---
title: "Probability Distributions"
date: 2020-04-15T18:32:33-05:00
draft: False
tags: ['Statistics']
categories: ['Textbooks']
katex: true
---

## Discrete Distributions

A discrete distribution on has specified values, such as integers. It has a probability mass function.

### Poisson

The poisson distribution expresses the probability that a given number of events occur in a time interval. The larger the lambda the more times the event will occur.

$$P(Z=k) = \frac{\lambda^k e^{-\lambda}}{k!}$$

$$ E[Z| \lambda] = \lambda $$

The poisson distribution provides a probability for any positive integer.

A larger lambda gives more to higher values. A smaller lambda gives more probability to smaller values.

### Bernoulli

The bernoulli distribution is for a value that can be either 0 or 1. The parameter p describes the probability the value will be 1 and (p-1) is the probability the value will be 0.

$$P(Z=1) = p $$
$$E[Z | p] = p $$

### Binomial

The binomial distribution parametrizes the number of times an event will happen in n tries. It is the extension of the bernoulli distribution from one attempt to n attempts. Each event is independent from every other event in the sequence.

$$ P(Z=k){N \choose k}p^{k}(1-p)^{N-k} $$

$$ E[Z | p, N] = Np $$


## Continuous Distributions

Can take on arbitrarily many values. It has a probability density function.

### Normal Distribution

The normal distribution is one of the most common distributions.

$$ f(x) = \frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{1}{2}(\frac{x-\mu}{\sigma})^2} $$

$$ E[x | \mu] = \mu $$

### Exponential Distribution

$$f_{z}(z | \lambda) = \lambda e^{- \lambda z} $$

$$ E[z | \lambda] = \frac{1}{\lambda} $$

A smaller lambda gives more density towards higher values.

### Logistic Function

This is a common S shaped curve / function. Its values go from 0 to 1 or from 1 to 0 depending on the sign of beta.

$$ p(t | \beta) = \frac{1}{1 + e^{\beta t}} $$