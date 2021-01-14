---
title: "“Data Strikes”: Evaluating the Effectiveness of a New Form of Collective Action Against Technology Companies"
date: 2020-11-26T15:32:49-06:00
draft: false
tags: ['tech policy']
categories: ['Papers']
---

By [Nicholas Vincent](http://nickmvincent.com/#/), [Brent Hecht](https://brenthecht.com/), [Shilad Sen](https://www.macalester.edu/mscs/facultystaff/shiladsen/)

[Paper Link](https://brenthecht.com/publications/thewebconference2019_datastrikes.pdf)

## Paper Motivation

There have been some calls for “data strikes“ in response to worries about the power of large technology companies. These strikes aim to starve business plans predicated on collecting large amounts of user data. Little is known about how a data strike would work or if it would even be effective.

## Paper Contribution

Focusing on recommender systems, the authors simulate data strikes under many conditions. The paper suggests that a data strike can be effective in tandem with a traditional boycott. Overall the paper provides evidence that data strikes could be a useful protest tool and that individuals have more power in their relationship with large technology companies then they realize.

### Background

There has been a growing criticism of large technology companies and the power that they wield. Many of these large tech companies depend on the public's “data labor“ to power their systems. Google requires users clicks to train its search engine; Amazon and Netflix require data from users in order to make recommendations to other users.

This dependence on user data is a powerful tool the public can leverage. “Data strikes“ could work in the following way:
First, users withhold their data from the platform thereby making the experience on the platform worse. Because the platform does not want to lose more customers as a result of the bad experience they make concessions in response.

Many of the calls for data strikes are based on the view that data is labor. A data strike is then similar to conventional workers strike that might be organized by a workers union. There has been more legislature pushing for the ability to erase data from a platform. This makes executing a data strike a lot easier. GDPR makes more powerful data strikes possible than previously possibleOther research shows that tech companies are quite dependent on free user created content. Previous research has shown that Google performance degrades when Wikipedia is removed from search results

There is currently almost no information about how successful a data strike might be, what form it might take or how to organize a data strike. The goal of this paper is improve our understanding of data strikes through empirical research. The authors situate data strikes in the context of a more traditional type of protest, boycotting. While boycotting is inherently a data strike, a data strike can still occur without boycotting.

### Data Strike Framework

In order to successfully simulate the impact of data strikes, we need a more narrow definition of what a data strike is. In traditional boycotts: protests are consumers who cut off flow to an asset. In a strike: participants are laborers who stop performing work for a firm. In most cases, a boycott against a tech company is implicitly a strike. If you stop using Youtube, they are also no longer collecting your data. You can be in a data strike without boycotting though. By using private browsing or deleting your data.

There are four ways these boycotts could impact revenue

- direct data labor effects -> decrease in performance
- indirect data labor effects -> other people respond to decrease in performance
- direct consumer effects -> people stop buying things
- indirect consumer effect -> loss of economy of scale because market size is smaller

### Methodology

The authors evaluate recommender systems under a variety of simulated data strikes [^1]. When evaluating a data strike we can not simply look at the RMSE of the system. RMSE does not take into account people leaving the platform. It is too narrow of a metric.

The authors use a new metric to evaluate the impact of a degradation in performance. They call their metric surface hits. This measures the fraction of hits (defined as a rating of 4.0) across a group of users. A perfect recommender system will have a surface hits value of 1.0. Surface hits decreases when users boycott.

**Simulation Configurations**

The authors ran simulations under a few different data strike simulations. They first look at just general date strikes. The users that boycott are a random subset ranging from 0.01% to 99%. Then the authors simulate strikes by set of homogenous set of users. Either people with shared demographic groups or similar rating history. They then also look at results where different amounts of people take part in the strike.
- e.g What happens to recommendations for women when 50% of women participate?

### Results
The authors simulations find that boycotts are much more effective that data strikes. [^2] Strikes are less effective when more data has been collected [^3]. The authors highlight  the need for a better way to measure the impact of a decrease in performance. Even a small decrease in performance can impact Netflix a ton.

There authors find Homogenous strikes are good at degrading performance for a specific group. When a group is more unique their strike is more likely to hurt.

While data strikes are less effective they boycotts they allow people to keep using the platform. This means people are less impacted by taking part in a data strike and therefore it lowers the barrier of entry to participating.

This simulations provide evidence that collective action against tech companies has the potential to be even more powerful than traditional boycotts. [^4]

### My closing Thoughts

This research paper is really thought provoking and explores a novel space really well. It both provides a framework for thinking about data strikes and some evidence about the impacts of a data strike. It also leaves a lot of open questions and possibilities for extensions. This is the type of research paper that I get really excited about. It helped explain a new space to me, gave me a framework to think about it and opened a ton of new questions in my head.

One place I think this paper could have been improved is to think about degradation in performance differently. I do not find the surface hits metric to be that helpful and I think its still not measuring what we are interested in. I would break down the problem into two separate steps. There is the first order impact on accuracy or effectiveness of the system. There are a lot of different ways to measure that effectiveness. Rather than just looking at one metric I would look at a few different ones. Then there is the impact of that effectiveness on user retention. How much does a decrease impact user retention? It is possible that a small decrease impacts it a lot or it is possible that a large decrease does not really matter that much.

This paper also introduces a lot of interesting questions about how to make a data strike actually happen. How would you coordinate it and make sure that everyone is bought in? How would you interact with the platform that you are striking from? How would you monitor the effectiveness of the strike?

One last thought: What if you purposely feed bad data rather than not giving it data? What if you went on Netflix and instead gave a high rating to movies that were bad rather than not giving it any data?

[^1]: The recommender system that the authors evaluate does not use a state of the art infrastructure. Some of the findings might be out of date with more state of the art systems.

[^2]: I feel like the way the authors are looking at this problem is kind of misaligned. The way to think about it is in terms of degradation over time. Recommender systems not static problems. It is that the data strike makes it so the recommender system cannot keep with new content or changes in preferences.

[^3]:  I would love a interface where I can play with simulation inputs and see results

[^4]: Is it possible that what makes tech companies have lock in and grow so big also makes it easier for them to fall?

