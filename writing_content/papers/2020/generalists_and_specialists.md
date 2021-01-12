---
title: "Generalists and Specialists: Using Community Embeddings to Quantify Activity Diversity in Online Platforms"
date: 2021-01-11T12:12:35-06:00
draft: false
tags: ['Design']
categories: ['Papers']
---
[Paper Link](https://dl.acm.org/doi/10.1145/3308558.3313729)

By [Isaac Waller](https://waller.is/) and [Ashton Anderson](http://www.cs.toronto.edu/~ashton/)

### Paper Motivation

In most spheres individuals are phased with the tradeoff between being a generalist or a specialist. Online platforms are no different. The authors wanted to explore if users concentrate deeply with a narrow focus or apply themselves less deeply but more broadly

### Paper Contribution

The authors define a measure of how generalist or specialist a user. The authors do so by creating community embeddings that represent communities in a high-dimensional space. Using their metrics the authors find online platforms contain a lot of diversity including extreme specialists and extreme generalists. The authors observe behavior on both Reddit and Github.

The authors find some behavior to be more common of specialists or generalists. Specialists stay in communities they contribute to where as generalists are more likely to stay on the platform as a whole. Generalists also engage with more diverse sets of users than specialists.

### Background

The specialist versus generalist framework is common across many different domains. It is a trade-off between breadth and depth. Viewing social networks through this lens elicits a number of questions.
- How connected is a platform on a global level? If almost all users are specialists then the platform is probably made up of isolated communities.
- Are users behavior patterns a result of their nature or based on the incentives of the platform itself?
- There has been much discussion in other realms about whether being a specialist or generalist leads to more success. Could we look at onlike platform through a similar light?

There are many real challenges in studying users diversity in actions. Measuring similarity between different types of activities is difficult. Previous researchers have used entropy as a measure of similarity. Entropy does not recognize the similarity in different communities though.

#### Community Embeddings

The authors present a new methodology to study generalists and specialists. In Reddit the authors are interested in the diversity of subreddits that users participate in. On GitHub the authors look at the different code repositories that users interact with.

The authors adopt [word2vec](https://en.wikipedia.org/wiki/Word2vec) to create a vector for each community.  They treat users in a community as the context for that community. Two communities are similar if the same users frequently comment in both of them.To measure the quality of their embeddings the authors perform a similar analogy task to what is done with word embeddings.  With good word embeddings if you subtract man from king and add women you should get queen. The authors adopt this process for their community embeddings. The authors use these vectors to define a similarity between any two communities using cosine similarity.To get the best possible community embeddings the authors performed a grid search over hyper parameters. Finding the right hyper parameters lead to a large increase in performance. Small changes in hyper parameters can lead to a sharp decline in performance.

A user's activity can now be represented as a distribution over the points in this vector space of communities. A specialists distribution would be very concentrated while a generalists would be quite diffuse. The authors define A __Generalists-Specialist Score__ or GS-Score as the weighted difference between the centroid of their distribution and all their other activity. GS-Score can range from -1 to 1 where -1 is an extreme generalist and 1 is a specialist. The authors validate there GS-Score by running an online quiz and showing people users behavior. They ask users to rank people in terms of specialist and generalist.

#### Results

The results from the paper can be divided into two categories. Users and community.
**users**
- There exists both extreme generalists and extreme specialists with most people lying with a score of between 0.5 and 1.
- On Reddit specialists comments average more upvotes than generalists
- The finding that specialists and generalists stay on the platform in different ways has interesting design implications. Platform designers might want to encourage exploration where community managers might want to seek out specialists.
- Generalists interact with a more diverse set of users than specialists

**communties**
- The authors define the activity diversity of a community as the average activity diversity of its users.
- The authors use their community embeddings to generate community reccomendations based on similarity in their vector space. It performs just as well aa state of the art collaborative filtering.
- The GS Score can also be helpful in predicting user retention. The authors train a simple logistic regression model using comment count, entropy and GS-score as features. GS-score is a really helpful feature.

## My Closing Thoughts

I thought this was a really solid paper. It takes a framework from another discipline and then applies that to study social networks. The paper does a good job of outlining why the specialist and generalist framework is helpful and quantifying it in this new space. I personally found the results from their experiments less interesting, but for those designing social networks this provides a very insightful way to do research about your platform. I would be suprised if a lot of social networks are not all ready doing this.

One thing I have trouble wrapping my head around is how much performance depends on finding the correct hyper parameters. Such depedence on hyper parameters makes me uncomfortable because it feels like the model is not robust. Hyper parameters are especially difficult when I am unable to wrap my head around why certain ones are better. With my most hyper parameters we can intuitively understand what the impact of increasing or decreasing the value is. But when there are a lot of hyper parameters and they interact in complex ways that can be quite difficult.

I felt the reccomendation part of the paper was not very strong. They framed reccomendation as trying to predict which communities a user will join in the next six months. I think having a stronger framework for a reccomendation task can be really important. I really enjoyed this [paper]({{< ref  "/writing/papers/2020/deconstructing_filter_bubble" >}}) that I read earlier this year that has a really strong framework for reccomendation. One idea from this paper that is worth further exploration is that recommendations are more important for specialists then they are for generalists.

This paper had a slightly different structure than a lot of the other academic papers I read. The related work section was at the end and the introduction was a lot longer. The introduction was packed with a ton of really good information. A helpful framework to think about organizing a paper might be thinking in terms of drop off. The highest number of people are going to read your abstract. Some percentage of users will drop off after the abstract. If we want to maximize engangement with our paper then we should try and put as much up front to get people to keep reading.


