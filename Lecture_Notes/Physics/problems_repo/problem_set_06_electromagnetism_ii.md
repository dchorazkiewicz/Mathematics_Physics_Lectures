# Problem Set 6

Electromagnetism II: Magnetism, induction, and electrodynamics.

---

## Problem 1 – Lorentz force

For the following data:

* $\vec B = (0,0,1)\ \mathrm{T}$
* $\vec v = (2,3,0)\ \mathrm{m/s}$
* $q = 1\ \mathrm{mC}$

1. Determine the Lorentz force $\vec F$ acting on the charge.
2. Solve the equation of motion for this charge, assuming that at time $t=0$ it is at the point $(0,0,0)$.
3. Calculate the magnitude $|\vec F|$.
4. Does the magnetic force do work?
5. Determine the radius of the trajectory for $m = 0.01\ \mathrm{kg}$.
6. How will $r$ change when the value of $B$ is doubled?

---

## Problem 2 – Velocity selection (crossed fields)

Crossed electric and magnetic fields can be used to select particles with a specific velocity. Assume we have:

$$
\vec E = (0,E,0)
$$

$$
\vec B = (0,0,B)
$$

1. Derive the condition for rectilinear motion.
2. Calculate $v_d$ for $E = 400\ \mathrm{V/m}$, $B = 0.8\  \mathrm{T}$.
3. Does the kinetic energy change in steady motion?
4. Interpret the operating principle of the velocity selector.

---

## Problem 3 – Magnetic moment of a loop

We have a conducting loop with $N$ turns, area $S$, through which a current $I$ flows. The loop is located in a uniform magnetic field $\vec B$.

1. Define the magnetic moment $\vec \mu$ of the loop:
2. Determine the torque $\vec M$.
3. For what angle is the torque maximum?
4. Determine the potential energy $U$.
5. Indicate the stable and unstable positions.

---

## Problem 4 – Rotating loop (induction)

A loop with area $S$ and $N$ turns is placed in a uniform magnetic field $\vec B$. The loop rotates with an angular velocity $\omega$ around an axis perpendicular to $\vec B$.

1. Determine $\Phi(t)$.
2. Determine $\mathcal{E}(t)$.
3. Calculate the amplitude $\mathcal{E}_0$.
4. How does the amplitude depend on $\omega$?
5. Interpret the mechanism of EMF generation.

---

## Problem 5 – Induction in a moving rod

We have a rod of length $L=0.25\,\mathrm{m}$, moving with a velocity $v=4\,\mathrm{m/s}$ perpendicular to a uniform magnetic field $\vec B=0.6\,\mathrm{T}$.

1. Determine $\mathcal{E}$.
2. Determine the potential difference between the ends.
3. What will happen if the motion is not perpendicular to $\vec B$?
4. How does $\mathcal{E}$ depend on $L$?
5. Where does the energy of the electric field in the rod come from?

---

## Problem 6 – Rod on metal rails in a $\vec B$ field

We have two conducting, parallel rails separated by $L$, along which a conducting rod slides without friction (it closes the circuit). The entire system has an electrical resistance $R$ (rails + rod + contacts). A uniform magnetic field $\vec B$ is perpendicular to the plane of the rails.

For example data:

* $m=0.20\ \mathrm{kg}$
* $L=0.30\ \mathrm{m}$
* $B=0.80\ \mathrm{T}$
* $R=0.50\ \Omega$
* $\alpha=25^\circ$
* $g=9.81\ \mathrm{m/s^2}$

1. Determine the motional EMF $\mathcal{E}(v)$ and the current $I(v)$.
2. Show that a magnetic braking force acts on the rod along the rails:
3. Write the equation of motion along the incline and reduce it to a form with "damping proportional to $v$".
4. Determine the terminal velocity $v_\infty$ (for an "infinitely long" incline).
5. Perform a power balance and show that in the steady state:

$$
mg\sin\alpha\cdot v = I^2R
$$

(gravitational energy is converted into Joule heat).

---

## Problem 7 – Loop pulled into a $B$ field region

A rectangular conducting loop with resistance $R$ has dimensions $a\times b$. It is pulled with a constant velocity $v$ into a region of uniform magnetic field $B$ perpendicular to the loop (the field exists only in a certain region of space).

For example data:

* $a=0.20\ \mathrm{m}$
* $b=0.10\ \mathrm{m}$
* $B=0.60\ \mathrm{T}$
* $R=0.40\ \Omega$
* $v=1.5\ \mathrm{m/s}$

1. Write down the flux $\Phi(t)$ in the entering phase (when part of the loop is already in the field, but not yet all of it).
2. Determine $\mathcal{E}$ and $I$ in this phase.
3. Determine the braking force $F(v)$.
4. Calculate the mechanical power required to maintain a constant $v$ and show that it is equal to the thermal power $I^2R$.
5. What happens to the current when the loop is entirely in the uniform field?

---

## Problem 8 – Self-induction

RL circuit: a coil with inductance $L$ and resistance $R$ is powered by a DC voltage $U$. After a long time, the circuit is in a steady state, then at time $t=0$ the power supply is disconnected, and the $L$–$R$ circuit remains without a source.

Data:

* $L=0.20\ \mathrm{H}$
* $R=5.0\ \Omega$
* $U=12\ \mathrm{V}$

1. Determine the steady current $I_0$ before disconnecting the power supply.
2. After disconnection: derive $I(t)$, the time constant $\tau$, and the voltage across the coil $U_L(t)$.
3. Calculate the energy stored in the magnetic field of the coil right before disconnection:

$$
W=\frac12 LI_0^2
$$

4. Show that this energy is converted into Joule heat in the resistor (integral of $I^2R$ over time).
5. (Briefly qualitatively) Why does an overvoltage appear when disconnecting the current?

---

## Problem 9 – Ideal vs. real transformer

Explain how a transformer works, what its ideal properties are, and what reality looks like. Where does the secondary voltage come from? What are the losses in a transformer? What are the typical values of the turns ratio and efficiency?

---

## Problem 10 – Eddy currents

Explain where eddy currents can be used to brake motion. What are the advantages and disadvantages of this solution? Which materials are best for generating eddy currents? How can the braking force be increased?