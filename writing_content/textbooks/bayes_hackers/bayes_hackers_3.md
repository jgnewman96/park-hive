---
title: "Bayesian Methods for Hackers: Chapter 3"
date: 2020-05-06T13:19:17-05:00
draft: false
tags: ['Data Science' , 'Statistics']
categories: ['TextBooks']
katex: true
---

# Notes

Chapter 3 in *Bayesian Method for Hackers* is center on Markov Chain Monte Carlo (MCMC). It is possible to use pymc3 and bayesian models without understanding the underlying algorithms. Understanding this algorithms plays a pivotal role though if we want to be serious practitioners. When our model works out perfectly, not knowing  the underlying algorithms is fine. But if we are trying to do anything complicated, our first attempt will almost certainly not work. When we have to debug and iterate, understanding how the algorithm works and how to diagnose problems becomes critical.

The chapter begins be having us think about the parameter space for our model. If our model has N unknowns then the solution space for our model is N dimensional. Using bayesian models, we identify what spaces in that N dimensional space are more likely and which are less likely. If we use non-bayesian methods then we identify just one point in that N dimensional space.

Priors in our bayesian model provide likelihoods for different places in our solution space. Often we will use a uniform prior which means everywhere in our solution space is equally like. After specifying our prior we then include in our data. When we include data, the solution space stays the same, but likelihood of different areas changes. Areas that line up with our data become more likely and areas that do not align with our data becomes less likely.

## Markov Chain Monte Carlo (MCMC)

So how do we find the areas in our solution space that are most likely? MCMC is an algorithm that does an intelligent search of the solution space. If the solution space is very large it could be difficult to search the entire space. MCMC works by exploring the nearby areas and moving towards areas of higher probability. If MCMC works it will move to the area of the highest probability and then sample many times in that area. Once we have gotten lots of samples in the highest probability area we can create a histogram of our models parameters.

Here is an outline for MCMC algorithms:
1. Start at a position (our prior)
2. Propose a new position
3. Accept/Reject position based on adherence to data & prior
4. If Accept move to new position, return to 1, if reject return to 1
5. After large number of iterations, return all positions

MCMC algorithms are memoryless. The algorithm only cares about the current position. The next step is only dependent on the step before it and not a long list of steps.  The algorithm is memoryless. It does not care about how it got to where it is.


## Diagnostics

Once we have run MCMC, how do we know if our result is a good one. The best way to diagnose MCMC is too look at a couple of different plots. Pymc3 comes built in with a lot of nice plotting tools. There are three different plots that are very helpful is assessing your fit.

A *posterior plot* allows us to view histograms for the posterior  of parameters in our model. We can inspect what is the most likely value for a parameter and what is the uncertainty about that parameter.

A *trace plot* allows us to view a scatter plot of where MCMC was sampling. Ideally we will see a fuzzy caterpillar. We want MCMC to be walking around in the highest probability space.

An *autocorrelation plot* allows us to view how related each sample is with the previous sample. When we do MCMC we want our chain to have low autocorrelation. This is not a sufficient condition but a necessary condition. If we have high autocorrelation then our chain is not doing a random walk in the highest probability space.

## Some extra MCMC Thoughts / Notes


- When we are sampling our parameters we should not mix different samples together. If the value of two parameters is related this will lead to bad inference.

- It can help with convergence to start at good values. This does not mean setting our prior to be at good values but rather setting our `testval` to be something that makes sense. It is especially good to start near the peak rather than far away from it. `pymc3` comes built with a capability to do this. We can specify that starting point should be the maximum a posterior estimate or the map.

-  When using MCMC, we often have to specify a burn-in period. The burn-in period is when we are still navigating to the region of highest probability. We do not want to include this time period in our final posterior histograms. We discard the burn-in period.

# Thoughts

- I really appreciated the approach of this chapter. It was really helpful for me to think about the solution space for our model. It can be really helpful to return to fundamentals when learning a new algorithm or working on a problem. For anytime of model there will also be a solution space and we can always use that to ground our thinking.

- To help the reader understand how MCMC was moving the author kept using the metaphor of traversing a mountain. We can think about optimization in terms of finding valleys. I find that metaphors are one of the most powerful way to explain things to people. It can be really difficult to grasp concepts in the abstract. Using a metaphor to ground thinking is so helpful.


