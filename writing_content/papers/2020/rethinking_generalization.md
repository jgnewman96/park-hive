---
title: "Understanding Deep Learning Requires Re-thinking Generalization"
date: 2020-08-13T17:39:34-04:00
draft: False
tags: ['Deep Learning']
categories: ['Papers']
---

By [Chiyuan Zhang, Samy Bengio, Moritz Hardt, Benjamin Recht, Oriol Vinyals](https://arxiv.org/abs/1611.03530)

### Papers Motivation

The authors note that successful deep learning models often exhibit small differences between training and test performance. This is generally attributed to modeling techniques that are supposed to achieve generalization, such as regularization.

### Papers Contribution

Using many experiments, the authors show that these traditional approaches do not provide a satisfactory answers for why deep learning generalizes well. Regularization is not what leads to good generalization, and state of the art deep learning can successfully fit random noise.


### Background

Neural networks often have more parameters than the number of data examples they are trained on. Yet these models do not exhibit overfitting. We observe a “small" generalization error (the difference between training and test error)

So why do some neural networks generalize well and others that don't?. The traditional view of generalization is unable to distinguish between neural networks that generalize well and those that do not.

### Randomization Tests

The authors ran an experiment where the true labels for a data set are replaced with random ones. The goal of this test is to understand the model capacity of a neural network. Even with random labels the neural networks achieve 0 training error. This means test error is equivalent to the results of a random guess because there is no correlation between the training data and the test data. As a result of changing our data, generalization error has gone up a lot without changing anything about the model. This may be a surprising result because if there is no signal in the data we would expect the network would struggle to learn anything.


The authors ran experiments on the continuum from no randomization to full randomization. Here are the six different experiments they ran
- Train with the True Labels
- Train with Partially corrupted labels, The label is corrupted with probability p
- Train with Random labels
- Train with Shuffled Pixels: A random permutation of pixels is chosen and then that permutation is applied to all images
- Train with Random Pixels: A different random permutation is applied to each image
- Train with data from a Gaussian: A Gaussian distribution is used to generate random pixels for each image

For every single one of these experiments the neural network is still able to converge

### Implications of randomization tests

This result proposes challenges for traditional methods of thinking about generalization
1. A neural network has the ability to memorize the entire data set
2. Optimization on random labels is still an easy problem
3. This experiment rules out VC-dimension, Rademacher complexity and uniform stability as possible explanations for generalization

### Explicit regularization
In the above experiments explicit regularization was not used. Regularizes are the standard tool to mitigate overfitting. __Explicit regularization is supposed to confine the solution space to one that should generalize well__.

To better understand the role of regularization the authors compare what happens when neural networks are trained with and without regularization. The authors look at three regularizes:
- Data augmentation: For example for image data, changing the brightness or saturation
- Weight Decay: Equivalent to an l2 regularizer on the weights. Essentially push the weights closer to zero
- Dropout: Mask out each element of a layer output randomly with a given dropout probability

The authors find the regularized neural networks do tend to generalize better, but even with all the regularizers turned off, the models generalize well. Data augmentation seems the be the most powerful regularizer and the other two do not make as much of a difference.

{{< quote >}}
It is difficult to say that the regularizers count as a fundamental phase change in the generalization capability of
{{< /quote >}}

### Finite sample expressivity

Previous work on expressivity has looked at the “population level“: What functions of the entire solution space, can or cannot be represented?. The authors argue that a more relevant question is what is the expressive power of a neural network on data of size n. When the number of parameters p of a network is greater than n, even just a simple two-layer neural network can represent any function of the input sample.

### Implicit regularization

Early stopping could help with generalization but it does not have overwhelming benefits. Batch normalization has been found to improve generalization performance. To test the impact of batch normalization they train the inception model without batch normalization. The impact on generalization is only about 3 to 4 percent.


### Can Linear Models help us Understand NN
If the number of dimensions is greater than the number of data points, we can fit any labeling. But can we generalize well with a rich model and no regularization? Do all solutions generalize equally well? Will one solution generalize better than others?

SGD finds a very specific solution to this problem based on how it makes updates. SGD find the minimum l2-norm solution to the problem. Said another way “out of all models that exactly fit the data, SGD will often converge to the solution with the minimum norm“. This minimum norm helps provide some guidance but it does not have full explanatory power

### My Closing Thoughts

This paper is written quite well and is approachable. It covers some dense topics but is the main body of the paper is readable. I have noticed that using the appendix well is an important part of making a paper approachable.

This paper also really drives home the importance of mixing theory with experimentation. They show that theory we have traditionally used, might not apply anymore. It is important to be constantly testing theory and aligning our theory with practice.

Recently, I have enjoyed reading papers less for their findings and more for lessons on experimental design. One of the nicest parts of this paper is how they set up their experiments.

Two thoughts on the actual contents of the paper.

1. In the one quote I have above, the authors use the term "phase change". I imagine what they mean using that term is that regularization is not something that brings you from non-generalization to generalization. But what determines generalization or non-generalization. I would have liked clearer definitions of those terms. Does a 5 percent difference in accuracy represent a phase change? what about 10%?

2. It is interesting that the authors think about generalization solely in terms of model properties. When I think about generalization I am often thinking about the properties of my data. To me generalization is not just fitting unseen data, but fitting unseen data that might have some distribution shift or a be generated in a different way. If the unseen data is exactly the same as the seen data, then a model which fits the data well will of course generalize.


