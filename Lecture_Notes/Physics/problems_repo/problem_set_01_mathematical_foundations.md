# Problem Set 1 – Mathematical Foundations

---

## Problem 1 – Vectors and linear transformations

Please write down all calculation steps, not just the final results.

**Given two vectors in three-dimensional space:**

$$
\vec a = (2,-1,3), \qquad
\vec b = (1,4,-2)
$$

* Calculate the lengths of the vectors $|\vec a|$, $|\vec b|$.
* Determine the normalized vector $\hat a = \frac{\vec a}{|\vec a|}$.
* Calculate the dot product $\vec a \cdot \vec b$ and the angle between the vectors.
* Calculate the cross product $\vec a \times \vec b$ and the area of the parallelogram spanned by these vectors.

**For the matrix:**

$$
A =
\begin{pmatrix}
2 & 1 & 0 \\
0 & 1 & -1 \\
1 & 0 & 1
\end{pmatrix}
$$

* Calculate $A\vec a$.
* Calculate $\det A$.
* Check if the transformation preserves the orientation of the space.

---

## Problem 2 – Parametric trajectory, velocity, and acceleration

Please write down all calculation steps, not just the final results. Please draw a graph of the trajectory and the velocity and acceleration vectors at selected points.

The parametric equation of the trajectory is given by:

$$
\vec r(t) = \bigl(t^2,\sin t, 5\bigr)
$$

* Determine the velocity

  $$
  \vec v(t) = \frac{d\vec r}{dt}
  $$

* Determine the acceleration

  $$
  \vec a(t) = \frac{d^2 \vec r}{dt^2}
  $$

* Calculate $|\vec v(1)|$.
* Calculate $\vec v \cdot \vec a$.
* Calculate $\vec v \times \vec a$.

---

## Problem 3 – Integration of motion

### A) For a given velocity:

$$
\vec v(t) = \bigl(2t,3,-e^{-t}\bigr), \qquad
\vec r(0) = (0,1,2)
$$

1. Determine

   $$
   \vec r(t) = \vec r(0) + \int_0^t \vec v(\tau)\, d\tau
   $$

2. Determine the acceleration $\vec a(t)$.

### B) For a given acceleration:

$$
\vec a(t) = \bigl(4,-\sin t,0\bigr),
\qquad
\vec v(0) = (1,0,2),
\qquad
\vec r(0) = (0,0,0)
$$

1. Determine

   $$
   \vec v(t) = \vec v(0) + \int_0^t \vec a(\tau)\, d\tau
   $$

2. Determine

   $$
   \vec r(t) = \int_0^t \vec v(\tau)\, d\tau+ \vec r(0)
   $$

---

## Problem 4 – Geometry of parametric curves

Investigate the following curves:

A) $\ x(t) = R\cos t,\quad  y(t) = R\sin t$

B) $\ x(t) = a\cos t, \quad y(t) = b\sin t$

C) $\ x(t) = t, \quad   y(t) = t^2$

D) $\ x(t) = \cosh t, \quad y(t) = \sinh t$

For each curve:

1. Eliminate the parameter (if possible).
2. Determine the type of curve.
3. Determine the velocity $\vec v(t)$ and acceleration $\vec a(t)$.
4. Check if the velocity/acceleration has a constant magnitude ($|\vec v| = const$ or $|\vec a| = const$).

---

## Problem 5 – Trajectory curvature and normal acceleration

For an ellipse:

$$
x = a\cos t, \qquad y = b\sin t
$$

1. Determine the velocity vector $\vec v(t)$ and the acceleration vector $\vec a(t)$.
2. Determine the unit tangent vector to the trajectory

   $$
   \hat T(t)=\frac{\vec v(t)}{|\vec v(t)|}.
   $$

3. Decompose the acceleration into tangential and normal components:

   $$
   \vec a(t)=\vec a_t(t)+\vec a_n(t),
   $$

   and determine the magnitude of the normal acceleration $a_n(t)=|\vec a_n(t)|$.

4. Using the relation

   $$
   a_n=\frac{v^2}{R},
   $$

   determine the radius of curvature of the trajectory at point $t=0$.

5. Compare the result with the case of a circle $a=b$.
6. **Physical interpretation.**
   Answer the following questions:

   * Does a greater trajectory curvature imply a greater normal acceleration?
   * Where on the ellipse is the trajectory more "curved": at the end of the major or minor semi-axis?
   * Explain why normal acceleration can be interpreted as the cause of the change in the direction of motion.

---

## Problem 6 – Curve length and numerical integration

A parametric trajectory in 2D is given:

$$
x(t) = t,\qquad y(t)=t^2,\qquad t\in[0,1]
$$

1. Determine the velocity vector:

   $$
   \vec v(t)=\frac{d\vec r}{dt}
   $$

2. Determine the magnitude of the velocity $|\vec v(t)|$.
3. Write the arc length of the trajectory as an integral:

   $$
   s = \int_0^1 |\vec v(t)|\,dt
   $$

4. Calculate this integral analytically (if possible) or reduce it to a form that requires a numerical method.
5. Implement the trapezoidal rule in HTML/JS to calculate $s$:
   - check the convergence of the result with an increasing number of divisions $N$,
   - plot the error as a function of $N$.

Requirement: visualization of the trajectory and the ability to change $N$ in the application.

---

## Problem 7 – Work of a force along a trajectory

Given force: 

$$
\vec F(x,y) = (y, 2x)
$$

Trajectory:

$$
x = t, \qquad y = t^2, \qquad t \in [0,1]
$$

1. Determine the velocity vector $\vec v(t)$.
2. Calculate the work done by the force $\vec F$ along the trajectory, i.e., the line integral:

   $$
   W = \int_C \vec F \cdot d\vec r
   $$

3. Write the integral as the limit of a Riemann sum and calculate its value numerically in HTML/JS, comparing it with the analytical result (if possible).

---

## Problem 8 – First-order differential equation

$$
\frac{dy}{dt} = -k y
$$

1. Solve the equation.
2. Visualize the solution in an HTML/JS application for different values of parameter $k$ and different initial conditions $y(0)$.

---

## Problem 9 – Harmonic oscillator

$$
\frac{d^2 x}{dt^2} + \omega^2 x = 0
$$

1. Find the general solution.
2. Solve for the given initial conditions.
3. Visualize (HTML application): $x(t)$, $x'(t)$, $x''(t)$ for selected parameters and initial conditions.

---

## Problem 10 – Angular momentum in circular motion

Consider circular motion in the $xy$ plane:

$$
\vec r(t)=\bigl(R\cos(\omega t),\,R\sin(\omega t),\,0\bigr)
$$

1. Determine the velocity:

   $$
   \vec v(t)=\dot{\vec r}(t)
   $$

2. Calculate the angular momentum with respect to the origin:

   $$
   \vec L(t)=m\,\vec r(t)\times \vec v(t)
   $$

3. Show that $|\vec L|=mR^2\omega$ is constant, and the vector $\vec L$ is perpendicular to the plane of motion.
4. Interpret the direction of $\vec L$ (right-hand rule).
5. (Optional) Add a constant centripetal force and calculate the torque:

   $$
   \vec \tau = \vec r \times \vec F
   $$

   Verify the relationship $\vec \tau = \frac{d\vec L}{dt}$ for uniform circular motion.