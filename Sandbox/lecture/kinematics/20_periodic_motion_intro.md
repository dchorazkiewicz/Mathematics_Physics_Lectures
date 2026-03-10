# Periodic motion (intro)

## Learning goals

- Define what it means for a motion to be periodic.
- Use the quantities period T, frequency f, and angular frequency omega, and convert between them.
- Recognize what “repeating state” means (position alone vs full state including velocity).
- Solve simple timing/counting questions for periodic motions (rotations, cycles, oscillations).

## Why this matters

Many systems in mechanics repeat patterns:

- rotating wheels,
- circular motion,
- oscillations (springs, pendulums, vibrations).

Before studying any particular model (like sinusoidal motion), you need a clear language for repetition: period, frequency, and phase-like ideas. This language also prevents unit mistakes (Hz vs rad/s, seconds vs cycles).

## Core idea

A motion is periodic if it repeats itself after a fixed time interval. The simplest definition uses a position function:

“The position repeats after time T.”

But often the full physical situation repeats only when both position and velocity repeat. For example, in many oscillations the object passes the same position twice per cycle with opposite velocity directions.

So you should be clear what is meant by “repeats” in a given context.

## Mathematical formulation

### Periodic position function

We say that position is periodic with period T if:

$$
x(t+T) = x(t)
$$

for all t in the interval of interest.

For vector motion (2D/3D):

$$
\vec{r}(t+T) = \vec{r}(t).
$$

### Period, frequency, angular frequency

- Period T: time for one full cycle (seconds).
- Frequency f: cycles per second (Hz):

$$
f = \frac{1}{T}.
$$

- Angular frequency omega: radians per second:

$$
\omega = 2\pi f = \frac{2\pi}{T}.
$$

These are different ways to describe the same “rate of repetition,” but the units are different.

### Counting cycles

If a motion has frequency f, then the number of cycles completed in time interval Delta t is:

$$
N = f\,\Delta t.
$$

If you know the period T instead:

$$
N = \frac{\Delta t}{T}.
$$

## Interpretation

- Frequency f tells you “how many cycles per second.”
- Angular frequency omega tells you “how many radians of phase per second” for motions that can be described by an angle-like phase.
- Period T is often easiest to visualize physically (“one cycle takes T seconds”).

Be careful: omega is not “revolutions per second.” It is radians per second. A wheel rotating at 1 revolution per second has omega = 2pi rad/s.

## Typical examples

1) **Uniform circular motion:** angle increases linearly with time; position repeats every revolution.

2) **A blinking light:** periodic intensity; a simple non-mechanical analogy.

3) **Back-and-forth oscillation:** position repeats every cycle, but a given position can occur twice per period with opposite velocity.

## Common mistakes

- Confusing frequency f (Hz) with angular frequency omega (rad/s).
- Forgetting the factor 2pi in omega = 2pi f.
- Saying “the motion repeats when it reaches the same position” without checking velocity direction (state may not repeat).
- Mixing “cycles” with “radians” in the same equation without conversion.

## Worked example

A wheel rotates uniformly. It makes 180 revolutions in 2 minutes.

Find:

1) the frequency f in Hz,  
2) the period T in seconds,  
3) the angular frequency omega in rad/s,  
4) how many radians the wheel rotates in 5 seconds.

### Step 1: Convert time and compute frequency

2 minutes is:

$$
120\,\text{s}.
$$

Frequency is revolutions per second:

$$
f = \frac{180}{120} = 1.5\,\text{Hz}.
$$

### Step 2: Period

$$
T = \frac{1}{f} = \frac{1}{1.5} \approx 0.667\,\text{s}.
$$

### Step 3: Angular frequency

$$
\omega = 2\pi f = 2\pi(1.5) = 3\pi \approx 9.42\,\text{rad/s}.
$$

### Step 4: Angle rotated in 5 seconds

Uniform rotation means angle increases linearly:

$$
\Delta\theta = \omega \Delta t = (3\pi)(5) = 15\pi \approx 47.1\,\text{rad}.
$$

Interpretation: 47.1 rad is about 7.5 revolutions, since 2pi rad is one revolution.

## Mini recap

- Periodic position: x(t+T) = x(t) (and similarly for vectors).
- Period, frequency, angular frequency:

$$
f=\frac{1}{T}, \qquad \omega = 2\pi f = \frac{2\pi}{T}.
$$

- Count cycles: N = f Delta t = Delta t / T.
- Always track units: Hz (cycles/s) vs rad/s.
