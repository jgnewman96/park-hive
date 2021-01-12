---
title: "Principles and Practices of Explainable Machine Learning"
date: 2020-12-06T15:43:44-06:00
draft: false
tags: ['Machine Learning']
categories: ['Papers']
---

By [Vaishak Belle](https://vaishakbelle.com/) and [Papantonis Ioannis](https://scholar.google.gr/citations?user=FGKM2o4AAAAJ&hl=en)

[Paper Link](https://arxiv.org/abs/2009.11698)

## Paper Motivation

Artificial intelligence has the potential for a large positive impact. Introducing AI will result in significant change in complex systems. There has been a growing concern about how to trust and understand AI. Current practitioners may not be aware of approaches emerging from academic literature about how to better understand models.

## Paper Contribution

This paper is a survey to help practitioners understand the field of explainable machine learning and know which are the right tools to apply. The paper aims to be readable and provide concrete information that is immediately useful.

## Background

The inner workings of many machine learning models can be quite difficult to understanding. Explainability is one direction which can generate insights that could be utilized by many different stakeholders. Data scientists can benefit from explainability by using it to for model debugging or improving model performance. Other stakeholders can use explainability to check robustness and reliability. Explainability also provides consumers with more transparency.

The authors argue we can use the following characteristics to think about a machine learning model

- Correctness: Are we confident that only the variables of interest contributed to our decision?
- Robustness: Are we confident the model will not be thrown off by minor changes?
- Bias: Are we aware of any data-specific biases that penalize certain sub groups?
- Improvement: In what ways can we improve the model?
- Transferability: What domains is this model applicable to and which ones is it not?
- Human comprehensibility: Are we able to explain the model's set to an expert of even better a lay person?

The authors provide another framework of breaking down **transparency** into three dimensions.

- Simulatability: Can a human simulate the model? Could a human calculate the model's output.
- Decomposability: Can the model be broken down into different parts and each part be understood?
- Algorithmic Transparency: What is the procedure the model goes through in order to generate its output.

These three different ways of looking at transparency highlight that transparency is not a binary. Transparency is a spectrum with some models obtaining more transparency and some obtaining less. [^1]

The authors provide another framework so that we can evaluate explainability. We want to know what does a good explainable representation of a model look like. Here are the different properties the authors ask us to think about.

- Comprehensibility: Are the representations of the model human comprehensible?
- Fidelity: Do our representations actually map to the model?
- Accuracy: Do our representations work for unseen examples?
- Scalability: Will our representation work for large and complex models?
- Generality: Does the method require some restriction or special circumstances?

The authors next break the different types of representations or explanations into a few different categories.

- Text Explanations: Use some text representation to explain the model
- Visual Explanation: Visualizations that facilitate an understanding of the model
- Local Explanations: how does a model work in a narrow area.
- Explanations by Example: show examples on the training data set to give a better understanding.
- Explanations by Simplification: Explain using a simpler model which is easier to interpret
- Feature Relevance Explanations: How much influence did each input have.

## Explainability [^2]

Models can be categorized into two categories, transparent models and opaque models. Transparent models we can look directly at their properties and understand immediately what is going on. For linear regressions we can look at their coefficients or with decisions trees we can look at their rules. [^3]. Then there are opaque models which we cannot understand by directly looking at them. Opaque models generally achieve higher accuracy since they can create more complex decision boundaries.

List of explainability approaches:

-  [Local Interpretable Model-Agnostic Explanations (LIME). Builds a local model that is similar that approximates the more complex one](https://arxiv.org/abs/1602.04938)
- [Anchors: Another approach that makes local rules which are equivalent to the more complex model](https://homes.cs.washington.edu/~marcotcr/aaai18.pdf)
- [Approximating a model using conjunctive normal form or disjunctive normal form](https://arxiv.org/abs/1606.05798)
- [Creating a decision tree to approximate a more complex model](https://dl.acm.org/doi/abs/10.1145/3077257.3077271)
- [Describe the smallest change to the input that would change the prediction](https://arxiv.org/abs/1711.00399)
- [SHAP: Tells you how important each feature was to a prediction](https://arxiv.org/abs/1705.07874)
- [QII: Measures impact of input on output](https://www.andrew.cmu.edu/user/danupam/datta-sen-zick-oakland16.pdf)
- [General Sensitivity Analysis](https://core.ac.uk/download/pdf/55616214.pdf)
- [Individual Conditional Expectation Plots](https://arxiv.org/abs/1309.6392)
- Random Forest Specific Approaches
    - Simplifications
        - [Make a RF interpretable by approximating it with a simpler model](https://arxiv.org/abs/1606.05390)
        - [Approximate a RF using one decision tree](https://link.springer.com/chapter/10.1007/978-3-540-74958-5_39)
        - [inTrees: simplifying a RF using only a few rules](https://arxiv.org/abs/1408.5456)
        - [Making RFs explainable using prototype points](https://arxiv.org/abs/1611.07115)
    - Feature Relevance
        - [Understanding how much each feature contributes to accuracy](https://arxiv.org/abs/1312.1121)
        - [Visualization to understand map from feature space to output space](https://arxiv.org/abs/1605.09196)
        - [Look at how permuting feature values would impact prediction](https://arxiv.org/abs/1706.06691)


The authors end the paper with a case study that show cases their suggested work flow. We are often aiming to maximize performance while also have explainability [^4]
1. First try a transparent model.
2. If our accuracy is not good enough and we can use an opaque model then try a more complex model
3. For a more complex model start using explainability techniques. Start with feature relevance and then move on to model simplification.
4. A good place to end up is a complex model with good accuracy and then a simpler model that you can use to explain the complex model.

## My Closing Thoughts

This paper ended up being quite a slog. It is really long and has a log of repetition. It was not structured in a way that made a lot of sense and the frameworks the authors introduced did not lead to anymore clarity on my part. I appreciated a lot of the things the authors tried, but for me this paper mostly missed the mark.

You could argue that I got a lot of good links out of this paper, but I actually think that is disappointing. No way am I going to read all of those papers. Often when I read survey papers I am disappointed. Maybe this is not the point, but I feel like they should be more opinionated. Just knowing about all the work in a field is often not useful. I still need to then comb through it myself. I want an opinion on what are the most valuable directions and what is going to stand the test of time.

In practice, I have never really seen people in industry care about explainability. They will rarely give up accuracy for explainability and people just are not that interested. If you give them some accuracy metrics and some robustness checks people are good.

This paper left me with one big question: Does making a paper like this actually have an impact? How much did this paper move the field forward? How many practitioners read it and if so how did it impact them? How would we start to measure the impact of a paper. I know a lot of people look at how many other papers cite a paper, but thats a very narrow metric. I would love to think up other ways to measure the impact of a paper.


[^1]: I like the idea of transparency as a spectrum but these different levels did not really do it for me. It was not clear how one builds on top of the other and how these are distinct properties.

[^2]: So you might have caught on by now that this paper tries to use frameworks and lists a lot. I appreciate that they are trying to use structure to help our thinking but I personally found all of the different structure overwhelming after a certain point. There was not one clear structure to follow that I could always return to. Maybe this space is just so complicated, but it does not really feel like it. I am going to try and breakdown the end of the paper using some of their structures from above with some of my own simplifications. I normally do not like to bring my own thoughts into paper summaries, but for this paper I feel like it is worthwhile.

[^3]: The authors mention this in the paper, but I find this breakdown between transparent and opaque is lacking because you can have a transparent model that becomes so large it is essentially opaque.

[^4]: In the example from the paper, the data scientists uses like ten different explanation techniques. This example is so distant from what I have seen during my time in industry. You might get to use one or two techniques. Also it can be difficult to implement the technique.
