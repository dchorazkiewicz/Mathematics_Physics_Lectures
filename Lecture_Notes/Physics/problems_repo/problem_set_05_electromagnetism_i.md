# Problem Set 5

Electromagnetism I: Field and forces.

---

## Problem 1 – Potential and energy

For a point charge $q = 4\ \mu\mathrm{C}$:

1. Calculate the potential at $r = 0.3\,\mathrm{m}$.
2. Calculate the potential difference between $0.3\,\mathrm{m}$ and $0.6\,\mathrm{m}$.
3. Calculate the work done to move a test charge $q_0 = 2\,\mu\mathrm{C}$.
4. Calculate the electric field intensity from the derivative of the potential.
5. Compare with Coulomb's law.

---

## Problem 2 – Coulomb's force

Two point charges are given:

$$
q_1 = 3\ \mu\mathrm{C}, \quad q_2 = -5\ \mu\mathrm{C}
$$

located at points:

$$
r_1 = (0,0), \quad r_2 = (0.4, 0.3)\,\mathrm{m}
$$

1. Determine the force vector acting on $q_2$.
2. Calculate its magnitude.
3. Determine the potential energy of the system.
4. Calculate the work required to separate the charges to a distance of $2\,\mathrm{m}$.

---

## Problem 3 – Field at a point from a system of charges

Two point charges are given:

* $+q\  \text{at point}\  (-a, 0)$
* $+2q\  \text{at point}\  (a, 0)$

1. Determine the field vector $\vec E(0, y)$, $\vec E(x, 0)$ and generally $\vec E(x, y)$.
2. Determine the condition for which the components $E_x = 0$, $E_y = 0$ and the zero field $\vec E = 0$.
3. Calculate the field for: $a = 0.2\,\mathrm{m}$, $y = 0.3\,\mathrm{m}$, $q = 2\,\mu\mathrm{C}$.
4. Investigate the limit $y \gg a$.
5. Does a point of zero field exist on the $y$-axis?

---

## Problem 4 – Motion of a particle in a uniform field

The following initial conditions are given:

* $m = 0.02\ \mathrm{kg}$
* $q = 1\ \mathrm{mC}$
* $\vec E = (30, 100)\,\mathrm{N/C}$
* $\vec v(0) = (20, 0)\,\mathrm{m/s}$
* $\vec r(0) = (0, 0)$

For them:

1. Write the equations of motion and solve them analytically.
2. Draw the motion trajectory.
3. Calculate the time to reach a vertical velocity of $50\,\mathrm{m/s}$.
4. Calculate the kinetic energy after $t = 0.05\,\mathrm{s}$.
5. Check the consistency with the energy balance.

---

## Problem 5 – Capacitor: energy and force

Parallel-plate capacitor:

* $S = 0.02\,\mathrm{m^2}$
* $d = 5\,\mathrm{mm}$
* $U = 500\,\mathrm{V}$

1. Calculate the capacitance.
2. Calculate the energy stored in the capacitor.
3. Calculate the electric field intensity between the plates.
4. Calculate the field energy density.
5. Calculate the force of attraction between the plates.

---

## Problem 6 – 2D field map

System: any three charges in a plane.

1. Implement a function calculating the field vector $\vec E(x, y)$.
2. Generate a vector field map.
3. Find the equilibrium point numerically.
4. Investigate the stability of the equilibrium point (small displacement).
5. Compare with the case of two charges.

Requirement: HTML visualization with the ability to change the positions of the charges.

---

## Problem 7 – Motion in a central field

Field:

$$
E(r) = k \frac{Q}{r^2} \hat r
$$

1. Write the equation of motion of the particle.
2. Consider the case of radial motion.
3. Implement the RK4 method.
4. Investigate the case of positive and negative energy.
5. Compare with the gravitational analogy.

Requirement: animation of the motion trajectory.

---

## Problem 8 – Energy of a three-charge system


1. Write the total energy of the system.
2. Calculate the energy for an equilateral triangle configuration.
3. Investigate the change in energy when changing the sign of one charge.
4. Find the minimum energy configuration (numerically).
5. Interpret the stability of the system.

---

## Problem 9 – Dipole in an external field

A dipole in a uniform field $E_0$.

1. Derive the formula for the torque acting on the dipole.
2. Calculate the potential energy of the dipole.
3. Determine the equation of angular motion.
4. Linearize the equation for small displacements.
5. Interpret the system as a harmonic oscillator.

---

## Problem 10 – Field flux (verification of Gauss's law)


1. Define the electric field flux.
2. Consider a sphere around a point charge.
3. Implement a discrete approximation of the flux.
4. Investigate the dependence on the number of grid points.
5. Compare with the analytical result.