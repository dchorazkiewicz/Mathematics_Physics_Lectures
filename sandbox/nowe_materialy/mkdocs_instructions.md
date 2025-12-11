# Instrukcja: Publikacja notatek jako strona WWW (MkDocs + GitHub Pages)

Zamiast generować statyczne pliki PDF, przechodzimy na nowoczesny standard dokumentacji technicznej. Wykorzystamy framework **MkDocs** z motywem **Material**, aby stworzyć responsywną stronę internetową z notatkami. Całość będzie hostowana na **GitHub Pages**.

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
> 1.  Stwórz wirtualne środowisko Python (`.venv`) i podaj komendę do jego aktywacji.
> 2.  Zainstaluj w tym środowisku pakiety: `mkdocs` oraz `mkdocs-material`.
> 3.  Wygeneruj strukturę nowego projektu w głównym katalogu (`mkdocs new .`).
> 4.  Nadpisz plik konfiguracyjny `mkdocs.yml`, ustawiając `site_name` na 'Notatki z Rachunku Różniczkowego' oraz zmieniając motyw (`theme`) na `name: material`.
>
> Nie uruchamiaj serwera, tylko przygotuj pliki."

*Pamiętaj, aby po wykonaniu instrukcji przez Agenta wpisać w terminalu komendę aktywującą środowisko (tą, którą poda Agent).*

## Krok 3: Publikacja strony (Deployment)

Gdy projekt jest gotowy, używamy jednej komendy, aby zbudować stronę i wysłać ją na serwer.

Wpisz w terminalu:

```bash
mkdocs gh-deploy
```

## Krok 4: Efekt końcowy

Twoja strona będzie dostępna pod adresem:

`https://<TWOJ_LOGIN>.github.io/<NAZWA_REPO>/`

### Wskazówki do edycji

  * Edytujesz pliki `.md` w katalogu `docs`.

  * Aby zaktualizować stronę po zmianach w notatkach, po prostu ponownie wpisz komendę `mkdocs gh-deploy`.

Czy chciałbyś, abym do sekcji z Agentem dodała instrukcję instalacji rozszerzeń do obsługi wzorów matematycznych?