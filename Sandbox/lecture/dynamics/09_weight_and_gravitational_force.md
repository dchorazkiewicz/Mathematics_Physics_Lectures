# Weight and gravitational force

## Learning goals

- Distinguish mass (property) from weight (force).
- Model near-Earth gravity as a constant downward force and use it correctly in free-body diagrams.
- Use sign conventions consistently for vertical motion (choose y up or y down and stick with it).
- Interpret “apparent weight” (scale reading) in accelerating situations.

## Why this matters

Confusing mass and weight is one of the fastest ways to break a dynamics solution. It leads to wrong units, wrong equations, and wrong intuition.

This section establishes a clean force model for gravity near Earth and shows how it appears in Newton’s second law problems (elevators, vertical acceleration, normal force contexts).

## Core idea

Mass m is a property of the object: it measures inertia.

Weight is a force: it is the gravitational force exerted on the object by Earth. Near Earth (for many intro problems), we model it as constant in magnitude and directed downward.

So:

- mass is measured in kg,
- weight is measured in N,
- weight depends on the gravitational environment and can change if g changes,
- mass does not change when you go to the Moon.

## Mathematical formulation

### Near-Earth gravity force model

Near Earth, gravitational force on a mass m is:

$\vec{W} = m\vec{g}.$

Here \vec{g} is the gravitational acceleration vector, pointing downward. Its magnitude is approximately:

$$
g \approx 9.8\,\text{m/s}^2.
$$

If you choose y positive upward, then:

$\vec{g} = -g\,\hat{j},$

so the weight force is:

$\vec{W} = -mg\,\hat{j}.$

### Weight vs “apparent weight”

A scale measures the normal force the scale exerts on you. That normal force is sometimes called apparent weight because it is what you feel as “heaviness.”

If you stand on a scale in an elevator, the vertical forces on you are:

- upward normal force N from the scale,
- downward weight mg.

Newton’s second law in y (taking y upward) is:

$N - mg = ma_y.$

So:

$N = m(g + a_y).$

This shows:

- if the elevator accelerates upward (a_y > 0), N > mg (you feel heavier),
- if it accelerates downward (a_y < 0), N < mg (you feel lighter),
- if it is in free fall (a_y = -g), N = 0 (weightless feeling).

## Interpretation

- Weight is the gravitational force on the object. It is always present near Earth regardless of motion.
- Apparent weight depends on acceleration because the normal force adjusts to produce the required net force.
- The symbol g is often used as the magnitude of gravitational acceleration; the sign comes from your coordinate choice.

## Typical examples

1) Object resting on a table: weight downward, normal upward. If acceleration is zero, these balance in y (but that is a net-force statement, not a third-law statement).

2) Elevator: same forces, but net force can be nonzero if accelerating.

3) Falling object with no contact: only weight acts (in the simple model), so acceleration is downward.

## Common mistakes

- Writing “m = mg” or treating g as a force.
- Mixing “g” as a magnitude and “-g” as a signed quantity in the same equation without stating the axis choice.
- Saying “weight changes when you accelerate.” The gravitational force mg does not change in the near-Earth model; the scale reading changes.
- Pairing weight and normal as a third-law pair (they act on the same object; third-law pairs act on different objects).

## Worked example

A person of mass:

$m = 70\,\text{kg}$

stands on a scale in an elevator. Take y upward and g = 9.8 m/s^2.

1) Find the scale reading when the elevator accelerates upward at 1.2 m/s^2.  
2) Find the scale reading when the elevator accelerates downward at 1.2 m/s^2.  
3) Compare both with the “at rest” reading.

### Step 1: Use the force balance equation

For the person:

$$
N - mg = ma_y \Rightarrow N = m(g + a_y).
$$

Compute mg:

$mg = (70)(9.8) = 686\,\text{N}.$

### Step 2: Accelerating upward

Here a_y = +1.2:

$N = 70(9.8 + 1.2) = 70(11.0) = 770\,\text{N}.$

### Step 3: Accelerating downward

Here a_y = -1.2:

$N = 70(9.8 - 1.2) = 70(8.6) = 602\,\text{N}.$

### Step 4: At rest / constant speed (a_y = 0)

$N = mg = 686\,\text{N}.$

Interpretation: the gravitational force mg is the same in all three cases, but the normal force (scale reading) changes because the acceleration changes.

## Mini recap

- Mass m (kg) is not weight.
- Weight is the gravitational force:

$\vec{W} = m\vec{g}.$

- A scale reads the normal force N, which depends on acceleration:

$$
N - mg = ma_y \Rightarrow N = m(g + a_y) \quad \text{(y upward)}.
$$

- “Heavier/lighter” in an elevator is about N, not about changing mg.
