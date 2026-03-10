# Motion from a given $v(t)$

## Learning goals

- Reconstruct position $x(t)$ from a given velocity function $v(t)$ by integration.
- Use an initial condition (e.g., $x(t_0)=x_0$) to determine the integration constant.
- Interpret displacement as an **area under the $v(t)$ graph**.
- Use the sign of $v(t)$ to reason about direction and net displacement.

## Why this matters

In experiments, velocity is often measured directly (speed sensors, motion tracking that differentiates position). In modeling, you may also be given velocity as the primary description. To recover the actual motion in space, you must integrate.

This section is also where the meaning of an integral becomes physically clear:

- integrating velocity accumulates displacement.

## Core idea

Velocity is the derivative of position:

$$
v(t) = \frac{dx}{dt}.
$$

So position is obtained by “undoing the derivative,” i.e., by integrating:

$$
x(t) = x(t_0) + \int_{t_0}^{t} v(\tau)\,d\tau.
$$

The key idea is that integration introduces an unknown constant (or equivalently, you need one position value to anchor the whole function).

## Mathematical formulation

### General reconstruction formula (1D)

If you know $v(t)$ and one initial condition $x(t_0)=x_0$, then:

$$
x(t) = x_0 + \int_{t_0}^{t} v(\tau)\,d\tau.
$If you perform an indefinite integral:$
\int v(t)\,dt = V(t) + C,
$then:$
x(t) = V(t) + C,
$$

and you determine $C$ from $x(t_0)=x_0$.

### Displacement as area under the velocity graph

Displacement from $t_1$ to $t_2$ is:

$$
\Delta x = x(t_2)-x(t_1) = \int_{t_1}^{t_2} v(t)\,dt.
$$

Graphically:

- positive area (where $v>0$) adds positive displacement,
- negative area (where $v<0$) adds negative displacement.

This is why “back and forth” motion can produce a small net displacement even if the total distance traveled is large.

### Vector extension (brief preview)

In 2D/3D:

$$
\vec{r}(t) = \vec{r}(t_0) + \int_{t_0}^{t} \vec{v}(\tau)\,d\tau,
$$

which is just the component-wise version of the 1D statement.

## Interpretation

- Integrating $v(t)$ gives position up to a constant: you need **one position value** to locate the motion in space.
- The integral over an interval gives displacement directly; it does not require you to first find $x(t)$ if you only need displacement.
- The sign of $v(t)$ tells direction: if $v<0$ over an interval, displacement over that interval is negative (for the chosen axis).

## Typical examples

1) **Constant velocity:** $v(t)=v_0$ integrates to $x(t)=x_0+v_0(t-t_0)$ (uniform motion).

2) **Linear velocity:** $v(t)=v_0+at$ integrates to a quadratic $x(t)$ (constant acceleration).

3) **Velocity that changes sign:** net displacement depends on signed areas; turning points occur where $v(t)=0$ (but you still must interpret).

## Common mistakes

- Forgetting the integration constant / failing to use the initial position to determine it.
- Treating $\int v(t)\,dt$ as “distance traveled.” It gives displacement; distance traveled would require integrating $|v(t)|$ when motion reverses.
- Mixing up the meaning of “area”: negative velocities produce negative contributions to displacement.
- Resetting time to zero for convenience and then forgetting to translate back to the original clock when combining intervals.
- Dropping units: the integral of (m/s) over s gives meters.

## Worked example

A particle moves along a line with velocity:

$$
v(t) = 4 - t
$$

for $0 \le t \le 6$, with $v$ in m/s and $t$ in s. At $t=0$, its position is:

$$
x(0)=2\,\text{m}.
$$

1) Find $x(t)$.  
2) Find the displacement from $t=0$ to $t=6$.  
3) Find the time when it changes direction, and compute the position at that time.

### Step 1: Integrate to get position

Use the reconstruction formula with $t_0=0$:

$$
x(t) = x(0) + \int_{0}^{t} (4-\tau)\,d\tau.
$Compute the integral:$
\int_{0}^{t} (4-\tau)\,d\tau = \left[4\tau - \frac{1}{2}\tau^2\right]_{0}^{t} = 4t - \frac{1}{2}t^2.
$So:$
x(t) = 2 + 4t - \frac{1}{2}t^2.
$$

### Step 2: Displacement from 0 to 6

Displacement is:

$$
\Delta x = \int_{0}^{6} (4-t)\,dt = \left[4t - \frac{1}{2}t^2\right]_{0}^{6} = 24 - 18 = 6\,\text{m}.
$$

So $x(6)=x(0)+\Delta x = 2+6 = 8\,\text{m}$ (consistent with the formula above).

### Step 3: Direction change time

Direction changes when $v(t)=0$:

$$
4 - t = 0 \;\Rightarrow\; t=4\,\text{s}.
$Compute the position at that time:$
x(4) = 2 + 4(4) - \frac{1}{2}(4)^2 = 2 + 16 - 8 = 10\,\text{m}.
$$

Interpretation: from $t=0$ to $t=4$, velocity is positive and the particle moves in the positive direction; after $t=4$, velocity is negative and it moves back.

## Mini recap

- Position from velocity (1D):

$$
x(t) = x_0 + \int_{t_0}^{t} v(\tau)\,d\tau.
$- Displacement over an interval:$
\Delta x = \int_{t_1}^{t_2} v(t)\,dt
$$

(signed area under $v(t)$).

- The integration constant is fixed by an initial position.
- Displacement is not the same as distance traveled when direction changes.
