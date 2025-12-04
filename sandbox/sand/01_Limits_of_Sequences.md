# Topic: The Limit of a Sequence

This document covers the formal definition of the limit of a sequence and provides solved examples as required for our study of Calculus.

## 1. Formal Definition of the Limit of a Sequence

A sequence $(a_n)$ has a limit $L$ if, for every real number $\epsilon > 0$, there exists a natural number $N$ such that for every natural number $n > N$, the terms of the sequence satisfy $|a_n - L| < \epsilon$.

In mathematical notation, this is expressed as:

$$ 
\lim_{n \to \infty} a_n = L \iff \forall \epsilon > 0, \exists N \in \mathbb{N} \text{ such that } \forall n > N, |a_n - L| < \epsilon
$$ 

This definition is the cornerstone of mathematical analysis and provides a rigorous way to describe the concept of convergence.

## 2. Solved Examples

Here are three examples demonstrating how to apply the definition to prove the limit of a sequence.

### Example 1: A Simple Rational Sequence

**Problem:** Prove that the sequence $a_n = \frac{1}{n}$ has a limit of $L=0$.

**Solution:**

We need to show that for any given $\epsilon > 0$, we can find an $N$ such that for all $n > N$, $|a_n - 0| < \epsilon$.

1.  **Set up the inequality:**
    We start with the expression $|a_n - L|$:
    $$ 
    \left| \frac{1}{n} - 0 \right| = \left| \frac{1}{n} \right| = \frac{1}{n}
    $$ 
    Since $n$ is a natural number, $n > 0$, so the absolute value is not strictly necessary but included for rigor.

2.  **Find N in terms of epsilon:**
    We want to find $N$ such that for all $n > N$, the following inequality holds:
    $$ 
    \frac{1}{n} < \epsilon
    $$ 
    Rearranging this for $n$, we get:
    $$ 
    n > \frac{1}{\epsilon}
    $$ 

3.  **Choose N:**
    Based on the above, we can choose $N$ to be any integer greater than $\frac{1}{\epsilon}$. A standard choice is $N = \lfloor \frac{1}{\epsilon} \rfloor + 1$ or simply stating that we choose $N > \frac{1}{\epsilon}$.

4.  **Conclusion:**
    For any $\epsilon > 0$, we choose $N > \frac{1}{\epsilon}$. Then for any $n > N$, it follows that $n > \frac{1}{\epsilon}$, which implies $\frac{1}{n} < \epsilon$. Thus, we have shown that $|a_n - 0| < \epsilon$ for all $n > N$. This completes the proof that $\lim_{n \to \infty} \frac{1}{n} = 0$.

### Example 2: A Linear Sequence

**Problem:** Prove that the sequence $a_n = \frac{2n+1}{n+1}$ has a limit of $L=2$.

**Solution:**

We need to show that for any given $\epsilon > 0$, we can find an $N$ such that for all $n > N$, $|\frac{2n+1}{n+1} - 2| < \epsilon$.

1.  **Set up the inequality and simplify:**
    $$ 
    \left| \frac{2n+1}{n+1} - 2 \right| = \left| \frac{2n+1 - 2(n+1)}{n+1} \right| = \left| \frac{2n+1 - 2n - 2}{n+1} \right| = \left| \frac{-1}{n+1} \right| = \frac{1}{n+1}
    $$ 

2.  **Find N in terms of epsilon:**
    We need to solve the inequality for $n$:
    $$ 
    \frac{1}{n+1} < \epsilon
    $$ 
    This gives:
    $$ 
    1 < \epsilon(n+1) \implies \frac{1}{\epsilon} < n+1 \implies n > \frac{1}{\epsilon} - 1
    $$ 

3.  **Choose N:**
    We can choose $N$ to be any integer greater than $\frac{1}{\epsilon} - 1$. For example, $N = \lfloor \frac{1}{\epsilon} - 1 \rfloor + 1$. If $\epsilon$ is large enough such that $\frac{1}{\epsilon} - 1$ is negative, any $N \ge 1$ will work.

4.  **Conclusion:**
    For any $\epsilon > 0$, let's choose $N > \frac{1}{\epsilon} - 1$. For any $n > N$, it follows that $n > \frac{1}{\epsilon} - 1$, which implies $n+1 > \frac{1}{\epsilon}$, and therefore $\frac{1}{n+1} < \epsilon$. We have successfully shown that $|\frac{2n+1}{n+1} - 2| < \epsilon$ for all $n > N$. This proves that $\lim_{n \to \infty} \frac{2n+1}{n+1} = 2$.

### Example 3: Squeeze Theorem

**Problem:** Find the limit of the sequence $a_n = \frac{\sin(n)}{n}$.

**Solution:**

For this problem, using the formal definition is complicated. A more direct approach is the **Squeeze Theorem**.

1.  **Establish Bounds:**
    We know that the sine function is bounded between -1 and 1 for all real numbers.
    $$ 
    -1 \le \sin(n) \le 1
    $$ 

2.  **Construct Bounding Sequences:**
    Since $n$ is a positive integer, we can divide the entire inequality by $n$ without changing the direction of the inequalities:
    $$ 
    -\frac{1}{n} \le \frac{\sin(n)}{n} \le \frac{1}{n}
    $$ 
    Let's define two new sequences, $b_n = -\frac{1}{n}$ and $c_n = \frac{1}{n}$.

3.  **Find the Limits of the Bounding Sequences:**
    From our first example (and it can be proven similarly), we know:
    $$ 
    \lim_{n \to \infty} c_n = \lim_{n \to \infty} \frac{1}{n} = 0
    $$ 
    $$ 
    \lim_{n \to \infty} b_n = \lim_{n \to \infty} -\frac{1}{n} = - \lim_{n \to \infty} \frac{1}{n} = 0
    $$ 

4.  **Apply the Squeeze Theorem:**
    Since $b_n \le a_n \le c_n$ for all $n$, and $\lim_{n \to \infty} b_n = \lim_{n \to \infty} c_n = 0$, the Squeeze Theorem states that the limit of $a_n$ must also be 0.

5.  **Conclusion:**
    Therefore, $\lim_{n \to \infty} \frac{\sin(n)}{n} = 0$.
