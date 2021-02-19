---
title: "Expanding Explainability: Towards Social Transparency in AI System"
date: 2021-02-07
tags: ['ai policy']
categories: ['paper']
---

[Paper Link](https://deepai.org/publication/expanding-explainability-towards-social-transparency-in-ai-systems)

By [Upol Eshan](https://www.linkedin.com/in/uehsan/), [Q. Vera Liao](http://qveraliao.com/), [Michael Muller](https://www.linkedin.com/in/michael-muller-a3a3476/), [Mark O. Riedl](https://www.linkedin.com/in/markriedl/) and  [Justin D. Weisz](https://www.linkedin.com/in/jweisz3/)

### Paper Motivation

Previous Explainable (XAI) approaches have been algorithmic centered and not human centered. 

### Paper Contribution

The authors explore the idea of Social Transparency (ST), which takes into account social context when explaining AI. The authors conduct 29 user interviews about a speculative design scenario. The authors develop a framework showing that ST can help improve trust in AI. 

### Background

In human-human interactions explanations are a primary vehicle of knowledge transfer. They play a key role in coordination between people. Explainability in AI systems not only helps with understanding the system but also more effective coordination within the system. Studies have found that current popular XAI techniques are ineffective and underused in real-world contexts. There is a large gap between current XAI techniques and how explanations are actually used by humans. One possible solution to this gap is to use the lense of Critical Technical Practice (CTP). CTP asks us to question the core assumptions in XAI and reflect on them to highlight shortcomings. We bring things that were previously unconscious into the forefront. 

> Put differently, a CTP-inspired reflective perspective on XAI will encourage us to ask: by continuing the dominant algorithm-centered paradigm in XAI, what perspectives are we missing? How might we incorporate the marginalized perspectives to embody alternative technology?

The authors suggest that we need to expand the boundaries of how we think about XAI. We cannot simply focus on the algorithm, but have to think about the algorithm in a social context. Rather than focus simply on transparency the authors ask us to focus our attention on socio-organizational factors. 

### Social Transparency in AI Systems

The authors suggest that adding ST into AI systems will help address an epistemic blind spot of XAI. The authors do not attempt to create a finished treatise on ST but showcase one example of what it might look like. They use a scenario-based design (SBD) method and user interviews to further their understanding. SBD balances roughness and concreteness to allow interviews to have flexibility. 

### User Interviews

The authors decided to create the following situation: You are a salesperson and an AI system is giving you a sales price that it recommends. The end-user is first provided with information that is only about the AI system it self. Then to incorporate ST users were shown information about other users who had interacted with the AI system. Users were then asked to provide their feedback on the incorporation of ST. In the image below blocks 2-5 are the ST portions. 

![Social Transparency](/papers/2021/social_transparency_example.png =90%x*)

### Findings

- Relying on only technical algorithmic transparency is not enough to empower complex decision making. AI systems often do not provide all of the relevant information need to make a decision. After receiving ST sellers lowered their average price from 110 to 73 and increased their confidence out of ten from 6.4 to 8.3 [^1]   
- ST helps calibrate trust in the model by making the AI's past decisions and people's interactions available. [^2]      
- ST provides context about how other users take the AI's information into account. This makes end users more confident in their interactions with the AI by recieving social validation from other users. 
- ST provides organizational context explaining what is acceptable in our organization. It transfers more knowledge about how the organization works with AI and sees the role of AI. It also gives you a contact point so you can reach out to people who previously had interactions to get their thoughts 

### Design with ST

There are four critical parts of including social transparency in a system.

- **WHAT**: Did person accept or reject and was the recommendation successful? The authors assert that this is a must have element. 
- **WHY**: Why did the person make a certain decision? Why comments are helpful but they need to be quality controlled and have a standard. 
- **WHO**: Who information provides end users with a touch point to get the rest of the story. Who is also matters because companies have hierarchies. 
- **WHEN**: Allows user to determine if information is still relevant

### Challenges with Social Transparency

- There is a tradeoff between transparency amd privacy: It makes past performance information available to others. 
- Social Transparency could led to group think and introduce biases. Users might follow what those in higher positions have done. 
- A social transparency tool might lead to information overload without telling the user what is actually important. 

### Overall Implications of Social Transparency

The majority of end users liked the incorporation of social transparency. It made the humans that are involved in the decision making process more concrete. Users were better able to conceptualize their own role in the system. There need to be more work done on which information to show as part of Social Transparency. If the amount of information is very large we cannot show all of it to users. 
     
## My Closing Thoughts

Overall I actually really like the idea of the paper, But I was quite frustrated reading it and wanted the paper to go in some different directions. I think the core idea of the paper is a good one which can be communicated in that one image above. I did not feel like the user interviews added much information and I felt that the paper rhetoric was often lacking. The user interviews only validated that this was a good idea, they did not dig into the challenges. Personally, I did not need this idea to be validated, I saw the image and knew it was an interesting idea that deserved further research. 

The authors did not discuss the downsides of Social Transparency nearly enough. During reading the paper I kept thinking about how it could lead to sub optimal outcomes. One of the big problems is that only certain types of errors are made apparent. For example, in their framing we see the error when people try to sell for too high and get rejected. We do not see the error however when people sell for too low of a price. This type of system therefore could lead to people consistently selling at too low of a price. Or what if the other people in the company are just ignoring the algorithm? Social Transparency could perpetuate that behavior. 

Another odd part of the paper was that they never discuss anything relating to performance metrics. In the image above it provides some explainability information but does not provide performance metrics for the model. If I want to have confidence in a model what I want to look at is the model's performance metrics. If the model performs really well then I will have more confidence. It seems like this is a key part of the equation that the authors ignored. If you have a really good model, then it seems like the social transparency part is less important. Based on the tone of the paper it seems like the authors assumed that the algorithm is inherently bad.
 
Another part of the paper that felt odd to me was that the authors treated the algorithm as static. Generally algorithms are changing over time. Also the recommendations from the algorithm should go back into the model to calibrate it. The Social Transparency data can actually be used to create a better model. If the algorithm is updating this makes the older parts of social transparency less relevant. None of this invalidates the idea of Social Transparency but these are some of the things I wished the authors focused on more. 

There was this whole section of the paper about crew knowledge and how there is undocumented knowledge in the organization. The authors argue that Social Transparency helps with this. But from my perspective at almost every place I have worked a little more effort into documentation goes such a long way. Yes there might always be some crew knowledge but I believe we should push for better documentation. People will use this idea of crew knowledge as an excuse to not do more documentation. In the paper the authors are comparing Social Transparency to a system without Social Transparency. I would be really interested to compare the system they suggest with other types of documentation. Like how do people feel about having nothing, vs having Social Transparency, vs having a [Model Card](https://arxiv.org/abs/1810.03993), vs having a Model Card and Social Transparency.  
    

[^1]: The authors assert that this change is a good one. But is it really? There is no way to tell. This change in behavior might actually be a negative consequence.
[^2]: The authors do not explore other ways to calibrate trust in model. Would people trust a model more if you show them it has high accuracy? Is that a linear relationship?
