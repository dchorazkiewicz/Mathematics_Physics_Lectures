# Classical Mechanics (Particle Mechanics): Kinematics and Dynamics

## How to use these notes

- The lecture is split into **small files**, each covering one narrow idea.
- Read in order. Later sections reuse notation and assumptions introduced earlier.
- Each conceptual file includes learning goals, typical examples, common mistakes, and at least one worked problem.

## Scope (what we model)

These notes focus on **classical (Newtonian) mechanics** at the level of a first university course, mainly using the **particle model**:

- We represent an object by a point located at its position.
- We track how that position changes with time.
- We use forces as **models of interaction** to predict acceleration and hence motion.

What is mostly *not* covered here: rigid-body rotation, Lagrangian/Hamiltonian formalisms, non-inertial frame machinery beyond introductory intuition, and relativistic mechanics.

## Prerequisites

- Algebra and trigonometry.
- Basic calculus ideas:
  - a derivative as an instantaneous rate of change,
  - an integral as accumulation (area under a curve).

When calculus is used, the physical meaning is explained alongside the mathematics.

## Global notation conventions

Time:

$t$

One-dimensional position, velocity, acceleration:

$$
x(t), \quad v(t) = \frac{dx}{dt}, \quad a(t) = \frac{dv}{dt} = \frac{d^2x}{dt^2}
$$

Vector position, velocity, acceleration (in 2D/3D):

$$
\vec{r}(t), \quad \vec{v}(t) = \frac{d\vec{r}}{dt}, \quad \vec{a}(t) = \frac{d\vec{v}}{dt}
$$

Forces and mass:

$\vec{F}, \quad m$

Near-Earth gravitational acceleration magnitude:

$g$

## Modeling assumptions (to be stated explicitly when used)

Common idealizations you will see throughout:

- “Neglect air resistance.”
- “Uniform gravity near Earth” (constant $g$).
- “Massless, inextensible rope” and “frictionless pulley” (in tension problems).
- “Friction coefficient model” (static and kinetic friction).

Every time an idealization matters, it will be stated as an assumption in the relevant section.
