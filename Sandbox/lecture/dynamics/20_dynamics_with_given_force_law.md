# Dynamics with a given force law

## Learning goals

- Translate a force law into an equation of motion using Newton’s second law.
- Recognize force laws depending on time, position, or velocity and what that implies about acceleration.
- Use initial conditions to determine a unique motion.
- Solve simple cases and interpret what the model assumes physically.

## Why this matters

In dynamics problems, the central input is not x(t). It is a force model:

- “The net force is constant.”
- “The force depends on position.”
- “The force depends on velocity (drag).”
- “The applied force varies with time.”

Each of these leads to a different kind of equation of motion. If you can translate a force law into a differential equation, you can connect dynamics back to kinematics systematically.

## Core idea

Force laws are model statements of the form:

$$
F_{\text{net}} = F(x, v, t).
$$

Newton’s second law then gives:

$$
m\frac{d^2x}{dt^2} = F\left(x, \frac{dx}{dt}, t\right).
$$

The “difficulty” of the dynamics problem is usually the difficulty of solving that equation.

But before solving, you must interpret the model:

- What is being neglected?
- Over what range is the force law expected to be valid?
- Are we modeling a net force or an individual force?

## Mathematical formulation

### Case A: time-dependent force F(t)

If:

$$
F_{\text{net}} = F(t),
$$

then:

$$
a(t) = \frac{F(t)}{m}.
$$

This becomes a kinematics reconstruction problem:

$$
a(t) \rightarrow v(t) \rightarrow x(t),
$$

using integration and initial conditions.

### Case B: position-dependent force F(x)

If:

$$
F_{\text{net}} = F(x),
$$

then:

$$
m\frac{d^2x}{dt^2} = F(x).
$$

Acceleration depends on position, so it is generally not constant. A classic example is a spring:

$$
F(x) = -kx.
$$

### Case C: velocity-dependent force F(v)

If:

$$
F_{\text{net}} = F(v),
$$

then:

$$
m\frac{dv}{dt} = F(v).
$$

This is a differential equation for v(t). A simple linear drag model is:

$$
F(v) = -bv,
$$

leading to:

$$
m\frac{dv}{dt} = -bv.
$$

### Case D: combined dependence F(x, v, t)

Many real systems have forces depending on multiple variables (e.g., gravity + drag + time-varying thrust). The same translation step applies; solving may require more advanced methods or approximations.

## Interpretation

- Force laws are not always exact. They are approximations valid in specified regimes.
- A force law should be read as a statement about a specific interaction or about the net force, depending on context.
- If you are given a force law, you should still draw an FBD to clarify which forces are included and what direction the force acts in.

## Typical examples

1) Rocket thrust schedule F(t): acceleration changes in time; integrate to get v(t) and x(t).

2) Spring force F(x) = -kx: acceleration depends on x; motion becomes oscillatory.

3) Linear drag F(v) = -bv: velocity decays exponentially toward zero (if no other forces act).

## Common mistakes

- Treating a force law as if it automatically gives constant acceleration.
- Forgetting that if F depends on x or v, then acceleration changes during the motion.
- Ignoring sign: writing “F = kx” instead of “F = -kx” for restoring springs.
- Mixing up net force with an individual force (e.g., treating a given applied force as the net force while friction is present).
- Using initial conditions inconsistently (wrong reference time).

## Worked example

A particle of mass m = 2.0 kg moves along a line. The net force is time-dependent:

$$
F_{\text{net}}(t) = 6t\,\text{N}.
$$

At t = 0:

$$
x(0)=1\,\text{m}, \qquad v(0)=0.
$$

Find a(t), v(t), and x(t).

### Step 1: Acceleration from the force law

Newton’s second law:

$$
a(t) = \frac{F_{\text{net}}(t)}{m} = \frac{6t}{2.0} = 3t.
$$

So:

$$
a(t) = 3t\,\text{m/s}^2.
$$

### Step 2: Integrate to get velocity

$$
v(t) = v(0) + \int_0^t a(\tau)\,d\tau = 0 + \int_0^t 3\tau\,d\tau.
$$

Compute:

$$
v(t) = \left[\frac{3}{2}\tau^2\right]_0^t = \frac{3}{2}t^2.
$$

So:

$$
v(t) = 1.5t^2\,\text{m/s}.
$$

### Step 3: Integrate to get position

$$
x(t) = x(0) + \int_0^t v(\tau)\,d\tau = 1 + \int_0^t 1.5\tau^2\,d\tau.
$$

Compute:

$$
x(t) = 1 + \left[0.5\tau^3\right]_0^t = 1 + 0.5t^3.
$$

So:

$$
x(t) = 1 + 0.5t^3\,\text{m}.
$$

### Step 4: Interpretation

Because the force grows in time, acceleration grows in time, so velocity grows faster than linearly and position grows faster than quadratically.

This example shows how a time-dependent force turns dynamics into a kinematics reconstruction problem.

## Mini recap

- Translate force laws into equations of motion using:

$$
m\frac{d^2x}{dt^2} = F\left(x, \frac{dx}{dt}, t\right).
$$

- If F depends only on t, then a(t) is known and you integrate to get v(t) and x(t).
- If F depends on x or v, acceleration is not constant; you generally get a differential equation that may be harder to solve.
- Always interpret the force law as a model with assumptions and a regime of validity.
