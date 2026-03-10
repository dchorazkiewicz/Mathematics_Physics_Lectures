# Newton’s second law

## Learning goals

- Use Newton’s second law to connect net force and acceleration in vector form.
- Interpret mass as a measure of inertia and understand what changes when m changes.
- Write Newton’s second law in components and solve for unknown accelerations or forces.
- Follow a reliable workflow: choose system → draw forces → write component equations → solve → interpret.

## Why this matters

Newton’s second law is the main predictive rule of introductory dynamics. It turns a force model into an acceleration, which you can then integrate using kinematics to obtain motion.

It also corrects two common misconceptions:

- forces do not “cause velocity,” they cause acceleration (changes in velocity),
- heavier mass does not mean “more force,” it means less acceleration for the same net force.

## Core idea

For a particle (or a system modeled as a particle), the net external force determines acceleration:

- direction of acceleration matches direction of net force,
- magnitude depends on the size of the net force and the mass.

This is the quantitative version of Newton’s first law: zero net force implies zero acceleration.

## Mathematical formulation

### Vector form

In an inertial frame:

$$
\sum \vec{F} = m\vec{a}.
$$

Here:

- the sum is over all external forces acting on the system,
- m is the mass of the particle (assumed constant in this course),
- \vec{a} is the acceleration of the particle.

### Component form (2D)

Choose axes x and y. Then the vector equation is equivalent to two scalar equations:

$$
\sum F_x = ma_x, \qquad \sum F_y = ma_y.
$$

In 3D you add:

$$
\sum F_z = ma_z.
$$

### Units check

If force is in newtons and mass in kilograms, acceleration comes out in m/s^2, consistent with:

$$
1\,\text{N} = 1\,\text{kg}\cdot\text{m/s}^2.
$$

### What “net force” means

Net force is a vector sum:

$$
\vec{F}_{\text{net}} = \sum \vec{F}.
$$

You must list all forces acting on the chosen system (gravity, normal, friction, tension, applied forces, etc.) and add them vectorially.

## Interpretation

### Mass as inertia

For a given net force magnitude, acceleration magnitude is:

$$
a = \frac{F_{\text{net}}}{m}.
$$

So:

- larger mass → smaller acceleration for the same net force,
- larger net force → larger acceleration for the same mass.

Mass here is not “weight” and not “how hard gravity pulls.” Weight is a force; mass is a property of the object.

### A standard solving workflow

1) Choose the system (what object are you writing the equation for?).  
2) Choose axes.  
3) Draw a free-body diagram (list all forces on the system).  
4) Resolve forces into components.  
5) Write \sum F_x = ma_x and \sum F_y = ma_y.  
6) Use constraints (e.g., a_y = 0 if it stays on a table).  
7) Solve for the unknowns and interpret the sign/direction.

## Typical examples

1) Block pulled on a horizontal surface (with or without friction).

2) Block on an incline (gravity components along and perpendicular to the plane).

3) Elevator accelerating up or down (tension vs weight determining acceleration).

## Common mistakes

- Writing \sum F = ma with F as a single force rather than the net sum.
- Mixing up mass and weight (using m = mg or similar incorrect identifications).
- Forgetting that \sum \vec{F} = m\vec{a} is a vector equation; you cannot treat directions as separate “afterthoughts.”
- Assuming that the largest force determines acceleration direction; it is the net vector sum that matters.
- Using a non-inertial frame without adding inertial forces (or without switching to an inertial frame).

## Worked example

A block of mass:

$$
m = 5.0\,\text{kg}
$$

is pulled along a horizontal surface by a horizontal force:

$$
F = 18\,\text{N}.
$$

The kinetic friction force magnitude is:

$$
f_k = 6.0\,\text{N},
$$

opposing the motion. Find:

1) the acceleration magnitude and direction,  
2) the net force.

### Step 1: Choose axes and list forces in the direction of motion

Choose x along the pull direction (positive). The horizontal forces are:

- +F (pull),
- -f_k (friction).

### Step 2: Compute net force in x

$$
F_{\text{net},x} = F - f_k = 18 - 6 = 12\,\text{N}.
$$

Direction: positive x.

### Step 3: Apply Newton’s second law in x

$$
\sum F_x = ma_x \Rightarrow 12 = (5.0)a_x.
$$

So:

$$
a_x = \frac{12}{5.0} = 2.4\,\text{m/s}^2.
$$

### Step 4: Net force vector (here 1D)

In this problem the net force is purely horizontal:

$$
\vec{F}_{\text{net}} = (12\,\text{N})\hat{i}.
$$

Interpretation: the block accelerates in the direction of the pull because the pull exceeds friction.

## Mini recap

- Newton’s second law (inertial frame):

$$
\sum \vec{F} = m\vec{a}.
$$

- Component form (2D):

$$
\sum F_x = ma_x, \qquad \sum F_y = ma_y.
$$

- Net force is the vector sum of all forces on the system.
- Use a consistent workflow: system → forces → components → equations → constraints → solve → interpret.
