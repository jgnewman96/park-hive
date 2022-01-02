---
title: "About This Project"
date: 2020-01-15
tags: []
categories: ['personal']
---

**Check out [repeated generator](https://repeatedgenerator.netlify.app/) for what I am working on in 2022**

The seeds for this project were planted when I was graduating college. I was looking for a way to express myself. I had ideas swirling around in my head but no where to put them. I wanted to write more and also publish my ideas. I was drawn to the idea of starting a blog. I began writing some posts on Medium and explored different structures with my partner Jenny. Here is [our first post](https://medium.com/the-fox-and-the-hedgehog/why-blog-11a7a0c166ef) written in 2018 right after we graduated college explaining why we wanted to blog. We proceeded to [publish a few more posts](https://medium.com/the-fox-and-the-hedgehog) exploring what was on our minds the summer after we graduated. One early theme you can see in these pieces is that we gravitated toward writing about other content we were interacting with. Often the impetus for a piece would be a book that we were reading or a few articles that we had read.

As we both became busier with full time jobs this blog floated into the background. It became difficult to put together pieces and we mostly stopped writing. It felt like pieces had to be polished and there was a fair amount of friction to even getting started. We had to write using Medium's tools and on their website. Writing is a really difficult task and any small fractions can be the difference between writing and just letting ideas float away.

 A [large part of my learning process](/#/internet_reading) is reading from other writers on the internet. I admired people who had their own website and would publish frequently. Websites helped develop writers unique styles and build their voices. Simultaneously I started reading academic papers again. I had notes about each paper but they were just being stored locally on my laptop. A website seemed like a nice way to get myself writing again more. I studied computer science, I should be able to create my own website.

Creating my own website connected a lot of different threads. I was withdrawing from social media, deleting all of my accounts and wanting more ownership of my online presence. I also wanted an opportunity to showcase more about than just my resume. Applying for jobs is a really difficult process and I felt like any resume could only present a narrow view of who I am. A website provides resources to learn more about me in a deeper way.

Through all of my reading I was accumulating a lot of knowledge but was lacking the ability to retain that knowledge or refer back to it. I would read things and then later not be able to find them again. Building a website also seemed like a way to help me retain all of the things I was reading. Both because I would have a written record that I could refer to, but also because it would force me to spend more time writing about what I was reading.

The first iteration of my website was built using [Wordpress](https://wordpress.com/). Using Wordpress was a short lived and failed experiment. I had difficulty learning Wordpress's tools and it felt like there was even more lock in then on Medium. I was constrained by what Wordpress provided and also had to do all of my writing in their tools. After a couple of months I decided to look into static site generators. I found [Hugo](https://gohugo.io/) and switched my site over in about a day using [Netlify](https://www.netlify.com/) to handle deployment. One of the nicest things about Hugo is all the [themes](https://themes.gohugo.io/) that have been developed. Themes make it so easy to create something that looks nice quickly. I used the [Minimal](https://themes.gohugo.io/theme/minimal/) theme and was so much happier about using Hugo rather than Wordpress.

One of the downsides of Hugo being so easy to get started with, was that I never really understood the tooling I was using. Each time I wanted to make a change to my website, I was mostly stumbling around trying out different things until something worked. I did not have a strong grasp over CSS and lacked an understanding of how the website was actually wired together. While Hugo was a a good starting place, I found it difficult to make changes, and when I did, not really understanding why they were working.

There was no real reason for me to leave Hugo though. I had no experience doing front-end development and almost all of the my needs were being met. After reading this [piece about Machine Learning research](http://joschu.net/blog/opinionated-guide-ml-research.html) I started keeping a work journal. The first iteration of this work journal was just a different google doc for each month and a new page for each day. While the process of keeping this journal was helpful, I rarely referred back to it. I was allured by the promise of switching my work journal over to [Roam Research](https://roamresearch.com/). Roam is a tool that is being built for what I wanted to do and Roam promised to make my journaling more accessible. I started taking all of my notes in Roam. Roam was absolutely a better solution but it still presented its own series of problems. My notes had to follow Roam's bullet point format and all of my notes had to exist in two places, both on Roam and on my website. I would take notes on Roam and then if I wanted to make a post on my website I had to reformat the note and move it into my text editor

I started thinking about building tooling that allowed me to do everything I wanted in one my place. I want a very low barrier to taking notes. I want all of my notes / posts to be searchable and connected. I want to then publish them to my website with minimal lift. I want easily extend my website, add new functionality and change how it looks. As I was expressing these ideas to my friend, he told me to read this [article](https://erikwinter.nl/articles/2020/why-i-built-my-own-shitty-static-site-generator/). I connected with a lot of the frustrations expressed in that post.

That post illuminated how our tools impact the way we think. I already knew this to some extent. I have spent a lot of time figuring out my coding set up and optimizing it to improve how I work. But really, my note taking tool and knowledge repository is my most important tool. It is the tool I use the most often and one I am going to use for my entire career. The tool is only going to grow in importance and value the more I use it. It absolutely makes sense for me to optimize this tool for my own use cases.

I decided to build my own website and note taking tool from scratch. I have currently only finished the website part and am still working on the note taking part of it. Building the tool from scratch forced me to learn a lot that I would not have otherwise. I have a much better understanding of CSS and how it interacts with HTML. I learned VueJS and can now build websites or make changes to websites much quicker. When I want to add something to this website it often can be measured in minutes of time rather than days now.

So what is this project? I think it can most aptly be described as my personal [archive](https://en.wikipedia.org/wiki/Archival_science). This website is both the actual archive itself and the tool that helps me create and maintain my archive.

For those interested here is more information about the technical stack of this tool:

- I built the front end using [Vue](https://vuejs.org/). I picked Vue because it seemed the easiest framework to pick up having not frontend experience.
- The backend is built using [Python](https://www.python.org/), [Docker](https://www.docker.com/) and [FastAPI](https://fastapi.tiangolo.com/). These are all tools I have used extensively and know very well. The best part about building this tool myself is that I can use Python to do all the backend.
- I use the javascript library [Showdown](https://github.com/showdownjs/showdown) to parse markdown.
- I developed my own version of sidenotes based on some code from [Tufte-CSS](https://github.com/edwardtufte/tufte-css)
- I use [Coolors](https://coolors.co/) to create the color scheme.
- I use [Goat Counter](https://www.goatcounter.com/) to monitor website usage
- I use [Vercel](https://github.com/vercel/vercel) to handle deployment of the frontend and backend


