---
title: "Voter Registration Databases and MRP"
date: 2020-01-07T08:00:07-08:00
draft: false
tags: ['Statistics']
categories: ['Papers']
---

## Summary

The authors outline that due to decreasing performance of phone polls new approaches to political polling are becoming prominent. These new methods of getting survey responses do not get perfectly random samples. The authors argue we can use new statistical methods to make accurate inference without random samples.

The authors lay out the following work flow:

1. Draw a survey sample directly from the voter database or matching responses from an already existing survey to the database
2. Use auxiliary data from the database to construct a flexible statistical model on the quantity (or quantities) of interest
3. Project inferences from the statistical model to the full target population on an individual level
4. Use the projected individual-level inferences, which can be seen as a pseudo-survey dataset, to construct larger group-level inferences about either the electorate as a whole or subgroups within the electorate.

The authors outline this with an example of creating a model for predicting 2012 Presidential Vote. They use a logistic regression model to predict vote for either Obama or Romney. The response variable comes from the survey data and all of the predictive variables come from the voter file data. They use some individual level variables such as gender and race. They interact all of the different variables with each other. They also use geographic level information about where an individual lives.

Once the authors have fit their individual model, they do post-stratification to ensure in each state the correct number of votes were assigned to each candidate. After doing this post stratification the authors then look at different aggregations of the data to examine trends in voting.

The authors end the paper by discussing different limitations and further opportunities for research. I will touch on a lot of these below.

## Thoughts

- The authors were able to use actual voting results to do post stratification on their model. They talk about how if you were doing pre-election modeling that would not be possible and you might get more biased results. In a lot of ways they picked an example that would work out very nicely. If we are building a model for 2020 vote, we would not be able to do post stratification. We would need to get a better sense of how much this post stratification changes the results. We could test out our model with a variable we do know the answer for to help understand this better.

- In the paper the authors only use one variable from the survey, the variable of interest, and then all other variables are in the voter database. But what if we wanted to use dependent variables from the survey. Imagine we asked a question about what is your primary news source and then wanted to use that. We would have to first create a model for news source and model that onto the voter file data. How would we propagate the uncertainty from that model into the model for vote? We also would probably have to make a model for turnout. The question boils down to how do we combine multiple different models?

- In the paper the authors mention that there is a limitation of their matching algorithm not being perfect. They also mention that some of the variables in the voter file are modeled. To start with we would want to use the existing infrastructure of matching and the model data. Eventually it could make sense to make models of these ourselves. This could be really beneficial if we find a way to combine models that is elegant and combines uncertainty.

- In the paper they report their results, but do not really explain how they reached their selection of dependent variables. They absolutely tried out multiple models with different dependent variables. It would be great to know what other models they tried out and what their performance was. It is a shame that academic papers generally only report the results of the final model. It would be interesting to see how much of a degradation there was in accuracy if they removed one of their variables. Predicting presidential vote is one of the easier things to predict, could they have reached a model of similar accuracy with a lot fewer variables?

- In this paper they just modeled one variable, which was a binary value. If we wanted to model two variables would it be more beneficial to make two different models. It might make more sense to have one model that jointly predicts both. I would lean towards the latter making more sense.

- In the paper they called out the fact that they did not consider how the survey data had come from different time periods. Do we weight data from three months ago less than data more recently? How do we do that? Would the model be substantially different if we trained it on data from different time periods. Could we use that to see how opinions have changed?

- Catalist seems like they do really good work. The paper that looks at the accuracy of their modeled variables is nice. It could be nice to work with them.

