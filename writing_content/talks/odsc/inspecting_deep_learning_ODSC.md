---
title: "Principled Methods for Analyzing Weight Matrices of Modern Production Quality Neural Networks"
date: 2019-10-30T13:55:58-07:00
draft: false
tags: ['Deep Learning']
categories: ['Talks']
---
Talk given by [Michael Mahoney](https://www.stat.berkeley.edu/~mmahoney/) and [Charles H. Martin](https://www.linkedin.com/in/charlesmartin14)

Talk [Slides](https://www.stat.berkeley.edu/~mmahoney/talks/dnn_kdd19_fin.pdf)

[Github](https://github.com/CalculatedContent/WeightWatcher)

## Motivation

What most practitioners of deep learning do is train models. Training models that do something is the easy part. The hard part is actually evaluating and testing those models. Most people evaluate their models by tieing them to a certain set of data and seeing the accuracy on that data. This has problem because it is tied to a given set of data and the potential problems with that data.

The speakers explain a new approach of directly inspecting the weight matrices in deep learning algorithms. Looking directly at this weight matrices could also help with problems of reproducibility. We can analyze these weight matrices to understand what makes a model start of the art and what makes a model generalize well.

Ideally we could develop some sort of theory about these weight matrices that we could use to guide us. We also want to be able to use that theory to help in practice with creating these deep learning models.

## Methods

The speakers demonstrate their approach by examining the weights in state of the art pre-trained models that have been released to the public. We can look at how the weight matrices have changed over time.

the speakers argue for looking at the singular value density for the weight matrices of the matrices. We can examine these histograms of the singular values using Random Matrix Theory (RMT). At the beginning of training we should see a certain pattern that corresponds to a random matrix. As the model gets trained though we see a different pattern emerge.

We see the entropy of this matrix go down over time. This makes sense because maximum entropy means we have a completely random matrix. As the entropy decrease this corresponds to a move away from random structure.

The speakers than examined different models and saw how models changed to develop a theory of what made a good model. What can we see in VGG 19 that makes it better than VGG 11?

Deep learning systems that display longer tails in this singular value histogram also known as empirical spectral density have better performance and are better able to generalize. When we have alphas that are closer to 2 the better the model performs.

Alpha is a parameter value in the [Marchenko-Pastur](https://en.wikipedia.org/wiki/Marchenko%E2%80%93Pastur_distribution) bulk decay which is a formula for long tailed random matrices. The speakers have created a tool that examines the singular values and gives a heuristic using this alpka to get a sense if the model is performing well.

The speakers than presented a graph with test accuracy plotted correlated with the alphas and they show the lower the alpha the better the test accuracy.

## My Thoughts

This talk was really cool and raised a lot of interesting ideas. My notes do not do it justice. I highly recommend checking it out.

One of the things that was cool is both of the speakers come from a none deep learning background. They took what they learned from other backgrounds and applied it here. Having people from other fields and having them apply their knowledge is so helpful. Physics is essentially everything tbh.


