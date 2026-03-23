# Problem Set 2

Mechanics I: Kinematics.

---

## Problem 1 – Uniform and uniformly accelerated motion

The equation of motion is given:

$$
x(t) = x_0 + v_0 t + \frac{1}{2} a t^2
$$

1. Determine the velocity $v(t)$ and acceleration $a(t)$.
2. For the given parameters $x_0=0$, $v_0=5\ \text{m/s}$, $a=-2\ \text{m/s}^2$:

    * calculate the stopping time,
    * the maximum velocity depending on the time and the sign of the acceleration,
    * calculate the maximum displacement.

3. Visualize $x(t)$, $v(t)$, $a(t)$.

---

## Problem 2 – Projectile motion

A body moves in the Earth's gravitational field without air resistance. Consider projectile motion with an initial velocity $v_0$ and an angle $\alpha$ relative to the horizontal. 
* Derive the equations of motion in the horizontal and vertical directions.
* Determine the time of flight.
* Determine the maximum height.
* Determine the range.
* For what angle is the range maximum?
* Prepare an animation of the trajectory for different $\alpha$.

---

## Problem 3 – Elimination of time and interpretation of acceleration

The path equation is given in parametric form:

$$
x(t)=2t^2, \qquad y(t)=3t^3
$$

* Eliminate the parameter $t$.
* Draw the trajectory.
* Calculate $\vec v(t)$, $|\vec v(t)|$, $\vec a(t)$ and $|\vec a(t)|$.
* Is the acceleration constant?

---

## Problem 4 – Circular motion

A body moves in a circle of radius $R$ with angular velocity $\omega$: 
* Determine $\vec r(t)$, $\vec v(t)$, $\vec a(t)$.
* Determine $|\vec r(t)|$, $|\vec v(t)|$, $|\vec a(t)|$.
* Show that the acceleration is centripetal.
* Visualize the vectors $\vec r$, $\vec v$, $\vec a$.

---

## Problem 5 – Elliptical motion (purely kinematic)

The path equation is given in parametric form:

$$
x(t)=a\cos(\omega t), \qquad y(t)=b\sin(\omega t)
$$

* Calculate the velocity and acceleration.
* Is the magnitude of the velocity constant?
* Where is the velocity maximum?
* Draw the trajectory and the graphs of $|\vec v(t)|$ and $|\vec a(t)|$.

---

## Problem 6 – Cycloid: trajectory of a point on a rolling circle

A circle of radius $R$ rolls without slipping along the $x$-axis. A point on the rim of the circle traces a cycloid: 
$$
x(t)=R(\omega t-\sin(\omega t)),\qquad
y(t)=R(1-\cos(\omega t))
$$

1. Determine the velocity vector $\vec v(t)$ and the acceleration $\vec a(t)$.
2. Calculate $|\vec v(t)|$ and indicate the moments when the point temporarily "stops" relative to the ground.
3. Determine the maximum values of $|\vec v|$ and $|\vec a|$.
4. Create an HTML animation:
   - the circle rolling on the axis,
   - the point on the rim,
   - the cycloid trace,
   - optionally, the vectors $\vec v$ and $\vec a$ at a chosen moment.
5. Compare the cycloid with circular motion in a reference frame attached to the circle.

---

## Problem 7 – 2D motion with a given acceleration

Given is the acceleration $\vec a = (2, -3)$ and the initial conditions: $\vec v(0)=(1,0)$, $\vec r(0)=(0,0)$

* Determine $\vec v(t)$.
* Determine $\vec r(t)$.
* Draw the trajectory, velocity vector, and acceleration vector at a few selected moments in time, or create an HTML animation.

---

## Problem 8 – Relative motion

Body A moves with velocity $\vec v_A=(3,1)$, body B with velocity $\vec v_B=(1,-2)$.

1. Determine the relative velocity $\vec v_{A/B}$.
2. Determine the direction of the relative motion.
3. Visualize the motion of both bodies in:
    - the reference frame attached to the origin of the coordinate system,
    - the reference frame attached to body A,
    - the reference frame attached to body B.

It is best to do this in the form of an HTML animation, but static graphs of trajectories and velocity vectors can also be drawn.

---

## Problem 9 – Change of reference frame (Copernican model → geocentric description)

Earth and Mars move in circles around the Sun in the same direction.

Assume the model (heliocentric system): 
$$
\vec r_Z(t) = R_Z\,\bigl(\cos(\omega_Z t),\sin(\omega_Z t)\bigr)
$$

$$
\vec r_M(t) = R_M\,\bigl(\cos(\omega_M t),\sin(\omega_M t)\bigr)
$$

1. Draw both motions in the heliocentric system (Sun in the center).
2. Determine the position of Mars relative to Earth (geocentric system):

      $$
      \vec r_{M/Z}(t)=\vec r_M(t)-\vec r_Z(t)
      $$

    * Explicitly write down the components $x_{M/Z}(t)$, $y_{M/Z}(t)$.

3. (HTML) Create an animation with two panels:
    * panel A: heliocentric motion (Earth and Mars on circles),
    * panel B: trajectory of Mars as seen from Earth (trace of $\vec r_{M/Z}(t)$).

---

## Problem 10 – Analysis of motion from numerical data

For the measurement data $x(t)=t+\frac{1}{20}t^2$ on the interval $t\in[0,10]$ with a time step of $\Delta t=0.1$:

1. Approximate the velocity using the finite difference method.
2. Approximate the acceleration using the finite difference method.
3. Compare with the analytical solution (if known).
4. Investigate the effect of the time step on accuracy.