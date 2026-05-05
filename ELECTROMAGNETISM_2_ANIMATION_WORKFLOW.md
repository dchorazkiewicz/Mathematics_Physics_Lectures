# Electromagnetism 2 Animation Workflow

This document is the working reference for creating the next HTML animations for:

- `Lecture_Notes/Physics/Electromagnetism_2.qmd`
- `Lecture_Notes/Physics/problems_repo/problem_set_06_electromagnetism_ii.md`

It summarizes what we are doing, where the files live, how we build and test the lecture, and what implementation style we are using for the animations.

## Current Status

At the moment, this is where we are in the `Electromagnetism_2` animation work:

- Problem 1 is implemented as:
  `Lecture_Notes/Physics/html_anim/electromagnetism_2/lorentz_force.html`
- Problem 2 is implemented as:
  `Lecture_Notes/Physics/html_anim/electromagnetism_2/velocity_selector.html`
- Problem 3 is now implemented as:
  `Lecture_Notes/Physics/html_anim/electromagnetism_2/magnetic_moment_loop.html`
- Problem 4 is now implemented as:
  `Lecture_Notes/Physics/html_anim/electromagnetism_2/rotating_loop_ac_generator.html`
- Problem 5 is now implemented as:
  `Lecture_Notes/Physics/html_anim/electromagnetism_2/motional_emf_moving_rod.html`
- Problem 6 is now implemented as:
  `Lecture_Notes/Physics/html_anim/electromagnetism_2/sliding_rod_braking.html`
- Problem 7 is now implemented as:
  `Lecture_Notes/Physics/html_anim/electromagnetism_2/loop_entering_field.html`
- Problem 8 is now implemented as:
  `Lecture_Notes/Physics/html_anim/electromagnetism_2/rl_decay_self_induction.html`

The lecture file currently embeds:

- Lorentz force animation,
- velocity selector animation,
- magnetic moment of a loop animation.
- rotating loop and AC generation animation.
- motional EMF in a moving rod animation.
- sliding rod on rails / electromagnetic braking animation.
- loop entering a magnetic field region animation.
- RL self-induction and decay animation.

So the next natural candidate for implementation is:

- Problem 9: ideal vs. real transformer

That means the current practical sequence is:

```text
done: Problem 1 -> done: Problem 2 -> done: Problem 3 -> done: Problem 4 -> done: Problem 5 -> done: Problem 6 -> done: Problem 7 -> done: Problem 8 -> next: Problem 9
```

## Session checkpoint

This is the current stopping point for the latest session:

- Problem 6 was expanded into a two-perspective animation:
  `Lecture_Notes/Physics/html_anim/electromagnetism_2/sliding_rod_braking.html`
  with side view + top view, clearer vectors, scrolling viewport, and cleaned equation block.
- Problem 7 was implemented as:
  `Lecture_Notes/Physics/html_anim/electromagnetism_2/loop_entering_field.html`
  showing overlap area, flux, EMF, current, and braking force during entry into the field region.
- Problem 8 was implemented as:
  `Lecture_Notes/Physics/html_anim/electromagnetism_2/rl_decay_self_induction.html`
  showing charging, disconnection, exponential decay, coil voltage, and magnetic energy.
- `Lecture_Notes/Physics/Electromagnetism_2.qmd` now embeds Problems 6, 7, and 8 as iframes.
- We are still only building and locally rendering animations.
  We are not publishing or deploying anything yet.
- The next recommended task is:
  Problem 9 - ideal vs. real transformer

## Current Tuning Notes

Important notes from the current state of the project:

- `velocity_selector.html` is intentionally display-scaled for teaching clarity rather than strict SI screen geometry,
- the default selector settings are tuned to a mild visible split around the selected speed,
- particles in the selector stop at the detector,
- the selector beams start from one source point to make the split visually honest,
- `magnetic_moment_loop.html` now uses an interactive 3D scene with orbitable camera,
- `rotating_loop_ac_generator.html` uses 3D geometry plus explicit flux and EMF plots to connect spatial rotation to sinusoidal signals.
- `motional_emf_moving_rod.html` uses a 3D rod-and-field scene to show charge separation and the geometric dependence of `ℰ = B L v sin α`.

## Main Goal

The lecture `Electromagnetism_2.qmd` is organized around concrete physics problems from:

- `Lecture_Notes/Physics/problems_repo/problem_set_06_electromagnetism_ii.md`

Each important problem should get its own dedicated interactive HTML animation placed in:

- `Lecture_Notes/Physics/html_anim/electromagnetism_2`

The lecture then embeds these animations with `iframe`.

So the workflow is:

```text
problem from problem set -> dedicated standalone HTML animation -> iframe in QMD lecture -> Quarto render -> final lecture HTML
```

## Files We Already Use

Main lecture:

- `Lecture_Notes/Physics/Electromagnetism_2.qmd`

Problem set:

- `Lecture_Notes/Physics/problems_repo/problem_set_06_electromagnetism_ii.md`

Animation folder for this lecture:

- `Lecture_Notes/Physics/html_anim/electromagnetism_2`

Animations already present:

- `Lecture_Notes/Physics/html_anim/electromagnetism_2/lorentz_force.html`
- `Lecture_Notes/Physics/html_anim/electromagnetism_2/velocity_selector.html`

General build mechanism description:

- `LECTURE_NOTES_BUILD_MECHANISM.md`

## Important Build Model

We are not building these animations through Python notebooks, matplotlib exports, or a separate frontend app.

For this lecture, the animation files are:

- standalone `.html` files,
- self-contained in structure,
- implemented directly with HTML + CSS + vanilla JavaScript,
- stored inside the lecture animation folder,
- embedded in the `.qmd` lecture through `iframe`.

The lecture itself is rendered with Quarto.

Typical local check:

```bash
quarto render Lecture_Notes/Physics/Electromagnetism_2.qmd
```

That creates:

- `Lecture_Notes/Physics/Electromagnetism_2.html`

This is the main fast feedback loop while working on one lecture.

## What We Use Python For

For these animations, Python is not the implementation tool.

We do not use Python to generate the animation frames or to run the animation logic.
Instead:

- animation logic lives in JavaScript inside the HTML file,
- drawing is done directly on a canvas,
- controls are native HTML sliders and buttons,
- styling is local CSS inside the same file.

Python exists in the repository for other project tasks, but for the `electromagnetism_2` animation work the default approach is:

```text
No Python for the animation itself.
Use standalone HTML/CSS/JS.
Use Quarto only to render the lecture page that embeds the animation.
```

If in the future we need helper calculations, symbolic derivation, or numerical experimentation, Python can be used as a scratch tool during development, but the final student-facing animation should still be a hand-authored standalone HTML file unless we explicitly decide otherwise.

## Standard Animation Design Rules

Each new animation for this lecture should follow these rules.

### 1. The animation must visualize one concrete problem

It should not be only a generic effect.
It should clearly support one task from:

- `Lecture_Notes/Physics/problems_repo/problem_set_06_electromagnetism_ii.md`

The student should be able to look at the animation and understand:

- what the physical setup is,
- what changes,
- what stays constant,
- what the key qualitative conclusion is.

### 2. The animation should be pedagogically clear before being physically fancy

We are optimizing first for:

- conceptual clarity,
- visible cause and effect,
- intuitive geometry,
- readable motion.

Only after that do we worry about extra realism.

This means it is acceptable to use display scaling factors if needed, as long as:

- the qualitative physics is correct,
- the important dependence is preserved,
- the straight/curved/stable/unstable behavior is represented correctly.

### 3. Keep the app self-contained

Each app should ideally contain:

- its own HTML structure,
- its own CSS block,
- its own JavaScript logic,
- no dependency on external frameworks.

This keeps embedding simple and makes future editing easier.

### 4. Match the visual style already used

The current style in this lecture family is established by:

- `lorentz_force.html`
- `velocity_selector.html`

That means:

- light blue panel background,
- rounded cards,
- canvas on the left,
- controls on the right,
- a legend and explanatory info boxes,
- readable teacher-friendly UI.

New animations should stay stylistically close to this family.

## Current Practical Workflow For Each New Animation

When creating the next animation, we should work in this order.

### Step 1. Read the target problem

Open:

- `Lecture_Notes/Physics/problems_repo/problem_set_06_electromagnetism_ii.md`

Decide which exact problem the animation is for.

Extract:

- physical geometry,
- what quantity is changing,
- what parameters are important,
- what the student must notice.

### Step 2. Check the matching chapter in the lecture

Open:

- `Lecture_Notes/Physics/Electromagnetism_2.qmd`

Look for the corresponding chapter and confirm:

- the intended storyline,
- the formula emphasis,
- the planned app behavior,
- the expected filename.

If the chapter already contains an `iframe` path, we should create that exact file.

### Step 3. Implement a dedicated HTML file

Create a new file in:

- `Lecture_Notes/Physics/html_anim/electromagnetism_2`

Recommended naming:

- one file per concept or per problem,
- simple lowercase name,
- underscores if needed.

Examples:

- `rotating_loop.html`
- `moving_rod_emf.html`
- `sliding_rod_braking.html`
- `loop_entering_field.html`
- `rl_decay.html`

### Step 4. Build the animation directly in HTML/CSS/JS

Default implementation pattern:

- wrapper container,
- internal `<style>` block,
- one `<canvas>`,
- control panel with sliders and buttons,
- explanatory text boxes,
- animation loop in JavaScript.

Default technical approach:

- use `canvas`,
- keep simulation state in a `state` object,
- update motion in a function like `update(dt)`,
- draw everything in a function like `draw()`,
- use `requestAnimationFrame(...)`,
- reset state whenever sliders change if that makes the concept clearer.

### Step 5. Tune for teaching clarity

Do not assume that literal SI scales will always look good on screen.

If needed, use display scaling factors such as:

- horizontal motion scaling,
- field effect scaling,
- zoom scaling,
- slower or faster animation time scaling.

But preserve the correct physical relation.

Examples:

- for the velocity selector, the key invariant is that the straight beam occurs for `v = E / B`,
- for Lorentz force, the key invariant is that the force is perpendicular to velocity,
- for RL decay, the key invariant will be exponential growth/decay and time constant behavior.

### Step 6. Render the lecture locally

After each meaningful change, run:

```bash
quarto render Lecture_Notes/Physics/Electromagnetism_2.qmd
```

This is our standard verification step.

Expected warnings:

- Quarto may complain about remote fonts or CDN resources when network is unavailable.

These warnings are acceptable if:

- the lecture HTML is still generated,
- the local animation works,
- there is no actual syntax or render error in our file.

### Step 7. Visually inspect and iterate

Most of the refinement is visual.

Typical iteration topics:

- animation too fast,
- animation too slow,
- split too weak,
- split too strong,
- particle should stop at detector,
- trajectories should start from one source point,
- labels overlap,
- detector should be clearer,
- field region should be longer or shorter,
- controls need better default values.

This is normal and expected.

## Lessons Learned From `velocity_selector.html`

The velocity selector animation already taught us several important workflow rules.

### 1. Use one source point if comparison matters

If the educational goal is to compare trajectories, starting beams from different `y` positions can hide the real effect.

When the point is “same source, different speed, different path”, all particles should start from the same point.

### 2. Stop particles at the detector

If a detector is shown, particles should stop there instead of flying past it.

This makes the detector meaningful and easier to read.

### 3. Split must be visually obvious

Even if the equations are correct, the animation can fail pedagogically if the separation is too small to notice.

It is acceptable to tune a display factor so that:

- the selected beam remains straight,
- the slower beam visibly bends one way,
- the faster beam visibly bends the other way.

### 4. We tune by small parameter edits

During iteration, the most useful adjustable parameters are:

- time scale,
- display velocity scale,
- bend/deflection scale,
- field region width,
- detector position.

These should remain easy to edit in the JS constants area near the top of the file.

## Recommended Template For Future Animations

For future work, this general structure is recommended:

```text
HTML
  wrapper
  title
  short explanatory paragraph
  left canvas panel
  right control panel
  equation/info boxes

CSS
  local styling inside the same file

JavaScript
  constants
  DOM bindings
  getParams()
  resetState()
  update(dt)
  draw()
  animation loop
  slider/button event handlers
```

## What To Do Next

For the next animation, the recommended starting procedure is:

1. Identify the next problem from `problem_set_06_electromagnetism_ii.md`.
2. Read the matching chapter in `Electromagnetism_2.qmd`.
3. Create a new standalone HTML file in `Lecture_Notes/Physics/html_anim/electromagnetism_2`.
4. Reuse the UI style from `lorentz_force.html` and `velocity_selector.html`.
5. Implement the smallest clear version first.
6. Render with Quarto.
7. Tune visually until the physics is immediately understandable.

## Short Working Principle

This is the short version we should remember later:

```text
Each problem in Electromagnetism 2 should get its own standalone HTML animation.
We implement animations directly in HTML/CSS/JS, not in Python.
We embed them in Electromagnetism_2.qmd with iframe.
We verify each iteration with quarto render Lecture_Notes/Physics/Electromagnetism_2.qmd.
We optimize primarily for teaching clarity, then tune motion and display scales until the idea is visually obvious.
```
