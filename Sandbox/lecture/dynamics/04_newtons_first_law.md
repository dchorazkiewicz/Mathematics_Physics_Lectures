# Newton’s first law

## Learning goals

- State Newton’s first law in words and interpret it as a statement about inertial motion.
- Understand inertia: why “no net force” corresponds to constant velocity, not necessarily rest.
- Use the net force concept correctly (distinguish individual forces from their sum).
- Recognize and correct the misconception “motion requires force.”

## Why this matters

Newton’s first law is the conceptual foundation of dynamics. It tells you what “no interaction effect” means:

- not “no motion,” but “no change in velocity.”

Without this idea, you will consistently invent extra forces (“force of motion,” “force in the direction of travel”) to match intuition, and your later free-body diagrams will be wrong.

## Core idea

There are two different questions:

1) What is the velocity right now?  
2) Is the velocity changing?

Newton’s first law is about the second question. It introduces the idea of a special kind of reference frame (inertial) in which the natural state of motion is constant velocity.

Inertia is the tendency of a body to maintain its current velocity unless interactions produce a net effect.

## Mathematical formulation

Newton’s first law (in an inertial frame) can be stated as:

If the net external force on a body is zero, then the body’s velocity is constant.

In symbols:

$$
\sum \vec{F} = \vec{0} \Rightarrow \vec{v} = \text{constant}.
$$

Equivalently, constant velocity implies zero acceleration:

$$
\vec{v} = \text{constant} \Rightarrow \vec{a} = \vec{0}.
$$

In a Newtonian framework, “zero net force” and “zero acceleration” go together. The second law will later make the quantitative connection.

## Interpretation

### Rest and constant-velocity motion are the same dynamic state

Rest is just the special case of constant velocity with:

$\vec{v}=\vec{0}.$

From the viewpoint of dynamics, “at rest” and “moving at constant velocity” are equivalent in the sense that neither requires a net force.

That is why a puck on a nearly frictionless table continues moving without needing a continuous push once it is already moving.

### Net force, not individual forces

Newton’s first law is about the sum of forces. You can have multiple nonzero forces and still have zero net force if they balance.

Example (conceptual):

- gravity pulls downward,
- the table pushes upward with a normal force,
- if these two balance, vertical net force is zero.

The object can still move horizontally at constant velocity while these vertical forces exist.

### What the law does not say

- It does not say that a body with zero net force must be at rest.
- It does not say that if the body is moving, there must be a force in the direction of motion.
- It does not say that “forces always come in pairs on the same body.” (That is a separate idea: Newton’s third law.)

## Typical examples

1) Puck on ice: once sliding, it continues approximately at constant velocity because friction is small.

2) Elevator at constant speed: forces are not zero, but net force is zero (tension balances weight), so acceleration is zero.

3) Car cruising at constant speed on level road: engine thrust and drag/friction forces can balance so net force is zero.

## Common mistakes

- Thinking “if it’s moving, a force must point in the direction of motion.”
- Confusing “no force” with “no net force.”
- Treating friction as always present and always the same size, then claiming first-law motion is impossible. In reality, the first law describes an ideal limit and is approximately true when resistive forces are small or balanced by other forces.
- Drawing a free-body diagram that includes a “force of motion” to explain constant velocity.

## Worked example

A crate is pulled across a floor at constant velocity. The rope pulls horizontally with tension magnitude:

$T = 50\,\text{N}.$

The crate’s motion is constant velocity (so acceleration is zero). Assume the only horizontal forces are tension (forward) and kinetic friction (backward).

1) What is the magnitude of the kinetic friction force?  
2) What is the net horizontal force?

### Step 1: Use constant velocity to infer zero acceleration

Constant velocity implies:

$a_x = 0.$

Newton’s first law (or the “no change in velocity means no net force” idea) tells you:

$F_{\text{net},x} = 0.$

### Step 2: Write the force balance in x

Let friction magnitude be f_k, acting opposite the motion. Then:

$T - f_k = 0.$

So:

$f_k = T = 50\,\text{N}.$

### Step 3: Net force

$F_{\text{net},x} = T - f_k = 0.$

Interpretation: the crate can move at constant speed even though forces act, as long as they balance.

## Mini recap

- In an inertial frame:

$$
\sum \vec{F} = \vec{0} \Rightarrow \vec{v}=\text{constant}.
$$

- Rest is a special case of constant velocity.
- The first law is about net force, not the absence of forces.
- If velocity is constant, you do not add a “force of motion” to explain it; you look for balanced forces.
