---
title: "150 Succesful Machine Learning Models: 6 Lessons Learned at Booking.com"
date: 2020-05-18T16:21:18-05:00
draft: False
tags: ['Machine Learning', 'Software Engineering']
categories: ['Papers']
---

[By Lucas Bernardi, Tehmis Mavridis, Pablo Estevez](https://dl.acm.org/doi/10.1145/3292500.3330744)

## Summary

This paper from Booking is not focused on algorithmic advances but on how the company has derived value from using Machine Learning. The authors argue that more papers similar to this one need to be published.

The authors highlight some parts of the Machine Learning process that are specific to booking. They do this to explain why there situation is different then other technology firms.
    - At Booking a bad recommendation is quite costly. A bad trip is much worse than recommending a bad song or television show
    - They have minimal support for a lot of tasks. Guests travel quite infrequently and past history is not always relevant

Part of the paper is exploring how we quantify the impact models are having on the business. Does high model accuracy automatically mean high business impact?

The authors provide a different lesson for each stage of the machine learning process: Inception, Modeling, Deployment, Monitoring, and Evaluation.

*Inception*

The authors broadly define machine learning models as tools to help you learn from your user base. This tool could be very specific such as optimizing the size of a layout. It could also be very broad and abstract such as understanding how flexible a user is about their trip.

The authors divide models into the following categories:

- traveler preference models: how flexible are you about aspects of your travel
- traveller context models; what is the theme of the trip, who are they going with, why are they going, what is the purpose of the trip
- item space navigation models; take in data about user interactions, clicks, scrolling, etc and then try to show most relevant items
- user interface optimization models: what the user interface should look like
- content curation: what format should content come in: free text, images
- content augmentation: augment that content with context, example: how good of a value is this, what is the price trend on this


*Modeling*

The authors propose estimating model business value using RCTs. We can compare key metrics such as conversion, customer service tickers or cancellations. The authors find that there is not necessarily a correlation between offline performance and increased business value. This means a more accurate model does not always mean a better business.

The authors propose the following explanations:
- value performance saturation: gains in accuracy do not actually mean business gains after a certain point
- uncanny valley effect: if a model is too accurate and predicts what a user can do it turns a user off
- proxy over-optimization: optimizes a proxy and not the real thing. driving clicks instead of conversions.


A key part of successful machine learning is being thought about how we set up the problem. There are multiple different set ups for the same problem. Whenever the team is starting to think about building a model they look at the following things

- learning difficulty: How well does a very simple baseline approach do. Prefer problems where baseline approach does a lot better than random
- data to concept match: how well does out data match what we are modeling
- selection bias: is our data biased because of the way we are getting it

*Deployment*

The authors note that throughout Booking latency increase conversion. Machine learning models take time and therefore decrease latency. The authors want to minimize how much they are increasing latency so they suggest using models that are sparse with fewer parameters. They also suggest minimizing feature transformations.

*Monitoring*

When models are in production it is critical to monitor the performance to assess if model drift is happening. Monitoring of models is hard for the following reasons

- incomplete feedback: we do not know always know the true labels, we just see the predictions
- delayed feedback:  we will sometimes not see the true label until much later

The authors suggest using response distribution analysis for monitoring. response distribution analysis involves inspecting a histogram of model predictions. We can use the following heuristics.

- A good discriminatory model has peak at 1 and peak at 0
- A bad model is unimodel with a center in the middle
- predicting one value a ton more than everything else might be bad.
- very noisy and non smooth distributions are a problem.
- differences in distribution between the training data and the predictions in product might be an indicator of drift

response distribution analysis is connivent because it can be applied to any classifier. It is robust to class distribution and addresses both incomplete and delayed feedback.

*Evaluation*

As mentioned earlier the authors use RCTs to evaluate their models. They use use three groups rather than the traditional treated and not treated There is control group C that experiences no change,  There are two treatment groups. Both invoke the model but only in T1 do users see the change.

This approach has two benefits. It allows us to isolate the impact of the decrease in latency and the impact of the model. It also gets rid of problems with eligibility criteria because some set of users will never even be eligible for the model.


## Thoughts

Overall this paper did not provide anything ground breaking but it did provide good context and insight into how a company is using Machine Learning. It is nice to see a paper from Booking. Most of the papers that come out of Industry are coming from very large organizations that do a lot of research like Google, Facebook or Amazon. This paper gives more insight into how a smaller company that is not as cutting edge is using ML.

Academic papers can often be so divorced from actual reality that in can be difficult to see the real impact that they have. It is important for academia to do research that does not have an immediate tangible impact, but it is also important to have research on how people are using these tools. Academia would undoubtedly benefit in some places with a tighter feedback loop with actual implementation. Is the research that academia is doing mattering and how are people using it? One of the highlights from this paper is that latency matters a lot. This might suggest more research should be focused on decreasing latency and making smaller models rather than continuing to make larger and larger models.

Industry on the flip side can also learn a lot from academia. Not every project needs to have a tangible business impact than can be seen immediately after the research is done. It is important to work on some projects that do not have an immediate use case. It is important to pursue things because they interest you sometimes rather than because it is good for the business.
