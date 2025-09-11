pandoc --pdf-engine=pdflatex template_dokumentu.md -o template_dokumentu.pdf


# Proompts:

# Przeczytaj filofozię przedmiotu który musimy przygotować. Czy rozumiesz ją?
#
# ---
# W template_dokumentu.md masz przykładowy materiał jednej (pierwszej) z dwunastu sekcji (jest to jeden z czterech materiałów dotyczących algebry liniowej). Być może zawartość końcowo ulegle zmianie.
#
# Masz dawne pliki z dawnym wykładem (pliki qmd) a także dawną listę z dawną lista problemów.
#
# W kontekście zaprezentowanej filozofii przedmiotu: zaproponuj podział całego materiału (Linear Algebra, Calculus, Analytic Geometry) na 12 sekcji. Nie twórz jeszcze samych materiałów, tylko przedstaw planowany podział.
#
# Czy wszystko zrozumiałeś?
#
# ---

#!/bin/bash

# Skrypt do konwersji wszystkich plików Markdown z przewodników dla studentów do formatu PDF.
# Używa pandoc z silnikiem pdflatex.

# Definicja katalogów
SOURCE_DIR="pliki_dla_studentów"
OUTPUT_DIR="pliki_dla_studentów/pdf_generowane"

# Utworzenie katalogu wyjściowego, jeśli nie istnieje
mkdir -p "$OUTPUT_DIR"

echo "Rozpoczynanie konwersji plików .md do .pdf w katalogu $SOURCE_DIR..."

# Pętla przez wszystkie pliki .md w katalogu źródłowym
for md_file in "$SOURCE_DIR"/*.md; do
  if [ -f "$md_file" ]; then
    # Pobranie nazwy pliku bez rozszerzenia
    base_name=$(basename "$md_file" .md)
    # Zdefiniowanie ścieżki pliku wyjściowego PDF
    pdf_file="$OUTPUT_DIR/${base_name}.pdf"

    echo "Przetwarzanie: $md_file -> $pdf_file"
    # Uruchomienie pandoc z opcjami formatowania
    pandoc --pdf-engine=pdflatex "$md_file" -o "$pdf_file"
  fi
done

echo "Konwersja zakończona. Pliki PDF znajdują się w katalogu: $OUTPUT_DIR"
