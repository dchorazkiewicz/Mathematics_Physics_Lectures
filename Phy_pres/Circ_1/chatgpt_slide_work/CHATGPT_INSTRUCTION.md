# ChatGPT Instructions for Circuit Lecture Slide Images

You are helping me generate images for a university-level physics lecture presentation in English.

## What I Have in My Repository

I have a prepared English lecture plan about electric current and basic circuit analysis.

In my repository, the lecture has been split into separate Markdown files, one file per slide:

* `slide_01.md`
* `slide_02.md`
* `slide_03.md`
* ...
* `slide_24.md`

Each slide file contains the source description for one slide:

* slide title
* teaching goal
* layout
* visual details
* labels, arrows, colors, symbols, and formulas
* what should not be drawn

The slide list already exists. Do not create a new slide list. Do not ask me to define the lecture again.

## What I Will Do in This Chat

I will paste one slide Markdown file at a time.

For example, I will paste the content of `slide_01.md`. After that, I may paste `slide_02.md`, then `slide_03.md`, and so on up to `slide_24.md`.

Your task is to generate one slide image from each pasted Markdown file.

After you finish one slide, wait for me to paste the next slide.

## Your Workflow for Each Pasted Slide

When I paste a slide Markdown file:

1. Treat the pasted Markdown as the complete source brief for one slide.
2. Do not change the slide topic.
3. Do not invent a new slide.
4. Do not summarize the whole lecture.
5. First internally convert the pasted description into a precise visual plan.
6. Then generate the slide image from that plan.
7. If you cannot generate an image directly, output one final image-generation prompt instead.
8. After finishing the slide, reply:

`READY FOR NEXT SLIDE`

Then wait for my next pasted slide Markdown file.

## What the Internal Visual Plan Must Control

For every slide, the visual plan must define:

* what appears at the top of the slide
* what appears in the center
* what appears on the left side
* what appears on the right side
* what appears at the bottom
* all arrows and their directions
* all colors
* all symbols and labels
* all formulas and formula placement
* what must not be drawn

The goal is to leave the image generator as little freedom of interpretation as possible.

## Global Visual Style

Use this style for every slide:

* 16:9 widescreen format
* white or very light warm academic background
* clean vector-like educational infographic style
* English language only
* minimal text
* readable labels
* simple sans-serif font
* slide title in the upper left
* one main idea per slide
* one clear central illustration, diagram, or circuit
* consistent line thickness
* no decorative clutter
* no dense paragraphs
* no unnecessary realism

## Color Language

Use colors consistently:

* blue: electrons, electric field, voltage
* red or orange: current, energy, heat
* gray: metal, wires, lattice, circuit elements
* green: correct results and important consequences

## Circuit Diagram Rules

For all circuit slides:

* draw wires thick and readable
* use one resistor style consistently
* draw batteries with the standard long-line and short-line symbol
* mark currents with arrows and labels such as `I`, `I_1`, `I_2`
* mark voltages with arrows or clear `+` and `-` signs
* mark nodes as black dots
* for mesh analysis, draw each mesh current as a clear circular arrow
* keep labels legible
* avoid overcrowding

## Hard Constraints

Do not:

* invent new slides
* ask me to define the presentation from scratch
* add extra explanatory text inside the image
* add decorative backgrounds
* add unrelated physics symbols
* produce multiple alternative concepts unless I explicitly ask
* change the language from English

## First Response

After I paste this instruction message, reply only:

`READY FOR SLIDE 01`

Then wait for me to paste the first slide Markdown file.
