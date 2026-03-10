# Vectors in mechanics

## Learning goals

- Distinguish **scalars** (magnitude only) from **vectors** (magnitude + direction).
- Represent displacement and position using vectors and **Cartesian components**.
- Compute vector magnitude and relate it to geometry.
- Understand why velocity, acceleration, and force are naturally treated as vectors in 2D/3D motion.

## Why this matters

Many mechanics statements are not just about “how much,” but also about “which way.” For example:

- “The particle moved 5 m” is incomplete unless you also specify the direction of the change in position.
- “The net force is 10 N” is incomplete unless you specify the direction the interaction tends to push/pull.

Vectors provide a language that keeps direction information attached to the quantity. This prevents common errors such as adding quantities that point in different directions as if they were ordinary numbers.

## Core idea

A **scalar** is described by one number (with units): mass, temperature, time interval, the *distance* traveled.

A **vector** is described by a magnitude and a direction: displacement, velocity (in 2D/3D), acceleration (in 2D/3D), force.

In mechanics we often:

- choose axes,
- express vectors in components along those axes,
- do algebra with components,
- translate back into geometric meaning (magnitude and direction).

## Mathematical formulation

### Vectors, components, and unit vectors

In 2D we commonly choose perpendicular axes with unit vectors $$\\hat{i}$$ (x-direction) and $$\\hat{j}$$ (y-direction). A general vector can be written as:

$$
\\vec{A} = A_x\\,\\hat{i} + A_y\\,\\hat{j}
$$

The numbers $$A_x$$ and $$A_y$$ are the **components** of $$\\vec{A}$$ in this coordinate system.

### Magnitude (length) of a vector

The magnitude of $$\\vec{A}$$ is:

$$
|\\vec{A}| = \\sqrt{A_x^2 + A_y^2}
$$

This is just the Pythagorean theorem: components form a right triangle.

### Position vector and displacement vector

The position of a particle in the plane can be described by a position vector:

$$
\\vec{r}(t) = x(t)\\,\\hat{i} + y(t)\\,\\hat{j}
$$

If the particle is at positions $$\\vec{r}(t_1)$$ and $$\\vec{r}(t_2)$$ at two times, the **displacement vector** is:

$$
\\Delta\\vec{r} = \\vec{r}(t_2) - \\vec{r}(t_1)
$$

In components:

$$
\\Delta\\vec{r} = \\big(x(t_2)-x(t_1)\\big)\\,\\hat{i} + \\big(y(t_2)-y(t_1)\\big)\\,\\hat{j}
$$

### Vector addition and subtraction (why components help)

If

$$
\\vec{A} = A_x\\,\\hat{i} + A_y\\,\\hat{j}, \\qquad \\vec{B} = B_x\\,\\hat{i} + B_y\\,\\hat{j},
$$

then

$$
\\vec{A} + \\vec{B} = (A_x+B_x)\\,\\hat{i} + (A_y+B_y)\\,\\hat{j}.
$$

This is the practical reason we use components: many geometric vector rules reduce to ordinary arithmetic once axes are chosen.

### Why velocity, acceleration, and force are vectors

If position in 2D/3D is a vector function of time, then its time-derivatives are also vectors:

$$
\\vec{v}(t) = \\frac{d\\vec{r}}{dt}, \\qquad \\vec{a}(t) = \\frac{d\\vec{v}}{dt} = \\frac{d^2\\vec{r}}{dt^2}.
$$

Forces model interactions that “push” or “pull” in a direction, so force is also a vector quantity:

$$
\\vec{F}
$$

Later, dynamics connects force and acceleration in vector form.

## Interpretation

- A vector is not just a pair of numbers; it is a geometric quantity that **points**.
- Components depend on the chosen axes, but the **physical vector** does not. Rotating axes changes $$A_x$$ and $$A_y$$, but not the vector itself.
- The displacement vector tells you the change in position from start to end, regardless of the path taken. The distance traveled is generally larger than or equal to the displacement magnitude.

## Typical examples

1) **Walking in a city grid.** Walk 3 blocks east then 4 blocks north. Your displacement is the vector sum; its magnitude is 5 blocks, not 7 blocks.

2) **Wind and airplane.** The plane’s velocity relative to the air and the wind velocity relative to the ground add as vectors to give the plane’s velocity relative to the ground.

3) **Projectile motion preview.** Horizontal and vertical motion can be analyzed via components because position, velocity, and acceleration are vectors.

## Common mistakes

- Adding magnitudes when you should add vectors (e.g., “3 m east + 4 m north = 7 m” for displacement).
- Confusing **displacement magnitude** with **distance traveled**.
- Dropping direction information by writing a vector equation as if it were a scalar equation.
- Mixing component values from different coordinate choices (changing axes mid-problem without updating components).
- Forgetting units on components (components carry the same units as the vector).

## Worked example

A particle moves in the plane. At time $$t_1$$ its position is

$$
\\vec{r}(t_1) = (2\\,\\text{m})\\,\\hat{i} + (1\\,\\text{m})\\,\\hat{j}.
$$

At a later time $$t_2$$ its position is

$$
\\vec{r}(t_2) = (8\\,\\text{m})\\,\\hat{i} + (5\\,\\text{m})\\,\\hat{j}.
$$

Assume $$t_2 - t_1 = 3\\,\\text{s}$$.

### Step 1: Compute the displacement vector

$$
\\Delta\\vec{r} = \\vec{r}(t_2) - \\vec{r}(t_1)
$$

Subtract components:

$$
\\Delta\\vec{r} = (8-2)\\,\\text{m}\\,\\hat{i} + (5-1)\\,\\text{m}\\,\\hat{j} = (6\\,\\text{m})\\,\\hat{i} + (4\\,\\text{m})\\,\\hat{j}.
$$

Interpretation: the net change in position is 6 m in the +x direction and 4 m in the +y direction.

### Step 2: Compute the magnitude of the displacement

$$
|\\Delta\\vec{r}| = \\sqrt{(6\\,\\text{m})^2 + (4\\,\\text{m})^2} = \\sqrt{36+16}\\,\\text{m} = \\sqrt{52}\\,\\text{m}.
$$

Numerically:

$$
|\\Delta\\vec{r}| \\approx 7.21\\,\\text{m}.
$$

### Step 3: Find the direction (angle) of the displacement

Let $$\\theta$$ be the angle measured from the +x axis toward the +y axis. Then:

$$
\\tan\\theta = \\frac{\\Delta y}{\\Delta x} = \\frac{4}{6} = \\frac{2}{3}.
$$

So

$$
\\theta = \\arctan\\left(\\frac{2}{3}\\right) \\approx 33.7^{\\circ}.
$$

### Step 4: Compute the average velocity vector over the interval

Average velocity is displacement divided by elapsed time:

$$
\\vec{v}_{\\text{avg}} = \\frac{\\Delta\\vec{r}}{\\Delta t} = \\frac{(6\\,\\text{m})\\,\\hat{i} + (4\\,\\text{m})\\,\\hat{j}}{3\\,\\text{s}}.
$$

So:

$$
\\vec{v}_{\\text{avg}} = (2\\,\\text{m/s})\\,\\hat{i} + \\left(\\frac{4}{3}\\,\\text{m/s}\\right)\\,\\hat{j}.
$$

Notice how the vector form keeps the direction information automatically.

## Mini recap

- Scalars have magnitude only; vectors have magnitude and direction.
- In Cartesian coordinates:

$$
\\vec{A} = A_x\\,\\hat{i} + A_y\\,\\hat{j}, \\qquad |\\vec{A}| = \\sqrt{A_x^2 + A_y^2}.
$$

- Position and displacement:

$$
\\vec{r}(t) = x(t)\\,\\hat{i} + y(t)\\,\\hat{j}, \\qquad \\Delta\\vec{r} = \\vec{r}(t_2) - \\vec{r}(t_1).
$$

- Velocity and acceleration are vector time-derivatives of position.
- Component methods turn vector algebra into ordinary arithmetic, but you must keep track of axes and units.
