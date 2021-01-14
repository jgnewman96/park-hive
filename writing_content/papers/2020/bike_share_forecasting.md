---
title: "Towards Fine-grained Flow Forecasting: A Graph Attention Approach for Bike Sharing Systems"
date: 2020-09-24T16:02:40-07:00
draft: False
tags: ['transportation policy', 'Deep Learning']
categories: ['Papers']
---

[By Suining He and Kang Shin](https://dl.acm.org/doi/abs/10.1145/3366423.3380097)


## Paper Motivation

Accurate bike-flow prediction at the station level is important for a bike sharing service's success. Existing methods are not successful at predicting fine-grained bike flow.

## Paper Contribution

The authors remedy this problem by proposing a spatiotemporal graph attention CNN for station-level flow prediction. Each bike station is a node and bike rides are edges on a graph. Their network captures differing station-to-station correlations. The new methods improvement in accuracy is shown using data from New York City, Chicago and Los Angeles

## Background

Bike sharing has recently been rolled out in many urban communities across the country. 35 million bike-share trips were taken in the US in 2017 and that number continues to grow.Predicting the number of pick-ups / drop-offs at each station is critical to creating a satisfactory bike sharing service. This allows better allocation of bikes to stations, decisions about when to build new stations and station re-location decisions to be made. Predicting bike-flow traffic is difficult for the following reasons

1. There is a very large number of bike stations that are often quite close together. It is difficult to accurately predict flows at the station level rather than at some higher cluster of stations.
2. Bikes are more likely to be picked up at stations with high supply and so the decisions of the bike authority directly impact the flows. There is not a universal flow but rather the flow is responsive to the conditions of the network.

## Problem, Data & Framework

A bike sharing system has N stations. Each station i has a location (lat_i, long_i). Each trip a user makes from one station to another is an edge in our graph. Bike stations are neighbors if there are trips between them. For each station we have the number of people who end a trip there and the number of people who start a trip there. We can divide this up into different time periods. We will also feed into our model other external factors (weather for example).

Given all of the flows from time period 1 to time period k, we want to predict the flows at time period k + 1

Three Data Sets are used in the paper:

- NYC (Citi Bike) - 502 stations, ~ 8 million trips in second half of 2015 through first half of 2016
- Chicago (Divvy) - 607 stations, ~ 3 million trips in the second half of 2018
- LA (Metro Bike) - 135 stations ~ 0.5 million trips in second half of 2017 to first half of 2018

## Model features
- station-to-station distances: A station's usage is correlated with the stations around it. The further stations are from each other the less correlated their usage is.
- Levels of Temporal Closeness: how closely two stations mirror each other depends on that time interval you look at. Some stations are similar on small time scales and some are similar on large time scales
- Points of InterestThe authors incorporate information about the city through points of interest. POIs are categorized into five groups commercial, residential, recreational, cultural and governmental. A station is then classified into one of those groups based on the majority type of nearby POIs.
- Weather data (7 types of conditions, temperature, sky visibility, wind speed, humidity) [^1]

## Model Architecture and Results

The authors go into a lot more detail about their model architecture and results. Their model achieves a higher accuracy defined by RMSE then a lot of comparable methods. They also do a sensitivity analysis show how their model performance degrades if you take certain pieces away.

## My Closing Thoughts
I struggled with this paper a lot! Like a lot! My main struggles with it come from me having been in industry recently rather than academia. I can understand why this is a satisfactory academic paper, but there are so many questions I wish the authors had addressed! Just a few are:

- What does RMSE actually mean in this context. How can we think about the normative impacts of 1 point decrease in RMSE?
- How easy is this approach to implement? Could other cities easily implement it?
- All of the training and evaluation was done offline. How hard would it be to set up this model to make real time predictions? How would we use these real time predictions?

The authors focused a lot of the paper on temporal impacts / structures. It is very interesting to see all the different ways time can be framed and how it can have an impact. I would have liked to see more discussion of time outside of just model implementation. Does predicting bike flow at the hour level matter? Why is hour level prediction more important than day level prediction? Why does our time interval matter when thinking about flow? How is a 15 minute time interval different from a 30 minute time interval?

I would have loved to see more details on the authors process. I know academic papers are short and you can only include so much. But what were the first things they tried? What did they try that did not work? How did they come up with hypothesis for how to improve their model. If what we care about is actually getting this model implemented in other places, that type of information would be really helpful. The authors had to use different hyper parameter values for the different cities. How do we think about these hyper parameters, what do they represent and how do different values mean different things for different cities?


This paper created a new methodology for solving a very difficult problem. Clearly the researchers spent a lot of time working on this problem and finding an approach that will be successful. In it is current state, I have a hard time seeing this research have a tangible impact on bike share. And maybe thats not the goal of these researchers or where their comparative advantage lies. Maybe their time is better spent developing another methodology for a different problem. I would love to see someone driving this work further and answer some of the questions I proposed above!

[^1]: There is no chance that all of these weather conditions matter. Why use all of them.
