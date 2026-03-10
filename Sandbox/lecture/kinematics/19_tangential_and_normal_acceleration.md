# Tangential and normal acceleration

## Learning goals

- Decompose acceleration into a part that changes speed (tangential) and a part that changes direction (normal).
- Use the relations for tangential and normal acceleration in common situations.
- Connect curvature (radius of curvature) to the required normal acceleration for a given speed.
- Interpret motion qualitatively: “speeding up vs turning” and how both can happen at once.

## Why this matters

Acceleration is often misunderstood as “the thing that makes you go faster.” In 2D motion, acceleration has two independent roles:

- it can change the magnitude of the velocity (speed),
- it can change the direction of the velocity.

The tangential/normal decomposition is a clean way to separate these roles. It also creates a direct bridge between kinematics (geometry of motion) and dynamics (required forces) later.

## Core idea

At each instant, the velocity vector points along the tangent to the trajectory. Acceleration can be split into:

- a tangential component (along the velocity direction) that changes speed,
- a normal component (perpendicular to velocity, toward the center of curvature) that changes direction.

Uniform circular motion is the special case where speed is constant, so tangential acceleration is zero and only normal acceleration remains.

## Mathematical formulation

Let v = |\vec{v}| be the speed. At any instant, define:

- \hat{t}: unit vector tangent to the trajectory (direction of \vec{v}),
- \hat{n}: unit vector normal to the trajectory pointing toward the center of curvature.

Then acceleration decomposes as:

$$
\vec{a} = a_t \hat{t} + a_n \hat{n}.
$$

### Tangential acceleration (changes speed)

The tangential component equals the time rate of change of speed:

$$
a_t = \frac{dv}{dt}.
$$

So if speed is constant, dv/dt = 0 and:

$$
a_t = 0.
$$

### Normal acceleration (changes direction)

If the trajectory has instantaneous radius of curvature R, then the normal component has magnitude:

$$
a_n = \frac{v^2}{R}.
$$

Its direction is toward the center of curvature (inward for circular motion).

For uniform circular motion, R is the circle radius and a_n is the centripetal acceleration from the previous section.

### Combining magnitudes (perpendicular components)

Since the tangential and normal directions are perpendicular, the acceleration magnitude is:

$$
|\vec{a}| = \sqrt{a_t^2 + a_n^2}.
$$

## Interpretation

- If \vec{a} is parallel to \vec{v}, the particle changes speed but not direction (purely tangential acceleration; straight-line motion).
- If \vec{a} is perpendicular to \vec{v}, the particle changes direction but not speed (purely normal acceleration; uniform circular motion locally).
- In general, both can occur simultaneously: a car can speed up while turning.

The normal component grows like v^2, so at higher speeds, even gentle turns require large normal acceleration.

## Typical examples

1) **Car turning at constant speed:** a_t = 0, a_n = v^2 / R.

2) **Car speeding up in a straight line:** a_n = 0, a_t = dv/dt.

3) **Car accelerating through a curve:** both a_t ≠ 0 and a_n ≠ 0.

## Common mistakes

- Saying “acceleration is toward the center” for all curved motion. Only the normal component is toward the center of curvature; there can also be a tangential component.
- Using a_n = v^2 / R with R misunderstood (it is radius of curvature, not “distance to origin”).
- Confusing a_t with dv_x/dt or dv_y/dt. Tangential acceleration is about speed v, not a particular coordinate component.
- Forgetting that a_t can be negative (speed decreasing) even if the object is still moving forward.

## Worked example

A car moves along a curved road. At a certain instant:

- its speed is:

$$
v = 20\,\text{m/s},
$$

- its speed is increasing at a rate:

$$
\frac{dv}{dt} = 1.5\,\text{m/s}^2,
$$

- the radius of curvature of the road at that point is:

$$
R = 80\,\text{m}.
$$

Find:

1) a_t,  
2) a_n,  
3) the magnitude of the total acceleration.

### Step 1: Tangential component

By definition:

$$
a_t = \frac{dv}{dt} = 1.5\,\text{m/s}^2.
$$

### Step 2: Normal component

Use:

$$
a_n = \frac{v^2}{R} = \frac{(20)^2}{80} = \frac{400}{80} = 5.0\,\text{m/s}^2.
$$

### Step 3: Total acceleration magnitude

Perpendicular components combine via Pythagoras:

$$
|\vec{a}| = \sqrt{a_t^2 + a_n^2} = \sqrt{(1.5)^2 + (5.0)^2}.
$$

Compute:

$$
|\vec{a}| = \sqrt{2.25 + 25} = \sqrt{27.25} \approx 5.22\,\text{m/s}^2.
$$

Interpretation: most of the acceleration is devoted to changing direction (normal component), while a smaller part changes speed.

## Mini recap

- Decomposition:

$$
\vec{a} = a_t \hat{t} + a_n \hat{n}.
$$

- Tangential part changes speed:

$$
a_t = \frac{dv}{dt}.
$$

- Normal part changes direction (radius of curvature R):

$$
a_n = \frac{v^2}{R}.
$$

- Total magnitude:

$$
|\vec{a}|=\sqrt{a_t^2+a_n^2}.
$$
