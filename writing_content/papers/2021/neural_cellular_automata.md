---
title: "Neural Cellular Automata Model of Pattern Formation"
date: 2021-03-10
tags: ['deep learning']
categories: ['paper']
---

By [Eyvind Niklasson](https://scholar.google.se/citations?user=x5sfH5MAAAAJ&hl=en),[Alexander Morvintsev](https://znah.net/), Ettore Randazzo and [Michael Levin](https://ase.tufts.edu/biology/labs/levin/)

[Paper Link](https://distill.pub/selforg/2021/textures/)

## Paper Motivation 

Patterns and textures are ill-defined concepts. As humans we are easily able to understand what Zebra strips look like and see a pattern. But no two zebras have the exact same set of strips. These type of patterns that are globally similar but uniquely different appear all over nature. 

Studying these patterns can help us understand their origins and how they are recognized by individuals. 

## Paper Contribution 
The authors apply Neural Cellular Automata to the task of texture synthesis. Texture synthesis involves reproducing the general appearance of a texture rather than making a perfect copy of what it has seen before. 

The authors introduce a loss function based on passing the image through another vision network. Using this loss function the authors are able to train simple networks that can generate textures. 
 
## Problem Set up and Model Details 
For a model to create patterns or textures it must learn a generative process. The generate process can be conceptualized as sampling from the distribution which governs this pattern. There is some distribution which characterizes the pattern and we want to sample one instance from that distribution.

A difficulty in creating a generative process for textures is building a loss function. How do we empirically quantify how close an example is to representing a pattern?  The authors us a Neural Cellular Automata (NCA) as the generator and then a different model is the distinguisher of patterns. The idea is similar to that of a [GAN](https://en.wikipedia.org/wiki/Generative_adversarial_network). Using the other model as a distinguisher provides the  gradient necessary for the generator to learn how to produce a certain style. 

    
The NCA works in the following way: every point of the images changes with time. A point changes in a way that depends on how the image is currently changing across space with respect to its neighbors. We can conceptualize an image as a 2D grid that wraps around the edges. We update a subset of the pixels in the grid at each time step. [^1]. 

The authors argue that NCAs are well suited for generating texture because they are similar to how texture generation works in nature. The authors propose a Partial Differential Equation (PDE) over the state of an image to characterize texture generation. They create a function that depends on the gradients and the Laplacian of the state space of the image. The state pace of the image is a vector whose components correspond to the visible RGB channels.

We can take the above approach and translate it into a deep learning setup. All of these operations are common operations in deep learning. Below is an image of the simple neural net that is used to update the image. The NCA model has 16 channels for each pixel as its output. The first three channels are the RGB values of the image. 

![generator architecture](/papers/2021/nca_generator.png =90%x*)


The authors use VGG as the discriminator of textures. A template image is feed into VGG and statistics are collected about the raw neurons in VGG. From previous research we have seen that convolutional neural nets that are trained on images seem to learn textures in their intermediate layers. 

The NCA is then run forward for between 32 and 64 iterations [^2] and the output image is put into VGG. The loss is the distance between the gram matrix between the template image and the NCA image. Then [ADAM](https://arxiv.org/abs/1412.6980) is used to update the weights of the NCA. They also do an experiment with Inception rather than VGG and get similar results.

![nca full system](/papers/2021/nca_full_system.png =90%x*)

 


## Results

The authors show that after a few iterations of training the NCA converges to a solution that looks similar to the input template. The solution using the NCA is not time invariant in that it keeps changing over time.

The authors also run many experiments to see how robust there framework is. For example they redefine the kernel to be s hexagon rather than a square and it still works. The NCA is able to generalize to a different kernel without being retrained. 

There are also a number of other examples in the paper that should be seen at the paper link. The visualizations are really quite powerful. They put two images side by side and run NCA's at different speed and find that they still coordinate. They also expand the size of the image halfway through the run and find it coordinates.
  
## My Closing Thoughts 

This paper is kind of incredible. It is the first paper that I have read on [Distill](https://distill.pub/) and I am already in love with Distill. A web page provides such a better interface to interact with than a PDF. The authors are able to create much better visualizations and make the paper format interactive. It felt like Distill provided an especially good medium for this paper.

I really enjoyed how the authors motivated this paper. They started with some observations about things in nature and then used that to drive their work. I love seeing research that gets inspiration from the natural world. 

I would have been interested to see how robust their model was to different parameterizations of the generator. What would have happen if there were more than 16 channels? What would have happened if there were fewer?

One of the coolest things about this paper was how it could learn with such little data and a very simple architecture. The NCA has a very simple architecture and it is able to learn how to generate a texture from just one example of that texture!

Currently, the authors train a different model for each texture. It seems like it would be easy to extend their work to have one model that can create multiple textures. We would essentially create a texture embedding by adding an additional layer that corresponds to the reference texture. This could be really powerful in that you could then make this into a texture generation tool. When creating a piece of art I want to give a certain area a texture. Let me select from a bunch of different reference textures or create a small instance of my own texture and then let it fill the space with that texture. 

[^1]: If all cells updated at the same time then each cell would need a different initial condition otherwise everything would end up symmetrical. 

[^2]: The authors found that using a stochastic number of updates steps worked as a good regularizer. 