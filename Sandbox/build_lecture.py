#!/usr/bin/env python3

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def ordered_sources() -> list[Path]:
    lecture = ROOT / "lecture"

    sources: list[Path] = [
        lecture / "00_frontmatter.md",
        lecture / "01_introduction.md",
    ]

    kinematics = lecture / "kinematics"
    sources += [kinematics / f"{i:02d}_{name}.md" for i, name in enumerate(
        [
            "reference_frames_and_position",
            "vectors_in_mechanics",
            "trajectory_and_position_function",
            "average_and_instantaneous_velocity",
            "average_and_instantaneous_acceleration",
            "uniform_motion",
            "uniformly_accelerated_motion",
            "free_fall_as_constant_acceleration",
            "piecewise_defined_motion",
            "motion_from_given_x_of_t",
            "motion_from_given_v_of_t",
            "motion_from_given_a_of_t",
            "inverse_kinematics_problems",
            "graphical_interpretation_x_v_a",
            "relative_motion_intro",
            "2d_motion_and_components",
            "projectile_motion",
            "uniform_circular_motion",
            "tangential_and_normal_acceleration",
            "periodic_motion_intro",
            "sinusoidal_motion",
            "kinematics_summary",
            "kinematics_problem_set",
        ],
        start=1,
    )]

    dynamics = lecture / "dynamics"
    sources += [dynamics / f"{i:02d}_{name}.md" for i, name in enumerate(
        [
            "why_kinematics_is_not_enough",
            "concept_of_force",
            "interactions_and_models",
            "newtons_first_law",
            "inertial_frames",
            "newtons_second_law",
            "equation_of_motion",
            "newtons_third_law",
            "weight_and_gravitational_force",
            "normal_force",
            "tension_force",
            "friction_static_and_kinetic",
            "spring_force_hookes_law",
            "free_body_diagrams",
            "resolving_forces_into_components",
            "particle_on_horizontal_surface",
            "particle_on_inclined_plane",
            "connected_bodies_and_tension",
            "circular_motion_and_centripetal_force",
            "dynamics_with_given_force_law",
            "from_force_to_acceleration_to_motion",
            "dynamics_summary",
            "dynamics_problem_set",
        ],
        start=1,
    )]

    combined = lecture / "combined"
    sources += [
        combined / "01_kinematics_to_dynamics_bridge.md",
        combined / "02_comparative_summary.md",
        combined / "03_final_review.md",
    ]

    return sources


def main() -> int:
    sources = ordered_sources()
    missing = [p for p in sources if not p.is_file()]
    if missing:
        print("ERROR: Missing expected lecture source files:", file=sys.stderr)
        for p in missing:
            print(f"  - {p.relative_to(ROOT)}", file=sys.stderr)
        return 2

    parts: list[str] = []
    for p in sources:
        text = p.read_text(encoding="utf-8").rstrip()
        header = f"<!-- SOURCE: {p.relative_to(ROOT)} -->"
        parts.append(header)
        parts.append(text)

    out_dir = ROOT / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "mechanics_lecture_full.md"

    out_path.write_text("\n\n".join(parts).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {out_path.relative_to(ROOT)} ({len(sources)} sections)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

