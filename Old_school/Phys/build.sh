#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

main_file="main.tex"
output_pdf="main.pdf"

if [[ ! -f "$main_file" ]]; then
    echo "Error: $main_file not found in $(pwd)" >&2
    exit 1
fi

pdflatex -interaction=nonstopmode -halt-on-error "$main_file"
pdflatex -interaction=nonstopmode -halt-on-error "$main_file"

find . \( \
    -name '*.aux' -o \
    -name '*.log' -o \
    -name '*.out' -o \
    -name '*.toc' -o \
    -name '*.fls' -o \
    -name '*.fdb_latexmk' -o \
    -name '*.synctex.gz' \
\) -type f -delete

echo "Built $output_pdf"
