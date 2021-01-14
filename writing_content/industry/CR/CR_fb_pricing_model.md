---
title: "Change Research: Poll Cost Model"
date: 2020-03-17T13:47:52-05:00
draft: True
tags: ['machine learning']
categories: ['Industry']
---

### Why do we need a Cost Model?

At Change Research we collect responses for our polls through targeted advertisements using Facebook and Instagram. We provide facebook with an advertisement that links to a Survey Monkey survey. These advertisements are then targeting to individuals based on certain criteria we set. For example, if we want a survey in the state of California we tell facebook to only show advertisements to people in California. Facebook charges Change Research to show these advertisements. We continue showing advertisements until we get a large enough sample. After we have achieved that sample, we tell facebook to stop showing ads. The cost of showing these ads on Facebook is how much it costs Change Research to field a poll.

For CR to be successful it is important we have a good understanding of how much it is going to cost us to field a poll. When we provide a price to a client, there are a couple of different things that go into that. The price a client sees is the price of fielding the survey through Facebook advertisements as well as an additional labor cost + profit margin. We provide the price to a client up front, but we do not know how much the survey is going to cost us. Having an accurate estimate of how much the survey is going to cost is essential for Change surveys being affordable and Change thriving as a business.

### Terminology

Before we start talking about the actual Cost Model it will be helpful to establish some terminology

- Impression: When someone is shown a Change Research Ad
- Click: When someone clicks on a Change Research Ad
- Start: If someone actually starts a Change Research Survey
- Weighted: When someone completes enough questions that their response is included in the poll

- Geo Targeting: Target a survey using FB's geographies, (State, County, City, Zip Codes, Congressional District)
- Geo Targeting with Points: Target using a geography that we manually create of circles
- Voterfile / Custom Audience Targeting: Target by providing FB a list of people

## Current Model

The current model that we have to predict FB cost works in the following way:

We assume that for every poll there is an average cost per click. A certain percentage of those clicks then turn into completed responses. We calculate the price of a survey using these two metrics.

            Survey Cost = (sample size / conversion rate) * CPC

*Example*

Survey with Sample Size of n: 800

Average Cost per Click: $0.50

Conversion rate of Clicks to Completes: 0.35

Total Survey Cost = (800 / 0.35) * 0.50 = $1143

The difficulty comes from estimating the average cost per click and the conversation rate of clicks to completes.

The current model does this in the following ways:

Conversion rate is a function of the number of questions in the survey. The more questions in a survey, the lower the conversion rate.

The average cost per click is a function of the following features:

 - size of population targeting
 - region of country we are targeting
 - how we are targeting (zip_codes, congressional_district)
 - ethnicity breakdown of region (%white, %african-american, %hispanic etc..)

## New Model

The new model has a similar overall structure as the old model but with a couple of key differences. Rather than estimating cost per click, the new model estimates cost per start. The other big change is that the new model does not assume an average cost that is constant. Instead we assume that our cost per respondent is increasing. The first respondent we get is our cheapest, the second one the second cheapest and so on.

Our first response is the cheapest because Facebook heavily optimizes who they show advertisements. The first person they show an ad is the person most likely to click. This means the more people who have clicked on the ad, the less likely later people are too click. Because we are getting fewer clicks for every impression we are going to be paying more for each click. Therefore we assume cost per start is a function of the number of people who have started the survey.

Similar to the first model there are also some geographic features that we incorporate. They are the following:

  - Are we using a custom audience?
  - What percentage of the population is white?
  - What percentage of the population is hispanic?
  - Are we targeting a congressional or state legislative district?
  - What is the density of the region?

We explored incorporating the following features but they did not improve the accuracy of the model
  - What region of the country are we targeting?
  - In the region we are targeting, what percentage of people voted in 2018?

## New Model and Uncertainty

The other big difference between the new model and the old model is that the new model incorporates uncertainty. The old model output one predicted price and that was all we got. The new model is built using [pymc3](https://docs.pymc.io/). Rather than just outputting one price it outputs a distribution for price.

Directly modeling this uncertainty is really helpful. Our current model is limited by the set of possible features and variability in facebook's targeting. The same exact surveys run at the same exact time might have different costs. Directly modeling that uncertainty gives us a better sense of the range where cost might be. Because under predicted is worse than over predicted, instead of using the mean / median as an estimate we can use a higher quantile. Using a higher quantile protects us aganist under predicting.




