# BUILDING THE FULL LECTURE

## What gets built

The builder concatenates all lecture source files (in a fixed pedagogical order) into:

`Sandbox/output/mechanics_lecture_full.md`

It inserts blank lines between files and **fails loudly** if any expected file is missing.

## Source order

The source order is encoded explicitly in `Sandbox/build_lecture.py` as an ordered list of file paths. This avoids fragile automatic discovery and makes edits easy:

- frontmatter
- introduction
- kinematics (01 → 23)
- dynamics (01 → 23)
- combined bridge/synthesis (01 → 03)

## How to run

From the repository root:

`python3 Sandbox/build_lecture.py`

If successful, you will find the merged output at:

`Sandbox/output/mechanics_lecture_full.md`

## After editing a section

1. Edit exactly one section file (preferred workflow).
2. Update `Sandbox/TODO.md` (mark the section status).
3. Re-run:

`python3 Sandbox/build_lecture.py`

