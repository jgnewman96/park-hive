---
title: "Effective Python"
date: 2021-02-13
tags: ['software engineering']
categories: ['textbooks']
---

By [Brett Slatkin](https://www.linkedin.com/in/bslatkin/)

**Where I found  it**: One of my former co-workers Devon recommended it to me. 

**Why I wanted to read it**: Most of the python I have learned has just been from google things over time. I never took an undergraduate course that involved python. Yet python has been my coding language for the past three years were I am coding a ton every day. This leads to me still googling how to do things fairly regularly and also not having a consistent code style. I was excited about the idea of reading this book because it would give me a cleaner style and take away some of the mental burden when I was coding of knowing how to do something.

* * *

I read __Effective Python__ over about the past six months. It is written in a way to makes it really easy to drop in and out of it and focus on the things that interest you the most. While not all 90 types immediately improved my code there were some that did. Reading the whole book also gave me a better sense of how to write my python code in general. Below is a list of certain things I picked up or started doing after reading this book. 

- I started using list comprehension and dictionary comprehension a lot more.
- When interacting with dictionaries I now use `.get` rather than accessing keys directly in a lot of scenarios
- I also use `defaultdict` with dictionaries. 
- I use generators where I had never done so before. Using `yield` can clean up code a lot
- In general my code has no become a lot ore object oriented using lots of classes
- I create classes that are Callables use the `__call__` method
- I learned to use `__init_subclass__` to have better documented `ABCs`
- I learned a lot more about how to use `async io` and what use cases it works with 

Overall I though __Effective Python__ was a good read and would recommend it for people who are writing python code a lot. 