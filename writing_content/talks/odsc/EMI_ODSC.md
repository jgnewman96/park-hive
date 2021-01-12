---
title: "Embed, Measure and Iterate"
date: 2019-11-01T11:00:03-07:00
draft: true
---

Talk given by Mayank Kejriwal 

Shows the word Quark five dirrenet times --> so what is in a word? nothing at all 
- what is meaning? what is a word? large topic that goes back a long time 
- axiom: you should know a word by the company it keeps

- algorithms are able to take the company a word keeps and then put it into a vector 
- what makes a good embedding? -> things that are similar are close in the space

but what if we want to do it in a down stream task? then we want something that is useful to me

two differenet views, can we use this? vs what does this say about what the world means

skip-gram ->  given the target word we want to predict the context words, the words around it 

continous bag of worlds (CBOW) -> takes the context and then tries to predict the world 
- fill in the blank 
- much more intuitive, more constrained 

actually skip-gram that works pretty well 

Embedding is not only for NLP and words, we can have embeddings 
- image embeddings 
    - one of the last layers of a CNN is essentially an embedding 
    - the very last layer before the categorization 
    - in this situation we use labels rather than neighborhood of words, label is the context
- Document embeddings 
    - converting a document to a vector 
    - bag of words 
    - topic models aka LDA is also an embedding 
- graph or network embeddings 
    - any network with nodes and edges 
    - can still use word embeddings 
    - DEEP WALK algorithm
        - from each node you can do a random walk

how do we evaluate embeddings 
- in vivo and in vitro 
- Example: word sense disambigution -> what is the sense of a word in a sentence 
    - in vitro 
        - given a corpus you have labels 
        - labels the sense of the word 
        - which one does the past on the corpus
    - in vivo 
        - incorporate your embeddings in some larger application 
        - measure impact by how much the embedding helps with the overall task 
the two will not get the same results 

example with word embeddings 
    - man is to woman what king is to ___? 
        - in vitro 
        - word analogy test 

- how would this work with word embeddings or graph embeddings? 
- do we even care about this really? --> can be problematic 

some evaluation questions

- how big of a dataset do I need, is it a general embedding or domain specific embedding 
- how do i transfer embeddings from one corpus to another 
- can I combine big public data with small private data to train embeddings?

Recommended workflow 
1. intilization: start with pre-trained embeddings 
2. measure performance on in vitro task, 
3. if in vitro is decent (define decent for yourself)
    A. integrate embedding model into existing pipeline and do in vivo evaluation 
4. Improve embeddings 
    - add domain specif knowledge 
    - add more context 
    - use some kind of transfer 
    - suprvised embeddings 
5. go back to step 2 

People are trying to embedd everything, representation learning 
- we want to move things into embedding space 

next steps: the web has so much knowledge 
- how do we use all this knowledge to take embeddings to the next level 
- its so heteregenous 
- how do we embed all of this together? 
- if we do this how do we evaluate it? 
- will give best performance for reccomendation? 
- company used to be other words, but now it is also links, videos, photos 
    - how would our embeddings for words change if also add the photos of that thing as a company? 

## thoughts 
- leaving a lot of room for questions is good 





