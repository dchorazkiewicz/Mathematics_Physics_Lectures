# Kinematics Problem Set

## Purpose

Practice the full kinematics toolbox:

- definitions of x(t), v(t), a(t) and their meanings,
- differentiation and integration reconstruction,
- sign conventions, turning points, and “speed vs velocity,”
- graph reasoning (slope/area),
- 2D component methods (projectiles, relative motion),
- circular/periodic and sinusoidal motion.

Assume all motion is along a line unless a problem explicitly states 2D. Always choose a coordinate system and state your sign convention.

## Warm-up problems

1. A particle has position:

$$
x(t)=5-3t.
$$

Find v(t), a(t), and the displacement from t=1 s to t=4 s.

2. The position is:

$$
x(t)=2t^2-4t+1.
$$

Find v(t) and a(t). At what times (if any) is the particle instantaneously at rest?

3. A cyclist moves in 1D. At t=0: x=0 m. At t=8 s: x=120 m.  
Find the average velocity on [0,8]. Does this tell you the cyclist’s speed at t=4 s? Explain briefly.

4. A velocity sensor reports:

$$
v(t)=6.
$$

If x(0)=2 m, find x(t).

5. An accelerometer reports:

$$
a(t)=-2.
$$

If v(0)=5 m/s, find v(t). At what time does v become zero?

## Standard problems

1. Constant acceleration. A particle has:

$$
x(0)=0,\qquad v(0)=3\,\text{m/s},
$$

and constant acceleration:

$$
a=1.2\,\text{m/s}^2.
$$

Find x(5 s) and v(5 s).

2. Free fall (sign practice). Choose y upward. A ball is dropped from rest from a height 18 m.  
Find the time to hit the ground and the impact velocity. Use g=9.8 m/s^2.

3. Free fall (thrown upward). A ball is thrown upward from ground level with v_0=12 m/s.  
Find the time to reach maximum height, the maximum height, and the total time to return to the ground (neglect air resistance).

4. Velocity given. A particle has:

$$
v(t)=4t-2.
$$

If x(1)=3 m, find x(t). Then find the displacement from t=1 to t=3.

5. Acceleration given. A particle has:

$$
a(t)=6t.
$$

If v(0)=0 and x(0)=1 m, find v(t) and x(t).

6. Turning point reasoning. A particle moves with:

$$
x(t)=t^3-3t.
$$

For which times is the particle moving in the positive direction? Find all turning times and the corresponding positions.

7. 2D components (basic). A particle has:

$$
\vec{r}(t)=(2t)\hat{i}+(t^2)\hat{j}.
$$

Find \vec{v}(t), \vec{a}(t), and the speed at t=1 s.

8. Relative motion (1D). A train moves east at 20 m/s relative to the ground. A passenger walks west at 1.5 m/s relative to the train.  
Find the passenger’s velocity relative to the ground.

9. Uniform circular motion. A point on a wheel of radius R=0.30 m rotates with frequency f=2.5 Hz.  
Find omega, the tangential speed v, and the centripetal acceleration magnitude a.

## Multi-step problems

1. Piecewise motion (accelerate, cruise, brake). A car starts from rest at x(0)=0.

- From t=0 to t=5 s it accelerates with a=2.0 m/s^2.
- From t=5 to t=12 s it moves with constant velocity.
- From t=12 s onward it brakes with a=-3.0 m/s^2 until it stops.

Find:

a) v(t) and x(t) on each interval,  
b) the stopping time,  
c) the total distance traveled.

2. “Back and forth” with areas. The velocity graph is described as:

- v increases linearly from 0 to 6 m/s on 0<=t<=2 s,
- then stays constant at 6 m/s on 2<=t<=4 s,
- then decreases linearly from 6 m/s to -2 m/s on 4<=t<=7 s.

Assume x(0)=0. Find x(7), and find the turning time when the particle changes direction.

3. Inverse kinematics (fit a quadratic). Assume constant acceleration and t_0=0. A particle satisfies:

$$
x(0)=1\,\text{m},\qquad x(2)=9\,\text{m},\qquad v(2)=0.
$$

Find x(t), v(t), and a. Check your result by interpreting the turning time.

4. Projectile motion (same launch/landing height). A ball is launched from ground level with v_0=18 m/s at angle 35 degrees above horizontal. Neglect air resistance.

a) Find the time of flight.  
b) Find the maximum height.  
c) Find the range.

5. Projectile motion (different landing height). A ball is thrown from a balcony at height y_0=12 m with speed 16 m/s at angle 30 degrees above horizontal. Use g=9.8 m/s^2. Neglect air resistance.

a) Find the time when it hits the ground (y=0).  
b) Find the horizontal distance from the balcony at impact.  
c) Find the impact velocity components.

6. Tangential + normal acceleration. A car moves through a curve of radius R=60 m. At an instant its speed is v=22 m/s and dv/dt= -1.0 m/s^2.

a) Find a_t and a_n.  
b) Find the magnitude of the total acceleration.  
c) Is the car speeding up or slowing down at that instant?

7. Sinusoidal motion (kinematics only). A particle has:

$$
x(t)=0.15\cos(5t-\frac{\pi}{3}).
$$

a) Find v(t) and a(t).  
b) Find T and f.  
c) Find the first time t>0 when x(t)=0.

## Conceptual questions

1. In 1D, can a particle have v=0 and a not equal to 0 at the same instant? Give a physical example.

2. In 2D, can a particle have constant speed but nonzero acceleration? Explain without using forces.

3. What is the difference between displacement and distance traveled? Give a motion where the displacement is zero but the distance is not.

4. If x(t) is a straight line on a graph, what can you say about v(t) and a(t)? State both mathematically and in words.

5. A student says: “Negative acceleration means the object is slowing down.” What is missing from this statement? Provide a corrected version.

6. You are given a trajectory curve in the x–y plane. Does that determine the motion uniquely? What information is missing?

7. Two motions have the same trajectory circle. One completes a revolution in 2 s, the other in 4 s. Compare their speeds and centripetal accelerations.

8. In sinusoidal motion, why does velocity reach its maximum magnitude at equilibrium crossings?

## Challenge problems

1. (Mixed reconstruction) A particle has acceleration:

$$
a(t)=k\sin(\omega t),
$$

with constants k and omega. Given v(0)=0 and x(0)=0:

a) find v(t) and x(t),  
b) find the displacement over one full period T=2pi/omega,  
c) interpret whether the particle necessarily returns to x=0 after one period.

2. (Non-constant acceleration, still kinematics) A particle has:

$$
x(t)=t^2\sin t.
$$

a) find v(t) and a(t),  
b) find all times in 0<=t<=2pi when v(t)=0 (you may leave answers in implicit form),  
c) explain why finding turning points can be harder than finding where x(t)=0.

3. (Constraint/inverse) A particle moves in 1D. Assume x(t) is a cubic polynomial. You are told:

$$
x(0)=0,\qquad x(1)=2,\qquad v(0)=0,\qquad v(1)=0.
$$

a) find x(t),  
b) determine where (in time) the particle changes direction,  
c) compute the maximum position reached on 0<=t<=1.
