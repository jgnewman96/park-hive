---
title: "Rotation 2: Bayesian Inference for Ratings"
date: 2019-10-25T13:40:46-07:00
draft: false
tags: ['Machine Learning']
categories: ['Industry']
---

## Project Description

Nielsen is best known for their linear television ratings which estimate the number of people who were watching a channel at any time. This information is estimated using a representative panel of households all across the United States. Households in Nielsen's Panel report all of the television that they watch. Each household's viewing is weight based on its demographics to ensure that the viewing is representative of the population.

While this approach gives an estimate of the number of people who are watching a given channel, there are some problems with it. When there is a show that is very widely watched, such as the Super Bowl, Nielsen's methodology does a good job of accurately estimating the viewership. But for shows with less viewership such as more niche shows or shows during the day time, Nielsen will regularly have no one in the panel viewing those shows. We can expect that the rating is not actually zero, but because the panel does not account for everyone it does a bad job estimating these low viewership shows.

The computational modeling team is exploring a new approach to calculate ratings. The team is exploring using Bayesian Inference to combine panel data with other data sources to create a more accurate estimate of TV viewership. 

### My Contribution

During my time on the computational modeling team my work focused on building tools that let the team iterate faster. I built a couple of different libraries for the team that allowed them to incorporate new data into their models and evaluate their models. I focused on reducing the amount of code that team members had to write and letting them focus on modeling decisions rather than engineering. 

*  I built a library that allowed the team to easily pull third party data. For example this library allowed the team to easily pull census data or weather data. This made it easier for the team to incorporate other data sources into their modeling process.  
*  I built a visualization tool that allowed the team to systematically evaluate their models. This visualization tool consisted of a user interface that allowed the team to understand quickly the success of their models and where their models were failing. The interface also allowed the team to explore feature importance and how different features were driving model output.  
*  The last tool I developed was a library that wrapped the model training process and made it seamless to publish a new model and visualize it. This made it easier for the the team to train a model, visualize it, come up with improvements and then train a new model. 

### What I Learned

This rotation was much more structured than my first rotation. I was working with a team that had already been working on a problem and had a defined direction. I was building software to help enable the team. This was the first time I built software that other people were going to use.

* I learned a lot about how to design software that is extendable and that people will actually use. I learned the real power of object oriented programming and how to use abstract classes. I learned how to make software diagrams and create user stories. I also got first hand experience with the necessity of focusing on your user and involving them in the creation process (how to get feedback from users and incorporating that as I develop). I also learned about how to make different parts of software independent and have them interact through contracts. This rotation taught me a lot about how to build software that people will actually use.  
*  I also learned about how to think about problems in a bayesian way. While I was not doing as much model development, I still had to understand how the team was approaching the problem and what were the advantageous of the new methodology. I learned about how MCMC (markov chain monte carlo) and SVI (stochastic variational inference) work. I really enjoy thinking about problems in terms of a data generating process now and using structural models rather than pure machine learning.
*  A big part of being on the computational modeling team was that we were working in a new space. This meant a lot of reading of recent papers and learning as we go. It is a very different process to apply something that is well established then to apply something that is still being developed. While at times it was difficult to be building something where best practices or approaches had yet to be established, it was quite exciting. 
*  The computational modeling team was based out of New York while I was working in Chicago. Through this process I learned how to best work with a remote team. It is so important to be friends with the people you work with and that is difficult when you are not seeing them  regularly. I learned how to put time into forming remote relationships and to learn about my teammates lives outside of work. 
