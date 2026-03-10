# Concept of force

## Learning goals

- Describe force as a model of interaction (not “stored motion” and not a mysterious cause).
- Explain why force is a vector quantity and how forces combine.
- Distinguish common interaction types: contact forces and long-range forces.
- Use units correctly (newton) and interpret what a force measurement means operationally.

## Why this matters

Dynamics is built around one central question:

Given a physical situation, what acceleration will occur?

To answer that, we need a language for interactions. Force is that language in Newtonian mechanics. But the word “force” comes with many misconceptions, so we start with a careful, operational meaning:

- a force is something you can infer from interaction effects and measure with instruments,
- it has direction as well as magnitude,
- and multiple forces can act at the same time.

## Core idea

Force is a model for an interaction between bodies (or between a body and an environment). Examples:

- a hand pushes a cart (contact interaction),
- Earth attracts a ball (gravitational interaction),
- a stretched spring pulls (elastic interaction),
- a surface resists penetration and may resist sliding (normal and friction interactions).

The same body can experience several interactions at once. Dynamics is about accounting for all of them and combining them into a net effect.

## Mathematical formulation

### Force as a vector

Force has magnitude and direction, so we represent it by a vector:

$$
\vec{F}.
$$

In 2D (Cartesian axes), we write:

$$
\vec{F} = F_x\hat{i} + F_y\hat{j}.
$$

### Combining forces (vector addition)

If several forces act on the same particle, the combined effect is represented by vector addition:

$$
\vec{F}_{\text{net}} = \vec{F}_1 + \vec{F}_2 + \cdots
$$

Component-wise, this means:

$$
F_{\text{net},x} = F_{1x} + F_{2x} + \cdots, \qquad F_{\text{net},y} = F_{1y} + F_{2y} + \cdots
$$

This is not yet Newton’s second law; it is how we represent multiple interactions as one net interaction vector.

### Units: newton

The SI unit of force is the newton (N). In Newtonian mechanics it is convenient to remember the dimensional meaning:

$$
1\,\text{N} = 1\,\text{kg}\cdot\text{m/s}^2.
$$

Later, when we connect force to acceleration, this unit relationship becomes natural rather than a definition to memorize.

## Interpretation

### Operational meaning (what “measuring a force” means)

A spring scale does not “detect a force in space.” It measures an interaction: the tension in the spring required to maintain a certain extension. The reading depends on the situation, including whether the object is accelerating.

So force is not a property that an isolated object “has.” Force arises from interactions.

### Force is not velocity

Velocity describes how position changes. Force models interaction; it will be connected to acceleration later.

You can have:

- nonzero velocity with zero net force (constant-velocity motion in an inertial frame),
- zero velocity with nonzero net force (an instant at a turning point),
- nonzero net force with changing direction only (uniform circular motion: speed constant but direction changes).

These examples show why “force = motion” is not a correct mental model.

## Typical examples

1) Contact push/pull: a person pushes a box. The direction is the push direction; the magnitude depends on how hard they push and the interaction details.

2) Gravity: a ball near Earth experiences a downward gravitational force. (The detailed model is handled later in the “weight” section.)

3) Spring: a stretched spring pulls back toward its equilibrium length.

4) Rope tension: an ideal rope pulls along its length, not sideways.

## Common mistakes

- Thinking that “motion requires force” (a misconception corrected formally with Newton’s first law later).
- Treating force as a scalar and adding magnitudes without direction.
- Thinking that the force on an object is always in the direction the object is moving.
- Confusing the name of a force with a formula (for example, thinking “friction is always mu N” even when static friction can be smaller).
- Forgetting to specify which object the force is acting on. A force is always “force on this body due to that interaction.”

## Worked example

Two horizontal forces act on a puck on a frictionless table. Choose x to the east and y to the north.

- Force 1 is 6 N east.
- Force 2 is 8 N north.

Find the net force vector, its magnitude, and its direction.

### Step 1: Write forces as vectors in components

$$
\vec{F}_1 = 6\,\hat{i}, \qquad \vec{F}_2 = 8\,\hat{j}.
$$

### Step 2: Add to get the net force

$$
\vec{F}_{\text{net}} = \vec{F}_1 + \vec{F}_2 = 6\,\hat{i} + 8\,\hat{j}.
$$

So the components are:

$$
F_{\text{net},x}=6\,\text{N}, \qquad F_{\text{net},y}=8\,\text{N}.
$$

### Step 3: Magnitude

$$
|\vec{F}_{\text{net}}| = \sqrt{6^2 + 8^2}\,\text{N} = \sqrt{100}\,\text{N} = 10\,\text{N}.
$$

### Step 4: Direction

Let theta be the angle measured from +x toward +y. Then:

$$
\tan\theta = \frac{8}{6} = \frac{4}{3}.
$$

So:

$$
\theta = \arctan\left(\frac{4}{3}\right) \approx 53.1^\circ.
$$

Interpretation: the net interaction points northeast, 53.1 degrees above the +x axis.

## Mini recap

- Force is a vector model of interaction:

$$
\vec{F}.
$$

- Multiple forces combine by vector addition:

$$
\vec{F}_{\text{net}} = \sum \vec{F}.
$$

- Units:

$$
1\,\text{N} = 1\,\text{kg}\cdot\text{m/s}^2.
$$

- Keep track of direction, components, and “force on which object due to what.”
