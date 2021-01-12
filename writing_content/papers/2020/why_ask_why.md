---
title: "Why Ask Why?: Forward Causal Inference and Reverse Causal Questions"
date: 2020-09-24T16:02:58-07:00
draft: false
tags: ['Statistics' ,'Economics']
categories: ['Papers']
---

[By Andrew Gelman and Guido Imbens](http://www.stat.columbia.edu/~gelman/research/unpublished/reversecausal_13oct05.pdf)

### Paper Motivation

Most statistics and economics literature focuses on the effect of a treatment not what caused an outcome.

### Paper Contribution

The authors argue that the search for a cause can be understood in a traditional statistical framework. We can think about identifying causes using model checking and hypothesis generation.

## Background
A map shows a high density of cancers in a small geographic region. This immediately leads to some questions &rarr; What is going on here? why are there so many cancers?

If we successfully answer these questions, depending on the answer, we might be able to prevent a similar thing from happening again. If we find that the cancers were caused by some agent in this region, we would then stop using that agent and make sure others do not use it as well. We would then be creating a policy that reduces cancer.

The purpose of this paper is show how these type of questions are still in the field of causal inference
## Forward and reverse causal questions
__Forward causal questions__: What would happen if we do X?
    - e.g. What is the effect of smoking on health? schooling on earnings?
__Reverse causal inference__: What causes Y?
    - e.g. Why does per capita income vary so much by county? Why did the economy collapse?

Generally researchers focus on the first type of questions and not the second type. They ask "What if?" questions rather than "Why?" questions.

{{< quote >}}
Forward causal inference is about estimation; reverse causal questions. are about model checking and hypothesis generation
{{< /quote >}}

To put it another way, the why questions are what motivate us to study what if questions. These what if questions can be studied using traditional statistical methods

The authors are not using reverse and forward in reference to time. We can ask forward causal questions about the past. For example, asking if a country was more democratic would it have had more economic growth is a forward causal question about something in the past.

### Example

**What is the effect of money on elections?**

The question above is too ill-defined to answer. If we narrow the question slightly it becomes answerable. What would the effect have been on the election if candidate A had gotten 1000 more dollars?

Here is a reverse causal question: Why do incumbents running for re-election get so much more funding than challengers? We have to reframe this question into a forward casual one to be able to answer it. Once we have formed a hypothesis about this question we can then test it out.

Reverse casual questions in this way lead to model checking and hypothesis forming. When we have a reverse casual question it means our current model of the world is not complete. There is a phenomenon that needs an explanation. Often these models are implicit and not clearly stated. In the above example, our model was that all candidates would receive the same amount of funding. We form a hypothesis, update our model and then check if that model does a good job fitting what we are seeing.

### Mathematical formulation

Let Y_i denote an outcome of interest for unit i. Let W_i be features we observe about unit i. Let Z_i be characteristics of i that we do not believe impact Y. So in units that have the same W, they should have the same Y.

But what if our data rejects this hypothesis? We see that even after controlling for W, differences in Z do lead to differences in Y?

There are two explanations that are still consistent with our original hypothesis that Z has no impact on Y
1. We omitted an important attribute, V. If we included this attribute the relationship would disappear
2. There might be something else that is actually causing Y. Y might be a function of some value X that we had not considered.

## Conclusion

A key difference this paper highlights is that of casual questions and causal statements. **Even if a question can not be directly answered, it does not mean that asking the question is useless**.Asking reverse casual questions can highlight anomalies and provides an opportunity for model improvement.
{{< quote >}}
By formalizing reverse casual reasoning within the process of data analysis, we hope to make a step toward connecting our statistical reasoning to the ways that we naturally think and talk about causality.
{{< /quote >}}

### My Closing Thoughts


- This paper reminds me of an idea in engineering "the importance of getting your abstraction right". While it is easy to dismiss this and say these kind of distinctions are trivial, I believe they are truly important. "getting the right [abstraction](https://en.wikipedia.org/wiki/Abstraction_(computer_science))" allows us to focus on the details that are important and not get caught up in minutia.  he type of abstraction we have and how well it fits our problem changes our thinking. Similarly, understanding casual questions in this light changes the whole process of doing research. It brings these why questions into the research process rather than saying they are not scientific.

- Part of what this paper is doing, is making something that is implicit, explicit. We are asking these why questions all the time. We might not have considered them part of our research in the past but they were. We just were not documenting them. By making it explicit there are less unsaid assumptions and more information is revealed.

- There has been a lot of pop science books written about how we can make our minds work in a more statistical way. That we have to train ourselves to think statistically. While this paper does not invalidate any of that, it kind of does the reverse. It shows how the ways we normally think are actually in line with statistical thinking. It broadens what we mean when we say statistical thinking to include questions we ask very naturally.


