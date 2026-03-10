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

$x(t)$

Velocity and acceleration are defined as time-derivatives:

$$
v(t) = \frac{dx}{dt}, \qquad a(t) = \frac{dv}{dt} = \frac{d^2x}{dt^2}
$$

The derivative here has a physical meaning:

- $v(t)$ is the **instantaneous rate of change** of position (how fast and in which direction the position coordinate is changing).
- $a(t)$ is the **instantaneous rate of change** of velocity (how quickly the velocity changes in time).

In dynamics, the central idea (developed later) is that interactions determine acceleration. In Newtonian particle mechanics, this is expressed by:

$$
\sum \vec{F} = m\vec{a}
$$

This equation is not “a definition of force.” It is a modeling principle: once you choose your force models, you have an equation that determines the acceleration, and then (using kinematics) the motion.

## Interpretation

- Kinematics can tell you **how** something moves (and reconstruct missing information from derivatives/integrals).
- Dynamics aims to tell you **what interaction models are consistent** with observed motion, or to **predict motion** under specified interactions.

You should get in the habit of asking two different questions:

1. **Description question (kinematics):** “Given $x(t)$ (or data), what are $v(t)$ and $a(t)$? What does the motion look like?”
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

$x(t) = 1 + 2t - t^2$

1) Compute velocity and acceleration.

Differentiate:

$$
v(t) = \frac{dx}{dt} = 2 - 2t
$$

Differentiate again:

$$
a(t) = \frac{dv}{dt} = -2
$$

So the acceleration is constant and negative (in this coordinate choice).

2) What can kinematics tell you, and what can’t it tell you?

- Kinematics tells you there is a turning time when $v(t)=0$:

$$
2 - 2t = 0 \;\Rightarrow\; t = 1
$$

- It tells you the motion is initially in the positive direction (since $v(0)=2>0$), then reverses after $t=1$.

But kinematics alone does not tell you *which interaction* caused the constant acceleration. If you additionally know the mass is $m=0.50\,\text{kg}$ and you adopt Newton’s second law (dynamics), then the **net force** would be:

$F_{\text{net}} = ma = (0.50)(-2) = -1\,\text{N}$

That net force could arise from many physical situations (gravity component, a spring, a constant push, etc.). Identifying a realistic force model is part of dynamics.

## Mini recap

- Kinematics describes motion via $x(t)$ (or $\vec{r}(t)$) and its derivatives.
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

- in 1D: a single coordinate $x(t)$,
- in 2D/3D: a position vector $\vec{r}(t)$ or a set of coordinates such as $x(t), y(t)$.

The **physical object** is real; the **numbers** you assign to represent its position are part of your description, and they depend on your chosen frame.

## Mathematical formulation

### Position in 1D

Choose:

- an origin (where $x=0$),
- a positive direction (for example, “to the right is positive”).

Then the position of a particle is described by a function of time:

$x(t)$

### Position in 2D (planar motion)

Choose perpendicular axes (for example, east as $x$ and north as $y$). The particle’s position can be written as a vector:

$\vec{r}(t)$

or in components (Cartesian coordinates):

$\vec{r}(t) = x(t)\,\hat{i} + y(t)\,\hat{j}$

where $\hat{i}$ and $\hat{j}$ are unit vectors along the chosen axes.

### Displacement (change in position)

Displacement is the difference between two positions (vector difference in 2D/3D, scalar difference in 1D). In 1D:

$\Delta x = x(t_2) - x(t_1)$

In vector form:

$\Delta \vec{r} = \vec{r}(t_2) - \vec{r}(t_1)$

Displacement is not “distance traveled.” Distance accumulates along the path; displacement depends only on the start and end positions.

### Changing the origin (same physical point, different coordinate)

Suppose you shift your origin by a constant amount. In 1D, if the new origin is located at coordinate $x_0$ in the old system, then the new coordinate is:

$x'(t) = x(t) - x_0$

This changes the numbers you call “position,” but it does not change the physical location of the particle. Importantly, displacement is unchanged by this shift:

$$
\Delta x' = x'(t_2) - x'(t_1) = \big(x(t_2)-x_0\big) - \big(x(t_1)-x_0\big) = x(t_2) - x(t_1) = \Delta x
$$

## Interpretation

1) **Frame dependence is not a flaw.** It is expected. The purpose of choosing a frame is to describe motion conveniently.

2) **Coordinates are labels, not physical substances.** The particle does not “have” a negative position; negative simply means “on the negative side of the chosen origin.”

3) **The particle model is a choice.** When we write $x(t)$ or $\vec{r}(t)$, we assume the object’s size/rotation can be neglected for the question at hand. If the object’s orientation matters (e.g., a rolling wheel), a richer model is needed.

4) **Some quantities are less sensitive to origin choices.** Position changes if you move the origin, but displacement does not. Later, you will see that velocity and acceleration are also unaffected by shifting the origin by a constant amount.

## Typical examples

1) **1D motion along a hallway.** Choose the door as $x=0$ and “toward the window” as positive. A student walking back and forth can have $x(t)$ that increases, decreases, and changes sign.

2) **2D motion on a map.** Choose axes east/north and an origin at a landmark. A runner’s position is a pair $\big(x(t), y(t)\big)$, or a vector $\vec{r}(t)$.

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
- time $t$ measured in seconds.

At $t=0$ the bicycle is 20 m west of the stop sign. At $t=5\,\text{s}$ it is 30 m east of the stop sign.

### Step 1: Translate the words into coordinates

“20 m west” means the coordinate is negative:

$x(0) = -20\,\text{m}$

“30 m east” means the coordinate is positive:

$x(5) = +30\,\text{m}$

### Step 2: Compute displacement

$\Delta x = x(5) - x(0) = 30 - (-20) = 50\,\text{m}$

Interpretation: the bicycle’s net change in position is 50 m to the east (in this chosen coordinate sense).

### Step 3: (Preview) Compute average velocity over the interval

Average velocity in 1D is displacement divided by elapsed time:

$$
v_{\text{avg}} = \frac{\Delta x}{\Delta t} = \frac{50\,\text{m}}{5\,\text{s}} = 10\,\text{m/s}
$$

This is a *kinematic* statement about how position changed; it does not yet explain what caused the motion.

### Step 4: Change the origin and verify what changes

Now choose a new origin at a tree that is 10 m east of the stop sign. In the old coordinates, the tree is at:

$x_0 = +10\,\text{m}$

Define the new coordinate:

$x'(t) = x(t) - x_0$

Compute the bicycle’s positions in the new coordinates:

$x'(0) = x(0) - 10 = -20 - 10 = -30\,\text{m}$

$x'(5) = x(5) - 10 = 30 - 10 = 20\,\text{m}$

Compute displacement in the new coordinates:

$\Delta x' = x'(5) - x'(0) = 20 - (-30) = 50\,\text{m}$

The numerical positions changed (because the origin moved), but the displacement did not. This is exactly what you should expect: displacement compares two positions within the *same* frame, so shifting the origin by a constant cancels out.

## Mini recap

- A reference frame specifies an origin, axes (positive directions), and a clock.
- Position is frame-dependent: $x(t)$ in 1D, $\vec{r}(t)$ in 2D/3D.
- Displacement is the difference of positions:

$$
\Delta x = x(t_2)-x(t_1), \qquad \Delta\vec{r} = \vec{r}(t_2)-\vec{r}(t_1)
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

In 2D we commonly choose perpendicular axes with unit vectors $\hat{i}$ (x-direction) and $\hat{j}$ (y-direction). A general vector can be written as:

$\vec{A} = A_x\,\hat{i} + A_y\,\hat{j}$

The numbers $A_x$ and $A_y$ are the **components** of $\vec{A}$ in this coordinate system.

### Magnitude (length) of a vector

The magnitude of $\vec{A}$ is:

$$
|\vec{A}| = \sqrt{A_x^2 + A_y^2}
$$

This is just the Pythagorean theorem: components form a right triangle.

### Position vector and displacement vector

The position of a particle in the plane can be described by a position vector:

$\vec{r}(t) = x(t)\,\hat{i} + y(t)\,\hat{j}$

If the particle is at positions $\vec{r}(t_1)$ and $\vec{r}(t_2)$ at two times, the **displacement vector** is:

$\Delta\vec{r} = \vec{r}(t_2) - \vec{r}(t_1)$

In components:

$$
\Delta\vec{r} = \big(x(t_2)-x(t_1)\big)\,\hat{i} + \big(y(t_2)-y(t_1)\big)\,\hat{j}
$$

### Vector addition and subtraction (why components help)

If

$$
\vec{A} = A_x\,\hat{i} + A_y\,\hat{j}, \qquad \vec{B} = B_x\,\hat{i} + B_y\,\hat{j},
$$

then

$\vec{A} + \vec{B} = (A_x+B_x)\,\hat{i} + (A_y+B_y)\,\hat{j}.$

This is the practical reason we use components: many geometric vector rules reduce to ordinary arithmetic once axes are chosen.

### Why velocity, acceleration, and force are vectors

If position in 2D/3D is a vector function of time, then its time-derivatives are also vectors:

$$
\vec{v}(t) = \frac{d\vec{r}}{dt}, \qquad \vec{a}(t) = \frac{d\vec{v}}{dt} = \frac{d^2\vec{r}}{dt^2}.
$$

Forces model interactions that “push” or “pull” in a direction, so force is also a vector quantity:

$\vec{F}$

Later, dynamics connects force and acceleration in vector form.

## Interpretation

- A vector is not just a pair of numbers; it is a geometric quantity that **points**.
- Components depend on the chosen axes, but the **physical vector** does not. Rotating axes changes $A_x$ and $A_y$, but not the vector itself.
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

A particle moves in the plane. At time $t_1$ its position is

$\vec{r}(t_1) = (2\,\text{m})\,\hat{i} + (1\,\text{m})\,\hat{j}.$

At a later time $t_2$ its position is

$\vec{r}(t_2) = (8\,\text{m})\,\hat{i} + (5\,\text{m})\,\hat{j}.$

Assume $t_2 - t_1 = 3\,\text{s}$.

### Step 1: Compute the displacement vector

$\Delta\vec{r} = \vec{r}(t_2) - \vec{r}(t_1)$

Subtract components:

$$
\Delta\vec{r} = (8-2)\,\text{m}\,\hat{i} + (5-1)\,\text{m}\,\hat{j} = (6\,\text{m})\,\hat{i} + (4\,\text{m})\,\hat{j}.
$$

Interpretation: the net change in position is 6 m in the +x direction and 4 m in the +y direction.

### Step 2: Compute the magnitude of the displacement

$$
|\Delta\vec{r}| = \sqrt{(6\,\text{m})^2 + (4\,\text{m})^2} = \sqrt{36+16}\,\text{m} = \sqrt{52}\,\text{m}.
$$

Numerically:

$$
|\Delta\vec{r}| \approx 7.21\,\text{m}.
$$

### Step 3: Find the direction (angle) of the displacement

Let $\theta$ be the angle measured from the +x axis toward the +y axis. Then:

$$
\tan\theta = \frac{\Delta y}{\Delta x} = \frac{4}{6} = \frac{2}{3}.
$$

So

$$
\theta = \arctan\left(\frac{2}{3}\right) \approx 33.7^{\circ}.
$$

### Step 4: Compute the average velocity vector over the interval

Average velocity is displacement divided by elapsed time:

$$
\vec{v}_{\text{avg}} = \frac{\Delta\vec{r}}{\Delta t} = \frac{(6\,\text{m})\,\hat{i} + (4\,\text{m})\,\hat{j}}{3\,\text{s}}.
$$

So:

$$
\vec{v}_{\text{avg}} = (2\,\text{m/s})\,\hat{i} + \left(\frac{4}{3}\,\text{m/s}\right)\,\hat{j}.
$$

Notice how the vector form keeps the direction information automatically.

## Mini recap

- Scalars have magnitude only; vectors have magnitude and direction.
- In Cartesian coordinates:

$$
\vec{A} = A_x\,\hat{i} + A_y\,\hat{j}, \qquad |\vec{A}| = \sqrt{A_x^2 + A_y^2}.
$$

- Position and displacement:

$$
\vec{r}(t) = x(t)\,\hat{i} + y(t)\,\hat{j}, \qquad \Delta\vec{r} = \vec{r}(t_2) - \vec{r}(t_1).
$$

- Velocity and acceleration are vector time-derivatives of position.
- Component methods turn vector algebra into ordinary arithmetic, but you must keep track of axes and units.

<!-- SOURCE: lecture/kinematics/03_trajectory_and_position_function.md -->

# Trajectory and position function

## Learning goals

- Distinguish the **trajectory** (geometric path in space) from the **law of motion** (position as a function of time).
- Describe planar motion using a position vector $\vec{r}(t)$ or component functions $x(t), y(t)$.
- Eliminate time (when appropriate) to obtain an equation for the trajectory, and understand what information is lost.
- Recognize that different time dependences can produce the **same trajectory**.

## Why this matters

Students often say “the trajectory is $x(t)$” or think that a curve like a parabola fully determines the motion. But a curve in space only tells you **where** the particle can be; it does not tell you **when** the particle is at each point, how fast it moves along the curve, or in which direction it is traversed.

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

$\vec{r}(t) = x(t)\,\hat{i} + y(t)\,\hat{j}$

Equivalently, you can specify the pair of component functions:

$x(t), \qquad y(t).$

This is the **law of motion**: it tells you where the particle is at each time.

### Trajectory as a geometric set

The **trajectory** is the set of points in the plane that the particle occupies at some time:

$\{(x(t), y(t)) \;\text{for all relevant } t\}.$

Often (but not always) you can eliminate $t$ between $x(t)$ and $y(t)$ to get a relation between $x$ and $y$:

$F(x,y) = 0.$

That relation describes a curve in space: the trajectory (or a part of it).

### What you lose when you eliminate time

If you eliminate $t$ and obtain a curve equation, you typically lose:

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

- Treating a curve equation like $y = f(x)$ as “the full motion” (it is only geometry, not timing).
- Confusing the **path length** (distance traveled along the curve) with displacement.
- Assuming that if two motions have the same trajectory, then they have the same velocity/acceleration at corresponding points (not true without timing information).
- Eliminating time incorrectly (for example, dividing by an expression that could be zero without checking).
- Forgetting that a single point on the trajectory may correspond to multiple times (especially in periodic motion).

## Worked example

Consider the planar motion defined by:

$x(t) = 2t, \qquad y(t) = t^2,$

for $t \ge 0$.

### Step 1: Identify what the law of motion tells you

At each time $t$, the position is:

$\vec{r}(t) = (2t)\,\hat{i} + (t^2)\,\hat{j}.$

This already answers questions like “Where is the particle at $t=3\,\text{s}$?”:

$x(3)=6, \qquad y(3)=9.$

### Step 2: Find the trajectory by eliminating time

From $x(t)=2t$ we solve for $t$:

$$
t = \frac{x}{2}.
$$

Substitute into $y(t)=t^2$:

$$
y = \left(\frac{x}{2}\right)^2 = \frac{x^2}{4}.
$$

So the trajectory is the parabola:

$$
y = \frac{x^2}{4}, \qquad x \ge 0.
$$

This describes the *shape* of the path in the plane.

### Step 3: Show that the same trajectory can come from a different time dependence

Define a new motion:

$\tilde{x}(t) = 2t^2, \qquad \tilde{y}(t) = t^4,$

for $t \ge 0$.

Eliminate time again. From $\tilde{x}(t)=2t^2$:

$$
t^2 = \frac{\tilde{x}}{2}.
$$

Then

$$
\tilde{y} = t^4 = \left(t^2\right)^2 = \left(\frac{\tilde{x}}{2}\right)^2 = \frac{\tilde{x}^2}{4}.
$$

So the **trajectory is the same parabola**, but the timing is different: the second motion moves along the curve more slowly near the origin (because $\tilde{x}(t)$ grows like $t^2$, not like $t$).

### Step 4: What did the curve equation fail to tell you?

The curve

$$
y = \frac{x^2}{4}
$$

does not tell you:

- whether the particle reaches a given point at time 1 s or 10 s,
- how fast it moves along the curve at a given moment,
- whether it ever stops or reverses direction (in other examples).

That information lives in the full functions $x(t), y(t)$.

## Mini recap

- The **law of motion** specifies position as a function of time:

$\vec{r}(t) = x(t)\,\hat{i} + y(t)\,\hat{j}.$

- The **trajectory** is the set of points visited in space; you can sometimes find it by eliminating $t$.
- Eliminating time gives geometry but typically loses timing, speed, and direction information.
- Different time dependences can produce the same trajectory.

<!-- SOURCE: lecture/kinematics/04_average_and_instantaneous_velocity.md -->

# Average and instantaneous velocity

## Learning goals

- Compute **average velocity** from positions (1D and vector form).
- Understand instantaneous velocity as a **limit** and as the **derivative** of position.
- Interpret velocity graphically as the **slope** of the position–time graph.
- Distinguish **speed** from **velocity**, and interpret the sign of velocity in 1D.

## Why this matters

In everyday language “velocity” often means “how fast.” In mechanics, velocity is more precise: it tracks **rate of change of position** and therefore includes direction. Confusing velocity with speed leads to sign errors, incorrect interpretations of turning points, and misuse of formulas.

Velocity is also the first place where the meaning of a derivative becomes physically concrete: it is not just a calculus symbol; it is an operational idea connected to motion.

## Core idea

Over a time interval, you can ask:

- “How much did the position change overall?” → displacement.
- “How quickly did that change happen on average?” → average velocity.

But motion can vary within an interval. To describe the motion at a particular instant, you need:

- instantaneous velocity: the velocity “at time $t$,” which is the limit of average velocity over smaller and smaller time intervals.

## Mathematical formulation

### Average velocity (1D)

If the position in 1D is $x(t)$, then over the interval from $t_1$ to $t_2$:

$$
v_{\text{avg}} = \frac{\Delta x}{\Delta t} = \frac{x(t_2)-x(t_1)}{t_2-t_1}.
$$

This is a single number (with sign) describing the net rate of change over that interval.

### Average velocity (vector form)

In 2D/3D, position is a vector $\vec{r}(t)$. Average velocity is:

$$
\vec{v}_{\text{avg}} = \frac{\Delta\vec{r}}{\Delta t} = \frac{\vec{r}(t_2)-\vec{r}(t_1)}{t_2-t_1}.
$$

### Instantaneous velocity as a limit (definition)

Instantaneous velocity at time $t$ is the limit of average velocity as the time interval shrinks to zero:

$$
v(t) = \lim_{\Delta t\to 0} \frac{x(t+\Delta t)-x(t)}{\Delta t}.
$$

This is exactly the derivative of $x(t)$:

$$
v(t) = \frac{dx}{dt}.
$$

In vector form:

$$
\vec{v}(t) = \frac{d\vec{r}}{dt}.
$$

### Graphical meaning (slope)

On a graph of $x$ versus $t$:

- the average velocity over $[t_1,t_2]$ is the **slope of the secant line** connecting the two points,
- the instantaneous velocity at $t$ is the **slope of the tangent line** at that point.

So:

- steep upward slope → large positive velocity,
- flat tangent → zero velocity,
- downward slope → negative velocity.

### Speed vs velocity

In 1D:

$\text{speed} = |v(t)|.$

In 2D/3D:

$\text{speed} = |\vec{v}(t)|.$

Speed is always nonnegative; velocity can be negative in 1D or point in different directions in 2D/3D.

## Interpretation

- **Sign matters in 1D.** A negative velocity does not mean “going backwards” in any absolute sense; it means moving in the negative direction of your chosen axis.
- **Zero velocity can occur even when the particle has moved.** For example, at a turning point (motion reverses direction), the instantaneous velocity can be zero at that instant.
- **Average velocity can be zero even when there was motion.** If a particle returns to its starting point, displacement is zero, so average velocity over the full interval is zero—even though it traveled a positive distance.

## Typical examples

1) **Return trip:** Walk 50 m east, then 50 m west back to the start. Over the whole trip:

- displacement is zero,
- average velocity is zero,
- but the distance traveled is 100 m and the average speed is not zero.

2) **Turning point:** A particle moves right, slows down, stops momentarily, then moves left. The instantaneous velocity passes through zero at the turning time.

3) **2D motion:** A particle can have constant speed but changing velocity (direction change). This will matter for circular motion later.

## Common mistakes

- Mixing up **distance traveled** with **displacement** when computing average velocity.
- Saying “velocity is negative so the particle is slowing down.” Negative means direction, not necessarily slowing.
- Treating “average velocity” as if it were the velocity at the midpoint of the interval (not generally true).
- Forgetting units: velocity has units of length/time (e.g., m/s).
- Confusing speed and velocity (dropping sign/direction information).

## Worked example

A particle moves along a line with position:

$x(t) = 4t - t^2$

where $x$ is in meters and $t$ is in seconds.

### Step 1: Compute average velocity on a time interval

Find the average velocity from $t_1=1\,\text{s}$ to $t_2=3\,\text{s}$.

Compute positions:

$x(1) = 4(1) - 1^2 = 3\,\text{m},$

$x(3) = 4(3) - 3^2 = 12 - 9 = 3\,\text{m}.$

So displacement is zero:

$\Delta x = x(3)-x(1) = 0.$

Therefore:

$$
v_{\text{avg}} = \frac{\Delta x}{\Delta t} = \frac{0}{3-1} = 0\,\text{m/s}.
$$

Interpretation: over this whole interval the particle ends where it started, so its net rate of change of position is zero.

### Step 2: Compute instantaneous velocity

Differentiate:

$$
v(t) = \frac{dx}{dt} = 4 - 2t.
$$

At $t=1\,\text{s}$:

$v(1) = 4 - 2 = 2\,\text{m/s}.$

At $t=3\,\text{s}$:

$v(3) = 4 - 6 = -2\,\text{m/s}.$

So the particle is moving in the positive direction at $t=1$ and in the negative direction at $t=3$.

### Step 3: Find the turning time (where velocity is zero)

Set $v(t)=0$:

$$
4 - 2t = 0 \;\Rightarrow\; t = 2\,\text{s}.
$$

At $t=2\,\text{s}$, the particle’s velocity is zero: it is the instant when the motion reverses direction.

## Mini recap

- Average velocity:

$$
v_{\text{avg}} = \frac{x(t_2)-x(t_1)}{t_2-t_1}, \qquad \vec{v}_{\text{avg}} = \frac{\vec{r}(t_2)-\vec{r}(t_1)}{t_2-t_1}.
$$

- Instantaneous velocity is the derivative:

$$
v(t) = \frac{dx}{dt}, \qquad \vec{v}(t) = \frac{d\vec{r}}{dt}.
$$

- Graphically: velocity is the slope of the $x(t)$ graph (secant for average, tangent for instantaneous).
- Speed is magnitude: $|v|$ or $|\vec{v}|$; velocity includes sign/direction.

<!-- SOURCE: lecture/kinematics/05_average_and_instantaneous_acceleration.md -->

# Average and instantaneous acceleration

## Learning goals

- Compute **average acceleration** from velocity change (1D and vector form).
- Define instantaneous acceleration as a **limit** and as the **derivative** of velocity.
- Connect acceleration to the **second derivative** of position.
- Understand that acceleration can come from changing **speed** *or* changing **direction**.

## Why this matters

“Acceleration” is often misheard as “speeding up.” In mechanics, acceleration is broader: it measures how velocity changes, and velocity includes direction. This is why an object moving at constant speed around a circle is still accelerating.

Acceleration is also the key bridge quantity:

- kinematics describes motion using $x(t), v(t), a(t)$,
- dynamics later determines $\vec{a}(t)$ from forces.

So you want a clear definition and reliable interpretation now.

## Core idea

Velocity can change in two ways:

1) **Magnitude change:** speed increases or decreases (speeding up / slowing down).
2) **Direction change:** even if speed stays constant, a change in direction means the velocity vector changes.

Acceleration captures both, because it measures change in velocity.

## Mathematical formulation

### Average acceleration (1D)

If velocity in 1D is $v(t)$, then over $[t_1,t_2]$:

$$
a_{\text{avg}} = \frac{\Delta v}{\Delta t} = \frac{v(t_2)-v(t_1)}{t_2-t_1}.
$$

### Average acceleration (vector form)

In 2D/3D:

$$
\vec{a}_{\text{avg}} = \frac{\Delta\vec{v}}{\Delta t} = \frac{\vec{v}(t_2)-\vec{v}(t_1)}{t_2-t_1}.
$$

### Instantaneous acceleration (definition)

Instantaneous acceleration is the limit as the time interval shrinks:

$$
a(t) = \lim_{\Delta t\to 0} \frac{v(t+\Delta t)-v(t)}{\Delta t} = \frac{dv}{dt}.
$$

Vector form:

$$
\vec{a}(t) = \frac{d\vec{v}}{dt}.
$$

### Relation to position

Since in 1D

$$
v(t) = \frac{dx}{dt},
$$

we get

$$
a(t) = \frac{dv}{dt} = \frac{d^2x}{dt^2}.
$$

In vector form:

$$
\vec{a}(t) = \frac{d^2\vec{r}}{dt^2}.
$$

### Graphical meaning

- On a graph of $v$ versus $t$, acceleration is the slope:
  - average acceleration → slope of the secant line,
  - instantaneous acceleration → slope of the tangent line.

This is the velocity-graph analog of the “velocity is slope of the position graph” idea.

## Interpretation

### Sign and “speeding up” in 1D

In 1D, acceleration and velocity are signed. Whether the particle is speeding up depends on the *combination* of signs:

- If $v(t)$ and $a(t)$ have the **same sign**, speed increases.
- If $v(t)$ and $a(t)$ have **opposite signs**, speed decreases.

This is worth practicing, because it prevents the common mistake “negative acceleration means slowing down.” Negative acceleration only means “acceleration points in the negative axis direction.”

### Direction change without speed change (vector idea)

In 2D/3D, a velocity vector can change even if its magnitude stays the same. If speed is constant but direction rotates, then $\vec{v}(t)$ changes and $\vec{a}(t)$ is nonzero.

You will see this explicitly in circular motion later, where acceleration points inward even at constant speed.

## Typical examples

1) **Car braking while moving forward (1D):** velocity is positive, acceleration is negative. The car slows down.

2) **Car accelerating in reverse (1D):** velocity is negative, acceleration is negative. The car speeds up (in the negative direction).

3) **Uniform circular motion (preview):** speed constant, direction changing → acceleration nonzero.

## Common mistakes

- Thinking “acceleration = change in speed” instead of “change in velocity.”
- Saying “negative acceleration means slowing down” without checking the sign of velocity.
- Confusing average acceleration with instantaneous acceleration (they can differ if acceleration varies in time).
- Treating “acceleration is zero” as “velocity is zero.” Zero acceleration can mean constant nonzero velocity.
- Forgetting units: acceleration has units of length/time² (e.g., m/s²).

## Worked example

A particle moves in 1D with velocity:

$v(t) = 6 - 3t$

with $v$ in m/s and $t$ in s.

### Step 1: Find the acceleration

Differentiate:

$$
a(t) = \frac{dv}{dt} = -3.
$$

So acceleration is constant:

$a(t) = -3\,\text{m/s}^2.$

### Step 2: Interpret the sign physically

At $t=0$:

$v(0)=6\,\text{m/s} > 0,$

so the particle initially moves in the positive direction. Since $a=-3<0$, the acceleration points in the negative direction, opposite to the motion, so the particle initially **slows down**.

### Step 3: Find when it stops (turning time in velocity)

Set $v(t)=0$:

$$
6 - 3t = 0 \;\Rightarrow\; t = 2\,\text{s}.
$$

At $t=2\,\text{s}$ the instantaneous velocity is zero.

### Step 4: What happens after the stop?

For $t>2$:

$v(t) = 6 - 3t < 0,$

so the particle moves in the negative direction. Acceleration is still negative, so now velocity and acceleration have the same sign: the particle **speeds up** (in the negative direction).

### Step 5: Compute an average acceleration check

Compute average acceleration from $t_1=0$ to $t_2=4$:

$v(0)=6, \qquad v(4)=6-12=-6.$

$$
a_{\text{avg}} = \frac{v(4)-v(0)}{4-0} = \frac{-6-6}{4} = -3\,\text{m/s}^2,
$$

matching the constant instantaneous acceleration.

## Mini recap

- Average acceleration:

$$
a_{\text{avg}} = \frac{v(t_2)-v(t_1)}{t_2-t_1}, \qquad \vec{a}_{\text{avg}} = \frac{\vec{v}(t_2)-\vec{v}(t_1)}{t_2-t_1}.
$$

- Instantaneous acceleration:

$$
a(t) = \frac{dv}{dt}, \qquad \vec{a}(t) = \frac{d\vec{v}}{dt}.
$$

- Relation to position:

$$
a(t) = \frac{d^2x}{dt^2}, \qquad \vec{a}(t) = \frac{d^2\vec{r}}{dt^2}.
$$

- Acceleration describes change in velocity: it can arise from changing speed or changing direction.

<!-- SOURCE: lecture/kinematics/06_uniform_motion.md -->

# Uniform motion (constant velocity)

## Learning goals

- Recognize uniform motion as motion with **constant velocity** and **zero acceleration**.
- Use the uniform-motion model to relate position and time in 1D and vector form.
- Interpret uniform motion on $x(t)$ and $v(t)$ graphs.
- Solve basic “meet/catch-up” and “when/where” problems with sign conventions.

## Why this matters

Uniform motion is the simplest nontrivial motion model:

- it is realistic over short time intervals (cruising car, conveyor belt),
- it is the baseline for interpreting graphs and signs,
- it becomes the “no net effect” case later in dynamics (Newton’s first law will tell you when constant velocity occurs).

Even here, most mistakes come not from algebra but from unclear definitions (position vs distance, sign conventions, and mixing frames).

## Core idea

If velocity is constant, then the particle covers equal displacements in equal time intervals. In 1D, “constant velocity” means:

- the position changes linearly with time,
- the direction of motion does not change (no turning point),
- acceleration is zero.

Uniform motion is a **model**: it describes situations where changes in velocity are small enough to neglect.

## Mathematical formulation

### 1D uniform motion

Assume constant velocity:

$v(t) = v_0 \quad \text{(constant)}.$

Then position is:

$x(t) = x_0 + v_0(t-t_0).$

Often we choose $t_0=0$ for convenience:

$x(t) = x_0 + v_0 t.$

Acceleration is the derivative of velocity:

$$
a(t) = \frac{dv}{dt} = 0.
$$

### Vector form (2D/3D)

If velocity is a constant vector $\vec{v}_0$, then:

$\vec{r}(t) = \vec{r}_0 + \vec{v}_0(t-t_0).$

This describes straight-line motion at constant speed in a fixed direction.

### Graphical signatures

For uniform motion in 1D:

- $x(t)$ is a straight line; its slope is $v_0$.
- $v(t)$ is a horizontal line at $v_0$.
- $a(t)$ is identically zero.

## Interpretation

- The sign of $v_0$ tells you direction along your chosen axis.
  - $v_0>0$: motion in the positive direction.
  - $v_0<0$: motion in the negative direction.
- The magnitude $|v_0|$ is the constant speed (in 1D).
- The same physical motion can have different coordinate descriptions if you shift the origin, but the constant velocity value does not change under an origin shift.

## Typical examples

1) **Cruising car (1D approximation):** A car moves at approximately constant speed on a straight highway segment. Over that segment, uniform motion is a good model.

2) **Moving walkway:** If you walk at constant speed relative to the walkway, and the walkway moves at constant speed relative to the ground, then your ground velocity is constant too (uniform motion), found by adding velocities (developed later).

3) **Two trains on parallel tracks:** Catch-up problems are uniform-motion problems when both trains maintain constant velocities.

## Common mistakes

- Using distance traveled in place of displacement when computing $x(t)$.
- Forgetting sign conventions: writing $x(t)=x_0+|v_0|t$ even when motion is in the negative direction.
- Mixing time origins: using $x_0$ measured at one time while using a formula with a different $t_0$.
- Assuming that “constant speed” automatically means “uniform motion” in 2D/3D. Constant speed with changing direction is **not** uniform motion because velocity is not constant.

## Worked example

Two cyclists move along a straight road (1D). Choose the x-axis along the road, with positive direction to the east.

- Cyclist A starts at the origin at $t=0$ and rides east at constant velocity $v_A = 6\,\text{m/s}$.
- Cyclist B starts 120 m east of the origin at $t=0$ and rides west at constant velocity $v_B = -4\,\text{m/s}$.

Find when and where they meet.

### Step 1: Write position functions

For cyclist A:

$x_A(t) = 0 + (6)t = 6t.$

For cyclist B:

$x_B(t) = 120 + (-4)t = 120 - 4t.$

### Step 2: Solve the meeting condition

They meet when positions are equal:

$x_A(t) = x_B(t).$

So:

$6t = 120 - 4t.$

$$
10t = 120 \;\Rightarrow\; t = 12\,\text{s}.
$$

### Step 3: Find the meeting position

Substitute back:

$x = x_A(12) = 6(12) = 72\,\text{m}.$

Interpretation: they meet 72 m east of the origin, 12 s after $t=0$.

### Step 4: Quick reasonableness check

The closing speed is:

$v_{\text{close}} = v_A - v_B = 6 - (-4) = 10\,\text{m/s}.$

Initial separation is 120 m, so meeting time should be:

$$
t = \frac{120}{10} = 12\,\text{s},
$$

consistent.

## Mini recap

- Uniform motion means **constant velocity** and **zero acceleration**.
- In 1D:

$x(t) = x_0 + v_0(t-t_0), \qquad v(t)=v_0, \qquad a(t)=0.$

- On graphs: $x(t)$ is linear; $v(t)$ is constant; $a(t)=0$.
- Keep sign conventions explicit; displacement (not distance) controls the position function.

<!-- SOURCE: lecture/kinematics/07_uniformly_accelerated_motion.md -->

# Uniformly accelerated motion (constant acceleration)

## Learning goals

- Recognize when the **constant-acceleration model** is appropriate and state its assumptions.
- Derive and use the standard relations for $v(t)$ and $x(t)$ under constant $a$.
- Use initial conditions correctly and interpret the meaning of $x_0$ and $v_0$.
- Solve basic constant-acceleration problems without “formula hunting,” and check results by units/signs.

## Why this matters

Constant acceleration is the next simplest model after uniform motion. It appears everywhere:

- near-Earth free fall (approximately constant $g$, neglecting air resistance),
- vehicles speeding up or braking at roughly steady rate,
- motion segments that can be approximated as having constant acceleration.

Many students memorize “the kinematic equations” without understanding where they come from. That leads to sign errors and applying them when the assumptions are not satisfied. Here we will derive them from the definitions of velocity and acceleration.

## Core idea

If acceleration is constant, then velocity changes at a constant rate, and position is a quadratic function of time.

The model is a statement about time dependence:

$a(t) = a_0 \quad \text{(constant)}.$

From this one assumption, the entire motion follows once you specify initial conditions.

## Mathematical formulation

### Assumptions (say them explicitly when you use the model)

We assume:

1. Motion is along a straight line (1D) or we are analyzing one component.
2. Acceleration is constant in time over the interval of interest:

$a(t) = a_0.$

3. The quantities $x_0$ and $v_0$ are the position and velocity at a chosen reference time $t_0$.

### Step 1: Derive velocity as a function of time

By definition:

$$
a(t) = \frac{dv}{dt}.
$$

If $a(t)=a_0$ is constant, then:

$$
\frac{dv}{dt} = a_0.
$$

Integrate from $t_0$ to $t$:

$$
\int_{v(t_0)}^{v(t)} dv = \int_{t_0}^{t} a_0\,dt.
$$

This gives:

$v(t) - v(t_0) = a_0(t-t_0).$

Define $v_0 = v(t_0)$, so:

$v(t) = v_0 + a_0(t-t_0).$

If we choose $t_0=0$:

$v(t) = v_0 + a_0 t.$

### Step 2: Derive position as a function of time

Velocity is the derivative of position:

$$
v(t) = \frac{dx}{dt}.
$$

Using $v(t)=v_0+a_0(t-t_0)$:

$$
\frac{dx}{dt} = v_0 + a_0(t-t_0).
$$

Integrate from $t_0$ to $t$:

$$
\int_{x(t_0)}^{x(t)} dx = \int_{t_0}^{t} \left(v_0 + a_0(\tau-t_0)\right)d\tau.
$$

Compute the integral:

$$
x(t) - x(t_0) = v_0(t-t_0) + \frac{1}{2}a_0(t-t_0)^2.
$$

Define $x_0 = x(t_0)$:

$$
x(t) = x_0 + v_0(t-t_0) + \frac{1}{2}a_0(t-t_0)^2.
$$

If $t_0=0$:

$$
x(t) = x_0 + v_0 t + \frac{1}{2}a_0 t^2.
$$

### A useful relation without time (optional but common)

Sometimes you want a relation between velocity and position when acceleration is constant. Start from:

$v(t) = v_0 + a_0(t-t_0),$

and

$$
x(t) - x_0 = v_0(t-t_0) + \frac{1}{2}a_0(t-t_0)^2.
$$

Eliminate $t-t_0$. Let $\Delta t = t-t_0$. Then:

$$
v - v_0 = a_0\Delta t \quad \Rightarrow\quad \Delta t = \frac{v-v_0}{a_0}.
$$

Substitute into the position equation:

$$
x - x_0 = v_0\left(\frac{v-v_0}{a_0}\right) + \frac{1}{2}a_0\left(\frac{v-v_0}{a_0}\right)^2.
$$

After simplification, you obtain:

$v^2 = v_0^2 + 2a_0(x-x_0).$

This relation is powerful, but it is still based on the same constant-acceleration assumption.

## Interpretation

- Constant acceleration means **velocity changes linearly** in time.
- Position is a quadratic in time; its graph is a parabola in the $x$–$t$ plane.
- Initial conditions matter:
  - $x_0$ is where the particle is at the chosen reference time.
  - $v_0$ is the velocity at that same time.
  - changing the choice of $t_0$ changes the numerical values of $x_0$ and $v_0$, but not the physical motion.

## Typical examples

1) **Braking car (1D):** If deceleration is approximately constant, you can predict stopping time and stopping distance.

2) **Free fall preview:** Over not-too-large height changes near Earth, acceleration is approximately constant and equal to $\pm g$ depending on your sign convention.

3) **Piecewise motion preview:** Real motion is often “constant acceleration for a while, then different constant acceleration,” which we will treat later as piecewise-defined motion.

## Common mistakes

- Using constant-acceleration formulas when acceleration is not constant (e.g., strong air resistance, changing engine force).
- Forgetting that the sign of $a_0$ depends on the chosen axis direction.
- Plugging numbers into a memorized equation without stating $x_0, v_0, t_0$ (mixing different reference times).
- Using $v^2 = v_0^2 + 2a_0(x-x_0)$ and then forgetting that squaring hides sign information: $v$ can be positive or negative depending on direction.
- Confusing “acceleration is constant” with “velocity is constant.” Constant acceleration generally means velocity is changing.

## Worked example

A train moves along a straight track. At $t=0$, it passes a marker with:

$x_0 = 0, \qquad v_0 = 12\,\text{m/s}.$

It then accelerates uniformly with:

$a_0 = 0.80\,\text{m/s}^2$

for 15 s.

1) Find its velocity and position at $t=15\,\text{s}$.  
2) How far does it travel during the *last* 5 s of this interval?

### Step 1: Velocity after 15 s

Use:

$v(t) = v_0 + a_0 t.$

So:

$v(15) = 12 + (0.80)(15) = 12 + 12 = 24\,\text{m/s}.$

### Step 2: Position after 15 s

Use:

$$
x(t) = x_0 + v_0 t + \frac{1}{2}a_0 t^2.
$$

So:

$$
x(15) = 0 + (12)(15) + \frac{1}{2}(0.80)(15)^2.
$$

Compute:

$(12)(15)=180,$

$$
\frac{1}{2}(0.80)(15)^2 = 0.40\cdot 225 = 90.
$$

Therefore:

$x(15) = 180 + 90 = 270\,\text{m}.$

### Step 3: Distance traveled in the last 5 seconds

The last 5 s is the interval from $t=10$ to $t=15$.

Compute:

$$
x(10) = (12)(10) + \frac{1}{2}(0.80)(10)^2 = 120 + 0.40\cdot 100 = 120 + 40 = 160\,\text{m}.
$$

Then:

$\Delta x = x(15)-x(10) = 270 - 160 = 110\,\text{m}.$

### Step 4: Quick checks

- Units: each term in $x(t)$ has units of meters.
- Reasonableness: the average velocity over the 15 s is roughly halfway between 12 and 24 m/s, i.e. about 18 m/s, so distance should be about $18\cdot 15 = 270$ m, matching.

## Mini recap

- Constant acceleration model:

$a(t)=a_0.$

- Derived relations (with reference time $t_0$):

$v(t) = v_0 + a_0(t-t_0),$

$$
x(t) = x_0 + v_0(t-t_0) + \frac{1}{2}a_0(t-t_0)^2.
$$

- Time-free relation (still constant-acceleration only):

$v^2 = v_0^2 + 2a_0(x-x_0).$

- State assumptions and sign conventions; use initial conditions consistently.

<!-- SOURCE: lecture/kinematics/08_free_fall_as_constant_acceleration.md -->

# Free fall as constant acceleration

## Learning goals

- State what “free fall” means in the idealized model and when it is a good approximation.
- Apply constant-acceleration kinematics to vertical motion with a clear **sign convention**.
- Solve both “dropped from rest” and “thrown upward” problems without sign confusion.
- Identify common sign/interpretation mistakes (especially at the top of the motion).

## Why this matters

Free fall is one of the most important constant-acceleration applications. It is also where sign mistakes are most common, because “up/down” intuition can conflict with algebra.

Learning to handle free fall cleanly builds a skill you will use throughout mechanics:

- choose a coordinate axis and stick with it,
- write $a$ with the correct sign,
- interpret results physically (especially velocity sign and turning points).

## Core idea

In the ideal free-fall model near Earth:

- the only significant influence is gravity,
- the acceleration has (approximately) constant magnitude $g$,
- and it points downward.

So the vertical motion can be modeled as 1D constant-acceleration motion.

This is a **model**, so it comes with assumptions:

- height changes are not so large that $g$ varies significantly,
- air resistance is neglected (or is small over the time interval),
- the object’s rotation/shape is not relevant (particle model).

## Mathematical formulation

### Choose a sign convention (two common choices)

You must choose an axis direction and keep it consistent.

**Choice A (often used): upward is positive.**  
Then the acceleration due to gravity is:

$a(t) = -g.$

**Choice B: downward is positive.**  
Then:

$a(t) = +g.$

Both are correct; the physics is the same. The algebra only works if you stay consistent.

In either case, once you have the correct sign for $a$, you can use the constant-acceleration relations from the previous section.

### Equations (using Choice A: upward positive)

Let $t_0=0$ for simplicity. With $a=-g$:

Velocity:

$v(t) = v_0 - gt.$

Position:

$$
x(t) = x_0 + v_0 t - \frac{1}{2}gt^2.
$$

Time-free relation:

$v^2 = v_0^2 - 2g(x-x_0).$

### Meaning of signs

- If $v>0$ (in Choice A), the object is moving upward.
- If $v<0$, it is moving downward.
- The acceleration is negative at all times in free fall (Choice A), even at the top, because gravity still points downward.

## Interpretation

### The “top of the motion” is not zero acceleration

When an object is thrown upward, there is an instant at the highest point where:

$v = 0.$

But acceleration is still:

$a = -g.$

Velocity can be zero at an instant without acceleration being zero. This is the key conceptual point that prevents a huge class of errors.

### Free fall vs “falling with air resistance”

With significant air resistance, acceleration is not constant: it changes with speed and can approach zero at terminal velocity. In that situation, the constant-acceleration equations are not valid; you need a different model (later, in dynamics).

## Typical examples

1) **Dropped from rest:** $v_0=0$ at release, acceleration is constant downward. Solve for time to hit the ground and impact speed.

2) **Thrown upward:** $v_0>0$ (if up is positive). Find time to reach maximum height, maximum height itself, and speed on return to the starting point.

3) **Thrown downward:** $v_0<0$ (in Choice A). Same equations; the sign tells the initial direction.

## Common mistakes

- Switching sign conventions mid-solution (“up is positive” in one equation, “down is positive” in another).
- Setting acceleration to zero at the top because velocity is zero.
- Using $g$ as a signed quantity sometimes and as a magnitude other times without stating which.
- Forgetting that the quadratic position equation can yield two times (on the way up and on the way down) for the same height.
- Using the time-free formula and then choosing the wrong sign for $v$ after taking a square root.

## Worked example

An object is thrown straight upward from a balcony. Choose upward as positive (Choice A). At release:

$x_0 = 12\,\text{m}, \qquad v_0 = 14\,\text{m/s}.$

Take:

$g = 9.8\,\text{m/s}^2.$

1) How long until the object reaches its highest point?  
2) What is the maximum height?  
3) When does it hit the ground ($x=0$), and what is its velocity just before impact?

### Step 1: Time to the highest point

At the top, $v=0$. Use:

$v(t) = v_0 - gt.$

Set to zero:

$$
0 = 14 - 9.8t \;\Rightarrow\; t_{\text{top}} = \frac{14}{9.8} \approx 1.43\,\text{s}.
$$

### Step 2: Maximum height

Use:

$$
x(t) = x_0 + v_0 t - \frac{1}{2}gt^2.
$$

At $t=t_{\text{top}}$:

$$
x_{\text{max}} = 12 + 14(1.43) - \frac{1}{2}(9.8)(1.43)^2.
$$

Compute pieces:

$$
14(1.43) \approx 20.02,
$$

$$
\frac{1}{2}(9.8)(1.43)^2 \approx 4.9\cdot 2.04 \approx 9.996.
$$

So:

$$
x_{\text{max}} \approx 12 + 20.02 - 10.00 \approx 22.0\,\text{m}.
$$

### Step 3: Time to hit the ground

Set $x(t)=0$:

$$
0 = 12 + 14t - \frac{1}{2}(9.8)t^2.
$$

Multiply by 2 to simplify:

$0 = 24 + 28t - 9.8t^2.$

Rearrange:

$9.8t^2 - 28t - 24 = 0.$

Solve the quadratic:

$$
t = \frac{28 \pm \sqrt{(-28)^2 - 4(9.8)(-24)}}{2(9.8)}.
$$

Compute the discriminant:

$(-28)^2 - 4(9.8)(-24) = 784 + 940.8 = 1724.8.$

$$
\sqrt{1724.8} \approx 41.53.
$$

So:

$$
t = \frac{28 \pm 41.53}{19.6}.
$$

One root is negative (unphysical for “after release”):

$$
t_1 = \frac{28 - 41.53}{19.6} \approx -0.69\,\text{s}.
$$

The physical impact time is:

$$
t_{\text{hit}} = \frac{28 + 41.53}{19.6} \approx 3.55\,\text{s}.
$$

### Step 4: Impact velocity

Use:

$v(t) = v_0 - gt.$

So:

$$
v_{\text{hit}} = 14 - 9.8(3.55) \approx 14 - 34.79 \approx -20.8\,\text{m/s}.
$$

Interpretation: the negative sign means the object is moving downward at impact (consistent with the chosen axis).

## Mini recap

- Free fall (ideal) near Earth is constant acceleration of magnitude $g$ directed downward.
- Choose a sign convention and keep it consistent. If upward is positive:

$$
a=-g, \qquad v(t)=v_0-gt, \qquad x(t)=x_0+v_0t-\frac{1}{2}gt^2.
$$

- At the top of an upward throw: $v=0$ but $a=-g$ still.
- Watch for two times at the same height and for sign loss when taking square roots in $v^2$ relations.

<!-- SOURCE: lecture/kinematics/09_piecewise_defined_motion.md -->

# Piecewise-defined motion

## Learning goals

- Read and write motion functions defined **on time intervals** (piecewise definitions).
- Enforce the correct **matching conditions** at the boundaries between intervals.
- Decide when position and velocity should be continuous, and interpret what discontinuities mean physically.
- Solve realistic “accelerate → cruise → brake” problems step by step.

## Why this matters

Real motion rarely follows one simple formula for all time. A car may:

1) accelerate from rest,
2) cruise at constant speed,
3) decelerate to a stop.

Each stage has a different kinematic rule. Piecewise modeling lets you describe such motion with simple segments while staying mathematically precise.

The main risk is inconsistency: if you choose separate formulas on each interval without matching them properly, you can accidentally create an impossible motion (teleporting position, velocity jumps without cause, etc.).

## Core idea

Piecewise motion means: “On this time interval, the motion follows one rule; on the next interval, it follows another rule.”

To make the motion physically meaningful, you typically require:

- **position continuity** at the switching time (no teleportation),
- often **velocity continuity** (no instantaneous change in velocity) unless an impulsive event occurs.

Acceleration may change suddenly (jump) when forces change suddenly (e.g., start braking). That is common and not automatically unphysical.

## Mathematical formulation

### Writing a piecewise position function

A piecewise definition has the form:

$$
x(t) =
\begin{cases}
x_1(t) & \text{for } t_0 \le t < t_1,\\
x_2(t) & \text{for } t_1 \le t < t_2,\\
\cdots
\end{cases}
$$

Similarly, you can specify $v(t)$ or $a(t)$ piecewise.

### Matching conditions at a boundary

Let the switch occur at $t=t_1$.

**Position continuity** means:

$\lim_{t\to t_1^-} x_1(t) = x_2(t_1).$

In many practical problems this is simply:

$x_1(t_1) = x_2(t_1).$

**Velocity continuity** means:

$\lim_{t\to t_1^-} v_1(t) = v_2(t_1).$

If velocity is discontinuous, the acceleration contains an impulse-like effect and the model is no longer “ordinary constant acceleration.” In introductory kinematics problems, velocity jumps are usually not intended unless explicitly stated (e.g., a bounce or a collision).

### A practical workflow for piecewise problems

1) Choose an axis and sign convention.  
2) Write the kinematic rule for the first interval (often constant $a$ or constant $v$).  
3) Use initial conditions to determine constants.  
4) Evaluate $x$ and $v$ at the switching time to generate the initial conditions for the next interval.  
5) Repeat.

## Interpretation

- A piecewise model describes a **single motion** with different regimes.
- Position continuity is a basic physical requirement for ordinary motion.
- Velocity continuity is typical unless an impulsive event occurs.
- Acceleration can change abruptly because it reflects changing influences (engine on/off, braking, friction changes).

## Typical examples

1) **Accelerate then cruise:** constant $a$ for a while, then constant $v$ after reaching a target speed.

2) **Cruise then brake:** constant $v$, then constant negative $a$ until stopping.

3) **Motion with a “turnaround”:** accelerate negatively until velocity becomes zero, then continue with negative velocity (a reversal) — still continuous, no teleportation.

## Common mistakes

- Using the same symbol $x_0, v_0$ for different intervals without clarifying which interval’s initial time they belong to.
- Forgetting to carry the end-of-interval position into the next interval (creating a jump in $x$).
- Assuming velocity is the same at the boundary even when acceleration was nonzero (or vice versa).
- Solving each interval independently with $t=0$ reset, then mixing times without converting (time variables must refer to the same clock unless you explicitly reparameterize).
- Interpreting “piecewise acceleration” as “piecewise position” automatically; you must integrate and apply boundary conditions.

## Worked example

A car moves along a straight road (1D). Choose x-axis along the road, positive forward. The motion has three stages:

1) **Stage I (accelerate):** from $t=0$ to $t=6\,\text{s}$ the car accelerates uniformly from rest with

$a = 2.0\,\text{m/s}^2.$

2) **Stage II (cruise):** from $t=6\,\text{s}$ to $t=16\,\text{s}$ the car moves at constant velocity.

3) **Stage III (brake):** from $t=16\,\text{s}$ onward it brakes with constant acceleration

$a = -3.0\,\text{m/s}^2$

until it stops.

Find:

- the piecewise formulas for $v(t)$ and $x(t)$ (with $x(0)=0$),
- the total distance traveled until the car stops.

### Step 0: Initial condition

At $t=0$:

$x(0)=0, \qquad v(0)=0.$

### Stage I: $0 \le t \le 6$

Velocity:

$$
v(t) = v_0 + at = 0 + (2.0)t = 2t.
$$

Position:

$$
x(t) = x_0 + v_0 t + \frac{1}{2}at^2 = 0 + 0 + \frac{1}{2}(2.0)t^2 = t^2.
$$

Evaluate at the boundary $t=6$ to pass initial conditions to Stage II:

$$
v(6) = 2\cdot 6 = 12\,\text{m/s},
$$

$$
x(6) = 6^2 = 36\,\text{m}.
$$

### Stage II: $6 \le t \le 16$

Constant velocity equal to the value reached at $t=6$:

$$
v(t) = 12\,\text{m/s}.
$$

Position must be continuous and should satisfy $x(6)=36$. A convenient form is:

$$
x(t) = x(6) + v(t-6) = 36 + 12(t-6).
$$

Evaluate at $t=16$:

$$
x(16) = 36 + 12(16-6) = 36 + 120 = 156\,\text{m},
$$

$$
v(16) = 12\,\text{m/s}.
$$

### Stage III: $t \ge 16$

Now acceleration is constant $a=-3.0\,\text{m/s}^2$ and initial conditions at $t=16$ are:

$$
x(16)=156\,\text{m}, \qquad v(16)=12\,\text{m/s}.
$$

Velocity for $t \ge 16$:

$$
v(t) = 12 - 3(t-16).
$$

The car stops when $v(t)=0$:

$$
0 = 12 - 3(t-16) \;\Rightarrow\; 3(t-16)=12 \;\Rightarrow\; t-16=4.
$$

So stopping time is:

$$
t_{\text{stop}} = 20\,\text{s}.
$$

Position for $t \ge 16$:

$$
x(t) = 156 + 12(t-16) + \frac{1}{2}(-3)(t-16)^2.
$$

At stopping time $t=20$ (so $t-16=4$):

$$
x(20) = 156 + 12\cdot 4 - \frac{3}{2}\cdot 4^2 = 156 + 48 - 24 = 180\,\text{m}.
$$

So the total distance traveled (since motion is forward throughout) is:

$$
180\,\text{m}.
$$

### Summary of the piecewise functions

Velocity:

$$
v(t) =
\begin{cases}
2t & 0 \le t \le 6,\\
12 & 6 \le t \le 16,\\
12 - 3(t-16) & 16 \le t \le 20.
\end{cases}
$$

Position:

$$
x(t) =
\begin{cases}
t^2 & 0 \le t \le 6,\\
36 + 12(t-6) & 6 \le t \le 16,\\
156 + 12(t-16) - \frac{3}{2}(t-16)^2 & 16 \le t \le 20.
\end{cases}
$$

Notice how each stage uses boundary values from the previous stage to guarantee continuity.

## Mini recap

- Piecewise motion uses different rules on different time intervals:

$$
x(t)=\begin{cases}x_1(t) & t_0\le t<t_1\\ x_2(t) & t_1\le t<t_2\end{cases}
$$

- Match conditions at boundaries:
  - usually require position continuity,
  - often require velocity continuity unless an impulse-like event is intended.
- Workflow: solve interval 1 → evaluate $x, v$ at boundary → use them as initial conditions for interval 2.
- Acceleration can change abruptly between intervals without being unphysical.

<!-- SOURCE: lecture/kinematics/10_motion_from_given_x_of_t.md -->

# Motion from a given $x(t)$

## Learning goals

- Given a position function $x(t)$, compute velocity $v(t)$ and acceleration $a(t)$ by differentiation.
- Use the sign of $v(t)$ to determine **direction of motion** and intervals of increasing/decreasing position.
- Find **turning times** (where the motion reverses direction) and interpret them correctly.
- Connect algebraic results to graphical ideas (slope and curvature of $x(t)$).

## Why this matters

In many problems you are given the position as a function of time (from a model, a fit to data, or a lab measurement). Then the “kinematics task” is to extract:

- how fast it moves (velocity),
- how its motion changes (acceleration),
- whether it ever stops or reverses direction.

This is also where calculus becomes a practical tool: the derivative is not an abstract operation; it is “the velocity you would measure at that instant.”

## Core idea

If you know where a particle is at every time, you can deduce how it moves:

- velocity is the rate of change of position,
- acceleration is the rate of change of velocity.

In 1D, signs are especially informative:

- $v>0$ means motion in the positive direction,
- $v<0$ means motion in the negative direction,
- $v=0$ can indicate a stop or a turning point (but you must check what happens around it).

## Mathematical formulation

Given $x(t)$, define:

$$
v(t) = \frac{dx}{dt},
$$

$$
a(t) = \frac{dv}{dt} = \frac{d^2x}{dt^2}.
$$

### Turning times and monotonicity

Turning times are candidates where velocity is zero:

$v(t)=0.$

To decide what happens at such a time $t^*$, check the sign of $v(t)$ just before and just after $t^*$:

- if $v$ changes from positive to negative, position reaches a local maximum and motion reverses from + to −,
- if $v$ changes from negative to positive, position reaches a local minimum and motion reverses from − to +,
- if $v$ is zero but does not change sign, the particle may “pause” without reversing (possible in some functions).

### Graphical connection

On the $x$ vs $t$ graph:

- $v(t)$ is the tangent slope,
- $a(t)$ relates to how that slope changes with time (curvature idea).

## Interpretation

- Knowing $x(t)$ gives full kinematic information in 1D (and similarly for each component in 2D/3D).
- Zero velocity at an instant does not necessarily mean the particle stays at rest for a while; it may be a momentary turning point.
- Acceleration sign does not directly tell you direction of motion; it tells you how velocity changes.

## Typical examples

1) **Quadratic position:** $x(t)=x_0+v_0t+\frac{1}{2}at^2$ produces linear velocity and constant acceleration. This is the constant-acceleration model seen earlier.

2) **Cubic position:** can produce multiple turning points (stop-and-go behavior).

3) **Sinusoidal position (preview):** gives oscillatory velocity and acceleration; velocity is zero at extrema of position.

## Common mistakes

- Confusing “position is zero” with “velocity is zero.” The particle can pass through the origin with nonzero speed.
- Finding times when $v(t)=0$ and automatically calling them “turning points” without checking sign change.
- Interpreting negative acceleration as “slowing down” without considering the sign of velocity.
- Differentiation errors (especially product/chain rule) that then propagate into wrong physical conclusions.
- Forgetting units: if $x$ is in meters and $t$ in seconds, then $v$ must be in m/s and $a$ in m/s².

## Worked example

A particle moves along a line with position:

$x(t) = t^3 - 6t^2 + 9t$

with $x$ in meters and $t$ in seconds. Analyze its motion for $t \ge 0$:

1) Find $v(t)$ and $a(t)$.  
2) Determine when the particle is at rest.  
3) Determine intervals of motion direction and find any turning points.

### Step 1: Compute velocity

Differentiate:

$$
v(t) = \frac{dx}{dt} = 3t^2 - 12t + 9.
$$

Factor:

$v(t) = 3(t^2 - 4t + 3) = 3(t-1)(t-3).$

### Step 2: Compute acceleration

Differentiate velocity:

$$
a(t) = \frac{dv}{dt} = 6t - 12 = 6(t-2).
$$

### Step 3: Find rest times

Rest times satisfy $v(t)=0$:

$$
3(t-1)(t-3)=0 \;\Rightarrow\; t=1\,\text{s} \text{ or } t=3\,\text{s}.
$$

So the particle is instantaneously at rest at 1 s and 3 s.

### Step 4: Determine direction of motion (sign of velocity)

Use the factored form $v(t)=3(t-1)(t-3)$ and test intervals:

- For $0 \le t < 1$: pick $t=0$:

$v(0)=3(-1)(-3)=9>0,$

so motion is in the positive direction.

- For $1 < t < 3$: pick $t=2$:

$v(2)=3(1)(-1)=-3<0,$

so motion is in the negative direction.

- For $t>3$: pick $t=4$:

$v(4)=3(3)(1)=9>0,$

so motion is again in the positive direction.

### Step 5: Identify turning points

Velocity changes sign at both rest times:

- At $t=1$: $v$ goes from positive to negative → turning point (local maximum of $x(t)$).
- At $t=3$: $v$ goes from negative to positive → turning point (local minimum of $x(t)$).

To make this concrete, compute the positions:

$x(1) = 1 - 6 + 9 = 4\,\text{m},$

$x(3) = 27 - 54 + 27 = 0\,\text{m}.$

So the particle reaches a maximum position of 4 m at 1 s, then moves back and reaches 0 m at 3 s, then moves forward again.

### Step 6: Interpret acceleration briefly

Acceleration:

$a(t)=6(t-2)$

is negative for $t<2$ and positive for $t>2$. This tells you how the velocity is changing, but direction of motion is determined by $v(t)$, not by the sign of $a(t)$ alone.

## Mini recap

- From $x(t)$ you get:

$$
v(t)=\frac{dx}{dt}, \qquad a(t)=\frac{d^2x}{dt^2}.
$$

- Rest times satisfy $v(t)=0$, but turning points require checking whether $v$ changes sign.
- Sign of $v(t)$ determines direction in 1D.
- Graphically: $v$ is slope of $x(t)$; acceleration controls how that slope changes.

<!-- SOURCE: lecture/kinematics/11_motion_from_given_v_of_t.md -->

# Motion from a given $v(t)$

## Learning goals

- Reconstruct position $x(t)$ from a given velocity function $v(t)$ by integration.
- Use an initial condition (e.g., $x(t_0)=x_0$) to determine the integration constant.
- Interpret displacement as an **area under the $v(t)$ graph**.
- Use the sign of $v(t)$ to reason about direction and net displacement.

## Why this matters

In experiments, velocity is often measured directly (speed sensors, motion tracking that differentiates position). In modeling, you may also be given velocity as the primary description. To recover the actual motion in space, you must integrate.

This section is also where the meaning of an integral becomes physically clear:

- integrating velocity accumulates displacement.

## Core idea

Velocity is the derivative of position:

$$
v(t) = \frac{dx}{dt}.
$$

So position is obtained by “undoing the derivative,” i.e., by integrating:

$$
x(t) = x(t_0) + \int_{t_0}^{t} v(\tau)\,d\tau.
$$

The key idea is that integration introduces an unknown constant (or equivalently, you need one position value to anchor the whole function).

## Mathematical formulation

### General reconstruction formula (1D)

If you know $v(t)$ and one initial condition $x(t_0)=x_0$, then:

$$
x(t) = x_0 + \int_{t_0}^{t} v(\tau)\,d\tau.
$If you perform an indefinite integral:$
\int v(t)\,dt = V(t) + C,
$then:$
x(t) = V(t) + C,
$$

and you determine $C$ from $x(t_0)=x_0$.

### Displacement as area under the velocity graph

Displacement from $t_1$ to $t_2$ is:

$$
\Delta x = x(t_2)-x(t_1) = \int_{t_1}^{t_2} v(t)\,dt.
$$

Graphically:

- positive area (where $v>0$) adds positive displacement,
- negative area (where $v<0$) adds negative displacement.

This is why “back and forth” motion can produce a small net displacement even if the total distance traveled is large.

### Vector extension (brief preview)

In 2D/3D:

$$
\vec{r}(t) = \vec{r}(t_0) + \int_{t_0}^{t} \vec{v}(\tau)\,d\tau,
$$

which is just the component-wise version of the 1D statement.

## Interpretation

- Integrating $v(t)$ gives position up to a constant: you need **one position value** to locate the motion in space.
- The integral over an interval gives displacement directly; it does not require you to first find $x(t)$ if you only need displacement.
- The sign of $v(t)$ tells direction: if $v<0$ over an interval, displacement over that interval is negative (for the chosen axis).

## Typical examples

1) **Constant velocity:** $v(t)=v_0$ integrates to $x(t)=x_0+v_0(t-t_0)$ (uniform motion).

2) **Linear velocity:** $v(t)=v_0+at$ integrates to a quadratic $x(t)$ (constant acceleration).

3) **Velocity that changes sign:** net displacement depends on signed areas; turning points occur where $v(t)=0$ (but you still must interpret).

## Common mistakes

- Forgetting the integration constant / failing to use the initial position to determine it.
- Treating $\int v(t)\,dt$ as “distance traveled.” It gives displacement; distance traveled would require integrating $|v(t)|$ when motion reverses.
- Mixing up the meaning of “area”: negative velocities produce negative contributions to displacement.
- Resetting time to zero for convenience and then forgetting to translate back to the original clock when combining intervals.
- Dropping units: the integral of (m/s) over s gives meters.

## Worked example

A particle moves along a line with velocity:

$$
v(t) = 4 - t
$$

for $0 \le t \le 6$, with $v$ in m/s and $t$ in s. At $t=0$, its position is:

$$
x(0)=2\,\text{m}.
$$

1) Find $x(t)$.  
2) Find the displacement from $t=0$ to $t=6$.  
3) Find the time when it changes direction, and compute the position at that time.

### Step 1: Integrate to get position

Use the reconstruction formula with $t_0=0$:

$$
x(t) = x(0) + \int_{0}^{t} (4-\tau)\,d\tau.
$Compute the integral:$
\int_{0}^{t} (4-\tau)\,d\tau = \left[4\tau - \frac{1}{2}\tau^2\right]_{0}^{t} = 4t - \frac{1}{2}t^2.
$So:$
x(t) = 2 + 4t - \frac{1}{2}t^2.
$$

### Step 2: Displacement from 0 to 6

Displacement is:

$$
\Delta x = \int_{0}^{6} (4-t)\,dt = \left[4t - \frac{1}{2}t^2\right]_{0}^{6} = 24 - 18 = 6\,\text{m}.
$$

So $x(6)=x(0)+\Delta x = 2+6 = 8\,\text{m}$ (consistent with the formula above).

### Step 3: Direction change time

Direction changes when $v(t)=0$:

$$
4 - t = 0 \;\Rightarrow\; t=4\,\text{s}.
$Compute the position at that time:$
x(4) = 2 + 4(4) - \frac{1}{2}(4)^2 = 2 + 16 - 8 = 10\,\text{m}.
$$

Interpretation: from $t=0$ to $t=4$, velocity is positive and the particle moves in the positive direction; after $t=4$, velocity is negative and it moves back.

## Mini recap

- Position from velocity (1D):

$$
x(t) = x_0 + \int_{t_0}^{t} v(\tau)\,d\tau.
$- Displacement over an interval:$
\Delta x = \int_{t_1}^{t_2} v(t)\,dt
$$

(signed area under $v(t)$).

- The integration constant is fixed by an initial position.
- Displacement is not the same as distance traveled when direction changes.

<!-- SOURCE: lecture/kinematics/12_motion_from_given_a_of_t.md -->

# Motion from a given $a(t)$

## Learning goals

- Reconstruct $v(t)$ from a given acceleration $a(t)$ by integration.
- Reconstruct $x(t)$ by integrating again, using **initial conditions** to fix constants.
- Understand why two initial conditions are needed to determine a unique position function from $a(t)$.
- Work confidently with common acceleration laws (polynomial and simple trigonometric forms).

## Why this matters

In kinematics, acceleration is sometimes provided directly:

- a sensor measures acceleration,
- a problem states “acceleration varies with time as …,”
- or later in dynamics, forces determine acceleration.

To get the motion, you must integrate. This is the core “reconstruction pipeline”:

$$
a(t) \rightarrow v(t) \rightarrow x(t).
$$

The most frequent errors here are not calculus complexity, but missing constants and mixing initial times.

## Core idea

Acceleration is the derivative of velocity, and velocity is the derivative of position:

$$
a(t) = \frac{dv}{dt}, \qquad v(t)=\frac{dx}{dt}.
$$

So:

- integrating $a(t)$ accumulates changes in velocity,
- integrating $v(t)$ accumulates changes in position.

Because you integrate twice, you need **two pieces of initial information** to pin down the motion, typically:

$$
v(t_0)=v_0, \qquad x(t_0)=x_0.
$$

## Mathematical formulation

### Step 1: Velocity from acceleration

Given $a(t)$ and $v(t_0)=v_0$:

$$
v(t) = v_0 + \int_{t_0}^{t} a(\tau)\,d\tau.
$$

### Step 2: Position from velocity

Given also $x(t_0)=x_0$:

$$
x(t) = x_0 + \int_{t_0}^{t} v(\tau)\,d\tau.
$Combining both steps:$
x(t) = x_0 + \int_{t_0}^{t} \left(v_0 + \int_{t_0}^{\tau} a(s)\,ds\right)d\tau.
$$

This expression looks nested, but the workflow is simple: integrate once to get $v(t)$, then integrate again to get $x(t)$.

### A practical note on constants

If you do indefinite integrals, you will get constants at each step:

$$
v(t) = \int a(t)\,dt + C_1,
$$

$$
x(t) = \int v(t)\,dt + C_2.
$$

Use the initial conditions to determine $C_1$ and $C_2$. Without them, there are infinitely many motions consistent with the same acceleration law.

## Interpretation

- The integral of acceleration over time gives the **change in velocity**:

$$
v(t_2)-v(t_1) = \int_{t_1}^{t_2} a(t)\,dt.
$$

- The integral of velocity gives **displacement**:

$$
x(t_2)-x(t_1) = \int_{t_1}^{t_2} v(t)\,dt.
$$

- If you only know $a(t)$, you cannot locate the motion in space: you still need initial position and velocity.

## Typical examples

1) **Polynomial acceleration:** $a(t)=kt$ gives quadratic velocity and cubic position.

2) **Sinusoidal acceleration:** $a(t)=A\cos(\omega t)$ leads to sinusoidal velocity and position with phase shifts. This previews periodic motion.

3) **Constant acceleration:** $a(t)=a_0$ returns the uniformly accelerated motion formulas from Section 07.

## Common mistakes

- Forgetting one of the two constants (integrating twice but applying only one initial condition).
- Using $v(t)=\int a(t)dt$ without adding the initial velocity.
- Using an initial condition at a different time than the one used in the integral limits (mixing $t_0$ values).
- Losing sign information: acceleration can be positive or negative depending on the chosen axis.
- Treating the integral of acceleration as “distance” rather than “velocity change.”

## Worked example

An object moves along a line with acceleration:

$a(t) = 2t$

with $a$ in m/s² and $t$ in s. At $t=0$:

$v(0) = 1\,\text{m/s}, \qquad x(0)=0.$

1) Find $v(t)$ and $x(t)$.  
2) Find the displacement from $t=0$ to $t=3$.

### Step 1: Integrate acceleration to get velocity

Use:

$$
v(t) = v(0) + \int_{0}^{t} 2\tau\,d\tau.
$$

Compute the integral:

$$
\int_{0}^{t} 2\tau\,d\tau = \left[\tau^2\right]_{0}^{t} = t^2.
$$

So:

$v(t) = 1 + t^2.$

### Step 2: Integrate velocity to get position

Use:

$$
x(t) = x(0) + \int_{0}^{t} (1+\tau^2)\,d\tau.
$$

Compute:

$$
\int_{0}^{t} (1+\tau^2)\,d\tau = \left[\tau + \frac{1}{3}\tau^3\right]_{0}^{t} = t + \frac{1}{3}t^3.
$$

So:

$$
x(t) = t + \frac{1}{3}t^3.
$$

### Step 3: Displacement from 0 to 3

Displacement is $x(3)-x(0)=x(3)$:

$$
x(3) = 3 + \frac{1}{3}(27) = 3 + 9 = 12\,\text{m}.
$$

### Optional check (velocity change)

Velocity change from 0 to 3 is:

$v(3)-v(0) = (1+9)-1 = 9\,\text{m/s},$

and also:

$$
\int_{0}^{3} 2t\,dt = \left[t^2\right]_{0}^{3} = 9,
$$

consistent.

## Mini recap

- Reconstruction pipeline:

$$
v(t) = v_0 + \int_{t_0}^{t} a(\tau)\,d\tau,
$$

$$
x(t) = x_0 + \int_{t_0}^{t} v(\tau)\,d\tau.
$$

- You generally need two initial conditions (one for $v$, one for $x$).
- Integrals have clear meanings:
  - area under $a(t)$ gives velocity change,
  - area under $v(t)$ gives displacement.

<!-- SOURCE: lecture/kinematics/13_inverse_kinematics_problems.md -->

# Inverse kinematics problems

## Learning goals

- Recognize inverse kinematics tasks: “find the motion law that fits given constraints.”
- Translate verbal/graphical constraints into equations involving $x(t), v(t), a(t)$.
- Choose a reasonable **function family** (e.g., polynomial for constant acceleration, sinusoid for periodic motion) and determine its parameters from conditions.
- Identify what extra information is needed when the constraints are insufficient.

## Why this matters

So far you have mostly done “forward” kinematics:

- given $x(t)$ → find $v(t)$ and $a(t)$,
- given $v(t)$ or $a(t)$ → reconstruct the rest using initial conditions.

Inverse kinematics goes the other way:

- you are told features of the motion (turning times, maximum height, average velocity, total displacement, etc.),
- and you must infer a motion function consistent with those features.

This is a powerful skill because real data and real questions often come as constraints, not as a neatly packaged formula.

## Core idea

An inverse kinematics problem has three repeating steps:

1) **Select a model form** (a family of functions) based on the physical description and assumptions.  
2) **Write equations** by applying the constraints to the model.  
3) **Solve for parameters** and check consistency (units, signs, and physical meaning).

The key is not guessing randomly; it is choosing a model family that matches the implied structure:

- constant acceleration → quadratic $x(t)$ or linear $v(t)$,
- periodic motion → sinusoidal $x(t)$,
- “starts and stops at given times” → ensure $v(t)=0$ at those times,
- “passes through points” → enforce $x(t_i)=x_i$.

## Mathematical formulation

### Common constraint types

Constraints usually come in a few standard forms:

Position at a time:

$x(t_i)=x_i$

Velocity at a time:

$v(t_i)=v_i$

Acceleration at a time:

$a(t_i)=a_i$

Turning time (rest instant):

$v(t^*)=0$

Total displacement on an interval:

$x(t_2)-x(t_1)=\Delta x$

Average velocity constraint:

$$
\frac{x(t_2)-x(t_1)}{t_2-t_1} = v_{\text{avg}}
$$

### Picking a model family (examples)

**Constant acceleration assumption**:

$$
x(t)=x_0+v_0(t-t_0)+\frac{1}{2}a_0(t-t_0)^2
$$

Unknown parameters: $x_0, v_0, a_0$ (or fewer if some are given).

**Quadratic position model (general)**:

$x(t)=At^2+Bt+C$

Unknown parameters: $A, B, C$.

This is equivalent to constant acceleration because:

$v(t)=2At+B, \qquad a(t)=2A.$

**Sinusoidal (periodic) model**:

$x(t)=x_{\text{eq}} + A\cos(\omega t + \phi)$

Unknown parameters: equilibrium offset $x_{\text{eq}}$, amplitude $A$, angular frequency $\omega$, phase $\phi$.

### When the data is not enough

If you have fewer independent constraints than parameters, you cannot determine a unique motion function. You can either:

- accept a family of solutions (with a free parameter),
- or decide what additional information would fix the motion (e.g., one more position/time measurement).

## Interpretation

Inverse kinematics is “model fitting with physics awareness.” The goal is not to create the true motion (real motion may be more complicated), but to create a motion model that:

- satisfies the stated constraints,
- respects the assumptions (e.g., constant acceleration),
- produces interpretable parameters (units and signs make sense).

Always check:

- parameter units,
- whether predicted velocities/positions match the intended direction,
- whether turning times are actually maxima/minima (check sign change of $v$).

## Typical examples

1) **Find a quadratic $x(t)$ that passes through three points** $\big(t_1,x_1\big),\big(t_2,x_2\big),\big(t_3,x_3\big)$.

2) **Given maximum height and launch time**, infer initial velocity in free fall (using $v(t_{\text{top}})=0$).

3) **Given period and amplitude**, write a sinusoidal position function up to a phase choice.

## Common mistakes

- Choosing a model family inconsistent with the assumptions (e.g., using constant-acceleration formulas when the problem implies periodic motion).
- Writing constraints with wrong quantities (e.g., using $x=0$ when the statement is about velocity).
- Forgetting that turning times require $v=0$, not $x=0$.
- Solving for parameters but not checking whether the solution matches the intended physical story (direction, timing).
- Assuming uniqueness without counting constraints vs unknowns.

## Worked example

Assume a particle moves in 1D with **constant acceleration**, and choose $t_0=0$. You are told:

- $x(0)=0$,
- the particle is instantaneously at rest at $t=2\,\text{s}$,
- $x(2\,\text{s})=12\,\text{m}$.

Find $x(t)$, $v(t)$, and $a$.

### Step 1: Choose a model family

Constant acceleration means:

$$
x(t) = x_0 + v_0 t + \frac{1}{2}a t^2.
$$

Here $x_0=x(0)=0$, so:

$$
x(t) = v_0 t + \frac{1}{2}a t^2.
$$

Velocity is:

$$
v(t) = \frac{dx}{dt} = v_0 + at.
$$

Unknowns: $v_0$ and $a$ (two unknowns → we need two independent constraints).

### Step 2: Use the “rest at t=2 s” constraint

Rest means $v(2)=0$:

$$
0 = v_0 + a(2) \;\Rightarrow\; v_0 = -2a.
$$

### Step 3: Use the position at t=2 s constraint

$$
x(2) = 12 = v_0(2) + \frac{1}{2}a(2)^2 = 2v_0 + 2a.
$$

Substitute $v_0=-2a$:

$12 = 2(-2a) + 2a = -4a + 2a = -2a.$

So:

$a = -6\,\text{m/s}^2.$

Then:

$v_0 = -2a = 12\,\text{m/s}.$

### Step 4: Write the final motion functions

Velocity:

$v(t) = v_0 + at = 12 - 6t.$

Position:

$$
x(t) = v_0 t + \frac{1}{2}a t^2 = 12t - 3t^2.
$$

### Step 5: Interpret the result

- The negative acceleration means acceleration points in the negative axis direction.
- The particle reaches a turning time at $t=2$ because:

$v(2)=12-12=0.$

- The position at that time is:

$x(2)=12(2)-3(2)^2=24-12=12\,\text{m},$

as required.

### A quick inverse-kinematics “consistency check” variant

With the same assumptions $x(0)=0$, constant acceleration, and $v(2)=0$, the model forces:

$x(4)=0$

(you can verify by substituting $x(t)=12t-3t^2$). If someone additionally claims “$x(4)=8\,\text{m}$,” then the constraints are incompatible: at least one assumption or measurement must be wrong.

This kind of check is a feature of inverse kinematics: you learn not only parameters, but also whether a set of statements can be true at the same time.

## Mini recap

- Inverse kinematics means inferring a motion law from constraints on $x(t), v(t), a(t)$.
- Workflow: choose a model family → translate constraints into equations → solve parameters → check consistency.
- Count unknown parameters vs independent constraints; if constraints conflict, the model assumptions (or the data) must be revised.
- A contradiction is not “failure”; it is diagnostic information about the assumptions.

<!-- SOURCE: lecture/kinematics/14_graphical_interpretation_x_v_a.md -->

# Graphical interpretation of $x(t)$, $v(t)$, and $a(t)$

## Learning goals

- Use **slope** to connect $x(t) \rightarrow v(t)$ and $v(t) \rightarrow a(t)$.
- Use **area** to connect $a(t) \rightarrow v(t)$ and $v(t) \rightarrow x(t)$ (as changes).
- Infer qualitative features (direction, speeding up/slowing down, turning points) from graphs without full algebra.
- Avoid common graph-reading traps (confusing height with slope, confusing area with value).

## Why this matters

In many real situations you do not have a clean formula—you have a graph or data. Graphical reasoning lets you answer questions like:

- “When is the particle moving forward/backward?”
- “When does it turn around?”
- “When is its speed increasing?”

without doing heavy computation. It also provides a powerful “sanity check” for algebraic work.

## Core idea

There are two fundamental links:

1) **Derivative link (slope):**

- velocity is the slope of the position graph,
- acceleration is the slope of the velocity graph.

2) **Integral link (area):**

- change in velocity is area under the acceleration graph,
- change in position is area under the velocity graph.

Once you internalize these four statements, most graph problems become systematic.

## Mathematical formulation

### Slope (derivatives)

$$
v(t) = \frac{dx}{dt}
$$

So on an $x$–$t$ graph, the slope of the tangent at time $t$ equals $v(t)$.

$$
a(t) = \frac{dv}{dt}
$$

So on a $v$–$t$ graph, the slope of the tangent at time $t$ equals $a(t)$.

### Area (integrals)

Change in velocity from $t_1$ to $t_2$:

$$
v(t_2)-v(t_1) = \int_{t_1}^{t_2} a(t)\,dt.
$Change in position from $t_1$ to $t_2$ (displacement):$
x(t_2)-x(t_1) = \int_{t_1}^{t_2} v(t)\,dt.
$$

Graphically, these are **signed areas**:

- area above the time axis contributes positively,
- area below contributes negatively.

## Interpretation

### Direction of motion (1D)

- If $v(t) > 0$, the particle moves in the positive direction.
- If $v(t) < 0$, it moves in the negative direction.

On the $x(t)$ graph, this corresponds to:

- increasing $x(t)$ → positive slope → $v>0$,
- decreasing $x(t)$ → negative slope → $v<0$.

### Turning points

A turning time occurs when the particle changes direction. In 1D this requires:

$$
v(t^*)=0
$$

and a sign change of $v$ across $t^*$.

On $x(t)$, turning points appear as local maxima/minima (slope zero and slope sign change).

### Speeding up vs slowing down (1D)

Speed increases when velocity and acceleration have the same sign.  
Speed decreases when they have opposite signs.

Graphically, on a $v(t)$ plot:

- if $v$ is positive and the graph slopes upward (positive acceleration), speed increases,
- if $v$ is positive and the graph slopes downward (negative acceleration), speed decreases,
- similarly for negative $v$ with sign logic reversed.

## Typical examples

1) **Constant velocity:** $x(t)$ is a straight line; $v(t)$ is a horizontal line; $a(t)=0$.

2) **Constant acceleration:** $v(t)$ is a straight line; $a(t)$ is a horizontal line; $x(t)$ is a parabola.

3) **Back-and-forth motion:** $v(t)$ crosses zero; $x(t)$ has peaks/valleys.

## Common mistakes

- Reading the *height* of the $x(t)$ graph as velocity. Velocity is the **slope**, not the height.
- Reading the *height* of the $v(t)$ graph as acceleration. Acceleration is the **slope** of $v(t)$.
- Confusing “area under $v(t)$” with “distance traveled.” It gives **displacement**; distance requires $\int |v(t)|dt$.
- Forgetting that areas are signed (negative velocity gives negative displacement).
- Drawing inferred graphs without matching continuity: if $x(t)$ is smooth, then $v(t)$ should be continuous; abrupt jumps in $v$ correspond to non-smooth $x(t)$.

## Worked example

You are given the following velocity–time graph description for motion in 1D:

- From $t=0$ to $t=2\,\text{s}$, velocity increases linearly from 0 to $4\,\text{m/s}$.
- From $t=2$ to $t=5\,\text{s}$, velocity is constant at $4\,\text{m/s}$.
- From $t=5$ to $t=7\,\text{s}$, velocity decreases linearly from $4\,\text{m/s}$ to $-2\,\text{m/s}$.

Assume $x(0)=0$. Find:

1) The acceleration on each interval.  
2) The displacement on each interval and the final position $x(7)$.  
3) Whether there is a turning point (direction change).

### Step 1: Acceleration from slopes of $v(t)$

Interval 0–2 s:

$$
a = \frac{4-0}{2-0} = 2\,\text{m/s}^2.
$Interval 2–5 s:$
a = 0.
$Interval 5–7 s:$
a = \frac{-2-4}{7-5} = \frac{-6}{2} = -3\,\text{m/s}^2.
$$

### Step 2: Displacement from areas under $v(t)$

Displacement is the signed area under the $v(t)$ curve.

Interval 0–2 s: triangle with base 2 and height 4:

$$
\Delta x_{0\to 2} = \frac{1}{2}(2)(4) = 4\,\text{m}.
$Interval 2–5 s: rectangle with width 3 and height 4:$
\Delta x_{2\to 5} = (3)(4) = 12\,\text{m}.
$Interval 5–7 s: trapezoid (average of endpoints times width):$
\Delta x_{5\to 7} = \frac{(4)+(-2)}{2}\cdot (2) = (1)(2) = 2\,\text{m}.
$Total displacement:$
\Delta x_{0\to 7} = 4 + 12 + 2 = 18\,\text{m}.
$Since $x(0)=0$:$
x(7)=18\,\text{m}.
$$

### Step 3: Turning point?

A turning time requires $v=0$ with sign change. On the last interval, velocity goes from +4 to −2, so it crosses zero once.

Find the crossing time. On 5–7 s the slope is −3 m/s², so:

$$
v(t) = 4 - 3(t-5).
$Set $v=0$:$
0 = 4 - 3(t-5) \;\Rightarrow\; 3(t-5)=4 \;\Rightarrow\; t=5 + \frac{4}{3} \approx 6.33\,\text{s}.
$$

So the particle changes direction at about 6.33 s.

## Mini recap

- Slope links:

$$
v(t)=\frac{dx}{dt}, \qquad a(t)=\frac{dv}{dt}.
$- Area links:$
v(t_2)-v(t_1)=\int_{t_1}^{t_2}a(t)dt, \qquad x(t_2)-x(t_1)=\int_{t_1}^{t_2}v(t)dt.
$$

- Turning points in 1D occur where $v=0$ with a sign change.
- Always ask: “Is this a slope question or an area question?”

<!-- SOURCE: lecture/kinematics/15_relative_motion_intro.md -->

# Relative motion (intro)

## Learning goals

- Explain what “relative motion” means: describing motion **with respect to a moving observer**.
- Compute relative position and relative velocity in simple 1D and 2D cases.
- Use the “velocity addition” idea correctly and interpret signs/directions.
- Solve standard train/boat/walkway-style problems using a consistent notation.

## Why this matters

Many motion descriptions are implicitly relative:

- “The passenger is walking forward at 1 m/s” (relative to the train).
- “The train moves at 20 m/s” (relative to the ground).

If you do not track *relative to what*, you will add the wrong quantities and get contradictions.

Relative motion is also the first step toward understanding why the **choice of reference frame** matters. Later, in dynamics, the idea of an **inertial frame** will build on this.

## Core idea

Motion is always described relative to some reference frame. If you change the observer (frame), the numerical description of velocity changes.

In the simplest (classical) situations, velocities add in an intuitive way:

- “velocity of A relative to C” equals “velocity of A relative to B” plus “velocity of B relative to C.”

The main challenge is bookkeeping: keeping track of *which object is measured relative to which*.

## Mathematical formulation

### Notation

Let:

- A be the object of interest (e.g., a person),
- B be an intermediate frame/object (e.g., a train),
- C be a reference frame (e.g., the ground).

We write:

$\vec{v}_{A/B}$

for “velocity of A relative to B.”

### Velocity addition (Galilean, classical)

In classical mechanics (at ordinary speeds), the velocities add as:

$\vec{v}_{A/C} = \vec{v}_{A/B} + \vec{v}_{B/C}.$

This can be understood component-wise in any chosen coordinate system.

### Relative position (simple form)

Similarly for position vectors:

$\vec{r}_{A/C} = \vec{r}_{A/B} + \vec{r}_{B/C}.$

In many intro problems you can treat this as “vector from C to A equals vector from C to B plus vector from B to A,” but you should keep the labels consistent.

## Interpretation

- These addition rules are not “new physics.” They are bookkeeping rules for changing observers in classical kinematics.
- Direction matters: all velocities are vectors (in 1D, signed scalars).
- If you reverse “who is relative to whom,” the sign changes:

$\vec{v}_{A/B} = -\vec{v}_{B/A}.$

## Typical examples

1) **Walking on a train (1D):** person walks forward relative to the train while the train moves relative to the ground.

2) **Moving walkway (1D):** your speed relative to the ground depends on your walking speed relative to the belt plus the belt’s speed.

3) **Boat in a river (2D):** boat’s velocity relative to the ground equals boat relative to water plus water relative to ground (current). This naturally becomes a vector addition problem.

## Common mistakes

- Adding speeds as numbers when directions differ (must add vectors or signed 1D velocities).
- Mixing “relative to ground” and “relative to train” in the same symbol without labels.
- Using the right formula but with swapped roles (e.g., using \vec{v}_{B/C} when you needed \vec{v}_{C/B}).
- Forgetting that “straight across the river” is a constraint on the *ground* trajectory, not on the boat’s velocity relative to the water.

## Worked example

A person walks on a moving walkway in a straight corridor (1D). Choose the positive direction along the corridor.

- The walkway moves at

$v_{W/G} = 1.2\,\text{m/s}$

relative to the ground (G), where W denotes the walkway.

- The person walks at

$v_{P/W} = 0.8\,\text{m/s}$

relative to the walkway, in the positive direction.

1) Find the person’s velocity relative to the ground.  
2) How long does it take to traverse a 60 m walkway segment?

### Step 1: Add velocities with clear labels

Use:

$v_{P/G} = v_{P/W} + v_{W/G}.$

So:

$v_{P/G} = 0.8 + 1.2 = 2.0\,\text{m/s}.$

### Step 2: Use uniform motion for travel time

If velocity relative to the ground is constant, then travel time over distance 60 m is:

$$
t = \frac{\Delta x}{v_{P/G}} = \frac{60\,\text{m}}{2.0\,\text{m/s}} = 30\,\text{s}.
$$

### Variant: walking against the walkway

If the person walks opposite the belt direction with

$v_{P/W} = -0.8\,\text{m/s},$

then:

$v_{P/G} = -0.8 + 1.2 = 0.4\,\text{m/s},$

and the same 60 m would take:

$$
t = \frac{60}{0.4} = 150\,\text{s}.
$$

This illustrates why sign conventions and labels matter: the same walking effort produces very different ground motion depending on the frame’s motion.

## Mini recap

- Relative velocity notation: $\vec{v}_{A/B}$ means “A relative to B.”
- Classical velocity addition:

$\vec{v}_{A/C} = \vec{v}_{A/B} + \vec{v}_{B/C}.$

- Reverse relation flips sign: $\vec{v}_{A/B}=-\vec{v}_{B/A}$.
- In 1D, treat velocities as signed; in 2D/3D, add vectors component-wise.

<!-- SOURCE: lecture/kinematics/16_2d_motion_and_components.md -->

# 2D motion and components

## Learning goals

- Describe planar motion using a position vector and component functions.
- Compute velocity and acceleration vectors component-wise and interpret them geometrically.
- Use the **independence of orthogonal components** to solve 2D kinematics problems systematically.
- Convert between vector form and coordinate form, and check consistency of units and signs.

## Why this matters

Most interesting motions are not purely 1D: projectiles, circular motion, and relative motion in a plane all require 2D thinking.

The good news is that 2D kinematics is not “harder calculus.” It is mostly good bookkeeping:

- choose axes,
- write component functions,
- apply 1D kinematics separately in each direction,
- then recombine into a vector picture.

This component approach is the backbone of projectile motion later.

## Core idea

In the plane, position has two coordinates. If you choose perpendicular axes with unit vectors:

$\hat{i}, \qquad \hat{j},$

then the position vector is:

$\vec{r}(t) = x(t)\,\hat{i} + y(t)\,\hat{j}.$

Differentiation applies component-wise:

$$
\vec{v}(t) = \frac{d\vec{r}}{dt} = \frac{dx}{dt}\,\hat{i} + \frac{dy}{dt}\,\hat{j},
$$

$$
\vec{a}(t) = \frac{d\vec{v}}{dt} = \frac{d^2x}{dt^2}\,\hat{i} + \frac{d^2y}{dt^2}\,\hat{j}.
$$

So planar kinematics is “two linked 1D problems” that share the same time variable t.

To keep notation explicit:

$t$

## Mathematical formulation

### Component definitions

Define velocity components:

$$
v_x(t) = \frac{dx}{dt}, \qquad v_y(t) = \frac{dy}{dt}.
$$

Then:

$\vec{v}(t) = v_x(t)\,\hat{i} + v_y(t)\,\hat{j}.$

Define acceleration components:

$$
a_x(t) = \frac{dv_x}{dt} = \frac{d^2x}{dt^2}, \qquad a_y(t) = \frac{dv_y}{dt} = \frac{d^2y}{dt^2},
$$

and:

$\vec{a}(t) = a_x(t)\,\hat{i} + a_y(t)\,\hat{j}.$

### Independence of orthogonal components (what it really means)

If you know the acceleration components as functions of time, you can solve for the corresponding position components separately using 1D methods:

$a_x(t) \rightarrow v_x(t) \rightarrow x(t),$

$a_y(t) \rightarrow v_y(t) \rightarrow y(t).$

The coupling between the components is only through the shared time variable t. There is no rule that says “a change in x must cause a change in y” unless the problem imposes a constraint (like motion along a fixed track).

### Speed from components

The speed is the magnitude of the velocity vector:

$$
|\vec{v}(t)| = \sqrt{v_x(t)^2 + v_y(t)^2}.
$$

This is often where students accidentally confuse “constant v_x” with “constant speed.” Even if v_x is constant, speed can change because v_y changes.

## Interpretation

- The velocity vector points in the instantaneous direction of motion; it is tangent to the trajectory.
- The acceleration vector tells you how the velocity changes; it can change the speed, the direction, or both.
- Component equations are not “less physical” than vector equations. They are the same physics expressed in a coordinate system.

## Typical examples

1) **Constant-velocity motion at an angle:** both x(t) and y(t) are linear in t. The trajectory is a straight line.

2) **Projectile motion preview:** horizontal acceleration is zero while vertical acceleration is constant (gravity):

$a_x = 0, \qquad a_y = \text{constant}.$

Horizontal and vertical motions are solved independently and then combined.

3) **River crossing:** the boat’s ground velocity is a vector sum of “boat relative to water” and “water relative to ground.”

## Common mistakes

- Treating v_x and v_y as if they were magnitudes (forgetting signs or direction).
- Mixing vector magnitudes with components (e.g., writing a projection relation but using the wrong angle definition):

$v_x = |\vec{v}|\cos\theta.$
- Thinking “constant v_x” means “constant speed.”
- Forgetting that the same time t must be used in both components.
- Switching axes mid-solution without updating component definitions.

## Worked example

A particle moves in the plane with position components:

$x(t) = 3t, \qquad y(t) = 2t - t^2,$

with x and y in meters and t in seconds.

1) Find:

$\vec{v}(t) \quad \text{and} \quad \vec{a}(t).$

2) Find the speed at:

$t=1\,\text{s}.$

3) Determine when the particle is moving upward vs downward.

### Step 1: Differentiate to get velocity components

$$
v_x(t) = \frac{dx}{dt} = 3,
$$

$$
v_y(t) = \frac{dy}{dt} = 2 - 2t.
$$

So:

$\vec{v}(t) = 3\,\hat{i} + (2-2t)\,\hat{j}.$

### Step 2: Differentiate again to get acceleration components

$$
a_x(t) = \frac{dv_x}{dt} = 0,
$$

$$
a_y(t) = \frac{dv_y}{dt} = -2.
$$

So:

$\vec{a}(t) = 0\,\hat{i} + (-2)\,\hat{j} = -2\,\hat{j}.$

Interpretation: acceleration is constant downward (negative y-direction), while the horizontal velocity stays constant.

### Step 3: Speed at t = 1 s

Compute components at t = 1:

$v_x(1) = 3, \qquad v_y(1) = 2-2(1) = 0.$

So:

$$
|\vec{v}(1)| = \sqrt{3^2 + 0^2} = 3\,\text{m/s}.
$$

### Step 4: Upward vs downward motion

The motion is upward when v_y(t) > 0 and downward when v_y(t) < 0.

Solve v_y(t) = 0:

$$
2 - 2t = 0 \Rightarrow t = 1\,\text{s}.
$$

So:

- for 0 \le t < 1, v_y > 0 (moving upward),
- for t > 1, v_y < 0 (moving downward).

Notice that the particle can be moving downward while still moving to the right, because v_x stays positive.

## Mini recap

- Planar motion:

$\vec{r}(t) = x(t)\,\hat{i} + y(t)\,\hat{j}.$

- Component-wise differentiation:

$$
\vec{v}(t) = v_x\,\hat{i} + v_y\,\hat{j}, \qquad v_x=\frac{dx}{dt}, \quad v_y=\frac{dy}{dt},
$$

$$
\vec{a}(t) = a_x\,\hat{i} + a_y\,\hat{j}, \qquad a_x=\frac{d^2x}{dt^2}, \quad a_y=\frac{d^2y}{dt^2}.
$$

- Orthogonal components are solved independently (same time t, separate 1D kinematics).
- Speed is magnitude:

$$
|\vec{v}|=\sqrt{v_x^2+v_y^2}.
$$

<!-- SOURCE: lecture/kinematics/17_projectile_motion.md -->

# Projectile motion (idealized, no air resistance)

## Learning goals

- Set up projectile motion in 2D using independent horizontal and vertical components.
- Derive the standard time-dependent formulas for position and velocity components under constant gravity.
- Eliminate time to obtain the trajectory equation and interpret what it says.
- Solve for time of flight, maximum height, and range in common launch/landing configurations.

## Why this matters

Projectile motion is a classic example where the “2D components” method pays off immediately:

- the horizontal motion is simple (often uniform),
- the vertical motion is constant-acceleration motion under gravity.

It also trains a crucial modeling skill: knowing exactly which assumptions make the problem solvable with simple equations.

## Core idea

In the ideal projectile model:

- after launch, the only acceleration is gravity,
- gravity points downward with constant magnitude g,
- there is no horizontal acceleration.

So you solve two 1D problems that share the same time variable:

$t.$

- horizontal: uniform motion,
- vertical: uniformly accelerated motion.

## Mathematical formulation

### Assumptions (state them when you use the model)

1) Motion is near Earth with approximately constant g.  
2) Air resistance is neglected.  
3) The projectile is treated as a particle.  
4) The coordinate system is chosen with x horizontal and y vertical.

Choose y positive upward. Then:

$a_x = 0, \qquad a_y = -g.$

### Initial conditions (launch)

At time:

$t=0,$

let:

$x(0) = x_0, \qquad y(0) = y_0.$

Let the initial speed be v_0 at launch angle theta above the horizontal. Then:

$v_x(0) = v_0\cos\theta, \qquad v_y(0) = v_0\sin\theta.$

### Solve the horizontal motion

Since horizontal acceleration is zero, horizontal velocity is constant:

$v_x(t) = v_0\cos\theta.$

Integrate:

$x(t) = x_0 + (v_0\cos\theta)t.$

### Solve the vertical motion

Since vertical acceleration is constant and equal to -g:

$v_y(t) = v_0\sin\theta - gt,$

$$
y(t) = y_0 + (v_0\sin\theta)t - \frac{1}{2}gt^2.
$$

### Trajectory equation (time eliminated)

From the horizontal solution:

$$
t = \frac{x-x_0}{v_0\cos\theta}.
$$

Substitute into the vertical position function:

$$
y = y_0 + (v_0\sin\theta)\left(\frac{x-x_0}{v_0\cos\theta}\right) - \frac{1}{2}g\left(\frac{x-x_0}{v_0\cos\theta}\right)^2.
$$

Simplify:

$$
y = y_0 + (x-x_0)\tan\theta - \frac{g}{2v_0^2\cos^2\theta}(x-x_0)^2.
$$

This is a parabola in the x–y plane.

### Maximum height (from v_y = 0)

At the top of the trajectory:

$v_y=0.$

$$
0 = v_0\sin\theta - gt_{\text{top}} \Rightarrow t_{\text{top}} = \frac{v_0\sin\theta}{g}.
$$

Plug into the vertical position function (or use a constant-acceleration relation) to get the maximum height:

$$
y_{\text{max}} = y_0 + \frac{(v_0\sin\theta)^2}{2g}.
$$

### Time of flight and range (special common case: same launch and landing height)

If the projectile lands at the same vertical level it was launched from, then:

$y(t_f)=y_0.$

Using:

$$
y(t) = y_0 + (v_0\sin\theta)t - \frac{1}{2}gt^2,
$$

set y(t_f) = y_0 and factor:

$$
0 = (v_0\sin\theta)t_f - \frac{1}{2}gt_f^2 = t_f\left(v_0\sin\theta - \frac{1}{2}gt_f\right).
$$

Ignoring t_f = 0, we get:

$$
t_f = \frac{2v_0\sin\theta}{g}.
$$

Range R is the horizontal displacement during this time:

$$
R = x(t_f)-x_0 = (v_0\cos\theta)t_f = \frac{2v_0^2\sin\theta\cos\theta}{g}.
$$

Using the identity:

$2\sin\theta\cos\theta=\sin(2\theta),$

$$
R = \frac{v_0^2}{g}\sin(2\theta).
$$

## Interpretation

- Horizontal and vertical motions share the same time variable t, but their accelerations differ: a_x = 0, a_y = -g.
- The trajectory is parabolic in the ideal model, but the time history matters: the projectile does not “follow a parabola at constant speed.”
- The range formula applies only when launch and landing heights are equal and air resistance is neglected.

## Typical examples

1) **Ball thrown from ground level:** compute time of flight, maximum height, and range.

2) **Thrown from a platform (different landing height):** solve the vertical equation for the impact time t, then compute the horizontal position at that time.

3) **Target hit problem:** choose a time t that matches a required horizontal displacement, then check whether the vertical position at that time matches the target height.

## Common mistakes

- Using the equal-height range formula when launch and landing heights differ.
- Forgetting that g is a magnitude while a_y = -g is a signed acceleration (for y positive upward).
- Mixing degrees and radians when using a calculator for sine and cosine.
- Treating horizontal velocity as changing under gravity (in the no-air-resistance model, horizontal velocity is constant).
- Taking a square root in a time-of-flight calculation and forgetting that only nonnegative times are physical.

## Worked example

A ball is thrown from ground level at speed:

$v_0 = 20\,\text{m/s}$

at an angle:

$\theta = 40^\circ$

above the horizontal. Neglect air resistance and take:

$g = 9.8\,\text{m/s}^2.$

Find:

1) time of flight,  
2) maximum height,  
3) range.

### Step 1: Resolve the initial velocity into components

$v_x(0) = v_0\cos\theta = 20\cos 40^\circ,$

$v_y(0) = v_0\sin\theta = 20\sin 40^\circ.$

Numerically:

$$
v_x(0) \approx 20(0.766) \approx 15.3\,\text{m/s},
$$

$$
v_y(0) \approx 20(0.643) \approx 12.9\,\text{m/s}.
$$

### Step 2: Time of flight (same launch and landing height)

Use:

$$
t_f = \frac{2v_0\sin\theta}{g} = \frac{2(20)\sin 40^\circ}{9.8}.
$$

Numerically:

$$
t_f \approx \frac{40(0.643)}{9.8} \approx \frac{25.7}{9.8} \approx 2.62\,\text{s}.
$$

### Step 3: Maximum height

Use:

$$
y_{\text{max}} = \frac{(v_0\sin\theta)^2}{2g}.
$$

Numerically:

$$
y_{\text{max}} \approx \frac{(12.9)^2}{19.6} \approx \frac{166}{19.6} \approx 8.47\,\text{m}.
$$

### Step 4: Range

Use either:

$R=v_x t_f$

or the range formula. Using:

$R=v_x t_f,$

$$
R \approx (15.3)(2.62) \approx 40.1\,\text{m}.
$$

### Step 5: Quick checks

- Units: time in seconds, height and range in meters.
- Reasonableness: the ball is in the air a few seconds and travels tens of meters—consistent with a 20 m/s throw.

## Mini recap

- Choose axes with y upward, then:

$a_x=0, \qquad a_y=-g.$

- Component solutions:

$x(t)=x_0+(v_0\cos\theta)t,$

$$
y(t)=y_0+(v_0\sin\theta)t-\frac{1}{2}gt^2.
$$

- Trajectory equation:

$$
y = y_0 + (x-x_0)\tan\theta - \frac{g}{2v_0^2\cos^2\theta}(x-x_0)^2.
$$

- Equal-height special results:

$$
t_f=\frac{2v_0\sin\theta}{g}, \qquad R=\frac{v_0^2}{g}\sin(2\theta), \qquad y_{\text{max}}=y_0+\frac{(v_0\sin\theta)^2}{2g}.
$$

<!-- SOURCE: lecture/kinematics/18_uniform_circular_motion.md -->

# Uniform circular motion

## Learning goals

- Explain why an object can have nonzero acceleration even when its speed is constant.
- Describe uniform circular motion using radius, angular position, angular speed, period, and frequency.
- Relate speed to angular speed and radius, and compute centripetal (inward) acceleration magnitude.
- Solve basic “car on a circular track / rotating object” problems with consistent units.

## Why this matters

Uniform circular motion is the simplest example that breaks the misconception:

“If speed is constant, acceleration must be zero.”

In circular motion, speed can be constant while the velocity vector changes direction continuously. This is the key intuition that later supports the dynamics idea of a required inward net force for circular motion.

## Core idea

Uniform circular motion means:

- the trajectory is a circle of radius R,
- the speed v is constant,
- direction changes continuously, so velocity changes,
- acceleration points toward the center (inward) even though speed is constant.

## Mathematical formulation

### Angular position, angular speed, period, frequency

Let theta(t) be the angular position (in radians) measured from some reference direction. Uniform circular motion means angular speed is constant:

$$
\omega = \frac{d\theta}{dt} = \text{constant}.
$$

Then:

$\theta(t) = \theta_0 + \omega t.$

The period T is the time for one full revolution (2pi radians):

$$
T = \frac{2\pi}{\omega}.
$$

The frequency f (revolutions per second, Hz) is:

$$
f = \frac{1}{T}.
$$

So:

$\omega = 2\pi f.$

### Speed and tangential velocity

The arc length traveled in time t is s = R theta. Differentiate:

$$
v = \frac{ds}{dt} = R\frac{d\theta}{dt} = R\omega.
$$

Velocity direction is tangent to the circle, so the velocity vector is tangential.

### Centripetal (inward) acceleration magnitude

Even though speed is constant, the velocity direction changes. The resulting acceleration points inward and has magnitude:

$$
a = \frac{v^2}{R}.
$$

Using v = R omega, this can also be written as:

$a = R\omega^2.$

These formulas give the magnitude. The direction is toward the center of the circle.

## Interpretation

- Constant speed does not imply constant velocity. In circular motion, the velocity vector “rotates.”
- Acceleration in uniform circular motion is perpendicular to the velocity (it changes direction of motion, not speed).
- The acceleration magnitude grows quickly with speed: doubling v makes a four times larger.

## Typical examples

1) **Car on a circular track:** compute required inward acceleration (and later, in dynamics, the required inward net force).

2) **Object on a rotating turntable:** relate rotation rate (rev/s) to angular speed and then to tangential speed.

3) **Satellite in circular orbit (idealized):** uniform circular motion provides a first kinematic description; dynamics later provides the cause.

## Common mistakes

- Thinking “constant speed” means “no acceleration.”
- Using degrees for theta and omega in formulas derived for radians. (In v = R omega and a = R omega^2, omega must be in rad/s.)
- Confusing R (radius) with “range” from projectile motion.
- Plugging into a = v^2 / R with inconsistent units (e.g., km/h and meters).
- Saying “centripetal force” in a kinematics section. Here we only talk about acceleration; forces belong to dynamics.

## Worked example

A car drives around a flat circular track of radius:

$R = 50\,\text{m}.$

Its speed is constant:

$v = 15\,\text{m/s}.$

Find:

1) the magnitude of the centripetal acceleration,  
2) the period T,  
3) the frequency f.

### Step 1: Centripetal acceleration

Use:

$$
a = \frac{v^2}{R}.
$$

So:

$$
a = \frac{(15)^2}{50} = \frac{225}{50} = 4.5\,\text{m/s}^2.
$$

### Step 2: Period from speed

One revolution distance is the circumference:

$2\pi R.$

At constant speed, time for one revolution is:

$$
T = \frac{2\pi R}{v} = \frac{2\pi(50)}{15}.
$$

Numerically:

$$
T \approx \frac{314}{15} \approx 20.9\,\text{s}.
$$

### Step 3: Frequency

$$
f = \frac{1}{T} \approx \frac{1}{20.9} \approx 0.0478\,\text{Hz}.
$$

### Optional: Angular speed

$$
\omega = \frac{v}{R} = \frac{15}{50} = 0.30\,\text{rad/s}.
$$

Check consistency:

$$
T = \frac{2\pi}{\omega} \approx \frac{2\pi}{0.30} \approx 20.9\,\text{s},
$$

same as before.

## Mini recap

- Uniform circular motion: circle of radius R, constant speed v, changing velocity direction.
- Angular relations:

$$
\theta(t)=\theta_0+\omega t, \qquad T=\frac{2\pi}{\omega}, \qquad \omega=2\pi f.
$$

- Speed and inward acceleration magnitudes:

$$
v=R\omega, \qquad a=\frac{v^2}{R}=R\omega^2.
$$

- Acceleration points inward; it changes direction of velocity, not its magnitude.

<!-- SOURCE: lecture/kinematics/19_tangential_and_normal_acceleration.md -->

# Tangential and normal acceleration

## Learning goals

- Decompose acceleration into a part that changes speed (tangential) and a part that changes direction (normal).
- Use the relations for tangential and normal acceleration in common situations.
- Connect curvature (radius of curvature) to the required normal acceleration for a given speed.
- Interpret motion qualitatively: “speeding up vs turning” and how both can happen at once.

## Why this matters

Acceleration is often misunderstood as “the thing that makes you go faster.” In 2D motion, acceleration has two independent roles:

- it can change the magnitude of the velocity (speed),
- it can change the direction of the velocity.

The tangential/normal decomposition is a clean way to separate these roles. It also creates a direct bridge between kinematics (geometry of motion) and dynamics (required forces) later.

## Core idea

At each instant, the velocity vector points along the tangent to the trajectory. Acceleration can be split into:

- a tangential component (along the velocity direction) that changes speed,
- a normal component (perpendicular to velocity, toward the center of curvature) that changes direction.

Uniform circular motion is the special case where speed is constant, so tangential acceleration is zero and only normal acceleration remains.

## Mathematical formulation

Let v = |\vec{v}| be the speed. At any instant, define:

- \hat{t}: unit vector tangent to the trajectory (direction of \vec{v}),
- \hat{n}: unit vector normal to the trajectory pointing toward the center of curvature.

Then acceleration decomposes as:

$\vec{a} = a_t \hat{t} + a_n \hat{n}.$

### Tangential acceleration (changes speed)

The tangential component equals the time rate of change of speed:

$$
a_t = \frac{dv}{dt}.
$$

So if speed is constant, dv/dt = 0 and:

$a_t = 0.$

### Normal acceleration (changes direction)

If the trajectory has instantaneous radius of curvature R, then the normal component has magnitude:

$$
a_n = \frac{v^2}{R}.
$$

Its direction is toward the center of curvature (inward for circular motion).

For uniform circular motion, R is the circle radius and a_n is the centripetal acceleration from the previous section.

### Combining magnitudes (perpendicular components)

Since the tangential and normal directions are perpendicular, the acceleration magnitude is:

$$
|\vec{a}| = \sqrt{a_t^2 + a_n^2}.
$$

## Interpretation

- If \vec{a} is parallel to \vec{v}, the particle changes speed but not direction (purely tangential acceleration; straight-line motion).
- If \vec{a} is perpendicular to \vec{v}, the particle changes direction but not speed (purely normal acceleration; uniform circular motion locally).
- In general, both can occur simultaneously: a car can speed up while turning.

The normal component grows like v^2, so at higher speeds, even gentle turns require large normal acceleration.

## Typical examples

1) **Car turning at constant speed:** a_t = 0, a_n = v^2 / R.

2) **Car speeding up in a straight line:** a_n = 0, a_t = dv/dt.

3) **Car accelerating through a curve:** both a_t ≠ 0 and a_n ≠ 0.

## Common mistakes

- Saying “acceleration is toward the center” for all curved motion. Only the normal component is toward the center of curvature; there can also be a tangential component.
- Using a_n = v^2 / R with R misunderstood (it is radius of curvature, not “distance to origin”).
- Confusing a_t with dv_x/dt or dv_y/dt. Tangential acceleration is about speed v, not a particular coordinate component.
- Forgetting that a_t can be negative (speed decreasing) even if the object is still moving forward.

## Worked example

A car moves along a curved road. At a certain instant:

- its speed is:

$v = 20\,\text{m/s},$

- its speed is increasing at a rate:

$$
\frac{dv}{dt} = 1.5\,\text{m/s}^2,
$$

- the radius of curvature of the road at that point is:

$R = 80\,\text{m}.$

Find:

1) a_t,  
2) a_n,  
3) the magnitude of the total acceleration.

### Step 1: Tangential component

By definition:

$$
a_t = \frac{dv}{dt} = 1.5\,\text{m/s}^2.
$$

### Step 2: Normal component

Use:

$$
a_n = \frac{v^2}{R} = \frac{(20)^2}{80} = \frac{400}{80} = 5.0\,\text{m/s}^2.
$$

### Step 3: Total acceleration magnitude

Perpendicular components combine via Pythagoras:

$$
|\vec{a}| = \sqrt{a_t^2 + a_n^2} = \sqrt{(1.5)^2 + (5.0)^2}.
$$

Compute:

$$
|\vec{a}| = \sqrt{2.25 + 25} = \sqrt{27.25} \approx 5.22\,\text{m/s}^2.
$$

Interpretation: most of the acceleration is devoted to changing direction (normal component), while a smaller part changes speed.

## Mini recap

- Decomposition:

$\vec{a} = a_t \hat{t} + a_n \hat{n}.$

- Tangential part changes speed:

$$
a_t = \frac{dv}{dt}.
$$

- Normal part changes direction (radius of curvature R):

$$
a_n = \frac{v^2}{R}.
$$

- Total magnitude:

$$
|\vec{a}|=\sqrt{a_t^2+a_n^2}.
$$

<!-- SOURCE: lecture/kinematics/20_periodic_motion_intro.md -->

# Periodic motion (intro)

## Learning goals

- Define what it means for a motion to be periodic.
- Use the quantities period T, frequency f, and angular frequency omega, and convert between them.
- Recognize what “repeating state” means (position alone vs full state including velocity).
- Solve simple timing/counting questions for periodic motions (rotations, cycles, oscillations).

## Why this matters

Many systems in mechanics repeat patterns:

- rotating wheels,
- circular motion,
- oscillations (springs, pendulums, vibrations).

Before studying any particular model (like sinusoidal motion), you need a clear language for repetition: period, frequency, and phase-like ideas. This language also prevents unit mistakes (Hz vs rad/s, seconds vs cycles).

## Core idea

A motion is periodic if it repeats itself after a fixed time interval. The simplest definition uses a position function:

“The position repeats after time T.”

But often the full physical situation repeats only when both position and velocity repeat. For example, in many oscillations the object passes the same position twice per cycle with opposite velocity directions.

So you should be clear what is meant by “repeats” in a given context.

## Mathematical formulation

### Periodic position function

We say that position is periodic with period T if:

$x(t+T) = x(t)$

for all t in the interval of interest.

For vector motion (2D/3D):

$\vec{r}(t+T) = \vec{r}(t).$

### Period, frequency, angular frequency

- Period T: time for one full cycle (seconds).
- Frequency f: cycles per second (Hz):

$$
f = \frac{1}{T}.
$$

- Angular frequency omega: radians per second:

$$
\omega = 2\pi f = \frac{2\pi}{T}.
$$

These are different ways to describe the same “rate of repetition,” but the units are different.

### Counting cycles

If a motion has frequency f, then the number of cycles completed in time interval Delta t is:

$N = f\,\Delta t.$

If you know the period T instead:

$$
N = \frac{\Delta t}{T}.
$$

## Interpretation

- Frequency f tells you “how many cycles per second.”
- Angular frequency omega tells you “how many radians of phase per second” for motions that can be described by an angle-like phase.
- Period T is often easiest to visualize physically (“one cycle takes T seconds”).

Be careful: omega is not “revolutions per second.” It is radians per second. A wheel rotating at 1 revolution per second has omega = 2pi rad/s.

## Typical examples

1) **Uniform circular motion:** angle increases linearly with time; position repeats every revolution.

2) **A blinking light:** periodic intensity; a simple non-mechanical analogy.

3) **Back-and-forth oscillation:** position repeats every cycle, but a given position can occur twice per period with opposite velocity.

## Common mistakes

- Confusing frequency f (Hz) with angular frequency omega (rad/s).
- Forgetting the factor 2pi in omega = 2pi f.
- Saying “the motion repeats when it reaches the same position” without checking velocity direction (state may not repeat).
- Mixing “cycles” with “radians” in the same equation without conversion.

## Worked example

A wheel rotates uniformly. It makes 180 revolutions in 2 minutes.

Find:

1) the frequency f in Hz,  
2) the period T in seconds,  
3) the angular frequency omega in rad/s,  
4) how many radians the wheel rotates in 5 seconds.

### Step 1: Convert time and compute frequency

2 minutes is:

$120\,\text{s}.$

Frequency is revolutions per second:

$$
f = \frac{180}{120} = 1.5\,\text{Hz}.
$$

### Step 2: Period

$$
T = \frac{1}{f} = \frac{1}{1.5} \approx 0.667\,\text{s}.
$$

### Step 3: Angular frequency

$$
\omega = 2\pi f = 2\pi(1.5) = 3\pi \approx 9.42\,\text{rad/s}.
$$

### Step 4: Angle rotated in 5 seconds

Uniform rotation means angle increases linearly:

$$
\Delta\theta = \omega \Delta t = (3\pi)(5) = 15\pi \approx 47.1\,\text{rad}.
$$

Interpretation: 47.1 rad is about 7.5 revolutions, since 2pi rad is one revolution.

## Mini recap

- Periodic position: x(t+T) = x(t) (and similarly for vectors).
- Period, frequency, angular frequency:

$$
f=\frac{1}{T}, \qquad \omega = 2\pi f = \frac{2\pi}{T}.
$$

- Count cycles: N = f Delta t = Delta t / T.
- Always track units: Hz (cycles/s) vs rad/s.

<!-- SOURCE: lecture/kinematics/21_sinusoidal_motion.md -->

# Sinusoidal motion

## Learning goals

- Write a sinusoidal position function with clear meaning of amplitude, angular frequency, and phase.
- Differentiate to obtain velocity and acceleration, and interpret their signs and extrema.
- Relate angular frequency omega to period T and frequency f.
- Solve basic problems: given x(t), find v(t), a(t), and identify when the particle passes equilibrium or reaches extrema.

## Why this matters

Sinusoidal motion is a fundamental pattern in mechanics:

- small oscillations of springs and pendulums,
- vibrations,
- many waves in time.

Even before learning the dynamics that produces it, you can do a lot of kinematics:

- predict when the object is at maximum displacement,
- when it passes equilibrium,
- how velocity and acceleration relate to position.

This section is also a good test of your derivative skills and your interpretation of sign changes.

## Core idea

A sinusoidal position function repeats with a fixed period and has a smooth back-and-forth structure. A standard form is:

“equilibrium position + amplitude × cosine with a phase.”

The key qualitative facts (which you can later prove with derivatives) are:

- velocity is zero at position extrema,
- speed is maximal at equilibrium crossings,
- acceleration tends to point toward equilibrium (for the cosine form), so it is opposite in sign to displacement.

## Mathematical formulation

### Standard form

Use:

$x(t) = x_{\text{eq}} + A\cos(\omega t + \phi),$

where:

- x_eq is the equilibrium (center) position,
- A is the amplitude (maximum displacement from equilibrium),
- omega is the angular frequency (rad/s),
- phi is the phase constant (radians).

The period is:

$$
T = \frac{2\pi}{\omega},
$$

and frequency is:

$$
f = \frac{1}{T} = \frac{\omega}{2\pi}.
$$

### Velocity and acceleration

Differentiate:

$$
v(t) = \frac{dx}{dt} = -A\omega\sin(\omega t + \phi).
$$

Differentiate again:

$$
a(t) = \frac{dv}{dt} = -A\omega^2\cos(\omega t + \phi).
$$

Notice that:

$a(t) = -\omega^2\big(x(t)-x_{\text{eq}}\big).$

This relationship is a hallmark of sinusoidal motion and foreshadows the dynamics of a spring-like restoring influence.

### Useful times (extrema and equilibrium crossings)

Position extrema occur when:

$$
v(t)=0 \Rightarrow \sin(\omega t + \phi)=0.
$$

Equilibrium crossings occur when:

$$
x(t)=x_{\text{eq}} \Rightarrow \cos(\omega t + \phi)=0.
$$

These conditions let you find important events without plotting the whole function.

## Interpretation

- Amplitude A sets the largest displacement from equilibrium.
- Larger omega means faster oscillation (shorter period).
- Velocity is shifted in phase by 90 degrees relative to position (cosine vs sine).
- Acceleration is proportional to negative displacement from equilibrium:

$a = -\omega^2(x-x_{\text{eq}}).$

So when x is above equilibrium (positive displacement), acceleration is negative (toward equilibrium), and vice versa.

## Typical examples

1) **Mass on a spring (preview):** position oscillates sinusoidally about equilibrium.

2) **Small-angle pendulum (preview):** approximately sinusoidal in time for small oscillations.

3) **Vibrating machine component:** measured displacement vs time is often close to sinusoidal.

## Common mistakes

- Confusing omega (rad/s) with f (Hz). They differ by a factor 2pi.
- Using degrees for omega t + phi when taking sine/cosine (these functions assume radians in calculus contexts).
- Forgetting the chain rule: derivative of cos(omega t + phi) brings down a factor omega.
- Mixing up equilibrium position x_eq with amplitude A (they play different roles).
- Thinking acceleration is zero at equilibrium. In sinusoidal motion, acceleration is zero at equilibrium crossings only if the cosine form is centered and there is no offset; more generally use the formula a = -omega^2(x - x_eq).

## Worked example

A particle oscillates along a line with:

$x(t) = 0.20\cos(4t),$

where x is in meters and t in seconds.

Find:

1) the amplitude A, angular frequency omega, period T, and frequency f,  
2) velocity v(t) and acceleration a(t),  
3) the maximum speed,  
4) the first time t > 0 when the particle passes through equilibrium x = 0.

### Step 1: Identify parameters

Comparing with x(t) = x_eq + A cos(omega t + phi), we have:

$$
x_{\text{eq}}=0, \qquad A=0.20\,\text{m}, \qquad \omega = 4\,\text{rad/s}, \qquad \phi=0.
$$

Then:

$$
T = \frac{2\pi}{\omega} = \frac{2\pi}{4} = \frac{\pi}{2} \approx 1.57\,\text{s},
$$

$$
f = \frac{1}{T} \approx 0.637\,\text{Hz}.
$$

### Step 2: Differentiate for velocity and acceleration

$$
v(t) = -A\omega\sin(\omega t) = -(0.20)(4)\sin(4t) = -0.80\sin(4t)\,\text{m/s}.
$$

$$
a(t) = -A\omega^2\cos(\omega t) = -(0.20)(16)\cos(4t) = -3.2\cos(4t)\,\text{m/s}^2.
$$

### Step 3: Maximum speed

Maximum speed is the amplitude of v(t):

$v_{\text{max}} = A\omega = (0.20)(4) = 0.80\,\text{m/s}.$

### Step 4: First equilibrium crossing after t=0

Equilibrium means x(t)=0, so:

$$
0.20\cos(4t)=0 \Rightarrow \cos(4t)=0.
$$

The first positive time occurs at:

$$
4t = \frac{\pi}{2} \Rightarrow t = \frac{\pi}{8} \approx 0.393\,\text{s}.
$$

## Mini recap

- Standard sinusoidal position:

$x(t)=x_{\text{eq}} + A\cos(\omega t+\phi).$

- Period/frequency:

$$
T=\frac{2\pi}{\omega}, \qquad f=\frac{\omega}{2\pi}.
$$

- Velocity and acceleration:

$$
v(t)=-A\omega\sin(\omega t+\phi), \qquad a(t)=-A\omega^2\cos(\omega t+\phi)=-\omega^2(x-x_{\text{eq}}).
$$

- Velocity is zero at extrema; speed is maximal at equilibrium crossings.

<!-- SOURCE: lecture/kinematics/22_kinematics_summary.md -->

# Kinematics summary

## Learning goals

- Summarize what kinematics can and cannot do (describe motion, not its cause).
- Use the core relations linking position, velocity, and acceleration in 1D and vector form.
- Choose the right kinematic tool: differentiation, integration, graphs, or constant-acceleration formulas.
- Avoid the most common conceptual and sign errors.

## Why this matters

Kinematics is the language of motion. If you have a clean kinematics toolbox, you can:

- interpret data quickly,
- build correct equations in dynamics later,
- and check whether an answer is physically reasonable.

The goal of this summary is not to add new topics, but to connect the whole part into one coherent workflow.

## Core idea

Kinematics is built around three linked quantities:

- position: where the particle is,
- velocity: how position changes in time,
- acceleration: how velocity changes in time.

In 1D these are signed scalars. In 2D/3D they are vectors. In either case, the logical structure is the same:

$x(t) \rightarrow v(t) \rightarrow a(t)$

by differentiation, and:

$a(t) \rightarrow v(t) \rightarrow x(t)$

by integration plus initial conditions.

## Mathematical formulation

### Core definitions (1D)

$$
v(t) = \frac{dx}{dt}
$$

$$
a(t) = \frac{dv}{dt} = \frac{d^2x}{dt^2}
$$

Average values on an interval:

$$
v_{\text{avg}} = \frac{x(t_2)-x(t_1)}{t_2-t_1}
$$

$$
a_{\text{avg}} = \frac{v(t_2)-v(t_1)}{t_2-t_1}
$$

### Core definitions (vector form)

$$
\vec{v}(t) = \frac{d\vec{r}}{dt}
$$

$$
\vec{a}(t) = \frac{d\vec{v}}{dt} = \frac{d^2\vec{r}}{dt^2}
$$

Average velocity:

$$
\vec{v}_{\text{avg}} = \frac{\vec{r}(t_2)-\vec{r}(t_1)}{t_2-t_1}
$$

### Graph links (slope and area)

Slope:

$$
\text{slope of } x(t) \text{ is } v(t), \qquad \text{slope of } v(t) \text{ is } a(t).
$$

Area (signed):

$$
v(t_2)-v(t_1) = \int_{t_1}^{t_2} a(t)\,dt
$$

$$
x(t_2)-x(t_1) = \int_{t_1}^{t_2} v(t)\,dt
$$

### Constant acceleration (1D, model)

Assume:

$a(t) = a_0 \quad \text{(constant)}.$

Then:

$v(t) = v_0 + a_0(t-t_0)$

$$
x(t) = x_0 + v_0(t-t_0) + \frac{1}{2}a_0(t-t_0)^2
$$

and the time-free relation:

$v^2 = v_0^2 + 2a_0(x-x_0).$

### 2D motion via components

$\vec{r}(t) = x(t)\,\hat{i} + y(t)\,\hat{j}$

$\vec{v}(t) = v_x(t)\,\hat{i} + v_y(t)\,\hat{j}$

$\vec{a}(t) = a_x(t)\,\hat{i} + a_y(t)\,\hat{j}$

with:

$$
v_x=\frac{dx}{dt}, \quad v_y=\frac{dy}{dt}, \quad a_x=\frac{d^2x}{dt^2}, \quad a_y=\frac{d^2y}{dt^2}.
$$

### Circular and periodic highlights (kinematic identities)

Uniform circular motion:

$$
v = R\omega, \qquad a = \frac{v^2}{R} = R\omega^2.
$$

Period relations:

$$
T = \frac{2\pi}{\omega}, \qquad f=\frac{1}{T}, \qquad \omega = 2\pi f.
$$

## Interpretation

- Sign and direction: in 1D the sign of v tells direction; the sign of a tells how v changes, not “speeding up” by itself.
- Turning points: a turning time requires v = 0 and a sign change of v across that time.
- Displacement vs distance: displacement depends only on endpoints; distance traveled accumulates along the path and is not captured by x(t_2)-x(t_1) when direction reverses.
- Models have assumptions: constant-acceleration equations are powerful but only valid when acceleration is constant on the interval.

## Typical examples

1) Given x(t), find v(t) and a(t), locate rest times and turning points.

2) Given v(t) (or a(t)), integrate with initial conditions to get x(t).

3) Use graphs: find displacement from the area under v(t), find acceleration from slope of v(t).

4) Solve motion in 2D by separating x and y components, then recombine.

## Common mistakes

- Not stating a sign convention and then mixing “up positive” with “down positive.”
- Treating negative acceleration as “slowing down” without checking the velocity sign.
- Using distance when the formula requires displacement (especially in average velocity).
- Forgetting integration constants and initial conditions when reconstructing x(t) from v(t) or a(t).
- Applying constant-acceleration formulas to situations where acceleration varies (for example, strong air resistance).
- Inverse problems: not counting constraints vs unknown parameters and assuming uniqueness when data is insufficient.

## Worked example

A particle moves along a line. Its acceleration is piecewise constant:

- for 0 <= t <= 4 s:

$a(t) = 2.0\,\text{m/s}^2,$

- for 4 <= t <= 10 s:

$a(t) = -1.0\,\text{m/s}^2.$

At t = 0:

$x(0)=0, \qquad v(0)=0.$

Find:

1) v(t) and x(t) on both intervals,  
2) whether the particle turns around, and when,  
3) the final position x(10).

### Step 1: Interval 1 (0 to 4 s)

With constant acceleration a = 2:

$v(t) = v(0) + at = 2t.$

$$
x(t) = x(0) + v(0)t + \frac{1}{2}at^2 = t^2.
$$

Compute boundary values at t = 4:

$v(4)=2(4)=8\,\text{m/s},$

$x(4)=4^2=16\,\text{m}.$

### Step 2: Interval 2 (4 to 10 s)

Use the boundary values at t = 4 as initial conditions for the second interval. Let:

$\tau = t-4.$

On this interval, acceleration is a = -1:

$v(t) = v(4) + (-1)\tau = 8 - (t-4).$

So:

$v(t) = 12 - t.$

Position:

$$
x(t) = x(4) + v(4)\tau + \frac{1}{2}(-1)\tau^2
$$

$$
x(t) = 16 + 8(t-4) - \frac{1}{2}(t-4)^2.
$$

### Step 3: Check for a turning time

Turning time requires v(t) = 0. On interval 2:

$$
12 - t = 0 \Rightarrow t = 12\,\text{s}.
$$

But this is outside the modeled interval (t <= 10 s). Therefore, the particle does not turn around during 0 to 10 s.

### Step 4: Final position x(10)

Use the interval-2 position formula with t = 10:

$$
x(10) = 16 + 8(10-4) - \frac{1}{2}(10-4)^2.
$$

Compute:

$$
8(6)=48, \qquad \frac{1}{2}(6)^2 = 18.
$$

So:

$x(10) = 16 + 48 - 18 = 46\,\text{m}.$

## Mini recap

- Definitions:

$$
v=\frac{dx}{dt}, \qquad a=\frac{dv}{dt}.
$$

- Reconstruction:

$$
v(t)=v_0+\int_{t_0}^{t}a(\tau)\,d\tau, \qquad x(t)=x_0+\int_{t_0}^{t}v(\tau)\,d\tau.
$$

- Graphs: slope gives derivatives; signed area gives changes.
- Constant acceleration gives a linear v(t) and quadratic x(t), but only when the assumption is valid.
- Good kinematics is careful about frames, signs, units, and what is being modeled.

<!-- SOURCE: lecture/kinematics/23_kinematics_problem_set.md -->

# Kinematics Problem Set

## Purpose

Practice the full kinematics toolbox:

- definitions of x(t), v(t), a(t) and their meanings,
- differentiation and integration reconstruction,
- sign conventions, turning points, and “speed vs velocity,”
- graph reasoning (slope/area),
- 2D component methods (projectiles, relative motion),
- circular/periodic and sinusoidal motion.

Assume all motion is along a line unless a problem explicitly states 2D. Always choose a coordinate system and state your sign convention.

## Warm-up problems

1. A particle has position:

$x(t)=5-3t.$

Find v(t), a(t), and the displacement from t=1 s to t=4 s.

2. The position is:

$x(t)=2t^2-4t+1.$

Find v(t) and a(t). At what times (if any) is the particle instantaneously at rest?

3. A cyclist moves in 1D. At t=0: x=0 m. At t=8 s: x=120 m.  
Find the average velocity on [0,8]. Does this tell you the cyclist’s speed at t=4 s? Explain briefly.

4. A velocity sensor reports:

$v(t)=6.$

If x(0)=2 m, find x(t).

5. An accelerometer reports:

$a(t)=-2.$

If v(0)=5 m/s, find v(t). At what time does v become zero?

## Standard problems

1. Constant acceleration. A particle has:

$x(0)=0,\qquad v(0)=3\,\text{m/s},$

and constant acceleration:

$a=1.2\,\text{m/s}^2.$

Find x(5 s) and v(5 s).

2. Free fall (sign practice). Choose y upward. A ball is dropped from rest from a height 18 m.  
Find the time to hit the ground and the impact velocity. Use g=9.8 m/s^2.

3. Free fall (thrown upward). A ball is thrown upward from ground level with v_0=12 m/s.  
Find the time to reach maximum height, the maximum height, and the total time to return to the ground (neglect air resistance).

4. Velocity given. A particle has:

$v(t)=4t-2.$

If x(1)=3 m, find x(t). Then find the displacement from t=1 to t=3.

5. Acceleration given. A particle has:

$a(t)=6t.$

If v(0)=0 and x(0)=1 m, find v(t) and x(t).

6. Turning point reasoning. A particle moves with:

$x(t)=t^3-3t.$

For which times is the particle moving in the positive direction? Find all turning times and the corresponding positions.

7. 2D components (basic). A particle has:

$\vec{r}(t)=(2t)\hat{i}+(t^2)\hat{j}.$

Find \vec{v}(t), \vec{a}(t), and the speed at t=1 s.

8. Relative motion (1D). A train moves east at 20 m/s relative to the ground. A passenger walks west at 1.5 m/s relative to the train.  
Find the passenger’s velocity relative to the ground.

9. Uniform circular motion. A point on a wheel of radius R=0.30 m rotates with frequency f=2.5 Hz.  
Find omega, the tangential speed v, and the centripetal acceleration magnitude a.

## Multi-step problems

1. Piecewise motion (accelerate, cruise, brake). A car starts from rest at x(0)=0.

- From t=0 to t=5 s it accelerates with a=2.0 m/s^2.
- From t=5 to t=12 s it moves with constant velocity.
- From t=12 s onward it brakes with a=-3.0 m/s^2 until it stops.

Find:

a) v(t) and x(t) on each interval,  
b) the stopping time,  
c) the total distance traveled.

2. “Back and forth” with areas. The velocity graph is described as:

- v increases linearly from 0 to 6 m/s on 0<=t<=2 s,
- then stays constant at 6 m/s on 2<=t<=4 s,
- then decreases linearly from 6 m/s to -2 m/s on 4<=t<=7 s.

Assume x(0)=0. Find x(7), and find the turning time when the particle changes direction.

3. Inverse kinematics (fit a quadratic). Assume constant acceleration and t_0=0. A particle satisfies:

$x(0)=1\,\text{m},\qquad x(2)=9\,\text{m},\qquad v(2)=0.$

Find x(t), v(t), and a. Check your result by interpreting the turning time.

4. Projectile motion (same launch/landing height). A ball is launched from ground level with v_0=18 m/s at angle 35 degrees above horizontal. Neglect air resistance.

a) Find the time of flight.  
b) Find the maximum height.  
c) Find the range.

5. Projectile motion (different landing height). A ball is thrown from a balcony at height y_0=12 m with speed 16 m/s at angle 30 degrees above horizontal. Use g=9.8 m/s^2. Neglect air resistance.

a) Find the time when it hits the ground (y=0).  
b) Find the horizontal distance from the balcony at impact.  
c) Find the impact velocity components.

6. Tangential + normal acceleration. A car moves through a curve of radius R=60 m. At an instant its speed is v=22 m/s and dv/dt= -1.0 m/s^2.

a) Find a_t and a_n.  
b) Find the magnitude of the total acceleration.  
c) Is the car speeding up or slowing down at that instant?

7. Sinusoidal motion (kinematics only). A particle has:

$$
x(t)=0.15\cos(5t-\frac{\pi}{3}).
$$

a) Find v(t) and a(t).  
b) Find T and f.  
c) Find the first time t>0 when x(t)=0.

## Conceptual questions

1. In 1D, can a particle have v=0 and a not equal to 0 at the same instant? Give a physical example.

2. In 2D, can a particle have constant speed but nonzero acceleration? Explain without using forces.

3. What is the difference between displacement and distance traveled? Give a motion where the displacement is zero but the distance is not.

4. If x(t) is a straight line on a graph, what can you say about v(t) and a(t)? State both mathematically and in words.

5. A student says: “Negative acceleration means the object is slowing down.” What is missing from this statement? Provide a corrected version.

6. You are given a trajectory curve in the x–y plane. Does that determine the motion uniquely? What information is missing?

7. Two motions have the same trajectory circle. One completes a revolution in 2 s, the other in 4 s. Compare their speeds and centripetal accelerations.

8. In sinusoidal motion, why does velocity reach its maximum magnitude at equilibrium crossings?

## Challenge problems

1. (Mixed reconstruction) A particle has acceleration:

$a(t)=k\sin(\omega t),$

with constants k and omega. Given v(0)=0 and x(0)=0:

a) find v(t) and x(t),  
b) find the displacement over one full period T=2pi/omega,  
c) interpret whether the particle necessarily returns to x=0 after one period.

2. (Non-constant acceleration, still kinematics) A particle has:

$x(t)=t^2\sin t.$

a) find v(t) and a(t),  
b) find all times in 0<=t<=2pi when v(t)=0 (you may leave answers in implicit form),  
c) explain why finding turning points can be harder than finding where x(t)=0.

3. (Constraint/inverse) A particle moves in 1D. Assume x(t) is a cubic polynomial. You are told:

$x(0)=0,\qquad x(1)=2,\qquad v(0)=0,\qquad v(1)=0.$

a) find x(t),  
b) determine where (in time) the particle changes direction,  
c) compute the maximum position reached on 0<=t<=1.

<!-- SOURCE: lecture/dynamics/01_why_kinematics_is_not_enough.md -->

# Why kinematics is not enough

## Learning goals

- State clearly what kinematics provides (description of motion) and what it does not (cause/prediction from interactions).
- Explain why the same kinematic motion can be produced by different physical situations.
- Identify acceleration as the bridge quantity between kinematics and dynamics.
- Understand what question dynamics answers that kinematics cannot.

## Why this matters

Kinematics is powerful: if you know x(t) or r(t), you can compute v(t) and a(t), predict where the particle will be, and interpret graphs.

But kinematics alone cannot answer questions like:

- Why did the motion happen?
- What changes if we change the surface, the mass, or the interaction?
- What motion will occur if we specify the environment and how the object is pushed or pulled?

Those are the questions you actually care about in most real problems. To answer them, you need a way to connect motion to interactions. That connection is dynamics.

## Core idea

Kinematics describes motion as a function of time. Dynamics explains and predicts motion by modeling interactions.

The key bridge is acceleration:

- In kinematics, acceleration can be given or measured and treated as input.
- In dynamics, acceleration is not “chosen.” It is determined by the net effect of interactions, represented by forces.

So the overall pipeline becomes:

$$
\text{interactions} \rightarrow \vec{F}_{\text{net}} \rightarrow \vec{a}(t) \rightarrow \vec{v}(t) \rightarrow \vec{r}(t).
$$

Kinematics handles the right side (a to v to r). Dynamics supplies the left side (forces giving a).

## Mathematical formulation

In kinematics, the core relations are definitions:

$$
\vec{v}(t) = \frac{d\vec{r}}{dt}, \qquad \vec{a}(t) = \frac{d\vec{v}}{dt}.
$$

These relations allow you to go from r(t) to v(t) to a(t), and by integration (with initial conditions) back again.

But nowhere in kinematics is there a rule that tells you what a(t) should be in a given physical situation. Many different a(t) are mathematically possible.

Dynamics adds an additional principle (developed carefully in later sections) that connects interaction models to acceleration. In its simplest form for a particle it is:

$$
\sum \vec{F} = m\vec{a}.
$$

This is the step that makes mechanics predictive: if you can model the forces, you can determine a(t), then use kinematics to determine the motion.

## Interpretation

### Same motion, different causes

Suppose you observe that a cart moves with constant acceleration a = 1.0 m/s^2 along a track. Kinematics can describe:

$$
v(t) = v_0 + at, \qquad x(t) = x_0 + v_0 t + \frac{1}{2}at^2.
$$

But kinematics does not tell you why a is 1.0. Several physically different situations could produce the same acceleration:

- a constant engine thrust with negligible friction,
- a cart on a slight incline,
- a spring pulling near a point where its force is approximately constant over a short distance,
- a combination of forces that happens to result in the same net effect.

Dynamics is the part of the course that teaches you how to build the force model and check which situations are consistent with the motion.

### Prediction requires a model of interaction

If you change the conditions (rougher surface, heavier load, different incline angle), kinematics alone cannot tell you what will happen next, because it has no “inputs” representing those physical changes.

Dynamics introduces those inputs through interaction models (forces), and then computes the acceleration.

## Typical examples

1) **Sliding block:** Kinematics can describe the measured motion down a table. Dynamics explains the motion difference between smooth and rough surfaces via friction.

2) **Car braking:** Kinematics describes the deceleration. Dynamics connects the deceleration to braking force and tire-road interaction, which change with road conditions.

3) **Circular motion:** Kinematics says that motion at constant speed in a circle requires inward acceleration a = v^2/R. Dynamics asks: what interaction provides the inward net force?

## Common mistakes

- Treating “force” as a synonym for “motion” (as if motion itself requires a force).
- Thinking that knowing x(t) automatically tells you what forces acted. It tells you a(t), but many force scenarios can produce the same a(t).
- Assuming acceleration is always “something you choose” rather than something that can be determined by the situation.
- Mixing levels: using dynamic ideas (forces) without first doing the kinematic step of identifying v and a.

## Worked example

You observe a cart moving along a line. Its position is measured (or fitted) as:

$x(t) = 2 + 3t + 0.50t^2$

with x in meters and t in seconds.

1) Use kinematics to find v(t) and a(t).  
2) Show explicitly why kinematics alone cannot identify the physical cause of the motion.  
3) If the cart has mass m = 4.0 kg, compute the required net force in the simplest Newtonian model.

### Step 1: Compute v(t) and a(t)

Differentiate:

$$
v(t) = \frac{dx}{dt} = 3 + 1.0t.
$$

Differentiate again:

$$
a(t) = \frac{dv}{dt} = 1.0.
$$

So the acceleration is constant:

$a = 1.0\,\text{m/s}^2.$

### Step 2: Why the cause is not determined by kinematics

From the data, you can say what acceleration occurred, but you cannot uniquely say what physical situation produced it. For example, both of the following could be consistent:

- A horizontal push that results in a constant net force (after friction is accounted for).
- A cart on an incline with no other forces along the track (gravity component providing constant acceleration).

Many other combinations are possible. Kinematics does not include “incline angle,” “friction coefficient,” or “engine force” as inputs, so it cannot choose among these causes.

### Step 3: The net force in the simplest dynamic model

If you now adopt Newton’s second law as a model for particle motion, then:

$F_{\text{net}} = ma = (4.0)(1.0) = 4.0\,\text{N}.$

This is still not a complete force analysis (it does not tell you which individual forces sum to 4.0 N), but it is already a dynamics statement: it connects the observed acceleration to a required net interaction.

## Mini recap

- Kinematics describes motion: r(t), v(t), a(t) and their relations.
- Kinematics does not determine a(t) from physical conditions; many different causes can produce the same motion.
- Dynamics introduces interaction models (forces) to determine acceleration:

$$
\sum \vec{F} = m\vec{a}.
$$

- Acceleration is the bridge: dynamics determines it; kinematics integrates it into motion.

<!-- SOURCE: lecture/dynamics/02_concept_of_force.md -->

# Concept of force

## Learning goals

- Describe force as a model of interaction (not “stored motion” and not a mysterious cause).
- Explain why force is a vector quantity and how forces combine.
- Distinguish common interaction types: contact forces and long-range forces.
- Use units correctly (newton) and interpret what a force measurement means operationally.

## Why this matters

Dynamics is built around one central question:

Given a physical situation, what acceleration will occur?

To answer that, we need a language for interactions. Force is that language in Newtonian mechanics. But the word “force” comes with many misconceptions, so we start with a careful, operational meaning:

- a force is something you can infer from interaction effects and measure with instruments,
- it has direction as well as magnitude,
- and multiple forces can act at the same time.

## Core idea

Force is a model for an interaction between bodies (or between a body and an environment). Examples:

- a hand pushes a cart (contact interaction),
- Earth attracts a ball (gravitational interaction),
- a stretched spring pulls (elastic interaction),
- a surface resists penetration and may resist sliding (normal and friction interactions).

The same body can experience several interactions at once. Dynamics is about accounting for all of them and combining them into a net effect.

## Mathematical formulation

### Force as a vector

Force has magnitude and direction, so we represent it by a vector:

$\vec{F}.$

In 2D (Cartesian axes), we write:

$\vec{F} = F_x\hat{i} + F_y\hat{j}.$

### Combining forces (vector addition)

If several forces act on the same particle, the combined effect is represented by vector addition:

$\vec{F}_{\text{net}} = \vec{F}_1 + \vec{F}_2 + \cdots$

Component-wise, this means:

$$
F_{\text{net},x} = F_{1x} + F_{2x} + \cdots, \qquad F_{\text{net},y} = F_{1y} + F_{2y} + \cdots
$$

This is not yet Newton’s second law; it is how we represent multiple interactions as one net interaction vector.

### Units: newton

The SI unit of force is the newton (N). In Newtonian mechanics it is convenient to remember the dimensional meaning:

$1\,\text{N} = 1\,\text{kg}\cdot\text{m/s}^2.$

Later, when we connect force to acceleration, this unit relationship becomes natural rather than a definition to memorize.

## Interpretation

### Operational meaning (what “measuring a force” means)

A spring scale does not “detect a force in space.” It measures an interaction: the tension in the spring required to maintain a certain extension. The reading depends on the situation, including whether the object is accelerating.

So force is not a property that an isolated object “has.” Force arises from interactions.

### Force is not velocity

Velocity describes how position changes. Force models interaction; it will be connected to acceleration later.

You can have:

- nonzero velocity with zero net force (constant-velocity motion in an inertial frame),
- zero velocity with nonzero net force (an instant at a turning point),
- nonzero net force with changing direction only (uniform circular motion: speed constant but direction changes).

These examples show why “force = motion” is not a correct mental model.

## Typical examples

1) Contact push/pull: a person pushes a box. The direction is the push direction; the magnitude depends on how hard they push and the interaction details.

2) Gravity: a ball near Earth experiences a downward gravitational force. (The detailed model is handled later in the “weight” section.)

3) Spring: a stretched spring pulls back toward its equilibrium length.

4) Rope tension: an ideal rope pulls along its length, not sideways.

## Common mistakes

- Thinking that “motion requires force” (a misconception corrected formally with Newton’s first law later).
- Treating force as a scalar and adding magnitudes without direction.
- Thinking that the force on an object is always in the direction the object is moving.
- Confusing the name of a force with a formula (for example, thinking “friction is always mu N” even when static friction can be smaller).
- Forgetting to specify which object the force is acting on. A force is always “force on this body due to that interaction.”

## Worked example

Two horizontal forces act on a puck on a frictionless table. Choose x to the east and y to the north.

- Force 1 is 6 N east.
- Force 2 is 8 N north.

Find the net force vector, its magnitude, and its direction.

### Step 1: Write forces as vectors in components

$\vec{F}_1 = 6\,\hat{i}, \qquad \vec{F}_2 = 8\,\hat{j}.$

### Step 2: Add to get the net force

$$
\vec{F}_{\text{net}} = \vec{F}_1 + \vec{F}_2 = 6\,\hat{i} + 8\,\hat{j}.
$$

So the components are:

$F_{\text{net},x}=6\,\text{N}, \qquad F_{\text{net},y}=8\,\text{N}.$

### Step 3: Magnitude

$$
|\vec{F}_{\text{net}}| = \sqrt{6^2 + 8^2}\,\text{N} = \sqrt{100}\,\text{N} = 10\,\text{N}.
$$

### Step 4: Direction

Let theta be the angle measured from +x toward +y. Then:

$$
\tan\theta = \frac{8}{6} = \frac{4}{3}.
$$

So:

$$
\theta = \arctan\left(\frac{4}{3}\right) \approx 53.1^\circ.
$$

Interpretation: the net interaction points northeast, 53.1 degrees above the +x axis.

## Mini recap

- Force is a vector model of interaction:

$\vec{F}.$

- Multiple forces combine by vector addition:

$$
\vec{F}_{\text{net}} = \sum \vec{F}.
$$

- Units:

$1\,\text{N} = 1\,\text{kg}\cdot\text{m/s}^2.$

- Keep track of direction, components, and “force on which object due to what.”

<!-- SOURCE: lecture/dynamics/03_interactions_and_models.md -->

# Interactions and models

## Learning goals

- Explain why mechanics requires modeling choices (what is included, what is neglected).
- Identify bodies, interactions, and the system boundary in a given situation.
- Choose an appropriate idealization (particle model, rigid surface, massless rope, etc.) and state assumptions explicitly.
- Understand how modeling choices determine which forces appear in the equations of motion.

## Why this matters

In real life, every object interacts with many things at once: air, supports, friction, internal parts, and more. If we tried to include everything, most problems would be impossible to solve.

Mechanics works because we build simplified models that keep the dominant effects and ignore the rest in a controlled way. The “art” of introductory dynamics is not advanced calculus; it is making good modeling choices and then applying Newton’s laws consistently.

## Core idea

A dynamics problem is always a modeling problem.

The general workflow is:

1) Decide what object(s) you will treat as your system.  
2) Decide what model you will use for each object (particle, rigid body, etc.).  
3) Identify external interactions acting on that system (forces).  
4) Write the equation(s) of motion and solve.

The system choice matters because forces are always “forces on the chosen system.” If you change the system boundary, the list of forces changes.

## Mathematical formulation

### System and environment

Choose a system S. External interactions are represented by forces on S due to objects outside S:

$\vec{F}_{\text{on S by environment}}.$

If you have multiple external interactions, you represent them as separate force vectors and sum them:

$$
\vec{F}_{\text{net, ext}} = \sum \vec{F}_{\text{ext}}.
$$

This net external force is what will appear in Newton’s second law for a particle system (later sections make this precise).

### Common idealizations (and what they imply)

Particle model:

- treat the object as a point with position vector:

$\vec{r}(t),$

- ignore rotation and size,
- keep only translational motion.

Rigid surface:

- surface does not deform significantly,
- contact forces can be represented by a normal force (and possibly friction).

Massless, inextensible rope (ideal string):

- rope has negligible mass,
- rope length does not change,
- tension is the same throughout a single rope segment (under common pulley idealizations).

Frictionless pulley:

- pulley does not dissipate energy,
- rope can slide without friction at the pulley,
- tension direction changes but magnitude is treated consistently.

Each assumption removes degrees of freedom or eliminates force terms that would otherwise appear.

### When “neglect” is justified

Neglecting a factor means:

- either it is small compared to other effects in the regime of interest,
- or it changes the result only slightly within acceptable error.

In an introductory course, the goal is to learn the dominant structure. Later courses refine the model when needed.

## Interpretation

- Modeling is not “cheating.” It is the core method of physics.
- A good model should be:
  - explicit about assumptions,
  - consistent with the question being asked,
  - testable against observation (even if only conceptually in homework).
- Two different models can both be useful if they apply to different regimes (for example, neglecting air resistance for slow, dense objects but not for a feather).

## Typical examples

1) Block on a table:

- system: the block,
- environment: Earth (gravity), table (normal, possibly friction), hand (push).

2) Two blocks connected by a rope:

- system can be one block at a time (to write separate equations),
- or both blocks together (to eliminate internal tension for certain questions).

3) Falling object:

- model A: free fall (neglect air resistance),
- model B: include drag force (acceleration not constant).

## Common mistakes

- Not stating assumptions and then mixing models (using “frictionless” in one step but including friction later).
- Confusing the system boundary: including an interaction force that is internal to the chosen system, or forgetting an external interaction.
- Treating “tension” or “normal force” as fixed formulas rather than forces determined by constraints and motion.
- Choosing a coordinate system that makes the algebra harder than necessary (addressed more in later dynamics sections).

## Worked example

A box is pulled across a horizontal floor by a rope at a fixed angle above the horizontal. You are asked to “find the acceleration.”

Before any equations, you must make modeling decisions. Here is a clean modeling setup.

### Step 1: Choose the system and model

System S: the box.

Model: particle (translational motion only), moving in the horizontal direction.

### Step 2: State assumptions

- The floor is rigid.
- The rope is light (massless) and does not stretch.
- Air resistance is neglected.
- Friction model: either frictionless floor or a kinetic friction coefficient is provided (you must choose based on the problem statement).

### Step 3: Identify external interactions (forces on the box)

Forces on the box include:

- gravitational force (downward),
- normal contact force from the floor (upward),
- rope tension along the rope direction,
- friction force along the floor (if friction is included), opposing the slipping direction.

At this stage you do not assign formulas like “normal equals mg.” You list the interactions first.

### Step 4: Choose axes consistent with the motion

Choose x horizontal, y vertical. Then each force can be resolved into x and y components, which later allows you to write:

$$
\sum F_x = m a_x, \qquad \sum F_y = m a_y.
$$

Since the box stays on the floor, you typically have:

$a_y = 0,$

which becomes a constraint that determines the normal force once the tension angle is known.

This example shows the main lesson: “writing equations” is not the first step. Identifying system, assumptions, and interactions is.

## Mini recap

- Dynamics problems require explicit modeling choices: system, assumptions, and interaction list.
- Forces are always “on the chosen system due to the environment.”
- Idealizations (particle, rigid surface, massless rope) simplify the force list and constraints.
- Good workflow: choose system → state assumptions → list forces → choose axes → write equations of motion.

<!-- SOURCE: lecture/dynamics/04_newtons_first_law.md -->

# Newton’s first law

## Learning goals

- State Newton’s first law in words and interpret it as a statement about inertial motion.
- Understand inertia: why “no net force” corresponds to constant velocity, not necessarily rest.
- Use the net force concept correctly (distinguish individual forces from their sum).
- Recognize and correct the misconception “motion requires force.”

## Why this matters

Newton’s first law is the conceptual foundation of dynamics. It tells you what “no interaction effect” means:

- not “no motion,” but “no change in velocity.”

Without this idea, you will consistently invent extra forces (“force of motion,” “force in the direction of travel”) to match intuition, and your later free-body diagrams will be wrong.

## Core idea

There are two different questions:

1) What is the velocity right now?  
2) Is the velocity changing?

Newton’s first law is about the second question. It introduces the idea of a special kind of reference frame (inertial) in which the natural state of motion is constant velocity.

Inertia is the tendency of a body to maintain its current velocity unless interactions produce a net effect.

## Mathematical formulation

Newton’s first law (in an inertial frame) can be stated as:

If the net external force on a body is zero, then the body’s velocity is constant.

In symbols:

$$
\sum \vec{F} = \vec{0} \Rightarrow \vec{v} = \text{constant}.
$$

Equivalently, constant velocity implies zero acceleration:

$$
\vec{v} = \text{constant} \Rightarrow \vec{a} = \vec{0}.
$$

In a Newtonian framework, “zero net force” and “zero acceleration” go together. The second law will later make the quantitative connection.

## Interpretation

### Rest and constant-velocity motion are the same dynamic state

Rest is just the special case of constant velocity with:

$\vec{v}=\vec{0}.$

From the viewpoint of dynamics, “at rest” and “moving at constant velocity” are equivalent in the sense that neither requires a net force.

That is why a puck on a nearly frictionless table continues moving without needing a continuous push once it is already moving.

### Net force, not individual forces

Newton’s first law is about the sum of forces. You can have multiple nonzero forces and still have zero net force if they balance.

Example (conceptual):

- gravity pulls downward,
- the table pushes upward with a normal force,
- if these two balance, vertical net force is zero.

The object can still move horizontally at constant velocity while these vertical forces exist.

### What the law does not say

- It does not say that a body with zero net force must be at rest.
- It does not say that if the body is moving, there must be a force in the direction of motion.
- It does not say that “forces always come in pairs on the same body.” (That is a separate idea: Newton’s third law.)

## Typical examples

1) Puck on ice: once sliding, it continues approximately at constant velocity because friction is small.

2) Elevator at constant speed: forces are not zero, but net force is zero (tension balances weight), so acceleration is zero.

3) Car cruising at constant speed on level road: engine thrust and drag/friction forces can balance so net force is zero.

## Common mistakes

- Thinking “if it’s moving, a force must point in the direction of motion.”
- Confusing “no force” with “no net force.”
- Treating friction as always present and always the same size, then claiming first-law motion is impossible. In reality, the first law describes an ideal limit and is approximately true when resistive forces are small or balanced by other forces.
- Drawing a free-body diagram that includes a “force of motion” to explain constant velocity.

## Worked example

A crate is pulled across a floor at constant velocity. The rope pulls horizontally with tension magnitude:

$T = 50\,\text{N}.$

The crate’s motion is constant velocity (so acceleration is zero). Assume the only horizontal forces are tension (forward) and kinetic friction (backward).

1) What is the magnitude of the kinetic friction force?  
2) What is the net horizontal force?

### Step 1: Use constant velocity to infer zero acceleration

Constant velocity implies:

$a_x = 0.$

Newton’s first law (or the “no change in velocity means no net force” idea) tells you:

$F_{\text{net},x} = 0.$

### Step 2: Write the force balance in x

Let friction magnitude be f_k, acting opposite the motion. Then:

$T - f_k = 0.$

So:

$f_k = T = 50\,\text{N}.$

### Step 3: Net force

$F_{\text{net},x} = T - f_k = 0.$

Interpretation: the crate can move at constant speed even though forces act, as long as they balance.

## Mini recap

- In an inertial frame:

$$
\sum \vec{F} = \vec{0} \Rightarrow \vec{v}=\text{constant}.
$$

- Rest is a special case of constant velocity.
- The first law is about net force, not the absence of forces.
- If velocity is constant, you do not add a “force of motion” to explain it; you look for balanced forces.

<!-- SOURCE: lecture/dynamics/05_inertial_frames.md -->

# Inertial frames

## Learning goals

- Define an inertial frame as a reference frame where Newton’s first law holds.
- Explain why Newton’s laws are simplest and most reliable in inertial frames.
- Connect inertial frames to relative motion (constant-velocity frames are inertial relative to each other).
- Recognize non-inertial effects qualitatively (why “extra forces” appear in accelerating frames).

## Why this matters

Newton’s laws are not statements about “all viewpoints.” They are statements about motion in special frames of reference.

If you apply Newton’s laws in a frame that is accelerating (like a turning car), you will see apparent effects that look like forces even when there is no physical interaction producing them. Understanding inertial frames prevents confusion and helps you choose a frame that makes problems easiest.

## Core idea

An inertial frame is defined by a simple physical criterion:

In an inertial frame, a particle with zero net force moves at constant velocity.

So inertial frames are the frames in which “free” motion is straight-line, constant-speed motion.

In practice, a frame attached to the ground is often a good approximation to inertial for many lab-scale problems, but not always (for example, for very precise measurements or large-scale Earth rotation effects).

## Mathematical formulation

### Defining property (Newton’s first law)

In an inertial frame:

$$
\sum \vec{F} = \vec{0} \Rightarrow \vec{a}=\vec{0}.
$$

### Relation between inertial frames (Galilean transformation idea)

If two frames move at constant velocity relative to each other (no relative acceleration), then both are inertial. In 1D, if:

$x' = x - ut,$

with constant u, then differentiating gives:

$v' = v - u,$

and:

$a' = a.$

So acceleration is the same in both frames, which is why Newton’s laws keep the same form in any inertial frame.

### What changes in a non-inertial frame (qualitative)

If the frame itself accelerates, then acceleration measurements include the frame’s acceleration. In such a frame, Newton’s second law can still be used if you introduce additional “inertial forces” (also called pseudo-forces) that account for the frame acceleration.

At this stage, the key point is conceptual:

- inertial frame: no extra forces are needed,
- accelerating frame: you must either switch frames or include inertial forces.

## Interpretation

- Inertial frames are not defined by being “at rest.” They are defined by having no acceleration relative to other inertial frames.
- The statement “the laws of physics are the same in all inertial frames” is a powerful simplification of classical mechanics.
- Non-inertial frames can still be used, but you must be careful: apparent forces can appear (for example, in a turning car you feel pushed outward even though the physical acceleration is inward).

## Typical examples

1) Train moving at constant speed: a passenger can do mechanics inside the train as if they were at rest (approximately inertial) because the train is not accelerating.

2) Car that accelerates or turns: the car frame is non-inertial. Loose objects slide relative to the car, and naive application of Newton’s laws without correction leads to confusion.

3) Rotating merry-go-round: objects appear to deflect relative to the rotating platform; describing this in the rotating frame requires inertial forces.

## Common mistakes

- Thinking “inertial” means “not moving.” Constant-velocity motion is inertial.
- Forgetting that the ground is only approximately inertial (usually good enough in intro problems).
- Applying Newton’s laws in an accelerating frame without adding inertial forces or without switching to an inertial frame.
- Treating inertial forces as real interaction forces. They are a bookkeeping device tied to the choice of frame.

## Worked example

A person stands in a train that is moving at constant speed. The person drops a ball from rest relative to the train.

1) Describe the motion as seen from the train frame.  
2) Describe the motion as seen from the ground frame.  
3) Explain why both descriptions are consistent with Newton’s laws without introducing extra forces.

### Step 1: Train frame description (approximately inertial)

In the train frame, the ball is released with zero horizontal velocity (relative to the train) and experiences only gravity vertically. So it falls straight down and lands at the person’s feet (neglect air resistance).

### Step 2: Ground frame description (also inertial)

In the ground frame, at the moment of release the ball already has the train’s horizontal velocity. Gravity provides vertical acceleration, but there is no horizontal acceleration (again neglect air resistance). So the ball follows a projectile-like path: it moves forward while falling.

### Step 3: Why no contradiction

The two frames move at constant velocity relative to each other, so both are inertial. They agree on acceleration:

$a_x = 0, \qquad a_y = -g.$

They disagree on velocity (because of the constant shift u), but that does not affect the force–acceleration relation in Newtonian mechanics. This is why Newton’s laws have the same form in any inertial frame.

## Mini recap

- Inertial frame: a frame where Newton’s first law holds.
- Any constant-velocity frame relative to an inertial frame is also inertial.
- Accelerating frames are non-inertial and require extra inertial forces if you insist on using Newton’s laws in that frame.
- Choose frames strategically: inertial frames simplify dynamics.

<!-- SOURCE: lecture/dynamics/06_newtons_second_law.md -->

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

$1\,\text{N} = 1\,\text{kg}\cdot\text{m/s}^2.$

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

$m = 5.0\,\text{kg}$

is pulled along a horizontal surface by a horizontal force:

$F = 18\,\text{N}.$

The kinetic friction force magnitude is:

$f_k = 6.0\,\text{N},$

opposing the motion. Find:

1) the acceleration magnitude and direction,  
2) the net force.

### Step 1: Choose axes and list forces in the direction of motion

Choose x along the pull direction (positive). The horizontal forces are:

- +F (pull),
- -f_k (friction).

### Step 2: Compute net force in x

$F_{\text{net},x} = F - f_k = 18 - 6 = 12\,\text{N}.$

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

$\vec{F}_{\text{net}} = (12\,\text{N})\hat{i}.$

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

<!-- SOURCE: lecture/dynamics/07_equation_of_motion.md -->

# Equation of motion

## Learning goals

- Explain what an equation of motion is: a differential equation that determines the motion.
- Build an equation of motion from a force model using Newton’s second law.
- Understand the role of initial conditions in selecting a unique motion.
- Solve simple 1D equations of motion and interpret the result physically.

## Why this matters

The central product of dynamics is not “the net force” by itself. It is the equation that connects the force model to the time evolution of the system.

Once you have an equation of motion, kinematics becomes the method for turning that equation into x(t), v(t), and predictions.

So a good dynamics solution typically has this structure:

force model → equation of motion → solve → interpret.

## Core idea

Newton’s second law is:

$$
\sum \vec{F} = m\vec{a}.
$$

If you express forces as functions of time, position, or velocity, then \vec{a} becomes a function of the unknown motion, and you obtain a differential equation for \vec{r}(t).

In 1D, because:

$$
a(t)=\frac{d^2x}{dt^2},
$$

Newton’s second law becomes a second-order differential equation for x(t).

## Mathematical formulation

### General 1D structure

Suppose the net force along x is modeled as:

$F_{\text{net}} = F(x, v, t).$

Then Newton’s second law gives:

$$
m\frac{d^2x}{dt^2} = F\left(x, \frac{dx}{dt}, t\right).
$$

This is an equation of motion. It determines x(t) once you supply two initial conditions (typically x(t_0) and v(t_0)).

### Special simple cases

1) Constant net force (or approximately constant):

$$
F_{\text{net}} = F_0 \quad \Rightarrow\quad m\frac{d^2x}{dt^2} = F_0.
$$

This implies constant acceleration:

$$
a = \frac{F_0}{m},
$$

so you recover the constant-acceleration kinematics formulas.

2) Net force proportional to velocity (a simple drag model):

$$
F_{\text{net}} = -bv \quad \Rightarrow\quad m\frac{dv}{dt} = -bv.
$$

This is a first-order equation for v(t) with an exponential solution (you will see this kind of structure again later).

3) Net force proportional to displacement (spring-like):

$$
F_{\text{net}} = -kx \quad \Rightarrow\quad m\frac{d^2x}{dt^2} = -kx.
$$

This produces sinusoidal motion (studied kinematically earlier), and dynamics explains why sinusoidal motion occurs.

## Interpretation

- The equation of motion is the mathematical expression of the force model plus Newton’s second law.
- It is usually a differential equation because acceleration involves derivatives of position.
- Two initial conditions are needed in 1D because the equation is second order: you must specify both where the particle is and how fast it is moving at some reference time.

The physics content is in the force model. The mathematics content is in solving the resulting differential equation.

## Typical examples

1) Block pulled with constant net force: equation of motion gives constant acceleration.

2) Falling with linear drag: equation of motion gives velocity approaching a terminal value.

3) Mass on a spring: equation of motion gives oscillations.

## Common mistakes

- Writing down kinematics formulas without first establishing a force model and equation of motion (in dynamics problems).
- Forgetting that forces may depend on x or v; assuming constant acceleration when the force model implies changing acceleration.
- Giving only one initial condition when solving a second-order equation for x(t).
- Mixing the variable meanings (using v for both a function v(t) and a constant without saying so).

## Worked example

A block of mass m slides on a horizontal frictionless surface. A constant horizontal force of magnitude F acts on it to the right. At t=0:

$x(0)=0,\qquad v(0)=0.$

1) Write the equation of motion.  
2) Solve for v(t) and x(t).  
3) Interpret the result and connect it back to constant-acceleration kinematics.

### Step 1: Force model

Frictionless surface means no friction force. Horizontally, the only force is the applied force:

$F_{\text{net}} = F.$

### Step 2: Equation of motion

Newton’s second law in 1D is:

$$
m\frac{d^2x}{dt^2} = F.
$$

So acceleration is constant:

$$
a = \frac{F}{m}.
$$

### Step 3: Solve for v(t)

Use:

$$
\frac{dv}{dt} = a = \frac{F}{m}.
$$

Integrate with v(0)=0:

$$
v(t) = \frac{F}{m}t.
$$

### Step 4: Solve for x(t)

Use:

$$
\frac{dx}{dt} = v(t) = \frac{F}{m}t.
$$

Integrate with x(0)=0:

$$
x(t) = \frac{F}{2m}t^2.
$$

### Step 5: Interpretation

- v(t) grows linearly in time, x(t) grows quadratically in time.
- This matches the kinematics of constant acceleration with:

$$
a = \frac{F}{m}.
$$

So the equation of motion method reproduces the familiar kinematics formulas, but now the acceleration is not an input; it is determined by the force model.

## Mini recap

- Force model + Newton’s second law produces an equation of motion:

$$
m\frac{d^2x}{dt^2} = F\left(x, \frac{dx}{dt}, t\right).
$$

- In 1D you typically need two initial conditions: x(t_0) and v(t_0).
- Solving the equation gives x(t), v(t), and predictions.
- Constant net force → constant acceleration; spring-like force → sinusoidal motion; drag-like force → exponential approach behavior.

<!-- SOURCE: lecture/dynamics/08_newtons_third_law.md -->

# Newton’s third law

## Learning goals

- State Newton’s third law and identify action–reaction force pairs correctly.
- Distinguish third-law pairs from “forces that balance” on a single object.
- Apply the third law to contact forces (normal, friction, tension) and to gravity.
- Avoid common misconceptions in multi-body problems.

## Why this matters

Newton’s third law is one of the most frequently misunderstood ideas in mechanics. Students often use it to “cancel” forces on a single object, which is almost always wrong.

The third law is not a rule about equilibrium. It is a rule about interactions between two bodies: forces come in mutual pairs, equal in magnitude and opposite in direction, acting on different objects.

Correct third-law thinking is essential for:

- building correct free-body diagrams,
- understanding tension and contact forces,
- solving connected-body and interaction problems.

## Core idea

Every interaction involves two bodies. If body A exerts a force on body B, then body B exerts a force on body A.

These two forces:

- have the same magnitude,
- have opposite directions,
- act on different bodies,
- occur at the same time.

## Mathematical formulation

Let \vec{F}_{A\to B} denote “force on B due to A.” Newton’s third law states:

$\vec{F}_{A\to B} = -\vec{F}_{B\to A}.$

Important: the two forces in the equation act on different objects (B and A respectively). That is why they do not cancel in a free-body diagram of a single object.

## Interpretation

### Third-law pairs vs balanced forces

- Third-law pair: forces between two bodies (A on B, B on A).
- Balanced forces: forces on the same body whose vector sum is zero.

Balanced forces are a condition for zero acceleration (Newton’s first/second law), not a direct consequence of the third law.

### Examples of third-law pairs (by interaction type)

Contact normal interaction:

- floor on box (upward normal on box),
- box on floor (downward normal on floor).

Friction interaction:

- floor on box (friction on box),
- box on floor (opposite friction on floor).

Gravity interaction:

- Earth on ball (gravitational force on ball),
- ball on Earth (equal and opposite gravitational force on Earth).

In many problems Earth’s acceleration is negligible because its mass is enormous, not because the third-law force “does not exist.”

## Typical examples

1) Person pushing a wall: the wall pushes back on the person with equal magnitude opposite direction. This is why the person feels the contact force.

2) Two blocks in contact: each block exerts a normal force on the other; those two forces are a third-law pair.

3) Rope tension: rope pulls on the block; the block pulls on the rope. Those are a third-law pair. (In an ideal rope, tensions at different points can be equal, but that is a separate modeling assumption.)

## Common mistakes

- Saying “action and reaction cancel, so there is no motion.” They act on different bodies, so they do not cancel in one object’s equation of motion.
- Pairing forces that act on the same body as a third-law pair (e.g., weight and normal on a block are not a third-law pair).
- Thinking the “bigger object exerts a bigger force.” The third law says the forces are equal in magnitude; differences in acceleration come from different masses and different net forces.
- Confusing “equal and opposite” with “balanced.” Equal and opposite can be balanced only if they act on the same object.

## Worked example

Two blocks A and B are in contact on a frictionless horizontal surface. A horizontal push is applied to block A, causing both blocks to accelerate to the right.

1) Identify the third-law pair associated with the contact between A and B.  
2) Explain why the contact forces do not cancel in the equation of motion for block B.

### Step 1: Identify the interaction forces

At the contact interface:

- block A pushes on block B (force on B due to A),
- block B pushes on block A (force on A due to B).

Call the force on B due to A:

$\vec{F}_{A\to B}.$

Then by Newton’s third law:

$\vec{F}_{B\to A} = -\vec{F}_{A\to B}.$

These two forces are a third-law pair.

### Step 2: Why there is no cancellation on block B

If you draw a free-body diagram for block B alone, you include forces acting on B. The contact force from A is one of them:

$\vec{F}_{A\to B}.$

But the reaction force \vec{F}_{B\to A} acts on A, not on B. Therefore it does not appear in B’s free-body diagram and cannot cancel \vec{F}_{A\to B} there.

So block B can accelerate because it experiences a net force to the right (provided by the contact with A).

## Mini recap

- Newton’s third law:

$\vec{F}_{A\to B} = -\vec{F}_{B\to A}.$

- Third-law forces act on different objects, so they do not cancel within a single free-body diagram.
- Do not confuse third-law pairs with balanced forces (net force zero on one body).
- Apply the rule to contact, friction, tension, and gravity interactions consistently.

<!-- SOURCE: lecture/dynamics/09_weight_and_gravitational_force.md -->

# Weight and gravitational force

## Learning goals

- Distinguish mass (property) from weight (force).
- Model near-Earth gravity as a constant downward force and use it correctly in free-body diagrams.
- Use sign conventions consistently for vertical motion (choose y up or y down and stick with it).
- Interpret “apparent weight” (scale reading) in accelerating situations.

## Why this matters

Confusing mass and weight is one of the fastest ways to break a dynamics solution. It leads to wrong units, wrong equations, and wrong intuition.

This section establishes a clean force model for gravity near Earth and shows how it appears in Newton’s second law problems (elevators, vertical acceleration, normal force contexts).

## Core idea

Mass m is a property of the object: it measures inertia.

Weight is a force: it is the gravitational force exerted on the object by Earth. Near Earth (for many intro problems), we model it as constant in magnitude and directed downward.

So:

- mass is measured in kg,
- weight is measured in N,
- weight depends on the gravitational environment and can change if g changes,
- mass does not change when you go to the Moon.

## Mathematical formulation

### Near-Earth gravity force model

Near Earth, gravitational force on a mass m is:

$\vec{W} = m\vec{g}.$

Here \vec{g} is the gravitational acceleration vector, pointing downward. Its magnitude is approximately:

$$
g \approx 9.8\,\text{m/s}^2.
$$

If you choose y positive upward, then:

$\vec{g} = -g\,\hat{j},$

so the weight force is:

$\vec{W} = -mg\,\hat{j}.$

### Weight vs “apparent weight”

A scale measures the normal force the scale exerts on you. That normal force is sometimes called apparent weight because it is what you feel as “heaviness.”

If you stand on a scale in an elevator, the vertical forces on you are:

- upward normal force N from the scale,
- downward weight mg.

Newton’s second law in y (taking y upward) is:

$N - mg = ma_y.$

So:

$N = m(g + a_y).$

This shows:

- if the elevator accelerates upward (a_y > 0), N > mg (you feel heavier),
- if it accelerates downward (a_y < 0), N < mg (you feel lighter),
- if it is in free fall (a_y = -g), N = 0 (weightless feeling).

## Interpretation

- Weight is the gravitational force on the object. It is always present near Earth regardless of motion.
- Apparent weight depends on acceleration because the normal force adjusts to produce the required net force.
- The symbol g is often used as the magnitude of gravitational acceleration; the sign comes from your coordinate choice.

## Typical examples

1) Object resting on a table: weight downward, normal upward. If acceleration is zero, these balance in y (but that is a net-force statement, not a third-law statement).

2) Elevator: same forces, but net force can be nonzero if accelerating.

3) Falling object with no contact: only weight acts (in the simple model), so acceleration is downward.

## Common mistakes

- Writing “m = mg” or treating g as a force.
- Mixing “g” as a magnitude and “-g” as a signed quantity in the same equation without stating the axis choice.
- Saying “weight changes when you accelerate.” The gravitational force mg does not change in the near-Earth model; the scale reading changes.
- Pairing weight and normal as a third-law pair (they act on the same object; third-law pairs act on different objects).

## Worked example

A person of mass:

$m = 70\,\text{kg}$

stands on a scale in an elevator. Take y upward and g = 9.8 m/s^2.

1) Find the scale reading when the elevator accelerates upward at 1.2 m/s^2.  
2) Find the scale reading when the elevator accelerates downward at 1.2 m/s^2.  
3) Compare both with the “at rest” reading.

### Step 1: Use the force balance equation

For the person:

$$
N - mg = ma_y \Rightarrow N = m(g + a_y).
$$

Compute mg:

$mg = (70)(9.8) = 686\,\text{N}.$

### Step 2: Accelerating upward

Here a_y = +1.2:

$N = 70(9.8 + 1.2) = 70(11.0) = 770\,\text{N}.$

### Step 3: Accelerating downward

Here a_y = -1.2:

$N = 70(9.8 - 1.2) = 70(8.6) = 602\,\text{N}.$

### Step 4: At rest / constant speed (a_y = 0)

$N = mg = 686\,\text{N}.$

Interpretation: the gravitational force mg is the same in all three cases, but the normal force (scale reading) changes because the acceleration changes.

## Mini recap

- Mass m (kg) is not weight.
- Weight is the gravitational force:

$\vec{W} = m\vec{g}.$

- A scale reads the normal force N, which depends on acceleration:

$$
N - mg = ma_y \Rightarrow N = m(g + a_y) \quad \text{(y upward)}.
$$

- “Heavier/lighter” in an elevator is about N, not about changing mg.

<!-- SOURCE: lecture/dynamics/10_normal_force.md -->

# Normal force

## Learning goals

- Interpret the normal force as a contact constraint force (surface response), not a fixed formula.
- Explain when N equals mg and when it does not.
- Set up Newton’s second law in the direction perpendicular to a surface to solve for N.
- Avoid common mistakes like assuming N = mg in all situations.

## Why this matters

The normal force appears in almost every contact problem: blocks on floors, inclines, elevators, and circular tracks.

Students often memorize “N = mg,” which is only true in special cases. In general, N is determined by the constraint “the object does not pass through the surface” and by the object’s acceleration relative to that surface.

If you get N wrong, you get friction wrong too, because many friction models use N.

## Core idea

The normal force is the force exerted by a surface on an object, perpendicular to the surface, preventing interpenetration.

Key points:

- N adjusts to whatever value is needed to satisfy the contact constraint.
- N can be larger than mg, smaller than mg, or even zero (loss of contact).
- N is not a third-law pair with weight; the third-law pair of N is the force the object exerts on the surface.

## Mathematical formulation

### Flat surface, vertical axis

Consider a block on a horizontal surface. Take y upward. Vertical forces are:

- N upward,
- weight mg downward.

Newton’s second law in y is:

$N - mg = ma_y.$

If the block has no vertical acceleration (a_y = 0), then:

$N = mg.$

This is the special case many students memorize, but it depends on the condition a_y = 0.

### Inclined surface (perpendicular direction)

For a block on an incline, the easiest method is to choose axes:

- one axis perpendicular to the plane,
- one axis parallel to the plane.

If the block stays in contact with the plane, its acceleration perpendicular to the plane is zero:

$a_\perp = 0.$

Then Newton’s second law perpendicular to the plane determines N. For example, if the only forces with perpendicular components are N and weight, you get:

$$
N - mg\cos\theta = 0 \Rightarrow N = mg\cos\theta.
$$

This is already different from mg.

### Loss of contact condition

If the solution gives N <= 0, that indicates the surface cannot “pull” on the object in the normal direction. The correct physical interpretation is usually:

- contact is lost,
- then N becomes 0 and the motion model changes.

## Interpretation

- N is a constraint force: it exists because the surface enforces a geometric constraint.
- You do not guess N. You solve for it using the perpendicular equation of motion and the contact constraint.
- Saying “N equals mg” is only correct when:
  - the surface is horizontal, and
  - there is no vertical acceleration, and
  - there are no other vertical forces (like a rope pulling up).

## Typical examples

1) Elevator floor: N differs from mg when the elevator accelerates.

2) Block pulled upward at an angle: N is reduced because the rope has an upward component.

3) Block on an incline: N = mg cos(theta) (if no other perpendicular forces).

4) Roller coaster crest: N can drop to zero at a high speed, leading to weightlessness.

## Common mistakes

- Assuming N = mg automatically.
- Forgetting to choose a perpendicular axis and accidentally using the parallel equation to solve for N.
- Confusing the third-law pair of N (object on surface) with mg (Earth on object).
- Allowing N to be negative without interpreting it as loss of contact.

## Worked example

A person of mass:

$m = 70\,\text{kg}$

stands on a bathroom scale in an elevator. The elevator accelerates downward with magnitude 2.0 m/s^2. Take y upward and g = 9.8 m/s^2.

Find the scale reading (the normal force N).

### Step 1: Write Newton’s second law in y

For the person, vertical forces are:

- N upward,
- mg downward.

So:

$N - mg = ma_y.$

The elevator accelerates downward, so a_y is negative:

$a_y = -2.0\,\text{m/s}^2.$

### Step 2: Solve for N

$N = m(g + a_y) = 70(9.8 - 2.0).$

Compute:

$N = 70(7.8) = 546\,\text{N}.$

### Step 3: Interpret

At rest, the scale would read mg = 686 N. Here it reads 546 N, smaller, because the net force must be downward to produce downward acceleration. This is a normal-force example of “apparent weight changes with acceleration.”

## Mini recap

- Normal force is a surface response force perpendicular to the surface.
- It is determined by Newton’s second law plus the contact constraint.
- Flat surface:

$N - mg = ma_y.$

- Incline (no perpendicular acceleration):

$$
N = mg\cos\theta \quad \text{(if only gravity contributes perpendicularly)}.
$$

- If a computed N <= 0, contact is lost and N becomes 0 with a new motion model.

<!-- SOURCE: lecture/dynamics/11_tension_force.md -->

# Tension force

## Learning goals

- Model tension as the pulling force transmitted by an ideal rope/string.
- Draw the correct direction of tension forces on each connected object.
- State standard pulley/rope assumptions and know what they imply about tension magnitude.
- Solve basic connected-body problems using separate free-body diagrams and Newton’s second law.

## Why this matters

Tension appears in many multi-body problems: hanging masses, pulleys, elevators, and towing. The most common errors are not algebraic; they are modeling errors:

- putting tension in the wrong direction,
- assuming tension equals weight,
- mixing up which body a given tension force acts on.

This section establishes a consistent tension model that you can reuse across many dynamics problems.

## Core idea

An ideal rope/string transmits a pulling interaction along its length. It can pull but cannot push.

Therefore:

- tension acts along the rope direction,
- tension on a body points away from the body along the rope (the rope pulls on the body),
- different bodies feel different tension forces, but they are connected through the rope model.

## Mathematical formulation

### Ideal rope assumptions (common in intro problems)

When a problem says “light rope” or “massless rope,” and a “frictionless pulley,” the usual idealization is:

- the rope has negligible mass,
- the rope does not stretch (inextensible),
- the pulley is frictionless and massless (in many problems).

Under these assumptions:

- the tension magnitude is the same everywhere along one continuous rope segment,
- the rope length constraint ties the accelerations of connected bodies.

If the pulley has significant mass or friction, tension can differ on the two sides. That is beyond the simplest model, and the problem statement will typically mention it explicitly.

### Direction rule (force on the body)

If a rope segment attached to a body points along some direction, the tension force exerted by the rope on the body points along that segment away from the body.

In diagrams, you label that force as T. You do not decide its magnitude by guessing; it is determined by the equations of motion plus constraints.

## Interpretation

- Tension is not a “new kind of physics.” It is a convenient name for the force a rope exerts.
- In many problems, T is the same on both sides of an ideal pulley, but that is a modeling assumption, not a universal law.
- A tension force is always part of an interaction pair: rope on mass and mass on rope (Newton’s third law). In a free-body diagram for the mass, you include only rope on mass.

## Typical examples

1) Hanging mass at rest: tension equals weight only if acceleration is zero and the only vertical forces are T and mg.

2) Atwood machine (two hanging masses): tension is generally not equal to either weight; it is determined by the coupled motion.

3) Block on a table connected to a hanging mass: horizontal tension pulls the block; vertical tension pulls the hanging mass.

## Common mistakes

- Drawing tension pointing toward the body instead of away along the rope.
- Assuming T = mg automatically for any hanging mass (only true in certain equilibrium/constant-speed cases).
- Using one equation for “the whole system” without separate free-body diagrams when different forces act on different bodies.
- Forgetting the constraint that the rope enforces equal-magnitude accelerations in many simple setups.
- Confusing the third-law pair of tension (mass on rope) with another force on the same mass.

## Worked example

Atwood machine (ideal). Two masses m_1 and m_2 hang from a light rope over a frictionless, massless pulley. Let:

$m_2 > m_1.$

Assume the rope does not stretch. Find:

1) the acceleration magnitude a,  
2) the tension T in the rope.

Take y upward for m_1 and y downward for m_2 (so both accelerations have the same sign a in their chosen positive directions).

### Step 1: Free-body diagram equations

For m_1 (moving up):

- tension T upward,
- weight m_1 g downward.

Newton’s second law:

$T - m_1 g = m_1 a.$

For m_2 (moving down; we chose downward as positive for this mass):

- weight m_2 g downward (positive),
- tension T upward (negative).

Newton’s second law:

$m_2 g - T = m_2 a.$

### Step 2: Solve the coupled equations

Add the equations:

$(T - m_1 g) + (m_2 g - T) = m_1 a + m_2 a.$

Simplify:

$(m_2 - m_1)g = (m_1 + m_2)a.$

So:

$$
a = \frac{(m_2 - m_1)g}{m_1 + m_2}.
$$

### Step 3: Solve for tension

Use the m_1 equation:

$T = m_1 g + m_1 a = m_1(g + a).$

Substitute a:

$$
T = m_1\left(g + \frac{(m_2 - m_1)g}{m_1 + m_2}\right)
= m_1 g\left( \frac{(m_1+m_2) + (m_2-m_1)}{m_1+m_2} \right)
= m_1 g\left(\frac{2m_2}{m_1+m_2}\right).
$$

So:

$$
T = \frac{2m_1 m_2}{m_1+m_2}g.
$$

### Step 4: Sanity checks

- If m_1 = m_2, then a = 0 and T = m_1 g, as expected.
- If m_2 >> m_1, then a approaches g and T approaches 2m_1 g (the light mass is pulled up strongly).

## Mini recap

- Tension is the pulling force a rope exerts along its length.
- In ideal rope + frictionless massless pulley problems, tension magnitude is the same along one rope segment.
- Always draw separate free-body diagrams and use the rope constraint for accelerations.
- Do not assume T = mg unless acceleration is known to be zero and the force list supports it.

<!-- SOURCE: lecture/dynamics/12_friction_static_and_kinetic.md -->

# Friction: static and kinetic

## Learning goals

- Model friction as a contact interaction that opposes relative slipping (or the tendency to slip).
- Distinguish static friction from kinetic friction and use the correct formula/inequality.
- Determine friction direction by reasoning about the would-be motion (not by guessing a sign).
- Avoid the mistake “friction always equals mu N.”

## Why this matters

Friction is where many dynamics solutions fail, because friction is not a single fixed magnitude with a fixed direction. Its value depends on what the system is trying to do.

In beginner problems, the goal is to learn a reliable method:

- decide whether the contact is sticking or slipping,
- choose static or kinetic friction accordingly,
- use Newton’s laws to solve for the required friction,
- then check whether the result is consistent with the static friction limit.

## Core idea

Friction is a contact force parallel to the surface. It acts to oppose:

- actual relative motion (sliding), or
- the tendency for relative motion (impending slip).

There are two regimes:

- static friction: no slipping at the contact,
- kinetic friction: slipping occurs.

Static friction is “self-adjusting” up to a maximum. Kinetic friction has (in the simplest model) a roughly constant magnitude proportional to the normal force.

## Mathematical formulation

### Static friction

Static friction magnitude f_s satisfies:

$0 \le f_s \le f_{s,\text{max}}.$

The common coefficient model is:

$f_{s,\text{max}} = \mu_s N.$

Important: in static contact, the actual friction magnitude is whatever is needed (within the limit) to prevent slipping.

### Kinetic friction

When slipping occurs, kinetic friction magnitude is modeled as:

$f_k = \mu_k N,$

and it points opposite the direction of relative sliding velocity at the contact.

Typically:

$\mu_k < \mu_s.$

### Direction rule (crucial)

Friction direction is determined by the relative slip direction (kinetic) or the would-be slip direction (static).

Procedure:

1) Predict the direction the object would tend to move relative to the surface if there were no friction.  
2) Friction points opposite that tendency.  
3) Solve for its magnitude using Newton’s laws.  
4) For static friction, check that the required magnitude does not exceed mu_s N.

## Interpretation

- Static friction can be zero (e.g., a book resting on a table with no horizontal forces).
- Static friction can be nonzero without motion (e.g., a block at rest on an incline).
- Kinetic friction does work that typically removes mechanical energy (it dissipates energy as heat in a real system).

The coefficient model is an approximation that works reasonably well in many textbook situations, but it is not a universal law of nature.

## Typical examples

1) Block on a horizontal surface with a small push: static friction matches the push so the block stays at rest (until the push exceeds the maximum).

2) Block sliding on a horizontal surface: kinetic friction has constant magnitude mu_k N opposite the sliding direction.

3) Block on an incline: static friction may hold it at rest; if it slips, kinetic friction acts up the plane when the block slides down.

## Common mistakes

- Using f_s = mu_s N as an equality in all static cases. Correct is f_s <= mu_s N.
- Assigning friction direction without thinking about the would-be motion.
- Mixing static and kinetic coefficients or using mu_k when the contact is not slipping.
- Forgetting that N can change in some situations (inclines, angled pulls), and friction depends on N in the coefficient model.
- Treating friction as always present even when there is no tendency to slip (it can be zero).

## Worked example

A block of mass m = 4.0 kg rests on a rough incline of angle theta = 25 degrees. The coefficient of static friction is mu_s = 0.50. Take g = 9.8 m/s^2.

1) Determine whether the block remains at rest or begins to slide.  
2) If it remains at rest, find the static friction magnitude.

Choose axes parallel and perpendicular to the plane.

### Step 1: Compute the normal force

Perpendicular to the plane the acceleration is zero (it stays in contact), so:

$$
N - mg\cos\theta = 0 \Rightarrow N = mg\cos\theta.
$$

Compute:

$N = (4.0)(9.8)\cos 25^\circ.$

Numerically, cos 25 degrees is approximately 0.906, so:

$$
N \approx 39.2(0.906) \approx 35.5\,\text{N}.
$$

### Step 2: Determine the tendency to slip

The component of weight down the plane is:

$mg\sin\theta.$

Numerically, sin 25 degrees is approximately 0.423, so:

$$
mg\sin\theta \approx 39.2(0.423) \approx 16.6\,\text{N}.
$$

Without friction, the block would tend to slide down the plane. Therefore static friction (if present) points up the plane.

### Step 3: Check the static friction limit

Maximum static friction is:

$$
f_{s,\text{max}} = \mu_s N \approx (0.50)(35.5) \approx 17.8\,\text{N}.
$$

To keep the block at rest, the required static friction magnitude must equal the downslope component:

$$
f_s = mg\sin\theta \approx 16.6\,\text{N}.
$$

Since:

$$
f_s \approx 16.6\,\text{N} \le 17.8\,\text{N} = f_{s,\text{max}},
$$

static friction can supply the needed value. Therefore the block remains at rest.

### Step 4: State the result

- The block does not slide.
- The static friction magnitude is approximately 16.6 N, directed up the plane.

## Mini recap

- Static friction:

$0 \le f_s \le \mu_s N.$

- Kinetic friction:

$f_k = \mu_k N.$

- Direction is opposite slip (kinetic) or opposite the tendency to slip (static).
- In static problems: solve for the required friction, then check it does not exceed mu_s N.

<!-- SOURCE: lecture/dynamics/13_spring_force_hookes_law.md -->

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

<!-- SOURCE: lecture/dynamics/14_free_body_diagrams.md -->

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

<!-- SOURCE: lecture/dynamics/15_resolving_forces_into_components.md -->

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

<!-- SOURCE: lecture/dynamics/16_particle_on_horizontal_surface.md -->

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

<!-- SOURCE: lecture/dynamics/17_particle_on_inclined_plane.md -->

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

<!-- SOURCE: lecture/dynamics/18_connected_bodies_and_tension.md -->

# Connected bodies and tension

## Learning goals

- Apply Newton’s second law to multi-body systems with ropes/pulleys.
- Use the rope constraint to relate accelerations (shared magnitude in common setups).
- Draw separate free-body diagrams and write separate equations for each body.
- Solve coupled equations for acceleration and tension, and interpret the result.

## Why this matters

Many realistic systems involve connected bodies: elevators with counterweights, blocks connected by ropes, pulleys, and towing.

The new difficulty is not a new law; it is bookkeeping:

- each body has its own forces and its own equation,
- the rope constraint connects their accelerations,
- tension is an internal interaction in the combined system, but an external force on each individual body.

## Core idea

In an ideal rope over an ideal pulley, the rope length is constant. That constraint typically implies:

- the connected bodies have accelerations of equal magnitude,
- the directions are opposite along the rope.

The correct workflow:

1) Draw an FBD for each body separately.  
2) Choose axes consistent with each body’s motion.  
3) Write Newton’s second law for each body.  
4) Use the rope constraint to connect accelerations.  
5) Solve the coupled system for the unknowns (a, T, etc.).

## Mathematical formulation

### Rope constraint (typical single-pulley systems)

If the rope is massless and inextensible and does not slip on the pulley, then the rope length is constant.

In many standard setups this gives:

$a_1 = a_2$

for acceleration magnitudes, with opposite directions depending on axis choices.

### Separate Newton equations

For each body i:

$$
\sum \vec{F}_i = m_i\vec{a}_i.
$$

You generally write scalar component equations along the direction of motion for each body.

### System approach (optional idea)

Sometimes it is useful to consider the two bodies together as one system to eliminate internal forces like tension. In that combined-system view, tension is internal and cancels in the net external force sum.

However, to find the tension itself you still need individual-body equations.

## Interpretation

- Tension is not “the same as weight.” It is determined by the coupled motion.
- The heavier side does not “pull with a bigger tension.” Tension is an internal interaction constrained by the rope model and the dynamics of both masses.
- Internal forces can cancel when you write a combined equation for the whole system, but they do not disappear from individual free-body diagrams.

## Typical examples

1) Block on a table connected to a hanging mass (with or without friction).

2) Two blocks connected on a horizontal surface.

3) Atwood machine (two hanging masses; already solved in the tension section, now as a template for solving).

## Common mistakes

- Writing one equation for the whole system and then trying to solve for tension without an individual-body equation.
- Using different acceleration magnitudes for connected bodies in a single-rope system.
- Mixing sign conventions: choosing axes inconsistently so that the rope constraint is written incorrectly.
- Treating tension as known (like T = mg) instead of as an unknown to solve for.
- Forgetting friction on the block on the table when it is stated to be present.

## Worked example

A block m_1 = 3.0 kg rests on a horizontal table. It is connected by a light rope over a frictionless pulley to a hanging mass m_2 = 2.0 kg.

The coefficient of kinetic friction between m_1 and the table is mu_k = 0.20. Take g = 9.8 m/s^2.

Assume the system moves with m_2 downward (so m_1 moves to the right).

Find:

1) the acceleration magnitude a,  
2) the rope tension T.

### Step 1: Free-body diagram equations

For m_1 (on table, x to the right):

Horizontal forces:

- tension T to the right,
- kinetic friction f_k to the left.

So:

$T - f_k = m_1 a.$

Vertical forces on m_1 balance (a_y = 0), so:

$N = m_1 g.$

Thus:

$f_k = \mu_k N = \mu_k m_1 g.$

For m_2 (hanging, choose positive downward to match assumed motion):

Forces:

- weight m_2 g downward (positive),
- tension T upward (negative).

So:

$m_2 g - T = m_2 a.$

### Step 2: Compute friction and solve the coupled system

Compute friction:

$f_k = \mu_k m_1 g = (0.20)(3.0)(9.8) = 5.88\,\text{N}.$

Now solve for a and T. From the m_1 equation:

$T = m_1 a + f_k.$

Substitute into the m_2 equation:

$m_2 g - (m_1 a + f_k) = m_2 a.$

Solve for a:

$m_2 g - f_k = (m_1 + m_2)a.$

So:

$$
a = \frac{m_2 g - f_k}{m_1 + m_2}.
$$

Plug in numbers:

$$
a = \frac{(2.0)(9.8) - 5.88}{3.0 + 2.0} = \frac{19.6 - 5.88}{5.0} = \frac{13.72}{5.0} = 2.74\,\text{m/s}^2.
$$

### Step 3: Solve for tension

Use:

$T = m_1 a + f_k = (3.0)(2.74) + 5.88 = 8.22 + 5.88 = 14.10\,\text{N}.$

### Step 4: Quick checks

- If friction were zero, acceleration would be m_2 g / (m_1 + m_2) = 19.6/5 = 3.92 m/s^2, larger than 2.74. Friction reduces acceleration, as expected.
- T is between m_2 g = 19.6 N and 0, reasonable.

## Mini recap

- Draw separate FBDs for each body.
- Write separate Newton equations and connect accelerations with the rope constraint.
- Tension is generally unknown and must be solved for.
- For a two-body table + hanging system, a common structure is:

$T - f_k = m_1 a, \qquad m_2 g - T = m_2 a,$

with:

$f_k = \mu_k m_1 g$

if the table block slides.

<!-- SOURCE: lecture/dynamics/19_circular_motion_and_centripetal_force.md -->

# Circular motion and centripetal force (role)

## Learning goals

- Connect circular motion kinematics (inward acceleration) to dynamics (required inward net force).
- Write the radial (inward) component equation with correct sign conventions.
- Understand that “centripetal force” is not a new force type; it is the name for the net inward force required for circular motion.
- Solve basic circular dynamics problems: mass on a string, car turning, and simple vertical circle conditions.

## Why this matters

Circular motion is where many students invent a “centrifugal force” as a real force in inertial frames. The correct dynamic idea is:

- circular motion requires inward acceleration,
- Newton’s second law then requires an inward net force.

Once you can write the radial force balance correctly, many circular-motion problems become straightforward.

## Core idea

Kinematics tells you that to move in a circle of radius R with speed v, the acceleration must point inward with magnitude:

$$
a_r = \frac{v^2}{R}.
$$

Dynamics says:

$$
\sum \vec{F} = m\vec{a}.
$$

So in the radial direction, the net force component must point inward with magnitude:

$$
F_{\text{net,inward}} = m\frac{v^2}{R}.
$$

This inward net force is what people call the centripetal force. It is not an extra force; it is the net of whatever real forces happen to have inward components.

## Mathematical formulation

### Radial axis and sign convention

Choose a radial axis pointing inward toward the center (this is often the cleanest choice). Then:

$$
a_r = \frac{v^2}{R}
$$

is positive (inward).

Newton’s second law in the radial direction becomes:

$$
\sum F_r = m\frac{v^2}{R}.
$$

Here the symbol \sum F_r means “sum of the inward components of all forces.”

### Common force contributors to radial direction

Depending on the situation, inward components can come from:

- tension in a string,
- normal force from a track,
- gravity components (in vertical circles),
- friction (for a car turning on a flat road, friction provides the inward force).

You project each real force onto the radial direction and sum.

## Interpretation

- Saying “centripetal force” answers the question “what is the net inward force?” not “which force is present?”
- If you draw an FBD and then add a new arrow labeled “centripetal force” in addition to tension/normal/gravity, you will double-count.
- If you describe motion from a rotating frame, you may introduce inertial forces (like centrifugal) as a bookkeeping device. In an inertial frame, you do not need them.

## Typical examples

1) Mass on a horizontal circle on a string: tension provides the inward force.

2) Car turning on a flat road: static friction provides the inward force (up to a limit), which sets a maximum safe speed for a given turn radius.

3) Vertical circle/loop: tension/normal and weight both contribute to radial force, and contact can be lost when normal force becomes zero.

## Common mistakes

- Treating “centripetal force” as a separate force in the free-body diagram.
- Writing m v^2/R and labeling it as a force without specifying which real forces sum to it.
- Choosing outward as positive and then forgetting the sign of a_r (sign conventions must be consistent).
- Using v^2/R with v not being the instantaneous speed (it must be the speed at that point).
- Confusing friction direction in turning problems (friction points toward the center for a car turning without slipping).

## Worked example

A 0.50 kg mass moves in a horizontal circle of radius R = 0.80 m at constant speed v = 4.0 m/s, attached to a string.

Neglect air resistance. Find the tension in the string.

### Step 1: Identify radial acceleration

$$
a_r = \frac{v^2}{R} = \frac{(4.0)^2}{0.80} = \frac{16}{0.80} = 20\,\text{m/s}^2.
$$

### Step 2: Radial force balance

In a horizontal circle, weight and normal (if any) are vertical and do not contribute to the radial (horizontal inward) direction. The only radial force is tension T.

So:

$$
T = m a_r = m\frac{v^2}{R}.
$$

Compute:

$T = (0.50)(20) = 10\,\text{N}.$

Interpretation: tension provides exactly the inward net force needed to continuously change the velocity direction.

## Mini recap

- Circular motion requires inward acceleration:

$$
a_r = \frac{v^2}{R}.
$$

- Dynamics in the radial direction (inward positive):

$$
\sum F_r = m\frac{v^2}{R}.
$$

- “Centripetal force” means the net inward force role; it is not an additional force you add to the FBD.

<!-- SOURCE: lecture/dynamics/20_dynamics_with_given_force_law.md -->

# Dynamics with a given force law

## Learning goals

- Translate a force law into an equation of motion using Newton’s second law.
- Recognize force laws depending on time, position, or velocity and what that implies about acceleration.
- Use initial conditions to determine a unique motion.
- Solve simple cases and interpret what the model assumes physically.

## Why this matters

In dynamics problems, the central input is not x(t). It is a force model:

- “The net force is constant.”
- “The force depends on position.”
- “The force depends on velocity (drag).”
- “The applied force varies with time.”

Each of these leads to a different kind of equation of motion. If you can translate a force law into a differential equation, you can connect dynamics back to kinematics systematically.

## Core idea

Force laws are model statements of the form:

$F_{\text{net}} = F(x, v, t).$

Newton’s second law then gives:

$$
m\frac{d^2x}{dt^2} = F\left(x, \frac{dx}{dt}, t\right).
$$

The “difficulty” of the dynamics problem is usually the difficulty of solving that equation.

But before solving, you must interpret the model:

- What is being neglected?
- Over what range is the force law expected to be valid?
- Are we modeling a net force or an individual force?

## Mathematical formulation

### Case A: time-dependent force F(t)

If:

$F_{\text{net}} = F(t),$

then:

$$
a(t) = \frac{F(t)}{m}.
$$

This becomes a kinematics reconstruction problem:

$a(t) \rightarrow v(t) \rightarrow x(t),$

using integration and initial conditions.

### Case B: position-dependent force F(x)

If:

$F_{\text{net}} = F(x),$

then:

$$
m\frac{d^2x}{dt^2} = F(x).
$$

Acceleration depends on position, so it is generally not constant. A classic example is a spring:

$F(x) = -kx.$

### Case C: velocity-dependent force F(v)

If:

$F_{\text{net}} = F(v),$

then:

$$
m\frac{dv}{dt} = F(v).
$$

This is a differential equation for v(t). A simple linear drag model is:

$F(v) = -bv,$

leading to:

$$
m\frac{dv}{dt} = -bv.
$$

### Case D: combined dependence F(x, v, t)

Many real systems have forces depending on multiple variables (e.g., gravity + drag + time-varying thrust). The same translation step applies; solving may require more advanced methods or approximations.

## Interpretation

- Force laws are not always exact. They are approximations valid in specified regimes.
- A force law should be read as a statement about a specific interaction or about the net force, depending on context.
- If you are given a force law, you should still draw an FBD to clarify which forces are included and what direction the force acts in.

## Typical examples

1) Rocket thrust schedule F(t): acceleration changes in time; integrate to get v(t) and x(t).

2) Spring force F(x) = -kx: acceleration depends on x; motion becomes oscillatory.

3) Linear drag F(v) = -bv: velocity decays exponentially toward zero (if no other forces act).

## Common mistakes

- Treating a force law as if it automatically gives constant acceleration.
- Forgetting that if F depends on x or v, then acceleration changes during the motion.
- Ignoring sign: writing “F = kx” instead of “F = -kx” for restoring springs.
- Mixing up net force with an individual force (e.g., treating a given applied force as the net force while friction is present).
- Using initial conditions inconsistently (wrong reference time).

## Worked example

A particle of mass m = 2.0 kg moves along a line. The net force is time-dependent:

$F_{\text{net}}(t) = 6t\,\text{N}.$

At t = 0:

$x(0)=1\,\text{m}, \qquad v(0)=0.$

Find a(t), v(t), and x(t).

### Step 1: Acceleration from the force law

Newton’s second law:

$$
a(t) = \frac{F_{\text{net}}(t)}{m} = \frac{6t}{2.0} = 3t.
$$

So:

$a(t) = 3t\,\text{m/s}^2.$

### Step 2: Integrate to get velocity

$$
v(t) = v(0) + \int_0^t a(\tau)\,d\tau = 0 + \int_0^t 3\tau\,d\tau.
$$

Compute:

$$
v(t) = \left[\frac{3}{2}\tau^2\right]_0^t = \frac{3}{2}t^2.
$$

So:

$v(t) = 1.5t^2\,\text{m/s}.$

### Step 3: Integrate to get position

$$
x(t) = x(0) + \int_0^t v(\tau)\,d\tau = 1 + \int_0^t 1.5\tau^2\,d\tau.
$$

Compute:

$x(t) = 1 + \left[0.5\tau^3\right]_0^t = 1 + 0.5t^3.$

So:

$x(t) = 1 + 0.5t^3\,\text{m}.$

### Step 4: Interpretation

Because the force grows in time, acceleration grows in time, so velocity grows faster than linearly and position grows faster than quadratically.

This example shows how a time-dependent force turns dynamics into a kinematics reconstruction problem.

## Mini recap

- Translate force laws into equations of motion using:

$$
m\frac{d^2x}{dt^2} = F\left(x, \frac{dx}{dt}, t\right).
$$

- If F depends only on t, then a(t) is known and you integrate to get v(t) and x(t).
- If F depends on x or v, acceleration is not constant; you generally get a differential equation that may be harder to solve.
- Always interpret the force law as a model with assumptions and a regime of validity.

<!-- SOURCE: lecture/dynamics/21_from_force_to_acceleration_to_motion.md -->

# From force to acceleration to motion

## Learning goals

- Use the full Newtonian pipeline: forces → net force → acceleration → velocity → position.
- Decide when acceleration is constant vs time-dependent based on the force model.
- Use initial conditions correctly to obtain a unique motion.
- Compare “kinematics-first” and “dynamics-first” problem statements and see how they connect.

## Why this matters

This is the synthesis step of the course so far.

In kinematics, you often start with x(t), v(t), or a(t) given and reconstruct the rest.

In dynamics, you usually start with physical information (what forces act, what constraints apply) and your job is to determine a(t). Once you have a(t), kinematics finishes the job.

So the same kinematic formulas you already know become useful tools, but now the acceleration is not assumed; it is derived.

## Core idea

The Newtonian workflow for a particle is:

1) Choose system and axes.  
2) Draw an FBD and write the net force.  
3) Use Newton’s second law to get acceleration:

$$
\sum \vec{F} = m\vec{a}.
$$

4) Use kinematics to turn acceleration into motion:

$\vec{a}(t) \rightarrow \vec{v}(t) \rightarrow \vec{r}(t),$

with initial conditions.

If the net force is constant, acceleration is constant and you can use constant-acceleration kinematics. If the net force depends on time/position/velocity, you must integrate accordingly (sometimes solving a differential equation).

## Mathematical formulation

### The pipeline in 1D

Start with a force model:

$F_{\text{net}}(x, v, t).$

Newton’s second law gives:

$$
a(t) = \frac{d^2x}{dt^2} = \frac{F_{\text{net}}(x, v, t)}{m}.
$$

Then reconstruct:

$$
v(t) = v_0 + \int_{t_0}^{t} a(\tau)\,d\tau,
$$

$$
x(t) = x_0 + \int_{t_0}^{t} v(\tau)\,d\tau.
$$

### What changes from kinematics-only problems

In a kinematics-only problem, you might be told:

$a(t) = a_0$

and asked to find x(t).

In a dynamics problem, you are not told a(t) directly. You infer it from forces:

$$
a = \frac{F_{\text{net}}}{m}.
$$

Then you proceed exactly as in kinematics, but with a derived acceleration.

## Interpretation

- Dynamics determines a(t) by modeling interactions and constraints.
- Kinematics turns that a(t) into motion, with constants fixed by initial conditions.
- Different force models can produce the same a(t) over a limited range; dynamics is where you justify the model and check its assumptions.

## Typical examples

1) Block on a table pulled with constant force and kinetic friction: net force is constant → constant acceleration → quadratic x(t).

2) Block on an incline with kinetic friction: net force along plane is constant → constant acceleration down the plane.

3) Force varying in time (thrust schedule): a(t) varies → integrate to get v(t), x(t).

## Common mistakes

- Treating the applied force as the net force while forgetting friction or other forces.
- Jumping to constant-acceleration kinematics without first checking whether the net force is constant.
- Losing track of sign conventions (especially on inclines and in vertical motion).
- Using initial conditions from the wrong time or wrong reference position.
- Forgetting that constraints (like a_y = 0) are part of the dynamics and affect N and friction.

## Worked example

A 4.0 kg block is pulled to the right along a horizontal surface by a constant horizontal force F = 30 N. The coefficient of kinetic friction is mu_k = 0.20. Take g = 9.8 m/s^2.

At time t=0:

$x(0)=0, \qquad v(0)=1.0\,\text{m/s}.$

Find:

1) the acceleration,  
2) v(t) and x(t),  
3) the position at t = 5.0 s.

### Step 1: Force model and net force

Vertical forces balance (a_y = 0), so:

$N = mg = (4.0)(9.8) = 39.2\,\text{N}.$

Kinetic friction magnitude:

$f_k = \mu_k N = 0.20(39.2) = 7.84\,\text{N}.$

Horizontal net force:

$F_{\text{net}} = F - f_k = 30 - 7.84 = 22.16\,\text{N}.$

Direction: to the right, so acceleration is positive in the chosen x direction.

### Step 2: Acceleration from Newton’s second law

$$
a = \frac{F_{\text{net}}}{m} = \frac{22.16}{4.0} = 5.54\,\text{m/s}^2.
$$

This is constant because both F and f_k are constant in this model.

### Step 3: Use kinematics to get v(t) and x(t)

With constant acceleration:

$v(t) = v(0) + at = 1.0 + 5.54t.$

$$
x(t) = x(0) + v(0)t + \frac{1}{2}at^2 = 0 + (1.0)t + \frac{1}{2}(5.54)t^2.
$$

So:

$x(t) = t + 2.77t^2.$

### Step 4: Evaluate at t = 5.0 s

$x(5) = 5 + 2.77(25) = 5 + 69.25 = 74.25\,\text{m}.$

Interpretation: the block already has some initial speed and then accelerates strongly due to a sizeable net force.

## Mini recap

- Dynamics: find the net force and compute acceleration:

$$
a = \frac{F_{\text{net}}}{m}.
$$

- Kinematics: integrate (or use constant-acceleration formulas) to get v(t) and x(t) with initial conditions.
- Always check whether the net force is constant before using constant-acceleration kinematics.

<!-- SOURCE: lecture/dynamics/22_dynamics_summary.md -->

# Dynamics summary

## Learning goals

- Summarize the Newtonian dynamics workflow and apply it consistently.
- Use Newton’s three laws with correct frame assumptions and correct force bookkeeping.
- Recognize the main force models (weight, normal, tension, friction, spring) and typical constraints.
- Avoid the most common conceptual errors in dynamics (net force, third-law pairs, friction direction, N not always mg).

## Why this matters

Dynamics is the “engine” of predictive mechanics: it tells you what acceleration follows from a modeled set of interactions.

If you can do dynamics well, you can:

- build equations of motion for new situations,
- decide which kinematics tools apply (constant acceleration vs variable acceleration),
- and interpret results physically (signs, directions, limiting cases).

This summary is a map: it ties together the recurring patterns so that you can solve new problems without memorizing dozens of special formulas.

## Core idea

The Newtonian logic chain is:

1) Choose an inertial frame (or account for non-inertial effects).  
2) Choose the system and model (particle, ideal rope, etc.).  
3) List external forces on the system with a free-body diagram.  
4) Add forces vectorially to get net force.  
5) Apply Newton’s second law to get acceleration.  
6) Use kinematics to get velocity and position.

In symbols:

$$
\text{FBD} \rightarrow \sum \vec{F} = m\vec{a} \rightarrow \vec{a}(t) \rightarrow \vec{v}(t) \rightarrow \vec{r}(t).
$$

## Mathematical formulation

### Newton’s laws (operational form)

First law (inertial frame): zero net force implies constant velocity:

$$
\sum \vec{F} = \vec{0} \Rightarrow \vec{v} = \text{constant}.
$$

Second law (inertial frame):

$$
\sum \vec{F} = m\vec{a}.
$$

Third law (interaction pairs):

$\vec{F}_{A\to B} = -\vec{F}_{B\to A}.$

### Standard force models (near Earth, intro level)

Weight:

$\vec{W} = m\vec{g}.$

Normal force N: constraint response perpendicular to a surface; determine from the perpendicular equation of motion plus constraints.

Kinetic friction:

$f_k = \mu_k N$

Static friction:

$0 \le f_s \le \mu_s N.$

Spring force (1D about equilibrium):

$F_{\text{spring}} = -kx.$

Tension T: force transmitted by an ideal rope along its length; often equal along one rope segment in ideal pulley problems.

### Component method

Choose axes and write:

$$
\sum F_x = ma_x, \qquad \sum F_y = ma_y.
$$

Use constraints like a_y = 0 (contact) or shared acceleration magnitudes (ideal rope).

### Equations of motion

If the net force model depends on x, v, or t, the equation of motion becomes:

$$
m\frac{d^2x}{dt^2} = F\left(x, \frac{dx}{dt}, t\right).
$$

Then kinematics is applied by solving/integrating with initial conditions.

## Interpretation

- Net force is a vector sum of external forces on the chosen system, not one “dominant force.”
- Third-law pairs act on different bodies, so they do not cancel in one body’s equation.
- Normal force is determined by constraints; it is not always mg.
- Friction direction is opposite slip or tendency to slip; static friction is self-adjusting up to a maximum.
- The choice of axes is part of the solution; align axes with constraints to simplify.

## Typical examples

1) Horizontal surface with friction and an angled pull: use y equation to find N, then friction, then x equation for a.

2) Inclined plane: decompose weight, solve N from perpendicular equation, then solve along-plane motion.

3) Connected bodies: draw separate FBDs, write separate equations, use rope constraint, solve for a and T.

4) Circular motion: write the radial equation sum F_r = m v^2/R and interpret which real forces provide the inward net force.

## Common mistakes

- Skipping the FBD and guessing forces.
- Using constant-acceleration kinematics without checking whether net force is constant.
- Confusing mass and weight; using g as a force.
- Treating “centripetal force” as an extra force arrow instead of the net inward force role.
- Writing static friction as f_s = mu_s N without checking the inequality.
- Allowing N < 0 without interpreting it as loss of contact.
- Mixing sign conventions mid-solution (especially vertical and incline problems).

## Worked example

A block m_1 = 4.0 kg lies on a rough table and is connected over a frictionless pulley to a hanging mass m_2 = 1.5 kg. The coefficient of kinetic friction between m_1 and the table is mu_k = 0.25. Take g = 9.8 m/s^2.

Assume m_2 moves downward (so m_1 moves right).

Find:

1) the acceleration a,  
2) the tension T.

### Step 1: Free-body diagrams and force models

For m_1 (on table, x to the right):

- T to the right,
- kinetic friction f_k to the left.

Vertical: N = m_1 g (no vertical acceleration).

So:

$T - f_k = m_1 a,$

$f_k = \mu_k N = \mu_k m_1 g.$

For m_2 (hanging, choose downward positive):

- m_2 g downward,
- T upward.

So:

$m_2 g - T = m_2 a.$

### Step 2: Compute friction

$f_k = (0.25)(4.0)(9.8) = 9.8\,\text{N}.$

### Step 3: Solve for acceleration

From the m_1 equation:

$T = m_1 a + f_k.$

Substitute into the m_2 equation:

$m_2 g - (m_1 a + f_k) = m_2 a.$

So:

$m_2 g - f_k = (m_1 + m_2)a.$

Compute m_2 g:

$m_2 g = (1.5)(9.8) = 14.7\,\text{N}.$

Thus:

$$
a = \frac{14.7 - 9.8}{4.0 + 1.5} = \frac{4.9}{5.5} = 0.891\,\text{m/s}^2.
$$

### Step 4: Solve for tension

$T = m_1 a + f_k = (4.0)(0.891) + 9.8 = 3.56 + 9.8 = 13.36\,\text{N}.$

### Step 5: Interpret and check

- Acceleration is much smaller than g, reasonable because friction is significant and the hanging mass is small.
- T is between f_k (about 10 N) and m_2 g (14.7 N), consistent with both equations.

## Mini recap

- Dynamics workflow: system + assumptions → FBD → components → \sum F = ma → solve → interpret.
- Know what each standard force model means and when it applies.
- Always check signs, limiting cases, and whether your assumptions (contact, slipping, constant net force) remain consistent.

<!-- SOURCE: lecture/dynamics/23_dynamics_problem_set.md -->

# Dynamics Problem Set

## Purpose

Practice Newtonian dynamics with emphasis on:

- correct free-body diagrams (system isolation and force listing),
- correct use of Newton’s laws in an inertial frame,
- friction direction and static vs kinetic logic,
- constraints (a_y = 0, rope constraints, circular constraints),
- translating force models into acceleration and (when needed) into motion using kinematics.

Unless stated otherwise, take g = 9.8 m/s^2.

## Warm-up problems

1. (Net force) Two horizontal forces act on a puck: 5 N east and 12 N west. Find the net force (magnitude and direction).

2. (Newton 2 in 1D) A 3.0 kg block experiences a net horizontal force of 9.0 N to the right. Find its acceleration.

3. (Mass vs weight) A 60 kg person stands still on a scale in an elevator moving at constant speed. What does the scale read (in N)?

4. (Normal force) A 4.0 kg block rests on a horizontal table. An upward force of 10 N is applied to the block. Find the normal force.

5. (Friction threshold) A 6.0 kg crate is on a horizontal floor with mu_s = 0.40. Find the maximum horizontal force that can be applied without causing slipping.

## Standard problems

1. (Horizontal with kinetic friction) A 8.0 kg box is pulled horizontally with force 30 N on a surface with mu_k = 0.25. Find the acceleration.

2. (Angled pull) A 12 kg crate is pulled with a 50 N rope at 25 degrees above horizontal on a surface with mu_k = 0.20. Find the acceleration. (Hint: use y equation to find N.)

3. (Incline, no friction) A 2.5 kg block slides on a frictionless 35-degree incline. Find its acceleration down the plane and the normal force.

4. (Incline, static friction check) A 10 kg block rests on a 20-degree incline with mu_s = 0.30. Determine whether it slips. If it does not slip, find the static friction magnitude.

5. (Spring force at an instant) A 1.5 kg mass on a frictionless horizontal spring (k = 200 N/m) is displaced by x = 0.08 m and released. Find the spring force and acceleration at release.

6. (Elevator “apparent weight”) A 75 kg person stands on a scale in an elevator accelerating upward at 1.6 m/s^2. Find the scale reading.

7. (Atwood machine) Two masses m_1 = 2.0 kg and m_2 = 3.5 kg hang over an ideal pulley. Find the acceleration and tension.

8. (Circular motion, role of centripetal force) A 0.40 kg mass moves in a horizontal circle of radius 0.60 m at speed 5.0 m/s on a string. Find the tension.

## Multi-step problems

1. (Block + hanging mass with friction) A block m_1 = 5.0 kg on a table (mu_k = 0.15) is connected over an ideal pulley to a hanging mass m_2 = 2.0 kg. Assume m_2 moves down.

a) Find a and T.  
b) Find the distance traveled in 3.0 s starting from rest (use kinematics after you find a).

2. (Static → kinetic transition) A 9.0 kg crate on a horizontal floor has mu_s = 0.50 and mu_k = 0.35. A horizontal force F is slowly increased from 0.

a) Find the force at which slipping begins.  
b) Immediately after slipping begins, find the acceleration when the applied force is held fixed at 60 N.

3. (Incline + rope) A 6.0 kg block on a 30-degree incline is pulled up the plane by a rope parallel to the plane with tension T = 40 N. The surface has mu_k = 0.20.

a) Find the acceleration (sign and magnitude).  
b) Determine whether the block moves up or down (consistency check).

4. (Circular motion with normal force) A 900 kg car goes around a flat circular turn of radius 70 m. The coefficient of static friction is mu_s = 0.80.

a) What provides the inward net force?  
b) Find the maximum speed before slipping occurs.

5. (Equation of motion from a force law) A particle of mass 1.0 kg moves in 1D with net force:

$F_{\text{net}}(t) = 4 - 2t$

in newtons, for 0 <= t <= 3 s. Given x(0)=0 and v(0)=1 m/s:

a) Find a(t).  
b) Find v(t) and x(t).  
c) Find x(3).

6. (Equation of motion with position-dependent force) A 0.50 kg particle moves in 1D under:

$F(x) = -3x$

in newtons, where x is in meters.  

a) Write the equation of motion.  
b) At x = 0.20 m, find the acceleration (magnitude and direction).  
c) Describe qualitatively why the motion tends to oscillate about x = 0.

## Conceptual questions

1. In an inertial frame, can an object move with constant velocity while forces act on it? Explain with an example.

2. Why do Newton’s third-law pairs not cancel in a free-body diagram of a single object?

3. A student claims: “If an elevator is moving upward, the normal force must be larger than mg.” What is wrong with this statement?

4. How do you decide the direction of static friction in a problem where the object is not moving?

5. What does the phrase “centripetal force” really mean, and why is it misleading to draw it as an extra force arrow?

6. In an ideal rope and pulley setup, why is tension often the same on both sides? What assumption is being used?

7. When you compute a normal force and get N <= 0, what is the correct physical interpretation?

8. In a dynamics problem, what is the difference between being given a(t) and being given F(t)?

## Challenge problems

1. (Two-body, static friction) A block m_1 on a table is connected over a pulley to a hanging mass m_2. The table is rough with coefficient of static friction mu_s. Find the largest m_2 for which the system can remain at rest. Express your answer in terms of m_1, mu_s, and g.

2. (Vertical circle condition) A mass m on a string moves in a vertical circle of radius R. At the top of the circle, what minimum speed is required to keep the string taut (tension nonnegative)? State your reasoning using the radial force balance.

3. (Piecewise dynamics + kinematics) A 2.0 kg cart is pushed on a horizontal surface with kinetic friction mu_k = 0.10. From t=0 to t=3 s, an applied force of 8 N acts to the right. After t=3 s, the applied force is removed and only friction acts.

a) Find the acceleration on each interval.  
b) Starting from rest at x(0)=0, find v(3) and x(3).  
c) Find how long after t=3 s the cart comes to rest and the total distance traveled.

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
