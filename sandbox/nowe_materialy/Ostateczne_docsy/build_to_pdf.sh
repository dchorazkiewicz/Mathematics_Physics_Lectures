#!/usr/bin/env bash
# Skrypt konwertuje podany plik Markdown do PDF przy pomocy pandoc + LaTeX
# Ustawia małe marginesy (domyślnie 1cm).

set -euo pipefail

INPUT=${1:-algebra_liniowa_zadania.md}
OUTPUT=${2:-${INPUT%.md}.pdf}
MARGIN=${3:-1cm}
#!/usr/bin/env bash
set -e
# Hardcodowany margines 3cm
INPUT=${1:-algebra_liniowa_zadania.md}
OUTPUT=${2:-${INPUT%.md}.pdf}
MARGIN=3cm

echo "Uruchamiam (margines=$MARGIN): pandoc $INPUT -o $OUTPUT -V geometry:margin=$MARGIN"
pandoc "$INPUT" -o "$OUTPUT" -V geometry:margin="$MARGIN"

echo "Gotowe: $OUTPUT"
  exit 2
