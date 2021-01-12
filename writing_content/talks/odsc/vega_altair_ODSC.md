---
title: "Declarative Data Visualization with Vega-Lite and Altair"
date: 2019-10-31T15:51:05-07:00
draft: false
tags: ['Design']
categories: ['Talks']
---
Talk given by [Dominik Moritz](https://www.domoritz.de/) at Apple/CMU and [Kanit "Ham" Wongsuphasawat](https://kanitw.github.io/) at Apple

## Motivation

So what is declarative data visualization? As programmers we are used to imperative programming. Imperative programming is specifying how to do a problem. For example you say, put a red circle here and put a blue circle there. It couples the specification with the execution. In declarative programming we only specify what should be done. We would say map x and y to specific position, not how to max x and y. This allows us to separate specification from execution. Now the compiler only handles how to do something, not what to do.

Using this approach allows us to focus on the data and the relationships in the data rather than how to visualize something. The speakers than talked through an example with matplotlib. Making a plot is easy in matplotlib, but once we start wanting to add any form of complexity, it gets really tough. Once we start trying to multiple variables and adding legends or titles, the code becomes quite unruly.

Declarative Data visualization is an alternative to matplotlib that should make it easier to work with data. Declarative data viz is inspired by the work of leland wilkerson, [the grammar of graphics](https://www.amazon.com/Grammar-Graphics-Statistics-Computing/dp/0387245448). But what is a grammar? It simply defines primitive building blocks that can be used to make data visualizations.

### Data Visualizartion Building Blocks

1. Data: The input to the visualization
2. Transformations: Different ways to transform the data (eg. filter, aggregation, binning)
3. Mark: A data-representative graphic, (eg. area , point, line, bar)
4. Encoding: A mapping between data and mark properties (eg. color, size)
5. Scale: Functions that map data values to visual values
6. Guides: Axis & legends that help us visualize scale

Using these building blocks the authors have created two libraries Vega-Lite (Javascript) and Altair(Python). These libraries using a grammar of graphics and the above building blocks. These building blocks make it much easier to build powerful and interactive data visualizations. ggplot which many people are already familiar with is a similar style library for R.

The rest of the talk was showing examples of vega and altair. Here is a [link](vega.github.io/editor) to web interface for vega-lite and [github repo](https://github.com/vega/vega-lite-tutorials) with examples of tutorials. In the tutorials they show how easy it is to do things that are quite hard in matplotlib. The showcase how easy it can be to take an altair visualization and then put it into a webpage. Lastly, they showed how easy it is to layer different plots together.

## My thoughts

Data Visualization in general is a very difficult task. There are so many different use cases and finding the right level of abstraction is difficult. In the talk they bring up how matplotlib has histogram has a level of abstraction. This is nice because it makes it really easy to create a histogram. But the speakers argued that histogram is the wrong layer of abstraction, it is not a fundamental building block. But instead using fundamental building blocks, it might make one type of graph harder, but it makes the entire eco system easier to interact with. It also makes it easier to build more complex visualizations. 

This is a classic example of identifying the right layer of abstraction. Doing user studies can be really difficult because user's might not even know what is possible. If you were trying to design a new visualization tool, studying users might give you only part of the story. This is why it can be important to try and predict what the user would want to do, rather than just observe.
