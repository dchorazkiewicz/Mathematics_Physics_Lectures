# Kinematics summary

## Learning goals

- Summarize what kinematics can and cannot do (describe motion, not its cause).
- Use the core relations linking position, velocity, and acceleration in 1D and vector form.
- Choose the right kinematic tool: differentiation, integration, graphs, or constant-acceleration formulas.
- Avoid the most common conceptual and sign errors.

## Why this matters

Kinematics is the language of motion. If you have a clean kinematics toolbox, you can:

- interpret data quickly,
- build correct equations in dynamics later,
- and check whether an answer is physically reasonable.

The goal of this summary is not to add new topics, but to connect the whole part into one coherent workflow.

## Core idea

Kinematics is built around three linked quantities:

- position: where the particle is,
- velocity: how position changes in time,
- acceleration: how velocity changes in time.

In 1D these are signed scalars. In 2D/3D they are vectors. In either case, the logical structure is the same:

$$
x(t) \rightarrow v(t) \rightarrow a(t)
$$

by differentiation, and:

$$
a(t) \rightarrow v(t) \rightarrow x(t)
$$

by integration plus initial conditions.

## Mathematical formulation

### Core definitions (1D)

$$
v(t) = \frac{dx}{dt}
$$

$$
a(t) = \frac{dv}{dt} = \frac{d^2x}{dt^2}
$$

Average values on an interval:

$$
v_{\text{avg}} = \frac{x(t_2)-x(t_1)}{t_2-t_1}
$$

$$
a_{\text{avg}} = \frac{v(t_2)-v(t_1)}{t_2-t_1}
$$

### Core definitions (vector form)

$$
\vec{v}(t) = \frac{d\vec{r}}{dt}
$$

$$
\vec{a}(t) = \frac{d\vec{v}}{dt} = \frac{d^2\vec{r}}{dt^2}
$$

Average velocity:

$$
\vec{v}_{\text{avg}} = \frac{\vec{r}(t_2)-\vec{r}(t_1)}{t_2-t_1}
$$

### Graph links (slope and area)

Slope:

$$
\text{slope of } x(t) \text{ is } v(t), \qquad \text{slope of } v(t) \text{ is } a(t).
$$

Area (signed):

$$
v(t_2)-v(t_1) = \int_{t_1}^{t_2} a(t)\,dt
$$

$$
x(t_2)-x(t_1) = \int_{t_1}^{t_2} v(t)\,dt
$$

### Constant acceleration (1D, model)

Assume:

$$
a(t) = a_0 \quad \text{(constant)}.
$$

Then:

$$
v(t) = v_0 + a_0(t-t_0)
$$

$$
x(t) = x_0 + v_0(t-t_0) + \frac{1}{2}a_0(t-t_0)^2
$$

and the time-free relation:

$$
v^2 = v_0^2 + 2a_0(x-x_0).
$$

### 2D motion via components

$$
\vec{r}(t) = x(t)\,\hat{i} + y(t)\,\hat{j}
$$

$$
\vec{v}(t) = v_x(t)\,\hat{i} + v_y(t)\,\hat{j}
$$

$$
\vec{a}(t) = a_x(t)\,\hat{i} + a_y(t)\,\hat{j}
$$

with:

$$
v_x=\frac{dx}{dt}, \quad v_y=\frac{dy}{dt}, \quad a_x=\frac{d^2x}{dt^2}, \quad a_y=\frac{d^2y}{dt^2}.
$$

### Circular and periodic highlights (kinematic identities)

Uniform circular motion:

$$
v = R\omega, \qquad a = \frac{v^2}{R} = R\omega^2.
$$

Period relations:

$$
T = \frac{2\pi}{\omega}, \qquad f=\frac{1}{T}, \qquad \omega = 2\pi f.
$$

## Interpretation

- Sign and direction: in 1D the sign of v tells direction; the sign of a tells how v changes, not “speeding up” by itself.
- Turning points: a turning time requires v = 0 and a sign change of v across that time.
- Displacement vs distance: displacement depends only on endpoints; distance traveled accumulates along the path and is not captured by x(t_2)-x(t_1) when direction reverses.
- Models have assumptions: constant-acceleration equations are powerful but only valid when acceleration is constant on the interval.

## Typical examples

1) Given x(t), find v(t) and a(t), locate rest times and turning points.

2) Given v(t) (or a(t)), integrate with initial conditions to get x(t).

3) Use graphs: find displacement from the area under v(t), find acceleration from slope of v(t).

4) Solve motion in 2D by separating x and y components, then recombine.

## Common mistakes

- Not stating a sign convention and then mixing “up positive” with “down positive.”
- Treating negative acceleration as “slowing down” without checking the velocity sign.
- Using distance when the formula requires displacement (especially in average velocity).
- Forgetting integration constants and initial conditions when reconstructing x(t) from v(t) or a(t).
- Applying constant-acceleration formulas to situations where acceleration varies (for example, strong air resistance).
- Inverse problems: not counting constraints vs unknown parameters and assuming uniqueness when data is insufficient.

## Worked example

A particle moves along a line. Its acceleration is piecewise constant:

- for 0 <= t <= 4 s:

$$
a(t) = 2.0\,\text{m/s}^2,
$$

- for 4 <= t <= 10 s:

$$
a(t) = -1.0\,\text{m/s}^2.
$$

At t = 0:

$$
x(0)=0, \qquad v(0)=0.
$$

Find:

1) v(t) and x(t) on both intervals,  
2) whether the particle turns around, and when,  
3) the final position x(10).

### Step 1: Interval 1 (0 to 4 s)

With constant acceleration a = 2:

$$
v(t) = v(0) + at = 2t.
$$

$$
x(t) = x(0) + v(0)t + \frac{1}{2}at^2 = t^2.
$$

Compute boundary values at t = 4:

$$
v(4)=2(4)=8\,\text{m/s},
$$

$$
x(4)=4^2=16\,\text{m}.
$$

### Step 2: Interval 2 (4 to 10 s)

Use the boundary values at t = 4 as initial conditions for the second interval. Let:

$$
\tau = t-4.
$$

On this interval, acceleration is a = -1:

$$
v(t) = v(4) + (-1)\tau = 8 - (t-4).
$$

So:

$$
v(t) = 12 - t.
$$

Position:

$$
x(t) = x(4) + v(4)\tau + \frac{1}{2}(-1)\tau^2
$$

$$
x(t) = 16 + 8(t-4) - \frac{1}{2}(t-4)^2.
$$

### Step 3: Check for a turning time

Turning time requires v(t) = 0. On interval 2:

$$
12 - t = 0 \Rightarrow t = 12\,\text{s}.
$$

But this is outside the modeled interval (t <= 10 s). Therefore, the particle does not turn around during 0 to 10 s.

### Step 4: Final position x(10)

Use the interval-2 position formula with t = 10:

$$
x(10) = 16 + 8(10-4) - \frac{1}{2}(10-4)^2.
$$

Compute:

$$
8(6)=48, \qquad \frac{1}{2}(6)^2 = 18.
$$

So:

$$
x(10) = 16 + 48 - 18 = 46\,\text{m}.
$$

## Mini recap

- Definitions:

$$
v=\frac{dx}{dt}, \qquad a=\frac{dv}{dt}.
$$

- Reconstruction:

$$
v(t)=v_0+\int_{t_0}^{t}a(\tau)\,d\tau, \qquad x(t)=x_0+\int_{t_0}^{t}v(\tau)\,d\tau.
$$

- Graphs: slope gives derivatives; signed area gives changes.
- Constant acceleration gives a linear v(t) and quadratic x(t), but only when the assumption is valid.
- Good kinematics is careful about frames, signs, units, and what is being modeled.
