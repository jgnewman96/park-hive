---
title: "Building Models and the Scientific Method"
date: 2019-12-21T17:18:01-06:00
draft: False
tags: ['Machine Learning' , 'Reflections']
categories: ['Industry' , 'Research']
---

In the past year there has been a large focus on what is wrong with the fields of Artificial Intelligence and Machine Learning. Coverage has focused on limitations of current deep learning and machine learning systems. Pieces have highlighted the dangers of implementing systems without understanding their implications or who they are going to impact. These pieces have highlighted areas where these fields need to grow. Machine Learning is still a relatively young field that needs to grow and learn. This piece is going to be a personal reflection on my experience in the field and some of the structural problems that I have not heard people talk about before. I will end the piece with some concrete recommendations about how Data Scientists can change their workflow which I believe will lead to better outcomes.

If you talk to Data Scientists or ML Engineers you might hear them talk about the different models they are building. They are building models to recommend movies you might like. They are building a new model that will tell you what type of wine you will enjoy. Building a model is a term that has come to be applied every where. But what does it actually mean to build a model? Does it just involve building a system that makes accurate predictions? From my experience in the field, practitioners have defined building a model as creating a system that can accomplish some task on its own. Building a model should be focused on gaining a greater understanding rather than building a system.

* * *

At times during my short lived career as a Data Scientist I have struggled to be engaged with what I am working on. I have struggled to feel like what I am doing matters. It feels like I am going through the motions rather than  critically thinking. This is an issue that I brought upon myself rather than something inherent of my jobs. But, it is an issue that is exacerbated by current practices in the field of data science.

I was / am attracted to the field of Machine Learning because it helps me better understand the nature of intelligence. Studying what makes an intelligent system and how to build intelligence are problems that motivate and inspire me. They are questions that force me to reflect on my own intelligence and life in the world around me. My introduction to the field was doing academic research during undergrad. We were regularly grappling with these questions; What is intelligence and how is it represented? Since I began working in industry my day to day can feel far away from these basic questions.

My experience of being a data scientist at a corporation has been quite different from doing academic research. While this was to be expected, and there are parts about this that are important, losing sight of these basic questions can be dangerous. Being a data scientist in industry can be limited to taking a known algorithm and just throwing data at it. It is about achieving a high accuracy rather than understanding mechanisms. I was solely focused on building a system that accomplishes a task by putting data into a random forest and maximizing accuracy. Will including these features make our model more accurate? What if I change some of the hyper parameters? I was focused on improving accuracy and had lost sight of what it meant to build a model.

Building a model should not mean putting data into an existing algorithm and hoping it has high accuracy. Model building should be a process of trying to understand mechanisms and how they drive outcomes. I was re-introduced to this direction through bayesian modeling and specifically the work of [Andrew Gelman](https://mc-stan.org/users/documentation/case-studies/golf.html). Building a model that helps you understand the world is a much more helpful direction than focusing on accuracy.

A model that helps you understand the world will be more valuable than a model that can accomplish a task. While automating tasks can save money in the short run, current approaches can miss the larger picture. Rarely do we solely care about the outcome of a specific task. What we actually care about is a larger question, which are specified task is only one part of.

If we are building a system to predict house prices, our end goal is normally not to just accurately predict house prices. We want to understand what are the factors that drive house prices. Why does one house cost more than another? Why do some houses in different regions cost more? What does differential house prices tell us about human preferences? Can we use this tool to make more affordable housing?

If we are building a system to recommend vacation destinations what is our actual end goal? It is not to just predict destinations but provide a meaningful service to customers. We want to make it easier for people to find vacations that they will enjoy. We should not focus on achieving a high prediction accuracy but on understanding why do people enjoy certain vacations? Why do different people enjoy different types of vacations? Why would a vacation to Iceland be enjoyable during one time of the year but terrible during another time of the year?

Our desired outcome is rarely accomplished by automating a task. What we care about is making decisions and understanding how different decisions lead to different outcomes.

* * *

So why is data science as a field struggling? Why is it focusing on the short term and the narrow rather than a greater understanding. There is a beautiful simplicity in optimizing a metric. Defining success in terms of error/accuracy leads us to forget about the larger picture. Practitioners need a better work flow that keeps the larger systems and questions in mind.

Data science as a field is missing the scientific method. Rather than forming hypothesis and then testing them, data scientists often just dive in head first. We have identified a task we want to solve and we write some code to create an automated solution. The scientific method though, provides a workflow that keeps the larger picture in mind. It forces us to form a theory about what the underlying mechanisms are and then test them out. The scientific method forces us to build a model. Only with this model can we understand the driving forces.

Lets return back to our example of predicting housing prices. Rather than taking a lot of data and putting it into an existing algorithm, lets imagine a different workflow. Without even seeing the data, lets form a hypothesis. We believe that houses in good school districts will cost more than similar houses in worse school districts. Now that we have a hypothesis about what drives housing prices we can test that hypothesis. If we find it to be true, we will have a better understanding of what drives housing prices. Even if it is false, we have gained more information about driving mechanisms. We will now have on record that a certain hypothesis is false and can test out a new one.

Data Science as a field is still young and evolving. We see the promise and potential of automating a task and forget to be systematic thinkers. We forget the larger goals and focus on one metric. There is a metric we can measure, so we optimize it. Using the scientific method forces us to build a model of the world. We have to form hypothesis and then test them out.


* * *

So what would a different workflow look like? Rather than just directly working with data lets begin by forming some hypothesis. We write down these hypothesis so that we can keep track of them. A great way to form hypothesis is by talking to subject matter experts. If we are creating a vacation destination model, lets talk to some travel agents.

Once we have our hypothesis lets test them out. After testing a couple of hypothesis, we use those results to form new ones. We will have a record of our different theories and whether or not they were correct. When we begin to automate our task we are no longer focused on optimizing accuracy but rather have an understanding of a system.

It is harder to measure how much of a system we understand than accuracy on a defined task. Our goal should be understanding of a system rather than optimizing a certain metric. Model building should be a process of using the scientific method to better understand the driving forces in the world around us.

----


