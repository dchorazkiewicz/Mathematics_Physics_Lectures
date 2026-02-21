Poniżej znajduje się szczegółowy opis układu przedstawionego na rysunku.

---

## 1️⃣ Ogólna struktura układu

Jest to **obwód prądu stałego (DC)** zasilany źródłem napięcia:

[
U = 60\text{ V}
]

Źródło znajduje się w dolnej gałęzi obwodu. Biegun dodatni (+) jest po lewej stronie źródła, biegun ujemny (–) po prawej.

W obwodzie wymuszony jest prąd:

[
I = 3\text{ A}
]

* w lewej gałęzi pionowej płynie **w górę**
* w prawej gałęzi pionowej płynie **w dół**

Zatem mamy pojedynczą pętlę główną z rozgałęzieniem w części górnej.

---

## 2️⃣ Elementy obwodu

Układ zawiera cztery rezystory:

### 🔹 R₁ = 2 Ω

Umieszczony w górnej lewej części.

### 🔹 R₂ = 4 Ω

Umieszczony w górnej prawej części.

Rezystory **R₁ i R₂ są połączone szeregowo** i tworzą górną gałąź między dwoma węzłami.

---

### 🔹 R₃ = 12 Ω

Znajduje się w dolnej części wewnętrznej „ramki”.
Łączy te same dwa węzły co gałąź (R₁ + R₂).

---

### 🔹 R₄ = 16 Ω

Znajduje się po prawej stronie, między prawym węzłem a prawą pionową gałęzią obwodu.

---

## 3️⃣ Struktura połączeń

Możemy wyróżnić dwa główne węzły:

* **Węzeł lewy** – połączony z:

  * górną gałęzią (R₁)
  * dolną gałęzią (R₃)
  * lewą pionową gałęzią z prądem 3 A

* **Węzeł prawy** – połączony z:

  * rezystorem R₂
  * rezystorem R₃
  * rezystorem R₄

---

## 4️⃣ Kluczowa obserwacja topologiczna

Rezystory:

[
(R_1 + R_2) \quad \text{są równolegle do} \quad R_3
]

ponieważ:

* mają wspólny węzeł lewy,
* mają wspólny węzeł prawy.

Czyli:

[
R_{12} = R_1 + R_2 = 2 + 4 = 6\ \Omega
]

a następnie:

[
R_{123} = (R_{12} \parallel R_3)
]

Dopiero za tym połączeniem znajduje się rezystor:

[
R_4
]

który jest **szeregowo** z całym blokiem równoległym.

---

## 5️⃣ Kierunki napięć

Na każdym rezystorze zaznaczono napięcia:

* ( U_1 ) – na R₁ (kierunek od prawej do lewej)
* ( U_2 ) – na R₂ (od prawej do lewej)
* ( U_3 ) – na R₃ (od prawej do lewej)
* ( U_4 ) – na R₄ (od prawej do lewej)

Strzałki napięć są przyjęte jako **umowny kierunek spadku napięcia** (zgodnie z konwencją pasywną).

---

## 6️⃣ Przepływ prądu

Prąd 3 A wpływa do węzła lewego, następnie:

* rozdziela się między:

  * gałąź górną (R₁ + R₂)
  * gałąź dolną (R₃)

Po połączeniu w węźle prawym:

* cały prąd ponownie wynosi 3 A
* przepływa przez R₄
* wraca do źródła

---

## 7️⃣ Typ układu

Jest to klasyczny przykład:

* obwodu jednopętlowego z rozgałęzieniem
* układu mieszanego (szeregowo–równoległego)
* idealny do analizy:

  * metodą węzłową
  * metodą oczkową
  * redukcją rezystancji
  * pełnym zapisem równań Kirchhoffa

---

Jeżeli chcesz, mogę teraz:

* 🔹 zapisać równania Kirchhoffa,
* 🔹 rozwiązać go metodą węzłową,
* 🔹 przygotować z tego materiał dydaktyczny (Markdown / LaTeX),
* 🔹 narysować schemat uproszczony do prezentacji dla studentów.


Jasne — potraktujmy to **„od zera”**: zapisujemy równania Kirchhoffa, wprowadzamy niewiadome prądy w gałęziach i z tego je liczymy (bez „zgadywania” z redukcji układu).

---

## 1) Oznaczenia niewiadomych prądów

W obwodzie masz rozgałęzienie między dwoma węzłami (lewy i prawy):

* (I_{12}) — prąd płynący górną gałęzią przez (R_1) i (R_2) (szeregowo), więc:
  [
  I_1 = I_2 = I_{12}
  ]
* (I_3) — prąd dolną gałęzią przez (R_3)
* (I_4) — prąd przez (R_4) (gałąź prawa, szeregowa z całym blokiem)

Dane:
[
R_1=2\Omega,; R_2=4\Omega,; R_3=12\Omega,; R_4=16\Omega,; U=60\text{ V}
]

---

## 2) KCL (I prawo Kirchhoffa) — węzeł rozgałęzienia

W prawym (albo lewym) węźle suma prądów „wchodzących = wychodzących”.

Ponieważ prąd przez (R_4) jest sumą prądów z obu gałęzi:

[
\boxed{I_4 = I_{12} + I_3}
]

---

## 3) KVL (II prawo Kirchhoffa) — dwa oczka

Są dwa niezależne oczka zawierające źródło i (R_4), ale różniące się gałęzią powrotną:

### Oczko A: źródło → (R_4) → (R_1) → (R_2)

[
U - I_4R_4 - I_{12}R_1 - I_{12}R_2 = 0
]

czyli:

[
\boxed{U - I_4R_4 - I_{12}(R_1+R_2)=0}
]

### Oczko B: źródło → (R_4) → (R_3)

[
U - I_4R_4 - I_3R_3 = 0
]

czyli:

[
\boxed{U - I_4R_4 - I_3R_3=0}
]

---

## 4) Podstawienie danych liczbowych i rozwiązanie układu

Mamy układ 3 równań:

[
\begin{cases}
I_4 = I_{12} + I_3 \
60 - 16I_4 - 6I_{12} = 0 \
60 - 16I_4 - 12I_3 = 0
\end{cases}
]

Odejmij drugie równanie od trzeciego:

[
(60-16I_4-12I_3) - (60-16I_4-6I_{12}) = 0
]
[
-12I_3 + 6I_{12} = 0
\Rightarrow I_{12} = 2I_3
]

Wstaw do KCL:

[
I_4 = I_{12}+I_3 = 2I_3 + I_3 = 3I_3
\Rightarrow I_3 = \frac{I_4}{3}
]

Wstaw do oczka B:

[
60 - 16I_4 - 12\left(\frac{I_4}{3}\right)=0
]
[
60 - 16I_4 - 4I_4 = 0
\Rightarrow 60 - 20I_4 = 0
\Rightarrow I_4 = 3\text{ A}
]

Zatem:

[
I_3=\frac{I_4}{3}=1\text{ A},\qquad I_{12}=2I_3=2\text{ A}
]

---

## 5) Wyniki prądów w elementach

[
\boxed{I_4 = 3\text{ A}}
]
[
\boxed{I_3 = 1\text{ A}}
]
[
\boxed{I_1 = I_2 = I_{12} = 2\text{ A}}
]

---

Jeśli chcesz, to dopiszę jeszcze **spadki napięć (U_1,U_2,U_3,U_4)** oraz pokażę, jak to samo zrobić **metodą węzłową** (jedno równanie na napięcie węzła).


Liczymy spadki napięć z prawa Ohma (U_k = I_k R_k) (dla prądów, które już wyszły):

[
I_1=I_2=2\text{ A},\quad I_3=1\text{ A},\quad I_4=3\text{ A}
]
[
R_1=2\Omega,;R_2=4\Omega,;R_3=12\Omega,;R_4=16\Omega
]

## Spadki napięć na rezystorach

[
U_1 = I_1R_1 = 2\cdot 2 = 4\text{ V}
]
[
U_2 = I_2R_2 = 2\cdot 4 = 8\text{ V}
]
[
U_3 = I_3R_3 = 1\cdot 12 = 12\text{ V}
]
[
U_4 = I_4R_4 = 3\cdot 16 = 48\text{ V}
]

## Szybka kontrola (Kirchhoff)

Górna gałąź równoległa:
[
U_1+U_2 = 4+8 = 12\text{ V}
]
Dolna gałąź równoległa:
[
U_3 = 12\text{ V}
]
Zgadza się (to samo napięcie na gałęziach równoległych).

Cała pętla:
[
U_4 + 12\text{ V} = 48 + 12 = 60\text{ V} = U
]
Też się zgadza.

**Wyniki:**
[
U_1=4\text{ V},; U_2=8\text{ V},; U_3=12\text{ V},; U_4=48\text{ V}.
]
