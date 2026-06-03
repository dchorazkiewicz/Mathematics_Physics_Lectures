# Old_school — Initial LaTeX Project Setup Instructions

## 1. Purpose

This document gives concrete instructions for creating the initial LaTeX templates inside the `Old_school` directory.

It is not a general style guide.
It is an implementation task for an AI agent.

The goal is to create clean starting LaTeX projects for three lecture-note areas:

1. Mathematics
2. Probabilistic Methods
3. Physics

Each project should compile successfully with `pdflatex`.

The initial files may contain only short placeholder content.
Do not generate full lecture notes at this stage.

---

## 2. General setup rules

For each project, create a modular LaTeX structure.

Each project must contain:

```text
main.tex
preamble.tex
macros.tex
styles.tex
chapters/
figures/
output/
```

The `main.tex` file should assemble the document.

The `preamble.tex` file should contain packages and document-level setup.

The `macros.tex` file should contain common mathematical macros.

The `styles.tex` file should contain theorem styles, colored boxes, and visual formatting.

The `chapters/` directory should contain chapter folders or chapter files.

The `figures/` directory should be reserved for figures.

The `output/` directory should be reserved for generated PDFs or copied build outputs if needed.

Use English folder and file names.

Use lowercase `snake_case`.

Compile each project after creating it.

---

## 3. LaTeX document settings

Each `main.tex` should use:

```latex
\documentclass[11pt,a4paper]{report}
```

Each project should use 2.5 cm margins through `geometry`:

```latex
\usepackage[a4paper,margin=2.5cm]{geometry}
```

The compilation engine is `pdflatex`.

Run:

```bash
pdflatex main.tex
pdflatex main.tex
```

The PDF should compile without errors.

Warnings are acceptable only if they do not prevent PDF generation, but they should be reported.

---

## 4. Shared preamble template

Create a `preamble.tex` file in each project with content similar to:

```latex
% Page layout
\usepackage[a4paper,margin=2.5cm]{geometry}

% Fonts and encoding
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}

% Mathematics
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{mathtools}

% Tables and graphics
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{array}

% Colors and boxes
\usepackage{xcolor}
\usepackage[most]{tcolorbox}

% Diagrams
\usepackage{tikz}

% Hyperlinks
\usepackage{hyperref}

\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    urlcolor=blue,
    citecolor=blue
}
```

---

## 5. Shared macros template

Create a `macros.tex` file in each project with content similar to:

```latex
% Number systems
\newcommand{\R}{\mathbb{R}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\C}{\mathbb{C}}

% Common operators
\newcommand{\dd}{\,\mathrm{d}}
\newcommand{\e}{\mathrm{e}}

% Vectors
\newcommand{\vect}[1]{\mathbf{#1}}

% Probability
\newcommand{\Prob}{\mathbb{P}}
\newcommand{\E}{\mathbb{E}}
\newcommand{\Var}{\operatorname{Var}}
```

Even if not all macros are immediately used in every project, this gives a consistent starting point.

---

## 6. Shared styles template

Create a `styles.tex` file in each project with content similar to:

```latex
% Theorem-like environments
\newtheorem{theorem}{Theorem}[chapter]
\newtheorem{proposition}{Proposition}[chapter]
\newtheorem{lemma}{Lemma}[chapter]
\newtheorem{corollary}{Corollary}[chapter]

\theoremstyle{definition}
\newtheorem{definition}{Definition}[chapter]
\newtheorem{example}{Example}[chapter]

\theoremstyle{remark}
\newtheorem{remark}{Remark}[chapter]

% Colored boxes
\newtcolorbox{definitionbox}{
    breakable,
    colback=blue!3,
    colframe=blue!60!black,
    title=Definition,
    fonttitle=\bfseries
}

\newtcolorbox{examplebox}{
    breakable,
    colback=green!3,
    colframe=green!50!black,
    title=Example,
    fonttitle=\bfseries
}

\newtcolorbox{remarkbox}{
    breakable,
    colback=yellow!8,
    colframe=yellow!50!black,
    title=Remark,
    fonttitle=\bfseries
}

\newtcolorbox{summarybox}{
    breakable,
    colback=gray!5,
    colframe=gray!60!black,
    title=Summary,
    fonttitle=\bfseries
}
```

The visual style is only a starting point. It may be changed later.

---

## 7. Mathematics initial project

Target folder:

```text
Old_school/Math/Math
```

Create the following structure:

```text
Old_school/Math/Math/
├── main.tex
├── preamble.tex
├── macros.tex
├── styles.tex
├── chapters/
│   ├── linear_algebra/
│   │   ├── chapter.tex
│   │   ├── vectors.tex
│   │   ├── matrices.tex
│   │   └── systems_of_linear_equations.tex
│   ├── analytic_geometry/
│   │   ├── chapter.tex
│   │   ├── coordinates.tex
│   │   ├── lines.tex
│   │   └── planes.tex
│   └── calculus/
│       ├── chapter.tex
│       ├── functions.tex
│       ├── limits.tex
│       ├── continuity.tex
│       └── derivatives.tex
├── figures/
└── output/
```

The three initial topic blocks are:

1. **Linear Algebra**
2. **Analytic Geometry**
3. **Calculus**

Use the word **Calculus** for the general block covering functions, limits, continuity, derivatives, integrals, and related topics.

The initial `main.tex` should include:

```latex
\documentclass[11pt,a4paper]{report}

\input{preamble}
\input{macros}
\input{styles}

\title{Mathematics Lecture Notes}
\author{}
\date{}

\begin{document}

\maketitle
\tableofcontents

\include{chapters/linear_algebra/chapter}
\include{chapters/analytic_geometry/chapter}
\include{chapters/calculus/chapter}

\end{document}
```

The file `chapters/linear_algebra/chapter.tex` should contain:

```latex
\chapter{Linear Algebra}

This chapter introduces the basic objects and methods of linear algebra.

\input{chapters/linear_algebra/vectors}
\input{chapters/linear_algebra/matrices}
\input{chapters/linear_algebra/systems_of_linear_equations}
```

The file `chapters/linear_algebra/vectors.tex` should contain:

```latex
\section{Vectors}

This section will introduce vectors and their basic operations.
```

The file `chapters/linear_algebra/matrices.tex` should contain:

```latex
\section{Matrices}

This section will introduce matrices and basic matrix operations.
```

The file `chapters/linear_algebra/systems_of_linear_equations.tex` should contain:

```latex
\section{Systems of Linear Equations}

This section will introduce systems of linear equations and their connection with matrices.
```

The file `chapters/analytic_geometry/chapter.tex` should contain:

```latex
\chapter{Analytic Geometry}

This chapter introduces geometric objects described using coordinates and algebraic equations.

\input{chapters/analytic_geometry/coordinates}
\input{chapters/analytic_geometry/lines}
\input{chapters/analytic_geometry/planes}
```

The file `chapters/analytic_geometry/coordinates.tex` should contain:

```latex
\section{Coordinates}

This section will introduce coordinate systems and the representation of points.
```

The file `chapters/analytic_geometry/lines.tex` should contain:

```latex
\section{Lines}

This section will introduce equations of lines and their geometric interpretation.
```

The file `chapters/analytic_geometry/planes.tex` should contain:

```latex
\section{Planes}

This section will introduce equations of planes in three-dimensional space.
```

The file `chapters/calculus/chapter.tex` should contain:

```latex
\chapter{Calculus}

This chapter introduces functions, limits, continuity, and derivatives.

\input{chapters/calculus/functions}
\input{chapters/calculus/limits}
\input{chapters/calculus/continuity}
\input{chapters/calculus/derivatives}
```

The file `chapters/calculus/functions.tex` should contain:

```latex
\section{Functions}

This section will introduce functions as mathematical objects describing dependence between quantities.
```

The file `chapters/calculus/limits.tex` should contain:

```latex
\section{Limits}

This section will introduce the concept of a limit.
```

The file `chapters/calculus/continuity.tex` should contain:

```latex
\section{Continuity}

This section will introduce continuity and its basic interpretation.
```

The file `chapters/calculus/derivatives.tex` should contain:

```latex
\section{Derivatives}

This section will introduce derivatives as rates of change.
```

---

## 8. Probabilistic Methods initial project

Target folder:

```text
Old_school/Math/Prob_meth
```

Create the following structure:

```text
Old_school/Math/Prob_meth/
├── main.tex
├── preamble.tex
├── macros.tex
├── styles.tex
├── chapters/
│   └── chapter_01_introduction.tex
├── figures/
└── output/
```

At the initial stage, do not create a detailed topic split.

The initial `main.tex` should include:

```latex
\documentclass[11pt,a4paper]{report}

\input{preamble}
\input{macros}
\input{styles}

\title{Probabilistic Methods Lecture Notes}
\author{}
\date{}

\begin{document}

\maketitle
\tableofcontents

\include{chapters/chapter_01_introduction}

\end{document}
```

The file `chapters/chapter_01_introduction.tex` should contain:

```latex
\chapter{Introduction to Probabilistic Methods}

This chapter introduces the role of probability in mathematical modelling, uncertainty, and data-informed reasoning.

The detailed structure of this course will be developed incrementally.
```

Later, the project may grow into folders such as:

```text
probability_spaces
conditional_probability
random_variables
distributions
expectation_and_variance
limit_theorems
```

but these should not be created now unless explicitly requested.

---

## 9. Physics initial project

Target folder:

```text
Old_school/Phys
```

Create the following structure:

```text
Old_school/Phys/
├── main.tex
├── preamble.tex
├── macros.tex
├── styles.tex
├── chapters/
│   ├── mathematical_preliminaries/
│   │   ├── chapter.tex
│   │   ├── vectors_and_coordinates.tex
│   │   ├── functions_and_graphs.tex
│   │   ├── derivatives_in_physics.tex
│   │   └── units_and_dimensions.tex
│   ├── kinematics/
│   │   ├── chapter.tex
│   │   ├── position_velocity_acceleration.tex
│   │   └── one_dimensional_motion.tex
│   ├── dynamics/
│   │   ├── chapter.tex
│   │   ├── force_and_mass.tex
│   │   └── newtons_laws.tex
│   └── electromagnetism/
│       ├── chapter.tex
│       ├── electric_charge_and_field.tex
│       └── electric_potential.tex
├── figures/
└── output/
```

The initial physics topic blocks are:

1. **Mathematical Preliminaries**
2. **Kinematics**
3. **Dynamics**
4. **Electromagnetism**

Use **Mathematical Preliminaries** for the introductory mathematical chapter.
This chapter should show which mathematical tools are needed in physics and how they are interpreted physically.

The initial `main.tex` should include:

```latex
\documentclass[11pt,a4paper]{report}

\input{preamble}
\input{macros}
\input{styles}

\title{Physics Lecture Notes}
\author{}
\date{}

\begin{document}

\maketitle
\tableofcontents

\include{chapters/mathematical_preliminaries/chapter}
\include{chapters/kinematics/chapter}
\include{chapters/dynamics/chapter}
\include{chapters/electromagnetism/chapter}

\end{document}
```

The file `chapters/mathematical_preliminaries/chapter.tex` should contain:

```latex
\chapter{Mathematical Preliminaries}

This chapter introduces the mathematical tools used throughout the physics lecture notes.

The goal is not to replace a mathematics course, but to show how mathematical concepts are used to describe physical quantities and physical laws.

\input{chapters/mathematical_preliminaries/vectors_and_coordinates}
\input{chapters/mathematical_preliminaries/functions_and_graphs}
\input{chapters/mathematical_preliminaries/derivatives_in_physics}
\input{chapters/mathematical_preliminaries/units_and_dimensions}
```

The file `chapters/mathematical_preliminaries/vectors_and_coordinates.tex` should contain:

```latex
\section{Vectors and Coordinates}

This section will introduce vectors, coordinate systems, and their role in describing physical quantities.
```

The file `chapters/mathematical_preliminaries/functions_and_graphs.tex` should contain:

```latex
\section{Functions and Graphs}

This section will introduce functions and graphs as tools for representing physical relationships.
```

The file `chapters/mathematical_preliminaries/derivatives_in_physics.tex` should contain:

```latex
\section{Derivatives in Physics}

This section will introduce derivatives as rates of change in physical contexts.
```

The file `chapters/mathematical_preliminaries/units_and_dimensions.tex` should contain:

```latex
\section{Units and Dimensions}

This section will introduce units, dimensions, and dimensional consistency.
```

The file `chapters/kinematics/chapter.tex` should contain:

```latex
\chapter{Kinematics}

This chapter introduces the mathematical description of motion.

\input{chapters/kinematics/position_velocity_acceleration}
\input{chapters/kinematics/one_dimensional_motion}
```

The file `chapters/kinematics/position_velocity_acceleration.tex` should contain:

```latex
\section{Position, Velocity, and Acceleration}

This section will introduce position, velocity, and acceleration as basic quantities used to describe motion.
```

The file `chapters/kinematics/one_dimensional_motion.tex` should contain:

```latex
\section{One-Dimensional Motion}

This section will introduce motion along a straight line.
```

The file `chapters/dynamics/chapter.tex` should contain:

```latex
\chapter{Dynamics}

This chapter introduces the relation between motion and its causes.

\input{chapters/dynamics/force_and_mass}
\input{chapters/dynamics/newtons_laws}
```

The file `chapters/dynamics/force_and_mass.tex` should contain:

```latex
\section{Force and Mass}

This section will introduce force and mass as basic concepts in dynamics.
```

The file `chapters/dynamics/newtons_laws.tex` should contain:

```latex
\section{Newton's Laws}

This section will introduce Newton's laws of motion.
```

The file `chapters/electromagnetism/chapter.tex` should contain:

```latex
\chapter{Electromagnetism}

This chapter introduces the basic concepts of electric and magnetic phenomena.

\input{chapters/electromagnetism/electric_charge_and_field}
\input{chapters/electromagnetism/electric_potential}
```

The file `chapters/electromagnetism/electric_charge_and_field.tex` should contain:

```latex
\section{Electric Charge and Electric Field}

This section will introduce electric charge and the electric field.
```

The file `chapters/electromagnetism/electric_potential.tex` should contain:

```latex
\section{Electric Potential}

This section will introduce electric potential and its relation to the electric field.
```

---

## 10. Compilation task

After creating the files, compile each project separately.

### Mathematics

```bash
cd Old_school/Math/Math
pdflatex main.tex
pdflatex main.tex
```

Expected output:

```text
main.pdf
```

### Probabilistic Methods

```bash
cd Old_school/Math/Prob_meth
pdflatex main.tex
pdflatex main.tex
```

Expected output:

```text
main.pdf
```

### Physics

```bash
cd Old_school/Phys
pdflatex main.tex
pdflatex main.tex
```

Expected output:

```text
main.pdf
```

---

## 11. Final report required from the agent

After completing the setup, report:

```text
Created:
- Old_school/Math/Math initial LaTeX project
- Old_school/Math/Prob_meth initial LaTeX project
- Old_school/Phys initial LaTeX project

Compilation:
- Mathematics: success/failure
- Probabilistic Methods: success/failure
- Physics: success/failure

Output PDFs:
- Old_school/Math/Math/main.pdf
- Old_school/Math/Prob_meth/main.pdf
- Old_school/Phys/main.pdf
```

If any compilation fails, report the exact error and fix it if possible.

Do not claim that a PDF was created unless compilation actually succeeded.
