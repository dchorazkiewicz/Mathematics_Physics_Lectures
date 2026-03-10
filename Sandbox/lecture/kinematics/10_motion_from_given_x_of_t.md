# Motion from a given $$x(t)$$

## Learning goals

- Given a position function $$x(t)$$, compute velocity $$v(t)$$ and acceleration $$a(t)$$ by differentiation.
- Use the sign of $$v(t)$$ to determine **direction of motion** and intervals of increasing/decreasing position.
- Find **turning times** (where the motion reverses direction) and interpret them correctly.
- Connect algebraic results to graphical ideas (slope and curvature of $$x(t)$$).

## Why this matters

In many problems you are given the position as a function of time (from a model, a fit to data, or a lab measurement). Then the “kinematics task” is to extract:

- how fast it moves (velocity),
- how its motion changes (acceleration),
- whether it ever stops or reverses direction.

This is also where calculus becomes a practical tool: the derivative is not an abstract operation; it is “the velocity you would measure at that instant.”

## Core idea

If you know where a particle is at every time, you can deduce how it moves:

- velocity is the rate of change of position,
- acceleration is the rate of change of velocity.

In 1D, signs are especially informative:

- $$v>0$$ means motion in the positive direction,
- $$v<0$$ means motion in the negative direction,
- $$v=0$$ can indicate a stop or a turning point (but you must check what happens around it).

## Mathematical formulation

Given $$x(t)$$, define:

$$
v(t) = \frac{dx}{dt},
$$

$$
a(t) = \frac{dv}{dt} = \frac{d^2x}{dt^2}.
$$

### Turning times and monotonicity

Turning times are candidates where velocity is zero:

$$
v(t)=0.
$$

To decide what happens at such a time $$t^*$$, check the sign of $$v(t)$$ just before and just after $$t^*$$:

- if $$v$$ changes from positive to negative, position reaches a local maximum and motion reverses from + to −,
- if $$v$$ changes from negative to positive, position reaches a local minimum and motion reverses from − to +,
- if $$v$$ is zero but does not change sign, the particle may “pause” without reversing (possible in some functions).

### Graphical connection

On the $$x$$ vs $$t$$ graph:

- $$v(t)$$ is the tangent slope,
- $$a(t)$$ relates to how that slope changes with time (curvature idea).

## Interpretation

- Knowing $$x(t)$$ gives full kinematic information in 1D (and similarly for each component in 2D/3D).
- Zero velocity at an instant does not necessarily mean the particle stays at rest for a while; it may be a momentary turning point.
- Acceleration sign does not directly tell you direction of motion; it tells you how velocity changes.

## Typical examples

1) **Quadratic position:** $$x(t)=x_0+v_0t+\frac{1}{2}at^2$$ produces linear velocity and constant acceleration. This is the constant-acceleration model seen earlier.

2) **Cubic position:** can produce multiple turning points (stop-and-go behavior).

3) **Sinusoidal position (preview):** gives oscillatory velocity and acceleration; velocity is zero at extrema of position.

## Common mistakes

- Confusing “position is zero” with “velocity is zero.” The particle can pass through the origin with nonzero speed.
- Finding times when $$v(t)=0$$ and automatically calling them “turning points” without checking sign change.
- Interpreting negative acceleration as “slowing down” without considering the sign of velocity.
- Differentiation errors (especially product/chain rule) that then propagate into wrong physical conclusions.
- Forgetting units: if $$x$$ is in meters and $$t$$ in seconds, then $$v$$ must be in m/s and $$a$$ in m/s².

## Worked example

A particle moves along a line with position:

$$
x(t) = t^3 - 6t^2 + 9t
$$

with $$x$$ in meters and $$t$$ in seconds. Analyze its motion for $$t \ge 0$$:

1) Find $$v(t)$$ and $$a(t)$$.  
2) Determine when the particle is at rest.  
3) Determine intervals of motion direction and find any turning points.

### Step 1: Compute velocity

Differentiate:

$$
v(t) = \frac{dx}{dt} = 3t^2 - 12t + 9.
$$

Factor:

$$
v(t) = 3(t^2 - 4t + 3) = 3(t-1)(t-3).
$$

### Step 2: Compute acceleration

Differentiate velocity:

$$
a(t) = \frac{dv}{dt} = 6t - 12 = 6(t-2).
$$

### Step 3: Find rest times

Rest times satisfy $$v(t)=0$$:

$$
3(t-1)(t-3)=0 \;\Rightarrow\; t=1\,\text{s} \text{ or } t=3\,\text{s}.
$$

So the particle is instantaneously at rest at 1 s and 3 s.

### Step 4: Determine direction of motion (sign of velocity)

Use the factored form $$v(t)=3(t-1)(t-3)$$ and test intervals:

- For $$0 \le t < 1$$: pick $$t=0$$:

$$
v(0)=3(-1)(-3)=9>0,
$$

so motion is in the positive direction.

- For $$1 < t < 3$$: pick $$t=2$$:

$$
v(2)=3(1)(-1)=-3<0,
$$

so motion is in the negative direction.

- For $$t>3$$: pick $$t=4$$:

$$
v(4)=3(3)(1)=9>0,
$$

so motion is again in the positive direction.

### Step 5: Identify turning points

Velocity changes sign at both rest times:

- At $$t=1$$: $$v$$ goes from positive to negative → turning point (local maximum of $$x(t)$$).
- At $$t=3$$: $$v$$ goes from negative to positive → turning point (local minimum of $$x(t)$$).

To make this concrete, compute the positions:

$$
x(1) = 1 - 6 + 9 = 4\,\text{m},
$$

$$
x(3) = 27 - 54 + 27 = 0\,\text{m}.
$$

So the particle reaches a maximum position of 4 m at 1 s, then moves back and reaches 0 m at 3 s, then moves forward again.

### Step 6: Interpret acceleration briefly

Acceleration:

$$
a(t)=6(t-2)
$$

is negative for $$t<2$$ and positive for $$t>2$$. This tells you how the velocity is changing, but direction of motion is determined by $$v(t)$$, not by the sign of $$a(t)$$ alone.

## Mini recap

- From $$x(t)$$ you get:

$$
v(t)=\frac{dx}{dt}, \qquad a(t)=\frac{d^2x}{dt^2}.
$$

- Rest times satisfy $$v(t)=0$$, but turning points require checking whether $$v$$ changes sign.
- Sign of $$v(t)$$ determines direction in 1D.
- Graphically: $$v$$ is slope of $$x(t)$$; acceleration controls how that slope changes.
