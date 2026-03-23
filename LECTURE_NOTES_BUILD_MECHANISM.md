# Lecture Notes Build Mechanism

This repository publishes lecture notes to GitHub Pages using two layers:

1. Quarto renders source lecture files from `Lecture_Notes/.../*.qmd` to standalone `.html` files.
2. MkDocs publishes the site from `docs/`, where the physics lecture pages are exposed through symlinks pointing at those generated Quarto HTML files.

## Main mechanism

- The main build script is [`rerun_all.sh`](/home/dch82/repo/Mathematics_Physics_Lectures/rerun_all.sh).
- For physics, it enters `Lecture_Notes/Physics` and runs:

```bash
quarto render <file>.qmd
```

for every `*.qmd` file in that directory.

- This produces HTML lecture pages such as:
  - `Lecture_Notes/Physics/Mechanics.html`
  - `Lecture_Notes/Physics/Waves.html`
  - `Lecture_Notes/Physics/Language_of_physics.html`

- Then the script creates symlinks inside `docs/Physics/...`, for example:
  - `docs/Physics/Mechanics/Mechanics.html` -> `Lecture_Notes/Physics/Mechanics.html`
  - `docs/Physics/Mechanics/Waves.html` -> `Lecture_Notes/Physics/Waves.html`

- `mkdocs.yml` points navigation entries at those HTML files in `docs/`.
- Finally, `rerun_all.sh` runs:

```bash
mkdocs gh-deploy
```

which publishes the whole site to GitHub Pages.

## Important practical consequence

Each lecture `.qmd` file can be rendered independently while writing the lecture. This is useful for checking the final HTML page before rebuilding the full site.

Typical examples:

```bash
cd Lecture_Notes/Physics
quarto render Mechanics.qmd
quarto render Waves.qmd
```

or from the repository root:

```bash
quarto render Lecture_Notes/Physics/Mechanics.qmd
```

This lets me inspect one lecture page locally without rerunning the entire project.

## Full project rebuild

To rebuild the main published materials and redeploy:

```bash
bash rerun_all.sh
```

That script:

- renders all physics `.qmd` files,
- renders mathematics and discrete mathematics notes,
- refreshes symlinks in `docs/`,
- deploys the MkDocs site.

## HTML simulations

The physics notes rely heavily on custom standalone HTML simulations stored under:

- `Lecture_Notes/Physics/html_anim/mechanics`
- `Lecture_Notes/Physics/html_anim/waves`
- `Lecture_Notes/Physics/html_anim/language_of_physics`
- and similar topic folders

These files are often embedded directly in Quarto lecture pages using `iframe`, for example in `Mechanics.qmd`.

So the lecture notes are not only static text rendered from Quarto. They also depend on dedicated hand-made HTML interactive visualizations that illustrate the topic being discussed.

## Mental model

Short version:

```text
QMD source -> Quarto HTML -> symlink into docs/ -> MkDocs nav -> GitHub Pages
```

And separately:

```text
custom HTML simulations -> embedded in QMD via iframe -> visible on final lecture page
```
