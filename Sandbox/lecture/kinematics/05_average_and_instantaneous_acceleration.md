# Average and instantaneous acceleration

## Learning goals

- Compute **average acceleration** from velocity change (1D and vector form).
- Define instantaneous acceleration as a **limit** and as the **derivative** of velocity.
- Connect acceleration to the **second derivative** of position.
- Understand that acceleration can come from changing **speed** *or* changing **direction**.

## Why this matters

“Acceleration” is often misheard as “speeding up.” In mechanics, acceleration is broader: it measures how velocity changes, and velocity includes direction. This is why an object moving at constant speed around a circle is still accelerating.

Acceleration is also the key bridge quantity:

- kinematics describes motion using $$x(t), v(t), a(t)$$,
- dynamics later determines $$\vec{a}(t)$$ from forces.

So you want a clear definition and reliable interpretation now.

## Core idea

Velocity can change in two ways:

1) **Magnitude change:** speed increases or decreases (speeding up / slowing down).
2) **Direction change:** even if speed stays constant, a change in direction means the velocity vector changes.

Acceleration captures both, because it measures change in velocity.

## Mathematical formulation

### Average acceleration (1D)

If velocity in 1D is $$v(t)$$, then over $$[t_1,t_2]$$:

$$
a_{\text{avg}} = \frac{\Delta v}{\Delta t} = \frac{v(t_2)-v(t_1)}{t_2-t_1}.
$$

### Average acceleration (vector form)

In 2D/3D:

$$
\vec{a}_{\text{avg}} = \frac{\Delta\vec{v}}{\Delta t} = \frac{\vec{v}(t_2)-\vec{v}(t_1)}{t_2-t_1}.
$$

### Instantaneous acceleration (definition)

Instantaneous acceleration is the limit as the time interval shrinks:

$$
a(t) = \lim_{\Delta t\to 0} \frac{v(t+\Delta t)-v(t)}{\Delta t} = \frac{dv}{dt}.
$$

Vector form:

$$
\vec{a}(t) = \frac{d\vec{v}}{dt}.
$$

### Relation to position

Since in 1D

$$
v(t) = \frac{dx}{dt},
$$

we get

$$
a(t) = \frac{dv}{dt} = \frac{d^2x}{dt^2}.
$$

In vector form:

$$
\vec{a}(t) = \frac{d^2\vec{r}}{dt^2}.
$$

### Graphical meaning

- On a graph of $$v$$ versus $$t$$, acceleration is the slope:
  - average acceleration → slope of the secant line,
  - instantaneous acceleration → slope of the tangent line.

This is the velocity-graph analog of the “velocity is slope of the position graph” idea.

## Interpretation

### Sign and “speeding up” in 1D

In 1D, acceleration and velocity are signed. Whether the particle is speeding up depends on the *combination* of signs:

- If $$v(t)$$ and $$a(t)$$ have the **same sign**, speed increases.
- If $$v(t)$$ and $$a(t)$$ have **opposite signs**, speed decreases.

This is worth practicing, because it prevents the common mistake “negative acceleration means slowing down.” Negative acceleration only means “acceleration points in the negative axis direction.”

### Direction change without speed change (vector idea)

In 2D/3D, a velocity vector can change even if its magnitude stays the same. If speed is constant but direction rotates, then $$\vec{v}(t)$$ changes and $$\vec{a}(t)$$ is nonzero.

You will see this explicitly in circular motion later, where acceleration points inward even at constant speed.

## Typical examples

1) **Car braking while moving forward (1D):** velocity is positive, acceleration is negative. The car slows down.

2) **Car accelerating in reverse (1D):** velocity is negative, acceleration is negative. The car speeds up (in the negative direction).

3) **Uniform circular motion (preview):** speed constant, direction changing → acceleration nonzero.

## Common mistakes

- Thinking “acceleration = change in speed” instead of “change in velocity.”
- Saying “negative acceleration means slowing down” without checking the sign of velocity.
- Confusing average acceleration with instantaneous acceleration (they can differ if acceleration varies in time).
- Treating “acceleration is zero” as “velocity is zero.” Zero acceleration can mean constant nonzero velocity.
- Forgetting units: acceleration has units of length/time² (e.g., m/s²).

## Worked example

A particle moves in 1D with velocity:

$$
v(t) = 6 - 3t
$$

with $$v$$ in m/s and $$t$$ in s.

### Step 1: Find the acceleration

Differentiate:

$$
a(t) = \frac{dv}{dt} = -3.
$$

So acceleration is constant:

$$
a(t) = -3\,\text{m/s}^2.
$$

### Step 2: Interpret the sign physically

At $$t=0$$:

$$
v(0)=6\,\text{m/s} > 0,
$$

so the particle initially moves in the positive direction. Since $$a=-3<0$$, the acceleration points in the negative direction, opposite to the motion, so the particle initially **slows down**.

### Step 3: Find when it stops (turning time in velocity)

Set $$v(t)=0$$:

$$
6 - 3t = 0 \;\Rightarrow\; t = 2\,\text{s}.
$$

At $$t=2\,\text{s}$$ the instantaneous velocity is zero.

### Step 4: What happens after the stop?

For $$t>2$$:

$$
v(t) = 6 - 3t < 0,
$$

so the particle moves in the negative direction. Acceleration is still negative, so now velocity and acceleration have the same sign: the particle **speeds up** (in the negative direction).

### Step 5: Compute an average acceleration check

Compute average acceleration from $$t_1=0$$ to $$t_2=4$$:

$$
v(0)=6, \qquad v(4)=6-12=-6.
$$

$$
a_{\text{avg}} = \frac{v(4)-v(0)}{4-0} = \frac{-6-6}{4} = -3\,\text{m/s}^2,
$$

matching the constant instantaneous acceleration.

## Mini recap

- Average acceleration:

$$
a_{\text{avg}} = \frac{v(t_2)-v(t_1)}{t_2-t_1}, \qquad \vec{a}_{\text{avg}} = \frac{\vec{v}(t_2)-\vec{v}(t_1)}{t_2-t_1}.
$$

- Instantaneous acceleration:

$$
a(t) = \frac{dv}{dt}, \qquad \vec{a}(t) = \frac{d\vec{v}}{dt}.
$$

- Relation to position:

$$
a(t) = \frac{d^2x}{dt^2}, \qquad \vec{a}(t) = \frac{d^2\vec{r}}{dt^2}.
$$

- Acceleration describes change in velocity: it can arise from changing speed or changing direction.
