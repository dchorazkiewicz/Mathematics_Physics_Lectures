# Problem Set 9 – Model Cosmology: from epicycles to gravity

---

## Problem 1 – Ptolemy's Model

1. Write the motion of a planet as a sum:
   - motion along the deferent (main circle),
   - motion along the epicycle.

   Example parametric representation:

   $$
   x(t) = R \cos(\omega t) + r \cos(\Omega t)
   $$
   $$
   y(t) = R \sin(\omega t) + r \sin(\Omega t)
   $$

2. Derive the parametric equations of the trajectory.
3. Investigate the condition for retrograde motion to occur.
4. Determine the moments of change in the direction of motion in angular projection.

**HTML (mandatory):**

- sliders: $R$, $r$, $\omega$, $\Omega$,
- trajectory trace,
- graph of ecliptic longitude $\varphi(t)$.

---

## Problem 2 – Copernicus's Model

1. Implement the motion of two planets in circles around the Sun:

   $$
   \vec r_Z(t) = R_Z (\cos \omega_Z t, \sin \omega_Z t)
   $$
   $$
   \vec r_M(t) = R_M (\cos \omega_M t, \sin \omega_M t)
   $$

2. Determine the position of Mars relative to Earth:

   $$
   \vec r_{M/Z}(t) = \vec r_M(t) - \vec r_Z(t)
   $$

3. Identify the moments of retrogradation.
4. Compare the relative trajectory with the epicyclic model.

**HTML:**

- heliocentric view,
- geocentric view,
- reference frame switch.

---

## Problem 3 – Comparison of models: number of parameters and quality of description

1. Fit the epicycle parameters to the trajectory generated in the heliocentric model.
2. Compare the number of parameters in both models.
3. Evaluate which model is more economical.
4. Interpret the result in the context of simplifying the description of phenomena.

---

## Problem 4 – Kepler's First and Second Laws

1. Implement an elliptical orbit:

   $$
   r(\theta) = \frac{a(1-e^2)}{1 + e \cos \theta}
   $$

2. Vary the eccentricity $e$ and observe the shape of the trajectory.
3. Numerically calculate the area swept out in equal time intervals:

   $$
   A = \frac{1}{2} \int r^2 \, d\theta
   $$

4. Verify the law of equal areas.

**HTML:**

- visualization of the focus,
- drawing area sectors,
- dynamic area comparison.

---

## Problem 5 – Kepler's Third Law (data analysis)

1. Load data for several planets $(a, T)$.
2. Plot the relationship:

   $$
   T^2 \text{ as a function of } a^3
   $$

3. Perform linear regression.
4. Estimate the proportionality constant from the relation:

   $$
   T^2 = C a^3
   $$

5. Evaluate the goodness of fit ($R^2$).

---

## Problem 6 – Two-body motion and the barycenter

1. Define the center of mass:

   $$
   \vec R = \frac{m_1 \vec r_1 + m_2 \vec r_2}{m_1 + m_2}
   $$

2. Show that for an isolated system:

   $$
   m_1 \vec r_1 + m_2 \vec r_2 = \text{const}
   $$

3. Write the equations of motion:

   $$
   m_1 \ddot{\vec r}_1 = - G \frac{m_1 m_2}{|\vec r_1 - \vec r_2|^3} (\vec r_1 - \vec r_2)
   $$
   $$
   m_2 \ddot{\vec r}_2 = - G \frac{m_1 m_2}{|\vec r_2 - \vec r_1|^3} (\vec r_2 - \vec r_1)
   $$

4. Investigate the dependence of the trajectory on the mass ratio $m_1/m_2$.

**HTML:**

- trajectories of both bodies,
- marked barycenter,
- mass ratio slider.

---

## Problem 7 – Newton's Gravity and orbit classification

Motion in a central field:

$$
\vec F = -\frac{GMm}{r^2} \hat r
$$

Total energy:

$$
E = \frac{1}{2} m v^2 - \frac{GMm}{r}
$$

1. Numerically investigate the cases:
   - $E < 0$ (bound orbit),
   - $E = 0$ (parabola),
   - $E > 0$ (hyperbola).
2. Determine the initial conditions leading to different types of orbits.

**HTML:**

- change of initial velocity,
- graph of energy over time,
- trajectory classification.

---

## Problem 8 – Orbit perturbation and precession (Newtonian extension)

Modified potential:

$$
U(r) = -\frac{GMm}{r} + \frac{\alpha}{r^2}
$$

1. Implement the equations of motion.
2. Observe the precession of the perihelion.
3. Investigate the effect of parameter $\alpha$.

**HTML:**

- animation of the ellipse axis drift,
- measurement of the precession angle.

---

## Problem 9 – Three-body system (classical problem)

1. Write the equations of motion for three masses:

$$
m_i \ddot{\vec r}_i = \sum_{j \ne i} -G \frac{m_i m_j}{|\vec r_i - \vec r_j|^3} (\vec r_i - \vec r_j)
$$

2. Implement a numerical method (e.g., RK4).
3. Investigate the stability of the configuration.

**HTML:**

- animation of three-body motion,
- ability to change masses and initial conditions.

---

## Problem 10 – Stability analysis and conserved quantities

1. Monitor for the three-body system:
   - total energy $E(t)$,
   - angular momentum $\vec L = \vec r \times m \vec v$,
   - position of the center of mass.
2. Evaluate the stability of the numerical method.
3. Compare different time steps $\Delta t$.
4. Investigate the effect of the integration scheme on orbit behavior.