---
title: 'Green AI'
date: Mon, 30 Sep 2019 03:40:49 +0000
draft: false
tags: ['Machine Learning']
categories: ['Papers']
---

[By Roy Schwartz, Jesse Dodge, Noah A. Smith, Oren Etzioni](https://arxiv.org/abs/1907.10597)

## Summary

The authors of this post argue that a large percentage of machine learning research focuses on Red AI and make a call for more research to be centered on Green AI. The authors define Red AI and Green AI as follows: 

* Red AI: research that makes small improvements on the state of the art by leveraging more computation resources
* Green AI: research that focuses on diminishing the amount of computation necessary to reach a result. Research that is able to reach similar levels of accuracy with higher efficiency. 

The authors of the paper are very careful to call out that Red AI is not bad and that there is important research would could be classified as Red AI. They argue that too much research falls into the category of Red AI and we should reward research more that falls into the category of Green AI. 

The authors specifically call out that access to computation resources is a luxury. When there is a necessity of large computation grows to replicate results or the ability to build upon results is only accessible to individuals with those resources. The authors believe that democratizing access is important, and when results are based on large compute that limits who can partake in the research process. 

In the paper the authors show that there are logarithmic returns to accuracy from an increase in the size of computation. This means if we increase computation size by a factor of 2, our accuracy will only increase by a factor of log(2). If there are truly logarithmic returns to scale of increasing compute size, then increasing compute will not be a sustainable way to continue building more accurate systems. 

The researchers propose FPO (total number of floating point operations) as a metric for measuring the efficiency of an algorithm. They outline the importance of having a metric to calculate efficient that is hardware independent. 

## Thoughts

* It is easy to forget than AI/ML is still such a young field. Best practices in terms of making improvements and how to build upon previous research are still being established. One difficulty in determining what research is of the highest quality is we do not know what directions will bring us the most success. It is possible that once we reach a certain level of compute or a certain amount of training data, our systems will actually have much greater capabilities. If that is the case, research that increases the amount of compute and gets higher accuracy is still important. I think the main takeaway from this paper is a call for more diversity research approaches. Because we do not necessarily know the best paths forward it is important we try lots of different paths.  We should reward research approaches that are new and that take different approaches rather than publishing every paper that gets slightly better results by using more resources. 
* In the paper, the authors argue that we should democratize the ability to do research. If only people with a lot of resources are able to do research, then we are limiting the number of places new ideas can come from. In theory this makes a lot of sense to me. With greater diversity and more input we should be able to make more progress. I would be very interested to see if there was a paper that looked at how democratizing a resource changed research outcomes.  
* The authors comprehensively explain their reasoning behind why FPO is a good metric for efficiency. It was refreshing to see the authors break the efficiency problem down into smaller chunks, propose alternative solutions and then explain why they believed their solution was optimal. This process of breaking the problem of efficiency down into smaller steps was key. If you were tasked with just creating a metric that tracks efficiency that is a very open ended problem. But the problem becomes a lot easier to tackle when the authors break efficiency down into three separate values. 
* One part of the paper I was particularly interested in exploring more is about hyper parameter search. Rarely in a paper do the authors explain how much time they spent optimizing hyper parameters or how those hyper parameters were optimized. Papers also rarely show model results when you use non-optimal hyper parameters and how far these results deviate from the optimal results. I would be curious to hear more about how long it takes researchers to get the best hyper parameters. If there is a large difference in performance between optimal and non-optimal hyper parameters and it is very computational intensive to find the correct hyper parameters are the results replicable?