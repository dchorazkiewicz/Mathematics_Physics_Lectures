# PLAN — Classical Mechanics Lecture (Modular Markdown)

This plan defines the full file tree, a short purpose for each section, dependency notes, and a status marker:

- `[ ]` not started
- `[~]` in progress
- `[x]` done

## Frontmatter and introduction

- [x] `lecture/00_frontmatter.md`  
  **Purpose:** Establish the scope (particle mechanics, kinematics → dynamics), prerequisites, notation conventions, and how to use the notes.  
  **Dependencies:** none (sets global conventions).

- [x] `lecture/01_introduction.md`  
  **Purpose:** Give a big-picture map of the course: what mechanics models, why idealizations are used, and how kinematics and dynamics fit together.  
  **Dependencies:** uses notation declared in frontmatter.

## PART I — Kinematics (describe motion without causes)

- [x] `lecture/kinematics/01_reference_frames_and_position.md`  
  **Purpose:** Define reference frames, coordinates, and position as a frame-dependent description.  
  **Dependencies:** uses frontmatter notation; foundational for all kinematics.

- [x] `lecture/kinematics/02_vectors_in_mechanics.md`  
  **Purpose:** Introduce vectors and components as the natural language for displacement, velocity, and acceleration in 2D/3D.  
  **Dependencies:** write after 01; used by 03+ and all 2D sections (16–19).

- [x] `lecture/kinematics/03_trajectory_and_position_function.md`  
  **Purpose:** Separate geometric path (trajectory) from the time-dependent law of motion $\vec{r}(t)$.  
  **Dependencies:** after 01–02.

- [x] `lecture/kinematics/04_average_and_instantaneous_velocity.md`  
  **Purpose:** Define average velocity and the derivative-based instantaneous velocity; distinguish speed vs velocity.  
  **Dependencies:** after 03; used by most later sections.

- [x] `lecture/kinematics/05_average_and_instantaneous_acceleration.md`  
  **Purpose:** Define acceleration as rate of change of velocity (and second derivative of position), including direction-change acceleration.  
  **Dependencies:** after 04; used by 07–08, 18–19, and dynamics bridge.

- [x] `lecture/kinematics/06_uniform_motion.md`  
  **Purpose:** Model constant-velocity motion; connect formulas to graphs and sign conventions.  
  **Dependencies:** after 04.

- [x] `lecture/kinematics/07_uniformly_accelerated_motion.md`  
  **Purpose:** Derive constant-acceleration kinematics (not memorization), emphasizing assumptions and initial conditions.  
  **Dependencies:** after 05; used by 08 and many examples.

- [x] `lecture/kinematics/08_free_fall_as_constant_acceleration.md`  
  **Purpose:** Apply constant-acceleration kinematics to near-Earth free fall with careful sign conventions and common pitfalls.  
  **Dependencies:** after 07.

- [x] `lecture/kinematics/09_piecewise_defined_motion.md`  
  **Purpose:** Handle motion defined by different rules on time intervals; enforce continuity/initial conditions across segments.  
  **Dependencies:** after 04–05 (and preferably after 06–07).

- [x] `lecture/kinematics/10_motion_from_given_x_of_t.md`  
  **Purpose:** Differentiate $x(t)$ or $\vec{r}(t)$ to find velocity/acceleration and interpret turning points and monotonicity.  
  **Dependencies:** after 04–05.

- [x] `lecture/kinematics/11_motion_from_given_v_of_t.md`  
  **Purpose:** Integrate velocity to reconstruct position, highlighting the integration constant and initial position.  
  **Dependencies:** after 04; complements 10.

- [x] `lecture/kinematics/12_motion_from_given_a_of_t.md`  
  **Purpose:** Integrate acceleration to get velocity and position; show how initial conditions determine constants.  
  **Dependencies:** after 05; bridges to dynamics later.

- [x] `lecture/kinematics/13_inverse_kinematics_problems.md`  
  **Purpose:** Solve “backwards” problems: infer motion laws or parameters from constraints and observed features.  
  **Dependencies:** after 10–12; uses graph/derivative ideas.

- [x] `lecture/kinematics/14_graphical_interpretation_x_v_a.md`  
  **Purpose:** Use slope/area interpretations to move between graphs of $x(t), v(t), a(t)$ without full algebra.  
  **Dependencies:** after 04–05; helpful before problem sets.

- [x] `lecture/kinematics/15_relative_motion_intro.md`  
  **Purpose:** Introduce relative position/velocity for moving observers (Galilean intuition, no advanced transforms).  
  **Dependencies:** after 01 and 04; later supports inertial frame discussion (dynamics 05).

- [x] `lecture/kinematics/16_2d_motion_and_components.md`  
  **Purpose:** Analyze planar motion component-wise; relate vector and coordinate forms; emphasize independence of orthogonal components.  
  **Dependencies:** after 02, 04, 05.

- [x] `lecture/kinematics/17_projectile_motion.md`  
  **Purpose:** Derive and solve projectile motion under constant gravity using component decomposition; clarify assumptions and limits.  
  **Dependencies:** after 16 and 07–08.

- [x] `lecture/kinematics/18_uniform_circular_motion.md`  
  **Purpose:** Explain motion at constant speed with changing direction; tangential velocity and inward acceleration.  
  **Dependencies:** after 02, 05, 16.

- [x] `lecture/kinematics/19_tangential_and_normal_acceleration.md`  
  **Purpose:** Decompose acceleration into tangential/normal parts; connect to curvature and circular motion intuition.  
  **Dependencies:** after 18; uses vectors/components.

- [x] `lecture/kinematics/20_periodic_motion_intro.md`  
  **Purpose:** Define periodic motion and the quantities period, frequency, and angular frequency.  
  **Dependencies:** after 04–05; prepares 21.

- [x] `lecture/kinematics/21_sinusoidal_motion.md`  
  **Purpose:** Work with sinusoidal position; compute velocity/acceleration; interpret phase/amplitude and extrema.  
  **Dependencies:** after 20 and 04–05.

- [x] `lecture/kinematics/22_kinematics_summary.md`  
  **Purpose:** Synthesize the kinematics toolbox and the relationships among $x, v, a$ (and vector analogs).  
  **Dependencies:** after all kinematics concept sections.

- [x] `lecture/kinematics/23_kinematics_problem_set.md`  
  **Purpose:** Practice conceptual, computational, graphical, inverse, and multi-step kinematics problems.  
  **Dependencies:** after 22 (or at least after 14).

## PART II — Dynamics (derive motion from interactions)

- [x] `lecture/dynamics/01_why_kinematics_is_not_enough.md`  
  **Purpose:** Motivate forces by showing that describing motion does not explain it; set the need for dynamics.  
  **Dependencies:** after kinematics 22 (or at least after 05 and 12 conceptually).

- [x] `lecture/dynamics/02_concept_of_force.md`  
  **Purpose:** Present force as a measurable interaction model; emphasize vector nature and examples of contact vs distance forces.  
  **Dependencies:** after dynamics 01; uses vectors from kinematics 02.

- [x] `lecture/dynamics/03_interactions_and_models.md`  
  **Purpose:** Teach modeling choices: system boundaries, particle model, simplifications, and what is being neglected.  
  **Dependencies:** after dynamics 02.

- [x] `lecture/dynamics/04_newtons_first_law.md`  
  **Purpose:** Build inertia intuition; explain equilibrium of motion and the role of net force.  
  **Dependencies:** after 03; prepares inertial frames.

- [x] `lecture/dynamics/05_inertial_frames.md`  
  **Purpose:** Define inertial frames and why Newton’s laws require them; connect to relative motion intuition.  
  **Dependencies:** after 04; draws on kinematics 15.

- [x] `lecture/dynamics/06_newtons_second_law.md`  
  **Purpose:** Introduce $\sum \vec{F} = m\vec{a}$ in vector and component form; teach careful interpretation.  
  **Dependencies:** after 05; uses kinematics acceleration concepts.

- [x] `lecture/dynamics/07_equation_of_motion.md`  
  **Purpose:** Show how a force model becomes a differential equation (equation of motion) whose solution is the motion.  
  **Dependencies:** after 06; uses kinematics integration ideas (11–12).

- [x] `lecture/dynamics/08_newtons_third_law.md`  
  **Purpose:** Identify action–reaction pairs and address misconceptions (not “forces cancel” on one body).  
  **Dependencies:** after 06.

- [x] `lecture/dynamics/09_weight_and_gravitational_force.md`  
  **Purpose:** Separate mass from weight; model near-Earth gravity and use it correctly in free-body diagrams.  
  **Dependencies:** after 06 and 08.

- [x] `lecture/dynamics/10_normal_force.md`  
  **Purpose:** Interpret normal force as a constraint/contact force; show when it differs from $mg$.  
  **Dependencies:** after 09.

- [x] `lecture/dynamics/11_tension_force.md`  
  **Purpose:** Model tension in ideal strings/ropes; state pulley assumptions and direction rules.  
  **Dependencies:** after 06 and 08.

- [x] `lecture/dynamics/12_friction_static_and_kinetic.md`  
  **Purpose:** Explain friction direction reasoning; static vs kinetic friction; emphasize inequality for static friction.  
  **Dependencies:** after 10; used heavily in 16–17.

- [x] `lecture/dynamics/13_spring_force_hookes_law.md`  
  **Purpose:** Introduce Hooke’s law as a restoring interaction with clear sign conventions and equilibrium length.  
  **Dependencies:** after 06–07.

- [x] `lecture/dynamics/14_free_body_diagrams.md`  
  **Purpose:** Teach how to isolate a body, list forces, and avoid omission/duplication; the core problem-solving tool in dynamics.  
  **Dependencies:** after 09–13 (at least basic force types introduced).

- [x] `lecture/dynamics/15_resolving_forces_into_components.md`  
  **Purpose:** Choose axes strategically and project forces to simplify Newton’s second law in components.  
  **Dependencies:** after 14; uses kinematics 02 and 16.

- [x] `lecture/dynamics/16_particle_on_horizontal_surface.md`  
  **Purpose:** Solve canonical Newton’s-law problems on flat surfaces with/without friction and angled pulls.  
  **Dependencies:** after 14–15 and 12.

- [x] `lecture/dynamics/17_particle_on_inclined_plane.md`  
  **Purpose:** Solve incline problems with careful decomposition, sign control, and friction cases.  
  **Dependencies:** after 15–16.

- [x] `lecture/dynamics/18_connected_bodies_and_tension.md`  
  **Purpose:** Set up coupled systems with shared acceleration; write separate free-body diagrams and solve simultaneous equations.  
  **Dependencies:** after 11 and 14–15.

- [x] `lecture/dynamics/19_circular_motion_and_centripetal_force.md`  
  **Purpose:** Reinterpret circular-motion acceleration dynamically as a requirement on the net radial force (centripetal role).  
  **Dependencies:** after kinematics 18–19 and dynamics 06.

- [x] `lecture/dynamics/20_dynamics_with_given_force_law.md`  
  **Purpose:** Work with forces depending on position/velocity/time and translate them into equations of motion with stated assumptions.  
  **Dependencies:** after 07; calculus reminder may be needed.

- [x] `lecture/dynamics/21_from_force_to_acceleration_to_motion.md`  
  **Purpose:** Synthesize the pipeline force → acceleration → kinematics; show complete worked bridges back to motion functions.  
  **Dependencies:** after 20; draws heavily on kinematics 11–12.

- [x] `lecture/dynamics/22_dynamics_summary.md`  
  **Purpose:** Compact conceptual synthesis of Newtonian dynamics and a repeatable solving workflow.  
  **Dependencies:** after all dynamics concept sections.

- [x] `lecture/dynamics/23_dynamics_problem_set.md`  
  **Purpose:** Practice free-body analysis, equations of motion, coupled systems, and mixed kinematics+dynamics problems.  
  **Dependencies:** after 22.

## Bridge and final synthesis

- [ ] `lecture/combined/01_kinematics_to_dynamics_bridge.md`  
  **Purpose:** Make explicit the central bridge: in kinematics acceleration can be prescribed; in dynamics it is determined by forces.  
  **Dependencies:** after kinematics 22 and dynamics 06–07.

- [ ] `lecture/combined/02_comparative_summary.md`  
  **Purpose:** Compare description vs explanation; relate kinematic quantities to forces and modeling choices.  
  **Dependencies:** after both summaries (kinematics 22, dynamics 22).

- [ ] `lecture/combined/03_final_review.md`  
  **Purpose:** Provide a final concept map, essential equations, common pitfalls, and a recommended study path.  
  **Dependencies:** last file; after all content.
