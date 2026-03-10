# Particle on a horizontal surface

## Learning goals

- Set up Newton’s second law for a particle/block on a horizontal surface with correct forces.
- Handle pulls/pushes with or without friction, including angled forces.
- Use the vertical equation to determine the normal force and then friction.
- Follow a repeatable solving workflow and avoid sign mistakes.

## Why this matters

This is the simplest “full” dynamics problem type because it includes the core ingredients you will reuse everywhere:

- weight and normal force,
- possible friction,
- an applied force,
- component equations and constraints (usually a_y = 0).

Once you can do horizontal-surface problems cleanly, inclines and connected bodies become much easier.

## Core idea

On a horizontal surface, the vertical motion is usually constrained:

$a_y = 0.$

That constraint is what determines the normal force. Friction (if present) depends on N in the simplest coefficient model, so you typically solve:

vertical equation → N → friction magnitude → horizontal equation → acceleration.

## Mathematical formulation

Choose axes:

- x along the surface (positive in the intended motion direction),
- y vertical upward.

Forces that commonly appear:

- weight mg downward,
- normal force N upward,
- applied force F (possibly at an angle),
- friction (static or kinetic) along the surface.

Newton’s second law:

$$
\sum F_x = ma_x, \qquad \sum F_y = ma_y.
$$

With the contact constraint:

$a_y = 0.$

### Friction model reminder

- If slipping: f_k = mu_k N.
- If not slipping: 0 <= f_s <= mu_s N and direction opposes the tendency to slip.

## Interpretation

- N is not automatically mg. It changes if the applied force has a vertical component.
- If you pull upward at an angle, N decreases and friction decreases.
- If you push downward at an angle, N increases and friction increases.

This is why “same magnitude of applied force” can produce different accelerations depending on the angle.

## Typical examples

1) Horizontal pull with kinetic friction: simplest acceleration calculation.

2) Angled pull (upward): reduced friction, larger acceleration.

3) Angled push (downward): increased friction, smaller acceleration.

4) Static friction threshold: find the maximum applied force before motion begins.

## Common mistakes

- Using N = mg even when the applied force has a vertical component.
- Choosing friction direction incorrectly (it opposes relative motion/tendency, not necessarily the applied force direction).
- Using static friction as an equality f_s = mu_s N in all cases.
- Forgetting that a_y = 0 is a constraint only while contact is maintained.
- Mixing degrees/radians in trig calculations.

## Worked example

A 10 kg crate is pulled along a horizontal floor by a rope with tension magnitude F = 40 N at angle 20 degrees above horizontal. The coefficient of kinetic friction is mu_k = 0.30. Take g = 9.8 m/s^2.

Find the acceleration magnitude.

### Step 1: Choose axes and list forces

Axes: x to the right, y up.

Forces on the crate:

- weight mg downward,
- normal force N upward,
- tension F at 20 degrees above +x,
- kinetic friction f_k opposite motion (to the left).

### Step 2: Resolve the applied force

$F_x = F\cos 20^\circ, \qquad F_y = F\sin 20^\circ.$

Numerically, cos 20 degrees ≈ 0.940, sin 20 degrees ≈ 0.342:

$$
F_x \approx 40(0.940) = 37.6\,\text{N},
$$

$$
F_y \approx 40(0.342) = 13.7\,\text{N}.
$$

### Step 3: Vertical equation to find N

No vertical acceleration, so a_y = 0:

$$
N + F_y - mg = 0 \Rightarrow N = mg - F_y.
$$

Compute mg:

$mg = (10)(9.8) = 98\,\text{N}.$

So:

$$
N \approx 98 - 13.7 = 84.3\,\text{N}.
$$

### Step 4: Friction magnitude

$$
f_k = \mu_k N \approx 0.30(84.3) = 25.3\,\text{N}.
$$

### Step 5: Horizontal equation for acceleration

$F_x - f_k = ma.$

So:

$37.6 - 25.3 = (10)a.$

$$
12.3 = 10a \Rightarrow a \approx 1.23\,\text{m/s}^2.
$$

Interpretation: pulling upward reduces N, which reduces friction and increases acceleration compared to a purely horizontal pull with the same magnitude.

## Mini recap

- Horizontal surface workflow:
  - write y equation with a_y = 0 to get N,
  - compute friction from N (if needed),
  - write x equation to get a_x.
- Angled pulls change N and therefore friction.
- Static friction uses an inequality; kinetic friction uses f_k = mu_k N in the simplest model.
