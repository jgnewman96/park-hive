---
title: "Datasheets for Datasets"
date: 2021-03-02
tags: ['ai policy']
categories: ['paper']
---

By [Timnit Gebru](https://en.wikipedia.org/wiki/Timnit_Gebru), [Jamie Morgenstern](http://jamiemorgenstern.com/), [Briana Vecchione](http://brianavecchione.org/), [Jennifer Wortman Vaughn](http://www.jennwv.com/), [Hanna Wallach](https://en.wikipedia.org/wiki/Hanna_Wallach), [Hal Daume III](http://users.umiacs.umd.edu/~hal/), [Kate Crawford](https://www.katecrawford.net/) 

[Paper Link](https://arxiv.org/abs/1803.09010)

## Paper Motivation
There is currently no standardized practice for how to document datasets. In the electronics industry every component is accompanied by a datasheet that describes its characteristics, recommended uses and test results

## Paper Contribution 

The authors propose that every dataset be accompanied with a datasheet that documents its motivation, collection process and reccomended usage. This will facilitate better communication between dataset creators and consumers. The major contribution of this paper is defining the questions that are asked on that datasheet. 

### Background

Machine learning models are trained and evaluated using a dataset. The characteristics and properties of this dataset will impact the model's behavior. Mismatches between the training dataset and the situation where the model is deployed can lead to unwanted biases or poor performance. 

The goal of datasheets is to address the needs of two key stakeholders, dataset creators and dataset consumers. For creators we should make known any underlying assumptions or potential risks and harms. For consumers it will allow them to make informed decisions about how to use the dataset. Datasheets will also be helpful for other people such as policy makers or individuals who are impacted by the model. [^1]

Datasheets may be different depending on the domain they are being used in. The creation of datasheet should not be automated. It runs counter to the idea of forcing a creator to reflect on the process of creating a dataset. 

### Development of datasheets 

To develop the questions that go on a datasheet the authors first created an intial set and then refined them based on feedback from many different people in their network. They then built two examples datasheets for two well known public datasets. After creating the datasheets they looked at the end product and noticed some gaps and redundancies which led to some changes. They followed that up by sending the questions to two real teams and asking them to make a datasheet and getting feedback from them. 

### Questions and Workflow

I was intially writing out all of the datasheet questions here and then decided not to. Basically the whole paper is just listing out the questions. The questions are grouped into a few different stages that are supposed to mimic the dataset life cycle. The sections are motivation, composition, collection process, preprocessing, distribution and maintence. The paper contains the full list of questions and a couple of examples so go look at that for more detail. 

## My closing thoughts

I am actually quite disappointed by this paper and felt it was underwhelming. I 100% agree with the motivating ideas and the need for this type of work. It is also clear the authors put a lot of work and thought into what questions to include in the datasheet. But I felt the contents of the paper were mostly just a list of questions. It feels like that list could have gone in the appendix. There are a number of related topics I would have loved to read the authors thoughts on. 

How did the datasheet questions change over time as they got feedback? What did they learn as they put it in front of other people? How do they imagine it might change over time? 

I also would have loved a more thorough discussion of how to think about adoption of this. Right now people are not creating datasheets for their dataset. Why not? Is it a lack of time, a lack of incentive or just because they do not know about datasheets. How much benefit are people actually getting when they create datasheets? What are some concrete examples of these benefits? It is one thing to just create a resource and it is another to actually work towards adoption. It feels like this work still leaves a lot on the table. 

Related to that above point, it was really disappointing to find that there was not any tooling available related to this work. There was not even a github repo that had the example datasheets, a blank datasheet which tracked the changes over time. If someone wanted to start creating datasheets they would have to copy the questions directly out of the paper pdf. Just some small simple tooling would make datasheets a lot more accessible and probably increase adoption greatly. Even just a web interface that allows someone to make it and stores it in a more interactive way than 6 page PDF would be a big win. That does not even dive into how we could integrate the documentation process better and come up with more dynamic visualizations. 

[^1]: I disagree a little bit with the authors framing here. I do not think it is dataset creators who get some of the most benefit. The dataset creator is actually the person who incurs the most cost. If the benefit was a lot greater than the cost, everyone would be doing this. The people who get the most benefit without any cost are some of the other stakeholders the authors call out.