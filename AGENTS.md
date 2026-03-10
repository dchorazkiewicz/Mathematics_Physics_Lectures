Poniżej masz spójny, kompletny **`AGENTS.md`** do wklejenia do katalogu głównego repo.

````md
# AGENTS.md

## Execution mode and work safety

This project must be developed in a **checkpointed, resumable workflow**.

The agent must **not** try to complete too much work in one uninterrupted pass.  
Instead, it must work in **small, controlled steps**, logging progress after each completed file and stopping for confirmation before continuing further.

The goal is to ensure:
- stable long-form quality,
- easy human review,
- resumable progress,
- low risk of context drift,
- and clear visibility into what has already been completed.

---

## Mandatory checkpoint rule

After completing **each substantive file** (for example a section Markdown file, planning file, or build-related file), the agent must:

1. save the file,
2. update the progress log,
3. update the task tracker,
4. provide a short summary of what was completed,
5. and then **stop and ask whether to continue**.

The agent must not silently continue through many sections in one run.

A “substantive file” means any file that contains actual project work, including:
- `PLAN.md`
- `STYLE_GUIDE.md`
- `TODO.md`
- `WORK_LOG.md`
- `BUILD.md`
- `build_lecture.py`
- any lecture section Markdown file

Very small mechanical actions, such as creating empty directories or creating placeholder stub files in a batch, do **not** require a stop after every single tiny action.  
However, once meaningful content has been written to a file, a checkpoint is required.

---

## Mandatory progress logging

The agent must maintain a persistent progress log inside:

`Sandbox/WORK_LOG.md`

If the file does not exist, create it.

This file must be updated **after every completed substantive file**.

Each log entry must include:
- timestamp if available,
- file path,
- action type (`created`, `drafted`, `revised`, `completed`),
- short summary of what was done,
- open issues or follow-up notes if any.

Recommended format:

```md
## 2026-03-10 18:30

- File: `Sandbox/lecture/kinematics/01_reference_frames_and_position.md`
- Action: `completed`
- Summary:
  - introduced reference frames
  - defined position relative to an origin
  - added 1D and 2D examples
  - included one worked example
- Notes:
  - later verify consistency with vector notation in section 02
````

The log should be append-only unless there is a strong reason to restructure it.

---

## Mandatory resumability

At the start of any new work session, the agent must first inspect:

* `Sandbox/WORK_LOG.md`
* `Sandbox/TODO.md`
* `Sandbox/PLAN.md`

Before doing new work, the agent must determine:

* what has already been completed,
* what is in progress,
* what remains to be done,
* and what the next logical file should be.

The agent must prefer resuming cleanly over regenerating or overwriting completed work.

If a file already exists, the agent must inspect it before editing it.
It must not blindly overwrite prior work.

---

## Mandatory status tracking

In addition to `WORK_LOG.md`, the agent must keep `Sandbox/TODO.md` up to date.

For each file or section, `TODO.md` should indicate one of:

* `[ ] not started`
* `[~] in progress`
* `[x] completed`
* `[R] needs revision`

Whenever a substantive file is completed or revised, the corresponding status in `TODO.md` must be updated immediately.

---

## Human-in-the-loop stop rule

After each checkpoint, the agent must explicitly stop and ask for confirmation to continue.

Preferred wording style:

* “Completed the next file and updated the logs. Continue to the next one?”
* “This section is done and progress was logged. Should I continue?”
* “The file has been created and tracked in WORK_LOG.md and TODO.md. Continue?”

The agent must not continue automatically unless the human explicitly asks it to continue.

---

## Batch creation exception

The agent may perform the following setup actions in one batch without stopping after every micro-step:

* creating the `Sandbox/` directory tree,
* creating empty files,
* creating placeholder stubs,
* initializing `PLAN.md`, `TODO.md`, `STYLE_GUIDE.md`, `WORK_LOG.md`, `BUILD.md`, and `build_lecture.py`

However, once it starts writing actual content into those files, checkpoint behavior must begin.

---

## Recovery rule

If work is interrupted, the agent must be able to resume from the logs.

When resuming, it should:

1. read `WORK_LOG.md`,
2. read `TODO.md`,
3. identify the last completed file,
4. identify the next logical target,
5. continue from there only after confirmation.

---

## Anti-overwrite rule

The agent must avoid destructive rewrites.

If a file already contains substantial content, the agent should:

* review it first,
* revise carefully,
* preserve good material,
* and log the revision in `WORK_LOG.md`.

Do not replace good existing content with newly generated content unless there is a clear improvement and the change is intentional.

---

## Goal

Create a long, coherent, pedagogically strong lecture on **classical mechanics**, split into two main parts:

1. **Kinematics**
2. **Dynamics**

The lecture must be developed in a **modular way**, as a collection of small Markdown files, each covering one narrow subsection.
Do **not** attempt to write the whole lecture in one pass.
The lecture must be built section by section, file by file.

The purpose of this workflow is to maximize:

* coherence,
* pedagogical clarity,
* mathematical correctness,
* consistency of notation,
* and local editability.

---

## Mandatory working directory

All generated work must be created inside a folder named:

`Sandbox/`

If it does not exist, create it.

Do not create the lecture directly in the repository root.
All source files, plans, partial drafts, logs, and build scripts must live under `Sandbox/`.

---

## Required directory structure

Create the following structure:

```text
Sandbox/
├── PLAN.md
├── BUILD.md
├── STYLE_GUIDE.md
├── TODO.md
├── WORK_LOG.md
├── build_lecture.py
│
├── lecture/
│   ├── 00_frontmatter.md
│   ├── 01_introduction.md
│   │
│   ├── kinematics/
│   │   ├── 01_reference_frames_and_position.md
│   │   ├── 02_vectors_in_mechanics.md
│   │   ├── 03_trajectory_and_position_function.md
│   │   ├── 04_average_and_instantaneous_velocity.md
│   │   ├── 05_average_and_instantaneous_acceleration.md
│   │   ├── 06_uniform_motion.md
│   │   ├── 07_uniformly_accelerated_motion.md
│   │   ├── 08_free_fall_as_constant_acceleration.md
│   │   ├── 09_piecewise_defined_motion.md
│   │   ├── 10_motion_from_given_x_of_t.md
│   │   ├── 11_motion_from_given_v_of_t.md
│   │   ├── 12_motion_from_given_a_of_t.md
│   │   ├── 13_inverse_kinematics_problems.md
│   │   ├── 14_graphical_interpretation_x_v_a.md
│   │   ├── 15_relative_motion_intro.md
│   │   ├── 16_2d_motion_and_components.md
│   │   ├── 17_projectile_motion.md
│   │   ├── 18_uniform_circular_motion.md
│   │   ├── 19_tangential_and_normal_acceleration.md
│   │   ├── 20_periodic_motion_intro.md
│   │   ├── 21_sinusoidal_motion.md
│   │   ├── 22_kinematics_summary.md
│   │   └── 23_kinematics_problem_set.md
│   │
│   ├── dynamics/
│   │   ├── 01_why_kinematics_is_not_enough.md
│   │   ├── 02_concept_of_force.md
│   │   ├── 03_interactions_and_models.md
│   │   ├── 04_newtons_first_law.md
│   │   ├── 05_inertial_frames.md
│   │   ├── 06_newtons_second_law.md
│   │   ├── 07_equation_of_motion.md
│   │   ├── 08_newtons_third_law.md
│   │   ├── 09_weight_and_gravitational_force.md
│   │   ├── 10_normal_force.md
│   │   ├── 11_tension_force.md
│   │   ├── 12_friction_static_and_kinetic.md
│   │   ├── 13_spring_force_hookes_law.md
│   │   ├── 14_free_body_diagrams.md
│   │   ├── 15_resolving_forces_into_components.md
│   │   ├── 16_particle_on_horizontal_surface.md
│   │   ├── 17_particle_on_inclined_plane.md
│   │   ├── 18_connected_bodies_and_tension.md
│   │   ├── 19_circular_motion_and_centripetal_force.md
│   │   ├── 20_dynamics_with_given_force_law.md
│   │   ├── 21_from_force_to_acceleration_to_motion.md
│   │   ├── 22_dynamics_summary.md
│   │   └── 23_dynamics_problem_set.md
│   │
│   └── combined/
│       ├── 01_kinematics_to_dynamics_bridge.md
│       ├── 02_comparative_summary.md
│       └── 03_final_review.md
│
└── output/
    └── mechanics_lecture_full.md
```

---

## Core workflow rules

### Rule 1 — One file at a time

Always work on **one substantive file at a time**.

Do not generate multiple large sections in one pass unless explicitly required.
The preferred workflow is:

1. read `PLAN.md`
2. read `TODO.md`
3. read `WORK_LOG.md`
4. select one target file
5. inspect the target file if it already exists
6. write or improve only that file
7. ensure consistency with notation and neighboring sections
8. update `TODO.md`
9. update `WORK_LOG.md`
10. stop and ask whether to continue

---

### Rule 2 — Small sections only

Each source Markdown file should cover **one concept only** or one tightly related cluster of concepts.

Target length:

* short concept files: 500–1000 words
* heavier derivation/example files: 800–1500 words
* summary/problem set files: as needed, but still structured

Never create giant unstructured chapters.

---

### Rule 3 — Pedagogy first

This lecture is for teaching, not just for storing formulas.

Every section must help students:

* build intuition,
* understand what is being modeled,
* connect equations to physical meaning,
* learn how to solve problems step by step,
* avoid common conceptual mistakes.

Do not write encyclopedic text.
Write like a careful university lecturer.

---

### Rule 4 — Mathematics must be readable

All mathematical formulas must use display math blocks:

```text
$$
...
$$
```

Do not use inline TeX for important formulas if display form is clearer.
Prefer clean notation and consistency.

---

### Rule 5 — Consistent notation

Use one notation system throughout the lecture.

Preferred defaults:

* time: $$t$$
* position in 1D: $$x(t)$$
* position vector: $$\vec{r}(t)$$
* velocity in 1D: $$v(t)$$
* velocity vector: $$\vec{v}(t)$$
* acceleration in 1D: $$a(t)$$
* acceleration vector: $$\vec{a}(t)$$
* force: $$\vec{F}$$
* mass: $$m$$
* gravitational acceleration: $$g$$

Do not randomly switch symbols unless there is a didactic reason and it is explicitly explained.

---

## Required file template for content sections

Every conceptual section file should follow this structure unless there is a strong reason not to:

```md
# Section Title

## Learning goals

State what the student should understand or be able to do after reading this section.

## Why this matters

Give motivation. Explain why this concept is needed.

## Core idea

Introduce the concept intuitively before formalism.

## Mathematical formulation

Present definitions, equations, and derivations.

## Interpretation

Explain what the equations mean physically.

## Typical examples

Give simple examples first, then slightly richer ones.

## Common mistakes

List misunderstandings or typical reasoning errors.

## Worked example

Provide at least one complete solved problem step by step.

## Mini recap

Summarize the main idea in 3–6 concise bullets or short paragraphs.
```

For problem set files, use this structure:

```md
# Problem Set Title

## Purpose

## Warm-up problems

## Standard problems

## Multi-step problems

## Conceptual questions

## Challenge problems
```

For summary files, use this structure:

```md
# Summary Title

## Big picture

## Key concepts

## Key equations

## Typical reasoning workflow

## Common pitfalls

## Final recap
```

---

## Lecture architecture and pedagogical logic

The lecture has two major parts.

---

# PART I — KINEMATICS

## Pedagogical role of Part I

Kinematics must explain how motion is described **without asking what causes it**.

It must build a very solid foundation in:

* position,
* displacement,
* velocity,
* acceleration,
* derivatives and integrals in motion,
* going from one kinematic quantity to another,
* interpreting graphs,
* analyzing representative motion models.

Students must leave this part understanding that kinematics describes motion itself, while dynamics explains why that motion occurs.

---

## Kinematics detailed plan

### 1. Reference frames and position

File: `lecture/kinematics/01_reference_frames_and_position.md`

Must include:

* what a reference frame is,
* why position must be defined relative to something,
* coordinate systems in simple settings,
* difference between physical object and its mathematical description,
* examples in 1D and 2D.

Expected outcomes:

* student understands that motion description is frame-dependent,
* student can define position relative to an origin.

---

### 2. Vectors in mechanics

File: `lecture/kinematics/02_vectors_in_mechanics.md`

Must include:

* scalars vs vectors,
* displacement vector,
* basic vector representation,
* components in Cartesian coordinates,
* magnitude and direction,
* why vectors are natural in mechanics.

Expected outcomes:

* student reads and writes vector quantities correctly,
* student understands why position, velocity, and acceleration may be vectors.

---

### 3. Trajectory and position function

File: `lecture/kinematics/03_trajectory_and_position_function.md`

Must include:

* trajectory as geometric path,
* position as function of time,
* distinction between path and law of motion,
* examples of 1D and 2D motion.

Expected outcomes:

* student distinguishes between “where the particle is” and “what path it follows”.

---

### 4. Average and instantaneous velocity

File: `lecture/kinematics/04_average_and_instantaneous_velocity.md`

Must include:

* average velocity,
* limiting process,
* derivative interpretation,
* geometric meaning,
* sign of velocity in 1D,
* difference between speed and velocity.

Expected outcomes:

* student computes velocity from $$x(t)$$ or $$\vec{r}(t)$$,
* student understands instantaneous rate of change.

---

### 5. Average and instantaneous acceleration

File: `lecture/kinematics/05_average_and_instantaneous_acceleration.md`

Must include:

* average acceleration,
* instantaneous acceleration,
* derivative of velocity,
* second derivative of position,
* speed change vs direction change.

Expected outcomes:

* student understands acceleration beyond “speeding up”.

---

### 6. Uniform motion

File: `lecture/kinematics/06_uniform_motion.md`

Must include:

* constant velocity,
* linear position function,
* motion graphs,
* physical interpretation,
* examples with sign and direction.

Expected outcomes:

* student can solve standard uniform motion problems,
* student interprets straight-line graphs correctly.

---

### 7. Uniformly accelerated motion

File: `lecture/kinematics/07_uniformly_accelerated_motion.md`

Must include:

* constant acceleration,
* derivation of $$v(t)$$ and $$x(t)$$,
* standard kinematic formulas,
* careful assumptions,
* meaning of initial conditions.

Expected outcomes:

* student can derive and use the standard equations rather than memorize blindly.

---

### 8. Free fall as constant acceleration

File: `lecture/kinematics/08_free_fall_as_constant_acceleration.md`

Must include:

* idealized free fall,
* choosing sign convention,
* upward/downward motion,
* thrown upward and dropped-from-rest cases,
* common sign errors.

Expected outcomes:

* student applies constant-acceleration equations in gravitational settings.

---

### 9. Piecewise defined motion

File: `lecture/kinematics/09_piecewise_defined_motion.md`

Must include:

* motion changing law over intervals,
* continuity issues,
* reading piecewise definitions,
* example: accelerate, cruise, decelerate.

Expected outcomes:

* student handles realistic segmented motion models.

---

### 10. Motion from given $$x(t)$$

File: `lecture/kinematics/10_motion_from_given_x_of_t.md`

Must include:

* compute velocity and acceleration from position,
* identify turning points,
* monotonicity and rest moments,
* interpretation from algebraic form.

Expected outcomes:

* student performs forward kinematic analysis.

---

### 11. Motion from given $$v(t)$$

File: `lecture/kinematics/11_motion_from_given_v_of_t.md`

Must include:

* integrate velocity to get position,
* role of integration constant,
* use of initial position,
* sign analysis of velocity.

Expected outcomes:

* student reconstructs motion from velocity data.

---

### 12. Motion from given $$a(t)$$

File: `lecture/kinematics/12_motion_from_given_a_of_t.md`

Must include:

* integrate acceleration to get velocity,
* then integrate again to get position,
* role of initial conditions,
* polynomial and simple trigonometric examples.

Expected outcomes:

* student can move from acceleration law to full motion description.

---

### 13. Inverse kinematics problems

File: `lecture/kinematics/13_inverse_kinematics_problems.md`

Must include:

* reasoning backwards from constraints,
* “find the law that matches conditions” type problems,
* identify needed data to reconstruct motion.

Expected outcomes:

* student understands that kinematics also includes inverse reasoning, not only direct computation.

---

### 14. Graphical interpretation of $$x(t)$$, $$v(t)$$, $$a(t)$$

File: `lecture/kinematics/14_graphical_interpretation_x_v_a.md`

Must include:

* slope and area interpretations,
* how to infer one graph from another,
* qualitative reasoning without full algebra,
* examples and non-examples.

Expected outcomes:

* student connects graphs with physical meaning.

---

### 15. Relative motion intro

File: `lecture/kinematics/15_relative_motion_intro.md`

Must include:

* motion relative to moving observers,
* relative position and velocity in simple cases,
* train/boat/walking walkway type problems.

Expected outcomes:

* student understands frame-relative description at a basic level.

---

### 16. 2D motion and components

File: `lecture/kinematics/16_2d_motion_and_components.md`

Must include:

* component-wise motion analysis,
* independence of orthogonal components,
* vector form and coordinate form,
* examples in plane motion.

Expected outcomes:

* student can decompose motion into components.

---

### 17. Projectile motion

File: `lecture/kinematics/17_projectile_motion.md`

Must include:

* horizontal and vertical components,
* derivation under constant gravity,
* trajectory equation,
* range, maximum height, time of flight,
* assumptions and limitations.

Expected outcomes:

* student solves standard projectile problems and understands the decomposition principle.

---

### 18. Uniform circular motion

File: `lecture/kinematics/18_uniform_circular_motion.md`

Must include:

* constant speed, changing direction,
* angular interpretation,
* velocity tangent to circle,
* inward acceleration.

Expected outcomes:

* student understands why acceleration can exist at constant speed.

---

### 19. Tangential and normal acceleration

File: `lecture/kinematics/19_tangential_and_normal_acceleration.md`

Must include:

* decomposition of acceleration,
* role of curvature,
* connection with circular motion,
* qualitative examples.

Expected outcomes:

* student distinguishes speed change from direction change.

---

### 20. Periodic motion intro

File: `lecture/kinematics/20_periodic_motion_intro.md`

Must include:

* what periodic motion means,
* period, frequency, angular frequency,
* repeated states.

Expected outcomes:

* student recognizes cyclic motion patterns.

---

### 21. Sinusoidal motion

File: `lecture/kinematics/21_sinusoidal_motion.md`

Must include:

* sinusoidal position,
* derived velocity and acceleration,
* phase shift and amplitude,
* interpretation of signs and extrema.

Expected outcomes:

* student can differentiate and interpret harmonic-type motion.

---

### 22. Kinematics summary

File: `lecture/kinematics/22_kinematics_summary.md`

Must include:

* conceptual synthesis,
* key equations,
* how the main quantities relate,
* what students should now be able to do.

---

### 23. Kinematics problem set

File: `lecture/kinematics/23_kinematics_problem_set.md`

Must include:

* conceptual questions,
* computational problems,
* graph-based problems,
* inverse problems,
* multi-step mixed problems.

---

# PART II — DYNAMICS

## Pedagogical role of Part II

Dynamics must explain how motion is determined by interactions.
The transition from kinematics to dynamics is central:

* in kinematics, acceleration may be given,
* in dynamics, acceleration is no longer taken as arbitrary,
* instead, acceleration is determined through forces.

Students must understand that:

* force is not motion,
* force is not velocity,
* force is a model of interaction,
* Newton’s laws connect interaction with acceleration.

---

## Dynamics detailed plan

### 1. Why kinematics is not enough

File: `lecture/dynamics/01_why_kinematics_is_not_enough.md`

Must include:

* kinematics describes motion but not its cause,
* motivating examples,
* transition from “what motion is” to “why it happens”.

Expected outcomes:

* student sees the necessity of introducing forces.

---

### 2. Concept of force

File: `lecture/dynamics/02_concept_of_force.md`

Must include:

* force as interaction model,
* not a mystical cause but a measurable physical quantity,
* vector character of force,
* examples from contact and distant interactions.

Expected outcomes:

* student has an operational notion of force.

---

### 3. Interactions and models

File: `lecture/dynamics/03_interactions_and_models.md`

Must include:

* modeling physical systems,
* identifying bodies and interactions,
* simplifications,
* particle model vs extended body intuition.

Expected outcomes:

* student understands that mechanics depends on idealization and modeling choices.

---

### 4. Newton’s First Law

File: `lecture/dynamics/04_newtons_first_law.md`

Must include:

* inertia,
* equilibrium of motion,
* rest and constant-velocity motion as equivalent dynamic states,
* role of net force.

Expected outcomes:

* student stops thinking that motion itself requires force.

---

### 5. Inertial frames

File: `lecture/dynamics/05_inertial_frames.md`

Must include:

* meaning of inertial frame,
* why Newton’s laws need appropriate frames,
* simple intuitive examples.

Expected outcomes:

* student sees that laws of motion are frame-sensitive.

---

### 6. Newton’s Second Law

File: `lecture/dynamics/06_newtons_second_law.md`

Must include:

* net force and acceleration,
* vector form,
* component form,
* mass as measure of inertia,
* careful problem interpretation.

Expected outcomes:

* student can write and solve $$\sum \vec{F} = m\vec{a}$$ in basic systems.

---

### 7. Equation of motion

File: `lecture/dynamics/07_equation_of_motion.md`

Must include:

* from force model to differential equation,
* why equations of motion are the central product of dynamics,
* simple solved forms in 1D.

Expected outcomes:

* student sees the structural link force → acceleration → motion.

---

### 8. Newton’s Third Law

File: `lecture/dynamics/08_newtons_third_law.md`

Must include:

* action-reaction pairs,
* pair identification,
* common misconceptions,
* difference between balancing forces and third-law pairs.

Expected outcomes:

* student correctly identifies interaction pairs.

---

### 9. Weight and gravitational force

File: `lecture/dynamics/09_weight_and_gravitational_force.md`

Must include:

* distinction between mass and weight,
* near-Earth gravitational force,
* vertical motion contexts,
* sign conventions and free-body usage.

Expected outcomes:

* student models gravitational force correctly.

---

### 10. Normal force

File: `lecture/dynamics/10_normal_force.md`

Must include:

* contact constraint interpretation,
* why normal force is not always equal to weight,
* flat and inclined examples.

Expected outcomes:

* student stops using $$N = mg$$ mechanically in all cases.

---

### 11. Tension force

File: `lecture/dynamics/11_tension_force.md`

Must include:

* rope/string idealization,
* direction of tension,
* connected bodies,
* common pulley assumptions.

Expected outcomes:

* student models tension consistently.

---

### 12. Friction: static and kinetic

File: `lecture/dynamics/12_friction_static_and_kinetic.md`

Must include:

* friction as interaction opposing relative slipping tendency,
* static vs kinetic friction,
* inequality for static friction,
* coefficient model,
* sign and direction analysis.

Expected outcomes:

* student avoids treating friction as always equal to $$\mu N$$.

---

### 13. Spring force and Hooke’s law

File: `lecture/dynamics/13_spring_force_hookes_law.md`

Must include:

* restoring tendency,
* sign structure,
* equilibrium length,
* simple examples.

Expected outcomes:

* student can model ideal spring force.

---

### 14. Free-body diagrams

File: `lecture/dynamics/14_free_body_diagrams.md`

Must include:

* what a free-body diagram is,
* how to isolate a body,
* how to choose forces,
* omission and duplication errors.

Expected outcomes:

* student builds correct force diagrams before writing equations.

---

### 15. Resolving forces into components

File: `lecture/dynamics/15_resolving_forces_into_components.md`

Must include:

* choosing axes,
* projections,
* incline-oriented coordinates,
* simplifying equations by good coordinate choice.

Expected outcomes:

* student uses components strategically.

---

### 16. Particle on a horizontal surface

File: `lecture/dynamics/16_particle_on_horizontal_surface.md`

Must include:

* basic free-body setup,
* pull/push cases,
* with and without friction,
* step-by-step solution procedure.

Expected outcomes:

* student solves foundational Newton’s law problems.

---

### 17. Particle on an inclined plane

File: `lecture/dynamics/17_particle_on_inclined_plane.md`

Must include:

* force decomposition,
* normal and parallel directions,
* friction and no-friction cases,
* careful sign control.

Expected outcomes:

* student handles incline mechanics reliably.

---

### 18. Connected bodies and tension

File: `lecture/dynamics/18_connected_bodies_and_tension.md`

Must include:

* shared acceleration,
* separate free-body diagrams,
* tension as internal interaction,
* solved multi-body examples.

Expected outcomes:

* student handles coupled equations.

---

### 19. Circular motion and centripetal force

File: `lecture/dynamics/19_circular_motion_and_centripetal_force.md`

Must include:

* inward acceleration requirement,
* force balance in radial direction,
* examples: string, turn, loop, banked style intuition if relevant.

Expected outcomes:

* student sees centripetal force as role, not a new physical force type.

---

### 20. Dynamics with given force law

File: `lecture/dynamics/20_dynamics_with_given_force_law.md`

Must include:

* force as function of position, velocity, or time in simple examples,
* resulting equations of motion,
* interpretation of model assumptions.

Expected outcomes:

* student connects force laws to differential motion laws.

---

### 21. From force to acceleration to motion

File: `lecture/dynamics/21_from_force_to_acceleration_to_motion.md`

Must include:

* the full conceptual pipeline,
* worked examples bridging dynamics and kinematics,
* explicit comparison with earlier kinematic-only approach.

Expected outcomes:

* student understands the real synthesis of both parts.

---

### 22. Dynamics summary

File: `lecture/dynamics/22_dynamics_summary.md`

Must include:

* conceptual synthesis,
* typical solving workflow,
* major force models,
* Newtonian logic in compact form.

---

### 23. Dynamics problem set

File: `lecture/dynamics/23_dynamics_problem_set.md`

Must include:

* conceptual questions,
* free-body exercises,
* standard equation-of-motion problems,
* coupled-system problems,
* mixed kinematics+dynamics problems.

---

# BRIDGE AND FINAL SYNTHESIS

### 1. Kinematics to dynamics bridge

File: `lecture/combined/01_kinematics_to_dynamics_bridge.md`

Must explicitly explain:

* in kinematics we may prescribe motion,
* in dynamics we derive motion from interactions,
* acceleration is the bridge quantity,
* why both perspectives are necessary.

---

### 2. Comparative summary

File: `lecture/combined/02_comparative_summary.md`

Must compare:

* position / velocity / acceleration vs force,
* description vs explanation,
* direct specification vs model-based derivation.

---

### 3. Final review

File: `lecture/combined/03_final_review.md`

Must provide:

* final conceptual map,
* essential equations,
* common pitfalls,
* recommended learning path for students.

---

## STYLE_GUIDE.md requirements

Create `Sandbox/STYLE_GUIDE.md` and define these rules there:

* tone: precise, calm, pedagogical, university-level
* target audience: first mechanics course
* priority: intuition before formalism
* formulas in `$$ ... $$`
* examples from simple to more complex
* each section must include at least one solved example
* avoid excessive verbosity
* avoid unexplained jumps in derivations
* do not assume students remember calculus perfectly; briefly re-explain derivative/integral meaning when pedagogically needed
* always distinguish clearly between scalar and vector equations
* explicitly mention assumptions in idealized models

---

## PLAN.md requirements

Create `Sandbox/PLAN.md` containing:

1. the full section tree,
2. one-paragraph purpose of each section,
3. dependency notes such as:

   * “write only after section X”
   * “must use notation introduced in Y”
   * “relies on free-body diagrams”
4. status markers:

   * `[ ] not started`
   * `[~] in progress`
   * `[x] done`

---

## TODO.md requirements

Create `Sandbox/TODO.md` as a living task list.

It should track:

* which files exist,
* which files still need writing,
* which files need revision,
* consistency checks still needed,
* whether full rebuild has been performed.

---

## WORK_LOG.md requirements

Create `Sandbox/WORK_LOG.md` as a persistent append-only work log.

It should track:

* completed files,
* revised files,
* short summary of each step,
* open issues,
* follow-up dependencies,
* checkpoint history.

The purpose of this file is to make the whole project resumable without guessing what was done earlier.

---

## BUILD.md requirements

Create `Sandbox/BUILD.md` describing how to merge the files into one lecture.

It must explain:

* source order,
* naming assumptions,
* output path,
* how to rerun the builder after changes.

---

## Build script requirements

Create `Sandbox/build_lecture.py`.

The script should:

1. read files in the correct pedagogical order,
2. concatenate them into:
   `Sandbox/output/mechanics_lecture_full.md`
3. insert blank lines between files,
4. fail loudly if an expected file is missing,
5. be easy to modify.

Prefer explicit ordered file lists over fragile automatic discovery.

---

## Writing standards for each section

Every section should satisfy the following checklist before being considered complete:

* concept introduced clearly
* motivation provided
* notation consistent
* formulas correct
* at least one worked example included
* common mistakes addressed
* recap included
* style consistent with neighboring sections

Before marking a file as completed:

* review internal clarity,
* compare notation with earlier sections,
* update `TODO.md`,
* update `WORK_LOG.md`,
* then stop and ask whether to continue.

---

## Special pedagogical requirements

### Kinematics must strongly emphasize:

* the meaning of derivatives in motion,
* the meaning of integrals in reconstruction,
* distinction between trajectory and time law,
* graphical reasoning,
* inverse reasoning,
* motion with non-constant acceleration,
* sinusoidal and circular examples as nontrivial motion patterns.

### Dynamics must strongly emphasize:

* force as interaction, not as “stored motion”,
* inertia,
* Newton’s laws as modeling principles,
* careful free-body analysis,
* difference between force types and force roles,
* how acceleration becomes determined rather than prescribed,
* explicit bridge from dynamics back to kinematics.

---

## Forbidden behaviors

Do not:

* write the whole lecture in one monolithic file first,
* skip `Sandbox/`,
* invent a different directory structure without strong reason,
* mix notation inconsistently,
* produce formula dumps without explanation,
* rely only on memorized formulas,
* omit worked examples,
* omit common mistakes,
* introduce advanced formalisms unless clearly motivated,
* continue automatically through many substantive files without stopping.

---

## Preferred operating mode

The preferred sequence of work is:

1. create the folder structure
2. create `PLAN.md`, `STYLE_GUIDE.md`, `TODO.md`, `WORK_LOG.md`, `BUILD.md`
3. create `build_lecture.py`
4. create all empty or stub lecture files
5. write frontmatter and introduction
6. write kinematics sections in order
7. write dynamics sections in order
8. write bridge and synthesis sections
9. rebuild full lecture
10. revise for consistency
11. improve transitions between neighboring sections

At every substantive step:

* update `TODO.md`
* update `WORK_LOG.md`
* stop and ask whether to continue

---

## Minimum quality bar

The final lecture should feel like:

* one coherent course,
* not a pile of disconnected notes,
* not raw AI-generated prose,
* not a formula cheat sheet.

It should read like a serious, carefully structured university lecture.

---

## Immediate first task

Your first task is to:

1. create the full `Sandbox/` directory structure,
2. create:

   * `PLAN.md`
   * `STYLE_GUIDE.md`
   * `TODO.md`
   * `WORK_LOG.md`
   * `BUILD.md`
   * `build_lecture.py`
3. create empty or stub Markdown files for all lecture sections,
4. then write:

   * `lecture/00_frontmatter.md`
   * `lecture/01_introduction.md`
   * `lecture/kinematics/01_reference_frames_and_position.md`

Do not skip the planning and scaffolding stage.

After each substantive file:

* update `WORK_LOG.md`
* update `TODO.md`
* summarize what was done
* stop and ask whether to continue

---

## Resume protocol

When starting or resuming work, always do this first:

1. read `Sandbox/WORK_LOG.md`
2. read `Sandbox/TODO.md`
3. read `Sandbox/PLAN.md`
4. determine the last completed substantive file
5. determine the next logical target
6. inspect that target file if it already exists
7. proceed with only one substantive file
8. checkpoint and stop

This protocol is mandatory.

---

## Final output philosophy

This project is not just about generating text.
It is about building a **maintainable lecture system**.

The resulting repository should support:

* iterative writing,
* human review,
* safe resumption,
* modular editing,
* and reliable final assembly.

Every decision should favor:

* clarity,
* recoverability,
* pedagogical quality,
* and structural consistency.
