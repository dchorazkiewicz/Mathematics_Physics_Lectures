# Reference frames and position

## Learning goals

- Explain what a **reference frame** is (observer + coordinates + clock) and why motion descriptions depend on it.
- Define **position** in 1D and 2D as a coordinate (or vector) **relative to an origin**.
- Distinguish clearly between the **physical object** and its **mathematical description** (particle model, coordinates).
- Compute displacement from positions and understand what changes (and what does not) when the origin is moved.

## Why this matters

There is no such thing as “the position of an object” without also saying *relative to what*. If you do not specify a reference frame, statements like “the particle is at 3 meters” are incomplete: 3 meters from where, along which direction, measured by which clock?

Kinematics begins by making these choices explicit. Later, in dynamics, the choice of frame becomes even more important because Newton’s laws are simplest in special frames called **inertial frames**.

## Core idea

A **reference frame** is the backdrop relative to which you describe motion. In the simplest settings it includes:

- an **origin** (the point you call zero),
- one or more **axes** (the directions you call positive),
- a **time coordinate** (a clock that defines the time variable).

Once a frame is chosen, the state “where is the object?” becomes a mathematical object:

- in 1D: a single coordinate $$x(t)$$,
- in 2D/3D: a position vector $$\\vec{r}(t)$$ or a set of coordinates such as $$x(t), y(t)$$.

The **physical object** is real; the **numbers** you assign to represent its position are part of your description, and they depend on your chosen frame.

## Mathematical formulation

### Position in 1D

Choose:

- an origin (where $$x=0$$),
- a positive direction (for example, “to the right is positive”).

Then the position of a particle is described by a function of time:

$$
x(t)
$$

### Position in 2D (planar motion)

Choose perpendicular axes (for example, east as $$x$$ and north as $$y$$). The particle’s position can be written as a vector:

$$
\\vec{r}(t)
$$

or in components (Cartesian coordinates):

$$
\\vec{r}(t) = x(t)\\,\\hat{i} + y(t)\\,\\hat{j}
$$

where $$\\hat{i}$$ and $$\\hat{j}$$ are unit vectors along the chosen axes.

### Displacement (change in position)

Displacement is the difference between two positions (vector difference in 2D/3D, scalar difference in 1D). In 1D:

$$
\\Delta x = x(t_2) - x(t_1)
$$

In vector form:

$$
\\Delta \\vec{r} = \\vec{r}(t_2) - \\vec{r}(t_1)
$$

Displacement is not “distance traveled.” Distance accumulates along the path; displacement depends only on the start and end positions.

### Changing the origin (same physical point, different coordinate)

Suppose you shift your origin by a constant amount. In 1D, if the new origin is located at coordinate $$x_0$$ in the old system, then the new coordinate is:

$$
x'(t) = x(t) - x_0
$$

This changes the numbers you call “position,” but it does not change the physical location of the particle. Importantly, displacement is unchanged by this shift:

$$
\\Delta x' = x'(t_2) - x'(t_1) = \\big(x(t_2)-x_0\\big) - \\big(x(t_1)-x_0\\big) = x(t_2) - x(t_1) = \\Delta x
$$

## Interpretation

1) **Frame dependence is not a flaw.** It is expected. The purpose of choosing a frame is to describe motion conveniently.

2) **Coordinates are labels, not physical substances.** The particle does not “have” a negative position; negative simply means “on the negative side of the chosen origin.”

3) **The particle model is a choice.** When we write $$x(t)$$ or $$\\vec{r}(t)$$, we assume the object’s size/rotation can be neglected for the question at hand. If the object’s orientation matters (e.g., a rolling wheel), a richer model is needed.

4) **Some quantities are less sensitive to origin choices.** Position changes if you move the origin, but displacement does not. Later, you will see that velocity and acceleration are also unaffected by shifting the origin by a constant amount.

## Typical examples

1) **1D motion along a hallway.** Choose the door as $$x=0$$ and “toward the window” as positive. A student walking back and forth can have $$x(t)$$ that increases, decreases, and changes sign.

2) **2D motion on a map.** Choose axes east/north and an origin at a landmark. A runner’s position is a pair $$\\big(x(t), y(t)\\big)$$, or a vector $$\\vec{r}(t)$$.

3) **Same situation, different convenience.** For a problem about motion near a particular point (a stop sign, a spring’s equilibrium point), placing the origin there often simplifies the algebra and the interpretation.

## Common mistakes

- Forgetting to specify an origin and positive direction before writing coordinates.
- Switching sign conventions mid-problem (for example, sometimes “up is positive,” later “down is positive” without updating equations).
- Confusing **position** with **distance traveled** (especially when motion reverses direction).
- Treating “negative position” as “impossible” rather than as “on the negative side of the chosen origin.”
- Mixing the physical object with the coordinate system (thinking the coordinate system is “attached” to space rather than chosen by the analyst).

## Worked example

A bicycle moves along a straight street. You choose a reference frame with:

- origin at a stop sign,
- positive direction pointing east,
- time $$t$$ measured in seconds.

At $$t=0$$ the bicycle is 20 m west of the stop sign. At $$t=5\\,\\text{s}$$ it is 30 m east of the stop sign.

### Step 1: Translate the words into coordinates

“20 m west” means the coordinate is negative:

$$
x(0) = -20\\,\\text{m}
$$

“30 m east” means the coordinate is positive:

$$
x(5) = +30\\,\\text{m}
$$

### Step 2: Compute displacement

$$
\\Delta x = x(5) - x(0) = 30 - (-20) = 50\\,\\text{m}
$$

Interpretation: the bicycle’s net change in position is 50 m to the east (in this chosen coordinate sense).

### Step 3: (Preview) Compute average velocity over the interval

Average velocity in 1D is displacement divided by elapsed time:

$$
v_{\\text{avg}} = \\frac{\\Delta x}{\\Delta t} = \\frac{50\\,\\text{m}}{5\\,\\text{s}} = 10\\,\\text{m/s}
$$

This is a *kinematic* statement about how position changed; it does not yet explain what caused the motion.

### Step 4: Change the origin and verify what changes

Now choose a new origin at a tree that is 10 m east of the stop sign. In the old coordinates, the tree is at:

$$
x_0 = +10\\,\\text{m}
$$

Define the new coordinate:

$$
x'(t) = x(t) - x_0
$$

Compute the bicycle’s positions in the new coordinates:

$$
x'(0) = x(0) - 10 = -20 - 10 = -30\\,\\text{m}
$$

$$
x'(5) = x(5) - 10 = 30 - 10 = 20\\,\\text{m}
$$

Compute displacement in the new coordinates:

$$
\\Delta x' = x'(5) - x'(0) = 20 - (-30) = 50\\,\\text{m}
$$

The numerical positions changed (because the origin moved), but the displacement did not. This is exactly what you should expect: displacement compares two positions within the *same* frame, so shifting the origin by a constant cancels out.

## Mini recap

- A reference frame specifies an origin, axes (positive directions), and a clock.
- Position is frame-dependent: $$x(t)$$ in 1D, $$\\vec{r}(t)$$ in 2D/3D.
- Displacement is the difference of positions:

$$
\\Delta x = x(t_2)-x(t_1), \\qquad \\Delta\\vec{r} = \\vec{r}(t_2)-\\vec{r}(t_1)
$$

- Shifting the origin changes position coordinates but does not change displacement.
- Be explicit about sign conventions to avoid common errors.
