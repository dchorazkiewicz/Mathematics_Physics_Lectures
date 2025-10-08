#!/usr/bin/env bash
# Skrypt konwertuje plik Markdown do PDF przy pomocy pandoc + LaTeX z marginesem 3cm.

set -euo pipefail

# Get the directory of the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$SCRIPT_DIR"

# Simple list of files to convert (new prefixed names)
FILES=(
	"code_en.md"
	"code_pl.md"
	"zadania_algebra_liniowa.md"
	"zadania_geometria_analityczna.md"
	"zadania_rachunek_rozniczkowy_calkowy.md"
)

MARGIN="3cm"

for INPUT in "${FILES[@]}"; do
	if [[ ! -f "$INPUT" ]]; then
		echo "Plik nie istnieje: $INPUT — pomijam." >&2
		continue
	fi
	OUTPUT="${INPUT%.md}.pdf"
	echo "Konwertuję: $INPUT -> $OUTPUT (margines=$MARGIN)"
	pandoc "$INPUT" -o "$OUTPUT" -V geometry:margin="$MARGIN" || {
		echo "Błąd konwersji $INPUT" >&2
		continue
	}
	echo "Gotowe: $OUTPUT"
done

echo "Wszystkie dostępne konwersje zakończone."
