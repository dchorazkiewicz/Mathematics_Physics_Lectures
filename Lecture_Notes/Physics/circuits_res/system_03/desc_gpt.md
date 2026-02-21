Na rysunku przedstawiono **obwód prądu stałego (DC)** złożony z sześciu rezystorów oraz wyraźnie zaznaczonych węzłów i kierunków prądów oraz napięć.

Poniżej pełny, uporządkowany opis struktury układu.

---

# 1️⃣ Węzły obwodu

W układzie wyróżniono cztery główne węzły:

* **A** – lewy wspólny węzeł (punkt rozdziału trzech gałęzi)
* **B** – górny prawy węzeł
* **C** – środkowy prawy węzeł
* **D** – dolny prawy węzeł

Węzeł **A** łączy trzy rezystory poziome (R1, R2, R3).
Węzły **B–C–D** tworzą pionową strukturę po prawej stronie.

---

# 2️⃣ Elementy obwodu

Układ zawiera sześć rezystorów:

### 🔹 Gałęzie poziome (od węzła A)

* **R1** – między węzłami **A–B**
* **R2** – między węzłami **A–C**
* **R3** – między węzłami **A–D**

Są to trzy równoległe „ramiona” wychodzące z węzła A.

---

### 🔹 Gałęzie pionowe (po prawej stronie)

* **R4** – między węzłami **B–C**
* **R5** – między węzłami **C–D**

Rezystory R4 i R5 są połączone **szeregowo** w pionowej kolumnie.

---

### 🔹 Gałąź skrajna prawa

* **R6** – między węzłami **B–D**

Rezystor R6 łączy bezpośrednio górny i dolny węzeł prawej strony.

---

# 3️⃣ Struktura topologiczna

Układ można interpretować jako:

* Trzy rezystory (R1, R2, R3) łączące wspólny węzeł A z trzema różnymi węzłami po prawej stronie.
* Po prawej stronie znajduje się:

  * szeregowe połączenie R4–R5,
  * równoległa do nich gałąź R6.

Czyli między węzłami B i D mamy:

* drogę przez R4 + R5,
* oraz równoległą drogę przez R6.

---

# 4️⃣ Zaznaczone prądy

Na schemacie oznaczono kierunki prądów:

* ( i_1 ) – przez R1 (od A do B)
* ( i_2 ) – przez R2 (od A do C)
* ( i_3 ) – przez R3 (od A do D)
* ( i_4 ) – przez R4 (od B do C)
* ( i_5 ) – przez R5 (od C do D)
* ( i_6 ) – przez R6 (od B do D)

Kierunki są przyjęte umownie (zgodnie ze strzałkami).

---

# 5️⃣ Zaznaczone napięcia

Każdy rezystor ma oznaczone napięcie:

* ( u_1 ) – na R1
* ( u_2 ) – na R2
* ( u_3 ) – na R3
* ( u_4 ) – na R4
* ( u_5 ) – na R5
* ( u_6 ) – na R6

Strzałki napięć określają przyjętą biegunowość (umowną).

---

# 6️⃣ Oczka (pętle)

Zaznaczono trzy oczka do zastosowania II prawa Kirchhoffa:

* 🔴 Oczko I (górne lewe)
* 🔴 Oczko II (dolne lewe)
* 🔴 Oczko III (prawe)

To sugeruje, że układ można rozwiązać:

* metodą prądów oczkowych,
* metodą węzłową,
* klasycznymi równaniami Kirchhoffa.

---

# 7️⃣ Charakter układu

Jest to:

* liniowy obwód rezystancyjny,
* obwód wielowęzłowy,
* układ mieszany (szeregowo-równoległy),
* układ mostkowy (ma strukturę przypominającą mostek rezystancyjny).

Nie jest to prosty układ redukowalny jedynie przez przekształcenia szeregowo-równoległe – wymaga pełnej analizy metodą Kirchhoffa.

---

Jeśli chcesz, mogę teraz:

* 🔹 zapisać równania węzłowe,
* 🔹 zapisać równania oczkowe,
* 🔹 wykonać pełne rozwiązanie symboliczne,
* 🔹 przygotować z tego materiał dydaktyczny (markdown / LaTeX),
* 🔹 albo przeanalizować topologię bardziej formalnie (graf obwodu).

Pewnie — zapiszę **równania oczkowe (metoda prądów oczkowych)** dla trzech oczek I, II, III z rysunku i rozwiążę je **symbolicznie**.

Ponieważ na schemacie **nie ma jawnie narysowanych źródeł** (napięciowych/prądowych), wprowadzę ogólne „siły elektromotoryczne” oczek:

* (E_1) — algebraiczna suma napięć źródeł w oczku I (zgodnie z kierunkiem oczka),
* (E_2) — dla oczka II,
* (E_3) — dla oczka III.

Jeśli w Twoim zadaniu źródeł faktycznie nie ma, wtedy na końcu po prostu podstawiasz (E_1=E_2=E_3=0) i dostajesz rozwiązanie trywialne.

---

## 1) Definicja prądów oczkowych

Przyjmuję prądy oczkowe zgodnie z czerwonymi strzałkami (zgodnie z ruchem wskazówek zegara):

* (I_1) — oczko **I**: gałąź (R1), (R4), (R2)
* (I_2) — oczko **II**: gałąź (R2), (R5), (R3)
* (I_3) — oczko **III**: gałąź (R4), (R6), (R5)

Wspólne rezystory:

* (R2) jest wspólny dla oczek I i II,
* (R4) jest wspólny dla oczek I i III,
* (R5) jest wspólny dla oczek II i III.

---

## 2) Równania oczkowe (KVL)

### Oczko I

[
R1,I_1 + R4,(I_1-I_3) + R2,(I_1-I_2)=E_1
]

### Oczko II

[
R3,I_2 + R5,(I_2-I_3) + R2,(I_2-I_1)=E_2
]

### Oczko III

[
R6,I_3 + R4,(I_3-I_1) + R5,(I_3-I_2)=E_3
]

Po uporządkowaniu do postaci liniowej:

[
(R1+R2+R4)I_1 - R2 I_2 - R4 I_3 = E_1
]
[
-R2 I_1 + (R2+R3+R5)I_2 - R5 I_3 = E_2
]
[
-R4 I_1 - R5 I_2 + (R4+R5+R6)I_3 = E_3
]

---

## 3) Rozwiązanie symboliczne

Wygodnie zdefiniować wspólny mianownik (wyznacznik układu):
[
\Delta =
\begin{aligned}
& R1R2R4 + R1R2R5 + R1R2R6 + R1R3R4 + R1R3R5 + R1R3R6 + R1R4R5 + R1R5R6 \
& + R2R3R4 + R2R3R5 + R2R3R6 + R2R4R6 + R2R5R6 + R3R4R5 + R3R4R6 + R4R5R6
\end{aligned}
]

Wtedy:

### Prąd oczkowy (I_1)

[
I_1=\frac{N_1}{\Delta}
]
gdzie
[
\begin{aligned}
N_1=&\ E_1(R2R4+R2R5+R2R6+R3R4+R3R5+R3R6+R4R5+R5R6)\
&+E_2(R2R4+R2R5+R2R6+R4R5)\
&+E_3(R2R4+R2R5+R3R4+R4R5)
\end{aligned}
]

### Prąd oczkowy (I_2)

[
I_2=\frac{N_2}{\Delta}
]
gdzie
[
\begin{aligned}
N_2=&\ E_1(R2R4+R2R5+R2R6+R4R5)\
&+E_2(R1R4+R1R5+R1R6+R2R4+R2R5+R2R6+R4R5+R4R6)\
&+E_3(R1R5+R2R4+R2R5+R4R5)
\end{aligned}
]

### Prąd oczkowy (I_3)

[
I_3=\frac{N_3}{\Delta}
]
gdzie
[
\begin{aligned}
N_3=&\ E_1(R2R4+R2R5+R3R4+R4R5)\
&+E_2(R1R5+R2R4+R2R5+R4R5)\
&+E_3(R1R2+R1R3+R1R5+R2R3+R2R4+R2R5+R3R4+R4R5)
\end{aligned}
]

---

## 4) Prądy gałęziowe (te z rysunku) w funkcji (I_1,I_2,I_3)

Przy zgodności z kierunkami strzałek na schemacie:

* przez (R1): (; i_1 = I_1)
* przez (R2) (A→C): (; i_2 = I_2 - I_1)
* przez (R3) (A→D): (; i_3 = -I_2)
* przez (R4) (B→C): (; i_4 = I_1 - I_3)
* przez (R5) (C→D): (; i_5 = I_2 - I_3)
* przez (R6) (B→D): (; i_6 = I_3)

Napięcia na rezystorach (w najprostszej postaci) dostajesz z prawa Ohma, np. (u_1=R1,i_1), (u_4=R4,i_4), itd. (z uwzględnieniem zwrotu strzałki napięcia na rysunku).

---

## 5) Przypadek bez źródeł

Jeżeli w tym układzie **nie ma żadnych źródeł**, to:
[
E_1=E_2=E_3=0 \quad\Rightarrow\quad I_1=I_2=I_3=0
]
a więc wszystkie prądy gałęziowe też wychodzą równe zero.

---

Jeśli powiesz mi, **gdzie jest źródło i jakie ma parametry** (np. napięcie między A i D, albo źródło w której gałęzi), to od razu podstawimy to do (E_1,E_2,E_3) i dostaniesz konkretne prądy/napięcia (wciąż symbolicznie lub liczbowo).
