---
title: "Reliance on Metrics is a Fundamental Challenge for AI"
date: 2020-09-24T16:03:09-07:00
draft: False
tags: ['Machine Learning']
categories: ['Papers']
---

[By Rachel Thomas and David Uminsky](https://arxiv.org/pdf/2002.08512.pdf)
### Paper Motivation

Optimizing a metric is central to current AI approaches. Metrics can lead to a myopic focus on short term goals leading to unexpected negative consequences. This reliance on metrics is a fundamental challenge of modern AI

### Paper Contribution
The paper reviews current examples of metrics gone wrong. The authors find the following problematic aspects of metrics
1. Any metric is just a proxy for what we really care about
2. Metrics can, and will be gamed
3. Metrics tend to overemphasize short-term concerns
4. Many online metrics are gathered in highly addictive environments

The authors create a framework to mitigate the harms of overemphasizing metrics by suggesting
1. Use multiple metrics to get a fuller picture
2. Combine metrics with qualitative measures
3. Involve a range of stakeholders

### Background

Metrics play a central role in decision making at many organizations. Their has been previous work highlighting the harms of using metrics. Metrics have an even higher risk in algorithms. Understanding the harm of an over reliance on metrics is a key part of understanding how AI is misused.

Current AI approaches are metric optimizers. While optimizing a metric is not unique to AI, AI is quite efficient at it.

### Applying Goodhart's Law to ML

Goodhart's Law states “when a measure becomes a target, it ceases to be a good measure“. Goodhart's law is from an economist in the 1970s named Charles Goodhart. When he first created the law he was talking about monetary institutions using a proxy metric for inflation.

When we use the term metric we usually mean a numeric value of interest. Machine Learning works by having a measure of a systems performance on a task. We then optimize that performance to train our system. There are a lot of choices that go into defining the performance metric for our system.
 - How much do we penalize wrong answers? Are all wrong answers penalized the same?

We can apply Goodhart's law to explain how AI's reliance on metrics is problematic for society

### The Problems with Metrics

#### Metrics are just proxies for what we care about

A case study from [Mullainathan and Obermeyer (2017)](https://scholar.harvard.edu/files/sendhil/files/aer.p20171084.pdf) lays out the following situation. We want to build a model to predict when people will have a stroke. The model we trained finds the following features are quite predictive.
- Have you had an accidental injury
- Have you had a benign breast lump or a colonoscopy?

These features don't seem like they are related to how likely it is you have a stroke. That is because they are not! But what they are correlated with is how likely you are to have been recorded as having a stroke.

The measure that we were using is a proxy for having a stroke. It is did you have a stroke that was recorded by a healthcare provider. This is influenced by how likely you are to utilize health care a lot, which those above features do correlate with.

Similar situations are measuring student performance by looking at test scores. Measuring crime by looking at arrest rates.

#### Metrics will be gamed

When all we care about is optimizing a metric we will often do something nonsensical to improve that metric. We see this all the time with students and test scores. Teachers end up teaching to the test because they know that is how they will be measured. When people know that a website uses metrics, there will always be instances of people trying to game them. If clicks is a metric that a website uses, there will be people who artificially increase their number of clicks.

#### metrics overemphasize short-term concerns

Long term trends are much harder to measure then short terms metrics with quick feedback. It is easier to measure time spent on Youtube than overall user satisfaction with Youtube or trust in Youtube.


#### metrics often gather data from highly addictive environments
Many tech companies use engagement metrics as proxy for user satisfaction. This often leads to algorithms doing the equivalent of feeding us junk food.

### A Framework for a Healthier Use of Metrics

Metrics are not something we should completely get rid of. They have a very real and important use case. We need to recognize their harms and mitigate them.

#### Use a slate of metrics to get a fuller picture

Having many data points gives us a better picture and stops us from optimizing any one thing. It is much harder to game several metrics at once.
#### Combine Metrics with Qualitative Information

We need to document more things about a model then just quantitative measures. What are the use cases, who built the model, what were their assumptions?
#### Involve a range of stakeholders

Including a range of stakeholders means more voices are heard and it is less likely that you missed something. You will have blindspots and bringing in other people helps you see them

## My closing thoughts

I really appreciate how the authors took Goodhart's Law from another field and applied it here. The authors identified how metrics are something that other fields have also struggled with. Looking at learnings other fields have had and then applying them to AI can be very powerful.

This paper made me think more about what makes a research paper. This is a position paper rather than a research paper. It doesn't do any research but rather states an argument and then tries to back it up with evidence and make a convincing argument. If this were a research paper the authors would have to define their framework better and try to evaluate the efficacy of the framework. A research paper tests a hypothesis where as a position paper can just state a hypothesis. Position papers seem like good precursors to writing research papers.

In the paper, there are a couple of times were they explicitly say something along the lines of "we recognize metrics are not all bad, and that they provide a use." But the tone of the paper felt so negative on metrics. How you parse and understand this paper might depend a lot on where your starting point is. I would have preferred a more balanced look at both the positives and the negatives. What makes metrics useful is also what makes them dangerous. But on the other hand, if you have not thought about the negative parts of metrics before, the tone of this paper might be perfect. It might force you to evaluate something you had not thought about before.

While I agree with everything in this paper, I struggled with it still. Coming from someone who is practicing machine learning in industry, it does not offer much practical action. How would I go about applying these frameworks to my actual work? I think this paper makes a cohesive and well backed argument, but it fails to be actionable. It is different to just say, "involve multiple stakeholders" than to show examples of how to do that and to give practitioners tools to help them.

