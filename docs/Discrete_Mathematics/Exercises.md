# Exercises

## **Set theory**

#### Task 1

Write down five elements for each of the following sets:

1. $n \in \mathbb{N}: n$ is divisible by 5
2. $\{2n + 1: n \in \mathbb{P}\}$
3. $\mathcal{P}(\{1, 2, 3, 4, 5\})$
4. $\{2^n: n \in \mathbb{N}\}$
5. $\{1/n: n \in \mathbb{P}\}$
6. $\{r \in \mathbb{Q}: 0 < r < 1\}$
7. $\{n \in \mathbb{N}: n + 1$ is a prime number$\}$

Whre $\mathbb{P}$ denotes the positive integers.

#### Task 2

Write the elements of the following sets:

1. $\{1/n: n = 1, 2, 3, 4\}$
2. $\{n^2 - n: n = 0, 1, 2, 3, 4\}$
3. $\{1/n^2: n \in \mathbb{P}, n$ is even$\}$
4. $\{2 + (-1)^n: n \in \mathbb{N}\}$


#### Task 3

Determine the following sets, i.e., write down their elements if the sets are non-empty and write $\emptyset$ if they are empty:

1. $\{n \in \mathbb{N}: n^2 = 9\}$
2. $\{n \in \mathbb{Z}: n^2 = 9\}$
3. $\{n \in \mathbb{Z}: n^2 = -9\}$
4. $\{n \in \mathbb{N}: 3 < n < 7\}$
5. $\{n \in \mathbb{Z}: 3 < |n| < 7\}$
6. $\{x \in \mathbb{Q}: x^2 = 2\}$
7. $\{x \in \mathbb{R}: x^2 = 2\}$
8. $\{x \in \mathbb{R}: x^2 = -2\}$
9. $\{x \in \mathbb{R}: x < 1 \land x \geq 2\}$
10. $\{3n + 1: n \in \mathbb{N} \land n \leq 6\}$
11. $\{n \in \mathbb{P}: n$ is a prime number and $n \leq 15\}$

#### Task 4

How many elements do the following sets have? Write $\infty$ if the set is infinite:

1. $\{n \in \mathbb{N}: n^2 = 2\}$
2. $\{n \in \mathbb{Z}: 0 < |n| \leq 73\}$
3. $\{n \in \mathbb{Z}: 5 \leq |n| \leq 73\}$
4. $\{n \in \mathbb{Z}: 5 < |n| < 73\}$
5. $\{n \in \mathbb{Z}: n$ is even and $|n| \leq 73\}$
6. $\{x \in \mathbb{Q}: 0 < x \leq 73\}$
7. $\{x \in \mathbb{Q}: x^2 = 2\}$
8. $\{x \in \mathbb{R}: 0.99 < x < 1.00\}$
9. $\mathcal{P}(\{0, 1, 2, 3\})$
10. $\mathcal{P}(\mathbb{N})$
11. $\{n \in \mathbb{N}: n$ is even$\}$
12. $\{n \in \mathbb{N}: n$ is prime$\}$
13. $\{n \in \mathbb{N}: n$ is even and prime$\}$
14. $\{n \in \mathbb{N}: n$ is even or prime$\}$


#### Task 5

Consider the sets $\{0, 1\}$, $(0, 1)$, and $[0, 1)$. Are the following statements true?

1. $\{0, 1\} \subseteq (0, 1)$
2. $\{0, 1\} \subseteq [0, 1)$
3. $(0, 1) \subseteq \{0, 1\}$
4. $(0, 1) \subseteq [0, 1)$
5. $\{0, 1\} \cap (0, 1) = \emptyset$
6. $(0, 1) \cap \mathbb{Q} = \emptyset$


#### Task 6

Let $U = \{1, 2, 3, 4, 5, \dots, 12\}$, $A = \{1, 3, 5, 7, 11\}$, $B = \{2, 3, 5, 7, 11\}$, $C = \{2, 3, 6, 12\}$, and $D = \{2, 4, 8\}$. Determine the following sets:

1. $A \cup B$
2. $A \cap C$
3. $(A \cup B) \cap C^c$
4. $A \setminus B$
5. $B \oplus D$
6. How many subsets does the set $C$ have?

Where $\oplus$ denotes the symmetric difference operation.

#### Task 7

Let $A = \{1, 2, 3\}$, $B = \{n \in \mathbb{P}: n$ is even$\}$, and $C = \{n \in \mathbb{P}: n$ is odd$\}$. 

1. Determine the sets $A \cap B$, $B \cap C$, $B \cup C$, $B \oplus C$.
2. Write down all subsets of $A$.
3. Which of the following sets: $A \oplus B$, $A \oplus C$, $A \setminus C$ are infinite?


#### Task 8

What is the set $A \oplus A$ for any set $A$? What is $A \oplus \emptyset$?



#### Task 9

Let $A = \{a, b, c\}$ and $B = \{a, b, d\}$.

* Write or draw all ordered pairs from the set $A \times A$.
* Write or draw all ordered pairs from the set $A \times B$.
* Write or draw all elements of the set $\{(x, y): x \in A, y \in B, x = y\}$.

#### Task 10

Write the elements of the following sets:

1. $\{(m, n) \in \mathbb{N}^2: m = n\}$
2. $\{(m, n) \in \mathbb{N}^2: m + n = 6\}$
3. $\{(m, n) \in \mathbb{N}^2: m = 3 \text{ and } n \text{ is prime}\}$
4. $\{(m, n) \in \mathbb{N}^2: \min(m, n) = 3\}$
5. $\{(m, n) \in \mathbb{N}^2: \max(m, n) = 3\}$



## **Functions**

### **Basics**

#### Task 1

For function $f: \mathbb{R} \to \mathbb{R}$ defined as follows:

$$
f(x) =
\begin{cases}
x^3, & \text{if } x \geq 1, \\
x, & \text{if } 0 \leq x < 1, \\
-x^3, & \text{if } x < 0.
\end{cases}
$$

1. Calculate $f(3)$, $f(1/3)$, $f(-1/3)$, and $f(-3)$.
2. Sketch the graph of $f$.
3. Determine $\text{Im}(f)$.


#### Task 2

Let $S = \{1, 2, 3, 4, 5\}$ and $T = \{a, b, c, d\}$. For each of the following questions, answer YES or NO. Provide a brief justification for your answer:

1. Are there **injective** functions from $S$ to $T$?
2. Are there **surjective** functions from $S$ to $T$?
3. Are there **injective** functions from $T$ to $S$?
4. Are there **surjective** functions from $T$ to $S$?
5. Are there **bijections** between $S$ and $T$?

#### Task 4

Let $S = \{1, 2, 3, 4, 5\}$Consider the following functions defined on $S$:

- $f(n) = n$,
- $g(n) = 6 - n$,
- $h(n) = \max(3, n)$,
- $k(n) = \max(1, n - 1)$.

Exercises:

1. Represent each function as a set of ordered pairs, and write down their elements.
2. Sketch the graph of each function.
3. Which of these functions are injective?

#### Task 5

Define the function $f: \mathbb{N} \times \mathbb{N} \to \mathbb{N}$ as $f(m, n) = 2^{m + 3n}$.

1. Calculate $f(m, n)$ for five distinct pairs $(m, n) \in \mathbb{N} \times \mathbb{N}$.
2. Explain why $f$ is not injective.
3. Does $f$ map $\mathbb{N} \times \mathbb{N}$ onto $\mathbb{N}$? Justify your answer.
4. Show that $g(m, n) = 2^{4m}n$ defines a function from $\mathbb{N} \times \mathbb{N}$ to $\mathbb{N}$ that is not injective.

#### Task 6

Define the following functions on $\mathbb{N}$:

- $f(n) = 3n$,
- $g(n) = n + (-1)^n$,
- $h(n) = \min(n, 100)$,
- $k(n) = \max(10, n - 5)$.

Qestions:

1. Which of these functions are injective?
2. Which of these functions map $\mathbb{N}$ onto $\mathbb{N}$?


###  **Function composition**

#### Task 1

Define three functions mapping $\mathbb{R} \to \mathbb{R}$ as follows:

- $f(x) = x^3 - 4x$,
- $g(x) = \frac{1}{x^2 + 1}$,
- $h(x) = x^4$.

Find:

1. $f \circ g$,
2. $g \circ f$,
3. $h \circ g$,
4. $g \circ h$.

#### Task 2

Show that if $f: S \to T$ and $g: T \to U$ are injective functions, then $g \circ f$ is also injective.


#### Task 15

Let $f$ and $g$ map $\mathbb{Z}$ to $\mathbb{Z}$, where $f(n) = n - 1$ for all $n \in \mathbb{Z}$, and $g$ is the characteristic function of even numbers in $\mathbb{Z}$:

$$
\begin{align*}
g(n) =
\begin{cases}
1, & \text{if } n \text{ is even}, \\
0, & \text{if } n \text{ is odd}.
\end{cases}
\end{align*}
$$

1. Compute $(g \circ f)(6)$, $(g \circ f)(7)$, $(g \circ f)(11)$, $(g \circ f)(12)$.
2. Determine $g \circ f$ and $f \circ g$.
3. Show that $g \circ f \neq f \circ g$ and that $g \circ f$ takes the value 0 wherever $f$ takes even values.


### **Inverse functions**

#### Task 1

Find the inverse functions of the following functions mapping $\mathbb{R}$ to $\mathbb{R}$:

1. $f(x) = 2x + 3$
2. $g(x) = x^3 - 2$
3. $h(x) = (x - 2)^3$
4. $k(x) = \sqrt{x} + 7$

#### Task 2

The functions $\log x$, $x^2$, $\sqrt{x}$, and $1/x$ are commonly available on calculators.

1. Determine the domains of these functions.
2. Which of these functions are inverses of each other?

#### Task 3

Here are several functions mapping $\mathcal{P}(N) \times \mathcal{P}(N)$ to $\mathcal{P}(N)$:

- $\text{SUM}(A, B) = A \cup B$,
- $\text{PRODUCT}(A, B) = A \cap B$,
- $\text{SYM}(A, B) = A \oplus B$.

Show that:

1. Prove that each of these functions maps $\mathcal{P}(N) \times \mathcal{P}(N)$ to $\mathcal{P}(N)$.
2. Prove that none of these functions is injective.
3. Determine the size of the set $F^{-1}(\{0\})$ and $F^{-1}(\{4\})$ for each of these functions $F$.

#### Task 4

The following two functions map $\mathbb{N} \to \mathbb{N}$:

- $f(n) = n + 1$,
- $g(n) = \max(0, n - 1)$.

Show that:

1. Calculate $f(n)$ for $n = 0, 1, 2, 3, 4, 73$.
2. Calculate $g(n)$ for $n = 0, 1, 2, 3, 4, 73$.
3. Prove that $f$ is injective but does not map $\mathbb{N}$ onto itself.
4. Prove that $g$ maps $\mathbb{N}$ onto $\mathbb{N}$ but is not injective.
5. Prove that $g \circ f = 1_\mathbb{N}$ but $f \circ g \neq 1_\mathbb{N}$.


#### Task 5

If $f: S \to S$ and $f \circ f = 1_S$, then $f$ is its own inverse. Show that the following functions are their own inverses:

1. $f(x) = 1/x$ (for $x \in (0, \infty)$),
2. $f(A) = A^c$ (for $A \subseteq S$),
3. $f(x) = 1 - x$ (for $x \in \mathbb{R}$).


#### Task 6

Let $f: S \to T$ and $g: T \to U$ be bijections. Prove that $g \circ f$ is also a bijection and that $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$.


#### Task 7

Define the function $f: \mathbb{R} \times \mathbb{R} \to \mathbb{R} \times \mathbb{R}$ as $f(x, y) = (x + y, x - y)$. 

1. Prove that $f$ is a bijection.
2. Prove that $f$ maps $\mathbb{R} \times \mathbb{R}$ onto itself.
3. Find the inverse function $f^{-1}$.
4. Find the composition $f \circ f^{-1}$ and $f^{-1} \circ f$.

## **Sequences and series**

#### Task 1

Calculate:

1. $\frac{7!}{5!}$
2. $\frac{10!}{6!4!}$
3. $\frac{9!}{0!}$
4. $\sum_{k=0}^{5} k!$
5. $\prod_{j=3}^{5} j$

#### Task 2

Simplify the fractions:

1. $\frac{n!}{(n - 1)!}$
2. $\frac{(n!)^2}{(n + 1)!(n - 1)!}$

#### Task 3

Calculate:

1. $\sum_{k=1}^{n} 3^k$ for $n = 1, 2, 3, 4$
2. $\sum_{k=n}^{3} k^3$ for $n = 3, 4, 5$
3. $\sum_{j=1}^{z} j$ for $n = 1, 2, 5$

#### Task 4

Calculate:

1. $\sum_{i=0}^{\infty} (-1)^i$
2. $\prod_{n=1}^{\infty} (2n + 1)$
3. $\sum_{k=3}^{8} (k^2 + 1)$
4. $\left(\sum_{k=3}^{8} k^2\right) + 1$

#### Task 5

Calculate:

1. $\prod_{n=1}^{m} (n - 3)$ for $m = 1, 2, 3, 4, 73$
2. $\prod_{m=1}^{k} \frac{k+1}{k}$ for $m = 1, 2, 3$. Provide a general formula for the product for all $k \in \mathbb{P}$.

#### Task 6

Calculate:

1. $\sum_{k=0}^{2} k^2$ for $n = 1, 2, 3, 4, 5$
2. Use your answer to part (1) to deduce a general formula for this sum.

#### Task 7

Consider the sequence defined by $a_n = \frac{n - 1}{n + 1}$ for $n \in \mathbb{P}$.

1. Write the first six terms of this sequence.
2. Calculate $a_{n+1} - a_n$ for $n = 1, 2, 3$.
3. Prove that $a_{n+1} + a_n = \frac{n(n+1)}{(n+1)(n+2)}$ for $n \in \mathbb{P}$.

#### Task 8

Consider the sequence defined by $b_n = \frac{1}{2} \left(1 + (-1)^n\right)$ for $n \in \mathbb{N}$.

1. Write the first seven terms of this sequence.
2. What is the set of all values of this sequence?



## **Logic**


#### Task 1

Let $p$, $q$, and $r$ be the following statements:

- $p$: "It is raining."
- $q$: "The sun is shining."
- $r$: "There are clouds in the sky."

Write the following statements using logical symbols with $p$, $q$, $r$, and logical operators:

1. It is raining, and the sun is shining.
2. If it is raining, then there are clouds in the sky.
3. If it is not raining, then the sun is not shining, and there are no clouds in the sky.
4. The sun is shining if and only if it is not raining.
5. If there are no clouds in the sky, then the sun is shining.

#### Task 2

Let $p$, $q$, and $r$ be as defined in Task 1. Translate the following logical expressions into plain English:

1. $p \land q \rightarrow r$
2. $\neg p \rightarrow q \lor r$
3. $\neg (p \lor q \lor r)$
4. $(p \rightarrow r) \rightarrow q$

#### Task 3

Provide the truth values of the statements in Tasks 1 and 2.

#### Task 4

Determine which of the following expressions are statements. Provide their truth values:

1. $x^2 = 2\quad \forall x \in \mathbb{R}$
2. $x^2 = 2$ for some $x \in \mathbb{R}$
3. $x^2 = x$
4. $x^2 = x$ for exactly one $x \in \mathbb{R}$
5. $xy = z$ implies $y = z$ for all $x, y, z \in \mathbb{R}$

#### Task 5

Rewrite the ambiguous expression $x^2 = y^2$ as:

1. A precise statement whose logical value is true.
2. A precise statement whose logical value is false.

#### Task 6

Provide the contrapositive of the following statements:

1. "If I am smart, then I am rich."
2. "If $x^2 = x$, then $x = 0$ or $x = 1$."
3. "If $2 + 2 = 4$, then $2 + 4 = 8$."

#### Task 7

Verify Goldbach's conjecture for small numbers, such as 6, 8, and 10. Check it for the number 98.


## **Relations**

#### Task 1

For the following relations in the set $S = \{0, 1, 2, 3\}$, determine which properties (Reflexive (Z), Irreflexive (PZ), Symmetric (S), Antisymmetric (AS), Transitive (P)) are satisfied:

1. $(m, n) \in R_1$, if $m + n = 3$,
2. $(m, n) \in R_2$, if $m - n$ is an even number,
3. $(m, n) \in R_3$, if $m \leq n$,
4. $(m, n) \in R_4$, if $m + n \leq 4$,
5. $(m, n) \in R_5$, if $\max\{m, n\} = 3$.

#### Task 2

Let $A = \{0, 1, 2\}$. Each of the following statements defines a relation $R$ in $A$, i.e., $(m, n) \in R$ if the statement is true for $m, n \in A$. Write each relation as a set of ordered pairs:

1. $m \leq n$,
2. $mn = 0$,
3. $m = n$,
4. $m^2 + n^2 = 2$,
5. $m^2 - n^2 = 2$,
6. $m \notin A$,
7. $m^2 = n$,
8. $mn = 2$,
9. $\max\{m, n\} = 1$.

#### Task 3

Which of the relations from Task 2 are reflexive, and which are symmetric?

#### Task 4

In the set $\mathbb{N}$, the following binary relations are defined:

1. Write the relation $R_1$ defined by $m + n = 5$ as a set of ordered pairs.
2. Write the relation $R_2$ defined by $\max\{m, n\} = 2$ as a set of ordered pairs.
3. Determine if $R_3$, defined by $m^3 - n^3 \equiv 0 \pmod{5}$, contains infinitely many ordered pairs. Write some examples.

#### Task 5

For each relation from Task 4, determine which properties: symmetric, antisymmetric, transitive, reflexive, irreflexive, are satisfied.


#### Task 6

Provide an example of a relation that is:

1. Antisymmetric and transitive but not reflexive,
2. Symmetric but not reflexive or transitive.

#### Task 7

Draw the graph of each relation from Task 1. Do not draw arrows if the relation is symmetric.

#### Task 8

Draw the graph of each relation from Task 2. Do not draw arrows if the relation is symmetric.


## Induction

#### Task 1

Prove the following statements by induction:

1. $1 + 2 + \dots + n = \frac{n(n+1)}{2}$ for all $n \in \mathbb{N}$.

#### Task 2

Prove the following statements by induction:

1. $1^2 + 2^2 + \dots + n^2 = \frac{n(n+1)(2n+1)}{6}$ for all $n \in \mathbb{N}$.

#### Task 3

Prove the following statements by induction:

1. $k! \geq 2^k$ for all $k\geq 4$
2. $37^{500}-37^4$ is divisible by 10.
3. For $n\geq0$

$$
\frac{1}{1\cdot 5}+
\frac{1}{5\cdot 9}+
\frac{1}{9\cdot 13}+
\cdots+
\frac{1}{(4n-3)(4n+1)}=
\frac{n}{4n+1}
$$

## Requrece


#### Task 1

Compute first 5 elements of the following sequences:

1. $a_0 = 1$, $a_{n+1} = 2a_n + 1$ for $n \in \mathbb{N}\setminus\{0\}$.
2. $b_0 = 2$, $b_{n+1} = b_n^2 - 1$ for $n \in \mathbb{N}\setminus\{0\}$.
3. $c_0 = 2,\ c_1 = 3$, $c_{n+2} = c_{n+1} \cdot c_n$ for $n \in \mathbb{N}\setminus\{0,1\}$.
4. $d_0 = 1,\ d_1 = 2$, $d_{n+2} = d_{n+1}/d_n$ for $n \in \mathbb{N}\setminus\{0,1\}$.

#### Task 2

Define folowing formulas and sequences using recurence:

1. $n!=1\cdot 2\cdot 3\cdot \ldots \cdot n$ for $n\geq 1$.
2. Fibonacci numbers.
3. Napier's number
4. $(2,2^2, (2^2)^2,((2^2)^2)^2,\ldots)$
5. $(2,2^2, 2^{2^{2}}, 2^{2^{2^{2}}},\ldots)$

## Number theory

#### Task 1

Check the following congruences:

1. $12 \equiv 2 \pmod{5}$
2. $12 \equiv 3 \pmod{10}$
3. $21 \equiv 1 \pmod{5}$
4. $23 \equiv 3 \pmod{4}$


#### Task 2

Probe that if $m' \equiv m \pmod{p}$ and $n' \equiv n \pmod{p}$, then:

1. $m'+n' \equiv m+n \pmod{p}$.
2. $m'n' \equiv mn \pmod{p}$.

### Task 3

Compute the following greatest common divisors:

1. $\gcd(12, 15)$
2. $\gcd(12, 18)$
3. $\gcd(72, 15)$
4. $\gcd(45, 12)$

### Task 4

Solve congruences of the form $ax \equiv b \pmod{m}$:

1. $2x \equiv 3 \pmod{5}$
2. $3x \equiv 4 \pmod{7}$
3. $4x \equiv 5 \pmod{6}$
4. $5x \equiv 6 \pmod{8}$
5. $6x \equiv 7 \pmod{9}$