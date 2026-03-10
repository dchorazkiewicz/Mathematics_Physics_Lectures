# 2D motion and components

## Learning goals

- Describe planar motion using a position vector and component functions.
- Compute velocity and acceleration vectors component-wise and interpret them geometrically.
- Use the **independence of orthogonal components** to solve 2D kinematics problems systematically.
- Convert between vector form and coordinate form, and check consistency of units and signs.

## Why this matters

Most interesting motions are not purely 1D: projectiles, circular motion, and relative motion in a plane all require 2D thinking.

The good news is that 2D kinematics is not “harder calculus.” It is mostly good bookkeeping:

- choose axes,
- write component functions,
- apply 1D kinematics separately in each direction,
- then recombine into a vector picture.

This component approach is the backbone of projectile motion later.

## Core idea

In the plane, position has two coordinates. If you choose perpendicular axes with unit vectors:

$$
\hat{i}, \qquad \hat{j},
$$

then the position vector is:

$$
\vec{r}(t) = x(t)\,\hat{i} + y(t)\,\hat{j}.
$$

Differentiation applies component-wise:

$$
\vec{v}(t) = \frac{d\vec{r}}{dt} = \frac{dx}{dt}\,\hat{i} + \frac{dy}{dt}\,\hat{j},
$$

$$
\vec{a}(t) = \frac{d\vec{v}}{dt} = \frac{d^2x}{dt^2}\,\hat{i} + \frac{d^2y}{dt^2}\,\hat{j}.
$$

So planar kinematics is “two linked 1D problems” that share the same time variable t.

To keep notation explicit:

$$
t
$$

## Mathematical formulation

### Component definitions

Define velocity components:

$$
v_x(t) = \frac{dx}{dt}, \qquad v_y(t) = \frac{dy}{dt}.
$$

Then:

$$
\vec{v}(t) = v_x(t)\,\hat{i} + v_y(t)\,\hat{j}.
$$

Define acceleration components:

$$
a_x(t) = \frac{dv_x}{dt} = \frac{d^2x}{dt^2}, \qquad a_y(t) = \frac{dv_y}{dt} = \frac{d^2y}{dt^2},
$$

and:

$$
\vec{a}(t) = a_x(t)\,\hat{i} + a_y(t)\,\hat{j}.
$$

### Independence of orthogonal components (what it really means)

If you know the acceleration components as functions of time, you can solve for the corresponding position components separately using 1D methods:

$$
a_x(t) \rightarrow v_x(t) \rightarrow x(t),
$$

$$
a_y(t) \rightarrow v_y(t) \rightarrow y(t).
$$

The coupling between the components is only through the shared time variable t. There is no rule that says “a change in x must cause a change in y” unless the problem imposes a constraint (like motion along a fixed track).

### Speed from components

The speed is the magnitude of the velocity vector:

$$
|\vec{v}(t)| = \sqrt{v_x(t)^2 + v_y(t)^2}.
$$

This is often where students accidentally confuse “constant v_x” with “constant speed.” Even if v_x is constant, speed can change because v_y changes.

## Interpretation

- The velocity vector points in the instantaneous direction of motion; it is tangent to the trajectory.
- The acceleration vector tells you how the velocity changes; it can change the speed, the direction, or both.
- Component equations are not “less physical” than vector equations. They are the same physics expressed in a coordinate system.

## Typical examples

1) **Constant-velocity motion at an angle:** both x(t) and y(t) are linear in t. The trajectory is a straight line.

2) **Projectile motion preview:** horizontal acceleration is zero while vertical acceleration is constant (gravity):

$$
a_x = 0, \qquad a_y = \text{constant}.
$$

Horizontal and vertical motions are solved independently and then combined.

3) **River crossing:** the boat’s ground velocity is a vector sum of “boat relative to water” and “water relative to ground.”

## Common mistakes

- Treating v_x and v_y as if they were magnitudes (forgetting signs or direction).
- Mixing vector magnitudes with components (e.g., writing a projection relation but using the wrong angle definition):

$$
v_x = |\vec{v}|\cos\theta.
$$
- Thinking “constant v_x” means “constant speed.”
- Forgetting that the same time t must be used in both components.
- Switching axes mid-solution without updating component definitions.

## Worked example

A particle moves in the plane with position components:

$$
x(t) = 3t, \qquad y(t) = 2t - t^2,
$$

with x and y in meters and t in seconds.

1) Find:

$$
\vec{v}(t) \quad \text{and} \quad \vec{a}(t).
$$

2) Find the speed at:

$$
t=1\,\text{s}.
$$

3) Determine when the particle is moving upward vs downward.

### Step 1: Differentiate to get velocity components

$$
v_x(t) = \frac{dx}{dt} = 3,
$$

$$
v_y(t) = \frac{dy}{dt} = 2 - 2t.
$$

So:

$$
\vec{v}(t) = 3\,\hat{i} + (2-2t)\,\hat{j}.
$$

### Step 2: Differentiate again to get acceleration components

$$
a_x(t) = \frac{dv_x}{dt} = 0,
$$

$$
a_y(t) = \frac{dv_y}{dt} = -2.
$$

So:

$$
\vec{a}(t) = 0\,\hat{i} + (-2)\,\hat{j} = -2\,\hat{j}.
$$

Interpretation: acceleration is constant downward (negative y-direction), while the horizontal velocity stays constant.

### Step 3: Speed at t = 1 s

Compute components at t = 1:

$$
v_x(1) = 3, \qquad v_y(1) = 2-2(1) = 0.
$$

So:

$$
|\vec{v}(1)| = \sqrt{3^2 + 0^2} = 3\,\text{m/s}.
$$

### Step 4: Upward vs downward motion

The motion is upward when v_y(t) > 0 and downward when v_y(t) < 0.

Solve v_y(t) = 0:

$$
2 - 2t = 0 \Rightarrow t = 1\,\text{s}.
$$

So:

- for 0 \le t < 1, v_y > 0 (moving upward),
- for t > 1, v_y < 0 (moving downward).

Notice that the particle can be moving downward while still moving to the right, because v_x stays positive.

## Mini recap

- Planar motion:

$$
\vec{r}(t) = x(t)\,\hat{i} + y(t)\,\hat{j}.
$$

- Component-wise differentiation:

$$
\vec{v}(t) = v_x\,\hat{i} + v_y\,\hat{j}, \qquad v_x=\frac{dx}{dt}, \quad v_y=\frac{dy}{dt},
$$

$$
\vec{a}(t) = a_x\,\hat{i} + a_y\,\hat{j}, \qquad a_x=\frac{d^2x}{dt^2}, \quad a_y=\frac{d^2y}{dt^2}.
$$

- Orthogonal components are solved independently (same time t, separate 1D kinematics).
- Speed is magnitude:

$$
|\vec{v}|=\sqrt{v_x^2+v_y^2}.
$$
