# Sinusoidal motion

## Learning goals

- Write a sinusoidal position function with clear meaning of amplitude, angular frequency, and phase.
- Differentiate to obtain velocity and acceleration, and interpret their signs and extrema.
- Relate angular frequency omega to period T and frequency f.
- Solve basic problems: given x(t), find v(t), a(t), and identify when the particle passes equilibrium or reaches extrema.

## Why this matters

Sinusoidal motion is a fundamental pattern in mechanics:

- small oscillations of springs and pendulums,
- vibrations,
- many waves in time.

Even before learning the dynamics that produces it, you can do a lot of kinematics:

- predict when the object is at maximum displacement,
- when it passes equilibrium,
- how velocity and acceleration relate to position.

This section is also a good test of your derivative skills and your interpretation of sign changes.

## Core idea

A sinusoidal position function repeats with a fixed period and has a smooth back-and-forth structure. A standard form is:

“equilibrium position + amplitude × cosine with a phase.”

The key qualitative facts (which you can later prove with derivatives) are:

- velocity is zero at position extrema,
- speed is maximal at equilibrium crossings,
- acceleration tends to point toward equilibrium (for the cosine form), so it is opposite in sign to displacement.

## Mathematical formulation

### Standard form

Use:

$$
x(t) = x_{\text{eq}} + A\cos(\omega t + \phi),
$$

where:

- x_eq is the equilibrium (center) position,
- A is the amplitude (maximum displacement from equilibrium),
- omega is the angular frequency (rad/s),
- phi is the phase constant (radians).

The period is:

$$
T = \frac{2\pi}{\omega},
$$

and frequency is:

$$
f = \frac{1}{T} = \frac{\omega}{2\pi}.
$$

### Velocity and acceleration

Differentiate:

$$
v(t) = \frac{dx}{dt} = -A\omega\sin(\omega t + \phi).
$$

Differentiate again:

$$
a(t) = \frac{dv}{dt} = -A\omega^2\cos(\omega t + \phi).
$$

Notice that:

$$
a(t) = -\omega^2\big(x(t)-x_{\text{eq}}\big).
$$

This relationship is a hallmark of sinusoidal motion and foreshadows the dynamics of a spring-like restoring influence.

### Useful times (extrema and equilibrium crossings)

Position extrema occur when:

$$
v(t)=0 \Rightarrow \sin(\omega t + \phi)=0.
$$

Equilibrium crossings occur when:

$$
x(t)=x_{\text{eq}} \Rightarrow \cos(\omega t + \phi)=0.
$$

These conditions let you find important events without plotting the whole function.

## Interpretation

- Amplitude A sets the largest displacement from equilibrium.
- Larger omega means faster oscillation (shorter period).
- Velocity is shifted in phase by 90 degrees relative to position (cosine vs sine).
- Acceleration is proportional to negative displacement from equilibrium:

$$
a = -\omega^2(x-x_{\text{eq}}).
$$

So when x is above equilibrium (positive displacement), acceleration is negative (toward equilibrium), and vice versa.

## Typical examples

1) **Mass on a spring (preview):** position oscillates sinusoidally about equilibrium.

2) **Small-angle pendulum (preview):** approximately sinusoidal in time for small oscillations.

3) **Vibrating machine component:** measured displacement vs time is often close to sinusoidal.

## Common mistakes

- Confusing omega (rad/s) with f (Hz). They differ by a factor 2pi.
- Using degrees for omega t + phi when taking sine/cosine (these functions assume radians in calculus contexts).
- Forgetting the chain rule: derivative of cos(omega t + phi) brings down a factor omega.
- Mixing up equilibrium position x_eq with amplitude A (they play different roles).
- Thinking acceleration is zero at equilibrium. In sinusoidal motion, acceleration is zero at equilibrium crossings only if the cosine form is centered and there is no offset; more generally use the formula a = -omega^2(x - x_eq).

## Worked example

A particle oscillates along a line with:

$$
x(t) = 0.20\cos(4t),
$$

where x is in meters and t in seconds.

Find:

1) the amplitude A, angular frequency omega, period T, and frequency f,  
2) velocity v(t) and acceleration a(t),  
3) the maximum speed,  
4) the first time t > 0 when the particle passes through equilibrium x = 0.

### Step 1: Identify parameters

Comparing with x(t) = x_eq + A cos(omega t + phi), we have:

$$
x_{\text{eq}}=0, \qquad A=0.20\,\text{m}, \qquad \omega = 4\,\text{rad/s}, \qquad \phi=0.
$$

Then:

$$
T = \frac{2\pi}{\omega} = \frac{2\pi}{4} = \frac{\pi}{2} \approx 1.57\,\text{s},
$$

$$
f = \frac{1}{T} \approx 0.637\,\text{Hz}.
$$

### Step 2: Differentiate for velocity and acceleration

$$
v(t) = -A\omega\sin(\omega t) = -(0.20)(4)\sin(4t) = -0.80\sin(4t)\,\text{m/s}.
$$

$$
a(t) = -A\omega^2\cos(\omega t) = -(0.20)(16)\cos(4t) = -3.2\cos(4t)\,\text{m/s}^2.
$$

### Step 3: Maximum speed

Maximum speed is the amplitude of v(t):

$$
v_{\text{max}} = A\omega = (0.20)(4) = 0.80\,\text{m/s}.
$$

### Step 4: First equilibrium crossing after t=0

Equilibrium means x(t)=0, so:

$$
0.20\cos(4t)=0 \Rightarrow \cos(4t)=0.
$$

The first positive time occurs at:

$$
4t = \frac{\pi}{2} \Rightarrow t = \frac{\pi}{8} \approx 0.393\,\text{s}.
$$

## Mini recap

- Standard sinusoidal position:

$$
x(t)=x_{\text{eq}} + A\cos(\omega t+\phi).
$$

- Period/frequency:

$$
T=\frac{2\pi}{\omega}, \qquad f=\frac{\omega}{2\pi}.
$$

- Velocity and acceleration:

$$
v(t)=-A\omega\sin(\omega t+\phi), \qquad a(t)=-A\omega^2\cos(\omega t+\phi)=-\omega^2(x-x_{\text{eq}}).
$$

- Velocity is zero at extrema; speed is maximal at equilibrium crossings.
