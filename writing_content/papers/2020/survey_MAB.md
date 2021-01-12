---
title: "A Survey on Practical Applications of Multi-Armed and Contextual Bandits"
date: 2020-06-08T13:19:21-05:00
draft: False
tags: ['Reinforcement Learning']
categories: ['Papers']
---

By [Djallel Bouneffouf and Irina Rish](http://arxiv.org/abs/1904.10040)

## Summary

The authors begin the paper by highlighting that Multi-Armed Bandit (MAB) algorithms have gotten a lot of attention recently for their ability to learn with less feedback. Multi-Armed Bandit approaches thrive in situations where we can not use a supervised approach and have to make decisions with minimal feedback. This paper is a survey of the top recent developments in the field. They authors introduce a taxonomy to classify different types of MAB problems and explain the state of the art in each category.

A MAB problem is a sequential decision making problem. At each point in time, an agent must choose the best action out of several alternatives. After the agent picks an action the agent observes the reward from that action. Observing the reward from the action gives us more information to help make a better decision in the next time period. At the core of MAB problems is finding a trade off between exploration and exploitation. Exploration is making a different decision and learning information about the reward from that decision, and exploitation is making a decision we have already made because we know it's reward. In a MAB problem agent must learn how to make decisions to maximize the cumulative reward over all time periods.

A specific type of MAB problem is a Contextual Multi Armed Bandit (CMAB). In CMAB there is a context, or feature set associated with each action. For example, if you want to pick which drug a person should take, then the context is information about the drug. The context might consist of who the manufacturer is, the efficacy of the drug in trials etc... For this problem, exploration is choosing a new drug, and exploitation is taking the same drug.

* * *

After laying out the high level formation of a CMAB problem the authors explain different applications

- Healthcare: Use a MAB approach for conducting clinical trials. Rather than one trial with one result we can think of trials as sequential decision making.
- Finance: Sequential portfolio decision making. We get rewards from making decisions and then have to make another decision.
- Dynamic Pricing: A retail company has to determine what price to set their goods for each time period.
- Recommender Systems: A system has to balance recommending similar things versus new ones. The system has lots of information about content but very little information about each user.
- Influence Maximization: A product wants to maximize the number of users that become aware of a product by selecting a seed groups of users to expose.
- Information Retrieval: What document should be returned to a specific user based on a search
- Dialogue Systems: Use Multi Armed Bandits to pick the best response to a piece of dialogue. Use MAB to make proactive chatbots. Having a multi-domain dialogue system where we want to choose which chatbot to use.
- Anomaly Detection: Maximize the number of true anomalies that is shown to the human. Having both exploration and exploitation is imperative to adapt to changes.

* * *

Next the authors discuss how bandits can be used in machine learning.

- Algorithm Selection: We can thinking of picking which algorithm to use in a problem as a MAB setting.
- Hyperparameter optimization: This can be turned into a bandit problem.
- Feature Selection: we want to only use a small subset of features, we need to pick features
- Active Learning: Labeling all examples is impossible so we need to pick which examples to label.


## Thoughts

In the beginning of the paper the authors assert that they create a taxonomy for MAB problems, but they never explain their taxonomy in the paper. They show the taxonomy in a couple of charts but never explain the different groups. The authors also do not look at how different algorithms work better for different groups in their taxonomy. They provide very little guidance about which version of MAB to use or the tradeoffs between different versions. I was hoping to see some discussion about how different versions of MAB work better for different problems.

Here is the authors taxonomy explained. They break MAB problems into four categories. A MAB problem is either contextual or non-contextual and it is either stationary or non-stationery. The authors explain what it means for it to be contextual, we observe some context about each arm that we can learn from. Pulling an arm gives us information about not just itself but other arms with a similar context. A non-stationery problem is one where the reward from pulling an arm actually changes over time. If you have to pick which stock to invest in, the reward from each stock changes over time.
