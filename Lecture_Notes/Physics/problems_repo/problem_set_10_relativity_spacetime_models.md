# Problem Set 10

Relativistic physics.

---

## Problem 1 – Time dilation

A spacecraft is moving with a velocity:

$$
v = 0.8c
$$

1. Calculate the Lorentz factor:

   $$
   \gamma = \frac{1}{\sqrt{1-\frac{v^2}{c^2}}}
   $$

2. How much time will pass on Earth if 5 years pass on the ship?
3. What is the percentage effect of the dilation?
4. What happens in the limit $v \to c$?
5. Interpret the result physically.

---

## Problem 2 – Length contraction

A rocket with a proper length:

$$
L_0 = 120\,\mathrm{m}
$$

moves with a velocity of $0.6c$. 
1. Calculate the length observed by a stationary observer:

   $$
   L = \frac{L_0}{\gamma}
   $$

2. What is the percentage of contraction?
3. Does the observer in the rocket see the contraction?
4. What is an invariant quantity?
5. Interpret the "rocket in a tunnel" paradox.

---

## Problem 3 – Lorentz transformation

Given events in frame $S$:

$$
x_1 = 0, \quad t_1 = 0
$$

$$
x_2 = 900\,\mathrm{m}, \quad t_2 = 4\,\mu\mathrm{s}
$$

Frame $S'$ moves with a velocity $v=0.6c$.

1. Apply the transformation:

   $$
   x' = \gamma (x - vt)
   $$

   $$
   t' = \gamma \left(t - \frac{vx}{c^2}\right)
   $$

2. Calculate the coordinates of the second event in $S'$.
3. Can the order of events change?
4. Calculate the spacetime interval:

   $$
   s^2 = c^2 t^2 - x^2
   $$

5. Verify its invariance.

---

## Problem 4 – Twin paradox

Twin A stays on Earth.
Twin B travels at a velocity of $0.9c$ for 10 years (Earth time) and returns. 
1. Calculate the proper time of twin B.
2. How many years younger is he when he returns?
3. Is the symmetry of the reference frames complete?
4. Indicate the moment the symmetry is broken.
5. Interpret this in the language of Minkowski spacetime.

---

## Problem 5 – Muons in the atmosphere

Muons are created at an altitude of 10 km.

Proper lifetime:

$$
\tau_0 = 2.2\,\mu\mathrm{s}
$$

Velocity:

$$
v = 0.995c
$$

1. Calculate the Lorentz factor.
2. Calculate the mean lifetime in the Earth's frame:

   $$
   \tau = \gamma \tau_0
   $$

3. What average distance does a muon travel?
4. Without relativity, would it reach the surface?

---

## Problem 6 – Minkowski diagram (HTML mandatory)

1. Implement the Lorentz transformation as a matrix.
2. Draw the $ct$ and $x$ axes.
3. Draw the $ct'$ and $x'$ axes.
4. Mark the light cone.
5. Allow velocity change with a slider.
6. Geometrically interpret time dilation and length contraction.

---

## Problem 7 – Relativistic energy and momentum

$$
E = \gamma mc^2
$$

$$
p = \gamma mv
$$

1. Calculate the total energy of an electron for $v=0.95c$.
2. Calculate the kinetic energy:

   $$
   E_k = (\gamma-1)mc^2
   $$

3. Compare with the classical result $\frac{1}{2} mv^2$.
4. Investigate the limit $v \ll c$.
5. Interpret the relation:

   $$
   E^2 = p^2 c^2 + m^2 c^4
   $$

---

## Problem 8 – Gravitational redshift

Approximation (weak field):

$$
\frac{\Delta f}{f} \approx \frac{\Delta \Phi}{c^2}
$$

1. Derive the shift for the Earth's surface.
2. Calculate the relative change in frequency.
3. Interpret it as gravitational time dilation.
4. Estimate the effect for a neutron star.
5. Compare the order of magnitude with laboratory experiments.

---

## Problem 9 – Schwarzschild radius


$$
r_s = \frac{2GM}{c^2}
$$

1. Calculate $r_s$ for the mass of the Sun.
2. Calculate $r_s$ for the Earth.
3. Calculate the redshift at $r=1.5r_s$.
4. What happens as $r \to r_s$?
5. Interpret the event horizon.

---

## Problem 10 – Numerical simulation of relativistic motion

Relativistic equation of motion:

$$
\frac{d}{dt}(\gamma m v) = F
$$

1. Implement the RK4 method.
2. Compare the motion under a constant force in the classical and relativistic models.
3. Investigate the asymptotic approach to $c$.
4. Create a graph of $v(t)$ and $x(t)$ for both models.
5. Evaluate the energy differences between the models.