---
title: "An Experimental Study of Structural Diversity in Social Networks"
date: 2020-08-07T15:17:42-04:00
draft: False
tags: ['Design']
categories: ['Papers']
---

By [Jessica Su, Krishna Kamath, Aneesh Sharma, Johan Ugander, and Sharad Goel](https://arxiv.org/abs/1909.03543)

This paper from Twitter and Stanford has the following motivation:
- The theory of structural diversity predicts that individuals derive increased utility from interacting with people from different parts of their social network. Previous evidence for this theory comes from observational studies which makes it difficult to make any casual statement.

## So what is structural diversity?

People consider the actions of their social contacts when making decisions. A basic framework is the following: the more people you know who do something, the more likely they are to do it.

- e.g. The more of your friends who ski, the more likely you are to ski

**Structural diversity** extends this framework. It is not simply the number of contacts, but also the network structure of those individuals. You are more likely to do something if your contact who due an activity contain structural diversity. Containing structural diversity means they come from different parts of your social network.

- e.g. A individual is more likely to ski if two work colleagues and two friends do then if four friends do.

If we accept the the theory of structural diversity we should find that people are more likely to take up an activity if the part of their network that does that activity is structurally diverse.

## The experiment

In this paper the authors conduct a randomized controlled experiment on Twitter to evaluate the casual impacts of structural diversity on actions. he authors first show that observational data is consistent with previous findings that structural diversity impacts retention on Twitter. However, in the randomized experiment, there is no difference in retention between the treatment groups with low, medium and high structural diversity. This experiment implies in our context the correlation between structural diversity and retention does not seem to be casual

The experiment was done on a randomly selected group of the 4.2 million users on Twitter during 2016. The outcome of interest in the paper is 3 month retention. The authors define 3 month retention as going on twitter once in the 30 day period 90-120 days since joining. [^1]

The quantitative definition they use for structural diversity is a variant of average pairwise cosine similarity. The lower the level of similarity the higher the diversity.
- sim(v, w) is the similarity for two users v and w
- It is the cosine similarity of the binary incidence vectors for users who follow them. Two users are considered similar if similar users follow them
    - Due to twitter's production system can only compute similarity for 40 most similar users and set everyone else to zero. [^2]

The key part of the experimental design for this paper is how they go about randomizing structural diversity. During sign up users are prompted to select topics they are interested in and then shown accounts related to those topics. Next users are asked to import contacts from their phone or email. After that users are shown recommended accounts to follow based on their social circle.

Twitter uses an ML algorithm to provide a ranked list of individuals. This ranked list is bast on how likely they believe the new users are to follow them. New users are shown the top 20 people of this ranked list. The authors manipulate this list of 20 people to divide users into groups of low, medium and high structural diversity.

For each new user, a similarity graph was created for their contacts. An edge is drawn between two users if they are in each others top 40 most similar users. One section in a users social network is a part of the graph that does not connect to other parts. Users were than eligible to be assigned into one of the random groups if they have one component of size 20, two components of size 10 and three components of size 7. This eligibility requirement is necessary because if they do not have this structure then they cannot be assigned to any of the three groups. [^3]

- A user is then assigned to one of the groups
    - high similarity -> all 20 people are from their largest component
    - medium similarity -> 10 people from their largest and 10 people from their second largest
    - low similarity -> 7 from the two largest and 6 from the next largest
    - control: Twitter's ML algorithm [^4]

They authors look at the subset of users in their study that decided to select all of the recommended people to follow. [^5]

## Results

The authors first show that if you just look at observational data, it does look like there is a correlation between structural diversity and retention. But this difference goes away when you look at the results of their experiment. But, it also turns out that this relationship goes away when you look only at eligible users.

## Closing Thoughts

* While the findings of this paper are kind of interesting, the most interesting part of this paper is running a huge experiment on a social network. The authors do a good job enumerating the difficulties of this and it is really cool to see this kind of work happening.

* While the authors do call out generalizability concerns in the conclusions of the paper, I think the beginning of the paper is overselling the results a little bit. The generalizability of their results is truly quite a narrow group.

* I wish the authors had focused more on this difference between data for eligible users and non-eligible users. The correlation between diversity and retention disappears when we look at only eligible users. This means that their finding of no effect makes a ton of sense, it is not in disagreement with the observational data. So why did this difference happen between eligible and non-eligible. It seems like eligible users had the a structural diverse network already on twitter whereas non-eligible did not. I really would have loved more discussion of this.

* I also would have loved to see more discussion of the normative impacts of their findings. How do their findings impact how we think about design in general. One of the reasons experiments is so powerful, is that often we can take the findings in apply it to another use case. There are so many tech companies that use Machine Learning to optimize the design of a system. What I want to see is research about why these design choices are working and therefore these design principles can be applied to other places.




[^1]: It does not make sense to me why the used such a narrow definition of retention / engagement. It seems like they could have used other metrics that were not a binary but rather continuous. Using a continuous variable would make me less concerned about forking paths

[^2]: I would have liked to see some evaluation of how this limitation impacts their results. If this was 20 vs. 60. vs. 100 what would that have looked like.

[^3]: We will return to this later, but this eligibility requirement is going to be a big deal. only 500,000 out of 4.2 million were eligible.

[^4]: I would be interested to have seen more discussion of twitter's ML algorithm. How does it work and how does the retention rates for control compare to the other groups.

[^5]: This diminishes the generalizability of findings to an even smaller sub population.
