# Organizacja pracy i konfiguracja środowiska dla notatek z Analizy Matematycznej

Jako przyszli inżynierowie, opanowanie narzędzi do dokumentowania procesu nauki jest równie ważne, co same obliczenia. Będziemy używać **Visual Studio Code (VSC)** do budowy profesjonalnej bazy wiedzy dla kursu Analizy Matematycznej.

Poniżej znajduje się plan organizacji materiałów do nauki, od prostych codziennych notatek po kompleksową dokumentację.

### Poziom 1: Podstawy – Markdown i struktura projektu

Zacznij tutaj, aby skupić się na nauce pojęć z Analizy, nie rozpraszając się skomplikowanym oprogramowaniem do formatowania.

**1. Organizacja plików**

Nie trzymaj wszystkich notatek z wykładów i ćwiczeń w jednym ogromnym pliku. Utrudnia to przeglądanie konkretnych zagadnień.

* Stwórz dedykowany **Folder Projektu** dla swoich notatek z Analizy.
* Twórz oddzielne pliki `.md` (Markdown) dla każdego tematu.
* Używaj jasnej konwencji nazewnictwa, aby ułatwić wyszukiwanie, na przykład:
    * `01_Ciagi_i_Szeregi.md`
    * `02_Rachunek_Rozniczkowy.md`
    * `03_Rachunek_Calkowy.md`

**2. Pisanie i matematyka**

VS Code pozwala pisać tekst i wzory matematyczne jednocześnie. Użyj funkcji podglądu (zazwyczaj `Ctrl+Shift+V`), aby widzieć renderowanie swoich notatek w czasie rzeczywistym. Do matematyki używamy składni LaTeX:

* **Wzory w tekście (inline):** Używaj pojedynczych znaków dolara dla wzorów wewnątrz zdania.
    Przykład: Pochodną sinusa jest $\frac{d}{dx}\sin(x) = \cos(x)$.

* **Wzory eksponowane (display):** Używaj podwójnych znaków dolara, aby wyśrodkować złożone wzory w nowej linii.

$$
\lim_{x \to 0} \frac{\ln(1+x)}{x} = 1
$$

Zapewnia to dokładność notatek i ich czytelność podczas powtórek.

### Poziom 2: Przenośność – Konwersja do PDF

Chociaż pliki `.md` są świetne do edycji, potrzebujesz stabilnego formatu, aby zabrać go na zajęcia lub udostępnić innym.

**Zdecydowanie zalecamy używanie Pandoc do tego zadania.**

* **Dlaczego Pandoc?** Jest to standard branżowy w konwersji dokumentów. W przeciwieństwie do prostych rozszerzeń typu "jedno kliknięcie", Pandoc daje pełną kontrolę nad wynikiem i poprawnie obsługuje złożoną matematykę w LaTeX.
* **Ostrzeżenie o "łatwej drodze":** Proste rozszerzenia VS Code (takie jak *Markdown PDF*) często polegają na prostej konwersji HTML i nie radzą sobie z renderowaniem zaawansowanych symboli matematycznych. Nie wybieraj łatwej ścieżki, jeśli skutkuje ona "rozsypanymi" wzorami.

**Twój Cel:** Profesjonalny PDF.
Masz dowolność w wyborze narzędzia, ale jeśli wybrana metoda nie wyrenderuje symboli matematycznych (np. pokazując surowy kod jak `$\int$` zamiast symbolu), dokument jest nieakceptowalny.

### Poziom 3: Zaawansowane – Przejście na LaTeX

Jeśli planujesz skompilować swoje notatki w większy, kompleksowy dokument (jak podsumowanie całego semestru) lub potrzebujesz bardziej złożonego formatowania, przejście na pełny **LaTeX** jest logicznym następnym krokiem.

* Zainstaluj dystrybucję TeX (taką jak TeX Live lub MiKTeX).
* Zainstaluj rozszerzenie **LaTeX Workshop** w VS Code.

To podejście daje lepsze narzędzia do zarządzania dużymi dokumentami i jest preferowaną ścieżką, gdy twoje notatki przekroczą możliwości prostego Markdowna.

---

### Oczekiwania wobec materiałów na zajęcia

Przychodząc na zajęcia lub konsultując temat, proszę trzymać się następujących standardów:

1.  **Format:** Miej notatki gotowe jako **PDF**. Nie polegaj na otwieraniu surowych plików `.md` ani pokazywaniu zrzutów ekranu.
2.  **Czytelność:** Upewnij się, że wszystkie symbole matematyczne są poprawnie wyrenderowane.
3.  **Organizacja:** Twój dokument powinien mieć wyraźne nagłówki odpowiadające omawianym zagadnieniom z Analizy.

---

### Twoje pierwsze zadanie: Konfiguracja cyfrowego notatnika

Na naszą następną sesję skonfigurujesz środowisko i stworzysz swój pierwszy zestaw notatek. To zadanie ma na celu upewnienie się, że swobodnie posługujesz się narzędziami, których będziemy używać przez cały kurs.

**1. Konfiguracja środowiska:**

* **Zainstaluj Visual Studio Code (VSC):** Jeśli jeszcze tego nie zrobiłeś, pobierz i zainstaluj VSC.
* **Zainstaluj rozszerzenia asystenta AI:** Usprawnij swoją pracę, instalując wtyczkę asystenta AI dla VSC (np. GitHub Copilot, Gemini itp.). Jest to wysoce zalecane.
* **Stwórz Projekt:**
    * Stwórz nowy folder projektu dla swoich notatek z analizy.
    * **Zainicjuj repozytorium Git** w tym folderze (`git init`).
    * (Opcjonalne, ale zalecane) Stwórz repozytorium na GitHubie i wypchnij (push) tam swój projekt. Lokalne repozytorium to wymóg minimalny.

**2. Twoja pierwsza notatka:**

* **Wybierz temat:** Wybierz dowolny temat z Analizy Matematycznej. Dobrym punktem wyjścia jest **definicja granicy ciągu**.
* **Stwórz plik Markdown:** Wewnątrz projektu stwórz nowy plik `.md` dla swojego tematu.
* **Napisz treść:** Twoja notatka powinna zawierać:
    * Formalną definicję wybranego pojęcia.
    * Kilka w pełni rozwiązanych przykładów, z każdym krokiem wyjaśnionym od początku do końca.
* **Wygeneruj PDF:** Skonwertuj swój plik `.md` na czysty dokument PDF. **Zalecamy skonfigurowanie Pandoc**, aby zapewnić wysoką jakość wyjściową. Jeśli używasz innych narzędzi, zweryfikuj, czy nie psują notacji matematycznej.

**3. Bądź gotów do prezentacji:**

* Na następnych zajęciach bądź przygotowany na **udostępnienie ekranu**.
* Powinieneś być w stanie zademonstrować swój sposób pracy (workflow): jak edytujesz plik Markdown, używasz podglądu VSC i prezentujesz finalny PDF. Celem jest pokazanie, że potrafisz efektywnie zarządzać swoimi notatkami.