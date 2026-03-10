# Average and instantaneous velocity

## Learning goals

- Compute **average velocity** from positions (1D and vector form).
- Understand instantaneous velocity as a **limit** and as the **derivative** of position.
- Interpret velocity graphically as the **slope** of the position–time graph.
- Distinguish **speed** from **velocity**, and interpret the sign of velocity in 1D.

## Why this matters

In everyday language “velocity” often means “how fast.” In mechanics, velocity is more precise: it tracks **rate of change of position** and therefore includes direction. Confusing velocity with speed leads to sign errors, incorrect interpretations of turning points, and misuse of formulas.

Velocity is also the first place where the meaning of a derivative becomes physically concrete: it is not just a calculus symbol; it is an operational idea connected to motion.

## Core idea

Over a time interval, you can ask:

- “How much did the position change overall?” → displacement.
- “How quickly did that change happen on average?” → average velocity.

But motion can vary within an interval. To describe the motion at a particular instant, you need:

- instantaneous velocity: the velocity “at time $$t$$,” which is the limit of average velocity over smaller and smaller time intervals.

## Mathematical formulation

### Average velocity (1D)

If the position in 1D is $$x(t)$$, then over the interval from $$t_1$$ to $$t_2$$:

$$
v_{\text{avg}} = \frac{\Delta x}{\Delta t} = \frac{x(t_2)-x(t_1)}{t_2-t_1}.
$$

This is a single number (with sign) describing the net rate of change over that interval.

### Average velocity (vector form)

In 2D/3D, position is a vector $$\vec{r}(t)$$. Average velocity is:

$$
\vec{v}_{\text{avg}} = \frac{\Delta\vec{r}}{\Delta t} = \frac{\vec{r}(t_2)-\vec{r}(t_1)}{t_2-t_1}.
$$

### Instantaneous velocity as a limit (definition)

Instantaneous velocity at time $$t$$ is the limit of average velocity as the time interval shrinks to zero:

$$
v(t) = \lim_{\Delta t\to 0} \frac{x(t+\Delta t)-x(t)}{\Delta t}.
$$

This is exactly the derivative of $$x(t)$$:

$$
v(t) = \frac{dx}{dt}.
$$

In vector form:

$$
\vec{v}(t) = \frac{d\vec{r}}{dt}.
$$

### Graphical meaning (slope)

On a graph of $$x$$ versus $$t$$:

- the average velocity over $$[t_1,t_2]$$ is the **slope of the secant line** connecting the two points,
- the instantaneous velocity at $$t$$ is the **slope of the tangent line** at that point.

So:

- steep upward slope → large positive velocity,
- flat tangent → zero velocity,
- downward slope → negative velocity.

### Speed vs velocity

In 1D:

$$
\text{speed} = |v(t)|.
$$

In 2D/3D:

$$
\text{speed} = |\vec{v}(t)|.
$$

Speed is always nonnegative; velocity can be negative in 1D or point in different directions in 2D/3D.

## Interpretation

- **Sign matters in 1D.** A negative velocity does not mean “going backwards” in any absolute sense; it means moving in the negative direction of your chosen axis.
- **Zero velocity can occur even when the particle has moved.** For example, at a turning point (motion reverses direction), the instantaneous velocity can be zero at that instant.
- **Average velocity can be zero even when there was motion.** If a particle returns to its starting point, displacement is zero, so average velocity over the full interval is zero—even though it traveled a positive distance.

## Typical examples

1) **Return trip:** Walk 50 m east, then 50 m west back to the start. Over the whole trip:

- displacement is zero,
- average velocity is zero,
- but the distance traveled is 100 m and the average speed is not zero.

2) **Turning point:** A particle moves right, slows down, stops momentarily, then moves left. The instantaneous velocity passes through zero at the turning time.

3) **2D motion:** A particle can have constant speed but changing velocity (direction change). This will matter for circular motion later.

## Common mistakes

- Mixing up **distance traveled** with **displacement** when computing average velocity.
- Saying “velocity is negative so the particle is slowing down.” Negative means direction, not necessarily slowing.
- Treating “average velocity” as if it were the velocity at the midpoint of the interval (not generally true).
- Forgetting units: velocity has units of length/time (e.g., m/s).
- Confusing speed and velocity (dropping sign/direction information).

## Worked example

A particle moves along a line with position:

$$
x(t) = 4t - t^2
$$

where $$x$$ is in meters and $$t$$ is in seconds.

### Step 1: Compute average velocity on a time interval

Find the average velocity from $$t_1=1\,\text{s}$$ to $$t_2=3\,\text{s}$$.

Compute positions:

$$
x(1) = 4(1) - 1^2 = 3\,\text{m},
$$

$$
x(3) = 4(3) - 3^2 = 12 - 9 = 3\,\text{m}.
$$

So displacement is zero:

$$
\Delta x = x(3)-x(1) = 0.
$$

Therefore:

$$
v_{\text{avg}} = \frac{\Delta x}{\Delta t} = \frac{0}{3-1} = 0\,\text{m/s}.
$$

Interpretation: over this whole interval the particle ends where it started, so its net rate of change of position is zero.

### Step 2: Compute instantaneous velocity

Differentiate:

$$
v(t) = \frac{dx}{dt} = 4 - 2t.
$$

At $$t=1\,\text{s}$$:

$$
v(1) = 4 - 2 = 2\,\text{m/s}.
$$

At $$t=3\,\text{s}$$:

$$
v(3) = 4 - 6 = -2\,\text{m/s}.
$$

So the particle is moving in the positive direction at $$t=1$$ and in the negative direction at $$t=3$$.

### Step 3: Find the turning time (where velocity is zero)

Set $$v(t)=0$$:

$$
4 - 2t = 0 \;\Rightarrow\; t = 2\,\text{s}.
$$

At $$t=2\,\text{s}$$, the particle’s velocity is zero: it is the instant when the motion reverses direction.

## Mini recap

- Average velocity:

$$
v_{\text{avg}} = \frac{x(t_2)-x(t_1)}{t_2-t_1}, \qquad \vec{v}_{\text{avg}} = \frac{\vec{r}(t_2)-\vec{r}(t_1)}{t_2-t_1}.
$$

- Instantaneous velocity is the derivative:

$$
v(t) = \frac{dx}{dt}, \qquad \vec{v}(t) = \frac{d\vec{r}}{dt}.
$$

- Graphically: velocity is the slope of the $$x(t)$$ graph (secant for average, tangent for instantaneous).
- Speed is magnitude: $$|v|$$ or $$|\vec{v}|$$; velocity includes sign/direction.
