---
title: "AI Neuroscience: Can we understand the neural networks we train?"
date: 2019-10-31T10:55:26-07:00
draft: false
tags: ['Deep Learning']
categories: ['Talks']
---
 Talk given by [Jason Yosinski](http://yosinski.com/). He works at Uber AI Labs and Recursion Pharmaceuticals

## Motivation

We train and use neural netwroks but we have a very minimal grasp on how they actual work. We have created systems that can beat humans players in games and actually create robots that can work. We have made huge advances in creating systems that can do impressive things. Most of the this improve has been driven by increase in computation and increase in amounts of data. Yet, scientific understaning is not connected to progress. When a computer becomes two times faster, that does not mean we understand it twice as much.

Currently we are building models that are more powerful than we can understand. Often we build things that are more complex than we can understand. But understanding falling two far behind what we do is dangerous. We need to work hard to keep our understanding closer to our progress.

* * *

Lets look at our understanding of a deep learning system. Alex Net was one of the first breakthrough networks in computer vision. At this point we can define the code for Alex Net in about ten lines of keras code. We define the size of the layers and the Relu between them. But this code is not actually the model itself, it is the skeleton of the model. The model consists of the actual matrices. Our model consists of the 60 million numbers that are in our matrices. It turns out then when we have all of the right numbers in the right places, these matrices can accomplish some pretty incredible things.

For the example of Alex Net, we understand the outer most part of the system. The input is image which is a bunch of pixels. The output is a classification of what is in the image. The difficulty comes from understanding the middle of the network. We can begin to understand the network by feeding images through the network and seeing what happens. We can plot the different parts of the network.

Jason developed a [visualization toolkit](http://yosinski.com/deepvis) that allows you to visualize how a neurel net is being activated when you feed an image through it. Jason during the talk demoed this tool to help us understand how the neurel net works. He showed how the first layer understand the lowest level of abstraction. So a transition from white to dark or essentially and edge. Then as we go further down the network we get to higher and higher levels of abstraction. SO one layer might have a detector for faces or for text.

The very first layer looks for patterns in pixel space. Then the second layer looks for patterns in the previous layer, not the pixel layer. By stacking these layers we slowly see more and more patterns. The first layer sees patters in an 11 x 11 pixel box. The second layer than has a 3 x 3 filter so it can see patterns in a 33 x 33 pixel space. Here is an [article](https://medium.com/@smallfishbigsea/a-walk-through-of-alexnet-6cbd137a5637) that outlies Alexnet's architecture for reference.

So now that we understand to some extent what it learns, can we understand why it learns these features. We neved told the system to learn faces or text or edges. We told it to learn how to classify pictures. We can conjecture that it learns these different abstractions because without them, it cannot accomplish the task we want it to. 

Imagine a seatbelt. A seatbelt is nothing but a grey stripe. But there are grey stripes everywhere. So it cannout just learn, grey stripe, otherwise it would classify so many things as a seatbelt. It had to learn that a seatbelt is gray stripe beneath a face. It is learning to detect a face, because that is an abstraction that will help it detect many other things. Or imagine a camera lense. If the system called everything that was a black circle a camera lens it would not be succesfuully. It should only label a black circle with text in the middle a camera lens.

Using this visualization tool we were able to understand a little about the middle layers of Alex Net. But we only looked at couple of neurons. It would take so long to understand one feature decoder. Understanding all of the neurons would take forver.

* * *

After publishing the paper on all of these findings, Jason was frustrated but entraced. We had improved our understanding of the system to some degree, but there still was so much to learn. He decided to try a different approach. Rather than passing a photo through a network and inspecting the neurons, lets ask a network what it thinks a guerilla is. We could start with a photo of white noice and feed it through the network. We could then slowly update the photo so that the network assigns a high probability of it being a guerilla. So at first it would have no idea what the photo was. Then we would back propogate through to the photo so that it thought it was more a guerilla. If we do this many times eventually the network will think it is a guerilla with very high probability and this should give us some understanding of what the network believes is a guerilla. 

But when they did this, they did not get a photo that looks anything like a guerilla. Yet the network says with very high probability it is a guerilla. He then wrote a paper about why this approach failed. It is great that in science when something fails it is a paper. In engineering when somethings fails, then you failed.

The next approach was to try the same thing but regularize the image space so no pixels are too extreme. Also make it so pixels do not change too quickly. They combined a bunch of regularizers (l1, l2, and spatial smoothness) and started getting better results. He showed examples with a hartebeast and a school bus. For the hartebeeast the networks does not learn hooves, because lots of animals have hooves. It does learn the horns and the shape of the top of the hartebeast are what defines a hartebeast. For a school buss it learns to look for patterns of yellow and windows and wheels. 

Know we kind of have an understanding of the network is learning. The regularizer allowed us to enfore a prior to keep images in a specific region.

* * *
Rather than using regularization though, we can use GANS. One network that determines whether or a not an image looks real and then another network that says does it look like a specific class. We then are also changing the input from being a specic class to being a caption.

What if we wanted to replace a network with a brain? We could then see how the brain work using a similar process. Unfortunately we cannot do back propogation through a brain.

But a group in harvard and Japan did something similar with Monkeys. They showed monkeys a blank image and then saw what neurons fired. They then altered that photo to make it excite those neurons even more. They did this iteratively until eventually they created a photo that looked like a monkey. The monkey was trying to recognize another monkey. 
 
* * * 

There must recent research is about trying to to understand what is happening during the training process. When we train an algorithm all we see is that the loss is going down. But what does that actually mean? We want to understand how is the network actually changing.

There must recent paper [LCA: loss change allocation for neurel network training](https://arxiv.org/abs/1909.01440) does exactly that. They examine the matrices over time to see how they are changing during the training process. It provides a rich visuilizations of how each neuron is changing.

They take away three things from this visualization.

1. Training is very noisy with different neurons going in different directions
2. It seems like some layers actually make the loss worse
3. There seems to be some levels of micro learning that is snychronized with nearby neurons being updated in similar ways.

This visualization gives us much more visibility into what is happening during training.

## My thoughts

Wow this was a really cool talk. I especially loved the iterative process of the research. We are interested in something, lets look at it and try and understand it. Okay, now that we have improved our understanding a little bit what are the next steps.

The idea that some of the neurons or layers are actually hurting the model in terms of loss is really odd to me. I am not sure what to make of that. The way Jason explained it was that it was because they were losing out to other layers. If we knew that one layer was hurting the model in terms of loss could we improve it by removing that layer? 

I am interested in how some of these visualizations, both the most recent ones about the training process and the ones used to visualize a trained model, could be used to improve the model training process. Is it possible that by providing these with end-users and them having a better understanding of the model is working we could improve the model building process. COuld we use these tools to better understand errors. If we look at an error and use this tool could we understand why the model is making an error and help make the model more robust?
