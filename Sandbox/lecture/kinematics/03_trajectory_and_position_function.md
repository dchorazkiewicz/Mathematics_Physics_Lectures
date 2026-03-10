# Trajectory and position function

## Learning goals

- Distinguish the **trajectory** (geometric path in space) from the **law of motion** (position as a function of time).
- Describe planar motion using a position vector $\vec{r}(t)$ or component functions $x(t), y(t)$.
- Eliminate time (when appropriate) to obtain an equation for the trajectory, and understand what information is lost.
- Recognize that different time dependences can produce the **same trajectory**.

## Why this matters

Students often say “the trajectory is $x(t)$” or think that a curve like a parabola fully determines the motion. But a curve in space only tells you **where** the particle can be; it does not tell you **when** the particle is at each point, how fast it moves along the curve, or in which direction it is traversed.

Mechanics needs both:

- **Geometry:** the set of points the particle visits (trajectory).
- **Timing:** how position changes with time (position function).

This distinction becomes essential in later topics like projectile motion and circular motion, where geometry alone can be misleading.

## Core idea

Think of a motion as a movie:

- The **trajectory** is like a long-exposure photograph of the moving object: it shows the shape traced out in space.
- The **position function** tells you the full movie frame-by-frame: it encodes timing and therefore speed and direction.

In 1D, the “trajectory” is just a line (the x-axis); timing still matters, but geometry is trivial. In 2D/3D, geometry becomes informative, but it is still not the whole story.

## Mathematical formulation

### Position as a function of time (law of motion)

In 2D, the motion is described by:

$\vec{r}(t) = x(t)\,\hat{i} + y(t)\,\hat{j}$

Equivalently, you can specify the pair of component functions:

$x(t), \qquad y(t).$

This is the **law of motion**: it tells you where the particle is at each time.

### Trajectory as a geometric set

The **trajectory** is the set of points in the plane that the particle occupies at some time:

$\{(x(t), y(t)) \;\text{for all relevant } t\}.$

Often (but not always) you can eliminate $t$ between $x(t)$ and $y(t)$ to get a relation between $x$ and $y$:

$F(x,y) = 0.$

That relation describes a curve in space: the trajectory (or a part of it).

### What you lose when you eliminate time

If you eliminate $t$ and obtain a curve equation, you typically lose:

- the **speed** along the curve (fast vs slow),
- the **direction** of travel (which way along the curve),
- the **timing** (where the particle is at a specific time),
- how many times the particle passes the same point (possible in loops/oscillations).

## Interpretation

Two motions can share the same trajectory but be physically very different. For example, moving along the same circle at different speeds gives the same trajectory (a circle) but different velocity and acceleration as functions of time.

Conversely, two motions can have very different trajectories even if their speed functions look similar: geometry depends on the direction of motion, not just the magnitude.

## Typical examples

1) **1D motion:** A particle moves along a line. The trajectory is the x-axis (or a segment of it). The interesting part is the timing: when does it pass a point, does it reverse direction, etc.

2) **Uniform circular motion:** The trajectory is a circle, but the position function can describe going around the circle quickly or slowly (different periods).

3) **Projectile motion preview:** The trajectory under uniform gravity (neglecting air resistance) is a parabola, but the same parabola could correspond to different launch speeds if the timing is changed (for example, by reparameterizing time).

## Common mistakes

- Treating a curve equation like $y = f(x)$ as “the full motion” (it is only geometry, not timing).
- Confusing the **path length** (distance traveled along the curve) with displacement.
- Assuming that if two motions have the same trajectory, then they have the same velocity/acceleration at corresponding points (not true without timing information).
- Eliminating time incorrectly (for example, dividing by an expression that could be zero without checking).
- Forgetting that a single point on the trajectory may correspond to multiple times (especially in periodic motion).

## Worked example

Consider the planar motion defined by:

$x(t) = 2t, \qquad y(t) = t^2,$

for $t \ge 0$.

### Step 1: Identify what the law of motion tells you

At each time $t$, the position is:

$\vec{r}(t) = (2t)\,\hat{i} + (t^2)\,\hat{j}.$

This already answers questions like “Where is the particle at $t=3\,\text{s}$?”:

$x(3)=6, \qquad y(3)=9.$

### Step 2: Find the trajectory by eliminating time

From $x(t)=2t$ we solve for $t$:

$$
t = \frac{x}{2}.
$$

Substitute into $y(t)=t^2$:

$$
y = \left(\frac{x}{2}\right)^2 = \frac{x^2}{4}.
$$

So the trajectory is the parabola:

$$
y = \frac{x^2}{4}, \qquad x \ge 0.
$$

This describes the *shape* of the path in the plane.

### Step 3: Show that the same trajectory can come from a different time dependence

Define a new motion:

$\tilde{x}(t) = 2t^2, \qquad \tilde{y}(t) = t^4,$

for $t \ge 0$.

Eliminate time again. From $\tilde{x}(t)=2t^2$:

$$
t^2 = \frac{\tilde{x}}{2}.
$$

Then

$$
\tilde{y} = t^4 = \left(t^2\right)^2 = \left(\frac{\tilde{x}}{2}\right)^2 = \frac{\tilde{x}^2}{4}.
$$

So the **trajectory is the same parabola**, but the timing is different: the second motion moves along the curve more slowly near the origin (because $\tilde{x}(t)$ grows like $t^2$, not like $t$).

### Step 4: What did the curve equation fail to tell you?

The curve

$$
y = \frac{x^2}{4}
$$

does not tell you:

- whether the particle reaches a given point at time 1 s or 10 s,
- how fast it moves along the curve at a given moment,
- whether it ever stops or reverses direction (in other examples).

That information lives in the full functions $x(t), y(t)$.

## Mini recap

- The **law of motion** specifies position as a function of time:

$\vec{r}(t) = x(t)\,\hat{i} + y(t)\,\hat{j}.$

- The **trajectory** is the set of points visited in space; you can sometimes find it by eliminating $t$.
- Eliminating time gives geometry but typically loses timing, speed, and direction information.
- Different time dependences can produce the same trajectory.
