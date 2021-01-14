---
title: "On the Legal Compatibility of Fairness Definitions"
date: 2021-01-11T12:49:56-06:00
draft: false
tags: ['legal policy', 'tech policy']
categories: ['Papers']
---

[Paper Link](https://arxiv.org/abs/1912.00761)

By Alice Xiang: [Linkedin](https://www.linkedin.com/in/alice-xiang-3832aa18/), [Twitter](https://twitter.com/alicexiang?lang=en) and Inioluwa Deborah Raji: [Linkedin](https://www.linkedin.com/in/deborah-raji-065751b2/?originalSubdomain=ca), [Twitter](https://twitter.com/rajiinio?lang=en)

### Paper Motivation

There has be a lot of literature that demonstrates gaps in machine learning fairness definitions.

### Paper Contribution
This paper shows that current fairness definitions misunderstand the legal terminology they claim to be derived from. These definitions are inappropriately co-opting legal language. This paper shows examples of this misalignment and explains what we can learn from these differences. The paper focused on U.S. anti-discrimination law.

### Background

The ML fairness community currently uses legal terms to motivate their research without a deep understanding of what those terms mean. To build accountability frameworks our machine learning definitions must be aligned with their legal definitions. It is important that the fairness definition successfully maps to the legal definition so we can use the fairness measure to establish liability.

This alignment must happen from both sides as results from research should also inform law. For forward progress to be made it is important that the legal community is also learning from the ML fairness community.

### Lessons from Anti-Discrimination Law

**Discrimination**

In ML literature “discrimination“ is often thought of as differing false positive rates by subsets of the data. Many approaches aim to adjust the predictor to remove this discrimination. This view is over-simplified when looking at the legal definitions of discrimination.

The Civil Rights Act of 1964, Fair Housing Act, Age Discrimination in Employment Act all define discrimination through motive rather than outcome. The definition of discrimination though is highly context specific to each of these fields.

**Protected Class / Sensitive Attribute**

In legal settings we see both people in the majority and the minority use this clause to argue for anti-discrimination. In ML so far this only shows up when thinking about minority groups. The ML community should recognize that it is possible for majority groups to use fairness definitions to harm those in the minority.

**Anti-classification and Anti-subordination**

The authors argue that most ML work currently focus on anti-classification which is that classifications should not be made based on protected attributes. When this paper was written the authors argue that ML work has not looked at anti-subordination which tries to actively dismantle social hierarchies. A paper which I read last year [Decolonial AI](decolonial_ai) looks at that.

**Affirmative Action**
Affirmative Action allows places to directly consider race when they are making decisions. Most ML research only focuses on how to not take protected attribute's into account.

**Disparate Treatment and Disparate Impact**

In ML work, authors use disparate treatment as a justification for not using protected class variables. Disparate impact is understand as when outcomes differ across subgroups. Researchers use this to think about fairness interventions. These definitions were made with human discriminators in mind though. Just replacing a human discriminator with an algorithmic one and using the same definition of fairness is not adequate. Disparate treatment is determined by intent. But intent is an inherently human characteristic and we cannot evaluate intent of an algorithm.

### General Legal Lessons for ML Fairness

Legal fairness frameworks struggle with intersectionality. We cannot just view someone based on characteristics but have to understand them as a person. ML Fairness should take intersectionality into account.

Procedural justice seeks to arrive at just outcomes through an iterative process of careful inspection. Our goals should be analyze an algorithm and its surrounding system in a similar way

### Lessons for Law from Fairness Research
- There is an importance to collecting data on protected attributes so that we want better understand fairness
- ML Fairness researchers focus more broadly than a specific sector like housing. They aim to make more general definitions of fairness
- ML Researchers have identified that it is possible for their to be a casual relationship even if a protected attribute does not exist in the data.

### My Closing Thoughts

The main thesis of this paper is an important one. It is critical that our legal definitions actually align with ML research. If they do not line up then we will have two separate systems that do not work together. What practitioners and researchers use to measure fairness will not align with what happens in a courtroom. The paper also highlights how researchers are currently just using legal language without really understanding what that legal language means. Rather than just using that language researchers should be more precise with their terminology.

It seems like since this paper was published there have been real examples of people building on top of this. This paper however does not have many citations. I wonder if this paper actually had an influence but it is not measured through citations or if there are just a lot of people thinking in the same ways right now. I keep wanting better ways to understand and measure the impact of papers.

I really appreciate the inclusion of affirmative action in this paper and it motivated some ideas in me. Imagine the following scenario. We build a classifier to determine if you are eligible for a loan. We then on top of that classifier bump up the probability that you will get a loan if you are a black. So much of fairness research has focused on how to avoid including certain attributes in the decision making process. I like this approach because it directly says we are going to take this into account and we can tell you how much we take it into account. It feels more transparent and more honest.




