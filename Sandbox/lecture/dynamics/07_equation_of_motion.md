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

$$
F_{\text{net}} = F(x, v, t).
$$

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

$$
x(0)=0,\qquad v(0)=0.
$$

1) Write the equation of motion.  
2) Solve for v(t) and x(t).  
3) Interpret the result and connect it back to constant-acceleration kinematics.

### Step 1: Force model

Frictionless surface means no friction force. Horizontally, the only force is the applied force:

$$
F_{\text{net}} = F.
$$

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
