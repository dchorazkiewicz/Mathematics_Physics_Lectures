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
x(t), \quad v(t) = \frac{dx}{dt}, \quad a(t) = \frac{dv}{dt} = \frac{d^2x}{dt^2}
$$

Vector position, velocity, acceleration (in 2D/3D):

$$
\vec{r}(t), \quad \vec{v}(t) = \frac{d\vec{r}}{dt}, \quad \vec{a}(t) = \frac{d\vec{v}}{dt}
$$

Forces and mass:

$$
\vec{F}, \quad m
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
v(t) = \frac{dx}{dt}, \qquad a(t) = \frac{dv}{dt} = \frac{d^2x}{dt^2}
$$

The derivative here has a physical meaning:

- $$v(t)$$ is the **instantaneous rate of change** of position (how fast and in which direction the position coordinate is changing).
- $$a(t)$$ is the **instantaneous rate of change** of velocity (how quickly the velocity changes in time).

In dynamics, the central idea (developed later) is that interactions determine acceleration. In Newtonian particle mechanics, this is expressed by:

$$
\sum \vec{F} = m\vec{a}
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
v(t) = \frac{dx}{dt} = 2 - 2t
$$

Differentiate again:

$$
a(t) = \frac{dv}{dt} = -2
$$

So the acceleration is constant and negative (in this coordinate choice).

2) What can kinematics tell you, and what can’t it tell you?

- Kinematics tells you there is a turning time when $$v(t)=0$$:

$$
2 - 2t = 0 \;\Rightarrow\; t = 1
$$

- It tells you the motion is initially in the positive direction (since $$v(0)=2>0$$), then reverses after $$t=1$$.

But kinematics alone does not tell you *which interaction* caused the constant acceleration. If you additionally know the mass is $$m=0.50\,\text{kg}$$ and you adopt Newton’s second law (dynamics), then the **net force** would be:

$$
F_{\text{net}} = ma = (0.50)(-2) = -1\,\text{N}
$$

That net force could arise from many physical situations (gravity component, a spring, a constant push, etc.). Identifying a realistic force model is part of dynamics.

## Mini recap

- Kinematics describes motion via $$x(t)$$ (or $$\vec{r}(t)$$) and its derivatives.
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
- in 2D/3D: a position vector $$\vec{r}(t)$$ or a set of coordinates such as $$x(t), y(t)$$.

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
\vec{r}(t)
$$

or in components (Cartesian coordinates):

$$
\vec{r}(t) = x(t)\,\hat{i} + y(t)\,\hat{j}
$$

where $$\hat{i}$$ and $$\hat{j}$$ are unit vectors along the chosen axes.

### Displacement (change in position)

Displacement is the difference between two positions (vector difference in 2D/3D, scalar difference in 1D). In 1D:

$$
\Delta x = x(t_2) - x(t_1)
$$

In vector form:

$$
\Delta \vec{r} = \vec{r}(t_2) - \vec{r}(t_1)
$$

Displacement is not “distance traveled.” Distance accumulates along the path; displacement depends only on the start and end positions.

### Changing the origin (same physical point, different coordinate)

Suppose you shift your origin by a constant amount. In 1D, if the new origin is located at coordinate $$x_0$$ in the old system, then the new coordinate is:

$$
x'(t) = x(t) - x_0
$$

This changes the numbers you call “position,” but it does not change the physical location of the particle. Importantly, displacement is unchanged by this shift:

$$
\Delta x' = x'(t_2) - x'(t_1) = \big(x(t_2)-x_0\big) - \big(x(t_1)-x_0\big) = x(t_2) - x(t_1) = \Delta x
$$

## Interpretation

1) **Frame dependence is not a flaw.** It is expected. The purpose of choosing a frame is to describe motion conveniently.

2) **Coordinates are labels, not physical substances.** The particle does not “have” a negative position; negative simply means “on the negative side of the chosen origin.”

3) **The particle model is a choice.** When we write $$x(t)$$ or $$\vec{r}(t)$$, we assume the object’s size/rotation can be neglected for the question at hand. If the object’s orientation matters (e.g., a rolling wheel), a richer model is needed.

4) **Some quantities are less sensitive to origin choices.** Position changes if you move the origin, but displacement does not. Later, you will see that velocity and acceleration are also unaffected by shifting the origin by a constant amount.

## Typical examples

1) **1D motion along a hallway.** Choose the door as $$x=0$$ and “toward the window” as positive. A student walking back and forth can have $$x(t)$$ that increases, decreases, and changes sign.

2) **2D motion on a map.** Choose axes east/north and an origin at a landmark. A runner’s position is a pair $$\big(x(t), y(t)\big)$$, or a vector $$\vec{r}(t)$$.

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

At $$t=0$$ the bicycle is 20 m west of the stop sign. At $$t=5\,\text{s}$$ it is 30 m east of the stop sign.

### Step 1: Translate the words into coordinates

“20 m west” means the coordinate is negative:

$$
x(0) = -20\,\text{m}
$$

“30 m east” means the coordinate is positive:

$$
x(5) = +30\,\text{m}
$$

### Step 2: Compute displacement

$$
\Delta x = x(5) - x(0) = 30 - (-20) = 50\,\text{m}
$$

Interpretation: the bicycle’s net change in position is 50 m to the east (in this chosen coordinate sense).

### Step 3: (Preview) Compute average velocity over the interval

Average velocity in 1D is displacement divided by elapsed time:

$$
v_{\text{avg}} = \frac{\Delta x}{\Delta t} = \frac{50\,\text{m}}{5\,\text{s}} = 10\,\text{m/s}
$$

This is a *kinematic* statement about how position changed; it does not yet explain what caused the motion.

### Step 4: Change the origin and verify what changes

Now choose a new origin at a tree that is 10 m east of the stop sign. In the old coordinates, the tree is at:

$$
x_0 = +10\,\text{m}
$$

Define the new coordinate:

$$
x'(t) = x(t) - x_0
$$

Compute the bicycle’s positions in the new coordinates:

$$
x'(0) = x(0) - 10 = -20 - 10 = -30\,\text{m}
$$

$$
x'(5) = x(5) - 10 = 30 - 10 = 20\,\text{m}
$$

Compute displacement in the new coordinates:

$$
\Delta x' = x'(5) - x'(0) = 20 - (-30) = 50\,\text{m}
$$

The numerical positions changed (because the origin moved), but the displacement did not. This is exactly what you should expect: displacement compares two positions within the *same* frame, so shifting the origin by a constant cancels out.

## Mini recap

- A reference frame specifies an origin, axes (positive directions), and a clock.
- Position is frame-dependent: $$x(t)$$ in 1D, $$\vec{r}(t)$$ in 2D/3D.
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

In 2D we commonly choose perpendicular axes with unit vectors $$\hat{i}$$ (x-direction) and $$\hat{j}$$ (y-direction). A general vector can be written as:

$$
\vec{A} = A_x\,\hat{i} + A_y\,\hat{j}
$$

The numbers $$A_x$$ and $$A_y$$ are the **components** of $$\vec{A}$$ in this coordinate system.

### Magnitude (length) of a vector

The magnitude of $$\vec{A}$$ is:

$$
|\vec{A}| = \sqrt{A_x^2 + A_y^2}
$$

This is just the Pythagorean theorem: components form a right triangle.

### Position vector and displacement vector

The position of a particle in the plane can be described by a position vector:

$$
\vec{r}(t) = x(t)\,\hat{i} + y(t)\,\hat{j}
$$

If the particle is at positions $$\vec{r}(t_1)$$ and $$\vec{r}(t_2)$$ at two times, the **displacement vector** is:

$$
\Delta\vec{r} = \vec{r}(t_2) - \vec{r}(t_1)
$$

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

$$
\vec{A} + \vec{B} = (A_x+B_x)\,\hat{i} + (A_y+B_y)\,\hat{j}.
$$

This is the practical reason we use components: many geometric vector rules reduce to ordinary arithmetic once axes are chosen.

### Why velocity, acceleration, and force are vectors

If position in 2D/3D is a vector function of time, then its time-derivatives are also vectors:

$$
\vec{v}(t) = \frac{d\vec{r}}{dt}, \qquad \vec{a}(t) = \frac{d\vec{v}}{dt} = \frac{d^2\vec{r}}{dt^2}.
$$

Forces model interactions that “push” or “pull” in a direction, so force is also a vector quantity:

$$
\vec{F}
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
\vec{r}(t_1) = (2\,\text{m})\,\hat{i} + (1\,\text{m})\,\hat{j}.
$$

At a later time $$t_2$$ its position is

$$
\vec{r}(t_2) = (8\,\text{m})\,\hat{i} + (5\,\text{m})\,\hat{j}.
$$

Assume $$t_2 - t_1 = 3\,\text{s}$$.

### Step 1: Compute the displacement vector

$$
\Delta\vec{r} = \vec{r}(t_2) - \vec{r}(t_1)
$$

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

Let $$\theta$$ be the angle measured from the +x axis toward the +y axis. Then:

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
- Describe planar motion using a position vector $$\vec{r}(t)$$ or component functions $$x(t), y(t)$$.
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
\vec{r}(t) = x(t)\,\hat{i} + y(t)\,\hat{j}
$$

Equivalently, you can specify the pair of component functions:

$$
x(t), \qquad y(t).
$$

This is the **law of motion**: it tells you where the particle is at each time.

### Trajectory as a geometric set

The **trajectory** is the set of points in the plane that the particle occupies at some time:

$$
\{(x(t), y(t)) \;\text{for all relevant } t\}.
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
x(t) = 2t, \qquad y(t) = t^2,
$$

for $$t \ge 0$$.

### Step 1: Identify what the law of motion tells you

At each time $$t$$, the position is:

$$
\vec{r}(t) = (2t)\,\hat{i} + (t^2)\,\hat{j}.
$$

This already answers questions like “Where is the particle at $$t=3\,\text{s}$$?”:

$$
x(3)=6, \qquad y(3)=9.
$$

### Step 2: Find the trajectory by eliminating time

From $$x(t)=2t$$ we solve for $$t$$:

$$
t = \frac{x}{2}.
$$

Substitute into $$y(t)=t^2$$:

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

$$
\tilde{x}(t) = 2t^2, \qquad \tilde{y}(t) = t^4,
$$

for $$t \ge 0$$.

Eliminate time again. From $$\tilde{x}(t)=2t^2$$:

$$
t^2 = \frac{\tilde{x}}{2}.
$$

Then

$$
\tilde{y} = t^4 = \left(t^2\right)^2 = \left(\frac{\tilde{x}}{2}\right)^2 = \frac{\tilde{x}^2}{4}.
$$

So the **trajectory is the same parabola**, but the timing is different: the second motion moves along the curve more slowly near the origin (because $$\tilde{x}(t)$$ grows like $$t^2$$, not like $$t$$).

### Step 4: What did the curve equation fail to tell you?

The curve

$$
y = \frac{x^2}{4}
$$

does not tell you:

- whether the particle reaches a given point at time 1 s or 10 s,
- how fast it moves along the curve at a given moment,
- whether it ever stops or reverses direction (in other examples).

That information lives in the full functions $$x(t), y(t)$$.

## Mini recap

- The **law of motion** specifies position as a function of time:

$$
\vec{r}(t) = x(t)\,\hat{i} + y(t)\,\hat{j}.
$$

- The **trajectory** is the set of points visited in space; you can sometimes find it by eliminating $$t$$.
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

- instantaneous velocity: the velocity “at time $$t$$,” which is the limit of average velocity over smaller and smaller time intervals.

## Mathematical formulation

### Average velocity (1D)

If the position in 1D is $$x(t)$$, then over the interval from $$t_1$$ to $$t_2$$:

$$
v_{\text{avg}} = \frac{\Delta x}{\Delta t} = \frac{x(t_2)-x(t_1)}{t_2-t_1}.
$$

This is a single number (with sign) describing the net rate of change over that interval.

### Average velocity (vector form)

In 2D/3D, position is a vector $$\vec{r}(t)$$. Average velocity is:

$$
\vec{v}_{\text{avg}} = \frac{\Delta\vec{r}}{\Delta t} = \frac{\vec{r}(t_2)-\vec{r}(t_1)}{t_2-t_1}.
$$

### Instantaneous velocity as a limit (definition)

Instantaneous velocity at time $$t$$ is the limit of average velocity as the time interval shrinks to zero:

$$
v(t) = \lim_{\Delta t\to 0} \frac{x(t+\Delta t)-x(t)}{\Delta t}.
$$

This is exactly the derivative of $$x(t)$$:

$$
v(t) = \frac{dx}{dt}.
$$

In vector form:

$$
\vec{v}(t) = \frac{d\vec{r}}{dt}.
$$

### Graphical meaning (slope)

On a graph of $$x$$ versus $$t$$:

- the average velocity over $$[t_1,t_2]$$ is the **slope of the secant line** connecting the two points,
- the instantaneous velocity at $$t$$ is the **slope of the tangent line** at that point.

So:

- steep upward slope → large positive velocity,
- flat tangent → zero velocity,
- downward slope → negative velocity.

### Speed vs velocity

In 1D:

$$
\text{speed} = |v(t)|.
$$

In 2D/3D:

$$
\text{speed} = |\vec{v}(t)|.
$$

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

$$
x(t) = 4t - t^2
$$

where $$x$$ is in meters and $$t$$ is in seconds.

### Step 1: Compute average velocity on a time interval

Find the average velocity from $$t_1=1\,\text{s}$$ to $$t_2=3\,\text{s}$$.

Compute positions:

$$
x(1) = 4(1) - 1^2 = 3\,\text{m},
$$

$$
x(3) = 4(3) - 3^2 = 12 - 9 = 3\,\text{m}.
$$

So displacement is zero:

$$
\Delta x = x(3)-x(1) = 0.
$$

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

At $$t=1\,\text{s}$$:

$$
v(1) = 4 - 2 = 2\,\text{m/s}.
$$

At $$t=3\,\text{s}$$:

$$
v(3) = 4 - 6 = -2\,\text{m/s}.
$$

So the particle is moving in the positive direction at $$t=1$$ and in the negative direction at $$t=3$$.

### Step 3: Find the turning time (where velocity is zero)

Set $$v(t)=0$$:

$$
4 - 2t = 0 \;\Rightarrow\; t = 2\,\text{s}.
$$

At $$t=2\,\text{s}$$, the particle’s velocity is zero: it is the instant when the motion reverses direction.

## Mini recap

- Average velocity:

$$
v_{\text{avg}} = \frac{x(t_2)-x(t_1)}{t_2-t_1}, \qquad \vec{v}_{\text{avg}} = \frac{\vec{r}(t_2)-\vec{r}(t_1)}{t_2-t_1}.
$$

- Instantaneous velocity is the derivative:

$$
v(t) = \frac{dx}{dt}, \qquad \vec{v}(t) = \frac{d\vec{r}}{dt}.
$$

- Graphically: velocity is the slope of the $$x(t)$$ graph (secant for average, tangent for instantaneous).
- Speed is magnitude: $$|v|$$ or $$|\vec{v}|$$; velocity includes sign/direction.

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

- kinematics describes motion using $$x(t), v(t), a(t)$$,
- dynamics later determines $$\vec{a}(t)$$ from forces.

So you want a clear definition and reliable interpretation now.

## Core idea

Velocity can change in two ways:

1) **Magnitude change:** speed increases or decreases (speeding up / slowing down).
2) **Direction change:** even if speed stays constant, a change in direction means the velocity vector changes.

Acceleration captures both, because it measures change in velocity.

## Mathematical formulation

### Average acceleration (1D)

If velocity in 1D is $$v(t)$$, then over $$[t_1,t_2]$$:

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

- On a graph of $$v$$ versus $$t$$, acceleration is the slope:
  - average acceleration → slope of the secant line,
  - instantaneous acceleration → slope of the tangent line.

This is the velocity-graph analog of the “velocity is slope of the position graph” idea.

## Interpretation

### Sign and “speeding up” in 1D

In 1D, acceleration and velocity are signed. Whether the particle is speeding up depends on the *combination* of signs:

- If $$v(t)$$ and $$a(t)$$ have the **same sign**, speed increases.
- If $$v(t)$$ and $$a(t)$$ have **opposite signs**, speed decreases.

This is worth practicing, because it prevents the common mistake “negative acceleration means slowing down.” Negative acceleration only means “acceleration points in the negative axis direction.”

### Direction change without speed change (vector idea)

In 2D/3D, a velocity vector can change even if its magnitude stays the same. If speed is constant but direction rotates, then $$\vec{v}(t)$$ changes and $$\vec{a}(t)$$ is nonzero.

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

$$
v(t) = 6 - 3t
$$

with $$v$$ in m/s and $$t$$ in s.

### Step 1: Find the acceleration

Differentiate:

$$
a(t) = \frac{dv}{dt} = -3.
$$

So acceleration is constant:

$$
a(t) = -3\,\text{m/s}^2.
$$

### Step 2: Interpret the sign physically

At $$t=0$$:

$$
v(0)=6\,\text{m/s} > 0,
$$

so the particle initially moves in the positive direction. Since $$a=-3<0$$, the acceleration points in the negative direction, opposite to the motion, so the particle initially **slows down**.

### Step 3: Find when it stops (turning time in velocity)

Set $$v(t)=0$$:

$$
6 - 3t = 0 \;\Rightarrow\; t = 2\,\text{s}.
$$

At $$t=2\,\text{s}$$ the instantaneous velocity is zero.

### Step 4: What happens after the stop?

For $$t>2$$:

$$
v(t) = 6 - 3t < 0,
$$

so the particle moves in the negative direction. Acceleration is still negative, so now velocity and acceleration have the same sign: the particle **speeds up** (in the negative direction).

### Step 5: Compute an average acceleration check

Compute average acceleration from $$t_1=0$$ to $$t_2=4$$:

$$
v(0)=6, \qquad v(4)=6-12=-6.
$$

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
- Interpret uniform motion on $$x(t)$$ and $$v(t)$$ graphs.
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

$$
v(t) = v_0 \quad \text{(constant)}.
$$

Then position is:

$$
x(t) = x_0 + v_0(t-t_0).
$$

Often we choose $$t_0=0$$ for convenience:

$$
x(t) = x_0 + v_0 t.
$$

Acceleration is the derivative of velocity:

$$
a(t) = \frac{dv}{dt} = 0.
$$

### Vector form (2D/3D)

If velocity is a constant vector $$\vec{v}_0$$, then:

$$
\vec{r}(t) = \vec{r}_0 + \vec{v}_0(t-t_0).
$$

This describes straight-line motion at constant speed in a fixed direction.

### Graphical signatures

For uniform motion in 1D:

- $$x(t)$$ is a straight line; its slope is $$v_0$$.
- $$v(t)$$ is a horizontal line at $$v_0$$.
- $$a(t)$$ is identically zero.

## Interpretation

- The sign of $$v_0$$ tells you direction along your chosen axis.
  - $$v_0>0$$: motion in the positive direction.
  - $$v_0<0$$: motion in the negative direction.
- The magnitude $$|v_0|$$ is the constant speed (in 1D).
- The same physical motion can have different coordinate descriptions if you shift the origin, but the constant velocity value does not change under an origin shift.

## Typical examples

1) **Cruising car (1D approximation):** A car moves at approximately constant speed on a straight highway segment. Over that segment, uniform motion is a good model.

2) **Moving walkway:** If you walk at constant speed relative to the walkway, and the walkway moves at constant speed relative to the ground, then your ground velocity is constant too (uniform motion), found by adding velocities (developed later).

3) **Two trains on parallel tracks:** Catch-up problems are uniform-motion problems when both trains maintain constant velocities.

## Common mistakes

- Using distance traveled in place of displacement when computing $$x(t)$$.
- Forgetting sign conventions: writing $$x(t)=x_0+|v_0|t$$ even when motion is in the negative direction.
- Mixing time origins: using $$x_0$$ measured at one time while using a formula with a different $$t_0$$.
- Assuming that “constant speed” automatically means “uniform motion” in 2D/3D. Constant speed with changing direction is **not** uniform motion because velocity is not constant.

## Worked example

Two cyclists move along a straight road (1D). Choose the x-axis along the road, with positive direction to the east.

- Cyclist A starts at the origin at $$t=0$$ and rides east at constant velocity $$v_A = 6\,\text{m/s}$$.
- Cyclist B starts 120 m east of the origin at $$t=0$$ and rides west at constant velocity $$v_B = -4\,\text{m/s}$$.

Find when and where they meet.

### Step 1: Write position functions

For cyclist A:

$$
x_A(t) = 0 + (6)t = 6t.
$$

For cyclist B:

$$
x_B(t) = 120 + (-4)t = 120 - 4t.
$$

### Step 2: Solve the meeting condition

They meet when positions are equal:

$$
x_A(t) = x_B(t).
$$

So:

$$
6t = 120 - 4t.
$$

$$
10t = 120 \;\Rightarrow\; t = 12\,\text{s}.
$$

### Step 3: Find the meeting position

Substitute back:

$$
x = x_A(12) = 6(12) = 72\,\text{m}.
$$

Interpretation: they meet 72 m east of the origin, 12 s after $$t=0$$.

### Step 4: Quick reasonableness check

The closing speed is:

$$
v_{\text{close}} = v_A - v_B = 6 - (-4) = 10\,\text{m/s}.
$$

Initial separation is 120 m, so meeting time should be:

$$
t = \frac{120}{10} = 12\,\text{s},
$$

consistent.

## Mini recap

- Uniform motion means **constant velocity** and **zero acceleration**.
- In 1D:

$$
x(t) = x_0 + v_0(t-t_0), \qquad v(t)=v_0, \qquad a(t)=0.
$$

- On graphs: $$x(t)$$ is linear; $$v(t)$$ is constant; $$a(t)=0$$.
- Keep sign conventions explicit; displacement (not distance) controls the position function.

<!-- SOURCE: lecture/kinematics/07_uniformly_accelerated_motion.md -->

# Uniformly accelerated motion (constant acceleration)

## Learning goals

- Recognize when the **constant-acceleration model** is appropriate and state its assumptions.
- Derive and use the standard relations for $$v(t)$$ and $$x(t)$$ under constant $$a$$.
- Use initial conditions correctly and interpret the meaning of $$x_0$$ and $$v_0$$.
- Solve basic constant-acceleration problems without “formula hunting,” and check results by units/signs.

## Why this matters

Constant acceleration is the next simplest model after uniform motion. It appears everywhere:

- near-Earth free fall (approximately constant $$g$$, neglecting air resistance),
- vehicles speeding up or braking at roughly steady rate,
- motion segments that can be approximated as having constant acceleration.

Many students memorize “the kinematic equations” without understanding where they come from. That leads to sign errors and applying them when the assumptions are not satisfied. Here we will derive them from the definitions of velocity and acceleration.

## Core idea

If acceleration is constant, then velocity changes at a constant rate, and position is a quadratic function of time.

The model is a statement about time dependence:

$$
a(t) = a_0 \quad \text{(constant)}.
$$

From this one assumption, the entire motion follows once you specify initial conditions.

## Mathematical formulation

### Assumptions (say them explicitly when you use the model)

We assume:

1. Motion is along a straight line (1D) or we are analyzing one component.
2. Acceleration is constant in time over the interval of interest:

$$
a(t) = a_0.
$$

3. The quantities $$x_0$$ and $$v_0$$ are the position and velocity at a chosen reference time $$t_0$$.

### Step 1: Derive velocity as a function of time

By definition:

$$
a(t) = \frac{dv}{dt}.
$$

If $$a(t)=a_0$$ is constant, then:

$$
\frac{dv}{dt} = a_0.
$$

Integrate from $$t_0$$ to $$t$$:

$$
\int_{v(t_0)}^{v(t)} dv = \int_{t_0}^{t} a_0\,dt.
$$

This gives:

$$
v(t) - v(t_0) = a_0(t-t_0).
$$

Define $$v_0 = v(t_0)$$, so:

$$
v(t) = v_0 + a_0(t-t_0).
$$

If we choose $$t_0=0$$:

$$
v(t) = v_0 + a_0 t.
$$

### Step 2: Derive position as a function of time

Velocity is the derivative of position:

$$
v(t) = \frac{dx}{dt}.
$$

Using $$v(t)=v_0+a_0(t-t_0)$$:

$$
\frac{dx}{dt} = v_0 + a_0(t-t_0).
$$

Integrate from $$t_0$$ to $$t$$:

$$
\int_{x(t_0)}^{x(t)} dx = \int_{t_0}^{t} \left(v_0 + a_0(\tau-t_0)\right)d\tau.
$$

Compute the integral:

$$
x(t) - x(t_0) = v_0(t-t_0) + \frac{1}{2}a_0(t-t_0)^2.
$$

Define $$x_0 = x(t_0)$$:

$$
x(t) = x_0 + v_0(t-t_0) + \frac{1}{2}a_0(t-t_0)^2.
$$

If $$t_0=0$$:

$$
x(t) = x_0 + v_0 t + \frac{1}{2}a_0 t^2.
$$

### A useful relation without time (optional but common)

Sometimes you want a relation between velocity and position when acceleration is constant. Start from:

$$
v(t) = v_0 + a_0(t-t_0),
$$

and

$$
x(t) - x_0 = v_0(t-t_0) + \frac{1}{2}a_0(t-t_0)^2.
$$

Eliminate $$t-t_0$$. Let $$\Delta t = t-t_0$$. Then:

$$
v - v_0 = a_0\Delta t \quad \Rightarrow\quad \Delta t = \frac{v-v_0}{a_0}.
$$

Substitute into the position equation:

$$
x - x_0 = v_0\left(\frac{v-v_0}{a_0}\right) + \frac{1}{2}a_0\left(\frac{v-v_0}{a_0}\right)^2.
$$

After simplification, you obtain:

$$
v^2 = v_0^2 + 2a_0(x-x_0).
$$

This relation is powerful, but it is still based on the same constant-acceleration assumption.

## Interpretation

- Constant acceleration means **velocity changes linearly** in time.
- Position is a quadratic in time; its graph is a parabola in the $$x$$–$$t$$ plane.
- Initial conditions matter:
  - $$x_0$$ is where the particle is at the chosen reference time.
  - $$v_0$$ is the velocity at that same time.
  - changing the choice of $$t_0$$ changes the numerical values of $$x_0$$ and $$v_0$$, but not the physical motion.

## Typical examples

1) **Braking car (1D):** If deceleration is approximately constant, you can predict stopping time and stopping distance.

2) **Free fall preview:** Over not-too-large height changes near Earth, acceleration is approximately constant and equal to $$\pm g$$ depending on your sign convention.

3) **Piecewise motion preview:** Real motion is often “constant acceleration for a while, then different constant acceleration,” which we will treat later as piecewise-defined motion.

## Common mistakes

- Using constant-acceleration formulas when acceleration is not constant (e.g., strong air resistance, changing engine force).
- Forgetting that the sign of $$a_0$$ depends on the chosen axis direction.
- Plugging numbers into a memorized equation without stating $$x_0, v_0, t_0$$ (mixing different reference times).
- Using $$v^2 = v_0^2 + 2a_0(x-x_0)$$ and then forgetting that squaring hides sign information: $$v$$ can be positive or negative depending on direction.
- Confusing “acceleration is constant” with “velocity is constant.” Constant acceleration generally means velocity is changing.

## Worked example

A train moves along a straight track. At $$t=0$$, it passes a marker with:

$$
x_0 = 0, \qquad v_0 = 12\,\text{m/s}.
$$

It then accelerates uniformly with:

$$
a_0 = 0.80\,\text{m/s}^2
$$

for 15 s.

1) Find its velocity and position at $$t=15\,\text{s}$$.  
2) How far does it travel during the *last* 5 s of this interval?

### Step 1: Velocity after 15 s

Use:

$$
v(t) = v_0 + a_0 t.
$$

So:

$$
v(15) = 12 + (0.80)(15) = 12 + 12 = 24\,\text{m/s}.
$$

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

$$
(12)(15)=180,
$$

$$
\frac{1}{2}(0.80)(15)^2 = 0.40\cdot 225 = 90.
$$

Therefore:

$$
x(15) = 180 + 90 = 270\,\text{m}.
$$

### Step 3: Distance traveled in the last 5 seconds

The last 5 s is the interval from $$t=10$$ to $$t=15$$.

Compute:

$$
x(10) = (12)(10) + \frac{1}{2}(0.80)(10)^2 = 120 + 0.40\cdot 100 = 120 + 40 = 160\,\text{m}.
$$

Then:

$$
\Delta x = x(15)-x(10) = 270 - 160 = 110\,\text{m}.
$$

### Step 4: Quick checks

- Units: each term in $$x(t)$$ has units of meters.
- Reasonableness: the average velocity over the 15 s is roughly halfway between 12 and 24 m/s, i.e. about 18 m/s, so distance should be about $$18\cdot 15 = 270$$ m, matching.

## Mini recap

- Constant acceleration model:

$$
a(t)=a_0.
$$

- Derived relations (with reference time $$t_0$$):

$$
v(t) = v_0 + a_0(t-t_0),
$$

$$
x(t) = x_0 + v_0(t-t_0) + \frac{1}{2}a_0(t-t_0)^2.
$$

- Time-free relation (still constant-acceleration only):

$$
v^2 = v_0^2 + 2a_0(x-x_0).
$$

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
- write $$a$$ with the correct sign,
- interpret results physically (especially velocity sign and turning points).

## Core idea

In the ideal free-fall model near Earth:

- the only significant influence is gravity,
- the acceleration has (approximately) constant magnitude $$g$$,
- and it points downward.

So the vertical motion can be modeled as 1D constant-acceleration motion.

This is a **model**, so it comes with assumptions:

- height changes are not so large that $$g$$ varies significantly,
- air resistance is neglected (or is small over the time interval),
- the object’s rotation/shape is not relevant (particle model).

## Mathematical formulation

### Choose a sign convention (two common choices)

You must choose an axis direction and keep it consistent.

**Choice A (often used): upward is positive.**  
Then the acceleration due to gravity is:

$$
a(t) = -g.
$$

**Choice B: downward is positive.**  
Then:

$$
a(t) = +g.
$$

Both are correct; the physics is the same. The algebra only works if you stay consistent.

In either case, once you have the correct sign for $$a$$, you can use the constant-acceleration relations from the previous section.

### Equations (using Choice A: upward positive)

Let $$t_0=0$$ for simplicity. With $$a=-g$$:

Velocity:

$$
v(t) = v_0 - gt.
$$

Position:

$$
x(t) = x_0 + v_0 t - \frac{1}{2}gt^2.
$$

Time-free relation:

$$
v^2 = v_0^2 - 2g(x-x_0).
$$

### Meaning of signs

- If $$v>0$$ (in Choice A), the object is moving upward.
- If $$v<0$$, it is moving downward.
- The acceleration is negative at all times in free fall (Choice A), even at the top, because gravity still points downward.

## Interpretation

### The “top of the motion” is not zero acceleration

When an object is thrown upward, there is an instant at the highest point where:

$$
v = 0.
$$

But acceleration is still:

$$
a = -g.
$$

Velocity can be zero at an instant without acceleration being zero. This is the key conceptual point that prevents a huge class of errors.

### Free fall vs “falling with air resistance”

With significant air resistance, acceleration is not constant: it changes with speed and can approach zero at terminal velocity. In that situation, the constant-acceleration equations are not valid; you need a different model (later, in dynamics).

## Typical examples

1) **Dropped from rest:** $$v_0=0$$ at release, acceleration is constant downward. Solve for time to hit the ground and impact speed.

2) **Thrown upward:** $$v_0>0$$ (if up is positive). Find time to reach maximum height, maximum height itself, and speed on return to the starting point.

3) **Thrown downward:** $$v_0<0$$ (in Choice A). Same equations; the sign tells the initial direction.

## Common mistakes

- Switching sign conventions mid-solution (“up is positive” in one equation, “down is positive” in another).
- Setting acceleration to zero at the top because velocity is zero.
- Using $$g$$ as a signed quantity sometimes and as a magnitude other times without stating which.
- Forgetting that the quadratic position equation can yield two times (on the way up and on the way down) for the same height.
- Using the time-free formula and then choosing the wrong sign for $$v$$ after taking a square root.

## Worked example

An object is thrown straight upward from a balcony. Choose upward as positive (Choice A). At release:

$$
x_0 = 12\,\text{m}, \qquad v_0 = 14\,\text{m/s}.
$$

Take:

$$
g = 9.8\,\text{m/s}^2.
$$

1) How long until the object reaches its highest point?  
2) What is the maximum height?  
3) When does it hit the ground ($$x=0$$), and what is its velocity just before impact?

### Step 1: Time to the highest point

At the top, $$v=0$$. Use:

$$
v(t) = v_0 - gt.
$$

Set to zero:

$$
0 = 14 - 9.8t \;\Rightarrow\; t_{\text{top}} = \frac{14}{9.8} \approx 1.43\,\text{s}.
$$

### Step 2: Maximum height

Use:

$$
x(t) = x_0 + v_0 t - \frac{1}{2}gt^2.
$$

At $$t=t_{\text{top}}$$:

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

Set $$x(t)=0$$:

$$
0 = 12 + 14t - \frac{1}{2}(9.8)t^2.
$$

Multiply by 2 to simplify:

$$
0 = 24 + 28t - 9.8t^2.
$$

Rearrange:

$$
9.8t^2 - 28t - 24 = 0.
$$

Solve the quadratic:

$$
t = \frac{28 \pm \sqrt{(-28)^2 - 4(9.8)(-24)}}{2(9.8)}.
$$

Compute the discriminant:

$$
(-28)^2 - 4(9.8)(-24) = 784 + 940.8 = 1724.8.
$$

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

$$
v(t) = v_0 - gt.
$$

So:

$$
v_{\text{hit}} = 14 - 9.8(3.55) \approx 14 - 34.79 \approx -20.8\,\text{m/s}.
$$

Interpretation: the negative sign means the object is moving downward at impact (consistent with the chosen axis).

## Mini recap

- Free fall (ideal) near Earth is constant acceleration of magnitude $$g$$ directed downward.
- Choose a sign convention and keep it consistent. If upward is positive:

$$
a=-g, \qquad v(t)=v_0-gt, \qquad x(t)=x_0+v_0t-\frac{1}{2}gt^2.
$$

- At the top of an upward throw: $$v=0$$ but $$a=-g$$ still.
- Watch for two times at the same height and for sign loss when taking square roots in $$v^2$$ relations.

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

Similarly, you can specify $$v(t)$$ or $$a(t)$$ piecewise.

### Matching conditions at a boundary

Let the switch occur at $$t=t_1$$.

**Position continuity** means:

$$
\lim_{t\to t_1^-} x_1(t) = x_2(t_1).
$$

In many practical problems this is simply:

$$
x_1(t_1) = x_2(t_1).
$$

**Velocity continuity** means:

$$
\lim_{t\to t_1^-} v_1(t) = v_2(t_1).
$$

If velocity is discontinuous, the acceleration contains an impulse-like effect and the model is no longer “ordinary constant acceleration.” In introductory kinematics problems, velocity jumps are usually not intended unless explicitly stated (e.g., a bounce or a collision).

### A practical workflow for piecewise problems

1) Choose an axis and sign convention.  
2) Write the kinematic rule for the first interval (often constant $$a$$ or constant $$v$$).  
3) Use initial conditions to determine constants.  
4) Evaluate $$x$$ and $$v$$ at the switching time to generate the initial conditions for the next interval.  
5) Repeat.

## Interpretation

- A piecewise model describes a **single motion** with different regimes.
- Position continuity is a basic physical requirement for ordinary motion.
- Velocity continuity is typical unless an impulsive event occurs.
- Acceleration can change abruptly because it reflects changing influences (engine on/off, braking, friction changes).

## Typical examples

1) **Accelerate then cruise:** constant $$a$$ for a while, then constant $$v$$ after reaching a target speed.

2) **Cruise then brake:** constant $$v$$, then constant negative $$a$$ until stopping.

3) **Motion with a “turnaround”:** accelerate negatively until velocity becomes zero, then continue with negative velocity (a reversal) — still continuous, no teleportation.

## Common mistakes

- Using the same symbol $$x_0, v_0$$ for different intervals without clarifying which interval’s initial time they belong to.
- Forgetting to carry the end-of-interval position into the next interval (creating a jump in $$x$$).
- Assuming velocity is the same at the boundary even when acceleration was nonzero (or vice versa).
- Solving each interval independently with $$t=0$$ reset, then mixing times without converting (time variables must refer to the same clock unless you explicitly reparameterize).
- Interpreting “piecewise acceleration” as “piecewise position” automatically; you must integrate and apply boundary conditions.

## Worked example

A car moves along a straight road (1D). Choose x-axis along the road, positive forward. The motion has three stages:

1) **Stage I (accelerate):** from $$t=0$$ to $$t=6\,\text{s}$$ the car accelerates uniformly from rest with

$$
a = 2.0\,\text{m/s}^2.
$$

2) **Stage II (cruise):** from $$t=6\,\text{s}$$ to $$t=16\,\text{s}$$ the car moves at constant velocity.

3) **Stage III (brake):** from $$t=16\,\text{s}$$ onward it brakes with constant acceleration

$$
a = -3.0\,\text{m/s}^2
$$

until it stops.

Find:

- the piecewise formulas for $$v(t)$$ and $$x(t)$$ (with $$x(0)=0$$),
- the total distance traveled until the car stops.

### Step 0: Initial condition

At $$t=0$$:

$$
x(0)=0, \qquad v(0)=0.
$$

### Stage I: $$0 \le t \le 6$$

Velocity:

$$
v(t) = v_0 + at = 0 + (2.0)t = 2t.
$$

Position:

$$
x(t) = x_0 + v_0 t + \frac{1}{2}at^2 = 0 + 0 + \frac{1}{2}(2.0)t^2 = t^2.
$$

Evaluate at the boundary $$t=6$$ to pass initial conditions to Stage II:

$$
v(6) = 2\cdot 6 = 12\,\text{m/s},
$$

$$
x(6) = 6^2 = 36\,\text{m}.
$$

### Stage II: $$6 \le t \le 16$$

Constant velocity equal to the value reached at $$t=6$$:

$$
v(t) = 12\,\text{m/s}.
$$

Position must be continuous and should satisfy $$x(6)=36$$. A convenient form is:

$$
x(t) = x(6) + v(t-6) = 36 + 12(t-6).
$$

Evaluate at $$t=16$$:

$$
x(16) = 36 + 12(16-6) = 36 + 120 = 156\,\text{m},
$$

$$
v(16) = 12\,\text{m/s}.
$$

### Stage III: $$t \ge 16$$

Now acceleration is constant $$a=-3.0\,\text{m/s}^2$$ and initial conditions at $$t=16$$ are:

$$
x(16)=156\,\text{m}, \qquad v(16)=12\,\text{m/s}.
$$

Velocity for $$t\ge 16$$:

$$
v(t) = 12 - 3(t-16).
$$

The car stops when $$v(t)=0$$:

$$
0 = 12 - 3(t-16) \;\Rightarrow\; 3(t-16)=12 \;\Rightarrow\; t-16=4.
$$

So stopping time is:

$$
t_{\text{stop}} = 20\,\text{s}.
$$

Position for $$t\ge 16$$:

$$
x(t) = 156 + 12(t-16) + \frac{1}{2}(-3)(t-16)^2
$$

At stopping time $$t=20$$ (so $$t-16=4$$):

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
- Workflow: solve interval 1 → evaluate $$x, v$$ at boundary → use them as initial conditions for interval 2.
- Acceleration can change abruptly between intervals without being unphysical.

<!-- SOURCE: lecture/kinematics/10_motion_from_given_x_of_t.md -->

# Motion from a given $$x(t)$$

## Learning goals

- Given a position function $$x(t)$$, compute velocity $$v(t)$$ and acceleration $$a(t)$$ by differentiation.
- Use the sign of $$v(t)$$ to determine **direction of motion** and intervals of increasing/decreasing position.
- Find **turning times** (where the motion reverses direction) and interpret them correctly.
- Connect algebraic results to graphical ideas (slope and curvature of $$x(t)$$).

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

- $$v>0$$ means motion in the positive direction,
- $$v<0$$ means motion in the negative direction,
- $$v=0$$ can indicate a stop or a turning point (but you must check what happens around it).

## Mathematical formulation

Given $$x(t)$$, define:

$$
v(t) = \frac{dx}{dt},
$$

$$
a(t) = \frac{dv}{dt} = \frac{d^2x}{dt^2}.
$$

### Turning times and monotonicity

Turning times are candidates where velocity is zero:

$$
v(t)=0.
$$

To decide what happens at such a time $$t^*$$, check the sign of $$v(t)$$ just before and just after $$t^*$$:

- if $$v$$ changes from positive to negative, position reaches a local maximum and motion reverses from + to −,
- if $$v$$ changes from negative to positive, position reaches a local minimum and motion reverses from − to +,
- if $$v$$ is zero but does not change sign, the particle may “pause” without reversing (possible in some functions).

### Graphical connection

On the $$x$$ vs $$t$$ graph:

- $$v(t)$$ is the tangent slope,
- $$a(t)$$ relates to how that slope changes with time (curvature idea).

## Interpretation

- Knowing $$x(t)$$ gives full kinematic information in 1D (and similarly for each component in 2D/3D).
- Zero velocity at an instant does not necessarily mean the particle stays at rest for a while; it may be a momentary turning point.
- Acceleration sign does not directly tell you direction of motion; it tells you how velocity changes.

## Typical examples

1) **Quadratic position:** $$x(t)=x_0+v_0t+\frac{1}{2}at^2$$ produces linear velocity and constant acceleration. This is the constant-acceleration model seen earlier.

2) **Cubic position:** can produce multiple turning points (stop-and-go behavior).

3) **Sinusoidal position (preview):** gives oscillatory velocity and acceleration; velocity is zero at extrema of position.

## Common mistakes

- Confusing “position is zero” with “velocity is zero.” The particle can pass through the origin with nonzero speed.
- Finding times when $$v(t)=0$$ and automatically calling them “turning points” without checking sign change.
- Interpreting negative acceleration as “slowing down” without considering the sign of velocity.
- Differentiation errors (especially product/chain rule) that then propagate into wrong physical conclusions.
- Forgetting units: if $$x$$ is in meters and $$t$$ in seconds, then $$v$$ must be in m/s and $$a$$ in m/s².

## Worked example

A particle moves along a line with position:

$$
x(t) = t^3 - 6t^2 + 9t
$$

with $$x$$ in meters and $$t$$ in seconds. Analyze its motion for $$t \ge 0$$:

1) Find $$v(t)$$ and $$a(t)$$.  
2) Determine when the particle is at rest.  
3) Determine intervals of motion direction and find any turning points.

### Step 1: Compute velocity

Differentiate:

$$
v(t) = \frac{dx}{dt} = 3t^2 - 12t + 9.
$$

Factor:

$$
v(t) = 3(t^2 - 4t + 3) = 3(t-1)(t-3).
$$

### Step 2: Compute acceleration

Differentiate velocity:

$$
a(t) = \frac{dv}{dt} = 6t - 12 = 6(t-2).
$$

### Step 3: Find rest times

Rest times satisfy $$v(t)=0$$:

$$
3(t-1)(t-3)=0 \;\Rightarrow\; t=1\,\text{s} \text{ or } t=3\,\text{s}.
$$

So the particle is instantaneously at rest at 1 s and 3 s.

### Step 4: Determine direction of motion (sign of velocity)

Use the factored form $$v(t)=3(t-1)(t-3)$$ and test intervals:

- For $$0 \le t < 1$$: pick $$t=0$$:

$$
v(0)=3(-1)(-3)=9>0,
$$

so motion is in the positive direction.

- For $$1 < t < 3$$: pick $$t=2$$:

$$
v(2)=3(1)(-1)=-3<0,
$$

so motion is in the negative direction.

- For $$t>3$$: pick $$t=4$$:

$$
v(4)=3(3)(1)=9>0,
$$

so motion is again in the positive direction.

### Step 5: Identify turning points

Velocity changes sign at both rest times:

- At $$t=1$$: $$v$$ goes from positive to negative → turning point (local maximum of $$x(t)$$).
- At $$t=3$$: $$v$$ goes from negative to positive → turning point (local minimum of $$x(t)$$).

To make this concrete, compute the positions:

$$
x(1) = 1 - 6 + 9 = 4\,\text{m},
$$

$$
x(3) = 27 - 54 + 27 = 0\,\text{m}.
$$

So the particle reaches a maximum position of 4 m at 1 s, then moves back and reaches 0 m at 3 s, then moves forward again.

### Step 6: Interpret acceleration briefly

Acceleration:

$$
a(t)=6(t-2)
$$

is negative for $$t<2$$ and positive for $$t>2$$. This tells you how the velocity is changing, but direction of motion is determined by $$v(t)$$, not by the sign of $$a(t)$$ alone.

## Mini recap

- From $$x(t)$$ you get:

$$
v(t)=\frac{dx}{dt}, \qquad a(t)=\frac{d^2x}{dt^2}.
$$

- Rest times satisfy $$v(t)=0$$, but turning points require checking whether $$v$$ changes sign.
- Sign of $$v(t)$$ determines direction in 1D.
- Graphically: $$v$$ is slope of $$x(t)$$; acceleration controls how that slope changes.

<!-- SOURCE: lecture/kinematics/11_motion_from_given_v_of_t.md -->

# Motion from a given $$v(t)$$

## Learning goals

- Reconstruct position $$x(t)$$ from a given velocity function $$v(t)$$ by integration.
- Use an initial condition (e.g., $$x(t_0)=x_0$$) to determine the integration constant.
- Interpret displacement as an **area under the $$v(t)$$ graph**.
- Use the sign of $$v(t)$$ to reason about direction and net displacement.

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

If you know $$v(t)$$ and one initial condition $$x(t_0)=x_0$$, then:

$$
x(t) = x_0 + \int_{t_0}^{t} v(\tau)\,d\tau.
$$

If you perform an indefinite integral:

$$
\int v(t)\,dt = V(t) + C,
$$

then:

$$
x(t) = V(t) + C,
$$

and you determine $$C$$ from $$x(t_0)=x_0$$.

### Displacement as area under the velocity graph

Displacement from $$t_1$$ to $$t_2$$ is:

$$
\Delta x = x(t_2)-x(t_1) = \int_{t_1}^{t_2} v(t)\,dt.
$$

Graphically:

- positive area (where $$v>0$$) adds positive displacement,
- negative area (where $$v<0$$) adds negative displacement.

This is why “back and forth” motion can produce a small net displacement even if the total distance traveled is large.

### Vector extension (brief preview)

In 2D/3D:

$$
\vec{r}(t) = \vec{r}(t_0) + \int_{t_0}^{t} \vec{v}(\tau)\,d\tau,
$$

which is just the component-wise version of the 1D statement.

## Interpretation

- Integrating $$v(t)$$ gives position up to a constant: you need **one position value** to locate the motion in space.
- The integral over an interval gives displacement directly; it does not require you to first find $$x(t)$$ if you only need displacement.
- The sign of $$v(t)$$ tells direction: if $$v<0$$ over an interval, displacement over that interval is negative (for the chosen axis).

## Typical examples

1) **Constant velocity:** $$v(t)=v_0$$ integrates to $$x(t)=x_0+v_0(t-t_0)$$ (uniform motion).

2) **Linear velocity:** $$v(t)=v_0+at$$ integrates to a quadratic $$x(t)$$ (constant acceleration).

3) **Velocity that changes sign:** net displacement depends on signed areas; turning points occur where $$v(t)=0$$ (but you still must interpret).

## Common mistakes

- Forgetting the integration constant / failing to use the initial position to determine it.
- Treating $$\int v(t)\,dt$$ as “distance traveled.” It gives displacement; distance traveled would require integrating $$|v(t)|$$ when motion reverses.
- Mixing up the meaning of “area”: negative velocities produce negative contributions to displacement.
- Resetting time to zero for convenience and then forgetting to translate back to the original clock when combining intervals.
- Dropping units: the integral of (m/s) over s gives meters.

## Worked example

A particle moves along a line with velocity:

$$
v(t) = 4 - t
$$

for $$0 \le t \le 6$$, with $$v$$ in m/s and $$t$$ in s. At $$t=0$$, its position is:

$$
x(0)=2\,\text{m}.
$$

1) Find $$x(t)$$.  
2) Find the displacement from $$t=0$$ to $$t=6$$.  
3) Find the time when it changes direction, and compute the position at that time.

### Step 1: Integrate to get position

Use the reconstruction formula with $$t_0=0$$:

$$
x(t) = x(0) + \int_{0}^{t} (4-\tau)\,d\tau.
$$

Compute the integral:

$$
\int_{0}^{t} (4-\tau)\,d\tau = \left[4\tau - \frac{1}{2}\tau^2\right]_{0}^{t} = 4t - \frac{1}{2}t^2.
$$

So:

$$
x(t) = 2 + 4t - \frac{1}{2}t^2.
$$

### Step 2: Displacement from 0 to 6

Displacement is:

$$
\Delta x = \int_{0}^{6} (4-t)\,dt = \left[4t - \frac{1}{2}t^2\right]_{0}^{6} = 24 - 18 = 6\,\text{m}.
$$

So $$x(6)=x(0)+\Delta x = 2+6 = 8\,\text{m}$$ (consistent with the formula above).

### Step 3: Direction change time

Direction changes when $$v(t)=0$$:

$$
4 - t = 0 \;\Rightarrow\; t=4\,\text{s}.
$$

Compute the position at that time:

$$
x(4) = 2 + 4(4) - \frac{1}{2}(4)^2 = 2 + 16 - 8 = 10\,\text{m}.
$$

Interpretation: from $$t=0$$ to $$t=4$$, velocity is positive and the particle moves in the positive direction; after $$t=4$$, velocity is negative and it moves back.

## Mini recap

- Position from velocity (1D):

$$
x(t) = x_0 + \int_{t_0}^{t} v(\tau)\,d\tau.
$$

- Displacement over an interval:

$$
\Delta x = \int_{t_1}^{t_2} v(t)\,dt
$$

(signed area under $$v(t)$$).

- The integration constant is fixed by an initial position.
- Displacement is not the same as distance traveled when direction changes.

<!-- SOURCE: lecture/kinematics/12_motion_from_given_a_of_t.md -->

# Motion from a given $$a(t)$$

## Learning goals

- Reconstruct $$v(t)$$ from a given acceleration $$a(t)$$ by integration.
- Reconstruct $$x(t)$$ by integrating again, using **initial conditions** to fix constants.
- Understand why two initial conditions are needed to determine a unique position function from $$a(t)$$.
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

- integrating $$a(t)$$ accumulates changes in velocity,
- integrating $$v(t)$$ accumulates changes in position.

Because you integrate twice, you need **two pieces of initial information** to pin down the motion, typically:

$$
v(t_0)=v_0, \qquad x(t_0)=x_0.
$$

## Mathematical formulation

### Step 1: Velocity from acceleration

Given $$a(t)$$ and $$v(t_0)=v_0$$:

$$
v(t) = v_0 + \int_{t_0}^{t} a(\tau)\,d\tau.
$$

### Step 2: Position from velocity

Given also $$x(t_0)=x_0$$:

$$
x(t) = x_0 + \int_{t_0}^{t} v(\tau)\,d\tau.
$$

Combining both steps:

$$
x(t) = x_0 + \int_{t_0}^{t} \left(v_0 + \int_{t_0}^{\tau} a(s)\,ds\right)d\tau.
$$

This expression looks nested, but the workflow is simple: integrate once to get $$v(t)$$, then integrate again to get $$x(t)$$.

### A practical note on constants

If you do indefinite integrals, you will get constants at each step:

$$
v(t) = \int a(t)\,dt + C_1,
$$

$$
x(t) = \int v(t)\,dt + C_2.
$$

Use the initial conditions to determine $$C_1$$ and $$C_2$$. Without them, there are infinitely many motions consistent with the same acceleration law.

## Interpretation

- The integral of acceleration over time gives the **change in velocity**:

$$
v(t_2)-v(t_1) = \int_{t_1}^{t_2} a(t)\,dt.
$$

- The integral of velocity gives **displacement**:

$$
x(t_2)-x(t_1) = \int_{t_1}^{t_2} v(t)\,dt.
$$

- If you only know $$a(t)$$, you cannot locate the motion in space: you still need initial position and velocity.

## Typical examples

1) **Polynomial acceleration:** $$a(t)=kt$$ gives quadratic velocity and cubic position.

2) **Sinusoidal acceleration:** $$a(t)=A\cos(\omega t)$$ leads to sinusoidal velocity and position with phase shifts. This previews periodic motion.

3) **Constant acceleration:** $$a(t)=a_0$$ returns the uniformly accelerated motion formulas from Section 07.

## Common mistakes

- Forgetting one of the two constants (integrating twice but applying only one initial condition).
- Using $$v(t)=\int a(t)dt$$ without adding the initial velocity.
- Using an initial condition at a different time than the one used in the integral limits (mixing $$t_0$$ values).
- Losing sign information: acceleration can be positive or negative depending on the chosen axis.
- Treating the integral of acceleration as “distance” rather than “velocity change.”

## Worked example

An object moves along a line with acceleration:

$$
a(t) = 2t
$$

with $$a$$ in m/s² and $$t$$ in s. At $$t=0$$:

$$
v(0) = 1\,\text{m/s}, \qquad x(0)=0.
$$

1) Find $$v(t)$$ and $$x(t)$$.  
2) Find the displacement from $$t=0$$ to $$t=3$$.

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

$$
v(t) = 1 + t^2.
$$

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

Displacement is $$x(3)-x(0)=x(3)$$:

$$
x(3) = 3 + \frac{1}{3}(27) = 3 + 9 = 12\,\text{m}.
$$

### Optional check (velocity change)

Velocity change from 0 to 3 is:

$$
v(3)-v(0) = (1+9)-1 = 9\,\text{m/s},
$$

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

- You generally need two initial conditions (one for $$v$$, one for $$x$$).
- Integrals have clear meanings:
  - area under $$a(t)$$ gives velocity change,
  - area under $$v(t)$$ gives displacement.

<!-- SOURCE: lecture/kinematics/13_inverse_kinematics_problems.md -->

# Inverse kinematics problems

## Learning goals

- Recognize inverse kinematics tasks: “find the motion law that fits given constraints.”
- Translate verbal/graphical constraints into equations involving $$x(t), v(t), a(t)$$.
- Choose a reasonable **function family** (e.g., polynomial for constant acceleration, sinusoid for periodic motion) and determine its parameters from conditions.
- Identify what extra information is needed when the constraints are insufficient.

## Why this matters

So far you have mostly done “forward” kinematics:

- given $$x(t)$$ → find $$v(t)$$ and $$a(t)$$,
- given $$v(t)$$ or $$a(t)$$ → reconstruct the rest using initial conditions.

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

- constant acceleration → quadratic $$x(t)$$ or linear $$v(t)$$,
- periodic motion → sinusoidal $$x(t)$$,
- “starts and stops at given times” → ensure $$v(t)=0$$ at those times,
- “passes through points” → enforce $$x(t_i)=x_i$$.

## Mathematical formulation

### Common constraint types

Constraints usually come in a few standard forms:

Position at a time:

$$
x(t_i)=x_i
$$

Velocity at a time:

$$
v(t_i)=v_i
$$

Acceleration at a time:

$$
a(t_i)=a_i
$$

Turning time (rest instant):

$$
v(t^*)=0
$$

Total displacement on an interval:

$$
x(t_2)-x(t_1)=\Delta x
$$

Average velocity constraint:

$$
\frac{x(t_2)-x(t_1)}{t_2-t_1} = v_{\text{avg}}
$$

### Picking a model family (examples)

**Constant acceleration assumption**:

$$
x(t)=x_0+v_0(t-t_0)+\frac{1}{2}a_0(t-t_0)^2
$$

Unknown parameters: $$x_0, v_0, a_0$$ (or fewer if some are given).

**Quadratic position model (general)**:

$$
x(t)=At^2+Bt+C
$$

Unknown parameters: $$A, B, C$$.

This is equivalent to constant acceleration because:

$$
v(t)=2At+B, \qquad a(t)=2A.
$$

**Sinusoidal (periodic) model**:

$$
x(t)=x_{\text{eq}} + A\cos(\omega t + \phi)
$$

Unknown parameters: equilibrium offset $$x_{\text{eq}}$$, amplitude $$A$$, angular frequency $$\omega$$, phase $$\phi$$.

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
- whether turning times are actually maxima/minima (check sign change of $$v$$).

## Typical examples

1) **Find a quadratic $$x(t)$$ that passes through three points** $$\big(t_1,x_1\big),\big(t_2,x_2\big),\big(t_3,x_3\big)$$.

2) **Given maximum height and launch time**, infer initial velocity in free fall (using $$v(t_{\text{top}})=0$$).

3) **Given period and amplitude**, write a sinusoidal position function up to a phase choice.

## Common mistakes

- Choosing a model family inconsistent with the assumptions (e.g., using constant-acceleration formulas when the problem implies periodic motion).
- Writing constraints with wrong quantities (e.g., using $$x=0$$ when the statement is about velocity).
- Forgetting that turning times require $$v=0$$, not $$x=0$$.
- Solving for parameters but not checking whether the solution matches the intended physical story (direction, timing).
- Assuming uniqueness without counting constraints vs unknowns.

## Worked example

Assume a particle moves in 1D with **constant acceleration**, and choose $$t_0=0$$. You are told:

- $$x(0)=0$$,
- the particle is instantaneously at rest at $$t=2\,\text{s}$$,
- $$x(2\,\text{s})=12\,\text{m}$$.

Find $$x(t)$$, $$v(t)$$, and $$a$$.

### Step 1: Choose a model family

Constant acceleration means:

$$
x(t) = x_0 + v_0 t + \frac{1}{2}a t^2.
$$

Here $$x_0=x(0)=0$$, so:

$$
x(t) = v_0 t + \frac{1}{2}a t^2.
$$

Velocity is:

$$
v(t) = \frac{dx}{dt} = v_0 + at.
$$

Unknowns: $$v_0$$ and $$a$$ (two unknowns → we need two independent constraints).

### Step 2: Use the “rest at t=2 s” constraint

Rest means $$v(2)=0$$:

$$
0 = v_0 + a(2) \;\Rightarrow\; v_0 = -2a.
$$

### Step 3: Use the position at t=2 s constraint

$$
x(2) = 12 = v_0(2) + \frac{1}{2}a(2)^2 = 2v_0 + 2a.
$$

Substitute $$v_0=-2a$$:

$$
12 = 2(-2a) + 2a = -4a + 2a = -2a.
$$

So:

$$
a = -6\,\text{m/s}^2.
$$

Then:

$$
v_0 = -2a = 12\,\text{m/s}.
$$

### Step 4: Write the final motion functions

Velocity:

$$
v(t) = v_0 + at = 12 - 6t.
$$

Position:

$$
x(t) = v_0 t + \frac{1}{2}a t^2 = 12t - 3t^2.
$$

### Step 5: Interpret the result

- The negative acceleration means acceleration points in the negative axis direction.
- The particle reaches a turning time at $$t=2$$ because:

$$
v(2)=12-12=0.
$$

- The position at that time is:

$$
x(2)=12(2)-3(2)^2=24-12=12\,\text{m},
$$

as required.

### A quick inverse-kinematics “consistency check” variant

With the same assumptions $$x(0)=0$$, constant acceleration, and $$v(2)=0$$, the model forces:

$$
x(4)=0
$$

(you can verify by substituting $$x(t)=12t-3t^2$$). If someone additionally claims “$$x(4)=8\,\text{m}$$,” then the constraints are incompatible: at least one assumption or measurement must be wrong.

This kind of check is a feature of inverse kinematics: you learn not only parameters, but also whether a set of statements can be true at the same time.

## Mini recap

- Inverse kinematics means inferring a motion law from constraints on $$x(t), v(t), a(t)$$.
- Workflow: choose a model family → translate constraints into equations → solve parameters → check consistency.
- Count unknown parameters vs independent constraints; if constraints conflict, the model assumptions (or the data) must be revised.
- A contradiction is not “failure”; it is diagnostic information about the assumptions.

<!-- SOURCE: lecture/kinematics/14_graphical_interpretation_x_v_a.md -->

# Graphical interpretation of $$x(t)$$, $$v(t)$$, and $$a(t)$$

## Learning goals

- Use **slope** to connect $$x(t) \rightarrow v(t)$$ and $$v(t) \rightarrow a(t)$$.
- Use **area** to connect $$a(t) \rightarrow v(t)$$ and $$v(t) \rightarrow x(t)$$ (as changes).
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

So on an $$x$$–$$t$$ graph, the slope of the tangent at time $$t$$ equals $$v(t)$$.

$$
a(t) = \frac{dv}{dt}
$$

So on a $$v$$–$$t$$ graph, the slope of the tangent at time $$t$$ equals $$a(t)$$.

### Area (integrals)

Change in velocity from $$t_1$$ to $$t_2$$:

$$
v(t_2)-v(t_1) = \int_{t_1}^{t_2} a(t)\,dt.
$$

Change in position from $$t_1$$ to $$t_2$$ (displacement):

$$
x(t_2)-x(t_1) = \int_{t_1}^{t_2} v(t)\,dt.
$$

Graphically, these are **signed areas**:

- area above the time axis contributes positively,
- area below contributes negatively.

## Interpretation

### Direction of motion (1D)

- If $$v(t) > 0$$, the particle moves in the positive direction.
- If $$v(t) < 0$$, it moves in the negative direction.

On the $$x(t)$$ graph, this corresponds to:

- increasing $$x(t)$$ → positive slope → $$v>0$$,
- decreasing $$x(t)$$ → negative slope → $$v<0$$.

### Turning points

A turning time occurs when the particle changes direction. In 1D this requires:

$$
v(t^*)=0
$$

and a sign change of $$v$$ across $$t^*$$.

On $$x(t)$$, turning points appear as local maxima/minima (slope zero and slope sign change).

### Speeding up vs slowing down (1D)

Speed increases when velocity and acceleration have the same sign.  
Speed decreases when they have opposite signs.

Graphically, on a $$v(t)$$ plot:

- if $$v$$ is positive and the graph slopes upward (positive acceleration), speed increases,
- if $$v$$ is positive and the graph slopes downward (negative acceleration), speed decreases,
- similarly for negative $$v$$ with sign logic reversed.

## Typical examples

1) **Constant velocity:** $$x(t)$$ is a straight line; $$v(t)$$ is a horizontal line; $$a(t)=0$$.

2) **Constant acceleration:** $$v(t)$$ is a straight line; $$a(t)$$ is a horizontal line; $$x(t)$$ is a parabola.

3) **Back-and-forth motion:** $$v(t)$$ crosses zero; $$x(t)$$ has peaks/valleys.

## Common mistakes

- Reading the *height* of the $$x(t)$$ graph as velocity. Velocity is the **slope**, not the height.
- Reading the *height* of the $$v(t)$$ graph as acceleration. Acceleration is the **slope** of $$v(t)$$.
- Confusing “area under $$v(t)$$” with “distance traveled.” It gives **displacement**; distance requires $$\int |v(t)|dt$$.
- Forgetting that areas are signed (negative velocity gives negative displacement).
- Drawing inferred graphs without matching continuity: if $$x(t)$$ is smooth, then $$v(t)$$ should be continuous; abrupt jumps in $$v$$ correspond to non-smooth $$x(t)$$.

## Worked example

You are given the following velocity–time graph description for motion in 1D:

- From $$t=0$$ to $$t=2\,\text{s}$$, velocity increases linearly from 0 to $$4\,\text{m/s}$$.
- From $$t=2$$ to $$t=5\,\text{s}$$, velocity is constant at $$4\,\text{m/s}$$.
- From $$t=5$$ to $$t=7\,\text{s}$$, velocity decreases linearly from $$4\,\text{m/s}$$ to $$-2\,\text{m/s}$$.

Assume $$x(0)=0$$. Find:

1) The acceleration on each interval.  
2) The displacement on each interval and the final position $$x(7)$$.  
3) Whether there is a turning point (direction change).

### Step 1: Acceleration from slopes of $$v(t)$$

Interval 0–2 s:

$$
a = \frac{4-0}{2-0} = 2\,\text{m/s}^2.
$$

Interval 2–5 s:

$$
a = 0.
$$

Interval 5–7 s:

$$
a = \frac{-2-4}{7-5} = \frac{-6}{2} = -3\,\text{m/s}^2.
$$

### Step 2: Displacement from areas under $$v(t)$$

Displacement is the signed area under the $$v(t)$$ curve.

Interval 0–2 s: triangle with base 2 and height 4:

$$
\Delta x_{0\to 2} = \frac{1}{2}(2)(4) = 4\,\text{m}.
$$

Interval 2–5 s: rectangle with width 3 and height 4:

$$
\Delta x_{2\to 5} = (3)(4) = 12\,\text{m}.
$$

Interval 5–7 s: trapezoid (average of endpoints times width):

$$
\Delta x_{5\to 7} = \frac{(4)+(-2)}{2}\cdot (2) = (1)(2) = 2\,\text{m}.
$$

Total displacement:

$$
\Delta x_{0\to 7} = 4 + 12 + 2 = 18\,\text{m}.
$$

Since $$x(0)=0$$:

$$
x(7)=18\,\text{m}.
$$

### Step 3: Turning point?

A turning time requires $$v=0$$ with sign change. On the last interval, velocity goes from +4 to −2, so it crosses zero once.

Find the crossing time. On 5–7 s the slope is −3 m/s², so:

$$
v(t) = 4 - 3(t-5).
$$

Set $$v=0$$:

$$
0 = 4 - 3(t-5) \;\Rightarrow\; 3(t-5)=4 \;\Rightarrow\; t=5 + \frac{4}{3} \approx 6.33\,\text{s}.
$$

So the particle changes direction at about 6.33 s.

## Mini recap

- Slope links:

$$
v(t)=\frac{dx}{dt}, \qquad a(t)=\frac{dv}{dt}.
$$

- Area links:

$$
v(t_2)-v(t_1)=\int_{t_1}^{t_2}a(t)dt, \qquad x(t_2)-x(t_1)=\int_{t_1}^{t_2}v(t)dt.
$$

- Turning points in 1D occur where $$v=0$$ with a sign change.
- Always ask: “Is this a slope question or an area question?”

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
