# Problem Set 3

Mechanics II: Dynamics and energy.

---

## Problem 1 – Newton's second law (constant force)

A constant force acts on a body of mass $m = 2\ \mathrm{kg}$:

$$
\vec F = [6, 2]\ \mathrm{N}
$$

The body starts with an initial velocity $\vec v(0) = (1, -1)\ \mathrm{\frac{m}{s}}$ from the point $\vec r(0)=(0,0)\ \mathrm{m}$. 
* Determine $\vec a(t)$.
* Determine $\vec v(t)$.
* Determine $\vec r(t)$.
* Draw the trajectory of the motion.
* Calculate the work done by the force at time $t=3\ \mathrm{s}$.
* Check the consistency with the work-energy theorem.

---

## Problem 2 – Inclined plane with friction

A body of mass $m$ slides down an inclined plane with an angle $\alpha$. The coefficient of kinetic friction is $\mu$. 
* Determine all forces acting on the body.
* Derive the acceleration $\vec a$.
* Calculate the time of descent from height $h$.
* Determine the final velocity $\vec v$.
* Check if the result is consistent with the energy balance.

---

## Problem 3 – Work of a variable force

Given a one-dimensional force:

$$
F(x)=-kx
$$

* Write down the equation of motion and solve it.
* Calculate the work done during the displacement from $0$ to $x_0$.
* Interpret the result as potential energy.
* Verify the relationship $F = -\frac{dU}{dx}$.
* Draw the graph of $F(x)$ and $U(x)$.

---

## Problem 4 – Conservation of energy

A body falls from a height $h$ without air resistance.

* Write down the total energy $E(h) = T(h) + U(h)$.
* Determine the velocity as a function of height $v(h)$.
* Compare with the solution from Newton's second law.
* At what height does the kinetic energy account for 75% of the total energy?

---

## Problem 5 – Momentum and one-dimensional head-on collision

Two bodies with masses $m_1, m_2$ move along a single straight line. The collision is elastic. 
* Write down the principles of conservation of momentum and energy.
* Determine the velocities after the collision.
* Consider the case $m_1 = m_2$.
* Consider the limit $m_2 \gg m_1$.
* Interpret the results physically.

---

## Problem 6 – Motion with linear drag

The drag force is given by the formula:

$$
F=-kv
$$

Initial conditions: $v(0)=v_0$, $x(0)=0$.

* Write down the equation of motion and solve it.
* Investigate the limit $\lim_{t\to\infty} v(t)$.
* Compare with motion without drag.

---

## Problem 7 – Vertical throw with drag

We have the equation of motion:

$$
m\frac{dv}{dt} = -mg - kv
$$

with initial conditions $v(0)=v_0$, $x(0)=0$.

* Solve the equation.
* Determine the maximum height.
* Compare with the case without drag.
* Perform a numerical simulation.
* Compare the analytical and numerical solutions.

---

## Problem 8 – Harmonic oscillator (formal dynamics)


$$
m\ddot x + kx = 0
$$

* Solve the equation.
* Determine the natural frequency.
* Write down the energy as a function of time.
* Show that energy is conserved.
* Interpret the motion in phase space.

---

## Problem 9 – Potential and conservative field

Given potential energy:

$$
U(x,y)=\frac{k}{2}(x^2+y^2)
$$

* Determine the force as the gradient of the potential.
* Write down the equations of motion.
* Determine the type of motion.
* Determine the total energy.
* Interpret the trajectory geometrically, presenting it in an HTML/JS application.

---

## Problem 10 – Numerical model of a dynamical system

Consider motion in a one-dimensional potential:

$$
U(x)=\frac{k}{2}x^2 + \lambda x^4
$$

* Determine the force.
* Write down the equation of motion.
* Solve numerically for selected parameters.
* Investigate the effect of initial energy on the type of motion.
* Create a visualization of $x(t)$ and the phase portrait.