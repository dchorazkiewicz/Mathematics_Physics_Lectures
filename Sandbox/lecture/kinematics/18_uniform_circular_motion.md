# Uniform circular motion

## Learning goals

- Explain why an object can have nonzero acceleration even when its speed is constant.
- Describe uniform circular motion using radius, angular position, angular speed, period, and frequency.
- Relate speed to angular speed and radius, and compute centripetal (inward) acceleration magnitude.
- Solve basic “car on a circular track / rotating object” problems with consistent units.

## Why this matters

Uniform circular motion is the simplest example that breaks the misconception:

“If speed is constant, acceleration must be zero.”

In circular motion, speed can be constant while the velocity vector changes direction continuously. This is the key intuition that later supports the dynamics idea of a required inward net force for circular motion.

## Core idea

Uniform circular motion means:

- the trajectory is a circle of radius R,
- the speed v is constant,
- direction changes continuously, so velocity changes,
- acceleration points toward the center (inward) even though speed is constant.

## Mathematical formulation

### Angular position, angular speed, period, frequency

Let theta(t) be the angular position (in radians) measured from some reference direction. Uniform circular motion means angular speed is constant:

$$
\omega = \frac{d\theta}{dt} = \text{constant}.
$$

Then:

$$
\theta(t) = \theta_0 + \omega t.
$$

The period T is the time for one full revolution (2pi radians):

$$
T = \frac{2\pi}{\omega}.
$$

The frequency f (revolutions per second, Hz) is:

$$
f = \frac{1}{T}.
$$

So:

$$
\omega = 2\pi f.
$$

### Speed and tangential velocity

The arc length traveled in time t is s = R theta. Differentiate:

$$
v = \frac{ds}{dt} = R\frac{d\theta}{dt} = R\omega.
$$

Velocity direction is tangent to the circle, so the velocity vector is tangential.

### Centripetal (inward) acceleration magnitude

Even though speed is constant, the velocity direction changes. The resulting acceleration points inward and has magnitude:

$$
a = \frac{v^2}{R}.
$$

Using v = R omega, this can also be written as:

$$
a = R\omega^2.
$$

These formulas give the magnitude. The direction is toward the center of the circle.

## Interpretation

- Constant speed does not imply constant velocity. In circular motion, the velocity vector “rotates.”
- Acceleration in uniform circular motion is perpendicular to the velocity (it changes direction of motion, not speed).
- The acceleration magnitude grows quickly with speed: doubling v makes a four times larger.

## Typical examples

1) **Car on a circular track:** compute required inward acceleration (and later, in dynamics, the required inward net force).

2) **Object on a rotating turntable:** relate rotation rate (rev/s) to angular speed and then to tangential speed.

3) **Satellite in circular orbit (idealized):** uniform circular motion provides a first kinematic description; dynamics later provides the cause.

## Common mistakes

- Thinking “constant speed” means “no acceleration.”
- Using degrees for theta and omega in formulas derived for radians. (In v = R omega and a = R omega^2, omega must be in rad/s.)
- Confusing R (radius) with “range” from projectile motion.
- Plugging into a = v^2 / R with inconsistent units (e.g., km/h and meters).
- Saying “centripetal force” in a kinematics section. Here we only talk about acceleration; forces belong to dynamics.

## Worked example

A car drives around a flat circular track of radius:

$$
R = 50\,\text{m}.
$$

Its speed is constant:

$$
v = 15\,\text{m/s}.
$$

Find:

1) the magnitude of the centripetal acceleration,  
2) the period T,  
3) the frequency f.

### Step 1: Centripetal acceleration

Use:

$$
a = \frac{v^2}{R}.
$$

So:

$$
a = \frac{(15)^2}{50} = \frac{225}{50} = 4.5\,\text{m/s}^2.
$$

### Step 2: Period from speed

One revolution distance is the circumference:

$$
2\pi R.
$$

At constant speed, time for one revolution is:

$$
T = \frac{2\pi R}{v} = \frac{2\pi(50)}{15}.
$$

Numerically:

$$
T \approx \frac{314}{15} \approx 20.9\,\text{s}.
$$

### Step 3: Frequency

$$
f = \frac{1}{T} \approx \frac{1}{20.9} \approx 0.0478\,\text{Hz}.
$$

### Optional: Angular speed

$$
\omega = \frac{v}{R} = \frac{15}{50} = 0.30\,\text{rad/s}.
$$

Check consistency:

$$
T = \frac{2\pi}{\omega} \approx \frac{2\pi}{0.30} \approx 20.9\,\text{s},
$$

same as before.

## Mini recap

- Uniform circular motion: circle of radius R, constant speed v, changing velocity direction.
- Angular relations:

$$
\theta(t)=\theta_0+\omega t, \qquad T=\frac{2\pi}{\omega}, \qquad \omega=2\pi f.
$$

- Speed and inward acceleration magnitudes:

$$
v=R\omega, \qquad a=\frac{v^2}{R}=R\omega^2.
$$

- Acceleration points inward; it changes direction of velocity, not its magnitude.
