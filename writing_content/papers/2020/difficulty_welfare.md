---
title: "A Difficulty in the Concept of Social Welfare"
date: 2020-07-27T11:59:27-04:00
draft: False
tags: ['Economics']
categories: ['Textbooks']
katex: true
---

I had waited to read this classic paper [By Kenneth Arrow](https://www.stat.uchicago.edu/~lekheng/meetings/mathofranking/ref/arrow.pdf) for a long time now. Since I started working in the political sphere I have been interested in how to best represents people's opinions and how to aggregate them. This paper is so impressive because it works directly from first principles and makes all of its assumptions quite clear.

Arrow begins by asserting there are two methods by which social choices can be made in a democracy. __Voting__ and a __Market Mechanism__. These are methods of aggregating individuals wills to make a collective social decision. Outside of a democracy there are some other ways social choices can be made: dictatorship, convention. In these other methods there is no conflict between different individuals wills. This paper is concerned with voting

Here is an example of voting to ground our thinking. We have a community of three voters and they must choose among three alternative Each person ranks the three choices by their preference.
- At a community level, we prefer option A to B if a majority of the community prefers option A over option B
    - Individual 1 Ranking: A > B > C
    - Individual 2 Ranking: B > C > A
    - Individual 3 Ranking: C > A > B

- A majority of the community prefers A over B, prefers B over C and prefers C over A. The focus of the will be how to effectively aggregate individual preferences to maintain certain desired behavior
- One example of a desired behavior &rarr; Transativity, e.g. If A is preferred to B and B preferred to C, then A should be preferred to C. We can ensure this at the individual level, but it might fall apart in aggregate. The above example shows this.

If just simple aggregation as in the above example does not satisfy our desired conditions, Are there better ways of aggregating individual preferences?

* * *

Economics is generally concerned with how to achieve a social maximum outcome derived from individual desires. But the search for a clear definition of social optimum is difficult. Economics has used a weaker definition in the post: **no individual can be made better off without making someone worse off**.

But this definition does not suffice for social policy. There are many policies that will satisfy the above condition and we must find a way to differentiate between them

***

{{< quote >}}

For any method of deriving social choices by aggregating individual preference patterns which satisfies certain natural conditions, it is possible to find individual preference patterns which give rise to a social choice pattern which is not a linear ordering

{{< /quote >}}

The above quote is effectively the thesis of this paper. There is no way to aggregate individual preferences to maintain certain desired behavior. This desired behavior will be outlined shortly.

Arrow is going to prove the above argument from the ground up. Lets define the problem:

### Problem Setting

We have a set of possible choices S. We need to pick one choice from S which.

- Within two values in the set we have three options X > Y, X = Y or X < Y.
- In our final ranking we want the following things to be true
    - For all X, X >= X
    - If X > Y, then X >= Y
    - if X > Y and Y > Z then X > Z - transitive property
    - if X = Y and Y = Z then X = Z
    - Either X >= Y or Y > X
    - if X > Y and  Y >= Z then X > Z
- If for all pairs of preferences we know which one is preferred, then we know the entire preference scale

- let \\(R_I\\) be the ordering relation of social states for individual let \\(R\\) be the ordering relation for the society
    - \\(R\\) depends on the ranking by all individuals \\(R_1 ..... R_n\\) where n is the number of individuals in the community
- We assume that individuals are rationale meaning there conditions follow the above constraints
    - We want to take the preferences from individuals and make an ordering among the states that is also rationale for society

The **Social Welfare Function** maps \\(R_1 ..... R_n\\) to \\(R\\). There are five conditions we want our social welfare function to meet
1. The social welfare function must be defined and deterministic for all possible individual orderings
2. If X > Y and then X either rises or does not fall in the ordering of each individual X > Y - __Positive association of social and individual values__
    - This condition does not hold for rank ordering:
        - Example: Three voters with four candidates (x, y, z, w)
        - first choice = 4 points, second choice = 3 points etc
        - Individual 1 and 2: X > Y > Z > W
        - Individual 3: Z > W > X > Y
        - Final Tally: X: 10,  Z: 8 Y: 7, W: 5
        - Now imagine candidate Y dies, we should by the above property maintain the same results. X either rises or does not fall. But we do not. Instead we get a tie Between Z & X
        - X: 7, Z: 7, W: 4
3. if the relationship between  X and Y is the same in two different orderings, then the social decision between X and Y must be the same - __The Independence of irrelevant alternatives__
4. Our social welfare function cannot be imposed. Imposes means that X >= Y regardless of individuals preferences  - __The condition of citizens sovereignty__
5. Our social welfare function cannot be dictatorial. Dictatorial means there exists an individual i such that the ordering of the group is always the same as individual i's ordering. - __The condition of non-dictatorship__

**The Possibility Theorem**: It will be shown that there is no social welfare function that satisfies conditions 1-5. These conditions lead to a contradiction.

***

### Prove

We will proof the possibility theorem by example. We have two individuals with three options, x, y and z. Individuals are 1 and 2 with orderings \\(R_1\\) and \\(R_2\\). Our proof will go by laying out a list of consequences of our conditions until we reach a contradiction

**Consequence 1**: If both rank x > y, then society as a whole prefers x > y
- By condition 4: there must be an ordering where X > Y for the society
- By Condition 2: If we raise X to the top of the ordering without changing anything then X will still be > Y.
- By Condition 3: Since the choice only depends on X relative to Y if X > Y for all individuals then X > Y

**Consequence 2**: if P1 has X > Y and P2 has Y > X, while society has X > Y  then whenever P1 has X > Y ,  society must have X > Y

e.g. If the will of person 1 prevails over 2, that will be the case still if 2 is indifferent or agrees with 1

- Take X for P2 and put it at the bottom of their list. If in this situation society prefers X > Y then by condition 2 if X moves any higher in P2‘s list society will still prefer X > Y.

- But what if we have a situation like the following.  P1 has X > Y > Z and P2 has Z > Y > X. Society has X > Y.  If P1 moves X down to Z > X > Y why does Society still need X > Y?
    - By condition 3, if the ordering is the same then the societal outcome must still be the same

**Consequence 3**:  If P1 has X > Y and P2 has Y > X  then X = Y

e.g. If the two individuals have exactly opposing interests on the choice between two alternatives society will be indifferent

Proving this one is going to be a doozy, and will show where a contradiction comes in.

We will prove this by contradiction. Suppose the above is not true. This mean either X >= Y or Y >= X. This would lead to a contradiction.

Assume we have P1: X >= Y and P2:  Y >= X and society X >= Y
- Consequence 2 Will hold. This means if P1: X >= Y and P2:  Y >= X  society will X >= Y. Lets now walk through some scenarios.

- P1:  X > Y > Z P2: Y > Z > X -> Society: X > Y > Z
    - New Consequence -> __p1: X >= Z and P2: X <= Z and Society must X >= Z__.
    - By consequence 2 the above has to hold.

- P1:  Y > X > Z, P2 : Z > Y > X, Society: Y > X > Z
    - Everyone prefers Y > X and the above consequence for X > Z .
    - Consequence ->  P1: Y >= Z and  P2: Z <= Y then Society Y>= Z

- P1: Y > Z > X P2 Z > X > Y -> society: Y> Z > X
    - Everyone prefers Z > X  and the above consequence for Y > Z
    - New Consequence: If P1: Y >= X and  P2: Y <= X -> Society  Y >= X
- P1: Z > Y > X, P2: X > Z > Y -> Society: Z > Y > X
    -  Everyone prefers Z > Y and the above consequence Y >= X
    -  New consequence : If P1: Z >= X and P2 X<= Z -> Society Z >= X
- P1: Z > X > Y: P2: X > Y > Z -> Society: Z > X > Y
    -  Everyone prefers X > Y  and the above consequence for Z > X
    -  New consequence: If P1: Z >= Y and P2: Z <= Y --> Society Z > Y
- By all of these consequences individual 1 is a dictator. Therefore the consequence must be false, therefore consequence 3 is proved

- Last Scenario
    - P1: X > Y > Z, P2: Z > X > Y
        - X > Y in all rankings
        - Y = Z by Consequence 3
        - X = Z By Consequence 3
        - X cannot be both indifferent and greater than consequence 3
- There is no social welfare function that satisfies conditions 1 - 5

***

### Implications of the possibility theorem

{{< quote >}}
If consumers values can be represented by a wide range of individual orderings, the doctrine of voters sovereignty is incompatible with that of collective rationality
{{< /quote >}}



{{< quote >}}
The failure of purely individualistic assumptions to lead to a well-defined social welfare function means, in effect, that there must be a divergence between social and private benefits if we are to be able to discuss a social optimum
{{< /quote >}}



## Thoughts

I was interested in reading this paper partly for the ideas expressed in it, but also because of how influential of a paper it is. I wanted to understand what made it such an influential paper. I was also interested in what reading a paper from the 1950s would be like.

One of the most striking aspects of the paper is how little reference there is to related work. When I read more modern papers it is often essential to understanding the other surrounding literature. Each paper is in dialogue with the papers that came before it. While this is still true for this paper, it is very much a response to other work happening at the time, it does not take previous research as given.

Arrow build his argument from pure fundamentals. He also does it in an approachable way. His prove can be understand because it is an example that is easy for us to wrap our heads around.

When I first read the paper, I was like this is kind of silly. Conditions 2 and 3 seems to be what makes the paper hold together. While I can understand why those conditions might be desirable, they do not seem necessary to me. But when you start thinking about what it would mean for those conditions not to hold, the paper makes more sense. If we took away conditions 2 and 3 then the social welfare function could start doing some really funky things.

It is in some ways surprising that the way we present research in 2020 is the same as it was in 1950. I would have imagined that 70 years of technological progress would have lead to a better way to present research findings.
