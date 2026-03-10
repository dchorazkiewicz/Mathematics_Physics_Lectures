# Relative motion (intro)

## Learning goals

- Explain what “relative motion” means: describing motion **with respect to a moving observer**.
- Compute relative position and relative velocity in simple 1D and 2D cases.
- Use the “velocity addition” idea correctly and interpret signs/directions.
- Solve standard train/boat/walkway-style problems using a consistent notation.

## Why this matters

Many motion descriptions are implicitly relative:

- “The passenger is walking forward at 1 m/s” (relative to the train).
- “The train moves at 20 m/s” (relative to the ground).

If you do not track *relative to what*, you will add the wrong quantities and get contradictions.

Relative motion is also the first step toward understanding why the **choice of reference frame** matters. Later, in dynamics, the idea of an **inertial frame** will build on this.

## Core idea

Motion is always described relative to some reference frame. If you change the observer (frame), the numerical description of velocity changes.

In the simplest (classical) situations, velocities add in an intuitive way:

- “velocity of A relative to C” equals “velocity of A relative to B” plus “velocity of B relative to C.”

The main challenge is bookkeeping: keeping track of *which object is measured relative to which*.

## Mathematical formulation

### Notation

Let:

- A be the object of interest (e.g., a person),
- B be an intermediate frame/object (e.g., a train),
- C be a reference frame (e.g., the ground).

We write:

$$
\vec{v}_{A/B}
$$

for “velocity of A relative to B.”

### Velocity addition (Galilean, classical)

In classical mechanics (at ordinary speeds), the velocities add as:

$$
\vec{v}_{A/C} = \vec{v}_{A/B} + \vec{v}_{B/C}.
$$

This can be understood component-wise in any chosen coordinate system.

### Relative position (simple form)

Similarly for position vectors:

$$
\vec{r}_{A/C} = \vec{r}_{A/B} + \vec{r}_{B/C}.
$$

In many intro problems you can treat this as “vector from C to A equals vector from C to B plus vector from B to A,” but you should keep the labels consistent.

## Interpretation

- These addition rules are not “new physics.” They are bookkeeping rules for changing observers in classical kinematics.
- Direction matters: all velocities are vectors (in 1D, signed scalars).
- If you reverse “who is relative to whom,” the sign changes:

$$
\vec{v}_{A/B} = -\vec{v}_{B/A}.
$$

## Typical examples

1) **Walking on a train (1D):** person walks forward relative to the train while the train moves relative to the ground.

2) **Moving walkway (1D):** your speed relative to the ground depends on your walking speed relative to the belt plus the belt’s speed.

3) **Boat in a river (2D):** boat’s velocity relative to the ground equals boat relative to water plus water relative to ground (current). This naturally becomes a vector addition problem.

## Common mistakes

- Adding speeds as numbers when directions differ (must add vectors or signed 1D velocities).
- Mixing “relative to ground” and “relative to train” in the same symbol without labels.
- Using the right formula but with swapped roles (e.g., using \vec{v}_{B/C} when you needed \vec{v}_{C/B}).
- Forgetting that “straight across the river” is a constraint on the *ground* trajectory, not on the boat’s velocity relative to the water.

## Worked example

A person walks on a moving walkway in a straight corridor (1D). Choose the positive direction along the corridor.

- The walkway moves at

$$
v_{W/G} = 1.2\,\text{m/s}
$$

relative to the ground (G), where W denotes the walkway.

- The person walks at

$$
v_{P/W} = 0.8\,\text{m/s}
$$

relative to the walkway, in the positive direction.

1) Find the person’s velocity relative to the ground.  
2) How long does it take to traverse a 60 m walkway segment?

### Step 1: Add velocities with clear labels

Use:

$$
v_{P/G} = v_{P/W} + v_{W/G}.
$$

So:

$$
v_{P/G} = 0.8 + 1.2 = 2.0\,\text{m/s}.
$$

### Step 2: Use uniform motion for travel time

If velocity relative to the ground is constant, then travel time over distance 60 m is:

$$
t = \frac{\Delta x}{v_{P/G}} = \frac{60\,\text{m}}{2.0\,\text{m/s}} = 30\,\text{s}.
$$

### Variant: walking against the walkway

If the person walks opposite the belt direction with

$$
v_{P/W} = -0.8\,\text{m/s},
$$

then:

$$
v_{P/G} = -0.8 + 1.2 = 0.4\,\text{m/s},
$$

and the same 60 m would take:

$$
t = \frac{60}{0.4} = 150\,\text{s}.
$$

This illustrates why sign conventions and labels matter: the same walking effort produces very different ground motion depending on the frame’s motion.

## Mini recap

- Relative velocity notation: $$\vec{v}_{A/B}$$ means “A relative to B.”
- Classical velocity addition:

$$
\vec{v}_{A/C} = \vec{v}_{A/B} + \vec{v}_{B/C}.
$$

- Reverse relation flips sign: $$\vec{v}_{A/B}=-\vec{v}_{B/A}$$.
- In 1D, treat velocities as signed; in 2D/3D, add vectors component-wise.
