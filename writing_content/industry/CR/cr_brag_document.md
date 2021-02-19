---
title: "Change Research Brag Document"
date: 2021-02-15
tags: ['reflection', 'resource']
categories: ['Industry']
---

I recently left Change Research where I worked for over a year to start a new job. During my time at Change Research (CR) I worked on a ton of different projects. Because the team was so small I had a ton of responsibility and the work I did mattered a lot to the companies' success. If I did not do something then it was not going to get done. I could push for us to prioritize the things that I thought were important. 

I am really proud of a lot of the work that I did at CR and I grew a lot as an engineer and a researcher there. After leaving CR though it is easy to feel distant from the work I and as if it does not matter anymore. I am not still working on those projects, there is no tangible product that I can interact with anymore. People outside of CR do not know about how hard I worked or the real progress that we made while I was there. 

One of my favorite tech writers, Julia Evans, has this idea of a [brag document](https://jvns.ca/blog/brag-documents/). A brag document is a document that lists all of the things that you worked on during a given interval. All the ways that you impacted the company or your co-workers. Writing a brag document provides an opportunity for you to reflect and find common themes in your work. 

## Overall Accomplishments 

Down below are all the projects that I worked on during my time at CR and all the engineering and data science work that I did. I am a strong believer that the way to have a large impact is not through IC work but how you impact those around you and the influence you have on the company. My largest accomplishments at CR are related to this and how I tried to push the company to be better in certain ways. 

#### Pushing us to have a clearer product vision

During my time at CR I was pushing for the company to have a more clear product vision. At many times it felt like our product vision would change quite rapidly and that we did not have clear goals of where we wanted the product to go overall. During my time I pushed for a more formalized product discovery process involving end users and a more defined planning process to scope out the work we wanted to do. 

#### Helping us think more clearly about data

I helped advance the way CR thought about data. One way this manifested was helping us change our database structure to make certain use cases a lot easier. I also worked to help us redefine how we think about poll accuracy and error. I helped us figure out how to combine data across multiple polls. 

#### Focusing on the ways we work together

During my time at CR I pushed the engineering team on a lot of ways that we collaborated. I got us to have design documents and design reviews. I pushed us to start using github issues to track our work. I helped figure out the integration with our first product manager and I also started the process of the company doing retrospectives.  

## Projects 

#### Pricing model

The first project I worked on at CR was developing our pricing model. When a client was interested in running a poll with us we had to give them a quote of how much it was going to cost. Fielding polls actually had quite variable costs based on where they were, when they were and how quickly they had to be fielded. I built a bayesian model using [pymc3](https://docs.pymc.io/) to estimate how much collecting a poll was going to cost us. 

#### Multi Poll Question Modeling

At CR we run polls for many different campaigns and organizations. There are some questions which appear on many different polls. "Which presidential candidate are you going to vote for?" is an example of one of these. Rather than each poll being a unit we can actually combine all of the raw data from the different polls. I built out our methodology to do this and actually proved that it is more accurate using the 2020  [presidential election](https://changeresearch.com/post/2020-presidential-model/). I used [pyro](https://pyro.ai/) to do this and built a pretty simple bayesian neural net. 

#### Weighting
Surveys that are not representative undergo a weighting to make them representative of the population. There are many different ways to do this post-stratification weighting. I built Change Research's weighting algorithm from scratch following this [paper](/#/post/opt_surv_weights). Change Research had a previous methodology before I re-wrote it, but it was very old, was slow and had limited functionality. 

Re-writing the weighting algorithm allowed us to deprecate a lot of code and also built an improved front end that made weighting a much better experience for users. It also allowed us to take on other projects in the future that would not have been possible with our old code base. 

I did all of the project management for this project. I built out the POC without anyone asking and then validated that it would be a huge help. I wrote all of the code and then the tested it out with end users. I iterated and drove adoption with end users by providing them with new functionality that the old algorithm did not provide. 

#### Automating Survey Fielding

I worked to automate the most time intensive process of fielding a poll at CR. Change Research collects samples for their polls through online advertising. I designed and built out a way to automate this process. By observing which people are responding to a survey and knowing what a representative sample looks like, we could adjust our ad spend to get a representative sample at a cost point we were happy with. I built a multi armed bandit approach to this process. 

#### Database Redesign
When I joined CR they had one MYSQL database that was both the production and the analytics database. This caused a number of problems and the MYSQL db made a lot of analytical tasks very slow. I helped CR migrate from one database to having a production Redis NOSQL DB and then an analytics database in Bigquery. I also helped design the database schemas to make analytics use cases as straightforward and easy as possible. 
