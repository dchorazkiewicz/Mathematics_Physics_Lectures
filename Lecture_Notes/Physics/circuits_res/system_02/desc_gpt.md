Na rysunku przedstawiono **liniowy obwód prądu stałego** złożony z rezystorów i idealnych źródeł napięcia. Układ jest płaski, posiada trzy oczka oraz trzy główne węzły oznaczone literami **a**, **b**, **c**.

---

## 🔷 1. Struktura topologiczna układu

Układ ma:

* **3 węzły główne:**

  * **a** – lewy górny węzeł
  * **b** – dolny wspólny węzeł (referencyjny)
  * **c** – prawy górny węzeł

* **3 oczka (pętle niezależne)** oznaczone numerami 1, 2, 3 (strzałki pokazują przyjęte kierunki obiegów do zapisu II prawa Kirchhoffa).

---

## 🔷 2. Elementy obwodu

Układ składa się z:

### 🔌 Źródła napięcia (idealne)

1. **E₁** – lewe źródło napięcia (gałąź między węzłami a–b)
2. **E₂** – prawe źródło napięcia (gałąź między węzłami c–b)

Strzałki przy źródłach oznaczają zwrot przyjętej biegunowości napięcia (kierunek wzrostu potencjału).

---

### 🟦 Rezystory

1. **R₁** – lewa gałąź pionowa (szeregowo z E₁)
2. **R₂** – prawa gałąź pionowa (szeregowo z E₂)
3. **R₃** – środkowa gałąź pionowa (między a–b przez R4/R5 węzłowo, ale fizycznie między węzłem środkowym a b)
4. **R₄** – poziomo między węzłem a a węzłem środkowym
5. **R₅** – poziomo między węzłem środkowym a węzłem c
6. **R₆** – górny rezystor łączący bezpośrednio węzeł a z węzłem c

Łącznie: **6 rezystorów + 2 źródła napięcia**

---

## 🔷 3. Gałęzie obwodu

Możemy wyróżnić następujące gałęzie:

1. a → b : (R₁ + E₁)
2. c → b : (R₂ + E₂)
3. węzeł środkowy → b : R₃
4. a → węzeł środkowy : R₄
5. węzeł środkowy → c : R₅
6. a → c : R₆

---

## 🔷 4. Prądy w układzie

Na schemacie zaznaczono kierunki przyjętych prądów:

* **I₁** – w lewej gałęzi pionowej (R₁, E₁)
* **I₂** – w prawej gałęzi pionowej (R₂, E₂)
* **I₃** – przez rezystor R₃ (w dół do węzła b)
* **I₄** – przez R₄ (od węzła środkowego w lewo)
* **I₅** – przez R₅ (od węzła środkowego w prawo)
* **I₆** – przez R₆ (z a do c)

Strzałki wyznaczają **umowne dodatnie kierunki prądów** (jeśli wynik obliczeń wyjdzie ujemny, oznacza to przeciwny rzeczywisty kierunek).

---

## 🔷 5. Napięcia na elementach

Na rezystorach zaznaczono spadki napięć:

* **U₁** – na R₁
* **U₂** – na R₂
* **U₃** – na R₃
* **U₄** – na R₄
* **U₅** – na R₅
* **U₆** – na R₆

Zgodnie z prawem Ohma:

[
U_k = R_k I_k
]

dla każdego rezystora (k = 1,\dots,6).

---

## 🔷 6. Charakter fizyczny układu

Jest to:

* obwód **rezystancyjny liniowy**
* zasilany **dwoma niezależnymi źródłami napięcia**
* posiadający **sprzężenie międzygałęziowe** przez rezystor R₆
* zawierający **mostkową strukturę poziomą (R4–R5–R6)**

Układ nie jest prostym szeregowym ani równoległym połączeniem — wymaga zastosowania:

* metody oczkowej
* metody węzłowej
* lub przekształceń macierzowych

---

## 🔷 7. Interpretacja topologiczna

Węzeł **b** pełni rolę:

* wspólnego punktu odniesienia
* naturalnego kandydata na masę (0 V)
* węzła o największym stopniu połączeń

Górne węzły **a** i **c** są połączone:

* bezpośrednio przez R₆
* pośrednio przez R₄–R₃–R₅

To powoduje istnienie trzeciego oczka (górnego).

---

## 🔷 8. Stopień złożoności

* Liczba węzłów: 3
* Liczba gałęzi: 6
* Liczba niezależnych oczek: 3

Zależność:
[
L = B - N + 1 = 6 - 3 + 1 = 4
]

Jedno oczko jest zależne, dlatego mamy 3 niezależne równania oczkowe.

---

Jeśli chcesz, mogę teraz:

* 🔹 zapisać pełne równania węzłowe
* 🔹 zapisać równania oczkowe
* 🔹 przygotować wersję dydaktyczną do prezentacji
* 🔹 wykonać analizę mocy w układzie
* 🔹 rozwiązać symbolicznie

Powiedz, w którą stronę idziemy 🙂


Pewnie — zrobię **pełne rozwiązanie symboliczne** metodą **węzłową (KCL)**, wyznaczając **napięcia węzłowe** oraz **wszystkie prądy gałęziowe** zgodnie ze strzałkami z rysunku.

Przyjmuję węzeł **b** jako odniesienie:
[
V_b=0.
]

Oznaczenia napięć węzłowych:

* (V_a) — potencjał węzła **a**
* (V_c) — potencjał węzła **c**
* (V_m) — potencjał **węzła środkowego** (połączenie (R_4,R_5,R_3))

Dodatkowo (ważne przy gałęziach z idealnym źródłem napięcia w szeregu z rezystorem):

* węzeł pomiędzy (E_1) i (R_1) ma potencjał (;V_{x1}=E_1) (bo źródło (E_1) jest między (b) i tym punktem),
* węzeł pomiędzy (E_2) i (R_2) ma potencjał (;V_{x2}=E_2).

---

## 1) Równania KCL w węzłach (układ równań)

Prądy liczę jako „**z węzła na zewnątrz**” wprost z różnic potencjałów.

### Węzeł (a)

Połączenia: do (m) przez (R_4), do (c) przez (R_6), do (b) przez gałąź ((R_1 \text{ w szereg z } E_1)):
[
\frac{V_a-V_m}{R_4}+\frac{V_a-V_c}{R_6}+\frac{V_a-E_1}{R_1}=0.
]

### Węzeł (c)

Połączenia: do (m) przez (R_5), do (a) przez (R_6), do (b) przez ((R_2 \text{ w szereg z } E_2)):
[
\frac{V_c-V_m}{R_5}+\frac{V_c-V_a}{R_6}+\frac{V_c-E_2}{R_2}=0.
]

### Węzeł (m)

Połączenia: do (a) przez (R_4), do (c) przez (R_5), do (b) przez (R_3):
[
\frac{V_m-V_a}{R_4}+\frac{V_m-V_c}{R_5}+\frac{V_m}{R_3}=0.
]

---

## 2) Rozwiązanie symboliczne napięć węzłowych

Wygodnie wprowadzić wspólny mianownik:
[
\begin{aligned}
D={}&
R_1R_2R_4+R_1R_2R_5+R_1R_2R_6+
R_1R_3R_4+R_1R_3R_5+R_1R_3R_6\
&+R_1R_4R_5+R_1R_5R_6+
R_2R_3R_4+R_2R_3R_5+R_2R_3R_6\
&+R_2R_4R_5+R_2R_4R_6+
R_3R_4R_6+R_3R_5R_6+R_4R_5R_6.
\end{aligned}
]

### Napięcie węzła (a)

[
\begin{aligned}
V_a=\frac{1}{D}\Big(&
E_1(R_2R_3R_4+R_2R_3R_5+R_2R_3R_6+R_2R_4R_5+R_2R_4R_6\
&\quad +R_3R_4R_6+R_3R_5R_6+R_4R_5R_6)
+E_2(R_1R_3R_4+R_1R_3R_5+R_1R_3R_6+R_1R_4R_5)
\Big).
\end{aligned}
]

### Napięcie węzła (c)

[
\begin{aligned}
V_c=\frac{1}{D}\Big(&
E_1(R_2R_3R_4+R_2R_3R_5+R_2R_3R_6+R_2R_4R_5)\
&+E_2(R_1R_3R_4+R_1R_3R_5+R_1R_3R_6+R_1R_4R_5+R_1R_5R_6\
&\quad +R_3R_4R_6+R_3R_5R_6+R_4R_5R_6)
\Big).
\end{aligned}
]

### Napięcie węzła środkowego (m)

[
V_m=\frac{R_3}{D}\Big(
E_1(R_2R_4+R_2R_5+R_2R_6+R_5R_6)+
E_2(R_1R_4+R_1R_5+R_1R_6+R_4R_6)
\Big).
]

Oraz (V_b=0).

---

## 3) Prądy gałęziowe (zgodne ze strzałkami na rysunku)

Przyjmuję kierunki jak na schemacie:

* (I_1): w górę w lewej gałęzi (od (b) do (a))
* (I_2): w górę w prawej gałęzi (od (b) do (c))
* (I_3): w dół przez (R_3) (od (m) do (b))
* (I_4): w lewo przez (R_4) (od (m) do (a))
* (I_5): w prawo przez (R_5) (od (m) do (c))
* (I_6): w prawo przez (R_6) (od (a) do (c))

Wtedy:

[
I_1=\frac{E_1-V_a}{R_1},\qquad
I_2=\frac{E_2-V_c}{R_2},
]
[
I_3=\frac{V_m}{R_3},\qquad
I_4=\frac{V_m-V_a}{R_4},\qquad
I_5=\frac{V_m-V_c}{R_5},\qquad
I_6=\frac{V_a-V_c}{R_6}.
]

Jeśli chcesz od razu w postaci „jednego ułamka” (wszystko nad (D)), to:

[
I_1=\frac{
E_1(R_2R_4+R_2R_5+R_2R_6+R_3R_4+R_3R_5+R_3R_6+R_4R_5+R_5R_6)
------------------------------------------------------------

E_2(R_3R_4+R_3R_5+R_3R_6+R_4R_5)
}{D},
]

[
I_2=\frac{

* E_1(R_3R_4+R_3R_5+R_3R_6+R_4R_5)

-

E_2(R_1R_4+R_1R_5+R_1R_6+R_3R_4+R_3R_5+R_3R_6+R_4R_5+R_4R_6)
}{D},
]

[
I_3=\frac{
E_1(R_2R_4+R_2R_5+R_2R_6+R_5R_6)+
E_2(R_1R_4+R_1R_5+R_1R_6+R_4R_6)
}{D},
]

[
I_4=\frac{

* E_1(R_2R_5+R_2R_6+R_3R_6+R_5R_6)
* E_2(R_1R_5)

- E_2(R_3R_6)
  }{D},
  ]

[
I_5=\frac{

* E_1(R_2R_4)

- E_1(R_3R_6)

* E_2(R_1R_4+R_1R_6+R_3R_6+R_4R_6)
  }{D},
  ]

[
I_6=\frac{
E_1(R_2R_4+R_3R_4+R_3R_5+R_4R_5)
--------------------------------

E_2(R_1R_5+R_3R_4+R_3R_5+R_4R_5)
}{D}.
]

---

## 4) Spadki napięć na rezystorach (jeśli chcesz „U1…U6”)

Dla rezystorów najprościej:
[
U_{Rk}=R_k I_k.
]

Czyli np.:

* (U_{R4}=R_4 I_4 = V_m - V_a)
* (U_{R5}=R_5 I_5 = V_m - V_c)
* (U_{R6}=R_6 I_6 = V_a - V_c)
* (U_{R3}=R_3 I_3 = V_m)

A dla gałęzi z (R_1,E_1):

* napięcie w punkcie między (E_1) i (R_1): (V_{x1}=E_1),
* spadek na (R_1) w kierunku prądu (I_1) (od dołu do góry): (U_{R1}=E_1 - V_a).

Analogicznie dla prawej:

* (V_{x2}=E_2),
* (U_{R2}=E_2 - V_c).

---

Jeśli chcesz, mogę teraz dopisać też **sprawdzenie (kontrola) równań KCL/KVL** oraz **bilans mocy** (\sum P_{\text{źródeł}}=\sum P_{\text{rezystorów}}) w pełnej symbolice.


Jasne. Przyjmuję **prądy oczkowe zgodnie z rysunkiem** (zgodnie ze strzałkami w oczkach 1,2,3), wszystkie **zgodnie z ruchem wskazówek zegara**:

* (I_{(1)}) — oczko **1** (lewe dolne),
* (I_{(2)}) — oczko **2** (prawe dolne),
* (I_{(3)}) — oczko **3** (górne).

Elementy wspólne:

* (R_3) jest wspólne dla oczek 1 i 2,
* (R_4) jest wspólne dla oczek 1 i 3,
* (R_5) jest wspólne dla oczek 2 i 3,
* (R_6) tylko w oczku 3,
* gałąź (R_1)–(E_1) tylko w oczku 1,
* gałąź (R_2)–(E_2) tylko w oczku 2.

Zakładam, że przechodząc w oczku 1 przez źródło (E_1) w górę mamy **wzrost napięcia** (tak jak strzałka przy (E_1)), analogicznie dla (E_2). Wtedy w równaniach oczkowych źródła stoją po prawej stronie jako „wymuszenia”.

---

## 1) Równania oczkowe (KVL)

### Oczko 1 (lewe dolne)

[
R_1 I_{(1)} + R_4\big(I_{(1)}-I_{(3)}\big) + R_3\big(I_{(1)}-I_{(2)}\big)=E_1
]

czyli po zebraniu:
[
(R_1+R_4+R_3)I_{(1)}-R_3 I_{(2)}-R_4 I_{(3)}=E_1
]

### Oczko 2 (prawe dolne)

[
R_2 I_{(2)} + R_5\big(I_{(2)}-I_{(3)}\big) + R_3\big(I_{(2)}-I_{(1)}\big)=E_2
]

czyli:
[
-R_3 I_{(1)}+(R_2+R_5+R_3)I_{(2)}-R_5 I_{(3)}=E_2
]

### Oczko 3 (górne)

[
R_6 I_{(3)} + R_4\big(I_{(3)}-I_{(1)}\big)+R_5\big(I_{(3)}-I_{(2)}\big)=0
]

czyli:
[
-R_4 I_{(1)}-R_5 I_{(2)}+(R_6+R_4+R_5)I_{(3)}=0
]

---

## 2) Rozwiązanie symboliczne prądów oczkowych

Wszystkie trzy prądy mają wspólny mianownik (\Delta):

[
\begin{aligned}
\Delta={}&
R_1R_2R_4+R_1R_2R_5+R_1R_2R_6+
R_1R_3R_4+R_1R_3R_5+R_1R_3R_6\
&+R_1R_4R_5+R_1R_5R_6+
R_2R_3R_4+R_2R_3R_5+R_2R_3R_6\
&+R_2R_4R_5+R_2R_4R_6+
R_3R_4R_6+R_3R_5R_6+R_4R_5R_6.
\end{aligned}
]

### Prąd oczkowy (I_{(1)})

[
\begin{aligned}
I_{(1)}=\frac{1}{\Delta}\Big(
&E_1(R_2R_4+R_2R_5+R_2R_6+R_3R_4+R_3R_5+R_3R_6+R_4R_5+R_5R_6)\
+&E_2(R_3R_4+R_3R_5+R_3R_6+R_4R_5)
\Big).
\end{aligned}
]

### Prąd oczkowy (I_{(2)})

[
\begin{aligned}
I_{(2)}=\frac{1}{\Delta}\Big(
&E_1(R_3R_4+R_3R_5+R_3R_6+R_4R_5)\
+&E_2(R_1R_4+R_1R_5+R_1R_6+R_3R_4+R_3R_5+R_3R_6+R_4R_5+R_4R_6)
\Big).
\end{aligned}
]

### Prąd oczkowy (I_{(3)})

[
\begin{aligned}
I_{(3)}=\frac{1}{\Delta}\Big(
&E_1(R_2R_4+R_3R_4+R_3R_5+R_4R_5)\
+&E_2(R_1R_5+R_3R_4+R_3R_5+R_4R_5)
\Big).
\end{aligned}
]

---

## 3) (Opcjonalnie) Jak z prądów oczkowych dostać prądy w gałęziach z rysunku

Jeśli Twoje prądy gałęziowe są jak na schemacie ((I_4) w (R_4), (I_5) w (R_5), (I_6) w (R_6), (I_3) w (R_3)), to:
[
I_{R1}=I_{(1)},\quad I_{R2}=I_{(2)},\quad
I_{R3}=I_{(1)}-I_{(2)},\quad
I_{R4}=I_{(1)}-I_{(3)},\quad
I_{R5}=I_{(2)}-I_{(3)},\quad
I_{R6}=I_{(3)}.
]

Jeżeli chcesz, dopasuję te znaki **dokładnie** do strzałek (I_1,\dots,I_6) z Twojego rysunku (bo np. (I_4) bywa narysowane w kierunku przeciwnym do (I_{R4})).


Jasne. Przyjmuję **prądy oczkowe zgodnie z rysunkiem** (zgodnie ze strzałkami w oczkach 1,2,3), wszystkie **zgodnie z ruchem wskazówek zegara**:

* (I_{(1)}) — oczko **1** (lewe dolne),
* (I_{(2)}) — oczko **2** (prawe dolne),
* (I_{(3)}) — oczko **3** (górne).

Elementy wspólne:

* (R_3) jest wspólne dla oczek 1 i 2,
* (R_4) jest wspólne dla oczek 1 i 3,
* (R_5) jest wspólne dla oczek 2 i 3,
* (R_6) tylko w oczku 3,
* gałąź (R_1)–(E_1) tylko w oczku 1,
* gałąź (R_2)–(E_2) tylko w oczku 2.

Zakładam, że przechodząc w oczku 1 przez źródło (E_1) w górę mamy **wzrost napięcia** (tak jak strzałka przy (E_1)), analogicznie dla (E_2). Wtedy w równaniach oczkowych źródła stoją po prawej stronie jako „wymuszenia”.

---

## 1) Równania oczkowe (KVL)

### Oczko 1 (lewe dolne)

[
R_1 I_{(1)} + R_4\big(I_{(1)}-I_{(3)}\big) + R_3\big(I_{(1)}-I_{(2)}\big)=E_1
]

czyli po zebraniu:
[
(R_1+R_4+R_3)I_{(1)}-R_3 I_{(2)}-R_4 I_{(3)}=E_1
]

### Oczko 2 (prawe dolne)

[
R_2 I_{(2)} + R_5\big(I_{(2)}-I_{(3)}\big) + R_3\big(I_{(2)}-I_{(1)}\big)=E_2
]

czyli:
[
-R_3 I_{(1)}+(R_2+R_5+R_3)I_{(2)}-R_5 I_{(3)}=E_2
]

### Oczko 3 (górne)

[
R_6 I_{(3)} + R_4\big(I_{(3)}-I_{(1)}\big)+R_5\big(I_{(3)}-I_{(2)}\big)=0
]

czyli:
[
-R_4 I_{(1)}-R_5 I_{(2)}+(R_6+R_4+R_5)I_{(3)}=0
]

---

## 2) Rozwiązanie symboliczne prądów oczkowych

Wszystkie trzy prądy mają wspólny mianownik (\Delta):

[
\begin{aligned}
\Delta={}&
R_1R_2R_4+R_1R_2R_5+R_1R_2R_6+
R_1R_3R_4+R_1R_3R_5+R_1R_3R_6\
&+R_1R_4R_5+R_1R_5R_6+
R_2R_3R_4+R_2R_3R_5+R_2R_3R_6\
&+R_2R_4R_5+R_2R_4R_6+
R_3R_4R_6+R_3R_5R_6+R_4R_5R_6.
\end{aligned}
]

### Prąd oczkowy (I_{(1)})

[
\begin{aligned}
I_{(1)}=\frac{1}{\Delta}\Big(
&E_1(R_2R_4+R_2R_5+R_2R_6+R_3R_4+R_3R_5+R_3R_6+R_4R_5+R_5R_6)\
+&E_2(R_3R_4+R_3R_5+R_3R_6+R_4R_5)
\Big).
\end{aligned}
]

### Prąd oczkowy (I_{(2)})

[
\begin{aligned}
I_{(2)}=\frac{1}{\Delta}\Big(
&E_1(R_3R_4+R_3R_5+R_3R_6+R_4R_5)\
+&E_2(R_1R_4+R_1R_5+R_1R_6+R_3R_4+R_3R_5+R_3R_6+R_4R_5+R_4R_6)
\Big).
\end{aligned}
]

### Prąd oczkowy (I_{(3)})

[
\begin{aligned}
I_{(3)}=\frac{1}{\Delta}\Big(
&E_1(R_2R_4+R_3R_4+R_3R_5+R_4R_5)\
+&E_2(R_1R_5+R_3R_4+R_3R_5+R_4R_5)
\Big).
\end{aligned}
]

---

## 3) (Opcjonalnie) Jak z prądów oczkowych dostać prądy w gałęziach z rysunku

Jeśli Twoje prądy gałęziowe są jak na schemacie ((I_4) w (R_4), (I_5) w (R_5), (I_6) w (R_6), (I_3) w (R_3)), to:
[
I_{R1}=I_{(1)},\quad I_{R2}=I_{(2)},\quad
I_{R3}=I_{(1)}-I_{(2)},\quad
I_{R4}=I_{(1)}-I_{(3)},\quad
I_{R5}=I_{(2)}-I_{(3)},\quad
I_{R6}=I_{(3)}.
]

Jeżeli chcesz, dopasuję te znaki **dokładnie** do strzałek (I_1,\dots,I_6) z Twojego rysunku (bo np. (I_4) bywa narysowane w kierunku przeciwnym do (I_{R4})).
