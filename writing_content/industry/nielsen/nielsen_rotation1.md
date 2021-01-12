---
title: "Rotation 1: Non-coop estimation"
date: 2019-10-25T13:40:46-07:00
draft: false
tags: ['Statistics']
categories: ['Industry']
---

 

## Project Description

Nielsen receives data from retailers about all of the items they sell. For example, Walmart sends Nielsen all of the products sold at each store in the past week. Brands, such as Johnson & Johnson, use this information to see how much of their product is being bought. Some retailers do not send Nielsen their data. We will refer to these retailers  as non-cooperators. Non-cooperators do not send Nielsen their data because the majority of the items they sell are from their own brand. A retailer that is a good example of this is Trader Joe's. Non-cooperators limit Nielsen's ability to give our clients accurate information about market share because there is part of the market that Nielsen cannot see. My project was to develop a new methodology for estimating the sales of non-cooperators. 

## My Contribution

I developed a new methodology that had a 20% improvement in accuracy over Nielsen's old methodology. Estimating non-cooperators' sales is a particular difficult task because there is good reason to believe that non-cooperating stores are fundamentally different from stores that do cooperate. My methodology was based on the principles of how kernel regression works. The methodology works in the following two steps:  

1. Use different features to assign a similarity score between each store 
2. Project a given store's sales using a weighted average of similar stores. 

### What I Learned

This rotation involved a lot of learning for me. It was my first foray into the business world. My project was completely open ended. I was tasked with a business problem and asked to solve it however I wanted to. I learned a lot about how to build a model from scratch, how to define success criteria and how to work efficiently. I discuss some of my main learnings in detail below. 

* Model acceptance is more complicated than just maximizing model accuracy. Models are just one part of a larger complex system. Verifying that a model is worthwhile involves understanding the role that a model plays in that larger system. We have to take into account model simplicity, model explainability as well as how the new model compares to the previous approach. This project was particular difficult because we did not have a truth set that we could use to measure model accuracy. We had to develop a proxy for model accuracy. Validating a model involves using lots of evidence besides just error rate.
* Building off of that point, I learned a lot about how being a good data scientist involves a lot more than being good at building models. It is of critical importance that a data scientist understands the business context and the role that their model plays in it. You have to be a good communicator and understand where different people are coming from. It does not matter if you have built the best model in the world, if it is solving the wrong problem. Building good models is only one skill that determines if you are a good data scientist. 
* This rotation also taught me the importance of understanding our data before beginning the modeling process. Even if a model should work in theory, if there is no signal in the data, even the best model will not be useful. Throughly exploring our data before hand and identifying the key relationships or structure is crucial. If you believe a certain modeling approach will work, find evidence in the data. Use the data to show that the assumptions you are making in the model building process are good ones. All models involve some assumptions. It is important that those assumptions are supported by data. 
* This rotation was the first time I was coding for the majority of the day, every day. I developed much better coding habits. I learned how to write good documentation for both myself and others. I also now understand how to better plan modularity in my code. 
* Meetings can be your best friend or your worst nightmare. Meetings are opportunities to hear other's opinions and get feedback on your work. Truly two of the most important things you can do. Meetings can also suck away all your time and zap your energy. A couple of tactics I have found that make meetings run smoothly: 
    * Clearly state the purpose and agenda of each meeting 
    * Send materials for the meeting ahead of time 
    * Make sure that everyone's voice is heard and that everyone is contributing. Each person should be at the meeting for a reason. 
    * Always take meeting notes and send them as a follow-up afterwards 
    * Meetings are places were decisions should be made and everyone should have action items after a meeting. Make sure actions items are clear and understood. 
