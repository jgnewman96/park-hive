---
title: "Trouble shooting Deep Neural Networks"
date: 2019-10-31T11:51:11-07:00
draft: false
tags: ['Deep Learning']
categories: ['Talks']
---

Talk given by [Josh Tobin](http://josh-tobin.com/) works at Open Ai and [Full stack Deep Learning](https://fullstackdeeplearning.com/). [Talk Resources](http://josh-tobin.com/troubleshooting-deep-neural-networks.html)

## Motivation

Troubleshooting neurel nets is hardest part of building a deep model. Even the best practitioners spend a long time trouble shooting. Josh argues that the vast majority of what the best practitioners do to troubleshoot their models can be broken down to a decision tree. During this talk he presents that decision tree. Generally, 80-90% of our time goes into debugging and tuning while only 10-20 percent is deriving math or building implemnations. Troubleshooting is defined as helping your model achieve optimal performance.

But why is troubleshooting Deep Learning so hard? Imagine that you are trying to replicate the results from a paper, but for some reason the lose you are achieving is worse than what the paper reports. It is very difficult to tell if you have a bug and where that bug might be. In software engineering bugs are generally quite loud. You will know immediately when something is breaking. In deep learning though, bugs are essentially silent. There are many possible causes of the error. It could be a case of simply having the wrong hyper parameters. Model performance can be very sensitive to hyper parameters.

## Strategy for Deep Learning Troubleshooting

Before we delve into the decision tree to follow, there is a certain mindset we need to have in mind when we are troubleshooting Deep Learning. We need to have a pessimistic mindet. It is going to be very difficult to disambiguate errors. We should not assume that things are going to work. By being pessimistic we are going to start as simple as possible, and then slowly ramp up complexity. By starting simple and slowly making changes we are able to understand why is our performance changing.

### Start Simple

The first step in starting simple is to choose a simple architecture.

- If our input is images &rarr; start with le net then move to res net
- If our input is sequences &rarr; start with a LSTM and then slowly move to transformer
- If our input is something else &rarr; start with a fully connected neural net with one hidden layer, where you go after that is problem dependent

But what about multiple inputs? &rarr; For example two images and sentence

- First map each into a lower dimenstional feature space
- For images conv net and sentence LSTM
- Then you flatten the outputs and concatenate them
- Finally send it through a fully connected layer to get an ouput

Some other good principles to starting simple

- Use sensible defaults
- Normalize inputs: do not pass raw images, substract the mean and divide by variance
- Consider simplyfing the problem

  - use a subset of you're data set
  - if you have many classes just start with a couple
  - create a simpler synthetic training set

### Implement and then Debug

The first step is really just getting your model to run. Here is a list of the most common bugs that might break your model at the very beginning.

- Incorrect shapes for tensors: A lot of libraries will silently broadcast tensor without your knowledge
- Preprocessing your inputs incorrectly
- Incorrect input to your loss function &rarr; softmaxed outputs to a loss that expecits logits
- Forgetting to set up train mode for the net correctly
  - toggling training / evaluation with batch normalization depedencies
- Numerical instability &rarr; inf/Nan
  - often stems from using an exp, log or div operation. Use off the shelf softmax rather than writing your own

Some general tips

- Use a light weight implementation: You should have the minimum number of possible line of code for v1. Ideally less than 200 lines of code. Each additional line of code is new chance for bugs
- Use of the shelf components when you can
- Build complicated data pipelines later in your development process. You should not spend time doing this when you are still debugging. Begin with a dataset that you can load into memory. 

Try to see if you can overfit a single batch. This will help catch a very large number of bugs. You should be able to the drive the error of your model to zero on a single batch. If you are unable to do this, it will help you find the source of potential bugs.

It is helpful to compare your results to known results. You might have an error if your model is performing worse than the best known results. Ideally you could compare your model with an official model implemntation evaluated on a similar dataset to yours. This would even allow you to compare your code with their code. A less ideal solution would be to compare with an unoffical model implementation on github. But be wary, lots of repos will have bugs in them. Worst case you can compare your results to the results from a paper with no code associated with it. It is also always good to compare with super simple baselines. How does your model compare to the average of outputs, or a linear regression? 

### Evaluate model, then decide what to do next

A good framework for doing model evaluation is thinking in terms of the bias variance decomposition. This allows you to think about underfitting and overfitting. We can look at the gap between our performance on our training set, our validation set and our test set. The gap between our training set and our validation set is how much our model is overfitting. Test error can be broken down into the following components
> test error = irreducible error + bias + variance + distribution shift + val overfitting

By breaking error into its parts we can identify what is causing our error and prioritize our improvements. Distribution shift happens when our training or validation data comes from a different distribution than our test set. For example our training data could come from the day time and our test could be from the night time. We can handle this by using two validation sets. One validation set from our training distribution and one from the test data. The difference in our error between these two validation sets is our error due to distribution shift.

### Improve model or data

The first place is to address under-fitting. Here are some things to try ranked from what you should try first to what you should try last.

- make your model bigger, wider or deeper
- reduce regularization
- do error anlysis
- choose a different model architecture
- tune hyper parameters
- add features

Second you shoud address over-fitting. Once again a list of what you should try from first to last

- add more training data
- add normalization
- do data augmentation
- add regularization
- do an error analysis
- choose a different model architecture
- tune hyper parameters
- Use early stopping
- Remove features
- Reduce Model size

After you have addressed over and underfitting you should move on to distribution shift. One note about over and under fitting, it is possible that combating one will exacerbate the other. You should not just treat them as isolation. You might fix underfitting then do some things to fix overfitting and then need to do some more to fix underfitting. Below is a list for what to try ranked from first to last to address distribution shift.

- do an error analysis: look at specific errors and prioritize places for more specific data collection
- Synthesize more data rather than collecting it
- Domain adaptation techniques. This is a new area of research that is not quite advanced enough

So how do we do an error analysis? We should look at our errors on the train-validation set and the test-validation set. We can go through a set of errors and manually classify them into different categories. We can then hopefully understand what is driving our errors and how many come from each category. We want to understand how much error does each category introduce and how costly are the possible solutions to fix it. We can then prioritize, if we want to collect more data.

It is important to ocassionaly re-balance your datasets. Switch what is your validation set and every so often check up on the held out test set.

### Tuning Hyper Parameters

There are so many differeny hyper parameters that tuning them can be quite daunting and difficult. You should first start with learning rate and batch size. These have been shown to be two of the more important hyper parameters. If this does not get you where you want then look at the others. Rather than doing a grid search you should do a coarse-to-fine random search. Begin by looking in a large range and then narrow in on smaller regions where you are getting best performance. You can also consider bayesian hyper-parameter optimization but this can be hard to implement and you should only invest in it as your code base matures.

### Conclusion

So why is trouble shooting so hard? Because there are many competing sources of error. We have to be pessimistic in our approach. It should be an iterative process where we start as simple as possible and then add complexity. Following the steps that were discussed in this talk should make it easier.

## My thoughts

Wow, this talk had such a good structure. It was broken down into itemized parts that were easily digestiable. This talk presented not just a good way to troubleshoot deep learning but a good framework for problem solving in general. Start simple and slowly add in complexity. Break the problem down into different parts.

In his presentation he essentially used topic sentences and transition sentences. At the beginning of every section was an introduction and at the end was a summary. He had one underlying example that he returned to trhough out the talk to ground his higher level theory in a concerete example.  

This talk and the one before it mafe me reflect that we should have more transparency into the traning process of models. It should be easier to replicate them. People should report common bugs in development and how to solve them. 
