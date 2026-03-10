# Inertial frames

## Learning goals

- Define an inertial frame as a reference frame where Newton’s first law holds.
- Explain why Newton’s laws are simplest and most reliable in inertial frames.
- Connect inertial frames to relative motion (constant-velocity frames are inertial relative to each other).
- Recognize non-inertial effects qualitatively (why “extra forces” appear in accelerating frames).

## Why this matters

Newton’s laws are not statements about “all viewpoints.” They are statements about motion in special frames of reference.

If you apply Newton’s laws in a frame that is accelerating (like a turning car), you will see apparent effects that look like forces even when there is no physical interaction producing them. Understanding inertial frames prevents confusion and helps you choose a frame that makes problems easiest.

## Core idea

An inertial frame is defined by a simple physical criterion:

In an inertial frame, a particle with zero net force moves at constant velocity.

So inertial frames are the frames in which “free” motion is straight-line, constant-speed motion.

In practice, a frame attached to the ground is often a good approximation to inertial for many lab-scale problems, but not always (for example, for very precise measurements or large-scale Earth rotation effects).

## Mathematical formulation

### Defining property (Newton’s first law)

In an inertial frame:

$$
\sum \vec{F} = \vec{0} \Rightarrow \vec{a}=\vec{0}.
$$

### Relation between inertial frames (Galilean transformation idea)

If two frames move at constant velocity relative to each other (no relative acceleration), then both are inertial. In 1D, if:

$x' = x - ut,$

with constant u, then differentiating gives:

$v' = v - u,$

and:

$a' = a.$

So acceleration is the same in both frames, which is why Newton’s laws keep the same form in any inertial frame.

### What changes in a non-inertial frame (qualitative)

If the frame itself accelerates, then acceleration measurements include the frame’s acceleration. In such a frame, Newton’s second law can still be used if you introduce additional “inertial forces” (also called pseudo-forces) that account for the frame acceleration.

At this stage, the key point is conceptual:

- inertial frame: no extra forces are needed,
- accelerating frame: you must either switch frames or include inertial forces.

## Interpretation

- Inertial frames are not defined by being “at rest.” They are defined by having no acceleration relative to other inertial frames.
- The statement “the laws of physics are the same in all inertial frames” is a powerful simplification of classical mechanics.
- Non-inertial frames can still be used, but you must be careful: apparent forces can appear (for example, in a turning car you feel pushed outward even though the physical acceleration is inward).

## Typical examples

1) Train moving at constant speed: a passenger can do mechanics inside the train as if they were at rest (approximately inertial) because the train is not accelerating.

2) Car that accelerates or turns: the car frame is non-inertial. Loose objects slide relative to the car, and naive application of Newton’s laws without correction leads to confusion.

3) Rotating merry-go-round: objects appear to deflect relative to the rotating platform; describing this in the rotating frame requires inertial forces.

## Common mistakes

- Thinking “inertial” means “not moving.” Constant-velocity motion is inertial.
- Forgetting that the ground is only approximately inertial (usually good enough in intro problems).
- Applying Newton’s laws in an accelerating frame without adding inertial forces or without switching to an inertial frame.
- Treating inertial forces as real interaction forces. They are a bookkeeping device tied to the choice of frame.

## Worked example

A person stands in a train that is moving at constant speed. The person drops a ball from rest relative to the train.

1) Describe the motion as seen from the train frame.  
2) Describe the motion as seen from the ground frame.  
3) Explain why both descriptions are consistent with Newton’s laws without introducing extra forces.

### Step 1: Train frame description (approximately inertial)

In the train frame, the ball is released with zero horizontal velocity (relative to the train) and experiences only gravity vertically. So it falls straight down and lands at the person’s feet (neglect air resistance).

### Step 2: Ground frame description (also inertial)

In the ground frame, at the moment of release the ball already has the train’s horizontal velocity. Gravity provides vertical acceleration, but there is no horizontal acceleration (again neglect air resistance). So the ball follows a projectile-like path: it moves forward while falling.

### Step 3: Why no contradiction

The two frames move at constant velocity relative to each other, so both are inertial. They agree on acceleration:

$a_x = 0, \qquad a_y = -g.$

They disagree on velocity (because of the constant shift u), but that does not affect the force–acceleration relation in Newtonian mechanics. This is why Newton’s laws have the same form in any inertial frame.

## Mini recap

- Inertial frame: a frame where Newton’s first law holds.
- Any constant-velocity frame relative to an inertial frame is also inertial.
- Accelerating frames are non-inertial and require extra inertial forces if you insist on using Newton’s laws in that frame.
- Choose frames strategically: inertial frames simplify dynamics.
