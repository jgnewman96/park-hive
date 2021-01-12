---
title: "AI & OR for Social Good"
date: 2019-11-01T14:51:30-07:00
draft: true
tags: ['ODSC']
---

[Phebe Vayanos](https://sites.google.com/usc.edu/phebevayanos/)

CASE - center for AI and society 

general approach: 
- discussion with community partners and policy makers 
- what is the question that keeps you up at night 
- what is a problem and what data do we need
- model it as a mathematical optimization problem 
- optimize something subject to some constraints 

often cannot solve it as is, real world problem is tough 
- reframe problem as tractable approximation 

once we come up with a solution we deploy it and evaluate the solution in the field 

then we talk with community partners again and iterate 

* * * 

intervations are one of two categories 
first type 
    - systems that take the form of a waitlist, individuals of different types 
    - we also have different types of resources 
    - housing resources and people who need houses 
    - allocating resources to people on the waitlist 
    - how long am i going to have to wait for my resource 
    - another example is kindey transplant 

second type 
    - social network 
    - try to improve substance abuse prevention 
    - segment the group and use the other people to do social network preventions 

* * * 

common characteristics of problems 
1. most of the work takes place under uncertainity 
- we do not know what is going to happen 

2. dynamic environments information will change over time 

3. problems are often quite large scale, need to make many decisions at the same time 

4. data - to improve decision making 

heteregenous population, hetergenous resources and socially sensitive settings 
- the need for fairnes and personalization 

* * * 

examples of five projects  

1. estimating wat times for recieving a scarce resource   
 - partner massachusters general hospital 
 - end stage renal disease in the US > 600,000 patients in the US 
 - prefered treatment is kidney transplant, better than dialysis 

 - focus on decesed donors 

 we have a severe organ shortage 

 100k patients waiting 
 36k added each year 
 19k transplants done a year 

 relatively this is FIFO problem 

 people reject an offer when they believe they can get a better kidney 

 we want to make a personalized estimate of wait time 

 - given patient with blod type x with a given rank how long until he recives a particular quality kidney 

 - knowing this time can help us make better decisions 

 - we want to make an interpretable decision

 Challenges: 
 - just predicting whether or not someone accepts or rejects is quite hard 
 - in practice it is very hard, because we do not know who is in front 

 inject a little bit of modeling to go with the data 

 we can think of this as a multiclass multiserving queuing issue 
 - what type of kidney you are willing to accept makes you in a certain class 

 not one queue but queues based on which kidney you are willing to accept 

 different quality of kidneys and different individuals 

 determine wait time of a certain patient

 we do not know the spped at which kidneys are going to be arriving 
 we also do not know how many people are in each queue 
 - we know the total people in the queue, by current rank 
 - we also do not know the sequence in which people arrived 

 we want to compute the clearing time of your queue, this is a function of all of our unkowns 

 very tough problem in applied probability 

 robust omptimization --> instead of building probability distributions, we build uncertainity sets 

 try to find worst case amount of time it will take 
 for all of unkown parameters lying in this uncertanity sets 
 we use the data to make these uncertainity sets 
 these values lie in this region with some uncertainity 

 takes an NP-hard problem and makes it a MILP (Mixed integer linear programming)

 took this and applied it to pennsalyvania 
 - works better than just estimating averagr 

 this was individual in system how long do i have to wait 

* * * 

if i am a policy maker how do i allocate resources 

core motivation is homelessness in LA 

more homeless than their our housing resources 

whenever a new person comes into the system score them , ask them a bunch of questions 
- how likely are they to exit homelessness at their own 
- most vulnerable gets the most housing 
- least vulnerable get the least resources 

this policy is not tied to outcome 
no tieing to resource actually helping someone 

want to design holistic system to actually help 

first want to understand what policy makers want out of their system 

try to predict how likely someone is to leave homeless ness 

policy design in combing those two 

first is to learn policy makers preferences 
- fairness, efficient, interpretable 

these are great but what do these even mean 

how do we balance the trade offs between them 

preference elicitation from policy makers, ask them questions and see what they prefer 
- show them two outcomes see what they actually prefer 

- we get their preferences from asking them question and learning their prefences 

a ton of possible preferences, how do we narrow this down 

adaptive elication 
- ask question, observe answer, pick next question to ask and so on 

once we have lerned perferences we can actually optimize policy 

each time a new resource arrives we want to determine who gets the resource 

once again we queues with people who are in queues
decision tree approach so that it is interpertable 
we also want it to be fair 

* * * 

suicide preventation 

who should we give trainings too for suicde prevention 

can social network information be leveraged to make these interventions more effective 

- uncertainity in avaliability and performance of students 
- limited data to inform us 
- network makes a combinatorial explosion 




## my thoughts 

- why adding structure is so helpful 
- interpretability 
- simplfying system 
- understanding of system 
