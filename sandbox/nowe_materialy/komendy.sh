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
    pandoc -V geometry:"margin=3cm" --pdf-engine=pdflatex "$md_file" -o "$pdf_file"
  fi
done

echo "Konwersja zakończona. Pliki PDF znajdują się w katalogu: $OUTPUT_DIR"
