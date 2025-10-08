#!/usr/bin/env bash
# Skrypt konwertuje plik Markdown do PDF przy pomocy pandoc + LaTeX z marginesem 3cm.

set -euo pipefail

# Get the directory of the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$SCRIPT_DIR"

# Simple list of files to convert (new prefixed names)
FILES=(
	1_1_Algebra_en.md
	1_1_Algebra.md
	1_2_Algebra_en.md
	1_2_Algebra.md
	1_3_Algebra_en.md
	1_3_Algebra.md
	1_4_Algebra_en.md
	1_4_Algebra.md
	2_1_Geometria.md
	2_1_Geometry_en.md
	2_2_Geometria.md
	2_2_Geometry_en.md
	2_3_Geometria.md
	2_3_Geometry_en.md
	3_1_Calculus_en.md
	3_1_Rachunek.md
	3_2_Calculus_en.md
	3_2_Rachunek.md
	3_3_Calculus_en.md
	3_3_Rachunek.md
	3_4_Calculus_en.md
	3_4_Rachunek.md
	3_5_Calculus_en.md
	3_5_Rachunek.md
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
