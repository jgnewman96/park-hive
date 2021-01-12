---
title: "Deconstructing the Filter Bubble: User Decision-Making and Recommender Systems"
date: 2020-11-26T15:47:47-06:00
draft: false
tags: ['Policy']
categories: ['Papers']
---

By [Guy Aridor](https://www.guyaridor.net/), [Duarte Goncalves](https://duartegoncalves.com/), [Shan Sikdar](https://www.linkedin.com/in/shan-sikdar-0b53785a)

[Paper Link](https://arxiv.org/pdf/1904.10527.pdf)

## Paper Motivation

There is a common theory that recommender systems lead to user consuming more similar content over time. This kind of affect is called a filter bubble where each user or group of users ends up in their own little bubble.

## Paper Contribution
The paper finds that recommendation can alleviate natural-filter bubble effects, but it also leads to more homogeneity across users. There is a trade off between homogenizing between user consumption and diversifying within user consumption. The authors argue that filter bubbling happens without recommendation systems and that recommendation systems will decrease the impact of filter bubbles.

The authors find that a more diverse set of consumed items does not always lead to greater consumer welfare. [^1] The authors assert that the benefit of a recommender system is the marginal welfare a user gains from having the recommender system versus not having it.

### Background

Recommender systems are critical when users face a really large decision pool. Users are not aware of most items and so need some way to sift through the available items. 75% of movies watched on Netflix and 35% of page views on amazon coming from recommendations. Recently there are worries about the unintended consequences of these systems. Could they lead to filter bubbles where users are not exposed to a diverse set of content or view points

Understanding the impacts of RS (recommender systems) is critical for designing systems that we want in our society

**Model of User Choice**

1. User sequentially choose items and face large choice sets. Consumers are long lived but consume a small portion of the choice set
2. Users are uncertain about how much value they will get from consuming the product.
3. Consumption of an item provides the user with more knowledge about their own preferences
4. a RS gives a user some signal about if they will enjoy a product. This can be broken up into user specific level impacts and based on data of other users

**Problem set up**
- There are n items in a product space T. We have a set of users I which face decisions about which n to consume.
- We can assign a monetary equivalent for each user for consuming an item, Before consuming an item the user does not know what that monetary value is. There evaluation before hand might be different than the actual monetary value they receive.
- P denotes the belief that a user has about how much they will enjoy an object n
- The realized value for consuming a good x can be decomposed into two parts. A users idiosyncratic taste. a common value component
- Consuming an item lets users learn more about related items

Rather than modeling how RS work the authors think about RS as giving users more information about how they will value a product

### Results
The authors look at three situations. For each situation they compare simulation results. The three situations are:
1. no RS
2. perfect RS
3. imperfect RS

We can also look at simulations results with different parameters. We can see how risk-aversion levels impact users behavior and how product correlation impacts users selections.

**Finding 1**: RS decrease local consumption because they recommend based on others taste
    - When users are more risk averse then they tend towards more local consumption.
    - When consuming an item tells you more about similar products that also leads to more local consumption.
    - recommendation decreases local consumption by providing information outside of your local space.

**Finding 2**: Converse of 1, RS increase diversity in consumption
**Finding 3**: The welfare gap between recommendation and no recommendation decreases as how much you learn about other products from one consumption choice increases
**Finding 4**: With no recommendations: diversity and welfare are negatively correlated with users have no risk aversion. They are uncorrelated when users have high levels of risk version.
**Finding 5**: Recommendation increases homogeneity across users

## Discussion
A recommender system should give users information they might not have.Rather than recommending a movie the user might know they will like, it should recommend a movie the user will like but that the user does not know about.
These findings Suggest an RS should collect more information about user beliefs and not only user experience! It also suggests a new way to formulate the problem of an RS: Predict what a user would consume with no recommendation, then give them something better than that.


## My Closing Thoughts

I really appreciated this research, but I think the framing should be switched. The abstract and introduction misrepresent the major contributions of this research. The findings from these simulations are not the major contributions. They are interesting, but it is hard to know how many situations they extend to. The main contribution of this research is that it provides a vocabulary and a structure to think about recommender systems. By providing this structure, it makes it easy for other researchers to extend this framework or build upon it. This structure provides a common vocabulary for us to examine RS.

Another novel contribution of this paper, is that it focuses on properties of the people. A RS will have a different outcome for different populations of interest. This broadens the scope of how we think about recommender systems. We cannot only focus on properties of the technology but must also reflect on properties of the people who are interacting with the technology.

A lot of these findings are probably dependent on the type of recommender system we are looking at. Different recommender systems will have different impacts and push people in different directions. I would be excited to see work looking at differences in recommender systems.

In this paper, they focus on comparisons between a world with RS and a world without RS. But that seems like a faulty comparison to me. There is not actually a world with no RS. Netflix is always going to present you with some choices. I guess it could only provide you with a search bar and that is the only way to interact with the platform but that seems like an unrealistic comparison.

I would be really really interested in a paper that builds upon this by trying to find some of the parameters from this model for an actual RS. Could we find values for some of these parameters for Youtube or Netflix's RS.

I wish this paper included some discussion of what we are trying to design for. Why is a filter bubble bad? Why is diversity in consumption good? This paper explicitly only focuses on individual consumer welfare, but most of the way I think about the potential impacts of RS is through societal welfare. How is society negatively impacted when everyone is consuming different content?

[^1]: But what about social welfare? This paper does not have any mention of that.

