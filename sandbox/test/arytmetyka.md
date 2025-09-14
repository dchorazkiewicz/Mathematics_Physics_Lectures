# Podstawy Arytmetyki i Systemów Pozycyjnych

## Spis Treści

1.  [Aksjomaty Peano](#aksjomaty-peano)
2.  [Definicje dodawania, mnożenia i potęgowania](#definicje-dodawania-mnożenia-i-potęgowania)
3.  [Dwie konstrukcje zbioru liczb naturalnych](#dwie-konstrukcje-zbioru-liczb-naturalnych)
4.  [Systemy zapisu liczb, w tym system pozycyjny](#systemy-zapisu-liczb-w-tym-system-pozycyjny)

---

## Aksjomaty Peano

Zaczniemy od samych fundamentów, czyli od tego, czym właściwie są liczby naturalne. Pod koniec XIX wieku włoski matematyk Giuseppe Peano zaproponował zestaw aksjomatów (założeń), które w precyzyjny sposób definiują zbiór liczb naturalnych. Dzięki nim możemy w sposób formalny budować całą arytmetykę.

Oto one:

Aksjomaty Peano definiują zbiór liczb naturalnych, oznaczany jako $\mathbb{N}$. Wprowadzają one pojęcie "następnika" liczby, co jest intuicyjnym odpowiednikiem dodania jedynki.

1.  **Istnieje liczba naturalna, którą nazywamy 0.**
    *   $0 \in \mathbb{N}$
    *   To jest nasz punkt startowy. W niektórych wersjach aksjomatów zaczyna się od 1, ale my przyjmiemy wersję z 0.

2.  **Każda liczba naturalna *n* ma swojego następcę, oznaczanego jako S(*n*).**
    *   Następnik S(*n*) również jest liczbą naturalną.
    *   Możemy myśleć o $S(n)$ jako o $n + 1$.

3.  **Liczba 0 nie jest następnikiem żadnej liczby naturalnej.**
    *   Nie istnieje taka liczba $n \in \mathbb{N}$, dla której $S(n) = 0$.
    *   To gwarantuje, że 0 jest "pierwszą" liczbą.

4.  **Różne liczby naturalne mają różne następniki.**
    *   Jeżeli $n \neq m$, to $S(n) \neq S(m)$.
    *   To zapewnia, że idąc "w górę" po liczbach, nigdy się nie zapętlimy ani nie spotkamy dwóch gałęzi prowadzących do tego samego miejsca.

5.  **Aksjomat indukcji matematycznej:** Jeżeli mamy zbiór *K*, który zawiera 0 i dla każdej liczby naturalnej *n* należącej do *K*, jej następnik S(*n*) również należy do *K*, to zbiór *K* zawiera wszystkie liczby naturalne.
    *   To jest najpotężniejszy z aksjomatów. Pozwala on na dowodzenie twierdzeń dla wszystkich liczb naturalnych. Jeśli potrafimy pokazać, że jakaś własność jest prawdziwa dla 0, oraz że jeśli jest prawdziwa dla $n$, to jest też prawdziwa dla $n+1$, to możemy być pewni, że jest prawdziwa dla wszystkich liczb naturalnych.

Te pięć prostych zasad stanowi solidny fundament, na którym zbudujemy operacje dodawania, mnożenia i potęgowania.

---

## Definicje dodawania, mnożenia i potęgowania

Mając solidny fundament w postaci Aksjomatów Peano, możemy teraz zdefiniować podstawowe operacje arytmetyczne. Zrobimy to w sposób rekurencyjny, czyli odwołując się do poprzednich kroków. Zauważ, jak każda kolejna definicja opiera się na poprzedniej.

### Dodawanie ($+$)

Dodawanie liczby $m$ do liczby $n$ (czyli $n + m$) definiujemy za pomocą dwóch reguł:

1.  **Warunek bazowy (dodawanie zera):** Dodanie 0 do dowolnej liczby naturalnej *n* pozostawia tę liczbę bez zmian.
    *   $n + 0 = n$

2.  **Krok rekurencyjny (dodawanie następnika):** Dodanie następnika liczby $m$ (czyli $S(m)$) do liczby $n$ jest tym samym, co wzięcie następnika sumy $n$ i $m$.
    *   $n + S(m) = S(n + m)$

**Przykład: Jak obliczyć 2 + 2?**

Pamiętajmy, że $1 = S(0)$ i $2 = S(1) = S(S(0))$.

$2 + 2 = 2 + S(1)$

*   Zgodnie z regułą 2: $2 + S(1) = S(2 + 1)$


Teraz musimy obliczyć $2 + 1$:
$2 + 1 = 2 + S(0)$

*   Zgodnie z regułą 2: $2 + S(0) = S(2 + 0)$
*   Zgodnie z regułą 1: $2 + 0 = 2$
*   Więc $2 + 1 = S(2) = 3$

Wracając do naszego pierwotnego problemu:
$2 + 2 = S(2 + 1) = S(3) = 4$

W ten sposób, używając tylko pojęcia następnika, zdefiniowaliśmy dodawanie!

### Mnożenie ($\cdot$)

Mnożenie budujemy na dodawaniu. Definiujemy je również za pomocą dwóch reguł:

1.  **Warunek bazowy (mnożenie przez zero):** Mnożenie dowolnej liczby naturalnej *n* przez 0 daje w wyniku 0.
    *   $n \cdot 0 = 0$

2.  **Krok rekurencyjny (mnożenie przez następnika):** Mnożenie liczby $n$ przez następnika liczby $m$ (czyli $S(m)$) jest równe iloczynowi $n$ i $m$, powiększonemu o $n$.
    *   $n \cdot S(m) = (n \cdot m) + n$

**Przykład: Jak obliczyć $3 \cdot 2$?**

$3 \cdot 2 = 3 \cdot S(1)$

*   Zgodnie z regułą 2: $3 \cdot S(1) = (3 \cdot 1) + 3$


Teraz musimy obliczyć $3 \cdot 1$:
$3 \cdot 1 = 3 \cdot S(0)$

*   Zgodnie z regułą 2: $3 \cdot S(0) = (3 \cdot 0) + 3$
*   Zgodnie z regułą 1: $3 \cdot 0 = 0$
*   Więc $3 \cdot 1 = 0 + 3 = 3$

Wracając do naszego pierwotnego problemu:
$3 \cdot 2 = (3 \cdot 1) + 3 = 3 + 3 = 6$ (korzystając z wcześniej zdefiniowanego dodawania).

### Potęgowanie ($\hat{}$)

Potęgowanie budujemy na mnożeniu.

1.  **Warunek bazowy (potęga zerowa):** Dowolna liczba naturalna $n$ (z wyjątkiem 0, choć to kwestia umowy) podniesiona do potęgi 0 daje 1. Pamiętajmy, że $1 = S(0)$.

    *   $n^0 = S(0)$

2.  **Krok rekurencyjny (potęga następnika):** Podniesienie liczby $n$ do potęgi $S(m)$ jest równe wynikowi $n^m$ pomnożonemu przez $n$.

    *   $n^{S(m)} = (n^m) \cdot n$

**Przykład: Jak obliczyć $2^3$?**

Pamiętajmy, że $1=S(0)$, $2=S(1)$, $3=S(2)$.

$2^3 = 2^{S(2)}$

*   Zgodnie z regułą 2: $2^{S(2)} = (2^2) \cdot 2$

Teraz musimy obliczyć $2^2$:
$2^2 = 2^{S(1)}$

*   Zgodnie z regułą 2: $2^{S(1)} = (2^1) \cdot 2$
*   Musimy obliczyć $2^1 = 2^{S(0)} = (2^0) \cdot 2 = 1 \cdot 2 = 2$.
*   Więc $2^2 = 2 \cdot 2 = 4$.

Wracając do naszego pierwotnego problemu:

$$2^3 = (2^2) \cdot 2 = 4 \cdot 2 = 8$$.

W ten sposób, zaczynając od pięciu prostych aksjomatów, zdefiniowaliśmy rekurencyjnie trzy podstawowe działania arytmetyczne. To pokazuje potęgę formalizmu matematycznego!

---

## Dwie konstrukcje zbioru liczb naturalnych

Aksjomaty Peano w genialny sposób opisują *właściwości* liczb naturalnych i jak powinny się one zachowywać. Nie mówią nam jednak, czym te liczby *są* w sensie fundamentalnym. Czy to obiekty fizyczne? Idee w naszych umysłach?

Na początku XX wieku matematycy, uzbrojeni w nowo powstałą teorię mnogości, pokazali, że liczby naturalne można *skonstruować* z najbardziej podstawowego obiektu matematycznego, jakim jest **zbiór**. Pokażemy dwie takie konstrukcje.

### Konstrukcja von Neumanna (oparta na liczbach porządkowych)

John von Neumann zaproponował niezwykle elegancką i dziś powszechnie przyjmowaną konstrukcję, w której każda liczba naturalna jest zbiorem wszystkich liczb ją poprzedzających.

Zaczynamy od jedynego zbioru, którego istnienie możemy założyć bez dodatkowych elementów – **zbioru pustego $\emptyset$**.

*   **0** definiujemy jako zbiór pusty: $0 := \emptyset$
*   **1** definiujemy jako zbiór zawierający 0: $1 := \{0\} = \{\emptyset\}$
*   **2** definiujemy jako zbiór zawierający 0 i 1: $2 := \{0, 1\} = \{\emptyset, \{\emptyset\}\}$
*   **3** definiujemy jako zbiór zawierający 0, 1 i 2: $3 := \{0, 1, 2\} = \{\emptyset, \{\emptyset\}, \{\emptyset, \{\emptyset\}\}\}$

Widzisz wzorzec? Każda kolejna liczba jest zbiorem liczb ją poprzedzających. Formalnie, następnik liczby $n$ to unia (suma) zbioru $n$ i zbioru zawierającego $n$:

$$ S(n) := n \cup \{n\} $$

Ta konstrukcja w piękny sposób spełnia aksjomaty Peano. Co więcej, wprowadza ona naturalną relację porządku: liczba $m$ jest mniejsza od $n$ ($m < n$) wtedy i tylko wtedy, gdy $m$ jest elementem zbioru $n$ ($m \in n$). Na przykład $2 < 3$, ponieważ $2 \in \{0, 1, 2\}$.

Ta metoda jest częścią szerszej teorii liczb porządkowych i stanowi standard w aksjomatycznej teorii mnogości.

### Konstrukcja Zermelo (pomysł Twojego syna!)

Druga, historycznie wcześniejsza konstrukcja, została zaproponowana przez Ernsta Zermelo. Jest ona być może jeszcze bardziej minimalistyczna i bardzo przypomina to, co zasugerowałeś!

Zasada jest prosta: każda kolejna liczba jest zbiorem jednoelementowym (singletonem) zawierającym swojego poprzednika.

*   **0** definiujemy jako zbiór pusty: $0 := \emptyset$
*   **1** definiujemy jako zbiór zawierający 0: $1 := \{0\} = \{\emptyset\}$
*   **2** definiujemy jako zbiór zawierający 1: $2 := \{1\} = \{\{\emptyset\}\}$
*   **3** definiujemy jako zbiór zawierający 2: $3 := \{2\} = \{\{\{\emptyset\}\}\}$

Ogólna zasada tworzenia następnika jest więc niezwykle prosta:

$$ S(n) := \{n\} $$

Ta konstrukcja również spełnia aksjomaty Peano. Jest bardzo elegancka w swojej prostocie, jednak ma pewną wadę w porównaniu do konstrukcji von Neumanna: nie ma w niej naturalnej relacji porządku. W modelu von Neumanna $2 < 3$ oznaczało $2 \in 3$. Tutaj $2$ nie jest elementem $3$, więc relację mniejszości trzeba definiować osobno. Z tego powodu w nowoczesnej matematyce częściej stosuje się konstrukcję von Neumanna, ale obie są w pełni poprawne.

---

## Systemy zapisu liczb, w tym system pozycyjny

Zdefiniowaliśmy, czym są liczby, ale jak je zapisywać? Przez tysiące lat ludzkość wymyśliła wiele sposobów na reprezentowanie liczb. Większość z nich była jednak niepraktyczna i utrudniała arytmetykę. Prawdziwą rewolucją okazał się system pozycyjny, którego używamy do dziś. Przyjrzyjmy się kilku systemom, aby docenić jego geniusz.

### System jedynkowy (unarny)

Najprostszy i najbardziej intuicyjny system, używany prawdopodobnie od zarania dziejów. Każda jednostka jest reprezentowana przez jeden symbol (np. kreskę).

*   **Zapis:** Liczba 5 to `|||||`, a 3 to `|||`.
*   **Zalety:** Banalnie prosty do zrozumienia i użycia dla małych liczb.
*   **Wady:** Skrajnie nieefektywny. Zapisanie liczby milion wymaga miliona kresek. Arytmetyka jest uciążliwa.

### System sumeryjski (babiloński) - pozycyjny, baza 60

Jeden z pierwszych znanych systemów pozycyjnych, stworzony ponad 4000 lat temu! Babilończycy używali systemu o podstawie **60** (seksagesymalny).

*   **Zapis:** Używali pisma klinowego. Mieli dwa podstawowe symbole: klin oznaczający 1 ($\blacktriangledown$) i klin oznaczający 10 ($\blacktriangleleft$). Liczby od 1 do 59 tworzyli przez powtarzanie tych symboli. Na przykład 23 to $\blacktriangleleft\blacktriangleleft\blacktriangledown\blacktriangledown\blacktriangledown$. Kluczowe było to, że **pozycja** grupy symboli miała znaczenie. Zapis $\blacktriangleleft\blacktriangledown$ $\blacktriangledown\blacktriangledown$ (11, 2) mógł oznaczać $11 \cdot 60^1 + 2 \cdot 60^0 = 662$.
*   **Zalety:**
    *   **Genialny do ułamków:** Baza 60 ma mnóstwo dzielników (1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60), co niezwykle ułatwiało obliczenia na ułamkach. To dziedzictwo przetrwało do dziś w postaci 60 minut w godzinie i 360 (6 * 60) stopni w okręgu.
    *   Był to system **pozycyjny**, co stanowiło gigantyczny skok koncepcyjny.
*   **Wady:** Przez długi czas Babilończycy **nie mieli symbolu zera**. Aby odróżnić 2 od 120 ($2 \cdot 60$), zostawiali puste miejsce, co było źródłem niejednoznaczności. Dopiero później wprowadzono specjalny symbol-separator, który pełnił rolę zera wewnątrz liczby, ale nie na jej końcu.

### System Majów - pozycyjny, baza 20 (z zerem!)

Cywilizacja Majów, niezależnie od reszty świata, stworzyła niezwykle zaawansowany system liczbowy.

*   **Zapis:** Był to system o podstawie **20** (wigesimalny), zapisywany pionowo. Używali tylko trzech symboli: kropki dla 1, kreski dla 5 oraz stylizowanego symbolu muszli dla **zera**.
*   **Zalety:**
    *   **Wynalezienie zera:** Majowie byli jedną z niewielu cywilizacji (i pierwszą na kontynentach amerykańskich), która samodzielnie wynalazła i używała konceptu zera jako pełnoprawnej liczby i symbolu zastępczego. To absolutny przełom!
    *   System był pozycyjny i bardzo spójny.
*   **Wady:** W zapisie kalendarzowym Majowie wprowadzali modyfikację: trzecia pozycja od dołu nie oznaczała $20^2=400$, lecz $18 \times 20 = 360$, aby lepiej przybliżyć długość roku. To sprawiało, że system nie był "czysto" dwudziestkowy w każdym zastosowaniu.

### System dziesiętny (hindusko-arabski) - nasz system

System, którego używamy na co dzień, jest zwieńczeniem tysięcy lat ewolucji myśli matematycznej. Jego siła leży w połączeniu trzech kluczowych idei:

1.  **System jest pozycyjny:** Wartość cyfry zależy od jej miejsca w liczbie. W liczbie **121** pierwsza jedynka oznacza 100, a druga jedynka oznacza 1.
2.  **Ma stałą bazę:** Bazą jest 10, co oznacza, że mamy 10 unikalnych symboli (cyfr) dla liczb od 0 do 9.
3.  **Posiada symbol zera:** Zero jest kluczowe. Pełni podwójną rolę: jest liczbą samą w sobie oraz symbolem zastępczym, który "trzyma" pozycję, jak w liczbie 105, gdzie zero informuje nas o braku dziesiątek.

Dowolną liczbę w systemie o podstawie $b$ możemy zapisać jako sumę potęg tej podstawy:

$$
(c_n c_{n-1} \dots c_1 c_0)_b = c_n \cdot b^n + c_{n-1} \cdot b^{n-1} + \dots + c_1 \cdot b^1 + c_0 \cdot b^0
$$

Na przykład:

$$
253_{10} = 2 \cdot 10^2 + 5 \cdot 10^1 + 3 \cdot 10^0 = 200 + 50 + 3
$$

*   **Zalety:** Niezwykle wydajny, uniwersalny i prosty w użyciu. Umożliwia wykonywanie skomplikowanych operacji arytmetycznych za pomocą prostych, powtarzalnych algorytmów (np. pisemne dodawanie czy mnożenie).
*   **Wady:** Z perspektywy historycznej – trudno o nich mówić. Jest to najbardziej zaawansowany i elastyczny system, jaki wymyślono.

Ta podróż od prostych kresek do abstrakcyjnego systemu pozycyjnego z zerem jest jedną z najważniejszych w historii ludzkiej myśli. To właśnie ten ostatni system otworzył drzwi do nowożytnej matematyki, nauki i technologii.

### Intuicja systemu pozycyjnego: Drzewa i słowa

Aby zrozumieć, na czym polega siła systemu pozycyjnego, możemy przeprowadzić eksperyment myślowy, który sam zaproponowałeś. Stwórzmy własny system nazywania kolejnych liczb naturalnych przy użyciu drzewa i alfabetu składającego się z trzech liter: `{a, b, c}`.

**Krok 1: Drzewo o głębokości 1**

Poniższe diagramy są przedstawione w środowisku `verbatim` z LaTeX, które gwarantuje, że ich tekstowa reprezentacja zostanie poprawnie przeniesiona do pliku PDF. Istnieją bardziej zaawansowane pakiety graficzne w LaTeX (jak `tikz`), które pozwalają na generowanie diagramów, ale `verbatim` jest najbezpieczniejszym sposobem w naszym przypadku.

Zaczynamy od korzenia (Root), z którego wyrastają 3 gałęzie, a każda kończy się liściem oznaczonym inną literą z naszego alfabetu.

\begin{verbatim}
      /-- a
Root--|-- b
      \-- c
\end{verbatim}

Przechodząc od korzenia do każdego liścia, tworzymy "słowa". Na tym etapie mamy 3 unikalne słowa: `a`, `b`, `c`. Możemy umówić się, że będą one reprezentować trzy pierwsze liczby:

*   1 $\leftrightarrow$ `a`
*   2 $\leftrightarrow$ `b`
*   3 $\leftrightarrow$ `c`

**Krok 2: Drzewo o głębokości 2**

Teraz rozbudowujemy nasze drzewo. Z każdego liścia (`a`, `b`, `c`) wyprowadzamy kolejne 3 gałęzie, które znów kończą się liśćmi `a`, `b`, `c`.

\begin{verbatim}
          /-- a  (aa)
      /-- a --|-- b  (ab)
     /      \-- c  (ac)
    /
   /          /-- a  (ba)
Root --|-- b --|-- b  (bb)
   \          \-- c  (bc)
    \
     \      /-- a  (ca)
      \-- c --|-- b  (cb)
            \-- c  (cc)
\end{verbatim}

Ścieżki od korzenia do nowych liści tworzą nam teraz 9 nowych, dwuliterowych słów:

*   `a` $\rightarrow$ `a` daje słowo `aa`
*   `a` $\rightarrow$ `b` daje słowo `ab`
*   `a` $\rightarrow$ `c` daje słowo `ac`
*   `b` $\rightarrow$ `a` daje słowo `ba`
*   `b` $\rightarrow$ `b` daje słowo `bb`
*   `b` $\rightarrow$ `c` daje słowo `bc`
*   `c` $\rightarrow$ `a` daje słowo `ca`
*   `c` $\rightarrow$ `b` daje słowo `cb`
*   `c` $\rightarrow$ `c` daje słowo `cc`

Mamy więc nowe, dłuższe słowa, które mogą reprezentować kolejne liczby.

**Krok 3: Drzewo o głębokości 3**

Gdybyśmy powtórzyli ten proces jeszcze raz, pełne drzewo stałoby się bardzo duże i nieczytelne. Możemy jednak pokazać, jak rozwija się jedna z gałęzi (np. gałąź `a`), aby zilustrować zasadę. Z każdego liścia z kroku 2 (`aa`, `ab`, `ac`, itd.) wyrastają kolejne 3 gałęzie.

\begin{verbatim}
                      /-- a  (aaa)
                  /-- a --|-- b  (aab)
                 /      \-- c  (aac)
                /
               /          /-- a  (aba)
           /-- a --|-- b --|-- b  (abb)
          /      \       \-- c  (abc)
         /        \
        /          \     /-- a  (aca)
       /            \-- c--|-- b  (acb)
      /                   \-- c  (acc)
     /
Root --|-- ... (gałąź 'b' rozwija się analogicznie, tworząc słowa od 'baa' do 'bcc')
     \
      \-- ... (gałąź 'c' rozwija się analogicznie, tworząc słowa od 'caa' do 'ccc')
\end{verbatim}

W ten sposób, dokładając kolejną literę, tworzymy $3 \times 9 = 27$ unikalnych, trzyliterowych słów. Oto one, wypisane w systematycznej kolejności, która odpowiada przechodzeniu przez drzewo:

*   `aa` $\rightarrow$ `a` daje słowo `aaa`
*   `aa` $\rightarrow$ `b` daje słowo `aab`
*   `aa` $\rightarrow$ `c` daje słowo `aac`
*   `ab` $\rightarrow$ `a` daje słowo `aba`
*   `ab` $\rightarrow$ `b` daje słowo `abb`
*   `ab` $\rightarrow$ `c` daje słowo `abc`
*   `ac` $\rightarrow$ `a` daje słowo `aca`
*   `ac` $\rightarrow$ `b` daje słowo `acb`
*   `ac` $\rightarrow$ `c` daje słowo `acc`
*   `ba` $\rightarrow$ `a` daje słowo `baa`
*   `ba` $\rightarrow$ `b` daje słowo `bab`
*   `ba` $\rightarrow$ `c` daje słowo `bac`
*   `bb` $\rightarrow$ `a` daje słowo `bba`
*   `bb` $\rightarrow$ `b` daje słowo `bbb`
*   `bb` $\rightarrow$ `c` daje słowo `bbc`
*   `bc` $\rightarrow$ `a` daje słowo `bca`
*   `bc` $\rightarrow$ `b` daje słowo `bcb`
*   `bc` $\rightarrow$ `c` daje słowo `bcc`
*   `ca` $\rightarrow$ `a` daje słowo `caa`
*   `ca` $\rightarrow$ `b` daje słowo `cab`
*   `ca` $\rightarrow$ `c` daje słowo `cac`
*   `cb` $\rightarrow$ `a` daje słowo `cba`
*   `cb` $\rightarrow$ `b` daje słowo `cbb`
*   `cb` $\rightarrow$ `c` daje słowo `cbc`
*   `cc` $\rightarrow$ `a` daje słowo `cca`
*   `cc` $\rightarrow$ `b` daje słowo `ccb`
*   `cc` $\rightarrow$ `c` daje słowo `ccc`

Te 27 słów może reprezentować kolejne 27 liczb. To pokazuje, jak budowanie coraz głębszych drzew daje nam dłuższe słowa, które pozwalają na reprezentację coraz większej liczby liczb.

**Wniosek i połączenie z systemem pozycyjnym**

W ten sposób odkryliśmy dwie fundamentalne zasady:

1.  **Zasada kombinacji:** Używając skończonego zestawu symboli (nasz alfabet `{a, b, c}`), możemy tworzyć nieskończenie wiele unikalnych "słów" (reprezentacji liczb), po prostu zwiększając ich długość.
2.  **Zasada pozycji (NAJWAŻNIEJSZA):** Zauważ, że litera `a` w słowie `ab` i litera `a` w słowie `ba` znajdują się na różnych pozycjach i przez to całe słowa reprezentują inne liczby. To jest właśnie **sedno systemu pozycyjnego**: znaczenie symbolu zależy od jego **pozycji** w zapisie.

Nasz standardowy system dziesiętny działa dokładnie tak samo!

*   Mamy alfabet 10 cyfr: `{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}`.
*   W liczbie `121`, pierwsza cyfra `1` (od lewej) oznacza `100`, a ostatnia cyfra `1` oznacza po prostu `1`. Ich wartość zależy od pozycji.

Twój system oparty na drzewie jest genialny w budowaniu intuicji. Standardowy system pozycyjny idzie o krok dalej: zamiast po prostu listować wszystkie słowa o długości 1, potem 2, potem 3, wprowadza płynne przejście (po `9` następuje `10`, a nie `00`), a wartość liczby można obliczyć ze znanego nam już wzoru:

$$
(c_n c_{n-1} \dots c_1 c_0)_b = c_n \cdot b^n + \dots + c_0 \cdot b^0
$$

Dzięki temu prostemu wzorowi arytmetyka staje się niezwykle łatwa. Ale idea tworzenia nieskończonej liczby nazw z kilku symboli i nadawania im znaczenia przez pozycję jest dokładnie tym, co odkryłeś za pomocą swojego drzewa!