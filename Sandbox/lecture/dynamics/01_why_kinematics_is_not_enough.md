# Why kinematics is not enough

## Learning goals

- State clearly what kinematics provides (description of motion) and what it does not (cause/prediction from interactions).
- Explain why the same kinematic motion can be produced by different physical situations.
- Identify acceleration as the bridge quantity between kinematics and dynamics.
- Understand what question dynamics answers that kinematics cannot.

## Why this matters

Kinematics is powerful: if you know x(t) or r(t), you can compute v(t) and a(t), predict where the particle will be, and interpret graphs.

But kinematics alone cannot answer questions like:

- Why did the motion happen?
- What changes if we change the surface, the mass, or the interaction?
- What motion will occur if we specify the environment and how the object is pushed or pulled?

Those are the questions you actually care about in most real problems. To answer them, you need a way to connect motion to interactions. That connection is dynamics.

## Core idea

Kinematics describes motion as a function of time. Dynamics explains and predicts motion by modeling interactions.

The key bridge is acceleration:

- In kinematics, acceleration can be given or measured and treated as input.
- In dynamics, acceleration is not “chosen.” It is determined by the net effect of interactions, represented by forces.

So the overall pipeline becomes:

$$
\text{interactions} \rightarrow \vec{F}_{\text{net}} \rightarrow \vec{a}(t) \rightarrow \vec{v}(t) \rightarrow \vec{r}(t).
$$

Kinematics handles the right side (a to v to r). Dynamics supplies the left side (forces giving a).

## Mathematical formulation

In kinematics, the core relations are definitions:

$$
\vec{v}(t) = \frac{d\vec{r}}{dt}, \qquad \vec{a}(t) = \frac{d\vec{v}}{dt}.
$$

These relations allow you to go from r(t) to v(t) to a(t), and by integration (with initial conditions) back again.

But nowhere in kinematics is there a rule that tells you what a(t) should be in a given physical situation. Many different a(t) are mathematically possible.

Dynamics adds an additional principle (developed carefully in later sections) that connects interaction models to acceleration. In its simplest form for a particle it is:

$$
\sum \vec{F} = m\vec{a}.
$$

This is the step that makes mechanics predictive: if you can model the forces, you can determine a(t), then use kinematics to determine the motion.

## Interpretation

### Same motion, different causes

Suppose you observe that a cart moves with constant acceleration a = 1.0 m/s^2 along a track. Kinematics can describe:

$$
v(t) = v_0 + at, \qquad x(t) = x_0 + v_0 t + \frac{1}{2}at^2.
$$

But kinematics does not tell you why a is 1.0. Several physically different situations could produce the same acceleration:

- a constant engine thrust with negligible friction,
- a cart on a slight incline,
- a spring pulling near a point where its force is approximately constant over a short distance,
- a combination of forces that happens to result in the same net effect.

Dynamics is the part of the course that teaches you how to build the force model and check which situations are consistent with the motion.

### Prediction requires a model of interaction

If you change the conditions (rougher surface, heavier load, different incline angle), kinematics alone cannot tell you what will happen next, because it has no “inputs” representing those physical changes.

Dynamics introduces those inputs through interaction models (forces), and then computes the acceleration.

## Typical examples

1) **Sliding block:** Kinematics can describe the measured motion down a table. Dynamics explains the motion difference between smooth and rough surfaces via friction.

2) **Car braking:** Kinematics describes the deceleration. Dynamics connects the deceleration to braking force and tire-road interaction, which change with road conditions.

3) **Circular motion:** Kinematics says that motion at constant speed in a circle requires inward acceleration a = v^2/R. Dynamics asks: what interaction provides the inward net force?

## Common mistakes

- Treating “force” as a synonym for “motion” (as if motion itself requires a force).
- Thinking that knowing x(t) automatically tells you what forces acted. It tells you a(t), but many force scenarios can produce the same a(t).
- Assuming acceleration is always “something you choose” rather than something that can be determined by the situation.
- Mixing levels: using dynamic ideas (forces) without first doing the kinematic step of identifying v and a.

## Worked example

You observe a cart moving along a line. Its position is measured (or fitted) as:

$$
x(t) = 2 + 3t + 0.50t^2
$$

with x in meters and t in seconds.

1) Use kinematics to find v(t) and a(t).  
2) Show explicitly why kinematics alone cannot identify the physical cause of the motion.  
3) If the cart has mass m = 4.0 kg, compute the required net force in the simplest Newtonian model.

### Step 1: Compute v(t) and a(t)

Differentiate:

$$
v(t) = \frac{dx}{dt} = 3 + 1.0t.
$$

Differentiate again:

$$
a(t) = \frac{dv}{dt} = 1.0.
$$

So the acceleration is constant:

$$
a = 1.0\,\text{m/s}^2.
$$

### Step 2: Why the cause is not determined by kinematics

From the data, you can say what acceleration occurred, but you cannot uniquely say what physical situation produced it. For example, both of the following could be consistent:

- A horizontal push that results in a constant net force (after friction is accounted for).
- A cart on an incline with no other forces along the track (gravity component providing constant acceleration).

Many other combinations are possible. Kinematics does not include “incline angle,” “friction coefficient,” or “engine force” as inputs, so it cannot choose among these causes.

### Step 3: The net force in the simplest dynamic model

If you now adopt Newton’s second law as a model for particle motion, then:

$$
F_{\text{net}} = ma = (4.0)(1.0) = 4.0\,\text{N}.
$$

This is still not a complete force analysis (it does not tell you which individual forces sum to 4.0 N), but it is already a dynamics statement: it connects the observed acceleration to a required net interaction.

## Mini recap

- Kinematics describes motion: r(t), v(t), a(t) and their relations.
- Kinematics does not determine a(t) from physical conditions; many different causes can produce the same motion.
- Dynamics introduces interaction models (forces) to determine acceleration:

$$
\sum \vec{F} = m\vec{a}.
$$

- Acceleration is the bridge: dynamics determines it; kinematics integrates it into motion.
