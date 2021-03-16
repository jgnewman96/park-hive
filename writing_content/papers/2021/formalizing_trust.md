---
title: "Formalizing Trust in Artificial Intelligence: Prerequisites, Causes and Goals of Human Trust in AI"
date: 2021-03-16
tags: ['ai policy']
categories: ['paper']
---
[Paper Link](https://arxiv.org/abs/2010.07487)

By [Alon Jacovi](https://alonjacovi.github.io/), [Tim Miller](https://people.eng.unimelb.edu.au/tmiller/), [Ana Marasovic](https://www.anamarasovic.com/) and [Yoav Goldberg](https://www.cs.bgu.ac.il/~yoavg/uni/)

## Paper Motivation

Trust is a central component of any interaction. We want the right balance of not too much trust but also not too little trust. How does trust work in humans relationships with AI?

## Paper Contribution

The authors create a model of trust between humans and AI based on sociology's interpersonal trust. There are two key components of this model
1. The __vulnerability__ of the user
2. The ability of the user to __anticipate__ the impact of an AI's decision

The authors then discuss how to build trustworthy AI and how to evaluate whether trust has manifested and is warranted.

### Background
The recent growth in XAI is partly motivated by wanting to increase trust between users and AI systems. Trustworthy AI seems to be a precursor to AI being safely implemented in society. There are many vague and unclear aspects of trust which are difficult to formalize using existing HCI tools. The authors turn to sociology and look at interpersonal trust to help formalize trust in this context.

### Defining Trust

The authors define interpersonal trust as
>  if A believes that B will act in A’s best interest, and accepts vulnerability to B’s actions, then A trusts B

The goal of this trust is to make collaboration between people easier. A must be impacted or vulnerable to B's decision and A must anticipate that B will act in A's best interest. By applying this definition to human-AI interactions it is clear that risk is a prerequisite for trust. There must be the possibility that B does not act in A's best interest.


**Contractual trust** is a more specific definition where the trustor has belief that the trustee will follow a contact. There are both specific types of trust and "broad trust". Broad trust is built on many different individual trusts. Explanations for a model can help increase one specific type of trust. This might lead to broad trust and it might not. Different types of documentation might lead to trust in a different way. A model card might make you trust that a model is not biased or a datasheet might make you believe that the model maintains privacy.  Contractual trust allows us to define trusting AI as believing that a set of contracts will hold. 


It is possible for someone to __trust__ a model without a model being __trustworthy__. Being Trustworthy is a property of the model where as trust is a property of the person in the interaction. A model is trustworthy if it will maintain the contract. A person has trust if they believe the model will keep the contract. 

Trust is __warranted__ if it is because a model is trustworthy and it is unwarranted if a model is not trustworthy

### Causing Trust
There are two different ways trust can be caused in a user. 

1. **Intrinsic trust**: When the user comprehends the true reasoning of the model and the reasoning matches the users priors of agreeable reasoning. If we have no prior on what behavior is trustworthy we cannot gain trust [^1]
            
2. **Extrinsic Trust**: When the user trusts the model not through explanation but through its behavior. This trust comes from observing symptoms rather than the inner model's workings. Extrinsic trust is developed through the model's evaluation scheme. The authors identify through different ways extrinsic trust can be brought about
1. By trusting the people who are deploying and rolling out the model 
2. By trusting the model after seeing its performance in the wild
3. By trust the model because of its performance in test sets. 

A key motivation for XAI is that it will increase users trust. XAI is a form of intrinsic trust that conveys understanding to users about the inner workings of the model. It does not impact trustworthiness but it does impact if trust aligns with trustworthiness. 

### Design Considerations

The authors listed quite a few design considerations that follow from their work but these two were the ones that most stuck out to me. 
1. AI developers should be explicit about the contracts that their models maintain.
2. We do not want to just increase trust but make trust align with trustworthiness. 


## My Closing Thoughts

I really appreciated this paper. It took a step back from XAI and asked some broader questions. What are the reasons we care about XAI? We care about XAI because we want to trust our system. But why is trust important? Trust is important it because it makes collaboration easier. With this larger framework it is now easier to think about XAI, why we use XAI and what things we should be thinking about when working on XAI. 

This paper covers a lot of ground so I want to call out the three ideas that felt the most impactful to me: 
1. That real trust requires vulnerability. That we have to accept some risk if we want to talk about trust. When there is not risk our methods for evaluating trust are not sufficient because there is no vulnerability. When people talk about AI they want there to be no vulnerability. The discussion does not feel like one about trust but rather one of trying to eliminate vulnerability. AI is not going to eliminate vulnerability. It is going to change what vulnerability looks like. We are much more accustomed to being vulnerable to other people and forgiving them if something goes wrong. We are not as forgiving when it comes to systems. 
2. By thinking of trust as many small contracts we can break it down into different parts. While "broad trust" is very difficult to wrap our heads around, these many small contracts that constitute trust make it much more manageable. I wish they had continued using this framework for more of the paper. They introduced it at the beginning and then kind of went away from it to discuss other things. 
3. The difference between trustworthy and trust and how that leads to unwarranted trust is insightful. Trust is no longer a property to maximize but a property that we want to be in alignment. We want trust to exist when we have a trustworthy system and we do not want trust when our system is not trustworthy. 

One place I feel the authors missed the mark is their discussion of the trustworthy property. The authors discuss the different ways to evaluate if a system is trustworthy or not. In my mind, we can never know if a system is trustworthy. Trustworthy is a latent variable that it is actually impossible for us to observe. We measure other things that correlate with a system being trustworthy, but we cannot measure the trustworthiness of a system. It is similar to how we can never know if our code is correct. Testing our code can provide evidence that our code is correct, but we will never know with certainty.  

I also felt like I had some difficulty with the definitions of intrinsic and extrinsic trust. Specifically that the authors categorized XAI work as intrinsic. I feel like there is some XAI work that might be intrinsic and some that might be extrinsic. For example, looking at the parameters of a linear regression model. This to me feels like intrinsic trust for sure. We are directly looking at properties of the system and gaining trust from them. Another example of this might be looking at the rules in a decision tree or feature importance in a model. But there are other types of XAI work that feels more like extrinsic trust. There are some XAI methods like [LIME](https://github.com/marcotcr/lime) which are tied to specific instances. These methods do not inform us about the general properties of the model but rather what the model is doing in a specific instance. That feels much more like extrinsic trust based on the authors definition. The distinction is almost one of general or specific. Is the trust due to some general property of the model or is it from a seeing a specific behavior of the model when it is applied? Understanding that XAI can fall into both of these categories and therefore how different XAI methods are trying to achieve trust in different ways is an interesting discussion. 

There are two types of works that I notice recurring in my readings. The first is embodied by a paper like this, the authors take a complicated concept formalize it to understand it in better detail. Some examples of work that also fall in this category are, [legal compatability of fairness definitions](/#/post/legal_compatability_fairness), [framework for unintended consequences of ML](/#/post/ML_harms_framework), or  [a cognitive process theory of writing](/#/post/theory_of_writing). The second category is papers that focuse on how our formalizations actually miss a lot and can be harmful. That things are much more context dependent and we have to be wary of the places our frameworks are blind. Some examples of that category are [reliance on metrics](/#/post/reliance_on_metrics) or [decolonial ai](/#/post/decolonial_ai). I am excited to think more about if there is a tension between these types of works. Are they both important especially as a field swings in one direction or another? 
         

[^1] : I really appreciate this point. It is easy to abstractly talk about trust without knowing what we are looking for. If we do not have a definition of trust and it is constantly moving then how will we ever trust a system? This does not mean there has to be one static definition of trust. Rather, in our specific context we should define what trust will mean. 


