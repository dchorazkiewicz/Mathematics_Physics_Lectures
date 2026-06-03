# Old_school — General Agent Working Rules

## 1. Purpose

This document defines the general rules for working with lecture-note projects inside the `Old_school` directory.

The repository is used to develop academic lecture notes in LaTeX. The final output of each project is a compiled PDF document.

The work is performed interactively with AI agents. The human author gives small, precise instructions. The agent modifies the relevant source files, compiles the document, checks the result, and reports what was changed.

The most important principle is:

```text
small change → compilation → PDF review → next small change
```

The agent should not try to complete or rewrite whole lecture courses unless explicitly instructed to do so.

---

## 2. Main projects

The `Old_school` directory contains three main lecture-note projects:

```text
Old_school/
├── Math/
│   ├── Math/
│   └── Prob_meth/
└── Phys/
```

The projects are:

1. `Old_school/Math/Math`
   General mathematics lecture notes.

2. `Old_school/Math/Prob_meth`
   Probabilistic methods lecture notes.

3. `Old_school/Phys`
   General physics lecture notes.

Each project should be treated as a separate LaTeX project.

---

## 3. Language policy

All visible teaching materials should be written in **English**, unless the human author explicitly requests another language.

This includes:

* chapter titles,
* section titles,
* definitions,
* examples,
* theorems,
* explanations,
* tables,
* figure captions,
* PDF-visible notes and comments.

Polish may be used only for internal repository notes, temporary TODO comments, or when explicitly requested.

---

## 4. Document class and page layout

All lecture-note projects should use the LaTeX `report` class.

Default setup:

```latex
\documentclass[11pt,a4paper]{report}
```

The page margins should be 2.5 cm:

```latex
\usepackage[a4paper,margin=2.5cm]{geometry}
```

The standard compilation engine is `pdflatex`, unless the project later explicitly requires another engine.

Preferred compilation command:

```bash
pdflatex main.tex
pdflatex main.tex
```

The second run is needed for references, the table of contents, numbering, and cross-references.

---

## 5. Modular LaTeX principle

The lecture notes must not be written as one huge monolithic LaTeX file.

Each project should have a clear `main.tex`, but the main file should only assemble the document.

The main file should:

1. declare the document class,
2. load the preamble,
3. load macros,
4. load visual styles,
5. start the document,
6. include the table of contents,
7. include chapter files,
8. end the document.

The actual teaching content should be stored in smaller files.

A typical structure is:

```text
CourseFolder/
├── main.tex
├── preamble.tex
├── macros.tex
├── styles.tex
├── chapters/
│   ├── topic_one/
│   │   ├── first_section.tex
│   │   └── second_section.tex
│   ├── topic_two/
│   │   └── first_section.tex
│   ├── chapter_topic_one.tex
│   └── chapter_topic_two.tex
├── figures/
└── output/
```

The `chapters` directory contains:
- A subdirectory for each topic, containing the `.tex` files for the sections of that chapter.
- A `chapter_*.tex` file for each chapter, which acts as a "table of contents" for that chapter, including the section files.

The goal is to make each file readable, reviewable, and easy to edit.

A single source file should usually correspond to a chapter, section, or substantial subsection. It does not need to be extremely small, but it should not become so large that it is difficult to inspect.

---

## 6. Main-file rule

Every project must have a `main.tex`.

A typical `main.tex` should look like this:

```latex
\documentclass[11pt,a4paper]{report}

\input{preamble}
\input{macros}
\input{styles}

\begin{document}

\tableofcontents

\include{chapters/chapter_topic_one}
\include{chapters/chapter_topic_two}

\end{document}
```

Each `chapter_*.tex` file may then include smaller section files from its dedicated folder:

```latex
% In chapters/chapter_linear_algebra.tex
\chapter{Linear Algebra}

\input{chapters/linear_algebra/vectors}
\input{chapters/linear_algebra/matrices}
\input{chapters/linear_algebra/systems_of_linear_equations}
```

The agent should normally work on the smallest relevant file.

---

## 7. Editing discipline

When the human author asks for a change, the agent should first classify the request as one of the following:

1. **Local change**
   A change affecting one section, example, table, figure, or paragraph.

2. **Structural change**
   A change affecting chapter order, included files, project structure, or the `main.tex`.

3. **Document-wide style change**
   A change affecting shared styles, macros, theorem boxes, table formatting, layout, or typography.

For a local change, edit only the relevant content file.

For a structural change, edit the relevant `chapter.tex`, `main.tex`, or folder structure.

For a document-wide style change, edit shared files such as:

```text
preamble.tex
macros.tex
styles.tex
```

The agent should not mix these levels unless necessary.

For example, if the task is:

```text
Add two examples explaining acceleration in one-dimensional motion.
```

then the agent should probably edit only:

```text
chapters/kinematics/one_dimensional_motion.tex
```

If the task is:

```text
Make all definition boxes more colorful.
```

then the agent should probably edit:

```text
styles.tex
```

and then recompile.

---

## 8. Incremental work

The work should proceed through small, controlled steps.

Preferred workflow:

```text
inspect project → identify target file → edit small part → compile → report result
```

The agent should not rewrite unrelated files.

The agent should not reorganize the project unless explicitly asked.

The agent should not generate large amounts of new lecture content unless explicitly asked.

Good tasks:

```text
Add a short subsection about matrix multiplication.
```

```text
Add a table comparing velocity and acceleration.
```

```text
Improve the explanation of conditional probability.
```

```text
Add a TikZ diagram for one-dimensional motion.
```

```text
Make theorem boxes visually clearer.
```

Bad tasks, unless explicitly confirmed:

```text
Rewrite the whole document.
```

```text
Create the full course content at once.
```

```text
Change all chapters without asking.
```

---

## 9. Compilation rule

After every substantial change, the agent should compile the document.

Default command:

```bash
pdflatex main.tex
pdflatex main.tex
```

If a project has a build script, the agent may use it instead, for example:

```bash
latexmk -pdf main.tex
```

or:

```bash
./build.sh
```

but only if the project already uses such a workflow.

The agent must check the compilation log.

The agent should not claim that compilation succeeded unless it actually ran the compilation command and confirmed success.

---

## 10. Reporting rule

After editing, the agent should report briefly:

```text
Changed:
- Added ...
- Updated ...
- Modified ...

Compilation:
- pdflatex completed successfully.
- Output PDF: main.pdf
```

If compilation fails, the agent should report:

```text
Changed:
- ...

Compilation:
- pdflatex failed.
- Error: ...
- Suggested fix: ...
```

If the cause is clear, the agent should fix it and recompile.

---

## 11. Mathematical writing style

The notes should be written in a clear academic style.

The style should be:

* precise,
* pedagogical,
* structured,
* readable,
* mathematically correct,
* suitable for students.

The agent should avoid vague statements such as:

```text
It is obvious that...
```

Prefer explanatory reasoning.

For example, instead of:

```text
Clearly, the function is continuous.
```

write:

```text
The function is continuous because it is a polynomial, and every polynomial is continuous on the whole real line.
```

Definitions, formulas, examples, and interpretations should be connected by explanatory text.

---

## 12. Mathematical notation

Mathematical notation should be written using real LaTeX mathematics.

Inline mathematics:

```latex
Let \( f : \mathbb{R} \to \mathbb{R} \) be a function.
```

Display mathematics:

```latex
\[
\lim_{x \to a} f(x) = L.
\]
```

Use standard notation consistently:

```latex
\mathbb{R}
\mathbb{N}
\mathbb{Z}
\varepsilon
\delta
\forall
\exists
\Rightarrow
\iff
```

Do not use fake mathematical notation in plain text when proper LaTeX notation is needed.

---

## 13. Visual style

The PDF should not look like raw, plain LaTeX output.

A moderate visual style is encouraged:

* colored definition boxes,
* example boxes,
* theorem boxes,
* remark boxes,
* clean tables,
* simple diagrams,
* highlighted summaries.

Color should improve readability, not decorate the document excessively.

Recommended packages include:

```latex
\usepackage{xcolor}
\usepackage{tcolorbox}
\usepackage{booktabs}
\usepackage{array}
\usepackage{tikz}
\usepackage{graphicx}
\usepackage{hyperref}
```

Tables should preferably use `booktabs`.

Avoid heavy table borders unless explicitly requested.

---

## 14. Naming conventions

Use English names for folders and files.

Use lowercase `snake_case`.

Good examples:

```text
linear_algebra
analytic_geometry
calculus
mathematical_preliminaries
one_dimensional_motion
systems_of_linear_equations
electric_charge_and_field
```

Avoid Polish folder names in the LaTeX project structure unless explicitly requested.

Avoid spaces in file names.

Avoid vague names such as:

```text
part1.tex
new_file.tex
notes.tex
stuff.tex
```

Prefer meaningful file names.

---

## 15. Course-specific writing expectations

### 15.1 Mathematics

The mathematics notes should be written as pure mathematical lecture notes.

They should emphasize:

* definitions,
* examples,
* theorem statements,
* proofs where appropriate,
* intuitive explanations,
* connections between concepts,
* precise notation.

Avoid unnecessary physics motivation unless explicitly requested.

---

### 15.2 Probabilistic Methods

The probabilistic methods notes should combine mathematical precision with interpretation.

They should emphasize:

* probability spaces,
* events,
* conditional probability,
* independence,
* random variables,
* distributions,
* expectation,
* variance,
* limit theorems,
* probabilistic modelling,
* examples and interpretations.

The notes should explain not only formulas, but also what the formulas mean.

---

### 15.3 Physics

The physics notes should combine physical meaning with mathematical formulation.

They should emphasize:

* physical interpretation,
* mathematical models,
* units,
* dimensional analysis,
* examples,
* diagrams,
* connection between formulas and phenomena.

Equations should not be presented as isolated formulas. They should be explained in terms of physical meaning.

---

## 16. Core rule

This repository is developed interactively.

The agent should work on small, meaningful LaTeX files rather than huge monolithic documents.

Every course has a `main.tex` file that assembles the document from chapters and smaller section files.

Most changes should be local, followed by compilation and PDF review.

Large document-wide changes are allowed only when the human author explicitly requests them.
