---
title: "Optimization of Survey Weights under a Large Number of Conflicting Constraints"
date: 2020-04-07T16:16:26-05:00
draft: False
tags: ['Statistics']
categories: ['Papers']
---

[By Matthew R. Williams and Terrance D. Savitsky](https://arxiv.org/abs/1901.03791)

## Summary

This paper provides a framework for creating survey weights using constrained optimization. The problem we are solving can be laid out in the following way:

We have a sample of size n taken from a population of size N. Each person in the population has a probability of being included in the survey. The probability of being in the sample is correlated with our response of interest. To account for this probability every person in our sample gets a weight of 1/p_i, where p_i is the probability of being selected. After applying these weights we can now infer about the population.

Here is an example to ground our thinking. Our population is doctors in the United States. We send out an email to all doctors asking them to participate in our survey. We are interested in do doctors support using more technology in hospitals. A sample of the doctors we email respond.  We want to answer questions about our population of doctors, not just our sample of doctors. Doctors with a higher probability of responding to our survey might be more likely to support technology. We need to downweight the doctors with a higher probability of being in our survey otherwise we will overrepresent the number of doctors who support using more technology. If we knew p_i for every doctor, we could apply a weight of 1/p_i to each doctor in our sample.

We do not actually know p_i though. It is  unobservable. We can observe other variables that might be correlated with p_i though. For example, gender or age or ethnicity might relate to p_i. Males might be more likely to be in our survey than females. We can weight our survey so that these variables line up with the population. If we know the population is 50% male, but our sample is 75% male, we then want to downweight those responses so that our sample lines up with the population.

We call these variables, weighting variables. We do not know ahead of time which weighting variables will lead to the best sample. If we have a matrix X of possible weighting variables, we need to somehow pick which weighting variables to use. As the size of X increases, the number of potential weighting variables grows, there no longer becomes a closed form solution to our problem. In order to solve this problem we can use constrained optimization with a loss function.

> "The focus shifts from finding one optimal solution to finding one or more reasonable solutions which satisfy most of the constraints and restrictions"

The constrained optimization allows us to use both *soft* and *hard* constraints. A hard constraint means that our solution most meet that constraint. For example our weights must make it so 50% of the sample is male. A soft constraint means that we want our solution to come as close as possible to the constraint. We penalize a solution the further away it is from the constraint.

When we use hard constraints it is possible that no solution will exist if we add a lot of constraints. Using soft constraints we will always be able to find a solution. When we use soft constraints we can weight how much we care about a given constraint. We might care about gender lining up with the population more than we care about age.

The rest of the paper discusses different options for deviances (their word for loss metrics). The authors then apply their solution to a data set and show the results.

The authors evaluate their model by looking at how many constraints it can hit. They argue that a weighting that meets more constraints is a better weighting.


## Thoughts

- The authors are not able to evaluate the accuracy of their weighting because they do not know the truth values for the variable of interest in the population. A next step in research would be to examine a setting where we knew the true value in a population. We could then answer questions about if different loss metrics led more accurate weights. It is also possible that each sample is unique and there will not be a set of weighting variables or a loss metric that is consistently the best.

- I enjoyed the reframing of weighting as a constrained optimization. This approach makes it clear what assumptions we are making and makes it easy to compare different weighting approaches. We can directly tell the algorithm we care about these constraints more than these other constraints. When we report our weighting we should be clear about what assumptions we made and why we made them. Another possible approach would be do to many runs of weighting and see how results change as we change our assumptions. This would provide insight into the importance of certain assumptions and how the result could be different if our assumption is wrong.



