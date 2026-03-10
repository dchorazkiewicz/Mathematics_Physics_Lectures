# Resolving forces into components

## Learning goals

- Choose axes strategically to simplify Newton’s second law equations.
- Resolve forces into components using projections and basic trigonometry.
- Use incline-aligned coordinates correctly (parallel/perpendicular to the plane).
- Avoid common trig/sign mistakes when decomposing forces.

## Why this matters

Newton’s second law is a vector equation, but almost all calculations are done component-wise.

Choosing bad axes can turn a simple problem into messy algebra. Choosing good axes can make the equations almost write themselves (especially on inclines and in tension problems).

This section is about technique: how to go from a geometric force diagram to clean scalar equations.

## Core idea

Any force vector can be decomposed into components along chosen perpendicular axes.

Two key ideas:

1) Components depend on the axes you choose, but the physical vector does not.  
2) Pick axes aligned with constraints and known directions (like “along the surface” and “perpendicular to the surface”).

## Mathematical formulation

### Component form of Newton’s second law (2D)

If you choose x and y axes, then:

$$
\sum F_x = ma_x, \qquad \sum F_y = ma_y.
$$

### Resolving a force at an angle

If a force of magnitude F makes angle theta with the +x axis, then its components are:

$F_x = F\cos\theta, \qquad F_y = F\sin\theta.$

You must decide what theta is measured from and keep that consistent.

### Incline-aligned axes

For a block on an incline of angle theta above horizontal, a convenient choice is:

- x axis parallel to the plane (positive up the plane),
- y axis perpendicular to the plane (positive away from the plane).

Then the weight mg decomposes into:

parallel component:

$(mg)_\parallel = mg\sin\theta,$

perpendicular component:

$(mg)_\perp = mg\cos\theta.$

Directions:

- (mg)_parallel points down the plane,
- (mg)_perp points into the plane.

This decomposition is used constantly in incline problems.

## Interpretation

- The goal of components is not to “make numbers.” It is to write correct scalar equations that capture the correct directions.
- You can always check your decomposition in limiting cases:
  - theta = 0: incline is flat, so (mg)_parallel should be 0 and (mg)_perp should be mg.
  - theta = 90 degrees: incline is vertical, so (mg)_parallel should be mg and (mg)_perp should be 0.

These checks catch many trig mix-ups.

## Typical examples

1) Pulling a block with a rope at an angle: resolve tension into horizontal and vertical components to find N and friction.

2) Incline with friction: resolve weight into parallel and perpendicular components; solve for N first, then friction.

3) Two-body tension problems: choose axes aligned with motion of each mass to keep equations simple.

## Common mistakes

- Swapping sine and cosine in incline decompositions (mixing which angle is used).
- Using degrees vs radians inconsistently in calculators (for numeric work, be explicit).
- Forgetting to assign a sign to a component (components are signed quantities).
- Decomposing forces but then writing equations in a different axis system.
- Solving for N using the parallel equation instead of the perpendicular one.

## Worked example

A block of mass m = 6.0 kg rests on an incline of angle theta = 30 degrees. The coefficient of kinetic friction is mu_k = 0.20 and the block slides down the incline.

Find the acceleration magnitude down the plane. Take g = 9.8 m/s^2.

### Step 1: Choose axes and list forces

Choose:

- x parallel to the plane, positive down the plane (since motion is down),
- y perpendicular to the plane, positive away from the plane.

Forces:

- weight mg downward,
- normal force N perpendicular outward,
- kinetic friction f_k up the plane (opposes sliding).

### Step 2: Resolve weight into components

Parallel component magnitude:

$(mg)_x = mg\sin\theta.$

Perpendicular component magnitude:

$(mg)_y = mg\cos\theta.$

### Step 3: Perpendicular equation to find N

No acceleration perpendicular to the plane, so a_y = 0:

$$
\sum F_y = 0 \Rightarrow N - mg\cos\theta = 0.
$$

So:

$N = mg\cos\theta.$

### Step 4: Friction magnitude

$f_k = \mu_k N = \mu_k mg\cos\theta.$

### Step 5: Parallel equation to find acceleration

Along the plane (positive down the plane):

$$
\sum F_x = ma_x \Rightarrow mg\sin\theta - f_k = ma.
$$

Substitute f_k:

$mg\sin\theta - \mu_k mg\cos\theta = ma.$

Cancel m:

$g(\sin\theta - \mu_k\cos\theta) = a.$

Now plug in numbers: sin 30 degrees = 0.5, cos 30 degrees approximately 0.866:

$a = 9.8(0.5 - 0.20\cdot 0.866).$

Compute:

$0.20\cdot 0.866 = 0.1732,$

$$
a \approx 9.8(0.3268) \approx 3.20\,\text{m/s}^2.
$$

Interpretation: friction reduces the downslope acceleration below g sin theta = 4.9 m/s^2.

## Mini recap

- Choose axes aligned with constraints (inclines: parallel/perpendicular).
- Resolve forces with sine/cosine consistently:

$F_x = F\cos\theta, \qquad F_y = F\sin\theta.$

- For an incline angle theta:

$(mg)_\parallel = mg\sin\theta, \qquad (mg)_\perp = mg\cos\theta.$

- Check limiting cases theta = 0 and theta = 90 degrees to catch trig errors.
