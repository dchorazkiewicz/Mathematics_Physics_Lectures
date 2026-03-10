# Uniformly accelerated motion (constant acceleration)

## Learning goals

- Recognize when the **constant-acceleration model** is appropriate and state its assumptions.
- Derive and use the standard relations for $v(t)$ and $x(t)$ under constant $a$.
- Use initial conditions correctly and interpret the meaning of $x_0$ and $v_0$.
- Solve basic constant-acceleration problems without “formula hunting,” and check results by units/signs.

## Why this matters

Constant acceleration is the next simplest model after uniform motion. It appears everywhere:

- near-Earth free fall (approximately constant $g$, neglecting air resistance),
- vehicles speeding up or braking at roughly steady rate,
- motion segments that can be approximated as having constant acceleration.

Many students memorize “the kinematic equations” without understanding where they come from. That leads to sign errors and applying them when the assumptions are not satisfied. Here we will derive them from the definitions of velocity and acceleration.

## Core idea

If acceleration is constant, then velocity changes at a constant rate, and position is a quadratic function of time.

The model is a statement about time dependence:

$a(t) = a_0 \quad \text{(constant)}.$

From this one assumption, the entire motion follows once you specify initial conditions.

## Mathematical formulation

### Assumptions (say them explicitly when you use the model)

We assume:

1. Motion is along a straight line (1D) or we are analyzing one component.
2. Acceleration is constant in time over the interval of interest:

$a(t) = a_0.$

3. The quantities $x_0$ and $v_0$ are the position and velocity at a chosen reference time $t_0$.

### Step 1: Derive velocity as a function of time

By definition:

$$
a(t) = \frac{dv}{dt}.
$$

If $a(t)=a_0$ is constant, then:

$$
\frac{dv}{dt} = a_0.
$$

Integrate from $t_0$ to $t$:

$$
\int_{v(t_0)}^{v(t)} dv = \int_{t_0}^{t} a_0\,dt.
$$

This gives:

$v(t) - v(t_0) = a_0(t-t_0).$

Define $v_0 = v(t_0)$, so:

$v(t) = v_0 + a_0(t-t_0).$

If we choose $t_0=0$:

$v(t) = v_0 + a_0 t.$

### Step 2: Derive position as a function of time

Velocity is the derivative of position:

$$
v(t) = \frac{dx}{dt}.
$$

Using $v(t)=v_0+a_0(t-t_0)$:

$$
\frac{dx}{dt} = v_0 + a_0(t-t_0).
$$

Integrate from $t_0$ to $t$:

$$
\int_{x(t_0)}^{x(t)} dx = \int_{t_0}^{t} \left(v_0 + a_0(\tau-t_0)\right)d\tau.
$$

Compute the integral:

$$
x(t) - x(t_0) = v_0(t-t_0) + \frac{1}{2}a_0(t-t_0)^2.
$$

Define $x_0 = x(t_0)$:

$$
x(t) = x_0 + v_0(t-t_0) + \frac{1}{2}a_0(t-t_0)^2.
$$

If $t_0=0$:

$$
x(t) = x_0 + v_0 t + \frac{1}{2}a_0 t^2.
$$

### A useful relation without time (optional but common)

Sometimes you want a relation between velocity and position when acceleration is constant. Start from:

$v(t) = v_0 + a_0(t-t_0),$

and

$$
x(t) - x_0 = v_0(t-t_0) + \frac{1}{2}a_0(t-t_0)^2.
$$

Eliminate $t-t_0$. Let $\Delta t = t-t_0$. Then:

$$
v - v_0 = a_0\Delta t \quad \Rightarrow\quad \Delta t = \frac{v-v_0}{a_0}.
$$

Substitute into the position equation:

$$
x - x_0 = v_0\left(\frac{v-v_0}{a_0}\right) + \frac{1}{2}a_0\left(\frac{v-v_0}{a_0}\right)^2.
$$

After simplification, you obtain:

$v^2 = v_0^2 + 2a_0(x-x_0).$

This relation is powerful, but it is still based on the same constant-acceleration assumption.

## Interpretation

- Constant acceleration means **velocity changes linearly** in time.
- Position is a quadratic in time; its graph is a parabola in the $x$–$t$ plane.
- Initial conditions matter:
  - $x_0$ is where the particle is at the chosen reference time.
  - $v_0$ is the velocity at that same time.
  - changing the choice of $t_0$ changes the numerical values of $x_0$ and $v_0$, but not the physical motion.

## Typical examples

1) **Braking car (1D):** If deceleration is approximately constant, you can predict stopping time and stopping distance.

2) **Free fall preview:** Over not-too-large height changes near Earth, acceleration is approximately constant and equal to $\pm g$ depending on your sign convention.

3) **Piecewise motion preview:** Real motion is often “constant acceleration for a while, then different constant acceleration,” which we will treat later as piecewise-defined motion.

## Common mistakes

- Using constant-acceleration formulas when acceleration is not constant (e.g., strong air resistance, changing engine force).
- Forgetting that the sign of $a_0$ depends on the chosen axis direction.
- Plugging numbers into a memorized equation without stating $x_0, v_0, t_0$ (mixing different reference times).
- Using $v^2 = v_0^2 + 2a_0(x-x_0)$ and then forgetting that squaring hides sign information: $v$ can be positive or negative depending on direction.
- Confusing “acceleration is constant” with “velocity is constant.” Constant acceleration generally means velocity is changing.

## Worked example

A train moves along a straight track. At $t=0$, it passes a marker with:

$x_0 = 0, \qquad v_0 = 12\,\text{m/s}.$

It then accelerates uniformly with:

$a_0 = 0.80\,\text{m/s}^2$

for 15 s.

1) Find its velocity and position at $t=15\,\text{s}$.  
2) How far does it travel during the *last* 5 s of this interval?

### Step 1: Velocity after 15 s

Use:

$v(t) = v_0 + a_0 t.$

So:

$v(15) = 12 + (0.80)(15) = 12 + 12 = 24\,\text{m/s}.$

### Step 2: Position after 15 s

Use:

$$
x(t) = x_0 + v_0 t + \frac{1}{2}a_0 t^2.
$$

So:

$$
x(15) = 0 + (12)(15) + \frac{1}{2}(0.80)(15)^2.
$$

Compute:

$(12)(15)=180,$

$$
\frac{1}{2}(0.80)(15)^2 = 0.40\cdot 225 = 90.
$$

Therefore:

$x(15) = 180 + 90 = 270\,\text{m}.$

### Step 3: Distance traveled in the last 5 seconds

The last 5 s is the interval from $t=10$ to $t=15$.

Compute:

$$
x(10) = (12)(10) + \frac{1}{2}(0.80)(10)^2 = 120 + 0.40\cdot 100 = 120 + 40 = 160\,\text{m}.
$$

Then:

$\Delta x = x(15)-x(10) = 270 - 160 = 110\,\text{m}.$

### Step 4: Quick checks

- Units: each term in $x(t)$ has units of meters.
- Reasonableness: the average velocity over the 15 s is roughly halfway between 12 and 24 m/s, i.e. about 18 m/s, so distance should be about $18\cdot 15 = 270$ m, matching.

## Mini recap

- Constant acceleration model:

$a(t)=a_0.$

- Derived relations (with reference time $t_0$):

$v(t) = v_0 + a_0(t-t_0),$

$$
x(t) = x_0 + v_0(t-t_0) + \frac{1}{2}a_0(t-t_0)^2.
$$

- Time-free relation (still constant-acceleration only):

$v^2 = v_0^2 + 2a_0(x-x_0).$

- State assumptions and sign conventions; use initial conditions consistently.
