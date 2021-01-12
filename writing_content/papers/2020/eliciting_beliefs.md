---
title: "Statistical Methods for Eliciting Probability Distributions"
date: 2020-01-05T17:34:38-06:00
draft: false
tags: ['Statistics']
categories: ['Papers']
---
[By Paul H. Garthwaite, Joseph B. Kadane and Anthony O’Hagan](http://www.stat.cmu.edu/tr/tr808/tr808.pdf)

## Summary

This paper is an overview of how to take experts believes and turn them into statistical distributions. It combines a long line of psychology research with statistics research. The situation we are examining is when we want to create a distribution over a value from an experts opinion. It is impossible to ask an expert to give us a probability distribution so we need a methodology to query an expert that allows us to create the distribution ourselves. An expert can be anyone who has information about the value we are interested in. If I was modeling how much time my friend sleeps, than my friend would be the expert.

So what does it mean for an elicitation to be successful? The authors argue that there is not a true distribution. We want to find the distribution that most closely matches the experts beliefs. An example of the setting the authors are describing is asking for an experts advice on an input to a model. Imagine we are modeling house prices. We have a couple of different variables and want to ask an expert how to weigh different variables. In this case the input is the weight of the variable and we want to create a distribution for that weight from the expert.

The paper defines four parts of the elicitation process:

1. The setup: selecting experts; training experts; identifying what to elicit.
2. We then elicit from the experts
3. We fit a distribution using the information we have elicited
4. We assess validity of elicitation and return to stage 2 if deemed necessary

The authors caution that if the expert cares about the end goal, the information they provide might be biased. The paper uses the example of asking a radiation expert about the impacts of Chernobyl. An expert might be incentivized to over play the impact because it increases the social attention to their field.

The authors highlight that whenever we do belief elicitation we should attempt to do the following things:

- Understand what an experts knowledge is based off of.
- Understand if the expert has any biases
- Train the expert so they understand how to accurately give information
- Keep a record of the elicitation

The authors review a long series of literature highlighting different ways our experts answers might be biased. Some of these are biases due to how we ask questions and some of them are biases due to human nature. Understanding these biases allows us to ask questions in ways that mitigate these biases. For example, research has shown humans are bad at estimating variances and bad at estimating means. Humans are much better at estimating medians, proportions and credible intervals. We should ask questions that line up with human's natural intuitions. Rather than asking an expert for the variance parameter of a distribution, we should ask them a question about proportions in an interval.

The next step is turning the experts answers into distributions. While it is nice to ask question using words, words can be very hard to turn into distributions. "quite likely" or "extremely likely" will mean different things to different people. It can be difficult to decide what distribution to use once we have information from the expert. We can choose a distribution from a family of distributions that most closely matches an expert's answers.

Another approach the authors mention is to use a hierarchical model and directly model the accuracy of the expert. This allows us to incorporate uncertainty and make less strong assumptions.

There is another section of the paper where the authors discuss how to pool together opinions from multiple experts. They discuss situations in which we get information from the experts together and separately. This is difficult because there is both the statistical question of how to combine different experts beliefs and the psychological question of how different experts might impact each other.



## My Thoughts

- The setting this papers talks about is a critical one. When we do not have a lot of data, it is often necessary to combine data with some human knowledge. We have much more flexibility in our modeling if we can create a distribution for a parameter rather than just a fixed value. This type of setting should happen a lot more when people are creating models. We should actively combine data with experts knowledge. This can be especially powerful in situations with very sparse data. What if we want to model the probability that an algorithm discriminates against people of color? We might only have very minimal data about this, but we will be able to ask experts opinions.

- That last example is a setting where we want to use people's answers directly as data in our model. Imagine we want to model the likelihood of the Lakers winning the NBA Championship. A powerful way to do this would be to ask all of the coaches their beliefs. Following the authors advice gives us a structured and systematic way to do this. Another example is asking someone how likely they are to vote. There is a distribution over this value. Finding an accurate way to get this distribution from a survey taker is very important.

- I really like the idea of adding another hierarchical step in our model and using that to model accuracy from our experts. This adds more complexity to our model but it gets rid of an assumption. This trade off between assumptions and complexity can be a difficult one to make. We diminish our complexity by making more assumptions. With the correct data and model this approach could be very powerful by reducing our assumptions.

- This paper was a bit too long for my liking and went into too much detail on the examples. I know it was a survey paper and so it condensed a lot of research but it did not do a great job of summing up general principles. The best way to write a survey paper is to combine summarizing of generalizable principles with examples that show case those principles.

- I am always wary when I read older papers. I am scared that there is a newer one that is more up to date and contains better information. Depending on the field a paper from 2005, could be ages ago or still quite relevant. It would be incredible if when reading a paper it told you if there was more recent research and this paper was now out of date.



