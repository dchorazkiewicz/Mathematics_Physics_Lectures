# Task List 06 — Algebra of Events and Conditional Probability

## Problem 1 — Event algebra from a two-way table

A university collected data about students’ study habits.

| Student type               | Submits homework on time | Does not submit on time | Total |
| -------------------------- | -----------------------: | ----------------------: | ----: |
| Attends lectures regularly |                       48 |                      12 |    60 |
| Does not attend regularly  |                       22 |                      18 |    40 |
| Total                      |                       70 |                      30 |   100 |

Let:

$$
A=\text{the student attends lectures regularly},
$$

$$
B=\text{the student submits homework on time}.
$$

1. Fill in the probabilities of the four disjoint regions:

$$
A\cap B,\quad A\cap B^c,\quad A^c\cap B,\quad A^c\cap B^c.
$$

2. Use these four regions to compute:

$$
P(A),\quad P(B),\quad P(A\cup B).
$$

3. Compute:

$$
P(A\mid B),\quad P(B\mid A).
$$

4. Are $A$ and $B$ mutually exclusive? Explain briefly.

5. Are $A$ and $B$ independent? Explain briefly.

6. Interpret $P(A\mid B)$ and $P(B\mid A)$ in words.

---

## Problem 2 — Four regions of a sample space

A company classifies support tickets according to two properties:

* whether the ticket is technical,
* whether the ticket was solved during the first contact.

The data are:

| Ticket type   | Solved during first contact | Not solved during first contact | Total |
| ------------- | --------------------------: | ------------------------------: | ----: |
| Technical     |                          90 |                              60 |   150 |
| Non-technical |                         160 |                              40 |   200 |
| Total         |                         250 |                             100 |   350 |

Let:

$$
T=\text{the ticket is technical},
$$

$$
S=\text{the ticket was solved during the first contact}.
$$

1. Fill in the probabilities of the four disjoint regions:

$$
T\cap S,\quad T\cap S^c,\quad T^c\cap S,\quad T^c\cap S^c.
$$

2. Verify that these four probabilities add up to $1$.

3. Use the four regions to compute:

$$
P(T\cup S),\quad P(T^c\cup S).
$$

4. Compute:

$$
P(S\mid T),\quad P(S\mid T^c).
$$

5. Does being a technical ticket change the probability of being solved during the first contact? Explain briefly.

---

## Problem 3 — Conditional probabilities are not symmetric

An online course platform records whether users watched a lecture and whether they passed a quiz.

| User behavior         | Passed quiz | Did not pass quiz | Total |
| --------------------- | ----------: | ----------------: | ----: |
| Watched lecture       |          72 |                18 |    90 |
| Did not watch lecture |          28 |                32 |    60 |
| Total                 |         100 |                50 |   150 |

Let:

$$
W=\text{the user watched the lecture},
$$

$$
Q=\text{the user passed the quiz}.
$$

1. Compute:

$$
P(Q\mid W),\quad P(W\mid Q).
$$

2. Compute:

$$
P(Q\mid W^c),\quad P(W\mid Q^c).
$$

3. Explain why $P(Q\mid W)$ and $P(W\mid Q)$ answer different questions.

4. Which probability is more useful if we want to know whether watching the lecture helps?

5. Which probability is more useful if we want to describe users who passed the quiz?

---

## Problem 4 — Inclusion–exclusion and double counting

A company surveyed 200 employees about two software tools.

* 130 employees use Tool A,
* 90 employees use Tool B,
* 60 employees use both tools.

Let:

$$
A=\text{the employee uses Tool A},
$$

$$
B=\text{the employee uses Tool B}.
$$

1. Compute:

$$
P(A),\quad P(B),\quad P(A\cap B).
$$

2. Use inclusion–exclusion to compute:

$$
P(A\cup B).
$$

3. Compute the probabilities of the three remaining regions:

$$
A\setminus B,\quad B\setminus A,\quad A^c\cap B^c.
$$

4. Compute:

$$
P(A\mid B),\quad P(B\mid A).
$$

5. Explain why:

$$
P(A\cup B)\neq P(A)+P(B).
$$

6. Which group is counted twice in $P(A)+P(B)$?

---

## Problem 5 — Independence from data

A streaming platform records whether users have a premium account and whether they watched a movie during the last weekend.

| Account type | Watched a movie | Did not watch a movie | Total |
| ------------ | --------------: | --------------------: | ----: |
| Premium      |              84 |                    36 |   120 |
| Free         |              56 |                    24 |    80 |
| Total        |             140 |                    60 |   200 |

Let:

$$
A=\text{the user has a premium account},
$$

$$
M=\text{the user watched a movie during the weekend}.
$$

1. Compute:

$$
P(A),\quad P(M),\quad P(A\cap M).
$$

2. Compute:

$$
P(M\mid A),\quad P(M\mid A^c).
$$

3. Decide whether $A$ and $M$ are independent.

4. Explain in words what independence means in this situation.

---

## Problem 6 — Dependence from data

A delivery company records whether a parcel is international and whether it is delayed.

| Parcel type   | Delayed | Not delayed | Total |
| ------------- | ------: | ----------: | ----: |
| Domestic      |      24 |         376 |   400 |
| International |      36 |         164 |   200 |
| Total         |      60 |         540 |   600 |

Let:

$$
I=\text{the parcel is international},
$$

$$
D=\text{the parcel is delayed}.
$$

1. Compute:

$$
P(I),\quad P(D),\quad P(I\cap D).
$$

2. Compute:

$$
P(D\mid I),\quad P(D\mid I^c).
$$

3. Are $I$ and $D$ independent? Explain briefly.

4. Does international shipping increase the probability of delay?

5. Compute:

$$
P(I\mid D).
$$

6. Explain the difference between $P(D\mid I)$ and $P(I\mid D)$.

---

## Problem 7 — Conditional probability with three categories

A company classifies customers into three activity levels:

* high activity,
* medium activity,
* low activity.

It records whether they renewed their subscription.

| Activity level | Renewed | Did not renew | Total |
| -------------- | ------: | ------------: | ----: |
| High           |      80 |            20 |   100 |
| Medium         |      90 |            60 |   150 |
| Low            |      30 |           120 |   150 |
| Total          |     200 |           200 |   400 |

Let:

$$
H=\text{the customer has high activity},
$$

$$
M=\text{the customer has medium activity},
$$

$$
L=\text{the customer has low activity},
$$

$$
R=\text{the customer renewed the subscription}.
$$

1. Explain why $H$, $M$, and $L$ form a partition of the sample space.

2. Compute:

$$
P(H),\quad P(M),\quad P(L).
$$

3. Compute:

$$
P(R\mid H),\quad P(R\mid M),\quad P(R\mid L).
$$

4. Use the law of total probability to compute:

$$
P(R).
$$

5. Compute:

$$
P(H\mid R),\quad P(M\mid R),\quad P(L\mid R).
$$

6. Interpret the difference between $P(R\mid H)$ and $P(H\mid R)$.

---

## Problem 8 — Bayes’ formula from a table

A fraud detection system classifies transactions as suspicious or not suspicious.

The historical data are:

| Transaction type | Marked suspicious | Not marked suspicious | Total |
| ---------------- | ----------------: | --------------------: | ----: |
| Fraudulent       |                98 |                     2 |   100 |
| Legitimate       |               297 |                  9603 |  9900 |
| Total            |               395 |                  9605 | 10000 |

Let:

$$
F=\text{the transaction is fraudulent},
$$

$$
S=\text{the transaction is marked suspicious}.
$$

1. Compute:

$$
P(F),\quad P(S\mid F),\quad P(S\mid F^c).
$$

2. Use the law of total probability to compute:

$$
P(S).
$$

3. Use Bayes’ formula to compute:

$$
P(F\mid S).
$$

4. Among suspicious transactions, are most transactions fraudulent or legitimate?

5. Why can this happen even if the system detects fraudulent transactions very well?

6. Explain the role of the base rate $P(F)$.

---

## Problem 9 — Law of total probability without a full table

A company receives orders through three channels:

* website,
* mobile app,
* phone.

The proportions of orders are:

$$
P(W)=0.50,
$$

$$
P(A)=0.35,
$$

$$
P(H)=0.15.
$$

The probability that an order is cancelled depends on the channel:

$$
P(C\mid W)=0.04,
$$

$$
P(C\mid A)=0.06,
$$

$$
P(C\mid H)=0.10.
$$

Here:

$$
W=\text{the order came through the website},
$$

$$
A=\text{the order came through the mobile app},
$$

$$
H=\text{the order came by phone},
$$

$$
C=\text{the order is cancelled}.
$$

1. Explain why $W$, $A$, and $H$ form a partition of the sample space.

2. Use the law of total probability to compute:

$$
P(C).
$$

3. Compute:

$$
P(W\mid C),\quad P(A\mid C),\quad P(H\mid C).
$$

4. Which channel is most likely among cancelled orders?

5. Is this necessarily the channel with the highest cancellation rate? Explain.

---

## Problem 10 — Comprehensive problem: event algebra, conditioning, independence, and Bayes

A company studies whether users complete an online onboarding process.

Users are divided into two groups:

* users who received a tutorial,
* users who did not receive a tutorial.

The data are:

| Group             | Completed onboarding | Did not complete onboarding | Total |
| ----------------- | -------------------: | --------------------------: | ----: |
| Received tutorial |                  180 |                          70 |   250 |
| No tutorial       |                  120 |                         130 |   250 |
| Total             |                  300 |                         200 |   500 |

Let:

$$
T=\text{the user received the tutorial},
$$

$$
C=\text{the user completed onboarding}.
$$

1. Fill in the probabilities of the four disjoint regions:

$$
T\cap C,\quad T\cap C^c,\quad T^c\cap C,\quad T^c\cap C^c.
$$

2. Use these four regions to compute:

$$
P(T),\quad P(C),\quad P(T\cup C).
$$

3. Compute:

$$
P(C\mid T),\quad P(C\mid T^c).
$$

4. Compute:

$$
P(T\mid C),\quad P(T\mid C^c).
$$

5. Are $T$ and $C$ independent? Explain briefly.

6. Does receiving the tutorial appear to change the probability of completing onboarding?

7. What is the difference between:

$$
P(C\mid T)
$$

and

$$
P(T\mid C)?
$$

8. Write a short interpretation of the result in words.
