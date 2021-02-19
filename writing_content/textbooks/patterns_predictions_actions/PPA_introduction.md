---
title: "Patterns Predictions and Actions: Chapter 1 - Introduction"
date: 2021-02-17
tags: ['machine learning']
categories: ['textbooks']
---
I was ecstatic when I heard that Ben Recht and Moritz Hardt had released a [new textbook on machine learing](https://mlstory.org/). Recht and Hardt are two professors who I admire a lot and who write papers that I have found to be quite accessible. I am excited to read their textbook and learn how they are teaching machine learning. 

I was able to convince my roommates to read this textbook with me. For each chapter I plan to post a summary and then also some discussion questions. 

* * * 

### History of Machine Learning

The introduction to the textbook begins with some history about data and where the first ideas of using data to make predictions come from. We are using data to make inferences about **unknown outcomes**. These **unknown outcomes** could either be in the future or just unobserved values that have already happened. We are attempting to use seen observations to make a prediction about the value of those unknown outcomes. 

Our predictions are going to be accurate if the patterns in our observed outcomes are consistent with the unknown outcomes. This can be described using the idea of **generalization**. Generalization means that the rules which are consistent with our observed outcomes also apply to the outcomes that we do not see. 

The authors formalize this in a bit more detail using distributions. We assume that our seen observation come from a fixed data generating process or a fixed distribution. We fit a model based on that data. We then want to apply that model to some other data. We can test the accuracy of our model by evaluating how well it performs on data that the model was not trained on, but that comes from the same distribution. 

Using datasets as benchmarks was an idea introduced in the 1980s that transformed machine learning. It is something that is now a core part of machine learning. One of the most common benchmarks is ImageNet which brought large increases in performance on computer vision tasks. Benchmarks provide a common set of vocabulary, measurements and organization that allows for more progress to occur even when research is so decentralized. 

The authors argue that all of machine learning follows this basic set up. Machine learning is just pattern recognition. There are a lot of nuances about how to do that pattern recognition and how to make it work for different problems, but machine learning is pattern recognition. 

* * *

### Topics Covered in Book

Predictions are only useful when we are able to take an action because of them. But this process of moving from patterns and predictions to actions is quite a delicate one. It is also one that is not talked about as much. We are building machine learning models not just to make accurate predictions but to use those predictions to take actions. The actions we take though will often influence the data that we see in the future. 

The way we understand the impact of an action is through experimentation. We model the environment we are on and then we are able to understand how a specific action changes that environment and therefore impacts utility. Dynamic programming is an optimization problem that extends this action framework. In dynamic programming we observe data, make an action and see what happens. We have to make many actions over many time periods. Even in situations where the impact of our actions have lots of uncertainty, by observing the impact of our actions we can create a chain of actions that achieves optimal outcomes.

Reinforcement learning is a specific way to take parts of dynamic programming. With reinforcement learning we suggest that one should take actions which were successful in the past. There is a balance between learning about the environment and acting on what we know about the environment. This is the tradeoff between __exploitation__ and __exploration__.  Exploration provides more information about the impact of an action at the expense of taking the best action based on what we already know. The optimal balance between these two can be computed using dynamic programming. We generally use bandit optimization instead because it is simple and effective. 

Causal inference is a newer field in machine learning that there has been a lot of recent interest in. Researchers see causal inference as way to make machine learning more reliable and robust. With causal inference we can estimate the impact of hypothetical actions from the data.

* * * 
### Discussion Questions 

1. How does the authors definition of **generalization** compare to what you have heard in the past? How does that idea compare to the idea of **external validation** in economics? 

2. Do you agree with how the authors view actions and the role they play in machine learning? Lets talk through some common machine learning use cases and think about what actions look like in that framework
- Computer Vision 
- Content Recommendation 
- Language Translation 
- Playing Games: Chess, Go, Atari, League of Legends, Dota

3. How do you think causal inference relates to machine learning? What are the differences between trying to measure the impact of an action and trying to predict some value?

4. Is understanding the history of machine learning important to being a researcher or practitioner today? How did learning a little bit about the history change the way you think about machine learning / statistics?
