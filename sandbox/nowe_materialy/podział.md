# Oto propozycja podziału na 12 sekcji:

---

### **Część I: Algebra Liniowa (4 sekcje)**

**Cel:** Zbudowanie solidnych fundamentów w operacjach na macierzach i ich zastosowaniach do rozwiązywania układów równań, które są kluczowe w wielu dziedzinach informatyki i inżynierii.

* **Sekcja 1.1: Wprowadzenie do Macierzy i Podstawowe Operacje**
    * **Tematyka:** Definicja macierzy, jej wymiary i elementy. Rodzaje macierzy (kwadratowa, diagonalna, jednostkowa). Intuicyjne operacje: dodawanie, odejmowanie, mnożenie przez skalar. Wprowadzenie do kluczowej, mniej intuicyjnej operacji: mnożenia macierzy.
    * *(Ta sekcja jest już częściowo zdefiniowana w `template_dokumentu.md`)*

* **Sekcja 1.2: Wyznaczniki i ich Własności**
    * **Tematyka:** Wprowadzenie pojęcia wyznacznika jako fundamentalnej własności macierzy kwadratowej. Metody obliczania dla macierzy 2x2 i 3x3 (reguła Sarrusa). Rozwinięcie Laplace'a jako uniwersalna metoda dla większych macierzy. Własności wyznaczników i ich interpretacja geometryczna (pole, objętość).

* **Sekcja 1.3: Macierz Odwrotna i jej Zastosowania**
    * **Tematyka:** Koncepcja macierzy odwrotnej jako "odwrotności mnożenia". Warunek istnienia macierzy odwrotnej (niezerowy wyznacznik). Metody obliczania: za pomocą dopełnień algebraicznych (wzór) oraz metodą bezwyznacznikową (eliminacja Gaussa-Jordana).

* **Sekcja 1.4: Układy Równań Liniowych: Od Teorii do Praktyki**
    * **Tematyka:** Zapisywanie układów równań w formie macierzowej ($A \cdot x = b$). Przedstawienie i porównanie trzech głównych metod rozwiązywania: wzorów Cramera (zastosowanie wyznaczników), metody eliminacji Gaussa (operacje na wierszach) oraz metody macierzy odwrotnej ($x = A^{-1} \cdot b$).

---

### **Część II: Geometria Analityczna (4 sekcje)**

**Cel:** Przełożenie intuicyjnych pojęć geometrycznych na precyzyjny język algebry. Opanowanie wektorów, prostych i płaszczyzn jako narzędzi do opisu i manipulacji obiektami w przestrzeni 2D i 3D.

* **Sekcja 2.1: Przestrzeń Kartezjańska i Wektory: Podstawowe Pojęcia**
    * **Tematyka:** Budowa kartezjańskiego układu współrzędnych. Wprowadzenie wektorów jako narzędzia do opisu przesunięć i wielkości fizycznych. Działania na wektorach: dodawanie, odejmowanie, mnożenie przez skalar. Długość wektora i wektor jednostkowy (wersor).

* **Sekcja 2.2: Iloczyn Skalarny, Wektorowy i Mieszany: Geometria i Zastosowania**
    * **Tematyka:** Iloczyn skalarny jako miara "podobieństwa" kierunków i narzędzie do obliczania kątów oraz sprawdzania prostopadłości. Iloczyn wektorowy (tylko w 3D) do znajdowania wektora prostopadłego i obliczania pola. Iloczyn mieszany jako metoda na obliczanie objętości i sprawdzanie współpłaszczyznowości.

* **Sekcja 2.3: Analityczny Opis Prostej i Płaszczyzny**
    * **Tematyka:** Różne formy równania prostej na płaszczyźnie i w przestrzeni 3D (ogólna, kierunkowa, parametryczna). Równanie płaszczyzny w przestrzeni 3D. Wzajemne położenie prostych i płaszczyzn (równoległość, prostopadłość, punkty i krawędzie przecięcia).

* **Sekcja 2.4: Krzywe i Powierzchnie Stopnia Drugiego**
    * **Tematyka:** Wprowadzenie do krzywych stożkowych: analityczny opis okręgu, elipsy, hiperboli i paraboli na płaszczyźnie. Wprowadzenie do podstawowych powierzchni w przestrzeni 3D: sfery, elipsoidy, paraboloidy.

---

### **Część III: Rachunek Różniczkowy i Całkowy (4 sekcje)**

**Cel:** Zrozumienie dwóch filarów analizy matematycznej – pochodnej i całki. Opanowanie pochodnej jako narzędzia do badania tempa zmian i optymalizacji, a całki do obliczania sum i wielkości agregujących.

* **Sekcja 3.1: Funkcje i Granice: Fundamenty Analizy Matematycznej**
    * **Tematyka:** Formalne wprowadzenie pojęcia funkcji, jej dziedziny i zbioru wartości. Intuicyjne i formalne pojęcie granicy ciągu i funkcji. Ciągłość funkcji jako warunek "nieodrywania długopisu od kartki".

* **Sekcja 3.2: Pochodna Funkcji: Interpretacja i Techniki Obliczania**
    * **Tematyka:** Definicja pochodnej jako granicy ilorazu różnicowego. Interpretacja geometryczna (nachylenie stycznej) i fizyczna (prędkość chwilowa). Wzory na pochodne podstawowych funkcji oraz reguły różniczkowania (suma, iloczyn, iloraz, funkcja złożona – reguła łańcuchowa).

* **Sekcja 3.3: Zastosowania Pochodnych: Analiza Funkcji i Optymalizacja**
    * **Tematyka:** Wykorzystanie pierwszej pochodnej do znajdowania przedziałów monotoniczności i ekstremów lokalnych. Wykorzystanie drugiej pochodnej do badania wklęsłości i wypukłości funkcji. Problemy optymalizacyjne. Wprowadzenie do rozwinięcia w szereg Taylora jako lokalnej aproksymacji funkcji wielomianem.

* **Sekcja 3.4: Całka: Od Pola pod Krzywą do Równań Różniczkowych**
    * **Tematyka:** Całka oznaczona jako granica sum Riemanna (pole pod wykresem). Całka nieoznaczona (funkcja pierwotna). Fundamentalne twierdzenie rachunku całkowego łączące całkę z pochodną. Podstawowe techniki całkowania. Wprowadzenie do równań różniczkowych jako modeli zjawisk dynamicznych.