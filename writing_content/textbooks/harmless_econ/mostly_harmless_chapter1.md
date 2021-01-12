---
title: "Mostly Harmless Econometrics: Chapters 1 & 2 "
date: 2020-07-15
draft: False
tags: ['Economics']
categories: ['TextBooks']
---

## Four Frequently Asked Questions

The authors begin the book by discussing how to formulate research questions. The explain the path to a research questions if by asking four questions.

1. What is the casual relationship of interest?

    - This is not to say you cannot have purely descriptive research but purely descriptive research is a step towards causal research
    - Causal research lets us answer questions about counterfactual worlds. A World in which something different has happened
    - Casual questions can be asked about any unit of observations. Individuals, schools, firms or even countries.

2. What experiment could ideally be used to capture the causal effect of interest?
    - Ideal experiments are almost always hypothetical. While we will not be able to carry them out they help us pick research topics
    - A research question that cannot be answered by an experiment is FUQ'd, fundamentally unidentified questions.
    - Here is an example of a FUQ'd question: Would kids be better off starting school later?
        - We could randomly select some kids to start at age 6 and some to start at age 5. We then would test the kids when they are in second grade.
            - But the 6 year olds will be older in second grade then the 5 year olds.
            - But if we tested them at the same age then the kids who started school earlier will have been in school for longer
        - There is no way to disentangle the start-age effect and the time-in-school effect

> If you cannot devise an experiment that answers your question in a world where anything goes, then the odds of generating useful results with a modest budget and non-experimental survey data seem pretty slim


3. What is your identification strategy?
    - an **identification strategy** is how a researcher uses observational data to approximate a real experiment

4. What is your mode of statistical inference?
    - The answer to the above questions contains the following information
        - What is the population to be studied?
        - What sample are we using?
        - What assumptions are made when constructing standard errors?

### The Experiment Ideal

The most **credible** and **influential** research designs use random assignment

Imagine trying to answer the following question : Do hospitals make people healthier?

- We are studying a poor elderly population. Some percentage of people in the hospital waiting room are admitted and some are not. We can compare these two groups.

- The authors collected data for this example and show that people who spent time in the hospital where sicker than those who did not spend time at the hospital.

- On face value this data could be used to suggest that hospitals make people sicker.

- But this comparison should not be taken at face value: people who go to hospitals are less healthy to begin with

- Lets formalize this with some math. hospital treatment is a binary variable {0, 1}. We are interested if health status is impacted by this variable.

- For each person there are two potential health values. One if they went to hospital and one if they do not. Ideally we would measure the difference in health values between these two values. But we cannot observe both of these outcomes, we can only see one of them.

- Because we cannot see both for one individual we must learn by comparing the average health of those who were and those were not hospitalized
- The difference between those who were hospitalized and those who were not contains selection bias. Since the sick are more likely to seek treatment those who were hospitalized will have worse starting health.

Random assignment solves this **selection** problem The group a person is assigned to is not connected to their starting condition.


Randomized trials are not problem free, but they do avoid this problem of selection. Here is one question we will still want to ask about randomized trails:
    - Does the randomization successfully balance the subject's characteristics across different treatment groups? We can compare covariates across groups to check this.

Randomized experiments can be quite costly though so we will often try to answer questions without them. We try to find natural experiments that mimic a randomized trail.

* * *

Regression is a useful tool for the study of causal questions.
- We will often need to control for other factors impacts in our regression
- For example: We often used conditional random assignment rather than pure random assignment
    - We might do random assignment within a school but then we will need to control for differences between schools

## Thoughts

- I love the way this book starts and the focus on how to get a research question. So often we are too focused on niche techniques and algorithms that we forget the core questions we need to ask at the beginning.

- The chapter does a really good job of using examples to highlight certain points.
