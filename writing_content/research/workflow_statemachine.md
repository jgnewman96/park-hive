---
title: "Workflow State Machine: Letter to Tushar"
date: 2020-04-18T09:47:25-05:00
draft: False
tags: ['Data Science', 'Reflections']
categories: ['Personal']
---

I have been think about my workflow a lot of late decided to write my friend [Tushar](https://tusharc.dev/) a letter. Here is that letter in full.

Hey Tush,

I hope you are getting some good relaxation in this weekend. It is a rainy day here in Baton Rouge so we are trapped inside. I have been thinking a lot about my work flow since reading that [Gelman piece](https://statmodeling.stat.columbia.edu/2020/04/04/toward-understanding-statistical-workflow/) post I forwarded you. I always find bouncing ideas off you to be really helpful. I have learned a lot from seeing and talking with you about your workflow. Here are some assorted thoughts, respond to whatever interests you.

When I am working on a more strictly engineering task my workflow is a lot better and I am in a much better headspace than when modeling. This relates a lot to the [debugging post](https://tusharc.dev/posts/debugging_attitude.html) you made last week. My thinking is much more systematic and defined when I am working on an engineering task. With engineering, I am able to build it up piece by piece, isolate different parts and have a good understanding of each part. It also feels like I am making tangible progress as I go.

My head space and process when I am modeling is much more chaotic. I will often just try something out and see if it improves my optimization metric. Very similar in a lot of ways to what you describe in your post. I do not reason about why making this change is important or what the significance of a parameter is. I just change the parameter hoping it will help.

I have been thinking about this bad tendency for a while now.  I wrote a [post](
{{< ref  "/writing/personal/model_building.md"  >}} )  earlier this year about how incorporating the scientific method might help. Here is a snippet from that piece which I think is pertinent.

> We see the promise and potential of automating a task and forget to be systematic thinkers. We forget the larger goals and focus on one metric. There is a metric we can measure, so we optimize it. ...... It is harder to measure how much of a system we understand than accuracy on a defined task. Our goal should be understanding of a system rather than optimizing a certain metric. Model building should be a process of using the scientific method to better understand the driving forces in the world around us.

My suggestion of using the scientific method was derived from two factors.
    1. The scientific method forces us to focus on understanding rather than specific metrics
    2. The scientific method provides a desirable workflow structure

Just knowing that the scientific method will help me has proven not enough to fix some of my bad habits. I will sometimes get into a good flow of defining hypothesis and then testing them out. I find that this is often when I will make the most progress on model iteration. As a bonus it also usually helps me find bugs in my code. But often I still abandon this process and focus on the one or two metrics I have defined.

* * *

Here are two thoughts about more changes I can make to my workflow

1. Building Model Understanding Functionality Early

Model understanding and interpretation should be a more integral part of my workflow. When I am evaluating a model it should focus less on the optimization metric. It should focus more on what the model is learning. I should build functionality that lets me see which features are important and how different features interact. I should then compare this to my a priori hypothesis and trends in the raw data. If I build this functionality it makes the scientific method structure a lot easier. I will have an understanding of how changes impact what my model is learning rather than the impact on the optimization metric.

2. Using State Machines

This idea is less concrete but has the potential to be more powerful. My thinking is *more systematic* if there is *more structure* in what I am working on. When my task is more narrowly defined it becomes a lot easier to wrap my head around. A couple of week ago Pointer contained an article about [state machines](https://blog.yoshuawuyts.com/state-machines/). I believe a modeling workflow can be defined using a state machine. This state machine would break the process into smaller parts a give the process more structure.

 A state machine is a graph that defines the possible states a process can be in. The article explains "State machines not only encode which transitions are valid, in doing so they also encode which transitions are invalid."

Why would using a state machine to model my workflow be so helpful? That state machine could enforce certain good practices and restrict bad habits. I would be forced to document before moving on to the next thing. Here is a very basic diagram of what a modeling workflow state machine could look like.

<center>

<img src="/img/writing/model_workflow.jpg" width="600">

</center>

This diagram is quite simplistic but a useful starting point. There are probably more states and more cycles within the graph. Each red circle represent a state and then the blue squares represent an action that must be taken before transitioning states. It might even be possible to define sub state machines for each state, so model evaluation could have its own state machine.

This diagram is illustrative because it highlights some of of the underlying structure in our workflows. While each practitioner will have their own tendencies there is some structure that workflows will follow. By making restrictions on this workflow we can help enforce good practices and remove bad practices.

I have some more thoughts related to all of this centering on documentation and information retrieval, but we can get to those later.

Respond to whatever interests you most but here are a couple questions to get the blood flowing:

1. What type of structures or frameworks do you use when modeling to help guide your thinking?
2. What tools / information do you find to be the most helpful in model understanding?
3. What am I missing with my State Machine representation? Not in terms of which states or connections, but the overall structure?

Thinking of you Tush! Hope you are doing well.

Judah
