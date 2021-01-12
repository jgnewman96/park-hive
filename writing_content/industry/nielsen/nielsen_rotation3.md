---
title: 'Rotation 3: Digital Pipeline Development'
date: 2019-10-25T13:40:46-07:00
draft: false
tags: ['Software Engineering']
categories: ['Industry']
---


### Project Description

Nielsen is in the process of transforming how we build our products. We are a ninety five year old company that is not technologically native. We are working on building products that are more maintainable and reducing the amount of work that we duplicate. Data science in particular is undergoing a large transformation within Nielsen. 

Previously, Data Science sat very far away from the final product and a large portion of the data science organization did not have the technical skills to build reliable technical products. The data science organization was very much seen as the place where research happened, but then technology would actually build products. There also would be very minimal day-to-day interactions between data science and technology. Data science would work on a project for a long time and then throw it over the wall to technology. 

Software development is never going to be Data Science's strong suit. The people who are in Data Science have different skill sets and have strengths in a different field. But we can work to develop better engineering skills within Data Science and have data science writing code that goes into production systems. I am working to improve how data science contributes products for the digital and advanced tv team. 

Moving data scientists closer to the product involves changing how we work on a couple of different fronts. One part of it is working with data scientists to improve their engineering skills. Another part of it is creating internal systems that better facilitate development. Another part is working with tech to figure out the best division of labor between the two separate organizations. There will not be a singular panacea that solves everything, but rather we have to work with lots of different individuals to figure out how we can put them in the best situations to succeed. 

### My Contribution

*  One of my big contributions this rotation is rewriting and automating our digital adjustment factors process. Digital adjustment factors is a process for how we adjust our digital numbers based on some known biases in our data. This process used to be highly manual with all of the code being stored in notebooks and someone having to run it manually. I have done all of the following things with the code in an effort to improve this process: 
    *   Taken large SQL queries and turned them into modular testable PySpark 
    *   Written both unit and integration tests for all of our code 
    *   Orchestrated the code using Airflow 
    *   The process is now callable through an API
*   While re-writing the adjustment factor process is a nice win, a large focus has been on using this process to develop learnings that can be used for future projects. I have written extensive documentation about how I automated this process and what best practices would be for future developers. While I was working on this project the beginning was quite slow as I was learning a fair amount. After that I was able to develop quite quickly. The hope is that by using my documentation other developers will be able to have a high velocity in their projects from the beginning. 
*   During this rotation I have also identified that there is a large gap in how we document and track models. I believe that is gap exists across the entire data science industry and not just within Nielsen. All models involve the data scientists making many different assumptions and decisions. We should make the data science process one that is a lot more transparent and accessible to all. I have been working with Nielsen to develop better practices documenting our data science work. 

### What I Learned

*   This rotation was the first time I had to write code that was directly going into one of our existing products. I have had a fair amount of experience writing code with tests, but most of previous experience was writing unit tests. This rotation I learned how to identify and write integration tests. I learned how to incorporate system monitoring into what I am building and how to build something that you can easily debug and identify what is causing issues. 
*   In this rotation it was very important for me to take what I was learning from one process and identify how it could be applied to many different process. I had to continually push myself to think outside of the scope of my project and focus on larger structures. I found that doing this big picture thinking was very helpful in doing better work locally. Connecting my work to larger processes helped me better understand the context of my work and make me more motivated. 
*   I had previously tried to take aspects of agile and incorporate them into my day-to-day but this was the first time I truly worked in an agile framework with sprints and the agile ceremonies. One of the places I see people failing the most with agile is too closely trying to follow the letter of the law. Agile is much more a way of thinking about work and planning rather than an exact script to follow. It is not about doing everything by the book but finding which parts of agile help you the most. 
*   A large part of this rotation has been working with many different teams across both data science and tech. I have had to understand how different people have found their own ideal workflows and identify the commonalities between them. It can be really easy to look at how different people do different things and recognize all the differences. While there will be lots of differences and those are important, we want to let teams and individuals locally optimize, it is just as important to identify the commonalities.  The places where we find a common structure are the places where we can use tools or a structure to help people focus their time. We want people focus their time not on the commonalities but the nuisances and uniqueness of their individual space. 