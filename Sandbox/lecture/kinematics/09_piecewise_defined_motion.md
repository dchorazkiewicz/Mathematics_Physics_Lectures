# Piecewise-defined motion

## Learning goals

- Read and write motion functions defined **on time intervals** (piecewise definitions).
- Enforce the correct **matching conditions** at the boundaries between intervals.
- Decide when position and velocity should be continuous, and interpret what discontinuities mean physically.
- Solve realistic “accelerate → cruise → brake” problems step by step.

## Why this matters

Real motion rarely follows one simple formula for all time. A car may:

1) accelerate from rest,
2) cruise at constant speed,
3) decelerate to a stop.

Each stage has a different kinematic rule. Piecewise modeling lets you describe such motion with simple segments while staying mathematically precise.

The main risk is inconsistency: if you choose separate formulas on each interval without matching them properly, you can accidentally create an impossible motion (teleporting position, velocity jumps without cause, etc.).

## Core idea

Piecewise motion means: “On this time interval, the motion follows one rule; on the next interval, it follows another rule.”

To make the motion physically meaningful, you typically require:

- **position continuity** at the switching time (no teleportation),
- often **velocity continuity** (no instantaneous change in velocity) unless an impulsive event occurs.

Acceleration may change suddenly (jump) when forces change suddenly (e.g., start braking). That is common and not automatically unphysical.

## Mathematical formulation

### Writing a piecewise position function

A piecewise definition has the form:

$$
x(t) =
\begin{cases}
x_1(t) & \text{for } t_0 \le t < t_1,\\
x_2(t) & \text{for } t_1 \le t < t_2,\\
\cdots
\end{cases}
$$

Similarly, you can specify $$v(t)$$ or $$a(t)$$ piecewise.

### Matching conditions at a boundary

Let the switch occur at $$t=t_1$$.

**Position continuity** means:

$$
\lim_{t\to t_1^-} x_1(t) = x_2(t_1).
$$

In many practical problems this is simply:

$$
x_1(t_1) = x_2(t_1).
$$

**Velocity continuity** means:

$$
\lim_{t\to t_1^-} v_1(t) = v_2(t_1).
$$

If velocity is discontinuous, the acceleration contains an impulse-like effect and the model is no longer “ordinary constant acceleration.” In introductory kinematics problems, velocity jumps are usually not intended unless explicitly stated (e.g., a bounce or a collision).

### A practical workflow for piecewise problems

1) Choose an axis and sign convention.  
2) Write the kinematic rule for the first interval (often constant $$a$$ or constant $$v$$).  
3) Use initial conditions to determine constants.  
4) Evaluate $$x$$ and $$v$$ at the switching time to generate the initial conditions for the next interval.  
5) Repeat.

## Interpretation

- A piecewise model describes a **single motion** with different regimes.
- Position continuity is a basic physical requirement for ordinary motion.
- Velocity continuity is typical unless an impulsive event occurs.
- Acceleration can change abruptly because it reflects changing influences (engine on/off, braking, friction changes).

## Typical examples

1) **Accelerate then cruise:** constant $$a$$ for a while, then constant $$v$$ after reaching a target speed.

2) **Cruise then brake:** constant $$v$$, then constant negative $$a$$ until stopping.

3) **Motion with a “turnaround”:** accelerate negatively until velocity becomes zero, then continue with negative velocity (a reversal) — still continuous, no teleportation.

## Common mistakes

- Using the same symbol $$x_0, v_0$$ for different intervals without clarifying which interval’s initial time they belong to.
- Forgetting to carry the end-of-interval position into the next interval (creating a jump in $$x$$).
- Assuming velocity is the same at the boundary even when acceleration was nonzero (or vice versa).
- Solving each interval independently with $$t=0$$ reset, then mixing times without converting (time variables must refer to the same clock unless you explicitly reparameterize).
- Interpreting “piecewise acceleration” as “piecewise position” automatically; you must integrate and apply boundary conditions.

## Worked example

A car moves along a straight road (1D). Choose x-axis along the road, positive forward. The motion has three stages:

1) **Stage I (accelerate):** from $$t=0$$ to $$t=6\,\text{s}$$ the car accelerates uniformly from rest with

$$
a = 2.0\,\text{m/s}^2.
$$

2) **Stage II (cruise):** from $$t=6\,\text{s}$$ to $$t=16\,\text{s}$$ the car moves at constant velocity.

3) **Stage III (brake):** from $$t=16\,\text{s}$$ onward it brakes with constant acceleration

$$
a = -3.0\,\text{m/s}^2
$$

until it stops.

Find:

- the piecewise formulas for $$v(t)$$ and $$x(t)$$ (with $$x(0)=0$$),
- the total distance traveled until the car stops.

### Step 0: Initial condition

At $$t=0$$:

$$
x(0)=0, \qquad v(0)=0.
$$

### Stage I: $$0 \le t \le 6$$

Velocity:

$$
v(t) = v_0 + at = 0 + (2.0)t = 2t.
$$

Position:

$$
x(t) = x_0 + v_0 t + \frac{1}{2}at^2 = 0 + 0 + \frac{1}{2}(2.0)t^2 = t^2.
$$

Evaluate at the boundary $$t=6$$ to pass initial conditions to Stage II:

$$
v(6) = 2\cdot 6 = 12\,\text{m/s},
$$

$$
x(6) = 6^2 = 36\,\text{m}.
$$

### Stage II: $$6 \le t \le 16$$

Constant velocity equal to the value reached at $$t=6$$:

$$
v(t) = 12\,\text{m/s}.
$$

Position must be continuous and should satisfy $$x(6)=36$$. A convenient form is:

$$
x(t) = x(6) + v(t-6) = 36 + 12(t-6).
$$

Evaluate at $$t=16$$:

$$
x(16) = 36 + 12(16-6) = 36 + 120 = 156\,\text{m},
$$

$$
v(16) = 12\,\text{m/s}.
$$

### Stage III: $$t \ge 16$$

Now acceleration is constant $$a=-3.0\,\text{m/s}^2$$ and initial conditions at $$t=16$$ are:

$$
x(16)=156\,\text{m}, \qquad v(16)=12\,\text{m/s}.
$$

Velocity for $$t\ge 16$$:

$$
v(t) = 12 - 3(t-16).
$$

The car stops when $$v(t)=0$$:

$$
0 = 12 - 3(t-16) \;\Rightarrow\; 3(t-16)=12 \;\Rightarrow\; t-16=4.
$$

So stopping time is:

$$
t_{\text{stop}} = 20\,\text{s}.
$$

Position for $$t\ge 16$$:

$$
x(t) = 156 + 12(t-16) + \frac{1}{2}(-3)(t-16)^2
$$

At stopping time $$t=20$$ (so $$t-16=4$$):

$$
x(20) = 156 + 12\cdot 4 - \frac{3}{2}\cdot 4^2 = 156 + 48 - 24 = 180\,\text{m}.
$$

So the total distance traveled (since motion is forward throughout) is:

$$
180\,\text{m}.
$$

### Summary of the piecewise functions

Velocity:

$$
v(t) =
\begin{cases}
2t & 0 \le t \le 6,\\
12 & 6 \le t \le 16,\\
12 - 3(t-16) & 16 \le t \le 20.
\end{cases}
$$

Position:

$$
x(t) =
\begin{cases}
t^2 & 0 \le t \le 6,\\
36 + 12(t-6) & 6 \le t \le 16,\\
156 + 12(t-16) - \frac{3}{2}(t-16)^2 & 16 \le t \le 20.
\end{cases}
$$

Notice how each stage uses boundary values from the previous stage to guarantee continuity.

## Mini recap

- Piecewise motion uses different rules on different time intervals:

$$
x(t)=\begin{cases}x_1(t) & t_0\le t<t_1\\ x_2(t) & t_1\le t<t_2\end{cases}
$$

- Match conditions at boundaries:
  - usually require position continuity,
  - often require velocity continuity unless an impulse-like event is intended.
- Workflow: solve interval 1 → evaluate $$x, v$$ at boundary → use them as initial conditions for interval 2.
- Acceleration can change abruptly between intervals without being unphysical.
