---
title: "Competing Bandits in Matching Markets"
date: 2020-01-15T14:26:31-08:00
draft: false
tags: ['Economics']
categories: ['Papers']
---

## Summary

This paper explores matching in two sided markets through the multi armed bandit problem. An example of a two sided market we can model using multi armed bandits is matching workers to employees. There is a pool of workers and a pool of employees. We want to find the optimal matching of employees and workers. Employees have preferences over workers, and workers have preferences over employees. There has been a lot of working that examines how to achieve an optimal matching. The most well known example of this is the [Gale-Shapley algorithm](http://www.eecs.harvard.edu/cs286r/courses/fall09/papers/galeshapley.pdf).

The novel contribution of this paper is it examines the setting where we do not know agents preferences. We have to learn them over time. In Gale-Shapley we know everyone's preferences and have to find a matching that is optimal according to those preferences. In this new situation, rather than making one matching using known preferences, there are multiple time steps and at each time step we have to make a matching. As we make matches we see the outcome of a match and learn agents preferences.

The paper sets up the scenario according the the following rules:

- There are N agents and K arms. (An arm is just a matching. So in the example of employees and workers, employers are agents and picking a worker is selecting an arm)
- N < K &rarr; every agent gets an arm
- At time step t each agent selects an arm
- Arms have preferences over agents which are known
- When multiple agents select the same arm, the agent which the arm has a higher preference for gets matched
- The agent receives a reward from matching to arm that is sampled from a gaussian with a mean based on the specific arm-agent pairing.
- An optimal match is defined as when an agent gets it preferred arm. A pessimal match is when an agent gets its least preferred arm.

This setting is difficult because there is a trade off between exploration and exploitation. If you know that an arm gives you a high reward you may want to keep pulling it over and over again. If you have find a worker that is good you want to keep hiring them. On the other hand, it is possible there is a worker that is even better that you do not know about. In order to find that worker that is even better you have to do exploring, rather than continuing to higher your known optimal. There is a trade-off between maximizing your pay-off with what you already know, versus being able to get a higher pay off from what you do not know.

The authors present two different platform that could facilitate the matching: decentralized and centralized.

* * *

In a centralized platform agents send in a ranking of arms and then the platform returns a matching vector. With a centralized platform we never have any conflicts where two agents select the same arm.

For a centralized platform one approach is the *explore-then-commit* approach. The explore section is devoted to learning agents preferences. The platform would return random matchings sampling from the space of all possible matchings. This would allow the platform to learn about agents preferences. The platform would then transition to the commit phase where it would create the best matching learned from the explore phase.

The authors argue this approach is not optimal because we are not taking advantage of what we learning during the explore phase. We only use what we have learned when we get to the commit phase. This could lead to us exploring matches that we know are not less optimal then when we have already tried. The authors propose another approach where at each time step the platform uses agents preferences to return a stable matching. The platform sees the results of this matching and learns more about preferences before creating the next stable matching at the next time step. The authors call this method Upper Confidence Bound (UCB) matching.

* * *

There are two types of decentralized platforms. In a decentralized platform with *partial information* agents observe each other actions and conflicts but cannot coordinate. In a decentralized platform with *no information* agents cannot even observe others actions.

Using Gale-Shapley matching it has been shown that agents cannot do better by faking their preferences. The authors also explore honesty in this setting. They find that under the assumption everyone else is honestly presenting their preferences, an agent cannot achieve a better outcome by submitting false preferences.

The authors look at the performance of both policies for centralized platforms and show that UCB approach performs better than explore-then-commit. They briefly look at the explore-then-commit strategy for decentralized platforms mostly as a way of motivating the necessity of further work.

## Thoughts

- I really enjoyed this paper! I have been thinking a lot about tradeoffs of late. In almost all things there is an inherent tradeoff between different approaches. We want to find a solution that takes the benefits of the different approaches into account and is able to act optimally. In this setting the tradeoff between exploitation and exploration is quite clear. This paper does a good job of taking something complicated and simplifying it to a place where we can see the core trade off.

-  The authors claim that this paper is a blend of machine learning and economics. In this paper I do not see many aspects of machine learning but here is why I imagine the authors make that claim. Machine Learning very rarely gives us to tools to handle scarcity. A classic machine learning setting would be learning agents preferences over arms. Machine learning would allow us to learn fairly good estimates of preferences without each agent having to sample every arm. By sampling a subset of the arms we would be able to create preferences for each agent. An example of this is Netflix learning users preferences of videos. Netflix is able to create estimates for a user's preference for a video, without them watching the video based on their preferences over other videos. In the Netflix situation though, multiple agents can watch the same video. We do not have to worry about finding an optimal matching because everyone can be watching the same video. But imagine a situation with scarcity. Only one person can watch each video. Machine Learning does not give us the tools to solve this problem. To solve this we need to turn towards economics. The first thing I learned in economics classes was how to think about an agent with a budget constraint. An agent only has so many resources and then has to allocate them in an optimal way. Economics give us the framework to answer this type of question by building a model of human behavior. We know users preferences and using this model we can derive what they will do. This paper blends machine learning and economics because we can use machine learning to learn agents preferences and then economics to predict behavior once we know preferences.


- Another way machine learning could be really powerful in this setting is to create individual policies for a decentralized platform. Imagine you are an agent in a decentralized platform and you have to make a decision between exploitation of what you know or exploring more. You could use the data you have already seen to help make this decision. If you assume rewards follow a known distribution, you could use the rewards you have seen to make an inference about what that distribution is. You can then make an educated decision about whether you are at a point where it makes sense to explore or to exploit.

- Another interesting line of research is examining how much worse a decentralized platform is from a centralized platform. While a centralized platform is nice because we have more information when we make decisions, there are also dangers of a centralized platform. It gives one entity a lot of control over the market. Imagine the centralized platform decided that it did not want to make matchings that were optimal for agents, but rather matchings that it found to be optimal. It will be important to understand how much worse decentralized platforms are at making matchings under different assumptions.

- This paper only looks at rewards coming from certain matchings. It does not consider that there might be socially optimal matchings that incorporate things outside of the individual rewards. It is possible that there are certain rewards we only receive when a set of matchings is made. For example if a certain ten matches are met, then there is an additional reward to each of the agents in those ten matches. This increases the complexity of the problem because it is not only about the individual match but about groups of matches.

- Another interesting direction is exploring a platform in between centralized and decentralized. I can imagine a scenario where small groups can coordinate and communicate but the entire set of agents cannot. What would happen if groups of ten agents could communicate?
