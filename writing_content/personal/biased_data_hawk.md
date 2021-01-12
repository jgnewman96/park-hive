---
title: "How do you Solve for Biased Data?"
date: 2019-10-25T16:44:33-07:00
draft: false
tags: ['Machine Learning']
categories: ['Personal']
---

My friend Hawkins recently sent me the following question:

> How do you work around biased data sets to produce non discriminatory results in ML?

I ended up writing him a fair amount while I wan on a plane. My response to him is replicated here in full.

* * *

Hey Hawk,

Thanks for asking this question. It is a really important one and it is always nice to think about these problems in a fair amount of depth. While I would not say there is a silver bullet for solving this problem I will try and talk through a couple of different approaches and some examples.

In the end we are always somewhat constrained by our data. It is kind of a cliche but the saying "garbage in, garbage out" rings very true. If your data is garbage then your model is going to be garbage. While that is kind of an extreme statement it applies in smaller places to. If our data is biased in some ways a model fit on that data is going to be biased.

This is a very large concern because as we start automating different processes with Machine Learning or Artificial Intelligence we end up propagating that bias. Lets think of this with an example.

Imagine we built a machine learning model to identify photos of wolves and dogs. We can think of this as a pretty simple task: wolves and dogs have some serious differences. We train a model and have a very high success rate. We then put our actual model into production and after about three months, we realize our model is starting to make a ton of errors. Why was our model good in our training set, good for three months and then all of a sudden started failing? It is because our data was biased. In the orginal data all the photos of wolves had snow in them. Rather than learning to actually identify wolves vs dogs. Our classifer learned to identify either snow or no snow.

Another couple of examples can help us see how biased data can affect us in other ways. Imagine we want to know who is going to win the next democratic primary. We create a online survey that asks people who they are going to vote for. This data set is going to be biased. What we care about is how the population is going to vote, but we only have information about people who use the internet. We know that there are people in the population who do not go on the internet and any information we would gain from our survey would not take those people into account.

One more example of bias for you. Imagine we want to predict who is most likely to commit a crime. We use a bunch of data about prior arrests. This data is going to be biased in so so so many different ways. We can imagine it is going to predict certain races are going to commit more crimes.

This propogation of bias is a huge issue when we start to work on automating different processes. Bias can show up in many different ways and impact outputs. I am going to talk about a couple of different ways I think about combating bias using the examples above.

One last thing to note though. It is only possible to work on combating these biases if we know they exist. If they are in our data but we do not know they exist, then we will not be able to combat them. This is why having models that are explanaible is so so important. When a model is explainable we can understand why it is making a decision and then we can recognize when it is biased. If the model is truly a black box, it is much more difficult to identify if it is biased and especially how it is biased.

* * *

There is a quote from statisican George Box that I have been thinking about a lot of late.

> All models are wrong, some are useful

This quote is so powerful to me because it calls out exactly what models are. They are a simplification of the real world that makes assumptions. These assumptions are going to be sometimes wrong. The real world is an intensely complex place, and that means models are not going to fully account for that complexity. Even though our model is wrong it can still be useful and represent some part of the truth.

Lets imagine, that we have identified a bias in our data and we want to fix it. We can attempt to correct for a bias by applying additonal structure to our model. This means we are applying outside knowledge that is not contained in our data. This is essentially what we are doing whenever we make a model. We are making assumptions about how the world works and fitting our data into that. All models are making certain assumptions about how data interacts and then using that to do something that is hopefully useful.

In the example where we only survey people who are online, we can then use some structure to adjust our model. We know that people who are online are systematically different from those who are not online. We can look at those differences and understand how those differences correspond to their voting preferences. We can then re-calibrate our model to take into account these differences and predict for the general population rather than just internet users. This approach will not be perfect, but it should be better and get rid of some of the bias.

Essentially, when our data is biased we add some additional structure to our model based on how we understand our data to be biased. Often this is in conjecture with getting some additional data which gives us a sense of how exactly it is biased. So we are combining our intuition of how the data is structured with both knowledge of the true problem we are trying to solve and some additional data. For example in this case we would be get census data about the entire population. This would allow us to see how our sample of internet users is different from the general population.

* * *

Another tactic that I personally appreciate a lot is incoporating more uncertainity into our models. We should be building models that are transparent about their uncertainity and can convey their uncertainity. When a model is not going to be able to perform well because of bias it should communicate that. It gives us a better idea of where our model is going to be accurate and where it is just grasping at straws.

There is a concept that is very commonly discussed in economics but almost never talked about with regard to ML that is really important here. The term is *external validity*.

Here is how external validity is used in economics and how I think it applies to Machine Learning. Imagine you run an experiment on college students. We would question the external validity of that experiment because does something that holds true for college students, hold true for elderly people? Essentially it helps us think about what is the scope of our findings. Where do our findings succesfully apply and where do they not?

Here is how I think this could be applied to Machine Learning. Imagine you train an face recognition system that can recognize faces of people on the street from cameras. But in your training data set you never included any days when it was raining. Your model still works, but it has problems with external validity. It most likely will not work well for times when it is raining outside.

Taking this vocubulary of external validity and applying it to machine learning would be a very helpful practice.

* * *

I know I kind of went on a couple of different tangents, but what you are asking about is really a core problem of applying Machine Learning and Artificial Intelligence. I think here are a couple of the takeways that are important.

* It is dire that we have models that are interpertable and explainable. Without this we will have very little understanding if our models are biased or how our models are biased.

* All of modeling is using assumptions about the structure of the world to leverage data in a meanigful way. We can implement certain structures or assumptions to help us work with bias data.

* Incorporating uncertainity into our models and transparency of that uncertainity should be a necessity. This allows us to better understand where our models are accurate and where they are not.

* Implementing Machine Learning has the very real implication of propogating bias. If we do not want to incorporate bias into our systems we have to be constantly testing to see if bias does exist and if so how we can mitigate it.

I hope this is helpful. Let me know if it answers your question or if you have any follow ups.
