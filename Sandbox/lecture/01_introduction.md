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
