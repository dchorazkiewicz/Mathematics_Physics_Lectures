# Projectile motion (idealized, no air resistance)

## Learning goals

- Set up projectile motion in 2D using independent horizontal and vertical components.
- Derive the standard time-dependent formulas for position and velocity components under constant gravity.
- Eliminate time to obtain the trajectory equation and interpret what it says.
- Solve for time of flight, maximum height, and range in common launch/landing configurations.

## Why this matters

Projectile motion is a classic example where the “2D components” method pays off immediately:

- the horizontal motion is simple (often uniform),
- the vertical motion is constant-acceleration motion under gravity.

It also trains a crucial modeling skill: knowing exactly which assumptions make the problem solvable with simple equations.

## Core idea

In the ideal projectile model:

- after launch, the only acceleration is gravity,
- gravity points downward with constant magnitude g,
- there is no horizontal acceleration.

So you solve two 1D problems that share the same time variable:

$$
t.
$$

- horizontal: uniform motion,
- vertical: uniformly accelerated motion.

## Mathematical formulation

### Assumptions (state them when you use the model)

1) Motion is near Earth with approximately constant g.  
2) Air resistance is neglected.  
3) The projectile is treated as a particle.  
4) The coordinate system is chosen with x horizontal and y vertical.

Choose y positive upward. Then:

$$
a_x = 0, \qquad a_y = -g.
$$

### Initial conditions (launch)

At time:

$$
t=0,
$$

let:

$$
x(0) = x_0, \qquad y(0) = y_0.
$$

Let the initial speed be v_0 at launch angle theta above the horizontal. Then:

$$
v_x(0) = v_0\cos\theta, \qquad v_y(0) = v_0\sin\theta.
$$

### Solve the horizontal motion

Since horizontal acceleration is zero, horizontal velocity is constant:

$$
v_x(t) = v_0\cos\theta.
$$

Integrate:

$$
x(t) = x_0 + (v_0\cos\theta)t.
$$

### Solve the vertical motion

Since vertical acceleration is constant and equal to -g:

$$
v_y(t) = v_0\sin\theta - gt,
$$

$$
y(t) = y_0 + (v_0\sin\theta)t - \frac{1}{2}gt^2.
$$

### Trajectory equation (time eliminated)

From the horizontal solution:

$$
t = \frac{x-x_0}{v_0\cos\theta}.
$$

Substitute into the vertical position function:

$$
y = y_0 + (v_0\sin\theta)\left(\frac{x-x_0}{v_0\cos\theta}\right) - \frac{1}{2}g\left(\frac{x-x_0}{v_0\cos\theta}\right)^2.
$$

Simplify:

$$
y = y_0 + (x-x_0)\tan\theta - \frac{g}{2v_0^2\cos^2\theta}(x-x_0)^2.
$$

This is a parabola in the x–y plane.

### Maximum height (from v_y = 0)

At the top of the trajectory:

$$
v_y=0.
$$

$$
0 = v_0\sin\theta - gt_{\text{top}} \Rightarrow t_{\text{top}} = \frac{v_0\sin\theta}{g}.
$$

Plug into the vertical position function (or use a constant-acceleration relation) to get the maximum height:

$$
y_{\text{max}} = y_0 + \frac{(v_0\sin\theta)^2}{2g}.
$$

### Time of flight and range (special common case: same launch and landing height)

If the projectile lands at the same vertical level it was launched from, then:

$$
y(t_f)=y_0.
$$

Using:

$$
y(t) = y_0 + (v_0\sin\theta)t - \frac{1}{2}gt^2,
$$

set y(t_f) = y_0 and factor:

$$
0 = (v_0\sin\theta)t_f - \frac{1}{2}gt_f^2 = t_f\left(v_0\sin\theta - \frac{1}{2}gt_f\right).
$$

Ignoring t_f = 0, we get:

$$
t_f = \frac{2v_0\sin\theta}{g}.
$$

Range R is the horizontal displacement during this time:

$$
R = x(t_f)-x_0 = (v_0\cos\theta)t_f = \frac{2v_0^2\sin\theta\cos\theta}{g}.
$$

Using the identity:

$$
2\sin\theta\cos\theta=\sin(2\theta),
$$

$$
R = \frac{v_0^2}{g}\sin(2\theta).
$$

## Interpretation

- Horizontal and vertical motions share the same time variable t, but their accelerations differ: a_x = 0, a_y = -g.
- The trajectory is parabolic in the ideal model, but the time history matters: the projectile does not “follow a parabola at constant speed.”
- The range formula applies only when launch and landing heights are equal and air resistance is neglected.

## Typical examples

1) **Ball thrown from ground level:** compute time of flight, maximum height, and range.

2) **Thrown from a platform (different landing height):** solve the vertical equation for the impact time t, then compute the horizontal position at that time.

3) **Target hit problem:** choose a time t that matches a required horizontal displacement, then check whether the vertical position at that time matches the target height.

## Common mistakes

- Using the equal-height range formula when launch and landing heights differ.
- Forgetting that g is a magnitude while a_y = -g is a signed acceleration (for y positive upward).
- Mixing degrees and radians when using a calculator for sine and cosine.
- Treating horizontal velocity as changing under gravity (in the no-air-resistance model, horizontal velocity is constant).
- Taking a square root in a time-of-flight calculation and forgetting that only nonnegative times are physical.

## Worked example

A ball is thrown from ground level at speed:

$$
v_0 = 20\,\text{m/s}
$$

at an angle:

$$
\theta = 40^\circ
$$

above the horizontal. Neglect air resistance and take:

$$
g = 9.8\,\text{m/s}^2.
$$

Find:

1) time of flight,  
2) maximum height,  
3) range.

### Step 1: Resolve the initial velocity into components

$$
v_x(0) = v_0\cos\theta = 20\cos 40^\circ,
$$

$$
v_y(0) = v_0\sin\theta = 20\sin 40^\circ.
$$

Numerically:

$$
v_x(0) \approx 20(0.766) \approx 15.3\,\text{m/s},
$$

$$
v_y(0) \approx 20(0.643) \approx 12.9\,\text{m/s}.
$$

### Step 2: Time of flight (same launch and landing height)

Use:

$$
t_f = \frac{2v_0\sin\theta}{g} = \frac{2(20)\sin 40^\circ}{9.8}.
$$

Numerically:

$$
t_f \approx \frac{40(0.643)}{9.8} \approx \frac{25.7}{9.8} \approx 2.62\,\text{s}.
$$

### Step 3: Maximum height

Use:

$$
y_{\text{max}} = \frac{(v_0\sin\theta)^2}{2g}.
$$

Numerically:

$$
y_{\text{max}} \approx \frac{(12.9)^2}{19.6} \approx \frac{166}{19.6} \approx 8.47\,\text{m}.
$$

### Step 4: Range

Use either:

$$
R=v_x t_f
$$

or the range formula. Using:

$$
R=v_x t_f,
$$

$$
R \approx (15.3)(2.62) \approx 40.1\,\text{m}.
$$

### Step 5: Quick checks

- Units: time in seconds, height and range in meters.
- Reasonableness: the ball is in the air a few seconds and travels tens of meters—consistent with a 20 m/s throw.

## Mini recap

- Choose axes with y upward, then:

$$
a_x=0, \qquad a_y=-g.
$$

- Component solutions:

$$
x(t)=x_0+(v_0\cos\theta)t,
$$

$$
y(t)=y_0+(v_0\sin\theta)t-\frac{1}{2}gt^2.
$$

- Trajectory equation:

$$
y = y_0 + (x-x_0)\tan\theta - \frac{g}{2v_0^2\cos^2\theta}(x-x_0)^2.
$$

- Equal-height special results:

$$
t_f=\frac{2v_0\sin\theta}{g}, \qquad R=\frac{v_0^2}{g}\sin(2\theta), \qquad y_{\text{max}}=y_0+\frac{(v_0\sin\theta)^2}{2g}.
$$
