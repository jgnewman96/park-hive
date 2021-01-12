---
title: "A Framework for Understanding Unintended Consequences of Machine Learning"
date: 2020-09-13T15:20:03-07:00
draft: false
tags: ['Machine Learning']
categories: ['Papers']
---

By [Harini Suresh and John Guttag](https://arxiv.org/abs/1901.10002)


### Paper Motivation

We need a better understanding of the potential unwanted consequences from machine learning. We often hear about “biased data“ but this term has become a catch all that prevents nuanced understanding.


### Paper Contribution

The authors propose a framework that partitions harms from machine learning into six different categories. The paper covers what contributes to each harm and how to remedy them. The authors argue it is critical that the solutions we develop are from application specific understandings rather than abstract notions of fairness. This framework aims to develop a vocabulary which can be used to clearly state what the problems are and make practitioners assumptions immediately understandable.

### Background

Machine Learning models learn from historical data and generalize to unseen data. In recent years we have seen the mindless application of ML lead to problems with predictive policing and facial recognition. Discussions of problems with ML focus on “biased data“ but biased data can mean many different things. Biased data is an imprecise term that does not provide direction about how to mitigate its consequences or prevent harm.  There are many other factors besides issues with data that can lead to machine learning causing harm.

To provide a richer framework of potential harms from ML, the authors break down a machine learning process into the following steps
1. Data Collection
2. Data Preparation
3. Model Development
4. Model Evaluation
5. Model Postprocessing
6. Model Deployment [^1]

## Sources of Bias

**Historical Bias**: When there is misalignment between the world and the values and objectives in the model

- Example: In 2018 5% of Fortune 500 CEOs were Women. Should a search for photos of CEOs represent that?

**Representation Bias**: When the population used to train the model is not representative of the population we apply the model to. This is often caused by our training sample containing too few people from certain populations. Fixing representation bias could come from changing the data collection phase or the model deployment phase.

- Example: ImageNet is a commonly used dataset to train computer vision systems. The majority of the images in it are from the U.S. This leads to models trained on ImageNet having poor performance on photos taken outside of the U.S. We could either collect more photos from outside the U.S. or not deploy systems trained on ImageNet for non-US use cases.

**Measurement Bias**: The set of features and labels that we use leave out information or introduce noise

- Example: Arrest rate is a proxy for crime. Not everyone who gets arrested commits a crime and plenty of people who commit a crime do not get arrested. Further, it is possible that the record keeping of arrest rates is noisy or biased. Certain regions might keeper tighter records or more detailed records are kept when the person arrested is a minority.
- Example: Often we use a measure that is a simplification of our outcome of interest. In lots of places income is used as quantitative measure of success. But success can mean a lot of different things besides income.
- Example: Minorities are more heavily policed and therefore more likely to be arrested. This means our model would predict minorities are more likely to commit crime. Minorities are predicted as having a higher chance to commit a crime because they are getting policed more to start, not because ethnicity is actually a predictor of how likely one is to commit a crime.

**Aggregation bias**: When different populations are combined and treated as homogenous. This can be seen when certain variables mean something different for different sub groups. Our model will fit the dominant population and then have a large error on non-dominant populations.
- Example: Diabetes is experienced differently for different ethnicities. HBA1C is a value that is used to measure how likely it is a patient has diabetes. The same level of HBA1C for one ethnicity means something very different for another ethnicity.


**Evaluation Bias**: When the way we are evaluating does not equally consider different populations. When we use metrics that are not representative of the way the model will be deployed
- Example: Facial recognition performs a lot worse on dark-skinned females. If dark-skinned females make up a small part of our data than wrong predictions for that population will not have a large impact on our accuracy metrics.

**Deployment Bias**: When a system is used or interpreted in inappropriate way. Models are deployed in a complex system with a lot of different actors using them in different ways. Often the people acting on the model score did not contribute to building the model.
- Example: Judges using risk assessment models to determine length of appropriate sentence.

## My Closing Thoughts

While I might not agree with all parts of the authors framework, I really appreciate them putting this framework on paper. It gives us all a more nuanced place to start the discussion. Once something is on paper we then have the opportunity to refine it and improve on it.

The paper touched on this briefly, but I want to see more discussion about how we have to build for the world we want, not the one we have. This is the fundamental way I think about historical bias. Every dataset we encounter is going to have biases of our society ingrained. I find a helpful starting place is identifying what the world we want looks like. Then we can begin to understand what is preventing us from being in that world.

In deployment bias the authors did not talk as much about how different stages in the ML lifecycle will often be completed by different people. It might be a different person in charge of deploying the model then the person who built the model. Having different people in charge of different sections can lead to a lose of information which can introduce misuse.

The formalizations and mitigations section of the paper is nice in theory but I felt it was kind of weak. The case studies at the end also seemed like they were rushed. Because space in a paper is limited it can be difficult to do certain sections full justice when they have to be short. I was reflecting on how it is very important to nail down the identity of your paper and then strip away sections that do not contribute to that identity. The paper might have been stronger by deleting those two sections, or just deleting one and fleshing out the other more.

Similarly, the related works section took up a lot of space in this paper. I personally really enjoyed the related works section, it gave me a lot of other papers that I want to read. But this was not a survey paper. All of the space taken up by the related work section took away from developing some of the ideas in the paper more fully.

All of the recent reading I have done about fair AI and ML makes me think about how important transparency is. By transparency I do not mean model transparency but process transparency. There is an entire system that has nothing to with ML that goes into building a model. There are organizations and actors, all which have flaws and blindspots. We should mandate more transparency into all of the different steps that went into building a model. People will always miss certain assumptions or practices that have the potential to be harmful. If we have transparency though we can collectively identify those dangers and then work to mitigate them.


[^1]: This list makes the process seems like a straightforward and linear one. From my experience the process does not always happen in this order and it is hardly linear. There will often be cycles in the process and things will often happen concurrently. Itemizing these steps is a useful beginning and helps ground the conversation.
