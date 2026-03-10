# Dynamics Problem Set

## Purpose

Practice Newtonian dynamics with emphasis on:

- correct free-body diagrams (system isolation and force listing),
- correct use of Newton’s laws in an inertial frame,
- friction direction and static vs kinetic logic,
- constraints (a_y = 0, rope constraints, circular constraints),
- translating force models into acceleration and (when needed) into motion using kinematics.

Unless stated otherwise, take g = 9.8 m/s^2.

## Warm-up problems

1. (Net force) Two horizontal forces act on a puck: 5 N east and 12 N west. Find the net force (magnitude and direction).

2. (Newton 2 in 1D) A 3.0 kg block experiences a net horizontal force of 9.0 N to the right. Find its acceleration.

3. (Mass vs weight) A 60 kg person stands still on a scale in an elevator moving at constant speed. What does the scale read (in N)?

4. (Normal force) A 4.0 kg block rests on a horizontal table. An upward force of 10 N is applied to the block. Find the normal force.

5. (Friction threshold) A 6.0 kg crate is on a horizontal floor with mu_s = 0.40. Find the maximum horizontal force that can be applied without causing slipping.

## Standard problems

1. (Horizontal with kinetic friction) A 8.0 kg box is pulled horizontally with force 30 N on a surface with mu_k = 0.25. Find the acceleration.

2. (Angled pull) A 12 kg crate is pulled with a 50 N rope at 25 degrees above horizontal on a surface with mu_k = 0.20. Find the acceleration. (Hint: use y equation to find N.)

3. (Incline, no friction) A 2.5 kg block slides on a frictionless 35-degree incline. Find its acceleration down the plane and the normal force.

4. (Incline, static friction check) A 10 kg block rests on a 20-degree incline with mu_s = 0.30. Determine whether it slips. If it does not slip, find the static friction magnitude.

5. (Spring force at an instant) A 1.5 kg mass on a frictionless horizontal spring (k = 200 N/m) is displaced by x = 0.08 m and released. Find the spring force and acceleration at release.

6. (Elevator “apparent weight”) A 75 kg person stands on a scale in an elevator accelerating upward at 1.6 m/s^2. Find the scale reading.

7. (Atwood machine) Two masses m_1 = 2.0 kg and m_2 = 3.5 kg hang over an ideal pulley. Find the acceleration and tension.

8. (Circular motion, role of centripetal force) A 0.40 kg mass moves in a horizontal circle of radius 0.60 m at speed 5.0 m/s on a string. Find the tension.

## Multi-step problems

1. (Block + hanging mass with friction) A block m_1 = 5.0 kg on a table (mu_k = 0.15) is connected over an ideal pulley to a hanging mass m_2 = 2.0 kg. Assume m_2 moves down.

a) Find a and T.  
b) Find the distance traveled in 3.0 s starting from rest (use kinematics after you find a).

2. (Static → kinetic transition) A 9.0 kg crate on a horizontal floor has mu_s = 0.50 and mu_k = 0.35. A horizontal force F is slowly increased from 0.

a) Find the force at which slipping begins.  
b) Immediately after slipping begins, find the acceleration when the applied force is held fixed at 60 N.

3. (Incline + rope) A 6.0 kg block on a 30-degree incline is pulled up the plane by a rope parallel to the plane with tension T = 40 N. The surface has mu_k = 0.20.

a) Find the acceleration (sign and magnitude).  
b) Determine whether the block moves up or down (consistency check).

4. (Circular motion with normal force) A 900 kg car goes around a flat circular turn of radius 70 m. The coefficient of static friction is mu_s = 0.80.

a) What provides the inward net force?  
b) Find the maximum speed before slipping occurs.

5. (Equation of motion from a force law) A particle of mass 1.0 kg moves in 1D with net force:

$F_{\text{net}}(t) = 4 - 2t$

in newtons, for 0 <= t <= 3 s. Given x(0)=0 and v(0)=1 m/s:

a) Find a(t).  
b) Find v(t) and x(t).  
c) Find x(3).

6. (Equation of motion with position-dependent force) A 0.50 kg particle moves in 1D under:

$F(x) = -3x$

in newtons, where x is in meters.  

a) Write the equation of motion.  
b) At x = 0.20 m, find the acceleration (magnitude and direction).  
c) Describe qualitatively why the motion tends to oscillate about x = 0.

## Conceptual questions

1. In an inertial frame, can an object move with constant velocity while forces act on it? Explain with an example.

2. Why do Newton’s third-law pairs not cancel in a free-body diagram of a single object?

3. A student claims: “If an elevator is moving upward, the normal force must be larger than mg.” What is wrong with this statement?

4. How do you decide the direction of static friction in a problem where the object is not moving?

5. What does the phrase “centripetal force” really mean, and why is it misleading to draw it as an extra force arrow?

6. In an ideal rope and pulley setup, why is tension often the same on both sides? What assumption is being used?

7. When you compute a normal force and get N <= 0, what is the correct physical interpretation?

8. In a dynamics problem, what is the difference between being given a(t) and being given F(t)?

## Challenge problems

1. (Two-body, static friction) A block m_1 on a table is connected over a pulley to a hanging mass m_2. The table is rough with coefficient of static friction mu_s. Find the largest m_2 for which the system can remain at rest. Express your answer in terms of m_1, mu_s, and g.

2. (Vertical circle condition) A mass m on a string moves in a vertical circle of radius R. At the top of the circle, what minimum speed is required to keep the string taut (tension nonnegative)? State your reasoning using the radial force balance.

3. (Piecewise dynamics + kinematics) A 2.0 kg cart is pushed on a horizontal surface with kinetic friction mu_k = 0.10. From t=0 to t=3 s, an applied force of 8 N acts to the right. After t=3 s, the applied force is removed and only friction acts.

a) Find the acceleration on each interval.  
b) Starting from rest at x(0)=0, find v(3) and x(3).  
c) Find how long after t=3 s the cart comes to rest and the total distance traveled.
