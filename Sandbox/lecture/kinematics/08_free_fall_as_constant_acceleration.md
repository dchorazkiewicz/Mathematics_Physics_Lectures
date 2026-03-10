# Free fall as constant acceleration

## Learning goals

- State what “free fall” means in the idealized model and when it is a good approximation.
- Apply constant-acceleration kinematics to vertical motion with a clear **sign convention**.
- Solve both “dropped from rest” and “thrown upward” problems without sign confusion.
- Identify common sign/interpretation mistakes (especially at the top of the motion).

## Why this matters

Free fall is one of the most important constant-acceleration applications. It is also where sign mistakes are most common, because “up/down” intuition can conflict with algebra.

Learning to handle free fall cleanly builds a skill you will use throughout mechanics:

- choose a coordinate axis and stick with it,
- write $$a$$ with the correct sign,
- interpret results physically (especially velocity sign and turning points).

## Core idea

In the ideal free-fall model near Earth:

- the only significant influence is gravity,
- the acceleration has (approximately) constant magnitude $$g$$,
- and it points downward.

So the vertical motion can be modeled as 1D constant-acceleration motion.

This is a **model**, so it comes with assumptions:

- height changes are not so large that $$g$$ varies significantly,
- air resistance is neglected (or is small over the time interval),
- the object’s rotation/shape is not relevant (particle model).

## Mathematical formulation

### Choose a sign convention (two common choices)

You must choose an axis direction and keep it consistent.

**Choice A (often used): upward is positive.**  
Then the acceleration due to gravity is:

$$
a(t) = -g.
$$

**Choice B: downward is positive.**  
Then:

$$
a(t) = +g.
$$

Both are correct; the physics is the same. The algebra only works if you stay consistent.

In either case, once you have the correct sign for $$a$$, you can use the constant-acceleration relations from the previous section.

### Equations (using Choice A: upward positive)

Let $$t_0=0$$ for simplicity. With $$a=-g$$:

Velocity:

$$
v(t) = v_0 - gt.
$$

Position:

$$
x(t) = x_0 + v_0 t - \frac{1}{2}gt^2.
$$

Time-free relation:

$$
v^2 = v_0^2 - 2g(x-x_0).
$$

### Meaning of signs

- If $$v>0$$ (in Choice A), the object is moving upward.
- If $$v<0$$, it is moving downward.
- The acceleration is negative at all times in free fall (Choice A), even at the top, because gravity still points downward.

## Interpretation

### The “top of the motion” is not zero acceleration

When an object is thrown upward, there is an instant at the highest point where:

$$
v = 0.
$$

But acceleration is still:

$$
a = -g.
$$

Velocity can be zero at an instant without acceleration being zero. This is the key conceptual point that prevents a huge class of errors.

### Free fall vs “falling with air resistance”

With significant air resistance, acceleration is not constant: it changes with speed and can approach zero at terminal velocity. In that situation, the constant-acceleration equations are not valid; you need a different model (later, in dynamics).

## Typical examples

1) **Dropped from rest:** $$v_0=0$$ at release, acceleration is constant downward. Solve for time to hit the ground and impact speed.

2) **Thrown upward:** $$v_0>0$$ (if up is positive). Find time to reach maximum height, maximum height itself, and speed on return to the starting point.

3) **Thrown downward:** $$v_0<0$$ (in Choice A). Same equations; the sign tells the initial direction.

## Common mistakes

- Switching sign conventions mid-solution (“up is positive” in one equation, “down is positive” in another).
- Setting acceleration to zero at the top because velocity is zero.
- Using $$g$$ as a signed quantity sometimes and as a magnitude other times without stating which.
- Forgetting that the quadratic position equation can yield two times (on the way up and on the way down) for the same height.
- Using the time-free formula and then choosing the wrong sign for $$v$$ after taking a square root.

## Worked example

An object is thrown straight upward from a balcony. Choose upward as positive (Choice A). At release:

$$
x_0 = 12\,\text{m}, \qquad v_0 = 14\,\text{m/s}.
$$

Take:

$$
g = 9.8\,\text{m/s}^2.
$$

1) How long until the object reaches its highest point?  
2) What is the maximum height?  
3) When does it hit the ground ($$x=0$$), and what is its velocity just before impact?

### Step 1: Time to the highest point

At the top, $$v=0$$. Use:

$$
v(t) = v_0 - gt.
$$

Set to zero:

$$
0 = 14 - 9.8t \;\Rightarrow\; t_{\text{top}} = \frac{14}{9.8} \approx 1.43\,\text{s}.
$$

### Step 2: Maximum height

Use:

$$
x(t) = x_0 + v_0 t - \frac{1}{2}gt^2.
$$

At $$t=t_{\text{top}}$$:

$$
x_{\text{max}} = 12 + 14(1.43) - \frac{1}{2}(9.8)(1.43)^2.
$$

Compute pieces:

$$
14(1.43) \approx 20.02,
$$

$$
\frac{1}{2}(9.8)(1.43)^2 \approx 4.9\cdot 2.04 \approx 9.996.
$$

So:

$$
x_{\text{max}} \approx 12 + 20.02 - 10.00 \approx 22.0\,\text{m}.
$$

### Step 3: Time to hit the ground

Set $$x(t)=0$$:

$$
0 = 12 + 14t - \frac{1}{2}(9.8)t^2.
$$

Multiply by 2 to simplify:

$$
0 = 24 + 28t - 9.8t^2.
$$

Rearrange:

$$
9.8t^2 - 28t - 24 = 0.
$$

Solve the quadratic:

$$
t = \frac{28 \pm \sqrt{(-28)^2 - 4(9.8)(-24)}}{2(9.8)}.
$$

Compute the discriminant:

$$
(-28)^2 - 4(9.8)(-24) = 784 + 940.8 = 1724.8.
$$

$$
\sqrt{1724.8} \approx 41.53.
$$

So:

$$
t = \frac{28 \pm 41.53}{19.6}.
$$

One root is negative (unphysical for “after release”):

$$
t_1 = \frac{28 - 41.53}{19.6} \approx -0.69\,\text{s}.
$$

The physical impact time is:

$$
t_{\text{hit}} = \frac{28 + 41.53}{19.6} \approx 3.55\,\text{s}.
$$

### Step 4: Impact velocity

Use:

$$
v(t) = v_0 - gt.
$$

So:

$$
v_{\text{hit}} = 14 - 9.8(3.55) \approx 14 - 34.79 \approx -20.8\,\text{m/s}.
$$

Interpretation: the negative sign means the object is moving downward at impact (consistent with the chosen axis).

## Mini recap

- Free fall (ideal) near Earth is constant acceleration of magnitude $$g$$ directed downward.
- Choose a sign convention and keep it consistent. If upward is positive:

$$
a=-g, \qquad v(t)=v_0-gt, \qquad x(t)=x_0+v_0t-\frac{1}{2}gt^2.
$$

- At the top of an upward throw: $$v=0$$ but $$a=-g$$ still.
- Watch for two times at the same height and for sign loss when taking square roots in $$v^2$$ relations.
