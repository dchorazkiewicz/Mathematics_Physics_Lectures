# From force to acceleration to motion

## Learning goals

- Use the full Newtonian pipeline: forces → net force → acceleration → velocity → position.
- Decide when acceleration is constant vs time-dependent based on the force model.
- Use initial conditions correctly to obtain a unique motion.
- Compare “kinematics-first” and “dynamics-first” problem statements and see how they connect.

## Why this matters

This is the synthesis step of the course so far.

In kinematics, you often start with x(t), v(t), or a(t) given and reconstruct the rest.

In dynamics, you usually start with physical information (what forces act, what constraints apply) and your job is to determine a(t). Once you have a(t), kinematics finishes the job.

So the same kinematic formulas you already know become useful tools, but now the acceleration is not assumed; it is derived.

## Core idea

The Newtonian workflow for a particle is:

1) Choose system and axes.  
2) Draw an FBD and write the net force.  
3) Use Newton’s second law to get acceleration:

$$
\sum \vec{F} = m\vec{a}.
$$

4) Use kinematics to turn acceleration into motion:

$\vec{a}(t) \rightarrow \vec{v}(t) \rightarrow \vec{r}(t),$

with initial conditions.

If the net force is constant, acceleration is constant and you can use constant-acceleration kinematics. If the net force depends on time/position/velocity, you must integrate accordingly (sometimes solving a differential equation).

## Mathematical formulation

### The pipeline in 1D

Start with a force model:

$F_{\text{net}}(x, v, t).$

Newton’s second law gives:

$$
a(t) = \frac{d^2x}{dt^2} = \frac{F_{\text{net}}(x, v, t)}{m}.
$$

Then reconstruct:

$$
v(t) = v_0 + \int_{t_0}^{t} a(\tau)\,d\tau,
$$

$$
x(t) = x_0 + \int_{t_0}^{t} v(\tau)\,d\tau.
$$

### What changes from kinematics-only problems

In a kinematics-only problem, you might be told:

$a(t) = a_0$

and asked to find x(t).

In a dynamics problem, you are not told a(t) directly. You infer it from forces:

$$
a = \frac{F_{\text{net}}}{m}.
$$

Then you proceed exactly as in kinematics, but with a derived acceleration.

## Interpretation

- Dynamics determines a(t) by modeling interactions and constraints.
- Kinematics turns that a(t) into motion, with constants fixed by initial conditions.
- Different force models can produce the same a(t) over a limited range; dynamics is where you justify the model and check its assumptions.

## Typical examples

1) Block on a table pulled with constant force and kinetic friction: net force is constant → constant acceleration → quadratic x(t).

2) Block on an incline with kinetic friction: net force along plane is constant → constant acceleration down the plane.

3) Force varying in time (thrust schedule): a(t) varies → integrate to get v(t), x(t).

## Common mistakes

- Treating the applied force as the net force while forgetting friction or other forces.
- Jumping to constant-acceleration kinematics without first checking whether the net force is constant.
- Losing track of sign conventions (especially on inclines and in vertical motion).
- Using initial conditions from the wrong time or wrong reference position.
- Forgetting that constraints (like a_y = 0) are part of the dynamics and affect N and friction.

## Worked example

A 4.0 kg block is pulled to the right along a horizontal surface by a constant horizontal force F = 30 N. The coefficient of kinetic friction is mu_k = 0.20. Take g = 9.8 m/s^2.

At time t=0:

$x(0)=0, \qquad v(0)=1.0\,\text{m/s}.$

Find:

1) the acceleration,  
2) v(t) and x(t),  
3) the position at t = 5.0 s.

### Step 1: Force model and net force

Vertical forces balance (a_y = 0), so:

$N = mg = (4.0)(9.8) = 39.2\,\text{N}.$

Kinetic friction magnitude:

$f_k = \mu_k N = 0.20(39.2) = 7.84\,\text{N}.$

Horizontal net force:

$F_{\text{net}} = F - f_k = 30 - 7.84 = 22.16\,\text{N}.$

Direction: to the right, so acceleration is positive in the chosen x direction.

### Step 2: Acceleration from Newton’s second law

$$
a = \frac{F_{\text{net}}}{m} = \frac{22.16}{4.0} = 5.54\,\text{m/s}^2.
$$

This is constant because both F and f_k are constant in this model.

### Step 3: Use kinematics to get v(t) and x(t)

With constant acceleration:

$v(t) = v(0) + at = 1.0 + 5.54t.$

$$
x(t) = x(0) + v(0)t + \frac{1}{2}at^2 = 0 + (1.0)t + \frac{1}{2}(5.54)t^2.
$$

So:

$x(t) = t + 2.77t^2.$

### Step 4: Evaluate at t = 5.0 s

$x(5) = 5 + 2.77(25) = 5 + 69.25 = 74.25\,\text{m}.$

Interpretation: the block already has some initial speed and then accelerates strongly due to a sizeable net force.

## Mini recap

- Dynamics: find the net force and compute acceleration:

$$
a = \frac{F_{\text{net}}}{m}.
$$

- Kinematics: integrate (or use constant-acceleration formulas) to get v(t) and x(t) with initial conditions.
- Always check whether the net force is constant before using constant-acceleration kinematics.
