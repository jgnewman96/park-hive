---
title: "Generative Models for Effective Machine Learning On Private, Decentralized Datasets"
date: 2020-08-02T11:37:47-04:00
draft: false
tags: ['Deep Learning']
categories: ['Papers']
---

[Paper by Augenstein et al.](https://arxiv.org/pdf/1911.06679.pdf)

I have stared a weekly reading group with my friend and former co-worker [Tushar Chandra](https://tusharc.dev/). Our format is that one person proposes a set of papers, and then the other picks a paper for the week.

## Summary

The authors motivate their paper with the following logical steps.
1. Manual data inspection is a key part of the machine learning workflow
2. There are occasions when manual data inspection is either undesirable or infeasible (privacy requirements, or federated learning where data is stored at the edge).
3. When data inspection is infeasible, generative models trained with federated methods can be a substitute for the role of manual data inspection.

The authors point out a **trade-off** between good data stewardship and the needs of a modeler. Good data stewardship can make modelers lives more difficulty. This work is driven by maintaining good data stewardship and not make a modelers life worse off.

The paper outlines six tasks where a modeler generally needs access to raw data
1. Sanity Checking Data
2. Debugging Mistakes
3. Debugging unknown labels/classes
4. Debugging poor performance on specific slice of data
5. Human labeling of additional data
6. Detecting bias in the training data

From my experience 2 through 4 are essentially the same thing. When you are debugging you do not know what the issue is until you identify it. This means the requirements for 2-4 are the same, because we are taking the same approach to debugging.

The authors argue that practitioners can use generative models instead of data inspection.

{{< quote >}}

Generative models will have a fundamental role to play in enabling the widespread us of privacy-preserving ML workflows

{{< /quote >}}

***
#### Differentially Private Federated Generative Models

The types of models proposed in the paper are a combination of three different technologies: generative models, federated learning and differential privacy

**Generative Models** are a class of models that can synthesize new examples.
- An example of a generative model is a Variational Auto Encoder or a GAN. A generative model takes data in a different latent space and maps it to the space our data resides in.
- For example, a VAE works in the following way.
    - There is an Encoder network and a Decoder Network. The Encoder network takes data examples, (images, text etc..) and maps them to a latent space. The Decoder network takes that latent space as input and maps it back to our original space. To train a model, we minimize the difference between the original data example and the output of passing that example through the Encoder and then out the Decoder.
    - Once we have trained the Decoder, we can use the Decoder to create new data examples by sampling from the latent space that the Encoder maps too.

**Federated Learning** is the processing of training and evaluating against distributed data
- The most common cases of federated learning are when working with mobile or IOT devices. Raw user data never leaves the edge device
- We train a model by randomly choosing a subset of devices to download the current model. Each device then locally computes a model update based on its data. The device then sends updates back to the coordinating server where they are aggregated to make a global update

**Differential Privacy** is a privacy guarantee for data that gets used to train the algorithm. The goal is that a model and its parameters can be released and yet information about any individual in the training data can not be reverse engineered. One way I have seen differential privacy formulated is the following: Adding or subtract an individual data point from the training data cannot have a meaningful impact on the model.

Differential privacy and federated learning together afford user privacy protections. While generative models often memorize certain examples leaking privacy, differential privacy will not allow a model to be published that displays this behavior.

***

The paper next discusses two case studies for how to use their proposed approach.


Differentially Private Federated RNNS for text
- An RNN works by taking a sequence of tokens as input and then outputting the probability of the next token. Tokens could be characters, words or sets of words depending on how you set up your task. We can frame an RNN as a generative model by sampling from that output distribution to generate many different sentences.

- Experiment: We have a keyboard app that uses a word level language model to offer next-word prediction (eg. gmail). Our goal is to detect a bug in the training model pipeline

- We have introduced a bug by incorrectly concatenating the first two tokens of every sentence. All of these incorrectly concatenated tokens will show up as out side of our vocabulary

- Our model is a word level model but we can also use a character level model for debugging. We can use these models to spot the bug. We observe that our OOV happens at the beginning of the sentence and contains a space.

Differential Private Federated GANs for images

- A GAN (generative adversarial network) works by training two models. One is a generator which maps a random input in a low dimensional space to a high dimensional space like an image. The other is a discriminator which judges whether an input is real or created by the generator. The two models are trained by trying to defeat the other one.

- Experiment: on-device handwriting classification &rarr; A bank app that scans a check and needs to process text. We introduce a new bug that flips pixel intensities. We see that more people start correcting the model output but we do not know why. We cannot inspect the data itself, but still need to find the source of the bug.

- We can do this by training two new models. One on data where we are performing the best and one where we performing the worst. We can contrast the images synthesized by the two GANs to identify the bug.

***

The authors conclude the paper with some current limitations.
    1. federated generative models should require little parameter tuning. Currently training a model requires a lot of parameter tuning and this can make using these types of models quite difficult.
    2. The fewer examples a bug shows up in, the harder it is to spot. It will be particularly tricky to spot bugs using generative models if they do not show up very often.

## Ending Thoughts

- I really enjoyed reading this paper. When I first started reading the paper I thought they were going to be introducing a new algorithm. But really what they are introducing is a framework or approach. You cannot blindly adopt this approach and get good performance and security. The practitioner needs to still be quite creative about debugging. But that is actually why I like this paper so much! The case studies show ways to be creative about debugging. These approaches could be really helpful even in a setting where you did not need to use federated learning.

- The paper does a really good job of using an appendix. There is so much content here that most of the results and the details of the experiments have to go in the appendix. This allows the main paper to be an easy read and do a very good explanation job. If you want to dig into the details, you can refer to the appendix.

- I have a particular affinity for papers that lay our future areas of research. They directly call out that while this work is very promising, it is still in its beginning and there are so many further avenues for research.

- Both of the examples in the paper assumed we had a trained model that worked and then a bug was introduced. I would bet that a much harder domain is when we are building a model for the very first time. Maybe it is unrealistic to say we will need to build a model without ever seeing any data. The more realistic approach is that once we put the model into action we will not see new users data. The task of trying to build a model without seeing data would be an interesting project though.

- It is interesting to me that the authors assert there are situations where we will not be able to see data. My experience with data stewardship has been that often raw data cannot be seen, but some version of de-anonymized data and with certain attributes hidden can be seen. I am having trouble imagining a scenario where no version of the data can be seen by the model builder. But it might just be something to aim for. I can understand how if you can guarantee users that data will never leave the device that is a pretty great privacy guarantee.



