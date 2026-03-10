# Uniform motion (constant velocity)

## Learning goals

- Recognize uniform motion as motion with **constant velocity** and **zero acceleration**.
- Use the uniform-motion model to relate position and time in 1D and vector form.
- Interpret uniform motion on $$x(t)$$ and $$v(t)$$ graphs.
- Solve basic “meet/catch-up” and “when/where” problems with sign conventions.

## Why this matters

Uniform motion is the simplest nontrivial motion model:

- it is realistic over short time intervals (cruising car, conveyor belt),
- it is the baseline for interpreting graphs and signs,
- it becomes the “no net effect” case later in dynamics (Newton’s first law will tell you when constant velocity occurs).

Even here, most mistakes come not from algebra but from unclear definitions (position vs distance, sign conventions, and mixing frames).

## Core idea

If velocity is constant, then the particle covers equal displacements in equal time intervals. In 1D, “constant velocity” means:

- the position changes linearly with time,
- the direction of motion does not change (no turning point),
- acceleration is zero.

Uniform motion is a **model**: it describes situations where changes in velocity are small enough to neglect.

## Mathematical formulation

### 1D uniform motion

Assume constant velocity:

$$
v(t) = v_0 \quad \text{(constant)}.
$$

Then position is:

$$
x(t) = x_0 + v_0(t-t_0).
$$

Often we choose $$t_0=0$$ for convenience:

$$
x(t) = x_0 + v_0 t.
$$

Acceleration is the derivative of velocity:

$$
a(t) = \frac{dv}{dt} = 0.
$$

### Vector form (2D/3D)

If velocity is a constant vector $$\vec{v}_0$$, then:

$$
\vec{r}(t) = \vec{r}_0 + \vec{v}_0(t-t_0).
$$

This describes straight-line motion at constant speed in a fixed direction.

### Graphical signatures

For uniform motion in 1D:

- $$x(t)$$ is a straight line; its slope is $$v_0$$.
- $$v(t)$$ is a horizontal line at $$v_0$$.
- $$a(t)$$ is identically zero.

## Interpretation

- The sign of $$v_0$$ tells you direction along your chosen axis.
  - $$v_0>0$$: motion in the positive direction.
  - $$v_0<0$$: motion in the negative direction.
- The magnitude $$|v_0|$$ is the constant speed (in 1D).
- The same physical motion can have different coordinate descriptions if you shift the origin, but the constant velocity value does not change under an origin shift.

## Typical examples

1) **Cruising car (1D approximation):** A car moves at approximately constant speed on a straight highway segment. Over that segment, uniform motion is a good model.

2) **Moving walkway:** If you walk at constant speed relative to the walkway, and the walkway moves at constant speed relative to the ground, then your ground velocity is constant too (uniform motion), found by adding velocities (developed later).

3) **Two trains on parallel tracks:** Catch-up problems are uniform-motion problems when both trains maintain constant velocities.

## Common mistakes

- Using distance traveled in place of displacement when computing $$x(t)$$.
- Forgetting sign conventions: writing $$x(t)=x_0+|v_0|t$$ even when motion is in the negative direction.
- Mixing time origins: using $$x_0$$ measured at one time while using a formula with a different $$t_0$$.
- Assuming that “constant speed” automatically means “uniform motion” in 2D/3D. Constant speed with changing direction is **not** uniform motion because velocity is not constant.

## Worked example

Two cyclists move along a straight road (1D). Choose the x-axis along the road, with positive direction to the east.

- Cyclist A starts at the origin at $$t=0$$ and rides east at constant velocity $$v_A = 6\,\text{m/s}$$.
- Cyclist B starts 120 m east of the origin at $$t=0$$ and rides west at constant velocity $$v_B = -4\,\text{m/s}$$.

Find when and where they meet.

### Step 1: Write position functions

For cyclist A:

$$
x_A(t) = 0 + (6)t = 6t.
$$

For cyclist B:

$$
x_B(t) = 120 + (-4)t = 120 - 4t.
$$

### Step 2: Solve the meeting condition

They meet when positions are equal:

$$
x_A(t) = x_B(t).
$$

So:

$$
6t = 120 - 4t.
$$

$$
10t = 120 \;\Rightarrow\; t = 12\,\text{s}.
$$

### Step 3: Find the meeting position

Substitute back:

$$
x = x_A(12) = 6(12) = 72\,\text{m}.
$$

Interpretation: they meet 72 m east of the origin, 12 s after $$t=0$$.

### Step 4: Quick reasonableness check

The closing speed is:

$$
v_{\text{close}} = v_A - v_B = 6 - (-4) = 10\,\text{m/s}.
$$

Initial separation is 120 m, so meeting time should be:

$$
t = \frac{120}{10} = 12\,\text{s},
$$

consistent.

## Mini recap

- Uniform motion means **constant velocity** and **zero acceleration**.
- In 1D:

$$
x(t) = x_0 + v_0(t-t_0), \qquad v(t)=v_0, \qquad a(t)=0.
$$

- On graphs: $$x(t)$$ is linear; $$v(t)$$ is constant; $$a(t)=0$$.
- Keep sign conventions explicit; displacement (not distance) controls the position function.
