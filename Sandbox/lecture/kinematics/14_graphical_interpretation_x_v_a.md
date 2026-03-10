# Graphical interpretation of $x(t)$, $v(t)$, and $a(t)$

## Learning goals

- Use **slope** to connect $x(t) \rightarrow v(t)$ and $v(t) \rightarrow a(t)$.
- Use **area** to connect $a(t) \rightarrow v(t)$ and $v(t) \rightarrow x(t)$ (as changes).
- Infer qualitative features (direction, speeding up/slowing down, turning points) from graphs without full algebra.
- Avoid common graph-reading traps (confusing height with slope, confusing area with value).

## Why this matters

In many real situations you do not have a clean formula—you have a graph or data. Graphical reasoning lets you answer questions like:

- “When is the particle moving forward/backward?”
- “When does it turn around?”
- “When is its speed increasing?”

without doing heavy computation. It also provides a powerful “sanity check” for algebraic work.

## Core idea

There are two fundamental links:

1) **Derivative link (slope):**

- velocity is the slope of the position graph,
- acceleration is the slope of the velocity graph.

2) **Integral link (area):**

- change in velocity is area under the acceleration graph,
- change in position is area under the velocity graph.

Once you internalize these four statements, most graph problems become systematic.

## Mathematical formulation

### Slope (derivatives)

$$
v(t) = \frac{dx}{dt}
$$

So on an $x$–$t$ graph, the slope of the tangent at time $t$ equals $v(t)$.

$$
a(t) = \frac{dv}{dt}
$$

So on a $v$–$t$ graph, the slope of the tangent at time $t$ equals $a(t)$.

### Area (integrals)

Change in velocity from $t_1$ to $t_2$:

$$
v(t_2)-v(t_1) = \int_{t_1}^{t_2} a(t)\,dt.
$Change in position from $t_1$ to $t_2$ (displacement):$
x(t_2)-x(t_1) = \int_{t_1}^{t_2} v(t)\,dt.
$$

Graphically, these are **signed areas**:

- area above the time axis contributes positively,
- area below contributes negatively.

## Interpretation

### Direction of motion (1D)

- If $v(t) > 0$, the particle moves in the positive direction.
- If $v(t) < 0$, it moves in the negative direction.

On the $x(t)$ graph, this corresponds to:

- increasing $x(t)$ → positive slope → $v>0$,
- decreasing $x(t)$ → negative slope → $v<0$.

### Turning points

A turning time occurs when the particle changes direction. In 1D this requires:

$$
v(t^*)=0
$$

and a sign change of $v$ across $t^*$.

On $x(t)$, turning points appear as local maxima/minima (slope zero and slope sign change).

### Speeding up vs slowing down (1D)

Speed increases when velocity and acceleration have the same sign.  
Speed decreases when they have opposite signs.

Graphically, on a $v(t)$ plot:

- if $v$ is positive and the graph slopes upward (positive acceleration), speed increases,
- if $v$ is positive and the graph slopes downward (negative acceleration), speed decreases,
- similarly for negative $v$ with sign logic reversed.

## Typical examples

1) **Constant velocity:** $x(t)$ is a straight line; $v(t)$ is a horizontal line; $a(t)=0$.

2) **Constant acceleration:** $v(t)$ is a straight line; $a(t)$ is a horizontal line; $x(t)$ is a parabola.

3) **Back-and-forth motion:** $v(t)$ crosses zero; $x(t)$ has peaks/valleys.

## Common mistakes

- Reading the *height* of the $x(t)$ graph as velocity. Velocity is the **slope**, not the height.
- Reading the *height* of the $v(t)$ graph as acceleration. Acceleration is the **slope** of $v(t)$.
- Confusing “area under $v(t)$” with “distance traveled.” It gives **displacement**; distance requires $\int |v(t)|dt$.
- Forgetting that areas are signed (negative velocity gives negative displacement).
- Drawing inferred graphs without matching continuity: if $x(t)$ is smooth, then $v(t)$ should be continuous; abrupt jumps in $v$ correspond to non-smooth $x(t)$.

## Worked example

You are given the following velocity–time graph description for motion in 1D:

- From $t=0$ to $t=2\,\text{s}$, velocity increases linearly from 0 to $4\,\text{m/s}$.
- From $t=2$ to $t=5\,\text{s}$, velocity is constant at $4\,\text{m/s}$.
- From $t=5$ to $t=7\,\text{s}$, velocity decreases linearly from $4\,\text{m/s}$ to $-2\,\text{m/s}$.

Assume $x(0)=0$. Find:

1) The acceleration on each interval.  
2) The displacement on each interval and the final position $x(7)$.  
3) Whether there is a turning point (direction change).

### Step 1: Acceleration from slopes of $v(t)$

Interval 0–2 s:

$$
a = \frac{4-0}{2-0} = 2\,\text{m/s}^2.
$Interval 2–5 s:$
a = 0.
$Interval 5–7 s:$
a = \frac{-2-4}{7-5} = \frac{-6}{2} = -3\,\text{m/s}^2.
$$

### Step 2: Displacement from areas under $v(t)$

Displacement is the signed area under the $v(t)$ curve.

Interval 0–2 s: triangle with base 2 and height 4:

$$
\Delta x_{0\to 2} = \frac{1}{2}(2)(4) = 4\,\text{m}.
$Interval 2–5 s: rectangle with width 3 and height 4:$
\Delta x_{2\to 5} = (3)(4) = 12\,\text{m}.
$Interval 5–7 s: trapezoid (average of endpoints times width):$
\Delta x_{5\to 7} = \frac{(4)+(-2)}{2}\cdot (2) = (1)(2) = 2\,\text{m}.
$Total displacement:$
\Delta x_{0\to 7} = 4 + 12 + 2 = 18\,\text{m}.
$Since $x(0)=0$:$
x(7)=18\,\text{m}.
$$

### Step 3: Turning point?

A turning time requires $v=0$ with sign change. On the last interval, velocity goes from +4 to −2, so it crosses zero once.

Find the crossing time. On 5–7 s the slope is −3 m/s², so:

$$
v(t) = 4 - 3(t-5).
$Set $v=0$:$
0 = 4 - 3(t-5) \;\Rightarrow\; 3(t-5)=4 \;\Rightarrow\; t=5 + \frac{4}{3} \approx 6.33\,\text{s}.
$$

So the particle changes direction at about 6.33 s.

## Mini recap

- Slope links:

$$
v(t)=\frac{dx}{dt}, \qquad a(t)=\frac{dv}{dt}.
$- Area links:$
v(t_2)-v(t_1)=\int_{t_1}^{t_2}a(t)dt, \qquad x(t_2)-x(t_1)=\int_{t_1}^{t_2}v(t)dt.
$$

- Turning points in 1D occur where $v=0$ with a sign change.
- Always ask: “Is this a slope question or an area question?”
