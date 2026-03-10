# Spring force and Hooke’s law

## Learning goals

- Model an ideal spring force using Hooke’s law and a clear sign convention.
- Distinguish spring extension/compression from absolute position and define equilibrium length.
- Use spring force together with other forces in Newton’s second law.
- Avoid common sign mistakes and “force magnitude only” reasoning.

## Why this matters

Springs are a standard model for “restoring” interactions: when displaced from equilibrium, they pull/push back toward equilibrium.

Even when no physical spring is present, many systems behave approximately like springs near a stable equilibrium (small displacements). Later, spring forces will also connect dynamics to sinusoidal motion.

## Core idea

An ideal spring exerts a force that:

- is proportional to how far it is stretched or compressed relative to its natural length,
- points in the direction that tends to restore the spring toward its equilibrium length.

The spring does not “want” a particular position in space; it “wants” a particular length. The force depends on extension/compression, not on where the spring is located.

## Mathematical formulation

### 1D spring attached along the x-axis

Choose an x-axis along the spring. Let x = 0 correspond to the spring’s equilibrium (natural) length configuration for the mass.

Hooke’s law (ideal spring) is:

$F_{\text{spring}} = -kx,$

where:

- k is the spring constant (N/m),
- x is the displacement from equilibrium (positive for extension in the +x direction, negative for compression in the -x direction),
- the minus sign encodes “restoring”: the force points opposite the displacement.

Vector form along the axis (if you want to emphasize direction):

$\vec{F}_{\text{spring}} = -kx\,\hat{i}.$

### Units

Since force is N and x is m, k must have units:

$[k] = \text{N/m}.$

### Combining with Newton’s second law

If the spring is the only force along x (frictionless horizontal spring–mass), then:

$$
m\frac{d^2x}{dt^2} = -kx.
$$

This is an equation of motion that produces sinusoidal motion. You do not need to solve it now to use Hooke’s law, but it shows the connection to oscillations.

## Interpretation

- If x > 0 (spring stretched), force is negative (pulls back).
- If x < 0 (spring compressed), force is positive (pushes back).
- Spring force is zero at equilibrium (x = 0).

Hooke’s law is an approximation that works well for small deformations in many real springs, but it has limits (springs can yield or become nonlinear at large extensions).

## Typical examples

1) Mass on a spring on a frictionless table: spring force provides acceleration toward equilibrium.

2) Vertical spring with gravity: equilibrium position is shifted because weight is balanced by spring force.

3) Two springs in series/parallel: effective stiffness changes (often treated later, but the force law remains restoring and proportional in the ideal model).

## Common mistakes

- Forgetting the minus sign and treating the spring force as always positive.
- Using x as absolute position rather than displacement from equilibrium length.
- Mixing extension and compression sign conventions mid-solution.
- Assuming Hooke’s law is exact for all extensions (it is a model with a valid range).
- Confusing the spring constant k (N/m) with energy or with a force.

## Worked example

A 2.0 kg block is attached to a horizontal spring with spring constant:

$k = 120\,\text{N/m}.$

The surface is frictionless. The block is displaced to the right by:

$x = 0.15\,\text{m}$

from equilibrium and released. At the release instant:

1) find the spring force,  
2) find the acceleration of the block (direction and magnitude).

### Step 1: Spring force

Hooke’s law:

$F_{\text{spring}} = -kx.$

So:

$F_{\text{spring}} = -(120)(0.15) = -18\,\text{N}.$

Interpretation: the negative sign means the force is to the left (toward equilibrium).

### Step 2: Acceleration

At that instant the only horizontal force is the spring force, so:

$$
F_{\text{net}} = ma \Rightarrow a = \frac{F_{\text{spring}}}{m}.
$$

So:

$$
a = \frac{-18}{2.0} = -9.0\,\text{m/s}^2.
$$

The block accelerates leftward toward equilibrium.

## Mini recap

- Ideal spring force (1D about equilibrium):

$F_{\text{spring}} = -kx.$

- The sign encodes restoring direction.
- k has units N/m and Hooke’s law has a regime of validity.
- Combine with Newton’s second law to get acceleration and (if desired) an equation of motion.
