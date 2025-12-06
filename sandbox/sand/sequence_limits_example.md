# Understanding Sequence Limits

This document provides a brief introduction to the concept of limits of sequences in calculus.

## What is a Sequence?

A sequence is an ordered list of numbers. We can denote a sequence as $(a_n)$, where $n$ is a natural number ($n \in \mathbb{N}$). 

For example, the sequence $(a_n) = \frac{1}{n}$ for $n \ge 1$ looks like this:
$1, \frac{1}{2}, \frac{1}{3}, \frac{1}{4}, \dots$

## Limit of a Sequence

The limit of a sequence is the value that the terms of a sequence "tend to". If a sequence has a limit, we say that the sequence is **convergent**.

### Formal Definition

A sequence $(a_n)$ has the limit $L$ if, for every $\epsilon > 0$, there exists a natural number $N$ such that for all $n > N$, we have $|a_n - L| < \epsilon$.

We write this as:
$$ 
\lim_{n \to \infty} a_n = L 
$$

This definition is often called the **epsilon-N definition** of a limit. It means that no matter how small a positive number $\epsilon$ you choose, you can always find a point in the sequence ($N$) after which all the terms are within a distance of $\epsilon$ from the limit $L$.

### Example: The limit of $(a_n) = \frac{1}{n}$

Let's prove that the limit of the sequence $(a_n) = \frac{1}{n}$ is 0.

$$ 
\lim_{n \to \infty} \frac{1}{n} = 0 
$$

**Proof:**

According to the definition, for any given $\epsilon > 0$, we need to find an $N$ such that for all $n > N$, we have:
$$ 
\left| \frac{1}{n} - 0 \right| < \epsilon 
$$
This simplifies to:
$$ 
\frac{1}{n} < \epsilon 
$$
Solving for $n$, we get:
$$ 
n > \frac{1}{\epsilon} 
$$
So, if we choose $N$ to be any integer greater than $\frac{1}{\epsilon}$, then for any $n > N$, the condition $|a_n - 0| < \epsilon$ will be satisfied.

For example, if we choose $\epsilon = 0.01$, then we need to find an $N$ such that for all $n > N$, $\frac{1}{n} < 0.01$. This means $n > 100$. So we can choose $N=100$. For all $n > 100$, the terms of the sequence are closer to 0 than 0.01.

This confirms that the limit of the sequence is indeed 0.

## Another Example: A constant sequence

Consider the sequence $(b_n) = c$, where $c$ is a constant. The terms are $c, c, c, \dots$.
The limit of this sequence is $c$.

$$ 
\lim_{n \to \infty} c = c 
$$

**Proof:**
For any $\epsilon > 0$, we need to find an $N$ such that for all $n > N$:
$$ 
|b_n - c| < \epsilon 
$$
Since $b_n = c$, this becomes:
$$ 
|c - c| = 0 < \epsilon 
$$
This inequality is true for any $\epsilon > 0$ and for all $n$. So we can choose any $N$, for instance $N=1$.

This shows that the concept of a limit aligns with our intuition.

## Detailed Proof: The limit of $(a_n) = \frac{n^2-1}{n^2}$

Let's walk through the proof that the limit of the sequence $(a_n) = \frac{n^2-1}{n^2}$ is 1.

**Step 1: Simplify the expression and identify the limit**

First, it's often helpful to simplify the algebraic expression of the sequence to better understand its behavior as $n$ gets very large.

$$
a_n = \frac{n^2-1}{n^2} = \frac{n^2}{n^2} - \frac{1}{n^2} = 1 - \frac{1}{n^2}
$$

As $n$ approaches infinity ($n \to \infty$), the term $\frac{1}{n^2}$ gets closer and closer to 0. So, intuitively, the limit of the sequence should be $1 - 0 = 1$. Our goal is to prove this formally.

We want to prove that:
$$
\lim_{n \to \infty} \left(1 - \frac{1}{n^2}\right) = 1
$$

**Step 2: Apply the Epsilon-N Definition of a Limit**

The formal definition of a limit states that for any small positive number $\epsilon$ (epsilon), we must be able to find a corresponding integer $N$ such that all terms of the sequence after the $N$-th term are within $\epsilon$ distance of the limit.

Let's write this mathematically. We need to show that for any $\epsilon > 0$, there exists an $N$ such that for all $n > N$:
$$
|a_n - L| < \epsilon
$$
In our case, $a_n = 1 - \frac{1}{n^2}$ and the limit $L=1$. So we substitute these into the formula:
$$
\left| \left(1 - \frac{1}{n^2}\right) - 1 \right| < \epsilon
$$

**Step 3: Solve the inequality for n**

Now, we simplify the expression inside the absolute value:
$$
\left| -\frac{1}{n^2} \right| < \epsilon
$$
Since the absolute value of a negative number is its positive counterpart:
$$
\frac{1}{n^2} < \epsilon
$$
Our goal is to find what $n$ needs to be for this inequality to hold true. We want to isolate $n$. First, we can take the reciprocal of both sides. Remember to flip the inequality sign when you do this:
$$
n^2 > \frac{1}{\epsilon}
$$
Now, we take the square root of both sides. Since $n$ is a positive integer, we only need to consider the positive root:
$$
n > \sqrt{\frac{1}{\epsilon}}
$$

**Step 4: Choose N and conclude the proof**

This final inequality tells us exactly how to find our $N$. If we choose $N$ to be any integer that is greater than $\sqrt{\frac{1}{\epsilon}}$, then for any integer $n$ that is greater than $N$, our starting condition $|a_n - 1| < \epsilon$ will be true.

Let's see this with a concrete example. Suppose someone challenges us with $\epsilon = 0.01$. We need to find an $N$ that works.
Using our formula, we need $n > \sqrt{\frac{1}{0.01}}$.
$$
n > \sqrt{100}
$$
$$
n > 10
$$
So, we can choose $N=10$. This guarantees that for every term in the sequence where $n > 10$ (e.g., $n=11, 12, \dots$), the value of that term will be less than $0.01$ away from our limit of 1.

Since we can find such an $N$ for *any* choice of $\epsilon > 0$, we have formally proven that:
$$
\lim_{n \to \infty} \frac{n^2-1}{n^2} = 1
$$
