---
title: "Improving Fairness in Machine Learning Systems: What Do Industry Practitioners Need?"
date: 2020-11-26T15:42:48-06:00
draft: false
tags: ['Data Science']
categories: ['Papers']

---

By Kenneth Holsten, [Jennifer Wortman Vaughn](http://www.jennwv.com/), [Hal Daume III](http://users.umiacs.umd.edu/~hal/), [Miroslav Dudik](https://www.microsoft.com/en-us/research/people/mdudik/) and [Hanna Wallach](http://dirichlet.net/)

[Paper Link](https://arxiv.org/pdf/1812.05239.pdf)


## Paper Motivation

There has been a recent surge in research developing tools to mitigate harms of machine learning. For these tools to have an impact they must actually meet industry practitioners needs

## Paper Contribution

The paper outlines commercial teams‘ challenges and needs when developing fairer ML systems.  The authors outline where there is disconnect between the current research and what people actually need. The papers findings come from interviews of 35 practitioners and survey of 267 different practitioners.

## Background

The current tools that are being created for ML practitioners to address challenges with bias are driven by algorithmic methods rather than real world needs. For tools to have an impact they must be driven by a deep understanding of the actual challenges engineers face when developing fairer ML systems. The goal of this work is to identify future opportunities for research and how to make that research align with engineer's actual needs

### Methods

The authors conducted 35 one-on-one interviews with ML engineers across 10 major companies. They then followed up the interview with a survey of 267 engineers to see if their themes generalized

The authors spend a fair chunk of the paper explaining the entire process of how they recruited subjects and how they conducted interviews. I will not replicate all of the information here. The one thing I do want to highlight is how the authors asked questions to understand interviewees ideal state of the world. Once they understood the ideal state of the world they next honed in on the current state of the world. This way of questioning allowed them to find where the most opportunities for improvement are.

**Fairness-aware Data Collection**

The majority of ML research on fairness has focused on algorithms treating the dataset as fixed. Many teams actually have the ability to change their datasets and that can be a fruitful starting point when thinking about fairness.Lots of the people they interviewed stated that they would try to collect more data to tackle fairness problems.Currently interviewees report not much thought is put into which data is ingested. If the data is there, it is going to be ingested. Interviewees express the desire for tools that better facilitate the collection of data in a fair way. Many engineers also specified the role of having a good test set as being important to capture bias. Tools to ensure that test sets covered all populations equally or showed errors in test sets by subgroups would be helpful.

**Challenges due to Blind Spots**

Interviewees highlighted not knowing where they should be looking for bias or which sub groups should be looked at. Lots of interviewees said it would be helpful to have additional support identifying relative sub populations.  Often blind spots are shown after a product has already been deployed and an outsider finds the blind spot. It would be helpful to have tools to help detect these blind spots before deployment. A useful tool could be one that facilitates knowledge and sharing across team or company boundaries.

**Needs for More Proactive Auditing Processes**
Current auditing processes are often reactive after an issue has been raised rather than before a product is deployed. People are not currently rewarded in their companies for addressing issues related to fairness. Fairness is not a priority for them. Fairness needs to be incorporated as part of the regular workflow of model development

One difficulty that came up over and over again is how fairness is so context dependent. This makes it hard to actually take knowledge from other places often. Getting fairness right takes a lot of time and work and in companies that work is not valued.

**Needs for More Holistic Auditing Methods**

Fairness is often a system level property rather than just applicable to one model. In complicated systems it can be much harder to find fairness problems.Fairness can be thought of as monitoring systems for real world harm rather than just monitoring one model for unfairness. This task is much more complicated and much more difficult. Simulation based systems for understanding complex interactions would be helpful.

**Addressing detected Issues**

Even once an issue has been identified it is not always easy to come up with a remedy. What would be the best approach, switching to a different model? or collecting more / different types of data?. For different contexts or different problems the best approach can be quite different. When teams have decided to collect more data, how much more data is sufficient for solving the problem?

**Biases in the Humans in the Loop**

The humans working on developing these models might have biases inherent in themselves that bleed through to the system

### My closing thoughts

This paper highlights so many opportunities to improve fairness practices for machine learning in industry. This is the level where fairness interventions will often make a difference. Writing a research paper about fairness might not actually make any systems more equitable. Creating tools that are easy for people to use that help detect bias and give them solutions to correct that bias will have a large impact. This paper does a great job of providing a huge number of different directions for research.

There is a lot of research about how it can be problematic to intervene in a community without actually understanding the context or the people in that community. To some extent, that is what fairness researchers do. They came up with a solution or a direction that does not actually recognize or help the needs of practitioners. While this type of research is not sexy, it is very important. We can build upon this paper in a way that solves real problems.

If the research community does not work on this and make it open source then some company is going to create tools to do this. IBM is already putting a lot of resources into creating tools around fairness. I would not be surprised if there are start ups that are already working on this. I would much prefer researchers to be working on this and making open source tools than having a company develop it.

One other takeaway from this work is that something that might help practitioners a lot is work that does not fall under the umbrella of research or software engineering. It is much more building communities and knowledge sharing. Taking the research that is already out there and making it more digestible. Creating communities for people to ask questions and connect with others. Often the most powerful thing you can do is not developing something new but making existing information more accessible and facilitating people to talk with each other. This type of work is not well incentivized though.

