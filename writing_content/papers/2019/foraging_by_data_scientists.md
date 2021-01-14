---
title: 'Towards Effective Foraging by Data Scientists to Find Past Analysis Choices'
date: 2019-10-08
draft: false
tags: ['Software Engineering']
categories: ['Papers']
---

[By Mary Beth Kery, Bonnie E. John, Patrick O’Flaherty, and Amber Horvath, Brad A. Myers](https://marybethkery.com/projects/Verdant/Towards_effective_foraging_by_data_scientists.pdf)

## Summary

The authors of the paper present a juypter lab extension called verdant that keeps track of notebook history. The goal of verdant is to to help data scientists answer questions about their research process even if they have not documented everything along the way. The need for this tool is motivated by how messy and non-linear the data scientist process is. Through out the data science process many different things are tried out and it is impossible to record everything. Verdant makes it possible for users to look back through what they did and answer key questions. 

The authors of the paper focus a lot on building an interface that makes information retrieval simple in easy. The tools provides a few different interfaces for information retrieval. They borrow best practices from the information foraging theory to guide their design. One of their key insights is that there is a certain structure behind all data science processes in notebooks and they use that to help guide the information they display. They use the structure of cells, artifacts that the data science has created and the passing of time to make search and retrieval easier. 

The authors evaluate their tool through a set of 15 user interactions with data scientists ay JuypterCon. From this set of interactions the authors verify that their tool helps with information retrieval and get feedback about how to make the tool even better. The authors show that by keeping this history and making it accesible to the data scientist they are able to answer questions about their process which they would not have been able to otherwise.   

## Thoughts

*   This is another example of bringing best practices from other fields. Bringing learnings from another field is always powerful and shows how problems field's face are often quite similar. While the actual task might be quite different, we can learn from how other fields have successfully solved essentially the same problem.
*   Defining a hierarchical structure for the different parts of a data scientists workflow gives the authors a systematic way to structure information. Identifying this underlying structure and then leveraging it is the real key to their paper. Finding this underlying structure is easier when we limit our scope to just notebooks. Notebooks have a defined structure of cells and only a limited number of actions can happen. Finding/defining this underlying structure for a more general purpose data science workflow is a difficult task.
*   A data scientists work happens at many different granularities. There is the scope of an individual coding session. There is the scope of a certain segment of model development such as EDA (exploratory data analysis). We could even think of different sprints as another scope. Verdant helps data scientists with information retrieval at a specific granularity: an individual working session. But what about if a data scientists wants to retrieve information from months ago? Information retrieval and information sharing over a larger scope is still an open problem.
*   Data scientists need a better structure for documentation over the span of an entire project. This paper has key insights about how to find underlying structure in the data science workflow and how to best structure information so that it can be found later. Documentation over the entire workflow will require a more active effort from the data scientists themselves. It will have to be a more active effort of saying this what is important because there is just too much information to passively store all of it. It will need to be a tool that helps lead the data scientists towards best practices of documentation