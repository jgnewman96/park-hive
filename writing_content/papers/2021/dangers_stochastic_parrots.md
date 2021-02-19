---
title: "On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?"
date: 2021-02-14
tags: ['ai policy']
categories: ['paper']
---

[Paper Link](http://faculty.washington.edu/ebender/papers/Stochastic_Parrots.pdf)

By [Emily Bender](https://faculty.washington.edu/ebender/), [Angelina Mcmillan-Major](https://www.linkedin.com/in/angelina-mcmillan-major-535188b5/), [Timnit Gebru](https://en.wikipedia.org/wiki/Timnit_Gebru) and [Margaret Mitchell](https://www.m-mitchell.com/)

## Paper Motivation

NLP has advanced a lot in recent years through the development of very large language models. These large models such as BERT and GPT 2/3 have improved upon the state of the art and expanded the tasks that were possible with language models. 

### Paper Contribution

This paper asks what are the possible risks of using large language models? How could we mitigate those risks? Is there such a thing as too big?. The authors provide recommendations such as understanding the environmental and financial costs, more carefully curating datasets rather than just ingesting anything on the web and encouraging other research directions besides bigger is better.

## Background

Language models are systems that are trained on string prediction tasks. Predicting the likelihood of a string given its preceding or surrounding context. Language models have improved through using pre-trained representations of words (word embeddings). Using embeddings decreases the amount of data needed to accomplish a supervised task.

Transformer models are continually benefitting from more parameters and more data. Larger language models are a result of increases in the number of parameters in the model and the amount of training data that the model use. Larger language models can be expected as long as the trend of increased performance continues. [^1]

There has also been a trend of taking larger models and making them smaller through distillation and quantization. While these models end up being smaller they still require the larger model to be trained first. 

## Potential risks from large language models 

### Environmental and Financial cost

- A previous paper estimated that training a large transformer model emits as much carbon dioxide as about 57 people would in a year. Cloud compute energy is not renewable and not carbon neutral
- Another paper looked at how financial costs led to increases in performance. An extra 150,000 dollars leads to only a 0.1 increase in [BLEU](https://en.wikipedia.org/wiki/BLEU). 

The authors suggest papers should be required to disclose training time, hyper parameters and cost. We should also report how much energy was required to train the model. This immense cost makes research less accessible. As a community we should be valuing not just performance but also efficiency of a model as a metric. 

The risks and benefits of a language model are not evenly distributed across people. The negative impacts of climate change impact marginalized communities first. Language models primarily benefit those who are already the most well off. 

### Risks from large amounts of training data

The large amounts of training data that are used in these models have been shown to include biases. They include stereotypes and derogatory references. These large datasets encode the dominant view which further harms people at the margin. Internet access and usage is not evenly distributed. Young users and those from developed countries are over represented. Surveys have also found that men are over represented in online platforms. 

Language changes over time especially as societal traditions and culture change. Only whats is covered by the media will be included in the language model. Also how the media covers something will impact how it shows up in the model. 

Language models are known to include bias such as stereotypical associations. Model auditing techniques are not robust enough to be sufficient. Auditing requires an a priori understanding of what to look for. We do not want to only mitigate bias but try and show safety. 

More resources need to be invested into curation and documentation of training data. Using large datasets we are more likely to incur documentation debt. The larger the dataset the more documentation it requires. We must budget for documentation needs and not collect more data than we can document 

### Misdirected research effort 

All research brings with it opportunity costs. Time that is spent on one direction is not spent on another. By focusing only on performance on leaderboards without deeper understanding we might be getting misleading results [^2]
   
### The path forward 

- We should do more careful planning ahead of time. Our research effort is a valuable resource and should be used towards building a system where benefits are not uneven. 
- More research should go towards understanding current models 
- We should look for use cases that help marginalized communities

### My Closing thoughts

This was the paper that led to Timnit Gebru's termination at Google. It is shocking to me that this was the paper that led to that. It did not feel like there was anything controversial in this paper at all. It was asking an important question and did so in a balanced way. 

One of the strongest points in this paper was how the benefits and risks of large language models are unevenly distributed. I appreciate that point because I think it is more actionable and provides insight rather than just saying the risks are larger than the benefits. If you just said the risks ae larger than the benefits, that is an easier point to contest. But by looking at the distribution the point is less debatable and we can reframe the discussion about how to make the benefits stronger for the people who recieve most of the risk. 

After reading this paper it feels like I need to read Gebru's other paper [Datasheets for Datasets](https://arxiv.org/abs/1803.09010). There is so much more research effort that goes into how to create larger language models rather than how to document datasets. It would be such a big win if more research energy was going into documentating datasets. Documenting large data sets is going to be hard. This means we have to put a lot of effort into learning how to do it and not let the enormity of the work make us inactive. 

I did not really understand section 6.1 and its discussion of meaning and coherence. I think the basic idea was that when a person says words they are going to an intended audience with a purpose. But language models do not have intent or audience. Because language models generate text or speech in a different way than humans we should interpret what is generated differently. This can be problematic though because when we see text we might not know if it came from a language model or a human. Even further because previously all text had come from a human we might interpret lanuguage model text in a specific way because historically all text came from humans. 

This made me think about how a human to AI interaction is fundamentally different than a human to human interaction. The emotional baggage and feelings that come with it is different. We should not use that as excuse to be rude to AIs (like I sometimes might be to Siri), but it is important to recognize this. I would be really interested to understand more about those differences. How do humans interact with a chatbot if they think there is a human on the other side versus if they think it is a language model? What would the implications of those findings be? Furthermore, langugage models are trained on text from situations where humans are communicating with other humans. Should we be modeling AI based communication tools on human to human interaction or should we be thinking about how AI to human interaction is a different paradigm?

This paper also sparked a new research idea in me. Language models are trained on lots of text from the web. After GPT-3 was released there started to be a lot of content on the web that was generated from GPT-3. This means that a future language model might be trained on the output of a previous language model. What are the implications of this? Could this lead to models skewing in a certain direction and slowly becoming more offensive. I would be curious to experiment with this. What happens if you train a language model directly on the output of another language model. What happens if you do that in succession for many different models?


[^1]: I would love a plot of some relationship between number of parameters and an accuracy metric. I think I have seen one before but I am not exactly sure where. 

[^2]: To me this is more a problem with our current tests than a problem that we focus on tests. If we cant measure something it is impossible to make progress on it. In my mind the solution is to change what our tests are. Lets have benchmarks the reward the things the authors in this paper want us to reward. 