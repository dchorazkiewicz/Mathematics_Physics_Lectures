# Free-body diagrams

## Learning goals

- Define what a free-body diagram (FBD) is and what it is for.
- Isolate a system correctly and list all external forces acting on it.
- Avoid the two big errors: omitting a force and including a force that does not act on the chosen body.
- Turn an FBD into component equations using Newton’s second law.

## Why this matters

Most dynamics mistakes come from wrong force lists, not from algebra.

A free-body diagram is the standard tool that forces you to be explicit about:

- what your system is,
- what interactions act on it,
- which directions those interactions act in.

If you draw a correct FBD, writing:

$$
\sum \vec{F} = m\vec{a}
$$

becomes routine. If you skip it, you will guess forces and typically guess wrong.

## Core idea

A free-body diagram is a picture of one isolated system showing only the forces acting on it from the outside.

Rules:

1) Choose the system (one object or a collection of objects).  
2) Draw the system as a simple shape (point/box).  
3) Draw all external forces as arrows on that shape.  
4) Label each force with a clear name and direction.  
5) Do not include forces the system exerts on other objects (those are not acting on the system).

The FBD is not a sketch of the whole scene. It is a force accounting diagram.

## Mathematical formulation

Once the FBD is drawn, Newton’s second law becomes:

$$
\sum \vec{F} = m\vec{a}.
$$

Most problems are solved by choosing axes and writing component equations. In 2D:

$$
\sum F_x = ma_x, \qquad \sum F_y = ma_y.
$$

Then you add constraints (like a_y = 0 for a block sliding on a table).

## Interpretation

### How to decide whether a force should be on the diagram

Ask: “Is there an interaction between the system and something outside the system that can exert a force?”

Common force sources:

- gravity (Earth on object),
- contact normal force (surface on object),
- friction (surface on object, parallel to surface),
- tension (rope on object),
- spring force (spring on object),
- applied pushes/pulls (hand, engine, etc.).

### Forces are not kinematic quantities

Do not put “velocity,” “acceleration,” or “motion direction” as forces. They are outcomes, not forces.

### Balanced vs unbalanced

Whether forces balance is not decided by “what looks symmetric.” It is decided by the net force sum and the acceleration.

## Typical examples

1) Block on a table pulled by a rope: forces include weight, normal, tension, friction (if present).

2) Hanging mass: forces include weight and tension.

3) Block on incline: forces include weight, normal, friction (if present).

4) Two blocks connected by a rope: draw separate FBDs for each block before writing equations.

## Common mistakes

- Omitting a force (most often: friction, normal, or tension).
- Including a force that does not act on the object (e.g., adding “force the object exerts on the rope” into the object’s FBD).
- Pairing forces incorrectly using Newton’s third law (e.g., treating weight and normal as a third-law pair).
- Drawing friction in the wrong direction (it opposes relative slip or the tendency to slip).
- Assuming normal equals mg without checking vertical acceleration and other vertical forces.

## Worked example

A block of mass m = 3.0 kg is pulled along a horizontal surface by a rope that makes an angle of 30 degrees above the horizontal. The rope tension magnitude is T = 20 N. The coefficient of kinetic friction is mu_k = 0.25. Take g = 9.8 m/s^2.

Find the block’s acceleration.

### Step 1: Choose the system and axes

System: the block.

Axes: x horizontal to the right, y vertical upward.

### Step 2: Draw the free-body diagram (describe it clearly)

Forces on the block:

- Weight mg downward.
- Normal force N upward (from the surface).
- Tension T along the rope, 30 degrees above the +x direction.
- Kinetic friction f_k along the surface opposing the motion (to the left).

### Step 3: Resolve forces into components

Tension components:

$T_x = T\cos 30^\circ, \qquad T_y = T\sin 30^\circ.$

Friction magnitude:

$f_k = \mu_k N.$

### Step 4: Write Newton’s second law in y to find N

The block does not accelerate vertically (it stays on the surface), so a_y = 0.

Sum of forces in y:

$N + T_y - mg = ma_y = 0.$

So:

$N = mg - T\sin 30^\circ.$

Compute:

$mg = (3.0)(9.8) = 29.4\,\text{N},$

$T\sin 30^\circ = 20(0.5) = 10\,\text{N}.$

So:

$N = 29.4 - 10 = 19.4\,\text{N}.$

Then kinetic friction magnitude is:

$f_k = \mu_k N = 0.25(19.4) = 4.85\,\text{N}.$

### Step 5: Write Newton’s second law in x and solve for a_x

Sum of forces in x:

$T_x - f_k = ma_x.$

Compute:

$$
T_x = 20\cos 30^\circ \approx 20(0.866) \approx 17.32\,\text{N}.
$$

So:

$17.32 - 4.85 = (3.0)a_x.$

$$
12.47 = 3.0a_x \Rightarrow a_x \approx 4.16\,\text{m/s}^2.
$$

Interpretation: pulling upward reduces the normal force, which reduces friction, which increases the acceleration compared to a purely horizontal pull of the same magnitude.

## Mini recap

- An FBD isolates one system and shows only external forces acting on it.
- Workflow:
  - choose system and axes,
  - list/draw forces,
  - resolve components,
  - write:

$$
\sum F_x = ma_x, \qquad \sum F_y = ma_y,
$$
  - apply constraints,
  - solve and interpret.
- Most dynamics errors are FBD errors (missing forces, wrong directions, wrong system boundary).
