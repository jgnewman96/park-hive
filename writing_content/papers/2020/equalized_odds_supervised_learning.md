---
title: "Equality of Opportunity in Supervised Learning"
date: 2020-08-28T11:23:08-07:00
draft: False
tags: ['Machine Learning', 'Policy']
categories: ['Papers']
---

### Paper Motivation

Model builders may want to ensure their model is fair with regard to a protected attribute. (E.g. Wanting to make sure our model is not discriminating against people because of their race). Previous research has shown that quantifying a model's fairness is not straight forward. Even if the protected attribute is not an input to the model it is still possible that the model is discriminatory.

### Paper Contribution

The authors present a methodology of adjusting a learned predictor to remove discrimination according to their definition of discrimination. The authors also investigate their measure of discrimination and highlight what it includes and what it is missing. They find that their notion of fairness both gives more actionable information and facilitates training learners that provide more utility. The authors methodological fix is a post-processing step rather than a wholesale change to the entire learning pipeline which can be quite costly

### Background

There is currently a lot of interest in algorithmically measuring and ensuring fairness of machine learning algorithms. There is still however (as of 2016, and 2020 as far as I know!) no vetted methodology for avoiding discrimination in machine learning. The most naive and simple is training the algorithm without the protected attribute. This approach is actually insufficient though because of __redundant encodings__. __redundant encodings__ is when the model effectively learns the protected attribute through other features in the dataset.

Another definition of fairness is __demographic parity__. __demographic parity__ means the decision of the classifier is independent of the protected attribute. Training classifiers that satisfy __demographic parity__ is flawed in two ways according to the authors.
1. It does not ensure fairness.
2. It also may cripple the utility we hope to achieve

The paper assumes the following problem setting. We have a target Y that we are trying to predict using available features X and a protected attribute A

### Fairness Definition
**equalized odds**: A predictor satisfies equalized odds with respect to a protected attribute if the predictor and the attribute are independent conditional on the outcome
- Our predictor can depend on the protected attribute but only through the actual outcomes.
- We must have equal true positive rates and false positive rates across classes in our protected attribute
- This definition punishes classifiers which only perform well for certain groups of the protected attribute

**equal opportunity** is a relaxed notion of equalized odds using the idea of a preferred outcome. If there is a preferred outcome, (getting a loan), then we only require parity for the preferred outcome.
- This is a weaker definition then equalized odds but still an interesting one because it allows for a more accurate model

**oblivious**: A measure is oblivious if it only depends on the joint distribution of the true outcome Y the protected attribute A and the classifier
    - An oblivious measure narrows the scope of different things to focus on when dealing with fairness. [^1]


### How do we achieve equalized odds

Equalized odds can be achieved through a post training correction that does not require changing the entire training pipeline. Using equalized odds we cant set up our problem via constrained optimization. We want to find the predictor that minimizes l2 loss while satisfying our fairness constraint. We want to minimize our loss subject to the constraint that the true positive and the false positive rates are equal.

The authors proof that this problem can be combined into one linear program the depends solely on the measures accessible to an oblivious measure. The authors also prove a method for achieve the same fairness guarantee when using a classifier that outputs a score rather than a prediction. The authors use the ROC curve, which depends on the false positive and the true positive rate to do so.The prove shows that the ROC curve must lie in a specific plane where every point on the plane meets our constraint.If we do so then any cutoff we choose to use as our final classification will satisfy our fairness constraint. While their solution is no longer a linear program it can still be solved numerically using ternary search

The authors also prove that a non-discriminating bayes optimal classifier can be derived from the Bayes optimal regressor. We can find a closed solution for how much worse the optimal solution that satisfies the constraint is than original optimal regressor.

### Do oblivious measures actually get rid of discrimination?
The authors introduce two scenarios that could be very different in terms of fairness but both met their definition of equalized odds.

Scenario 1: We have a feature X1 (great great grandfather's profession) that is highly correlated with the protected attribute. It is independent from the target but the protected attribute is correlated with the target. There is a second value X2 (criminal history in justice situations) which is only correlated to the protected attribute through the target variable.

- A classifier that would be fair here would only depend on X2 and not X1
- A more accurate classifier would take into account X1 but this would not meet our measure of fairness

Scenario 2: We have a variable X3 (wealth) which is correlated with our protected attribute and predictive of our target.
- Using X3 in our model may or may not be seen fair discriminatory but by our measure it would be considered as unfair. We can correct our model to be one that uses X3 but does satisfy equalized odds

The two scenarios above seem fairly different. The difference in these scenarios is not picked up by equalized odds. Both models would satisfy equalized odds. These two scenarios are actually indistinguishable using any oblivious test. The authors prove this by creating a proof that follows the two scenarios they outlined above.

### Case study: FICO Scores
The authors and the paper with a case study examining different fairness measures in the context of FICO scores with regard to race. FICO scores are used to predict credit worthiness in the US. The five different classifiers looked at are.
1. Max profit: there is no fairness constraint
2. Race blind: The threshold for determining a loan is the same for each group
3. Demographic parity: A threshold is determined for each group so that the same percentage in each group is above the cutoff
4. Equal opportunity: The fraction of non-defaulting group members that qualify for the loans is the same
5. Equalized odds: The fraction of non-defaulters and the fraction of defaulters that qualify for loans is the same across each group

Using the authors proposed metrics (equal opportunity and equalized odds) we get a threshold in between max profit / race blind and demographic parity. Under max-profit and race blind situations minorities would have a much harder time qualifying for loans. Under demographic parity the opposite would be true

### Conclusion

The authors argue that a better path forward is to measure unfairness rather than proving fairness. Proving fairness is very difficult and there will always be certain things we miss.

Requiring certain fairness constraints can force the model builder to collect better data rather than relying on protected attributes

## My Closing Thoughts

After finishing the paper realized I was still a little unsure about how to implement the post-processing adjustment. The paper could have benefitted from clearly identifying what the adjustment is and how people could make that adjustment. After going back through the paper I understand how to set up the optimization problem after we have trained a classifier. But more explicitly taking the reader through these steps would make it easier for practitioners to adopt this approach.

I find that papers are stronger when proofs are in the appendix. It makes the main body of the paper readable and allows more detail in the proofs. This switch might have also helped clear up some of the confusion I faced on initial read.

It seems that since this paper was published the community has agreed we need stronger definitions of fairness and that a post-processing step is not enough. The authors of this paper call out as much in the body of the paper. But we also do not want to kill the good for the sake of the perfect. Would it be great if most practitioners adopted this approach? 100%. That would require building this approach into packages and making it easier for people to do.

I really appreciate framing fairness as a constrained optimization problem. We want to find the best classifier while still maintaining fairness. Once we have identified it as a constrained optimization problem it is easier to identify what tools to use and which mental frameworks are helpful. This problem framework is what I found to be the most compelling part of the paper.

I really appreciated the part in the conclusion about measuring unfairness rather than proving fairness. Fairness is not some binary. A model is not either fair or unfair. It will have some amount of unfairness. Measuring that unfairness and where it is coming from seems to be the most helpful path moving forward. So that leaves the question. What are the sources of unfairness and how do we measure them?

[^1]: Narrowing of scope in such a way is both instrumental and limiting. It makes the problem more tractable and easy to wrap our head around one part of it. But it also means any solution we have is incomplete. The authors mention as much later in the paper.
