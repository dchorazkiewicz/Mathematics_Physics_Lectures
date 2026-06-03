# Task List 1 — Events and Probability (Sample Spaces)

## Visualizing Sample Spaces with Tree Diagrams

Before solving the tasks below, it is often helpful to **visualize the experiment using a tree diagram**.

A **tree diagram** represents a random experiment step by step.

- Each **branch** represents a possible result of a single step of the experiment.
- Each **level of the tree** corresponds to the next stage of the experiment.
- Each **path from the root to a leaf** represents one **elementary outcome**.

This method is especially useful when:

- the experiment consists of **several consecutive steps**,
- **the order of outcomes matters**,
- we want to **construct the sample space systematically**.

In such a diagram:

- the **root** represents the start of the experiment,
- each **branching** corresponds to the possible outcomes of the next step,
- each **leaf of the tree** corresponds to one element of the **sample space**.

---

### Example — Rock–Paper–Scissors Played Twice

Consider an experiment in which a player chooses one of three options:

- Rock ($R$)
- Paper ($P$)
- Scissors ($S$)

Suppose the choice is made **twice in a row**, and the **order matters**.

The experiment can be represented by the following **tree diagram**.

```
START
 │
 ├── R
 │     ├── R
 │     ├── P
 │     └── S
 │
 ├── P
 │     ├── R
 │     ├── P
 │     └── S
 │
 └── S
       ├── R
       ├── P
       └── S
```

Each **path from the root to a leaf** represents one elementary outcome:

$$
(R,R), (R,P), (R,S),
(P,R), (P,P), (P,S),
(S,R), (S,P), (S,S)
$$

Therefore the sample space contains

$$
3 \times 3 = 9
$$

elementary outcomes.

---

### Why Tree Diagrams Are Useful

Tree diagrams help to:

- **construct the sample space step by step**,
- clearly see how the **number of outcomes grows**,
- distinguish experiments **with replacement** and **without replacement**,
- understand what an **elementary outcome** represents.

You are encouraged to **draw tree diagrams for the experiments in the following tasks whenever possible**.

---

### Optional exploration with simulations

Another useful way to understand random experiments is to **simulate them on a computer**.

You are encouraged to experiment with simple simulations, for example by asking an AI assistant or a chat tool to help you create a small **HTML/JavaScript program** that performs repeated random trials.

For instance, you could simulate:

- repeated **coin tosses**,
- repeated **die rolls**,
- repeated **card draws**.

Such programs can generate many outcomes and display the results of the experiment.

This type of computational experiment is commonly known as a **Monte Carlo simulation**.

In a Monte Carlo simulation, the computer performs the same random experiment **many thousands or even millions of times**.  
The results can then be used to estimate probabilities by observing the **relative frequencies of events**.

When running such simulations, you may notice that:

- every run of the program produces a **different sequence of outcomes**,  
- the **observed frequencies fluctuate** when the number of trials is small,  
- but as the number of trials increases, the frequencies tend to **approach the theoretical probabilities** that you compute analytically.

For example, when tossing a fair coin the theoretical probability of heads is

$$
P(H) = \frac{1}{2}
$$

In a simulation of only a few tosses you might observe:

- 7 heads out of 10 tosses,
- or 3 heads out of 10 tosses.

However, if the simulation performs thousands or millions of tosses, the **relative frequency of heads** will typically become closer and closer to \(0.5\).

It will **never match the theoretical value perfectly**, but it will usually **approach it more closely as the number of trials increases**.

When creating your simulations, you may therefore consider adding a feature that allows the program to run **very long Monte Carlo experiments**, so that you can observe how the empirical frequencies gradually approach the theoretical probabilities calculated in the exercises below.

---


## Task 1 — Coin Tossing

Consider an experiment consisting of tossing a **fair coin**.

The order of outcomes matters.

1. Define the **sample space** $\Omega_1$ for **one coin toss**.
2. Construct the **sample space** $\Omega_2$ for **two coin tosses**.
3. Construct the **sample space** $\Omega_3$ for **three coin tosses**.
4. Determine the **number of elementary outcomes** in each sample space.
5. Briefly describe what an **elementary outcome** represents in each case.

---

## Task 2 — Rolling a Die

Consider an experiment consisting of rolling a **fair six-sided die**.

The order of outcomes matters.

1. Define the **sample space** $\Omega_1$ for **one roll of the die**.
2. Construct the **sample space** $\Omega_2$ for **two consecutive rolls**.
3. Construct the **sample space** $\Omega_3$ for **three consecutive rolls**.
4. Determine the **number of elementary outcomes** in each sample space.
5. Briefly describe what an **elementary outcome** represents in this experiment.

---

## Task 3 — Drawing Cards

Consider an experiment consisting of drawing cards from a **standard 52-card deck**.

The order of outcomes matters.
Treat each outcome as an **ordered sequence** of drawn cards.

1. Define the **sample space** $\Omega_1$ for **drawing one card**.
2. Construct the **sample space** $\Omega_2$ for **two consecutive draws with replacement**.
3. Construct the **sample space** $\Omega_2'$ for **two consecutive draws without replacement**.
4. Determine the **number of elementary outcomes** in both cases.
5. Briefly describe what an **elementary outcome** represents in these experiments.

---

## Task 4 — Weekly Weather Observation

The weather on a given day can be classified into **exactly one** of the following states:

- Sunny ($S$)
- Cloudy ($C$)
- Rainy ($R$)

The weather is observed **once per day for seven consecutive days**.

1. Define the **sample space** $\Omega_1$ for the weather observed on **one day**.
2. Construct the **sample space** $\Omega_2$ for **two consecutive days**.
3. Define the **sample space** $\Omega_7$ describing the weather observed during **seven consecutive days**.
4. Determine the **number of elementary outcomes** in each sample space.
5. Briefly describe what an **elementary outcome** represents in the case of a **weekly observation**.

## Task 5 — Buffon's Needle Experiment

Consider an experiment in which a needle of length $L$ is thrown randomly onto a floor with equally spaced parallel lines.  
The distance between neighboring lines is $d$.

1. Describe the **sample space** $\Omega$ of this experiment.

2. Identify the **parameters that determine the outcome of a single throw**.

3. Represent an elementary outcome using appropriate variables describing:

   - the **position** of the needle relative to the nearest line,
   - the **orientation angle** of the needle.

4. Express the sample space $\Omega$ as a **set of possible values of these variables**.
   (You may restrict to $x \in [0, \tfrac{d}{2}]$ for the distance of the needle's center from the nearest line and $\theta \in [0, \tfrac{\pi}{2}]$ for the angle, using symmetry.)

5. Briefly explain why the sample space in this experiment is **continuous**, unlike the sample spaces in the previous tasks.


## Task 6 — Events and Probabilities in Coin Tossing

Refer to **Task 1**, where the sample spaces for one, two, and three coin tosses were defined.

Assume the coin is **fair**, so all elementary outcomes are **equally likely**.

First assign probabilities to all **elementary outcomes** in the sample spaces:

- $\Omega_1$ (one toss),
- $\Omega_2$ (two tosses),
- $\Omega_3$ (three tosses).

Then describe the following **events as subsets of the sample space** and compute their probabilities.

---

### One Coin Toss

Compute the probability of the following events:

- $A_1$ — the result is **heads**,
- $B_1$ — the result is **tails**,
- $C_1$ — the result is **not tails**.

---

### Two Coin Tosses

Compute the probability of the following events:

- $A_2$ — **exactly one head** occurs,
- $B_2$ — **at least one head** occurs,
- $C_2$ — **both tosses give the same result**.

---

### Three Coin Tosses

Compute the probability of the following events:

- $A_3$ — **exactly two heads** occur,
- $B_3$ — **at least one tail** occurs,
- $C_3$ — **all three tosses give the same result**.

---

Finally, define **one additional event** on $\Omega_3$ and compute its probability.


## Task 7 — Events and Probabilities in Die Rolling

Refer to **Task 2**, where the sample spaces for one, two, and three rolls of a fair six-sided die were defined.

Assume the die is **fair**, so all elementary outcomes are **equally likely**.

First assign probabilities to all **elementary outcomes** in the sample spaces:

- $\Omega_1$ (one roll),
- $\Omega_2$ (two rolls),
- $\Omega_3$ (three rolls).

Then describe the following **events as subsets of the sample space** and compute their probabilities.

---

### One Die Roll

Compute the probability of the following events:

- $A_1$ — the result is **even**,
- $B_1$ — the result is **greater than 4**,
- $C_1$ — the result is **at most 3**.

---

### Two Die Rolls

Compute the probability of the following events:

- $A_2$ — the **sum of the results equals 7**,
- $B_2$ — **both results are the same**,
- $C_2$ — the **sum of the results is at least 10**.

---

### Three Die Rolls

Compute the probability of the following events:

- $A_3$ — **the sum of the results equals 10**,
- $B_3$ — **exactly two rolls give the same number**,
- $C_3$ — the outcomes contain **two twos and one three** (in any order).

---

Finally, define **one additional event** on $\Omega_3$ and compute its probability.


## Task 8 — Events and Probabilities in Card Drawing

Refer to **Task 3**, where the sample spaces for drawing cards from a standard 52-card deck were defined.

Assume the deck is **well-shuffled**. In each experiment, every **ordered sequence of draws** is **equally likely** (with or without replacement as specified).

First assign probabilities to all **elementary outcomes** in the sample spaces:

- $\Omega_1$ (one card drawn),
- $\Omega_2$ (two cards drawn with replacement),
- $\Omega_2'$ (two cards drawn without replacement).

Then describe the following **events as subsets of the sample space** and compute their probabilities.

---

### One Card Drawn

Compute the probability of the following events:

- $A_1$ — the card is a **heart**,
- $B_1$ — the card is a **king**,
- $C_1$ — the card is **not a face card** (not J, Q, or K).

---

### Two Cards Drawn (with replacement)

Compute the probability of the following events:

- $A_2$ — **both cards are hearts**,
- $B_2$ — **both cards have the same rank**,
- $C_2$ — **at least one card is an ace**.

---

### Two Cards Drawn (without replacement)

Compute the probability of the following events:

- $A_3$ — **both cards are hearts**,
- $B_3$ — **both cards have the same rank**,
- $C_3$ — **one card is a king and the other is a queen** (in any order).

---

Finally, define **one additional event** on $\Omega_2'$ and compute its probability.

## Task 9 — Events and Probabilities in Weekly Weather Observation

Refer to **Task 4**, where the sample space $\Omega_7$ describing the weather during seven consecutive days was defined.

Each day can be in exactly one of the following states:

- Sunny ($S$)
- Cloudy ($C$)
- Rainy ($R$)

Model the weather as **7 independent days**, where each of the three states occurs with probability $\frac{1}{3}$.

Describe the following events as subsets of $\Omega_7$ and compute their probabilities.

---

### Events

Compute the probability of the following events:

- $A$ — **the entire weekend is sunny** (Saturday and Sunday are both $S$),

- $B$ — **Wednesday, Thursday, and Friday are all rainy**,

- $C$ — **at least one day during the week is sunny**,

- $D$ — **no rainy day occurs during the entire week**,

- $E$ — **exactly two days during the week are sunny**.

---

Finally, define **one additional event** on $\Omega_7$ and compute its probability.


## Task 10 — Events and Probabilities in Buffon's Needle Experiment

Refer to **Task 5**, where the sample space $\Omega$ of Buffon's needle experiment was defined.

A needle of length $L$ is thrown randomly onto a plane with equally spaced parallel lines.  
The distance between neighboring lines is $d$.

Assume $L \le d$. Let $X \in [0, \tfrac{d}{2}]$ be the distance from the needle's center to the nearest line and $\theta \in [0, \tfrac{\pi}{2}]$ the angle between the needle and the lines. Assume $X$ and $\theta$ are independent and **uniformly distributed** on these intervals.

Describe the following events and compute their probabilities.

---

### Events

Compute the probability of the following events:

- $A$ — the needle **intersects one of the lines**,

- $B$ — the needle **does not intersect any line**,

- $C$ — the **angle between the needle and the lines is smaller than $\frac{\pi}{6}$**,

- $D$ — the **center of the needle falls at a distance less than $\frac{d}{4}$ from the nearest line**,

- $E$ — the needle **intersects a line and the angle with the lines is greater than $\frac{\pi}{4}$**.

---

Finally, define **one additional event** in this experiment and compute its probability.
