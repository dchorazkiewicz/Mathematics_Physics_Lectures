# Motion from a given $a(t)$

## Learning goals

- Reconstruct $v(t)$ from a given acceleration $a(t)$ by integration.
- Reconstruct $x(t)$ by integrating again, using **initial conditions** to fix constants.
- Understand why two initial conditions are needed to determine a unique position function from $a(t)$.
- Work confidently with common acceleration laws (polynomial and simple trigonometric forms).

## Why this matters

In kinematics, acceleration is sometimes provided directly:

- a sensor measures acceleration,
- a problem states “acceleration varies with time as …,”
- or later in dynamics, forces determine acceleration.

To get the motion, you must integrate. This is the core “reconstruction pipeline”:

$$
a(t) \rightarrow v(t) \rightarrow x(t).
$$

The most frequent errors here are not calculus complexity, but missing constants and mixing initial times.

## Core idea

Acceleration is the derivative of velocity, and velocity is the derivative of position:

$$
a(t) = \frac{dv}{dt}, \qquad v(t)=\frac{dx}{dt}.
$$

So:

- integrating $a(t)$ accumulates changes in velocity,
- integrating $v(t)$ accumulates changes in position.

Because you integrate twice, you need **two pieces of initial information** to pin down the motion, typically:

$$
v(t_0)=v_0, \qquad x(t_0)=x_0.
$$

## Mathematical formulation

### Step 1: Velocity from acceleration

Given $a(t)$ and $v(t_0)=v_0$:

$$
v(t) = v_0 + \int_{t_0}^{t} a(\tau)\,d\tau.
$$

### Step 2: Position from velocity

Given also $x(t_0)=x_0$:

$$
x(t) = x_0 + \int_{t_0}^{t} v(\tau)\,d\tau.
$Combining both steps:$
x(t) = x_0 + \int_{t_0}^{t} \left(v_0 + \int_{t_0}^{\tau} a(s)\,ds\right)d\tau.
$$

This expression looks nested, but the workflow is simple: integrate once to get $v(t)$, then integrate again to get $x(t)$.

### A practical note on constants

If you do indefinite integrals, you will get constants at each step:

$$
v(t) = \int a(t)\,dt + C_1,
$$

$$
x(t) = \int v(t)\,dt + C_2.
$$

Use the initial conditions to determine $C_1$ and $C_2$. Without them, there are infinitely many motions consistent with the same acceleration law.

## Interpretation

- The integral of acceleration over time gives the **change in velocity**:

$$
v(t_2)-v(t_1) = \int_{t_1}^{t_2} a(t)\,dt.
$$

- The integral of velocity gives **displacement**:

$$
x(t_2)-x(t_1) = \int_{t_1}^{t_2} v(t)\,dt.
$$

- If you only know $a(t)$, you cannot locate the motion in space: you still need initial position and velocity.

## Typical examples

1) **Polynomial acceleration:** $a(t)=kt$ gives quadratic velocity and cubic position.

2) **Sinusoidal acceleration:** $a(t)=A\cos(\omega t)$ leads to sinusoidal velocity and position with phase shifts. This previews periodic motion.

3) **Constant acceleration:** $a(t)=a_0$ returns the uniformly accelerated motion formulas from Section 07.

## Common mistakes

- Forgetting one of the two constants (integrating twice but applying only one initial condition).
- Using $v(t)=\int a(t)dt$ without adding the initial velocity.
- Using an initial condition at a different time than the one used in the integral limits (mixing $t_0$ values).
- Losing sign information: acceleration can be positive or negative depending on the chosen axis.
- Treating the integral of acceleration as “distance” rather than “velocity change.”

## Worked example

An object moves along a line with acceleration:

$a(t) = 2t$

with $a$ in m/s² and $t$ in s. At $t=0$:

$v(0) = 1\,\text{m/s}, \qquad x(0)=0.$

1) Find $v(t)$ and $x(t)$.  
2) Find the displacement from $t=0$ to $t=3$.

### Step 1: Integrate acceleration to get velocity

Use:

$$
v(t) = v(0) + \int_{0}^{t} 2\tau\,d\tau.
$$

Compute the integral:

$$
\int_{0}^{t} 2\tau\,d\tau = \left[\tau^2\right]_{0}^{t} = t^2.
$$

So:

$v(t) = 1 + t^2.$

### Step 2: Integrate velocity to get position

Use:

$$
x(t) = x(0) + \int_{0}^{t} (1+\tau^2)\,d\tau.
$$

Compute:

$$
\int_{0}^{t} (1+\tau^2)\,d\tau = \left[\tau + \frac{1}{3}\tau^3\right]_{0}^{t} = t + \frac{1}{3}t^3.
$$

So:

$$
x(t) = t + \frac{1}{3}t^3.
$$

### Step 3: Displacement from 0 to 3

Displacement is $x(3)-x(0)=x(3)$:

$$
x(3) = 3 + \frac{1}{3}(27) = 3 + 9 = 12\,\text{m}.
$$

### Optional check (velocity change)

Velocity change from 0 to 3 is:

$v(3)-v(0) = (1+9)-1 = 9\,\text{m/s},$

and also:

$$
\int_{0}^{3} 2t\,dt = \left[t^2\right]_{0}^{3} = 9,
$$

consistent.

## Mini recap

- Reconstruction pipeline:

$$
v(t) = v_0 + \int_{t_0}^{t} a(\tau)\,d\tau,
$$

$$
x(t) = x_0 + \int_{t_0}^{t} v(\tau)\,d\tau.
$$

- You generally need two initial conditions (one for $v$, one for $x$).
- Integrals have clear meanings:
  - area under $a(t)$ gives velocity change,
  - area under $v(t)$ gives displacement.
