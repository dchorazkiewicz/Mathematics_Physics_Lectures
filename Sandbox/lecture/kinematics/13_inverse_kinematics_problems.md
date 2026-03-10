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
