---
title: "Building Intelligent Agents That Can Interpret, Generate and Learn from Natural Language"
date: 2019-10-30T10:50:20-07:00
draft: false
tags: ['Reinforcement Learning']
categories: ['Talks']
---
Talk given by [Jacob Andreas](http://web.mit.edu/jda/www/)

## Motivation

Ideally we have systems that understand us in our natural language and can do things. We are beginning to have autonomous agents in the world around us. Both agents in the virtual world such a personal assistants and agents in the physical world like Roombas. We want to build automated agents that can take actions based on natural language

## How do we design agents?

We can break down the agent design problem in the following way. We have a context which consists of our environment and our available actions. And then we have our data which consists of our instructions and supervision.

So imagine we want to teach an agent to navigate our house. The environment would be where in the house is the agent and what do they see nearby. The available actions would be the movements the agent could make. The instructions would be a certain task we wanted to agent to accomplish. For example, "Go sit on the sofa". Lastly, the supervision would be whether or not a series of actions accomplishes the instructions.

Every time an agent takes an action it changes the state. Each action is a transition from one state to another state. The language of the instructions corresponds to a series of actions. It is essentially a machine translation problem of translating instructions into a set of actions.

## Does this approach work? 

We can get fairly far with this approach. One problem with it though is that it treats each state as independent. But generally we will actually need to understand the previous state.

We might have to enrich the state space so that it includes something about completion of certain parts of the instruction. We can do this by adding a state space which corresponds an action to a given part of the instruction. Essentially attention in this machine translation problem. This only works though when the instructions are a series of actions.

What if the instructions were instead a goal?

## Constraints approach

Another approach is that we read the instructions and make constraints of our final state. To do this we take advantage of linguistic structure. Lets look at an example.

"Sit on the chair next to the bed"

What we would do is parse this text into a set of constraints for the final space. The constraints could be:

1. Be sitting
2. Be on a chair
3. Be next to the bed

We then just have to get a series of actions that brings us to a final state that meets those constraints.

But how do we get a language of constraints that is powerful enough to represent everything? How do we know what being sitting is or being next to a chair is?

How can we get all the benefits of the constraint approach with needing all of these pre learned things?

We can change the approach to rather than predicting individual actions we predict the full action set. We have no intermediate logical structure but rather text to a full action set.

## What else can we do with these same tools?

Rather than just training agents we can also do instruction generation. We can take a set of actions and map it to language. We can imagine this is really helpful for navigational guidance.

## My Thoughts

This talk had a really nice flow and was incredibly well motivated. it started out simple and then built up in complexity. It followed a logical thinking pattern and told a story.

This talk seemed to follow a similar recent trend of adding more structure to models. Adding more structure to models can actually help a lot. What can be difficult is how do we pick what structure to add, what level of abstractions do we use?

One thing I was thinking about during this talk was how we often break problems down into smaller problems to solve them. This is often necessary. It is almost impossible to think about really complex problems. But I was playing around with the idea of how using proxy problems can bring us down the wrong rabbit hole.

For example imagine we want to build an intelligent system. So far our approach has been to build very narrowly intelligent system. The hope is by starting here and doing this well, we will eventually learn how to do the harder thing. Is it possible though, that by optimizing the simpler thing, we actually are not taking the best approaches to solve the larger problem.

In the end I would argue yes that is possible, but what else can we really do? We need to have intermediate approaches. We just should keep in mind the larger issue we are actually trying to solve and understand we are using a proxy which might not generalize to the larger issue.

