# Newton’s third law

## Learning goals

- State Newton’s third law and identify action–reaction force pairs correctly.
- Distinguish third-law pairs from “forces that balance” on a single object.
- Apply the third law to contact forces (normal, friction, tension) and to gravity.
- Avoid common misconceptions in multi-body problems.

## Why this matters

Newton’s third law is one of the most frequently misunderstood ideas in mechanics. Students often use it to “cancel” forces on a single object, which is almost always wrong.

The third law is not a rule about equilibrium. It is a rule about interactions between two bodies: forces come in mutual pairs, equal in magnitude and opposite in direction, acting on different objects.

Correct third-law thinking is essential for:

- building correct free-body diagrams,
- understanding tension and contact forces,
- solving connected-body and interaction problems.

## Core idea

Every interaction involves two bodies. If body A exerts a force on body B, then body B exerts a force on body A.

These two forces:

- have the same magnitude,
- have opposite directions,
- act on different bodies,
- occur at the same time.

## Mathematical formulation

Let \vec{F}_{A\to B} denote “force on B due to A.” Newton’s third law states:

$$
\vec{F}_{A\to B} = -\vec{F}_{B\to A}.
$$

Important: the two forces in the equation act on different objects (B and A respectively). That is why they do not cancel in a free-body diagram of a single object.

## Interpretation

### Third-law pairs vs balanced forces

- Third-law pair: forces between two bodies (A on B, B on A).
- Balanced forces: forces on the same body whose vector sum is zero.

Balanced forces are a condition for zero acceleration (Newton’s first/second law), not a direct consequence of the third law.

### Examples of third-law pairs (by interaction type)

Contact normal interaction:

- floor on box (upward normal on box),
- box on floor (downward normal on floor).

Friction interaction:

- floor on box (friction on box),
- box on floor (opposite friction on floor).

Gravity interaction:

- Earth on ball (gravitational force on ball),
- ball on Earth (equal and opposite gravitational force on Earth).

In many problems Earth’s acceleration is negligible because its mass is enormous, not because the third-law force “does not exist.”

## Typical examples

1) Person pushing a wall: the wall pushes back on the person with equal magnitude opposite direction. This is why the person feels the contact force.

2) Two blocks in contact: each block exerts a normal force on the other; those two forces are a third-law pair.

3) Rope tension: rope pulls on the block; the block pulls on the rope. Those are a third-law pair. (In an ideal rope, tensions at different points can be equal, but that is a separate modeling assumption.)

## Common mistakes

- Saying “action and reaction cancel, so there is no motion.” They act on different bodies, so they do not cancel in one object’s equation of motion.
- Pairing forces that act on the same body as a third-law pair (e.g., weight and normal on a block are not a third-law pair).
- Thinking the “bigger object exerts a bigger force.” The third law says the forces are equal in magnitude; differences in acceleration come from different masses and different net forces.
- Confusing “equal and opposite” with “balanced.” Equal and opposite can be balanced only if they act on the same object.

## Worked example

Two blocks A and B are in contact on a frictionless horizontal surface. A horizontal push is applied to block A, causing both blocks to accelerate to the right.

1) Identify the third-law pair associated with the contact between A and B.  
2) Explain why the contact forces do not cancel in the equation of motion for block B.

### Step 1: Identify the interaction forces

At the contact interface:

- block A pushes on block B (force on B due to A),
- block B pushes on block A (force on A due to B).

Call the force on B due to A:

$$
\vec{F}_{A\to B}.
$$

Then by Newton’s third law:

$$
\vec{F}_{B\to A} = -\vec{F}_{A\to B}.
$$

These two forces are a third-law pair.

### Step 2: Why there is no cancellation on block B

If you draw a free-body diagram for block B alone, you include forces acting on B. The contact force from A is one of them:

$$
\vec{F}_{A\to B}.
$$

But the reaction force \vec{F}_{B\to A} acts on A, not on B. Therefore it does not appear in B’s free-body diagram and cannot cancel \vec{F}_{A\to B} there.

So block B can accelerate because it experiences a net force to the right (provided by the contact with A).

## Mini recap

- Newton’s third law:

$$
\vec{F}_{A\to B} = -\vec{F}_{B\to A}.
$$

- Third-law forces act on different objects, so they do not cancel within a single free-body diagram.
- Do not confuse third-law pairs with balanced forces (net force zero on one body).
- Apply the rule to contact, friction, tension, and gravity interactions consistently.
