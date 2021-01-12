---
title: "ML Flow: Platform for Complete Machine Learning Life Cycle"
date: 2019-10-29T13:53:00-07:00
draft: false
tags: ['Machine Learning']
categories: ['Talks']
---
Talk given by [Jules Damji](https://www.linkedin.com/in/dmatrix/):
git hub [repo](https://github.com/dmatrix/spark-saturday/tree/master/tutorials/mlflow/src/python)

## Motivation

Machine learning development is complex. This is not due to the underlying theory but rather all of the different stages in development. Each stage has its own requirements and goals. We have developed tools and best practices for this for traditional software development, but not Machine Learning.

Here are the differences between traditional software and machine learning

Traditional Software:

- Meet a functional specification
- Quality depends on the code
- One software stack

Machine Learning

- Optimize a metric (accuracy)
- Constantly experiment to improve it
- Quality depends on input data and parameters
- Compare and combine many libraries models & algorithms

## What is ML development

ML Development follows the below life cycle:

Raw Data --> Data Prep --> Training --> Deploy, Repeat

Each of these stages has its own tools and its own work environment. This difficulty manifests itself in different ways.

1. Tracking Parameters: If you just want to track one thing this is easy. But as the number of things we want to track grows this problem explodes.
2. Scale: Often the scale of the problem we are working on is very large and we need something that is still efficient and quick
3. Model Exchange: How do you give a model that you developed to someone else and make sure they have all the necessary information?
4. Governance: How do we track the a model is doing what we want it to and that it is being used properly?

Large industry leading companies have built custom machine learning problems to solve these problems:

- Facebook: [FBLearner](https://engineering.fb.com/core-data/introducing-fblearner-flow-facebook-s-ai-backbone/)
- Uber: [Michelangelo](https://eng.uber.com/michelangelo/)
- AirBnb: [BigHead](https://databricks.com/session/bighead-airbnbs-end-to-end-machine-learning-platform)
- Google: [TFX](https://www.tensorflow.org/tfx)

## Introduction to Mlflow

But these platforms are tied to companies infrastructure and limited to a subset of algorithms. If you do not work at one of these companies you are out of luck.

[Mlflow](https://mlflow.org/) is a tool built by DataBricks designed to provide similar benefits in an open manner that anyone can use. Mlflow was designed with the following design principles:

1. Modular Design: You do not have to use all of it and you are not locked in. It is made up of distinct components and you can use what you want.
2. Design is API first
    - APIs are very intuitive to developers and allow them to construct immensely powerful things.

## Components of Mlflow

There are currently four different components of Mlflow. They are listed out below with details about each one of them.

### 1. Mlflow Tracking

 A simple API that allows the developer to track different things during their ML development.It provides both an API for your code and UI to visualize what you are tracking. It allows you to track all of the following things

- parameters: inputs to your code
- metrics: measurements of performance
- tags and notes: extra information
- artifacts: files, data and models
- source: what code ran?
- version

### 2. Mlflow Projects

Mlflow projects provides a packing format that makes it reproducible to run a model on any platform. It is essentially a directory that has code, configuration, dependencies and data. We can run our models either remotely or locally. We use a yaml file to specify all of the necessary information.

### 3. Mlflow Models

Mlflow models is a format the supports diverse deployment tools. It creates an abstraction in between model code and deployment tools that can be translated. It allows us to specify a model that then can be deployed in a lot of different ways.
  
### 4. Mlflow Registry

A repository of named, versioned models with tags and comments. This tool allows us to tag different versions of a model and see how a model changes over time. We can track a model through development, staging, production and even retirement. We can easily load a specific version of a model and look at model lineage.

## My Thoughts

First, I love all of this work so much. Mlflow is such a cool tool. I am all behind it. I have not had much experience using it yet but I cannot wait to start using it regularly. I imagine it is going to become an integral part of all of my developments moving forward.

I specifically love how they engage with the open source community and want to get feedback. Jules was constantly asking for feedback and wanting people to contribute to the project. I love building things that are open and transparent. When he gives these talks he is making the tool known to more people and getting feedback at the same time.

There were a couple parts of his talk I did kind of disagree with though. Specifically I sort of disagreed with the whole motivation section and setting up data science as very different from traditional software development. I believe the two are actually a lot more similar then we often say and are doing a disservice by treating them as such distinct things. Software engineering is a much more developed field and we can take a lot of the learnings from it and apply it to data science or machine learning development. I might have to write about this in more length at some point.

One thing that I really want to see is a tool that tracks the exploratory part of the data science life cycle. Ml flow seems to be a tool that is designed only once you have reached a model. But to me that most important part of the life cycle happens before that. How did you decided on the model that you did? What did you find that was interesting in the data? What are the assumptions that you made? In the end tuning parameters or metrics do not help you answer the most important questions.

I talked a little bit about this with Jules after the talk. He suggested having a notebook that tracks this and making it an artifact. He also mentioned using tags and notes. I will be interested to try this out with my next project.

In general, I struggle with hands on tutorials. I find they rarely give you enough time to truly learn on your own. It either should give me like a full half hour to work on implementing something, or should not really have me write any code.
