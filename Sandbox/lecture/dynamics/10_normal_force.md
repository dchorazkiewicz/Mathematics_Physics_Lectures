# Normal force

## Learning goals

- Interpret the normal force as a contact constraint force (surface response), not a fixed formula.
- Explain when N equals mg and when it does not.
- Set up Newton’s second law in the direction perpendicular to a surface to solve for N.
- Avoid common mistakes like assuming N = mg in all situations.

## Why this matters

The normal force appears in almost every contact problem: blocks on floors, inclines, elevators, and circular tracks.

Students often memorize “N = mg,” which is only true in special cases. In general, N is determined by the constraint “the object does not pass through the surface” and by the object’s acceleration relative to that surface.

If you get N wrong, you get friction wrong too, because many friction models use N.

## Core idea

The normal force is the force exerted by a surface on an object, perpendicular to the surface, preventing interpenetration.

Key points:

- N adjusts to whatever value is needed to satisfy the contact constraint.
- N can be larger than mg, smaller than mg, or even zero (loss of contact).
- N is not a third-law pair with weight; the third-law pair of N is the force the object exerts on the surface.

## Mathematical formulation

### Flat surface, vertical axis

Consider a block on a horizontal surface. Take y upward. Vertical forces are:

- N upward,
- weight mg downward.

Newton’s second law in y is:

$N - mg = ma_y.$

If the block has no vertical acceleration (a_y = 0), then:

$N = mg.$

This is the special case many students memorize, but it depends on the condition a_y = 0.

### Inclined surface (perpendicular direction)

For a block on an incline, the easiest method is to choose axes:

- one axis perpendicular to the plane,
- one axis parallel to the plane.

If the block stays in contact with the plane, its acceleration perpendicular to the plane is zero:

$a_\perp = 0.$

Then Newton’s second law perpendicular to the plane determines N. For example, if the only forces with perpendicular components are N and weight, you get:

$$
N - mg\cos\theta = 0 \Rightarrow N = mg\cos\theta.
$$

This is already different from mg.

### Loss of contact condition

If the solution gives N <= 0, that indicates the surface cannot “pull” on the object in the normal direction. The correct physical interpretation is usually:

- contact is lost,
- then N becomes 0 and the motion model changes.

## Interpretation

- N is a constraint force: it exists because the surface enforces a geometric constraint.
- You do not guess N. You solve for it using the perpendicular equation of motion and the contact constraint.
- Saying “N equals mg” is only correct when:
  - the surface is horizontal, and
  - there is no vertical acceleration, and
  - there are no other vertical forces (like a rope pulling up).

## Typical examples

1) Elevator floor: N differs from mg when the elevator accelerates.

2) Block pulled upward at an angle: N is reduced because the rope has an upward component.

3) Block on an incline: N = mg cos(theta) (if no other perpendicular forces).

4) Roller coaster crest: N can drop to zero at a high speed, leading to weightlessness.

## Common mistakes

- Assuming N = mg automatically.
- Forgetting to choose a perpendicular axis and accidentally using the parallel equation to solve for N.
- Confusing the third-law pair of N (object on surface) with mg (Earth on object).
- Allowing N to be negative without interpreting it as loss of contact.

## Worked example

A person of mass:

$m = 70\,\text{kg}$

stands on a bathroom scale in an elevator. The elevator accelerates downward with magnitude 2.0 m/s^2. Take y upward and g = 9.8 m/s^2.

Find the scale reading (the normal force N).

### Step 1: Write Newton’s second law in y

For the person, vertical forces are:

- N upward,
- mg downward.

So:

$N - mg = ma_y.$

The elevator accelerates downward, so a_y is negative:

$a_y = -2.0\,\text{m/s}^2.$

### Step 2: Solve for N

$N = m(g + a_y) = 70(9.8 - 2.0).$

Compute:

$N = 70(7.8) = 546\,\text{N}.$

### Step 3: Interpret

At rest, the scale would read mg = 686 N. Here it reads 546 N, smaller, because the net force must be downward to produce downward acceleration. This is a normal-force example of “apparent weight changes with acceleration.”

## Mini recap

- Normal force is a surface response force perpendicular to the surface.
- It is determined by Newton’s second law plus the contact constraint.
- Flat surface:

$N - mg = ma_y.$

- Incline (no perpendicular acceleration):

$$
N = mg\cos\theta \quad \text{(if only gravity contributes perpendicularly)}.
$$

- If a computed N <= 0, contact is lost and N becomes 0 with a new motion model.
