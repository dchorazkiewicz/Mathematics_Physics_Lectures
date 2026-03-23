# Problem Set 11

Modern Physics.

---

## Problem 1 – Wave-particle duality (de Broglie)

An electron moves with a velocity of $v = 2.0 \times 10^6 \, \mathrm{m/s}$.


1. Calculate the momentum of the electron.
2. Calculate the de Broglie wavelength.
3. Compare it with the typical size of an atom ($\sim 10^{-10} \, \mathrm{m}$).
4. How will $\lambda$ change when the velocity is doubled?
5. Will the wave effect be easier or harder to observe?

---

## Problem 2 – Bohr model of the hydrogen atom


1. Derive the quantization condition for angular momentum.
2. Derive the formula for the orbit radius.
3. Calculate the energy of the $n=1$ level.
4. Calculate the energy of the $n=3 \to n=2$ transition.
5. Determine the wavelength of the emitted photon.

---

## Problem 3 – Photoelectric effect

For a metal with a work function of $W = 3.2 \, \mathrm{eV}$.


1. Determine the threshold frequency.
2. Calculate the maximum kinetic energy of the electrons for light with $f = 1.5 f_0$.
3. Calculate the stopping potential.
4. Does increasing the intensity change the kinetic energy?
5. What contradicted the classical wave theory?

---

## Problem 4 – Schrödinger equation (1D infinite potential well)

For a well of width $L$:


1. Write down the Schrödinger equation and the boundary conditions.
2. Derive the formula for the energy levels.
3. Calculate the ratio $E_2/E_1$.
4. How does the energy change when $L$ is doubled?
5. Where is the probability maximum for $n=1$?

---

## Problem 5 – Quantum tunneling

A particle with energy $E = 3\ \mathrm{eV}$ approaches a potential barrier with the following parameters:

* $U_0 = 5 \, \mathrm{eV}$
* $a = 0.5 \, \mathrm{nm}$


1. Explain what can happen.
2. Name a physical phenomenon that utilizes tunneling.

---

## Problem 6 – Evolution of a wave packet (illustrative simulation)

1. Build a Gaussian wave packet:

   $$
   \psi(x,0)=e^{-\frac{x^2}{2\sigma^2}} e^{ik_0 x}
   $$

2. Implement the time evolution (FFT).
3. Investigate the spreading of the packet.
4. Interpret it in the context of the uncertainty principle.

Requirement: animation of $|\psi(x,t)|^2$.

---

## Problem 7 – Quantum harmonic oscillator (visualization of levels)


1. Build an HTML/JS application to visualize the probability density for the energy levels $n=0,1,2,3,4,5$.
2. Interpret the shape of the wavefunction and the probability density.
3. Explain why the particle must have zero-point energy.

---

## Problem 8 – Radioactive decay (probabilistic model)

The number of nuclei that have not decayed at time $t$ is given by the formula:

$$
N(t)=N_0 e^{-\lambda t}
$$


1. Implement a Monte Carlo simulation of the decay using random sampling of the decay time for each nucleus following an exponential distribution.
2. Compare the simulation with the analytical solution.
3. Investigate the fluctuations for a small $N_0$.
4. Determine the half-life.

Requirement: graph of the simulation and the continuous solution.

---

## Problem 9 – Nuclear fission and binding energy


1. Explain the concept of mass defect.
2. Calculate the energy released for a mass defect of $\Delta m=0.2 \, \mathrm{u}$.
3. Compare the energy with a chemical reaction.
4. Explain why the maximum of the binding energy occurs around iron.

---

## Problem 10 – Free question

Write a note on any topic related to physics!