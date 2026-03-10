# STYLE GUIDE — Classical Mechanics Lecture (Kinematics + Dynamics)

## Tone and audience

- **Tone:** precise, calm, pedagogical, university-level.
- **Audience:** students in a first course in classical mechanics (with basic high-school algebra and a first exposure to derivatives/integrals).
- **Priority:** intuition and modeling meaning before formalism; formulas support understanding, not replace it.

## Mathematical writing rules

- Use **display math** for important formulas:

$\text{use this, not inline TeX for key equations}$

- When calculus appears, briefly remind the reader what a derivative/integral *means physically* (rate of change; accumulation/area), without assuming perfect recall.
- Always distinguish **scalar** vs **vector** equations and say explicitly when a statement is component-wise.
- State assumptions for idealized models (e.g., particle model, neglect air resistance, uniform gravity, massless rope).
- Keep notation consistent across files (see below).

## Notation defaults (global)

- time: $t$
- position in 1D: $x(t)$
- position vector: $\vec{r}(t)$
- velocity in 1D: $v(t)$
- velocity vector: $\vec{v}(t)$
- acceleration in 1D: $a(t)$
- acceleration vector: $\vec{a}(t)$
- force: $\vec{F}$
- mass: $m$
- gravitational acceleration magnitude near Earth: $g$

## Section structure (concept files)

Each conceptual section should follow this template unless there is a strong reason not to:

1. Learning goals
2. Why this matters
3. Core idea
4. Mathematical formulation
5. Interpretation
6. Typical examples
7. Common mistakes
8. Worked example (at least one, fully solved)
9. Mini recap (3–6 concise bullets/short paragraphs)

## Examples and problem solving

- Start with simple cases; then add one “slightly richer” variant.
- Show a repeatable workflow (e.g., choose coordinates → write definitions/laws → compute → check units/signs → interpret).
- Avoid unexplained jumps in derivations; make intermediate steps explicit when they carry conceptual load.

