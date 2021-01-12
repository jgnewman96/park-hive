---
title: 'Model Cards for Model Reporting'
date: Sat, 05 Oct 2019 22:08:21 +0000
draft: false
tags: ['Machine Learning']
categories: ['Papers']
---

[By Margaret Mitchell, Simone Wu, Andrew Zaldivar, Parker Barnes, Lucy Vasserman, Ben Hutchinson, Elena Spitzer, Inioluwa Deborah Raji, Timnit Gebru](https://arxiv.org/abs/1810.03993)

## Summary

The authors propose that machine learning models should be accompanied by documentation known as "model cards". A model card should outline who built the model, what the purpose of the model is, how it was validated and what it's performance is according to many different metrics. The authors focus on models that are making decisions about humans. They specifically call out models that characterize people and speak to the importance of evaluating how a model classifies different groups of people differently. 

The authors believe that model cards will better ensure that models are not misused and provide greater transparency into the performance details of a model. Some other benefits that the authors highlight about model cards is: 

* Creating model cards will force model builders to be more thoughtful and careful during the model building process. They will have to think ahead into how the model is being applied and what the weak points of the model might be. 
* Model cards will allow anyone to make better decisions about a model. It will provide both technical and non-technical users with insight into model performance and model use cases. 
* Model cards will also allow us to track how model's change over time. When a model gets updated it's model card should also get updated. By seeing the model card over time we can better understand how the model has changed over time. 

## Thoughts

* I really appreciated how this paper referenced best practices from other fields.  Other fields have been around for much longer and developed standards about how to document products. Machine Learning can learn from these other fields and adopt best practices for  documentation and providing resources about models. 
* I appreciate the human-centric approach to machine learning that this paper takes. Even if a machine learning model is not making classifications directly about humans, we should still take a human centric view of it.  All technology should be thought of with a human-centric approach. Why was this technology built, who is it going to impact and how is it going to impact them. We often get so wrapped up in technological progress we forget that technology is about enabling humans. 
* During my undergraduate studies of economics a term we talked about a lot was external validity. External validity is about generalizing our findings in one scenario to other scenarios. Very rarely is external validity talked about in the Machine Learning setting. One big reason might be because of the blackbox nature of some machine learning algorithms. When something is a black box it is less clear what circumstances it is valid for and which it is not. Even though the authors do not use the term external validity, they do use this kind of thinking. They specifically call out, if a model was trained in pristine conditions, it might not be valid for suboptimal conditions. It is critical to have more of this type of thinking in the Machine Learning community. 
* From my experience, even if data scientists know they should document, they will not. There is not a good tool to document that makes the process easy. Currently, documentation is a pain that feels like it slows the process down. We need to find a better way for data scientists to document their process.