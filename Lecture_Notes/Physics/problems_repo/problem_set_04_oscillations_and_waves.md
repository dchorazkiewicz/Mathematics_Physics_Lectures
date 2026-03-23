# Problem Set 4

Oscillations and waves: dynamical systems and propagation of disturbances.

## Problem 1 – Harmonic motion: motion parameters

A function describing harmonic motion is given:

$$
x(t) = A \cos(\omega t + \varphi)
$$

1. Determine the period $T$ and the frequency $f$.
2. Determine the maximum velocity and the maximum acceleration.
3. For $A = 0.2$ m, $f = 2$ Hz:

   * calculate $\omega$,
   * calculate $v_{\max}$,
   * calculate $a_{\max}$.

Answers: full derivation + interpretation.

---

## Problem 2 – Energy of a harmonic oscillator

A system with the following initial parameters is given:

* $m = 1\ \mathrm{kg}$
* $k = 100\ \mathrm{N/m}$
* $x(0) = 2\ \mathrm{m}$
* $v(0) = 1\ \mathrm{m/s}$

1. Determine the natural frequency.
2. Calculate the total energy of the system.
3. For what displacement does the kinetic energy account for 50% of the total energy?

Answers: full derivation + interpretation.

---

## Problem 3 – Harmonic wave

The wave equation is given:

$$
y(x,t) = A \sin(kx - \omega t)
$$

1. Determine the wavelength.
2. Determine the phase velocity.
3. Calculate $v$ for $k = 4\pi$, $\omega = 20\pi$.
4. Does the point $x = \lambda$ oscillate in phase with the point $x = 0$?

Answers: full derivation + interpretation.

---

## Problem 4 – Wave equation

The function is given:

$$
y(x,t) = A \cos(kx - \omega t)
$$

1. Verify that it satisfies the wave equation:

$$
\frac{\partial^2 y}{\partial t^2} = v^2 \frac{\partial^2 y}{\partial x^2}
$$

2. Determine the relationship between $v$, $k$, and $\omega$.

Answers: algebraic relation.

---

## Problem 5 – Superposition of waves, beats, and group velocity

Two harmonic waves are given:

$$
y_1(x,t)=A\sin(kx-\omega t)
$$

$$
y_2(x,t)=A\sin(kx-(\omega+\Delta\omega)t)
$$

1. Determine the resultant wave $y=y_1+y_2$ and reduce it to a product form (carrier × envelope).
2. Identify the beat frequency and the beat period at the point $x=0$.
3. Interpret physically: what does the envelope describe, and what does the carrier wave describe?
4. Use Python/HTML/JS to generate the two waves and their superposition, showing the phenomenon of beats and the motion of the envelope.

---

## Problem 6 – Damped oscillator

Equation:

$$
m \frac{d^2 x}{dt^2} + b \frac{dx}{dt} + k x = 0
$$

1. Derive the general solution for each case.
2. Present the classification of cases: underdamped, critically damped, overdamped.
3. Solve the equation numerically (RK4).
4. Investigate the effect of parameter $b$.
5. Generate the graph of $x(t)$.
6. Generate the phase portrait.

HTML requirement: interactive slider for $b$.

---

## Problem 7 – Forced oscillator and resonance

$$
m \frac{d^2 x}{dt^2} + b \frac{dx}{dt} + k x = F_0 \cos(\Omega t)
$$

1. Solve the equation analytically, determining the amplitude of oscillations as a function of $\Omega$.
2. Solve the equation numerically.
3. Investigate the steady-state amplitude as a function of $\Omega$.
4. Generate the resonance curve.
5. Investigate the phase shift.
6. Interpret the phenomenon of resonance.

HTML requirement: interactive change of the forcing frequency.

---

## Problem 8 – Two coupled springs (two degrees of freedom)

Two masses connected to walls in a series configuration by springs with constants $k_1$, $k_2$, and $k_3$.

1. Write down the equations of motion.
2. Determine the natural frequencies.
3. Find the normal modes.
4. Solve numerically for arbitrary initial conditions.
5. Identify the energy exchange between the masses.

HTML requirement: animation of the motion of both masses.

---

## Problem 9 – Chain of $N$ springs (discrete wave model)

System: $N$ masses connected by springs.

1. Write down the equations of motion.
2. Solve numerically for $N = 20, 50, 100$.
3. Introduce a local initial disturbance.
4. Observe the propagation of the pulse.
5. Investigate the effect of the values of $k$ and $m$ on the propagation speed.

HTML requirement: animation of the entire chain.

---

## Problem 10 – Double pendulum and deterministic chaos

Objective: **purely numerical analysis** of a double pendulum and visualization of deterministic chaos.

Consider a double pendulum (two massive points $m_1, m_2$ on massless rods $l_1, l_2$) in a uniform gravitational field $g$. Assume the equations of motion from the standard form for a double pendulum (we do not derive them analytically in this problem set).

1. Write the coordinates $(x_1,y_1)$ and $(x_2,y_2)$ as functions of the angles $(\theta_1,\theta_2)$ (for animation).
2. Implement a numerical integration of the equations (e.g., RK4) and check numerical stability (e.g., energy drift for different $\Delta t$).
3. Investigate the sensitivity to initial conditions: **simulate simultaneously 50 copies** of the system with minimally different initial conditions (e.g., a perturbation only in $\theta_2(0)$ on the order of $10^{-4}$–$10^{-2}$ rad).
4. Experiment with different scales of perturbation and observe the divergence of the trajectories.

Starting parameters (to standardize results): $m_1=m_2=1$, $l_1=l_2=1$, $g=9.81$, integration step $\Delta t\le 0.01$ s.

HTML requirement: animation of the double pendulum in "ensemble" mode — **50 pendulums simultaneously**, each in a **different color**, to show the divergence; add a reset and the ability to set the perturbation scale.