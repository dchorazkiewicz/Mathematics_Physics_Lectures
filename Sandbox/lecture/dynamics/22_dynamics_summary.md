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

$$
\vec{F}_{A\to B} = -\vec{F}_{B\to A}.
$$

### Standard force models (near Earth, intro level)

Weight:

$$
\vec{W} = m\vec{g}.
$$

Normal force N: constraint response perpendicular to a surface; determine from the perpendicular equation of motion plus constraints.

Kinetic friction:

$$
f_k = \mu_k N
$$

Static friction:

$$
0 \le f_s \le \mu_s N.
$$

Spring force (1D about equilibrium):

$$
F_{\text{spring}} = -kx.
$$

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

$$
T - f_k = m_1 a,
$$

$$
f_k = \mu_k N = \mu_k m_1 g.
$$

For m_2 (hanging, choose downward positive):

- m_2 g downward,
- T upward.

So:

$$
m_2 g - T = m_2 a.
$$

### Step 2: Compute friction

$$
f_k = (0.25)(4.0)(9.8) = 9.8\,\text{N}.
$$

### Step 3: Solve for acceleration

From the m_1 equation:

$$
T = m_1 a + f_k.
$$

Substitute into the m_2 equation:

$$
m_2 g - (m_1 a + f_k) = m_2 a.
$$

So:

$$
m_2 g - f_k = (m_1 + m_2)a.
$$

Compute m_2 g:

$$
m_2 g = (1.5)(9.8) = 14.7\,\text{N}.
$$

Thus:

$$
a = \frac{14.7 - 9.8}{4.0 + 1.5} = \frac{4.9}{5.5} = 0.891\,\text{m/s}^2.
$$

### Step 4: Solve for tension

$$
T = m_1 a + f_k = (4.0)(0.891) + 9.8 = 3.56 + 9.8 = 13.36\,\text{N}.
$$

### Step 5: Interpret and check

- Acceleration is much smaller than g, reasonable because friction is significant and the hanging mass is small.
- T is between f_k (about 10 N) and m_2 g (14.7 N), consistent with both equations.

## Mini recap

- Dynamics workflow: system + assumptions → FBD → components → \sum F = ma → solve → interpret.
- Know what each standard force model means and when it applies.
- Always check signs, limiting cases, and whether your assumptions (contact, slipping, constant net force) remain consistent.
