---
title: "Interpretable Knowledge Discovery Reinforced by Visual Methods"
date: 2019-10-29T08:05:34-07:00
draft: false
tags: [ 'Design']
categories: ['Talks']

---
Talk given by [Boris Kovalerchuk](http://www.cwu.edu/~borisk/) , [Slides](http://www.cwu.edu/~borisk/ODSC/IML_tutorial.pdf)

## Motivation

Boris motivated the need for visual techniques with an example on the Iris data set. He showed three different models for the Iris data set, shown below.

<img src="/img/iris_classify.jpg" width="800">

He highlighted that the problem with each of these analytical approaches is that they generalize to areas we have seen before. Ideally, instead we would have a model that classified points in space we had seen before and refused to classify points in the unknown space.

But how do we know which spaces we have seen and which we have not? This can be done easily visually in 2 dimensions, but what about in higher dimensions.

Visualization is important because it allows us to answer questions in ways we cannot analytically. It also is easier to communicate and identify patterns. Good visualizations communicate information quickly and efficiently.

But visualizing data from high dimensions is very difficult. Anything larger than 3-dimensions is almost immediately intractable. How do we visualize high dimension data without loss of information?

## Talk Outline

The goal of the talk was to highlight how can we use visualizations to aid ML

Boris identified four different ways visualization can be used in conjunction with Machine Learning.

1. Visualize ML Models
2. Discover ML models using visual means
3. Explain models using visualization
4. Combining visual and analytical approaches for discovery

Overall, Visual Knowledge discovery allows us to make less of a trade off between interpretability and accuracy

### Visualize a trained model

Boris provided a couple different examples of how to visualize a model once it is already trained. He used the examples of how to visualize an association rules model and Tensor Board.

He argued that visualization can give models some explanability, but not the necessary depth of understanding. For example, a Decision Tree visualization can tell us what cutoffs a model is using. But it does not explain to user why it is using those cut offs.

By providing this proxy it is actually doing us a disservice. We believe we know why it it is outputting certain results, but we do not actually know.

Boris argues we should use analytical approaches from the beginning

### Using A Visual Approach from the start

Using visualization as an approach is very intuitive to people in low dimensional spaces. If we had 2-d data we would almost always create a scatter plot of it. But in higher dimensions because visualizations are harder people move away from this approach. We need visualizations that work in higher dimensions.

A common approach that people using for visualization high dimensional data is PCA (principal component analysis). PCA projects high dimensional data into 2 dimensions. But PCA is problematic because it is not interpretable. When we look at the data after PCA the coordinate plane it is on does not mean anything to us.

Boris then referenced the [Johnson Lindenstrauss Lemma](https://en.wikipedia.org/wiki/Johnson%E2%80%93Lindenstrauss_lemma) which provides a mathematical formulation on how hard it is to map high dimensional spaces to low dimensional spaces. When we use PCA we will lose a lot of information.

Imagine you have a 10 dimensional cube. There will be 1024 points in this cube. When you project this cube to 2 dimensions it will get projected into only four points. This means 256 points that used to be in different parts in the space will now be identical. By projecting this high dimensional space we have lost a lot of potential information.

This means there is potentially a big problem using PCA or t-SNE to find outliers. It might work, but it is also possibly then when we project the data down we are losing lots of information. We might have convinced ourselves that we have found all the outliers using this approach, when really we have not. What is a dense area in 2 dimensions might actually be very spread out in N dimensions.

There are approaches to visualizing high dimensional data in ways that we want understand. If we want to visualize a point in seven dimensions we will have to use a graph in 2 dimensions. One example of this is the [parallel coordinate plot](https://en.wikipedia.org/wiki/Parallel_coordinates)

In reality we should combine the two approaches. We should use PCA and the lossey approach, but recognize that it has its weaknesses. We should combine it with other visualization approaches that do not have the same weaknesses.

## My Thoughts

I left Boris's talk about half way through because I had to talk some calls for work. He did a good job motivating why visualization is important and why some of our current approaches are not sufficient.

I would have really appreciated a delicate balance of highlighting the benefits of certain approaches and how they can be used in conjecture. That might not have been the focus of Boris' talk, but I believe that will always be the key. ANy approach will have weaknesses and blind spots. Its about recognizing those weaknesses and using other approaches in conjecture.

Giving a four hour talk is just so tough. I think four hour talks almost never make sense unless a good portion of it is just personal work. Maintaining focus for that long of a time and learning new things that whole time is just unsustainable
