# Tension force

## Learning goals

- Model tension as the pulling force transmitted by an ideal rope/string.
- Draw the correct direction of tension forces on each connected object.
- State standard pulley/rope assumptions and know what they imply about tension magnitude.
- Solve basic connected-body problems using separate free-body diagrams and Newton’s second law.

## Why this matters

Tension appears in many multi-body problems: hanging masses, pulleys, elevators, and towing. The most common errors are not algebraic; they are modeling errors:

- putting tension in the wrong direction,
- assuming tension equals weight,
- mixing up which body a given tension force acts on.

This section establishes a consistent tension model that you can reuse across many dynamics problems.

## Core idea

An ideal rope/string transmits a pulling interaction along its length. It can pull but cannot push.

Therefore:

- tension acts along the rope direction,
- tension on a body points away from the body along the rope (the rope pulls on the body),
- different bodies feel different tension forces, but they are connected through the rope model.

## Mathematical formulation

### Ideal rope assumptions (common in intro problems)

When a problem says “light rope” or “massless rope,” and a “frictionless pulley,” the usual idealization is:

- the rope has negligible mass,
- the rope does not stretch (inextensible),
- the pulley is frictionless and massless (in many problems).

Under these assumptions:

- the tension magnitude is the same everywhere along one continuous rope segment,
- the rope length constraint ties the accelerations of connected bodies.

If the pulley has significant mass or friction, tension can differ on the two sides. That is beyond the simplest model, and the problem statement will typically mention it explicitly.

### Direction rule (force on the body)

If a rope segment attached to a body points along some direction, the tension force exerted by the rope on the body points along that segment away from the body.

In diagrams, you label that force as T. You do not decide its magnitude by guessing; it is determined by the equations of motion plus constraints.

## Interpretation

- Tension is not a “new kind of physics.” It is a convenient name for the force a rope exerts.
- In many problems, T is the same on both sides of an ideal pulley, but that is a modeling assumption, not a universal law.
- A tension force is always part of an interaction pair: rope on mass and mass on rope (Newton’s third law). In a free-body diagram for the mass, you include only rope on mass.

## Typical examples

1) Hanging mass at rest: tension equals weight only if acceleration is zero and the only vertical forces are T and mg.

2) Atwood machine (two hanging masses): tension is generally not equal to either weight; it is determined by the coupled motion.

3) Block on a table connected to a hanging mass: horizontal tension pulls the block; vertical tension pulls the hanging mass.

## Common mistakes

- Drawing tension pointing toward the body instead of away along the rope.
- Assuming T = mg automatically for any hanging mass (only true in certain equilibrium/constant-speed cases).
- Using one equation for “the whole system” without separate free-body diagrams when different forces act on different bodies.
- Forgetting the constraint that the rope enforces equal-magnitude accelerations in many simple setups.
- Confusing the third-law pair of tension (mass on rope) with another force on the same mass.

## Worked example

Atwood machine (ideal). Two masses m_1 and m_2 hang from a light rope over a frictionless, massless pulley. Let:

$m_2 > m_1.$

Assume the rope does not stretch. Find:

1) the acceleration magnitude a,  
2) the tension T in the rope.

Take y upward for m_1 and y downward for m_2 (so both accelerations have the same sign a in their chosen positive directions).

### Step 1: Free-body diagram equations

For m_1 (moving up):

- tension T upward,
- weight m_1 g downward.

Newton’s second law:

$T - m_1 g = m_1 a.$

For m_2 (moving down; we chose downward as positive for this mass):

- weight m_2 g downward (positive),
- tension T upward (negative).

Newton’s second law:

$m_2 g - T = m_2 a.$

### Step 2: Solve the coupled equations

Add the equations:

$(T - m_1 g) + (m_2 g - T) = m_1 a + m_2 a.$

Simplify:

$(m_2 - m_1)g = (m_1 + m_2)a.$

So:

$$
a = \frac{(m_2 - m_1)g}{m_1 + m_2}.
$$

### Step 3: Solve for tension

Use the m_1 equation:

$T = m_1 g + m_1 a = m_1(g + a).$

Substitute a:

$$
T = m_1\left(g + \frac{(m_2 - m_1)g}{m_1 + m_2}\right)
= m_1 g\left( \frac{(m_1+m_2) + (m_2-m_1)}{m_1+m_2} \right)
= m_1 g\left(\frac{2m_2}{m_1+m_2}\right).
$$

So:

$$
T = \frac{2m_1 m_2}{m_1+m_2}g.
$$

### Step 4: Sanity checks

- If m_1 = m_2, then a = 0 and T = m_1 g, as expected.
- If m_2 >> m_1, then a approaches g and T approaches 2m_1 g (the light mass is pulled up strongly).

## Mini recap

- Tension is the pulling force a rope exerts along its length.
- In ideal rope + frictionless massless pulley problems, tension magnitude is the same along one rope segment.
- Always draw separate free-body diagrams and use the rope constraint for accelerations.
- Do not assume T = mg unless acceleration is known to be zero and the force list supports it.
