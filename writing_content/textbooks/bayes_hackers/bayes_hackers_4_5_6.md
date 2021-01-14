---
title: "Bayesian Methods for Hackers: Chapters 4, 5 and 6"
date: 2020-05-06T13:19:28-05:00
draft: False
tags: ['machine learning' , 'Statistics']
categories: ['TextBooks']
katex: true
---

I have decided to combine my notes from chapters four, five, and six into one post. These chapters are light on new information and heavier on examples and applications. The power of this book is the number of examples it provides. One way to learn is to look at examples and then adopt them for your own use case. This book is perfect for that type of learning.

## Chapter 4

Chapter four is centered on the law of large numbers. The author assumes that many people have not heard about law of large numbers but I learned about the law of large numbers many times during undergrad. We had to derive the law in three different classes I was in.

I believe the author is highlighting the law of large numbers because he believes the application of it is not always intuitive. People understand the law of large numbers really easily when working with simple data sets. But as our data sets become more complicated we forget to think about the law of large numbers.

Here is an example where I think the author really wants us to think about the law of large numbers. We have a data set that tracks student performance across different schools. We might want to include in our model some impact unique to each school. We have to be careful because it is possible that we do not have a lot of data for some schools. We build one model for all students but we lose track of the fact that our model will be more accurate and less noisy for schools where we have more data.

THe problem is that we treat all inference the same. Imagine we built a logistic regression model. While logistic regression does have confidence intervals for the learned coefficients, practitioners do not always use them. This is one reason baking uncertainty into all of our models is critical. If we include uncertainty then we will know that our estimate for kids in schools where we have less data is more uncertain than in schools where we have more data.

## Chapter 5

Chapter 5 introduces the idea of loss functions. When we are training traditional Machine Learning techniques the loss functions are often directly baked into training. When we train a neural net we have to specify what our loss function is. The author shows how we can use loss functions with models we have trained with pymc3 to make our models flexible to different contexts.

Incorporating different loss functions is important because it allows us to treat different types of errors differently. Rarely do all types of errors have the same consequence. For example, over predicting might be more dangerous than under predicting. Or under predicting by 2% might be a lot worse right around 0 then it is in other places. Loss functions allow us to tie our models closely to the business context we are using them in.

The author uses an example of stock market returns. We care about the difference in our prediction from the truth but we also really care about the sign difference. It is much worse for us to get the sign wrong in our error then an equivalent error of the same margin where we do not get the sign wrong.


## Chapter 6

Chapter 6 is all about how we pick our priors. The author breaks priors down into two separate categories. One type of prior is an *objective* prior. Objective priors are ones where we are not including any additional information. Every point in our solution space is equally likely. *Subjective* priors on the other hand are where we include some information and therefore make certain places in our solution space more likely and others less likely.

In this chapter the authors explore how to get information from domain experts and to include that in our model through priors. Often domain experts are not statistics experts and so we do not want to ask them to give us a distribution. Instead we want to solicit feedback in a way more native to them and then we can turn their input into a distribution. Earlier this year I read a [paper]({{< ref  "/writing/papers/2020/eliciting_beliefs.md"  >}}) that was a survey of different ways to do this.

Two useful resources that were linked in this chapter. The chapter mentioned how  it can be helpful it use[Conjuge priors](https://en.wikipedia.org/wiki/Conjugate_prior#Table_of_conjugate_distributions) for mathematical simplicity. The chapter also introduced me to the idea of prior distributions over matrices. This is really powerful when we want to predict multiple things that are correlated with each other. The [Wishart Distribution](https://en.wikipedia.org/wiki/Wishart_distribution) and the [LKJ distribution] (http://bois.caltech.edu/distribution_explorer/multivariate_continuous/lkj.html) are distributions over matrices.

At the end of the chapter the author shows my favorite derivation I learned in school. The derivation shows that penalized linear regression is the same as bayesian regression with certain priors. We show that using l1 or l2 norm corresponds to different priors. Understanding regularization as a prior was such a helpful step for me.


