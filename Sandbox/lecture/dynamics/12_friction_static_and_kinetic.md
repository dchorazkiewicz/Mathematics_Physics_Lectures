# Friction: static and kinetic

## Learning goals

- Model friction as a contact interaction that opposes relative slipping (or the tendency to slip).
- Distinguish static friction from kinetic friction and use the correct formula/inequality.
- Determine friction direction by reasoning about the would-be motion (not by guessing a sign).
- Avoid the mistake “friction always equals mu N.”

## Why this matters

Friction is where many dynamics solutions fail, because friction is not a single fixed magnitude with a fixed direction. Its value depends on what the system is trying to do.

In beginner problems, the goal is to learn a reliable method:

- decide whether the contact is sticking or slipping,
- choose static or kinetic friction accordingly,
- use Newton’s laws to solve for the required friction,
- then check whether the result is consistent with the static friction limit.

## Core idea

Friction is a contact force parallel to the surface. It acts to oppose:

- actual relative motion (sliding), or
- the tendency for relative motion (impending slip).

There are two regimes:

- static friction: no slipping at the contact,
- kinetic friction: slipping occurs.

Static friction is “self-adjusting” up to a maximum. Kinetic friction has (in the simplest model) a roughly constant magnitude proportional to the normal force.

## Mathematical formulation

### Static friction

Static friction magnitude f_s satisfies:

$0 \le f_s \le f_{s,\text{max}}.$

The common coefficient model is:

$f_{s,\text{max}} = \mu_s N.$

Important: in static contact, the actual friction magnitude is whatever is needed (within the limit) to prevent slipping.

### Kinetic friction

When slipping occurs, kinetic friction magnitude is modeled as:

$f_k = \mu_k N,$

and it points opposite the direction of relative sliding velocity at the contact.

Typically:

$\mu_k < \mu_s.$

### Direction rule (crucial)

Friction direction is determined by the relative slip direction (kinetic) or the would-be slip direction (static).

Procedure:

1) Predict the direction the object would tend to move relative to the surface if there were no friction.  
2) Friction points opposite that tendency.  
3) Solve for its magnitude using Newton’s laws.  
4) For static friction, check that the required magnitude does not exceed mu_s N.

## Interpretation

- Static friction can be zero (e.g., a book resting on a table with no horizontal forces).
- Static friction can be nonzero without motion (e.g., a block at rest on an incline).
- Kinetic friction does work that typically removes mechanical energy (it dissipates energy as heat in a real system).

The coefficient model is an approximation that works reasonably well in many textbook situations, but it is not a universal law of nature.

## Typical examples

1) Block on a horizontal surface with a small push: static friction matches the push so the block stays at rest (until the push exceeds the maximum).

2) Block sliding on a horizontal surface: kinetic friction has constant magnitude mu_k N opposite the sliding direction.

3) Block on an incline: static friction may hold it at rest; if it slips, kinetic friction acts up the plane when the block slides down.

## Common mistakes

- Using f_s = mu_s N as an equality in all static cases. Correct is f_s <= mu_s N.
- Assigning friction direction without thinking about the would-be motion.
- Mixing static and kinetic coefficients or using mu_k when the contact is not slipping.
- Forgetting that N can change in some situations (inclines, angled pulls), and friction depends on N in the coefficient model.
- Treating friction as always present even when there is no tendency to slip (it can be zero).

## Worked example

A block of mass m = 4.0 kg rests on a rough incline of angle theta = 25 degrees. The coefficient of static friction is mu_s = 0.50. Take g = 9.8 m/s^2.

1) Determine whether the block remains at rest or begins to slide.  
2) If it remains at rest, find the static friction magnitude.

Choose axes parallel and perpendicular to the plane.

### Step 1: Compute the normal force

Perpendicular to the plane the acceleration is zero (it stays in contact), so:

$$
N - mg\cos\theta = 0 \Rightarrow N = mg\cos\theta.
$$

Compute:

$N = (4.0)(9.8)\cos 25^\circ.$

Numerically, cos 25 degrees is approximately 0.906, so:

$$
N \approx 39.2(0.906) \approx 35.5\,\text{N}.
$$

### Step 2: Determine the tendency to slip

The component of weight down the plane is:

$mg\sin\theta.$

Numerically, sin 25 degrees is approximately 0.423, so:

$$
mg\sin\theta \approx 39.2(0.423) \approx 16.6\,\text{N}.
$$

Without friction, the block would tend to slide down the plane. Therefore static friction (if present) points up the plane.

### Step 3: Check the static friction limit

Maximum static friction is:

$$
f_{s,\text{max}} = \mu_s N \approx (0.50)(35.5) \approx 17.8\,\text{N}.
$$

To keep the block at rest, the required static friction magnitude must equal the downslope component:

$$
f_s = mg\sin\theta \approx 16.6\,\text{N}.
$$

Since:

$$
f_s \approx 16.6\,\text{N} \le 17.8\,\text{N} = f_{s,\text{max}},
$$

static friction can supply the needed value. Therefore the block remains at rest.

### Step 4: State the result

- The block does not slide.
- The static friction magnitude is approximately 16.6 N, directed up the plane.

## Mini recap

- Static friction:

$0 \le f_s \le \mu_s N.$

- Kinetic friction:

$f_k = \mu_k N.$

- Direction is opposite slip (kinetic) or opposite the tendency to slip (static).
- In static problems: solve for the required friction, then check it does not exceed mu_s N.
