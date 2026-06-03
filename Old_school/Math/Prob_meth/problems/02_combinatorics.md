# Task List 02 — Combinatorics for Probability

## Introduction

Many probability problems start by counting outcomes: the size of a sample space, the number of favorable outcomes, or the number of possible codes or arrangements. The main difficulty is usually not the formula, but recognizing which counting model applies.

In this task list you will practice:

* identifying the correct counting model,
* translating a problem description into a precise outcome type,
* using the model to count outcomes in probability contexts.

## Key Counting Questions

Before choosing a formula, decide:

1. Does **order** matter?
2. Are we using **all objects** or only **some of them**?
3. Are **repetitions allowed**?
4. Are objects **distinguishable** or **indistinguishable**?
5. What kind of outcome are we describing?
   * a set,
   * a sequence,
   * a linear arrangement,
   * or a circular arrangement?

## Decision Tree for Choosing a Model

The following flowchart provides a quick procedure for identifying the correct counting model.
Students can apply these questions directly when solving exam problems.

```text
START

Are we using ALL objects?

 ├─ YES
 │
 │   Are objects arranged in a circle?
 │
 │   ├─ YES → Circular permutation
 │   │
 │   └─ NO
 │        │
 │        Are some objects identical?
 │
 │        ├─ YES → Permutation with repeated elements
 │        │
 │        └─ NO  → Permutation
 │
 └─ NO (only SOME objects)
     │
     Does order matter?
     │
     ├─ NO  → Combination
     │
     └─ YES
          │
          Is repetition allowed?
          │
          ├─ YES → Sequence with repetition
          │
          └─ NO  → k-permutation
```

When solving a counting problem, students should answer a small sequence of questions:

1. Are we using **all objects or only some of them**?
2. Does **order matter**?
3. Is **repetition allowed**?
4. Are some objects **identical**?

The answers determine which combinatorial model applies.

## Overview of Counting Models

Selections: **combination** (unordered), **k-permutation (ordered selection without repetition)**, **sequence with repetition**.

Arrangements of all objects: **permutation**, **circular permutation**, **permutation with repeated elements**.

---

## Permutations

A **permutation** is an arrangement of all elements of a set, where order matters.

If a set contains $n$ distinct elements, then the number of permutations is

$$
P_n = n!
$$

Permutations are used when:

* all available objects are arranged,
* order matters,
* repetitions are not allowed.

Typical examples:

* arranging books on a shelf, 
* seating people in a row, 
* ordering questions in a test.

---

## Circular Permutations

When objects are arranged in a circle, rotations may represent the same arrangement.

If $n$ distinct objects are arranged around a circle and only relative position matters, then the number of circular permutations is

$$
(n-1)!
$$

This model is used when:

* objects are arranged around a round table, 
* absolute position is irrelevant,
* only relative placement matters.

---

## Combinations

A **combination** is a selection of elements where order does not matter.

The number of ways to choose $k$ elements from $n$ distinct elements is

$$
\binom{n}{k} = \frac{n!}{k!(n-k)!}
$$

Combinations are used when:

* only some objects are chosen,
* order does not matter,
* repetition is not allowed.

Typical examples:

* choosing a committee,
* selecting cards from a deck,
* choosing endpoints of a segment.

---

## k-Permutations (Ordered Selections Without Repetition)

In some European textbooks the term "variation" is used for ordered selections.
In this course we use the standard English terminology: **k-permutations** (ordered selections).

A **k-permutation** (or ordered selection without repetition) is an ordered selection of $k$ elements from an $n$-element set, where no element may be used more than once.

The number of such ordered selections is

$$
P(n,k) = \frac{n!}{(n-k)!}
$$

This model is used when:

* only some objects are chosen,
* order matters,
* repetition is not allowed.

Typical examples:

* assigning medals,
* forming numbers with distinct digits,
* choosing ordered positions.

---

## Sequences With Repetition

A **sequence of length $(k)$** over an $(n)$-element set is an ordered selection where each position may contain any of the $(n)$ symbols and repetition is allowed.

The number of such sequences is

$$
n^k
$$

This model is used when:

* order matters,
* repetition is allowed,
* each position is chosen independently.

Typical examples:

* PIN codes,
* repeated coin tosses,
* repeated die rolls,
* telephone numbers.

---

## Permutations with Repeated Elements

When some objects are identical, the number of distinct permutations must account for indistinguishable elements. These are called **permutations with repeated elements** (or **permutations of a multiset**).

If among $n$ objects there are:

* $n_1$ identical objects of one type,
* $n_2$ identical objects of another type,
* and so on,

then the number of distinct arrangements is

$$
\frac{n!}{n_1!n_2!\dots n_r!}
$$

This model is used when:

* objects of the same type are indistinguishable,
* all objects are arranged,
* order matters at the level of positions, but equal objects are treated as identical.

Typical examples:

* arranging colored balls,
* arranging letters with repeated symbols.

---

## Distinguishable and Indistinguishable Objects

A fundamental distinction in combinatorics is whether objects are treated as **distinguishable** or **indistinguishable**.

### Distinguishable objects

Objects are distinguishable if they are treated as different individual items.

Example:

$$
R_1, R_2, R_3
$$

are three different red balls.

### Indistinguishable objects

Objects are indistinguishable if only their type matters.

Example:

three red balls all counted simply as

$$
R
$$

In many problems, the same physical collection may lead to different counts depending on how the outcomes are recorded.

---

## Order and Recording Rules

In combinatorial and probabilistic problems, the way outcomes are recorded is crucial.

Examples:

* If three balls are drawn and the order of drawing is recorded, then the outcome is a sequence.
* If the same three balls are drawn but only the selected set matters, then order is ignored.
* If only colors are recorded, then objects of the same color may become indistinguishable.

Thus the same experiment may lead to different sample spaces depending on the recording rule.

---

## Product Rule and Sum Rule

If a process consists of several independent stages, and:

* the first stage can be completed in $a$ ways,
* the second in $b$ ways,
* the third in $c$ ways,

then the whole process can be completed in

$$
a \cdot b \cdot c
$$

ways.

This rule is used throughout combinatorics, especially in code construction and multi-step selections.

---

If a task can be completed in one of several mutually exclusive ways, then the total number of outcomes is the sum of the numbers of outcomes in each case.

If one case gives $a$ possibilities and another disjoint case gives $b$, then the total is

$$
a+b
$$

This rule is useful when a problem must be split into cases.

---

## Task 1 — Recognizing Counting Models

For each situation determine which combinatorial model is most appropriate:

- permutation  
- circular permutation  
- combination  
- k-permutation (ordered selection without repetition)  
- sequence with repetition  
- permutation with repeated elements  

#### Problems:

1. Arranging 7 students in a line.  
2. Choosing 4 members of a committee from 12 people.  
3. Assigning gold, silver, and bronze medals among 15 athletes.  
4. Forming a 6-digit PIN code.  
5. Arranging the letters of the word **BANANA**.  
6. Seating 6 people around a round table.

---

## Task 2 — Permutations

1. In how many ways can 8 different books be arranged on a shelf?  
2. In how many ways can 8 people sit in a row if two particular people must sit next to each other?  
3. In how many ways can they sit if those two people must **not** sit next to each other?  
4. In how many ways can 10 questions in a test be ordered if the first question is fixed?

---

## Task 3 — Permutations with Repeated Elements

1. How many distinct arrangements of the word **MISSISSIPPI** are possible?
3. How many distinct arrangements of **STATISTICS** are possible?
4. How many of the arrangements of **STATISTICS** start with the letter **S**?

---

## Task 4 — Circular Permutations

1. In how many ways can 8 people sit around a round table?  
2. In how many ways can they sit if two particular people must sit next to each other?  
3. In how many ways can they sit if those two people must sit opposite each other?

---

## Task 5 — Combinations

1. A committee of 4 people is chosen from 12 students. How many committees are possible?  
2. How many committees contain a particular student?  
3. How many committees contain **at least one** of two particular students?  
4. How many committees contain exactly two women if the group consists of 7 men and 5 women?

---

## Task 6 — Combinations in Card Problems

A standard deck contains 52 cards.

1. In how many ways can 5 cards be drawn so that the hand contains **exactly 2 hearts**?  
2. In how many ways can a 5-card hand contain **at least one heart**?  
3. In how many ways can a 5-card hand contain **no face cards** (J, Q, K)?

---

## Task 7 — k-Permutations (Ordered Selections Without Repetition)

1. In how many ways can the first three places be assigned among 12 runners?  
2. How many 4-digit numbers with **distinct digits** can be formed from the digits 1–9?  
3. How many of these numbers are **divisible by 5**?

---

## Task 8 — Sequences with Repetition

1. How many 5-digit PIN codes are possible if digits may repeat?  
2. How many such codes contain **at least one repeated digit**?  
3. How many such codes have **all digits different**?

---

## Task 9 — Digit Restrictions

1. How many **5-digit numbers** exist?  
2. How many of them are **even**?  
3. How many contain **no repeated digits**?  
4. How many contain **at least one repeated digit**?

---

## Task 10 — Urn Models

An urn contains:

- 5 red balls  
- 4 blue balls  
- 3 green balls  

#### Problems:

1. Three balls are drawn **without replacement**. How many samples are possible if **order is ignored**?  
2. How many samples contain **exactly two red balls**?  
3. Three balls are drawn and the **order of colors is recorded**. How many outcomes are possible?  
4. How many outcomes contain **exactly two red balls**?


## Task 11 — Modeling Outcomes

In combinatorial and probabilistic problems, the number of possible outcomes depends on **how the results of an experiment are recorded**.

The same physical experiment may lead to different counting models depending on whether:

* objects are treated as **distinguishable or indistinguishable**,
* **order is recorded or ignored**,
* positions are treated as **distinct places**.

Answer the following conceptual questions.

---

### 1. Distinguishable vs Indistinguishable Objects

A box contains:

- 4 red balls  
- 4 blue balls  
- 3 green balls  

Thus there are 11 balls in total.

1. How many **linear arrangements of all 11 balls** are possible if balls of the same color are treated as **indistinguishable**?
2. How many arrangements are possible if every ball is **individually labeled**, for example $R_1, R_2, R_3, R_4, B_1, B_2, B_3, B_4, G_1, G_2, G_3$?
3. Explain why the answers in parts (1) and (2) are different.

---

### 2. Recording Order vs Ignoring Order

Three balls are drawn **without replacement** from the same box.

1. How many outcomes are possible if **only the set of colors is recorded** (order ignored)?
2. How many outcomes are possible if **the sequence of colors is recorded**?
3. Explain why recording the order changes the counting model.

---

### 3. PIN Code vs Number

A security system uses **4-digit PIN codes** consisting of digits from 0 to 9.

1. How many different PIN codes are possible if **repetition is allowed**?
2. Consider **4-digit numbers**, where the first digit cannot be zero.  
   How many such numbers exist?
3. Explain why a **PIN code** and a **4-digit number** are counted using different rules.
4. Explain why the codes $1234$ and $4321$ must be treated as **different outcomes**.

---

## Task 12 — Mixed Counting Problem

The following problem combines several counting models.  
For each part:

* determine which **counting model** is most appropriate,
* compute the **number of possible outcomes**.

---

### 1. Student ID Codes

A university introduces student identifiers consisting of:

- two **letters** chosen from the set $\{ A,B,C,D,E\}$
- followed by **three digits** from $0$ to $9$.

#### Problems:

1. How many identifiers are possible if **letters and digits may repeat**?
2. How many identifiers are possible if **letters may not repeat but digits may repeat**?
3. How many identifiers are possible if **neither letters nor digits may repeat**?

---

### 2. Medal Assignment

In a race with **12 runners**, medals are awarded for:

- gold  
- silver  
- bronze

#### Problems:

1. In how many ways can the medals be assigned?
2. Suppose two particular runners must **both receive medals**.  
   In how many ways can the medals be assigned?

---

### 3. Committee Selection

A committee of **4 people** is chosen from **10 students**, including **6 men and 4 women**.

1. How many committees are possible?
2. How many committees contain **exactly two women**?
3. How many committees contain **at least one woman**?

---

### 4. Circular Seating

Seven people sit around a **round table**.

1. How many different seating arrangements are possible?
2. In how many arrangements do two particular people sit **next to each other**?

---

### 5. Passwords

A password consists of **5 characters** chosen from:

- the digits $0–9$,
- the letters $A–Z$.

#### Problems:

1. How many passwords are possible if **repetition is allowed**?
2. How many passwords are possible if **no character may repeat**?
3. Which counting model is used in each case?
