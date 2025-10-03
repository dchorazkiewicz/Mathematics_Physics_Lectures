#!/usr/bin/env bash
# Skrypt konwertuje plik Markdown do PDF przy pomocy pandoc + LaTeX z marginesem 3cm.

set -euo pipefail

# Get the directory of the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$SCRIPT_DIR"

INPUT="algebra_liniowa_zadania.md"
OUTPUT="${INPUT%.md}.pdf"
MARGIN="3cm"

echo "Uruchamiam (margines=$MARGIN): pandoc $INPUT -o $OUTPUT -V geometry:margin=$MARGIN"
pandoc "$INPUT" -o "$OUTPUT" -V geometry:margin="$MARGIN"

echo "Gotowe: $OUTPUT"
