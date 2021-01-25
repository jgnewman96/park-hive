---
title: "From Optimizing Engagement to Measuring Value"
date: 2021-01-25
tags: ['design', 'machine learning']
categories: ['paper']
---

[Paper Link](https://arxiv.org/abs/2008.12623)

By [Smitha Milli](http://smithamilli.com/), [Luca Belli](https://www.linkedin.com/in/lbelli/) and [Moritz Hardt](https://mrtz.org/)

### Paper Motivation

Recommendation engines are built to increase user engagement (often measured by clicks). This measure of engagement is different from the actual value that we want to deliver users. Just because a user clicks on an item does not mean it delivers value to them.

### Paper Contribution

The authors introduce a new approach to building recommendation systems. Their approach can be broken down into three steps. Each one of this steps is a novel contribution.
1. Use measurement theory to  aggregate different engagement signals into one measure of value.
2. Provide a general latent variable model that relates value to the observed engagement signals. We can use this model to optimize for the value that the designer cares about
3. Provide guidance for the designer in evaluating and revising the model

The authors implement their approach on twitter and assess the validity of their new approach

### Background

We should build recommendation systems to take into account engagement only as it correlates with the value we want to deliver to users. Engagement with an item  provides some signal for “value“ but is not necessarily equivalent. Different types of engagement might provide different value. Not all clicks on an item can be treated as equal. Specifying an objective function for the value we actually want to deliver is much more difficult than optimizing engagement.

### Measurement Theory and Latent Variable Models

Measurement theory provides a basis for measuring unobservable values such as “quality of life“. The unobservable value is thought of as a latent variable which we can relate to observable variables through a model. We can extend this to our context by thinking of the value of a recommendation as the latent variable.

This latent variable model will contain both V our value from the recommendation and all our observables engagement behaviors such as clicks, likes or shares. We can now formulate our objective clearly. Given a set of behaviors, what is the probability a user values an item.[^1]  The authors use a model that treats one type of behavior as an __anchor variable__. For this anchor variable we know the probability of value given this behavior. Strong explicit feedback from a user serves as a good candidate for the anchor variable. Reporting a content item or downvoting would also be good choices.

We represent user behavior using a binary random vector. Each possible action is one bit in the vector. The first bit is whether or not you click, the second bit is whether or not you reply etc.. The anchor variable allows us to connect all of the different possible behaviors to our latent "value" variable. The latent variable model (LVM) is represented as a Bayesian network. This is a DAG that has a factorization of the joint distribution of variables. This is important because some actions can only occur after another (e.g. a click can only retweet after clicking). The DAG makes modeling this dependencies straightforward. The image below shows the DAG that the authors used for twitter.

![Twitter Dag](/papers/2021/twitter_dag.jpg =90%x*)


For the authors strategy to work the following assumptions must hold
1. Regardless of the other behaviors that happen, the anchor introduces information about the "value"
2. An anchor variable has no children. This means a user cannot exhibit the anchor behavior and then another type of behavior.
3. The amount of information that is conveyed when a user exhibits the anchor behavior does not depend on which other behavior was exhibited.

The authors prove that given these assumptions, we can understand the relationship between behaviors and "value" based on observable behaviors. This happens in the following steps:
- we observe the probability of the anchor and other behavior through data
- we set the probability of value given the anchor
- we set a prior on the probability of value in general
- we can use some historical data to estimate the relationship between the anchor and the parents of the anchor. We do this using two datasets. one dataset has algorithmic recommended content and one has random content. we assume the algorithmic content is more often valuable. The two datasets will also have different observed behavior, but the relationship between value and behavior across the two should be the same. By setting the amount of value we think is in each dataset we can estimated the probability of parent nodes of the anchor giving value.

### Case Study on Twitter

Twitter contains many different types of behavior: clicks, favorites, retweets, replies and much more. Specifying one objective using all of these behaviors is difficult. The typical approach is one objective that trades-off all these behaviors using linear weights.

Twitter gives users the option to hit “See less often“ on tweets. The authors use this behavior as the anchor variable and assume when a user hits this then they do not value that tweet. Their model naturally learns the relationship between other behaviors and value. The designers do not have to manually make a linear weight for each behavior. They can also re-train the model at anytime incorporating new data. The authors applied this bayesian network to ML driven push notifications.

The authors fit their model on three days of data that contained all user interactions with ML-based push notifications.

The results from fitting their model can be seen in the table below

![Twitter Results](/papers/2021/value_LVM_results.jpg =90%x*)



### Assessing validity

The authors provide five different possible ways to assess the validity of their approach. They argue that we should not evaluate the model based on it's relationship to engagement. The whole nature of this paper is that engagement is a faulty metric.

1. **Evidence based on content**: Are the behaviors available on the platform sufficient to capture value? It is necessary to design a platform which allows users to give rich feedback.
2. **Evidence based on cognitive processes**: When we ask users about value do their assessments line up with what our model learned?
3. **Evidence based on internal structure**:Does our model learn that behaviors which we think of as having a stronger signal actually have a stronger signal?
    - This is the only type of validation that the authors actually do. The authors believe that the values that are learned from their model are aligned with their priors. All behaviors that are supposed to be a signal of value seem to be. The rank ordering also lines up with the authors prior.
4. **Evidence based on relations with other variables**: Does our measure of value correlate with what users say they value in a survey?

5. **Evidence based on consequences**: Do we see that users enjoy the platform more and engage with it more after introduction of our new method?


## My Closing thoughts

Overall this was a really enjoyable paper to read and provided good insight into a novel approach. The approach was well motivated and the model was outlined quite well. They did not discuss all implementation details but at a high level what the authors did is very clear. I particularly appreciated how they accompanied some of their mathematical notation with plain text descriptions.

This paper does not discuss designing systems to get feedback in depth, but while reading this paper I was constantly returning to this article about [Tik Tok by Eugene Wei](https://www.eugenewei.com/blog/2020/9/18/seeing-like-an-algorithm). Systems are limited in the ways they allow users to give feedback. If you allow users to give more rich feedback you can learn more about what users value and what they do not. The results of this paper make it clear that twitter does not allow many ways for users to give negative feedback. Every type of feedback led to assuming an increase in value from that piece.

In the paper there were a couple of different assumptions the authors made that I was curious about. They assumed a prior probability that an item provides value of 0.5. That seems like a pretty high prior to me! 50% of items provide value. That would be really good. Then also with their historical datasets they set the amount of value. For a random set of recommendations they set probability of value as 0. That also seems really low to me.

But that also raises another question! What is a random notification? I seriously doubt it is just a random text string. It would have been helpful if the authors defined the space of notifications. Providing some of those details would have been really helpful. There is still a lot missing in terms of actually operationalizing this. Are the notifications that we are sending set and we just have to determine when to send them? Do we need another model that actually does NLP work with notifications?

From the paper it seems like the authors never actually incorporated their model into twitter's production system. I would have loved to see how the model would have worked in production. Did it lead to better user outcomes? Did it lead to users staying on twitter for longer?

The last thing I would have been interested in is a discussion of what the value metric actually means. What does a probability of value of 0.7 mean? How does that compare to a probability of value of 0.6? What are the normative implications of these values?

[^1]: In this paper they treat value as a binary. Either an item provides value or it does not. I am curious if the model might look slightly different if we treated value as a continuos variable? My intuition is that it does not make a difference because they model the probability an item provides value. This means we can predict anything from 0 to 1. It is possible though that things could look slightly different by using a more expressive space than 0 to 1.
