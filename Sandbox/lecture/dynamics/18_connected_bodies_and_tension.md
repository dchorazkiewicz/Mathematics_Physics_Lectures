# Connected bodies and tension

## Learning goals

- Apply Newton’s second law to multi-body systems with ropes/pulleys.
- Use the rope constraint to relate accelerations (shared magnitude in common setups).
- Draw separate free-body diagrams and write separate equations for each body.
- Solve coupled equations for acceleration and tension, and interpret the result.

## Why this matters

Many realistic systems involve connected bodies: elevators with counterweights, blocks connected by ropes, pulleys, and towing.

The new difficulty is not a new law; it is bookkeeping:

- each body has its own forces and its own equation,
- the rope constraint connects their accelerations,
- tension is an internal interaction in the combined system, but an external force on each individual body.

## Core idea

In an ideal rope over an ideal pulley, the rope length is constant. That constraint typically implies:

- the connected bodies have accelerations of equal magnitude,
- the directions are opposite along the rope.

The correct workflow:

1) Draw an FBD for each body separately.  
2) Choose axes consistent with each body’s motion.  
3) Write Newton’s second law for each body.  
4) Use the rope constraint to connect accelerations.  
5) Solve the coupled system for the unknowns (a, T, etc.).

## Mathematical formulation

### Rope constraint (typical single-pulley systems)

If the rope is massless and inextensible and does not slip on the pulley, then the rope length is constant.

In many standard setups this gives:

$a_1 = a_2$

for acceleration magnitudes, with opposite directions depending on axis choices.

### Separate Newton equations

For each body i:

$$
\sum \vec{F}_i = m_i\vec{a}_i.
$$

You generally write scalar component equations along the direction of motion for each body.

### System approach (optional idea)

Sometimes it is useful to consider the two bodies together as one system to eliminate internal forces like tension. In that combined-system view, tension is internal and cancels in the net external force sum.

However, to find the tension itself you still need individual-body equations.

## Interpretation

- Tension is not “the same as weight.” It is determined by the coupled motion.
- The heavier side does not “pull with a bigger tension.” Tension is an internal interaction constrained by the rope model and the dynamics of both masses.
- Internal forces can cancel when you write a combined equation for the whole system, but they do not disappear from individual free-body diagrams.

## Typical examples

1) Block on a table connected to a hanging mass (with or without friction).

2) Two blocks connected on a horizontal surface.

3) Atwood machine (two hanging masses; already solved in the tension section, now as a template for solving).

## Common mistakes

- Writing one equation for the whole system and then trying to solve for tension without an individual-body equation.
- Using different acceleration magnitudes for connected bodies in a single-rope system.
- Mixing sign conventions: choosing axes inconsistently so that the rope constraint is written incorrectly.
- Treating tension as known (like T = mg) instead of as an unknown to solve for.
- Forgetting friction on the block on the table when it is stated to be present.

## Worked example

A block m_1 = 3.0 kg rests on a horizontal table. It is connected by a light rope over a frictionless pulley to a hanging mass m_2 = 2.0 kg.

The coefficient of kinetic friction between m_1 and the table is mu_k = 0.20. Take g = 9.8 m/s^2.

Assume the system moves with m_2 downward (so m_1 moves to the right).

Find:

1) the acceleration magnitude a,  
2) the rope tension T.

### Step 1: Free-body diagram equations

For m_1 (on table, x to the right):

Horizontal forces:

- tension T to the right,
- kinetic friction f_k to the left.

So:

$T - f_k = m_1 a.$

Vertical forces on m_1 balance (a_y = 0), so:

$N = m_1 g.$

Thus:

$f_k = \mu_k N = \mu_k m_1 g.$

For m_2 (hanging, choose positive downward to match assumed motion):

Forces:

- weight m_2 g downward (positive),
- tension T upward (negative).

So:

$m_2 g - T = m_2 a.$

### Step 2: Compute friction and solve the coupled system

Compute friction:

$f_k = \mu_k m_1 g = (0.20)(3.0)(9.8) = 5.88\,\text{N}.$

Now solve for a and T. From the m_1 equation:

$T = m_1 a + f_k.$

Substitute into the m_2 equation:

$m_2 g - (m_1 a + f_k) = m_2 a.$

Solve for a:

$m_2 g - f_k = (m_1 + m_2)a.$

So:

$$
a = \frac{m_2 g - f_k}{m_1 + m_2}.
$$

Plug in numbers:

$$
a = \frac{(2.0)(9.8) - 5.88}{3.0 + 2.0} = \frac{19.6 - 5.88}{5.0} = \frac{13.72}{5.0} = 2.74\,\text{m/s}^2.
$$

### Step 3: Solve for tension

Use:

$T = m_1 a + f_k = (3.0)(2.74) + 5.88 = 8.22 + 5.88 = 14.10\,\text{N}.$

### Step 4: Quick checks

- If friction were zero, acceleration would be m_2 g / (m_1 + m_2) = 19.6/5 = 3.92 m/s^2, larger than 2.74. Friction reduces acceleration, as expected.
- T is between m_2 g = 19.6 N and 0, reasonable.

## Mini recap

- Draw separate FBDs for each body.
- Write separate Newton equations and connect accelerations with the rope constraint.
- Tension is generally unknown and must be solved for.
- For a two-body table + hanging system, a common structure is:

$T - f_k = m_1 a, \qquad m_2 g - T = m_2 a,$

with:

$f_k = \mu_k m_1 g$

if the table block slides.
