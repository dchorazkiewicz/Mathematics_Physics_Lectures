# Instrukcja: Publikacja notatek jako strona WWW (MkDocs + GitHub Pages)

Niniejszy dokument to przewodnik, który pozwoli Wam samodzielnie zbudować i opublikować nowoczesną stronę z dokumentacją – dokładnie taką, jaką teraz widzicie. Wykorzystamy framework **MkDocs** z motywem **Material** oraz darmowy hosting **GitHub Pages**, aby w szybki i profesjonalny sposób udostępniać notatki z matematyki w internecie.

## Krok 1: Inicjalizacja Repozytorium (VS Code)

Wykorzystamy wbudowane funkcje Visual Studio Code do szybkiej publikacji projektu.

1.  Otwórz **Visual Studio Code** i wybierz `File > Open Folder...`, wskazując nowy, pusty katalog na dysku.
2.  Stwórz w tym folderze dowolny plik, np. pusty plik o nazwie `README.md` (Git wymaga przynajmniej jednego pliku, aby utworzyć repozytorium).
3.  Zapisz plik.
4.  Przejdź do zakładki **Source Control** (ikona grafu/drzewka na lewym pasku bocznym).
5.  Kliknij niebieski przycisk **Publish to GitHub**.
6.  Wybierz opcję publikacji jako **Public repository**.

*Po tej operacji Twój folder jest już połączony z GitHubem.*

## Krok 2: Automatyczna konfiguracja (Agent AI)

Teraz poprosimy Agenta AI w Visual Studio Code o przygotowanie środowiska Python i struktury MkDocs.

Skopiuj poniższy **Prompt** i wklej go do czatu z Agentem:

> **Prompt dla Agenta:**
>
> "Jesteś ekspertem od dokumentacji technicznej w Pythonie. Proszę o przygotowanie środowiska pod MkDocs w bieżącym folderze. Wykonaj następujące kroki:
>
> 1. Stwórz wirtualne środowisko Python (`.venv`) i podaj komendę do jego aktywacji.
> 2. Zainstaluj w tym środowisku pakiety: `mkdocs` oraz `mkdocs-material`.
> 3. Wygeneruj strukturę nowego projektu w głównym katalogu (`mkdocs new .`).
> 4. Nadpisz plik konfiguracyjny `mkdocs.yml`, ustawiając `site_name` na 'Notatki z Matematyki' oraz zmieniając motyw (`theme`) na `name: material`.
>
> Nie uruchamiaj serwera, tylko przygotuj pliki."

*Pamiętaj, aby po wykonaniu instrukcji przez Agenta wpisać w terminalu komendę aktywującą środowisko (tą, którą poda Agent).*

## Krok 3: Publikacja strony (Deployment)

Gdy projekt jest wstępnie gotowy, używamy jednej komendy, aby zbudować stronę i wysłać ją na serwer.

Wpisz w terminalu:

```bash
mkdocs gh-deploy
````

## Krok 4: Efekt końcowy

Nie musisz zgadywać adresu swojej strony ani ręcznie go konstruować. Po pomyślnym wykonaniu komendy `mkdocs gh-deploy`, spójrz na logi w terminalu.

Na samym końcu pojawi się bezpośredni link do Twojej opublikowanej strony. Wystarczy, że go klikniesz (w VS Code zazwyczaj z wciśniętym klawiszem `Ctrl` lub `Cmd`), aby zobaczyć swoje notatki w sieci.

## Krok 5: Jak pracować na co dzień? (Local Development)

Nie musisz wysyłać strony na serwer GitHub (`gh-deploy`) za każdym razem, gdy poprawisz literówkę lub dodasz jeden wzór. Efektywniejsza praca polega na podglądzie zmian lokalnie na Twoim komputerze.

**Instrukcja pracy bieżącej:**

1.  Wpisz w terminalu VS Code:
    ```bash
    mkdocs serve
    ```
2.  Otwórz w przeglądarce adres, który się wyświetli (zazwyczaj `http://127.0.0.1:8000/`).
3.  Edytuj pliki `.md` w folderze `docs`. Za każdym razem, gdy zapiszesz plik (`Ctrl+S`), strona w przeglądarce odświeży się automatycznie.
4.  Dopiero gdy skończysz pracę i będziesz zadowolony z efektu, zatrzymaj serwer (`Ctrl+C`) i wyślij zmiany "w świat" komendą z kroku 3:
    ```bash
    mkdocs gh-deploy
    ```

## Krok 6: Dodawanie treści i konfiguracja matematyki

Podobnie jak wcześniej, pliki z notatkami (Markdown) tworzymy w folderze `docs`. Aby nowa notatka była widoczna na pasku bocznym strony, musi zostać dodana do pliku konfiguracyjnego `mkdocs.yml`. Ponadto, musimy upewnić się, że MkDocs potrafi renderować wzory matematyczne (LaTeX).

Wykorzystajmy Agenta, aby stworzył przykładową notatkę, dodał ją do nawigacji i skonfigurował obsługę matematyki.

Skopiuj poniższy **Prompt** i wklej go do Agenta:

> **Prompt dla Agenta (Dodawanie treści i LaTeX):**
>
> "Proszę o rozbudowę projektu o nową notatkę i konfigurację matematyki.
>
> 1.  Stwórz w folderze `docs` plik o nazwie `pochodne.md`. Wpisz w nim krótką notatkę na temat pochodnych funkcji, zawierającą definicję oraz przykładowy wzór sformatowany w LaTeX (użyj dolarów).
> 2.  Zaktualizuj plik `mkdocs.yml`, dodając ten plik do sekcji nawigacji (`nav`) pod nazwą 'Pochodne'.
> 3.  **Bardzo ważne:** Zmodyfikuj `mkdocs.yml` tak, aby dodać pełną obsługę renderowania wzorów matematycznych. Skonfiguruj rozszerzenie `pymdownx.arithmatex` oraz dodaj niezbędne wpisy `extra_javascript` i `extra_css` (dla biblioteki MathJax lub KaTeX), aby wzory na stronie wyświetlały się poprawnie, a nie jako surowy kod."

**Co zrobić po wykonaniu zadania przez Agenta?**

1.  Uruchom serwer lokalny: `mkdocs serve`.
2.  Sprawdź w przeglądarce, czy nowa zakładka "Pochodne" się pojawiła i czy wzory matematyczne wyglądają ładnie (nie są surowym tekstem z dolarami).
3.  Jeśli wszystko działa, zatrzymaj serwer i opublikuj zmiany: `mkdocs gh-deploy`.
4.  Otwórz link z logów i sprawdź wersję publiczną.

## Krok 7: Interaktywne Symulacje (HTML + AI)

Twoja dokumentacja nie musi ograniczać się do statycznego tekstu. Nowoczesne czaty AI (takie jak **Gemini, Claude, czy ChatGPT**) potrafią generować działające symulacje fizyczne i matematyczne w języku HTML/JavaScript. Możesz je łatwo "wszczepić" do swojej strony z notatkami.

**Proces tworzenia symulacji:**

1.  **Generowanie kodu:** Udaj się do wybranego czata AI (np. Gemini lub Claude) i poproś o wygenerowanie symulacji.

      * *Przykładowy prompt do zewnętrznego AI:*
        > "Napisz dla mnie symulację rzutu ukośnego (lub wizualizację dodawania macierzy) jako pojedynczy plik HTML z wbudowanym CSS i JavaScript. Chcę, aby użytkownik mógł zmieniać parametry suwakami, a wynik był widoczny na wykresie/animacji."

2.  **Zapisywanie pliku:**

      * Skopiuj otrzymany kod HTML.
      * W folderze `docs` (tam gdzie masz pliki `.md`) stwórz nowy plik, np. `rzut_ukosny.html` i wklej do niego kod.

3.  **Integracja z nawigacją:**

      * Pliki HTML można dodawać do menu strony dokładnie tak samo, jak pliki Markdown.
      * Poproś Agenta w VS Code o dodanie tego pliku do nawigacji.

Skopiuj poniższy **Prompt** i wklej go do Agenta w VS Code:

> **Prompt dla Agenta (Integracja HTML):**
>
> "W folderze `docs` stworzyłem plik HTML z symulacją. Proszę, zaktualizuj plik `mkdocs.yml`:
>
> 1.  Znajdź sekcję `nav`.
> 2.  Dodaj do niej nową pozycję o nazwie 'Symulacja', która będzie wskazywać na ten plik HTML w folderze `docs`.
> 3.  Upewnij się, że struktura pliku konfiguracyjnego pozostanie poprawna."

**Weryfikacja:**
Uruchom `mkdocs serve`. W menu powinieneś zobaczyć nową pozycję "Symulacja". Po kliknięciu otworzy się Twoja interaktywna aplikacja stworzona przez AI. Gdy będziesz zadowolony, wypchnij zmiany na serwer (`mkdocs gh-deploy`).





















Jasne, oto zaktualizowany **Krok 2**, zawierający zmodyfikowany prompt dla Agenta, który zadba o higienę repozytorium (plik `.gitignore`).

---

## Krok 2: Automatyczna konfiguracja (Agent AI)

Teraz poprosimy Agenta AI w Visual Studio Code o przygotowanie środowiska Python, struktury MkDocs oraz zabezpieczenie repozytorium przed wysyłaniem zbędnych plików.

Skopiuj poniższy **Prompt** i wklej go do czatu z Agentem:

> **Prompt dla Agenta:**
>
> "Jesteś ekspertem od dokumentacji technicznej w Pythonie. Proszę o przygotowanie środowiska pod MkDocs w bieżącym folderze. Wykonaj następujące kroki:
>
> 1. Stwórz wirtualne środowisko Python (`.venv`) i podaj komendę do jego aktywacji.
> 2. Stwórz plik `.gitignore`, aby wykluczyć pliki tymczasowe z repozytorium. Dodaj do niego koniecznie:
>    - `.venv/` (środowisko wirtualne),
>    - `site/` (folder zbudowanej strony),
>    - `__pycache__/`.
> 3. Zainstaluj w tym środowisku pakiety: `mkdocs` oraz `mkdocs-material`.
> 4. Wygeneruj strukturę nowego projektu w głównym katalogu (`mkdocs new .`).
> 5. Nadpisz plik konfiguracyjny `mkdocs.yml`, ustawiając `site_name` na 'Notatki z Matematyki' oraz zmieniając motyw (`theme`) na `name: material`.
>
> Nie uruchamiaj serwera, tylko przygotuj pliki."

*Pamiętaj, aby po wykonaniu instrukcji przez Agenta wpisać w terminalu komendę aktywującą środowisko (tą, którą poda Agent).*