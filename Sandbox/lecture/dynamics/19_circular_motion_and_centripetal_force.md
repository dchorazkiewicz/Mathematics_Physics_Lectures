# Circular motion and centripetal force (role)

## Learning goals

- Connect circular motion kinematics (inward acceleration) to dynamics (required inward net force).
- Write the radial (inward) component equation with correct sign conventions.
- Understand that “centripetal force” is not a new force type; it is the name for the net inward force required for circular motion.
- Solve basic circular dynamics problems: mass on a string, car turning, and simple vertical circle conditions.

## Why this matters

Circular motion is where many students invent a “centrifugal force” as a real force in inertial frames. The correct dynamic idea is:

- circular motion requires inward acceleration,
- Newton’s second law then requires an inward net force.

Once you can write the radial force balance correctly, many circular-motion problems become straightforward.

## Core idea

Kinematics tells you that to move in a circle of radius R with speed v, the acceleration must point inward with magnitude:

$$
a_r = \frac{v^2}{R}.
$$

Dynamics says:

$$
\sum \vec{F} = m\vec{a}.
$$

So in the radial direction, the net force component must point inward with magnitude:

$$
F_{\text{net,inward}} = m\frac{v^2}{R}.
$$

This inward net force is what people call the centripetal force. It is not an extra force; it is the net of whatever real forces happen to have inward components.

## Mathematical formulation

### Radial axis and sign convention

Choose a radial axis pointing inward toward the center (this is often the cleanest choice). Then:

$$
a_r = \frac{v^2}{R}
$$

is positive (inward).

Newton’s second law in the radial direction becomes:

$$
\sum F_r = m\frac{v^2}{R}.
$$

Here the symbol \sum F_r means “sum of the inward components of all forces.”

### Common force contributors to radial direction

Depending on the situation, inward components can come from:

- tension in a string,
- normal force from a track,
- gravity components (in vertical circles),
- friction (for a car turning on a flat road, friction provides the inward force).

You project each real force onto the radial direction and sum.

## Interpretation

- Saying “centripetal force” answers the question “what is the net inward force?” not “which force is present?”
- If you draw an FBD and then add a new arrow labeled “centripetal force” in addition to tension/normal/gravity, you will double-count.
- If you describe motion from a rotating frame, you may introduce inertial forces (like centrifugal) as a bookkeeping device. In an inertial frame, you do not need them.

## Typical examples

1) Mass on a horizontal circle on a string: tension provides the inward force.

2) Car turning on a flat road: static friction provides the inward force (up to a limit), which sets a maximum safe speed for a given turn radius.

3) Vertical circle/loop: tension/normal and weight both contribute to radial force, and contact can be lost when normal force becomes zero.

## Common mistakes

- Treating “centripetal force” as a separate force in the free-body diagram.
- Writing m v^2/R and labeling it as a force without specifying which real forces sum to it.
- Choosing outward as positive and then forgetting the sign of a_r (sign conventions must be consistent).
- Using v^2/R with v not being the instantaneous speed (it must be the speed at that point).
- Confusing friction direction in turning problems (friction points toward the center for a car turning without slipping).

## Worked example

A 0.50 kg mass moves in a horizontal circle of radius R = 0.80 m at constant speed v = 4.0 m/s, attached to a string.

Neglect air resistance. Find the tension in the string.

### Step 1: Identify radial acceleration

$$
a_r = \frac{v^2}{R} = \frac{(4.0)^2}{0.80} = \frac{16}{0.80} = 20\,\text{m/s}^2.
$$

### Step 2: Radial force balance

In a horizontal circle, weight and normal (if any) are vertical and do not contribute to the radial (horizontal inward) direction. The only radial force is tension T.

So:

$$
T = m a_r = m\frac{v^2}{R}.
$$

Compute:

$T = (0.50)(20) = 10\,\text{N}.$

Interpretation: tension provides exactly the inward net force needed to continuously change the velocity direction.

## Mini recap

- Circular motion requires inward acceleration:

$$
a_r = \frac{v^2}{R}.
$$

- Dynamics in the radial direction (inward positive):

$$
\sum F_r = m\frac{v^2}{R}.
$$

- “Centripetal force” means the net inward force role; it is not an additional force you add to the FBD.
