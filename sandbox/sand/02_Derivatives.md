# Topic: Derivatives

This document introduces the concept of the derivative, its formal definition, and provides examples of its computation.

## 1. Formal Definition of the Derivative

The derivative of a function $f(x)$ with respect to the variable $x$ is the function $f'(x)$ whose value at any point $x$ is given by:

$$
f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
$$

provided this limit exists. The derivative $f'(x)$ represents the instantaneous rate of change of the function $f(x)$ at point $x$, which geometrically is the slope of the tangent line to the graph of $f(x)$ at that point.

## 2. Basic Differentiation Rules

While the limit definition is fundamental, we typically use a set of rules for computation.

*   **Power Rule:** If $f(x) = x^n$ for any real number $n$, then $f'(x) = nx^{n-1}$.
*   **Constant Multiple Rule:** If $g(x) = c \cdot f(x)$ where $c$ is a constant, then $g'(x) = c \cdot f'(x)$.
*   **Sum/Difference Rule:** If $h(x) = f(x) \pm g(x)$, then $h'(x) = f'(x) \pm g'(x)$.
*   **Product Rule:** If $h(x) = f(x)g(x)$, then $h'(x) = f'(x)g(x) + f(x)g'(x)$.
*   **Quotient Rule:** If $h(x) = \frac{f(x)}{g(x)}$ and $g(x) \neq 0$, then $h'(x) = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}$.
*   **Chain Rule:** If $h(x) = f(g(x))$, then $h'(x) = f'(g(x)) \cdot g'(x)$.

## 3. Solved Examples of Computation

Here are some examples of computing derivatives.

### Example 1: Using the Power and Sum Rules

**Problem:** Find the derivative of the function $f(x) = 3x^4 - 5x^2 + 7$.

**Solution:**

We apply the power rule and sum/difference rule to each term.

1.  **Derivative of the first term:**
    The derivative of $3x^4$ is $3 \cdot (4x^{4-1}) = 12x^3$.

2.  **Derivative of the second term:**
    The derivative of $-5x^2$ is $-5 \cdot (2x^{2-1}) = -10x^1 = -10x$.

3.  **Derivative of the third term:**
    The derivative of a constant (7) is 0.

4.  **Combine the results:**
    $$
f'(x) = 12x^3 - 10x + 0 = 12x^3 - 10x
$$

### Example 2: Using the Product Rule

**Problem:** Find the derivative of the function $h(x) = x^2 \sin(x)$.

**Solution:**

Let $f(x) = x^2$ and $g(x) = \sin(x)$. We need to use the product rule: $h'(x) = f'(x)g(x) + f(x)g'(x)$.

1.  **Find the derivatives of the parts:**
    *   $f'(x) = \frac{d}{dx}(x^2) = 2x$
    *   $g'(x) = \frac{d}{dx}(\sin(x)) = \cos(x)$

2.  **Apply the product rule formula:**
    $$
h'(x) = (2x)(\sin(x)) + (x^2)(\cos(x))
$$

3.  **Simplify:**
    $$
h'(x) = 2x\sin(x) + x^2\cos(x)
$$

### Example 3: Using the Quotient Rule

**Problem:** Find the derivative of the function $h(x) = \frac{e^x}{x^2+1}$.

**Solution:**

Let $f(x) = e^x$ and $g(x) = x^2+1$. We use the quotient rule: $h'(x) = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}$.

1.  **Find the derivatives of the parts:**
    *   $f'(x) = \frac{d}{dx}(e^x) = e^x$
    *   $g'(x) = \frac{d}{dx}(x^2+1) = 2x$

2.  **Apply the quotient rule formula:**
    $$
h'(x) = \frac{(e^x)(x^2+1) - (e^x)(2x)}{(x^2+1)^2}
$$

3.  **Simplify:**
    We can factor out $e^x$ from the numerator.
    $$
h'(x) = \frac{e^x(x^2 - 2x + 1)}{(x^2+1)^2} = \frac{e^x(x-1)^2}{(x^2+1)^2}
$$

### Example 4: Using the Chain Rule

**Problem:** Find the derivative of the function $h(x) = \cos(x^3)$.

**Solution:**

This is a composition of functions. Let the outer function be $f(u) = \cos(u)$ and the inner function be $g(x) = x^3$. We use the chain rule: $h'(x) = f'(g(x)) \cdot g'(x)$.

1.  **Find the derivatives of the parts:**
    *   $f'(u) = -\sin(u)$
    *   $g'(x) = 3x^2$

2.  **Apply the chain rule formula:**
    First, find $f'(g(x))$ by substituting $g(x)$ into $f'(u)$:
    $$
f'(g(x)) = -\sin(x^3)
$$
    Now, multiply by $g'(x)$:
    $$
h'(x) = -\sin(x^3) \cdot (3x^2)
$$

3.  **Simplify:**
    $$
h'(x) = -3x^2\sin(x^3)
$$
