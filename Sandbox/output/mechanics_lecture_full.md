<!-- SOURCE: lecture/00_frontmatter.md -->

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

$$
t
$$

One-dimensional position, velocity, acceleration:

$$
x(t), \\quad v(t) = \\frac{dx}{dt}, \\quad a(t) = \\frac{dv}{dt} = \\frac{d^2x}{dt^2}
$$

Vector position, velocity, acceleration (in 2D/3D):

$$
\\vec{r}(t), \\quad \\vec{v}(t) = \\frac{d\\vec{r}}{dt}, \\quad \\vec{a}(t) = \\frac{d\\vec{v}}{dt}
$$

Forces and mass:

$$
\\vec{F}, \\quad m
$$

Near-Earth gravitational acceleration magnitude:

$$
g
$$

## Modeling assumptions (to be stated explicitly when used)

Common idealizations you will see throughout:

- “Neglect air resistance.”
- “Uniform gravity near Earth” (constant $$g$$).
- “Massless, inextensible rope” and “frictionless pulley” (in tension problems).
- “Friction coefficient model” (static and kinetic friction).

Every time an idealization matters, it will be stated as an assumption in the relevant section.

<!-- SOURCE: lecture/01_introduction.md -->

# Introduction

## Learning goals

- Distinguish clearly between **kinematics** (describing motion) and **dynamics** (explaining/predicting motion from interactions).
- Understand what it means to **model** a real object as a particle with a position function.
- Interpret derivatives and integrals as **rates of change** and **accumulation** in the context of motion.

## Why this matters

If you cannot separate “what the motion is” from “why the motion happens,” mechanics becomes a list of formulas to memorize. This lecture aims to build a reliable mental model:

- In **kinematics**, you are given (or you measure) motion and you describe it precisely.
- In **dynamics**, you propose interaction models (forces) and use them to *determine* the motion.

The bridge between the two is **acceleration**.

## Core idea

Mechanics starts with a choice: we decide what aspects of a real situation matter and what can be neglected. Often, the first useful model is a **particle**:

- the object is represented by a point,
- its location is described by coordinates,
- its motion is a function of time.

This is already a strong abstraction: the same physical object can be described by many coordinate choices (different origins/axes), and the same motion can be expressed in different mathematical forms.

## Mathematical formulation

In one dimension, motion is described by a position function:

$$
x(t)
$$

Velocity and acceleration are defined as time-derivatives:

$$
v(t) = \\frac{dx}{dt}, \\qquad a(t) = \\frac{dv}{dt} = \\frac{d^2x}{dt^2}
$$

The derivative here has a physical meaning:

- $$v(t)$$ is the **instantaneous rate of change** of position (how fast and in which direction the position coordinate is changing).
- $$a(t)$$ is the **instantaneous rate of change** of velocity (how quickly the velocity changes in time).

In dynamics, the central idea (developed later) is that interactions determine acceleration. In Newtonian particle mechanics, this is expressed by:

$$
\\sum \\vec{F} = m\\vec{a}
$$

This equation is not “a definition of force.” It is a modeling principle: once you choose your force models, you have an equation that determines the acceleration, and then (using kinematics) the motion.

## Interpretation

- Kinematics can tell you **how** something moves (and reconstruct missing information from derivatives/integrals).
- Dynamics aims to tell you **what interaction models are consistent** with observed motion, or to **predict motion** under specified interactions.

You should get in the habit of asking two different questions:

1. **Description question (kinematics):** “Given $$x(t)$$ (or data), what are $$v(t)$$ and $$a(t)$$? What does the motion look like?”
2. **Explanation question (dynamics):** “What forces act? What is the net force? What acceleration follows?”

## Typical examples

- **A car that speeds up then slows down:** kinematics describes the changing velocity; dynamics explains it via engine force, braking, and friction.
- **A thrown ball:** kinematics predicts the parabolic path under constant acceleration; dynamics justifies why acceleration is (approximately) constant near Earth.
- **An object on an incline:** kinematics might start from measured acceleration; dynamics derives that acceleration from gravity, normal force, and friction.

## Common mistakes

- Treating mechanics as “plug into the right formula” rather than a modeling workflow.
- Confusing **position** with **distance traveled** (distance accumulates along the path; position is a coordinate relative to an origin).
- Thinking that “motion requires a force” (a misconception addressed carefully when Newton’s first law is introduced).
- Treating acceleration as only “speeding up,” ignoring acceleration caused by **changing direction** (important in 2D and circular motion).

## Worked example

An object moves along a line with position

$$
x(t) = 1 + 2t - t^2
$$

1) Compute velocity and acceleration.

Differentiate:

$$
v(t) = \\frac{dx}{dt} = 2 - 2t
$$

Differentiate again:

$$
a(t) = \\frac{dv}{dt} = -2
$$

So the acceleration is constant and negative (in this coordinate choice).

2) What can kinematics tell you, and what can’t it tell you?

- Kinematics tells you there is a turning time when $$v(t)=0$$:

$$
2 - 2t = 0 \\;\\Rightarrow\\; t = 1
$$

- It tells you the motion is initially in the positive direction (since $$v(0)=2>0$$), then reverses after $$t=1$$.

But kinematics alone does not tell you *which interaction* caused the constant acceleration. If you additionally know the mass is $$m=0.50\\,\\text{kg}$$ and you adopt Newton’s second law (dynamics), then the **net force** would be:

$$
F_{\\text{net}} = ma = (0.50)(-2) = -1\\,\\text{N}
$$

That net force could arise from many physical situations (gravity component, a spring, a constant push, etc.). Identifying a realistic force model is part of dynamics.

## Mini recap

- Kinematics describes motion via $$x(t)$$ (or $$\\vec{r}(t)$$) and its derivatives.
- Velocity and acceleration are rates of change in time.
- Dynamics explains/predicts acceleration from forces; acceleration is the bridge.
- Mechanics is a modeling discipline: choices and assumptions matter.

<!-- SOURCE: lecture/kinematics/01_reference_frames_and_position.md -->

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

<!-- SOURCE: lecture/kinematics/02_vectors_in_mechanics.md -->

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

<!-- SOURCE: lecture/kinematics/03_trajectory_and_position_function.md -->

# Trajectory and position function

## Learning goals

- Distinguish the **trajectory** (geometric path in space) from the **law of motion** (position as a function of time).
- Describe planar motion using a position vector $$\\vec{r}(t)$$ or component functions $$x(t), y(t)$$.
- Eliminate time (when appropriate) to obtain an equation for the trajectory, and understand what information is lost.
- Recognize that different time dependences can produce the **same trajectory**.

## Why this matters

Students often say “the trajectory is $$x(t)$$” or think that a curve like a parabola fully determines the motion. But a curve in space only tells you **where** the particle can be; it does not tell you **when** the particle is at each point, how fast it moves along the curve, or in which direction it is traversed.

Mechanics needs both:

- **Geometry:** the set of points the particle visits (trajectory).
- **Timing:** how position changes with time (position function).

This distinction becomes essential in later topics like projectile motion and circular motion, where geometry alone can be misleading.

## Core idea

Think of a motion as a movie:

- The **trajectory** is like a long-exposure photograph of the moving object: it shows the shape traced out in space.
- The **position function** tells you the full movie frame-by-frame: it encodes timing and therefore speed and direction.

In 1D, the “trajectory” is just a line (the x-axis); timing still matters, but geometry is trivial. In 2D/3D, geometry becomes informative, but it is still not the whole story.

## Mathematical formulation

### Position as a function of time (law of motion)

In 2D, the motion is described by:

$$
\\vec{r}(t) = x(t)\\,\\hat{i} + y(t)\\,\\hat{j}
$$

Equivalently, you can specify the pair of component functions:

$$
x(t), \\qquad y(t).
$$

This is the **law of motion**: it tells you where the particle is at each time.

### Trajectory as a geometric set

The **trajectory** is the set of points in the plane that the particle occupies at some time:

$$
\\{(x(t), y(t)) \\;\\text{for all relevant } t\\}.
$$

Often (but not always) you can eliminate $$t$$ between $$x(t)$$ and $$y(t)$$ to get a relation between $$x$$ and $$y$$:

$$
F(x,y) = 0.
$$

That relation describes a curve in space: the trajectory (or a part of it).

### What you lose when you eliminate time

If you eliminate $$t$$ and obtain a curve equation, you typically lose:

- the **speed** along the curve (fast vs slow),
- the **direction** of travel (which way along the curve),
- the **timing** (where the particle is at a specific time),
- how many times the particle passes the same point (possible in loops/oscillations).

## Interpretation

Two motions can share the same trajectory but be physically very different. For example, moving along the same circle at different speeds gives the same trajectory (a circle) but different velocity and acceleration as functions of time.

Conversely, two motions can have very different trajectories even if their speed functions look similar: geometry depends on the direction of motion, not just the magnitude.

## Typical examples

1) **1D motion:** A particle moves along a line. The trajectory is the x-axis (or a segment of it). The interesting part is the timing: when does it pass a point, does it reverse direction, etc.

2) **Uniform circular motion:** The trajectory is a circle, but the position function can describe going around the circle quickly or slowly (different periods).

3) **Projectile motion preview:** The trajectory under uniform gravity (neglecting air resistance) is a parabola, but the same parabola could correspond to different launch speeds if the timing is changed (for example, by reparameterizing time).

## Common mistakes

- Treating a curve equation like $$y = f(x)$$ as “the full motion” (it is only geometry, not timing).
- Confusing the **path length** (distance traveled along the curve) with displacement.
- Assuming that if two motions have the same trajectory, then they have the same velocity/acceleration at corresponding points (not true without timing information).
- Eliminating time incorrectly (for example, dividing by an expression that could be zero without checking).
- Forgetting that a single point on the trajectory may correspond to multiple times (especially in periodic motion).

## Worked example

Consider the planar motion defined by:

$$
x(t) = 2t, \\qquad y(t) = t^2,
$$

for $$t \\ge 0$$.

### Step 1: Identify what the law of motion tells you

At each time $$t$$, the position is:

$$
\\vec{r}(t) = (2t)\\,\\hat{i} + (t^2)\\,\\hat{j}.
$$

This already answers questions like “Where is the particle at $$t=3\\,\\text{s}$$?”:

$$
x(3)=6, \\qquad y(3)=9.
$$

### Step 2: Find the trajectory by eliminating time

From $$x(t)=2t$$ we solve for $$t$$:

$$
t = \\frac{x}{2}.
$$

Substitute into $$y(t)=t^2$$:

$$
y = \\left(\\frac{x}{2}\\right)^2 = \\frac{x^2}{4}.
$$

So the trajectory is the parabola:

$$
y = \\frac{x^2}{4}, \\qquad x \\ge 0.
$$

This describes the *shape* of the path in the plane.

### Step 3: Show that the same trajectory can come from a different time dependence

Define a new motion:

$$
\\tilde{x}(t) = 2t^2, \\qquad \\tilde{y}(t) = t^4,
$$

for $$t \\ge 0$$.

Eliminate time again. From $$\\tilde{x}(t)=2t^2$$:

$$
t^2 = \\frac{\\tilde{x}}{2}.
$$

Then

$$
\\tilde{y} = t^4 = \\left(t^2\\right)^2 = \\left(\\frac{\\tilde{x}}{2}\\right)^2 = \\frac{\\tilde{x}^2}{4}.
$$

So the **trajectory is the same parabola**, but the timing is different: the second motion moves along the curve more slowly near the origin (because $$\\tilde{x}(t)$$ grows like $$t^2$$, not like $$t$$).

### Step 4: What did the curve equation fail to tell you?

The curve

$$
y = \\frac{x^2}{4}
$$

does not tell you:

- whether the particle reaches a given point at time 1 s or 10 s,
- how fast it moves along the curve at a given moment,
- whether it ever stops or reverses direction (in other examples).

That information lives in the full functions $$x(t), y(t)$$.

## Mini recap

- The **law of motion** specifies position as a function of time:

$$
\\vec{r}(t) = x(t)\\,\\hat{i} + y(t)\\,\\hat{j}.
$$

- The **trajectory** is the set of points visited in space; you can sometimes find it by eliminating $$t$$.
- Eliminating time gives geometry but typically loses timing, speed, and direction information.
- Different time dependences can produce the same trajectory.

<!-- SOURCE: lecture/kinematics/04_average_and_instantaneous_velocity.md -->

# Average And Instantaneous Velocity

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/kinematics/05_average_and_instantaneous_acceleration.md -->

# Average And Instantaneous Acceleration

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/kinematics/06_uniform_motion.md -->

# Uniform Motion

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/kinematics/07_uniformly_accelerated_motion.md -->

# Uniformly Accelerated Motion

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/kinematics/08_free_fall_as_constant_acceleration.md -->

# Free Fall As Constant Acceleration

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/kinematics/09_piecewise_defined_motion.md -->

# Piecewise Defined Motion

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/kinematics/10_motion_from_given_x_of_t.md -->

# Motion From Given X Of T

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/kinematics/11_motion_from_given_v_of_t.md -->

# Motion From Given V Of T

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/kinematics/12_motion_from_given_a_of_t.md -->

# Motion From Given A Of T

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/kinematics/13_inverse_kinematics_problems.md -->

# Inverse Kinematics Problems

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/kinematics/14_graphical_interpretation_x_v_a.md -->

# Graphical Interpretation X V A

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/kinematics/15_relative_motion_intro.md -->

# Relative Motion Intro

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/kinematics/16_2d_motion_and_components.md -->

# 2D Motion And Components

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/kinematics/17_projectile_motion.md -->

# Projectile Motion

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/kinematics/18_uniform_circular_motion.md -->

# Uniform Circular Motion

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/kinematics/19_tangential_and_normal_acceleration.md -->

# Tangential And Normal Acceleration

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/kinematics/20_periodic_motion_intro.md -->

# Periodic Motion Intro

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/kinematics/21_sinusoidal_motion.md -->

# Sinusoidal Motion

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/kinematics/22_kinematics_summary.md -->

# Kinematics Summary

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/kinematics/23_kinematics_problem_set.md -->

# Kinematics Problem Set

## Purpose

TODO

## Warm-up problems

1. TODO

## Standard problems

1. TODO

## Multi-step problems

1. TODO

## Conceptual questions

1. TODO

## Challenge problems

1. TODO

<!-- SOURCE: lecture/dynamics/01_why_kinematics_is_not_enough.md -->

# Why Kinematics Is Not Enough

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/dynamics/02_concept_of_force.md -->

# Concept Of Force

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/dynamics/03_interactions_and_models.md -->

# Interactions And Models

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/dynamics/04_newtons_first_law.md -->

# Newtons First Law

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/dynamics/05_inertial_frames.md -->

# Inertial Frames

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/dynamics/06_newtons_second_law.md -->

# Newtons Second Law

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/dynamics/07_equation_of_motion.md -->

# Equation Of Motion

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/dynamics/08_newtons_third_law.md -->

# Newtons Third Law

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/dynamics/09_weight_and_gravitational_force.md -->

# Weight And Gravitational Force

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/dynamics/10_normal_force.md -->

# Normal Force

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/dynamics/11_tension_force.md -->

# Tension Force

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/dynamics/12_friction_static_and_kinetic.md -->

# Friction Static And Kinetic

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/dynamics/13_spring_force_hookes_law.md -->

# Spring Force Hookes Law

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/dynamics/14_free_body_diagrams.md -->

# Free Body Diagrams

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/dynamics/15_resolving_forces_into_components.md -->

# Resolving Forces Into Components

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/dynamics/16_particle_on_horizontal_surface.md -->

# Particle On Horizontal Surface

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/dynamics/17_particle_on_inclined_plane.md -->

# Particle On Inclined Plane

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/dynamics/18_connected_bodies_and_tension.md -->

# Connected Bodies And Tension

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/dynamics/19_circular_motion_and_centripetal_force.md -->

# Circular Motion And Centripetal Force

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/dynamics/20_dynamics_with_given_force_law.md -->

# Dynamics With Given Force Law

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/dynamics/21_from_force_to_acceleration_to_motion.md -->

# From Force To Acceleration To Motion

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/dynamics/22_dynamics_summary.md -->

# Dynamics Summary

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/dynamics/23_dynamics_problem_set.md -->

# Dynamics Problem Set

## Purpose

TODO

## Warm-up problems

1. TODO

## Standard problems

1. TODO

## Multi-step problems

1. TODO

## Conceptual questions

1. TODO

## Challenge problems

1. TODO

<!-- SOURCE: lecture/combined/01_kinematics_to_dynamics_bridge.md -->

# Kinematics To Dynamics Bridge

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/combined/02_comparative_summary.md -->

# Comparative Summary

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO

<!-- SOURCE: lecture/combined/03_final_review.md -->

# Final Review

## Learning goals

- TODO

## Why this matters

TODO

## Core idea

TODO

## Mathematical formulation

TODO

## Interpretation

TODO

## Typical examples

TODO

## Common mistakes

- TODO

## Worked example

TODO

## Mini recap

- TODO
