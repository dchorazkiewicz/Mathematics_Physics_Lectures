# Particle on an inclined plane

## Learning goals

- Set up correct free-body diagrams for a block on an incline.
- Choose axes parallel and perpendicular to the plane and decompose weight correctly.
- Solve both no-friction and friction cases with consistent sign conventions.
- Decide whether the block slips or stays at rest by checking the static friction condition.

## Why this matters

Incline problems are the first place where strategic axis choice becomes essential. They also combine several core force ideas:

- weight and its components,
- normal force as a constraint response,
- friction direction reasoning,
- Newton’s second law in components.

Once you can solve incline problems reliably, connected-body and circular motion dynamics becomes much easier.

## Core idea

The incline imposes a geometric constraint: the block cannot accelerate into or away from the surface as long as contact is maintained.

So:

- the perpendicular acceleration is usually zero (a_perp = 0),
- which lets you solve for N,
- then friction (if present) depends on N,
- and the parallel equation gives the acceleration along the plane.

The direction of friction depends on the tendency to slip:

- if the block tends to slide down, friction points up the plane,
- if it tends to slide up, friction points down the plane.

## Mathematical formulation

Choose axes:

- x parallel to the plane,
- y perpendicular to the plane.

Let theta be the incline angle above horizontal. Decompose weight:

parallel component magnitude:

$mg\sin\theta,$

perpendicular component magnitude:

$mg\cos\theta.$

If the block stays in contact with the plane:

$a_y = 0.$

So the perpendicular equation gives:

$$
N - mg\cos\theta = 0 \Rightarrow N = mg\cos\theta
$$

(assuming no other forces with perpendicular components).

Friction:

- kinetic: f_k = mu_k N, direction opposite sliding,
- static: 0 <= f_s <= mu_s N, direction opposite tendency to slip.

Parallel equation (sign depends on axis choice):

$$
\sum F_x = ma_x.
$$

## Interpretation

- The incline turns a vertical gravitational force into a component along the motion direction.
- N is smaller than mg on an incline: N = mg cos theta (in the simple case).
- Friction is not “always mu N.” Static friction adjusts; kinetic friction uses f_k = mu_k N in the simplest model.

## Typical examples

1) Block slides down a frictionless incline: acceleration is g sin theta down the plane.

2) Block rests on an incline: static friction may hold it; check f_s <= mu_s N.

3) Block pulled up an incline by a rope: friction direction depends on whether the block is moving up or down (or about to).

## Common mistakes

- Swapping sin and cos in the weight decomposition.
- Forgetting that friction direction depends on the tendency to slip, not on the sign of the applied force alone.
- Using N = mg instead of N = mg cos theta (in the simple incline case).
- Solving for static friction as f_s = mu_s N without checking whether the required friction is smaller.
- Ignoring the possibility of no motion (static equilibrium) when static friction is strong enough.

## Worked example

A block of mass m = 5.0 kg is on a 30-degree incline.

Case A: frictionless surface.  
Case B: coefficient of kinetic friction mu_k = 0.20 (and the block is sliding down).

Take g = 9.8 m/s^2. Find the acceleration magnitude down the plane in each case.

Choose x down the plane (positive), y perpendicular outward.

### Case A: no friction

Perpendicular:

$N = mg\cos\theta.$

Parallel forces: only the downslope component of weight:

$$
\sum F_x = mg\sin\theta = ma.
$$

So:

$a = g\sin\theta = 9.8\sin 30^\circ = 9.8(0.5) = 4.9\,\text{m/s}^2.$

### Case B: kinetic friction

Perpendicular gives the same N:

$N = mg\cos\theta.$

Kinetic friction magnitude:

$f_k = \mu_k N = \mu_k mg\cos\theta.$

Friction points up the plane (negative x) because motion is down the plane.

Parallel equation:

$mg\sin\theta - f_k = ma.$

Substitute:

$mg\sin\theta - \mu_k mg\cos\theta = ma.$

Cancel m:

$a = g(\sin\theta - \mu_k\cos\theta).$

Plug in numbers: sin 30 degrees = 0.5, cos 30 degrees ≈ 0.866:

$$
a = 9.8(0.5 - 0.20\cdot 0.866) = 9.8(0.3268) \approx 3.20\,\text{m/s}^2.
$$

Interpretation: friction reduces the acceleration compared to the frictionless value.

## Mini recap

- Choose axes along/perpendicular to the plane.
- Decompose weight:

$$
mg\sin\theta \text{ (parallel)}, \qquad mg\cos\theta \text{ (perpendicular)}.
$$

- If contact is maintained and no other perpendicular forces:

$N = mg\cos\theta.$

- Along the plane:
  - frictionless: a = g sin theta,
  - with kinetic friction down the plane:

$a = g(\sin\theta - \mu_k\cos\theta).$
