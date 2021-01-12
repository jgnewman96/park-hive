---
title: "When your bid data seems too small: Accurate Inferences Beyond the Empirical Distribution"
date: 2019-11-01T11:54:08-07:00
draft: true
tags: ['ODSC']
---

Talk given by [Gregory Valiant](https://theory.stanford.edu/~valiant/)

huge advances in ML with good performances but we often need an unreasonably large amount of data 

humans learn language in 30Million utterances 
computers need greater than 10 billon word corpus and still not great 

how do we extract as much information as possible from given amount of data? 

very fundmanetal stastics tasks --> starting place for NLP 
* * * 

three different things
- Learning Populations of parameters 
    - can a large number of data sources compensate for little data from each source 
    - heterogenity of each data 
    - do some people have higher propability of male or female children 
    two types of articles 
        - game theoretic approach -> want to pass as many genes as possible, will having a girl or boy have a higher chance to pass on genes 
        - difference in shape of weight in sperm for women and men change how sperm swim and this determines 
    - we just want some stastics, but this is hard because each person provides a little data 
    - broader motivation 
        - consists of large heteregouns data sources each with different models 

        look at the following model 
            - n people, ith person has coin with bias p_i 
            - we observe k indepdent toses of each coin 
            - the empire estimatte for each p_i is unrealiable, error = 1 / sqrt(k)

Steins paradox 
- shrinking back towards the mean 

we actualy want a distribution of probabilites which approxiametes the true probability in the distribution 

- we do not care about a specific person, we care about the set or distribution
- make a distance between the two sets or wassestrein distance 

estimate average of probabilties --> get the low odrer movements and then find a distribution where the moments match

part 2 - estimating learnability 
- some distribution of labeled examples 
- data with labels essentially 

we have too few examples to generalize 

can we tell whether a good model exists 

if we wanted to learn a linear function that maps x to y 
- we want to find a function that minimizes the error 

our goal: is not to find the function, we do not have the data to do that 
- instead estimate what the error of the best function would be 

the best function explains 80% of the variance in y 

is that easy then finding the best thing? 

applications: 
- in some settings this is all we want to do 
- predict diabetes risk based on your genome 
- we do not actually want to know the model but how could of a model we can 

estimate value of data before collecting it 
- we collect some data --> see how good it could be 
- then we decide if we want to collect more data 

- the general answer is yes 

example with linear regression 
- sample proof of this, gonna need to read the paper 

what can we say about the unseen part of the distribution 
- ra fisher all the data about the butterflies i have seen so far 
- how many butterflies will i see in the future 

whats the value of collecting more data? 
- how many samples would you need to see to see all of the examples in the distribution 
- learn from the data about what we do not know about the data


inferences are possible with under-sampeled 

dont ask what is the structure of the data 

ask what is the structure of the distribution or phenomen underling the data 