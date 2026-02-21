Na rysunku widoczny jest **dwuwęzłowy obwód prądu stałego** z dwoma źródłami napięcia i trzema rezystorami, tworzący układ dwóch oczek połączonych wspólną gałęzią środkową.

---

## 🔎 1. Struktura topologiczna układu

Układ składa się z:

* **dwóch oczek (mesh 1 i mesh 2)**,
* **jednego górnego węzła „a”**,
* **jednego dolnego węzła wspólnego (masa / punkt odniesienia)**,
* **trzech gałęzi rezystancyjnych**,
* **dwóch idealnych źródeł napięcia**.

---

## ⚡ 2. Elementy aktywne – źródła napięcia

### 🔹 Źródło po lewej stronie: ( E_1 )

* Umieszczone w lewej pionowej gałęzi.
* Strzałka skierowana **do góry** oznacza przyjęty zwrot napięcia źródła.
* Zasila lewe oczko (oznaczone „1”).

### 🔹 Źródło po prawej stronie: ( E_2 )

* Umieszczone w prawej pionowej gałęzi.
* Strzałka również skierowana **do góry**.
* Zasila prawe oczko (oznaczone „2”).

Źródła te wymuszają różnicę potencjałów między dolnym a górnym węzłem po swoich stronach.

---

## 🔧 3. Elementy pasywne – rezystory

### 🔹 ( R_1 )

* Górna lewa gałąź pozioma.
* Łączy lewy górny punkt z węzłem „a”.
* Płynie przez niego prąd ( I_1 ) (skierowany w prawo).
* Oznaczone napięcie: ( U_1 ) (strzałka w lewo – przyjęta polaryzacja napięcia).

---

### 🔹 ( R_2 )

* Górna prawa gałąź pozioma.
* Łączy prawy górny punkt z węzłem „a”.
* Płynie przez niego prąd ( I_2 ) (skierowany w lewo).
* Oznaczone napięcie: ( U_2 ) (strzałka w prawo).

---

### 🔹 ( R_3 )

* Gałąź środkowa pionowa.
* Łączy węzeł „a” z dolnym węzłem (wspólnym).
* Płynie przez niego prąd ( I_3 ) (skierowany w dół).
* Oznaczone napięcie: ( U_3 ) (strzałka w górę).

---

## 🔵 4. Węzły

### 🔹 Węzeł „a” (górny centralny)

To punkt połączenia trzech gałęzi:

* ( R_1 )
* ( R_2 )
* ( R_3 )

Spełnia I prawo Kirchhoffa:

[
I_1 + I_2 = I_3
]
(przy przyjętych zwrotach prądów)

---

### 🔹 Dolny węzeł

* Wspólny punkt odniesienia (można traktować jako masę).
* Łączy dolne końce:

  * źródła ( E_1 )
  * źródła ( E_2 )
  * rezystora ( R_3 )

---

## 🔁 5. Oczka prądowe

Na rysunku zaznaczono dwa oczka:

### 🔹 Oczko 1 (lewe)

Obejmuje:

* źródło ( E_1 )
* rezystor ( R_1 )
* rezystor ( R_3 )

Kierunek obiegu – przeciwnie do ruchu wskazówek zegara.

---

### 🔹 Oczko 2 (prawe)

Obejmuje:

* źródło ( E_2 )
* rezystor ( R_2 )
* rezystor ( R_3 )

Kierunek obiegu – zgodnie z ruchem wskazówek zegara.

---

## 📌 6. Charakter fizyczny układu

Układ jest:

* liniowy (rezystory idealne),
* stacjonarny (DC),
* dwupętlowy,
* posiada jedną gałąź wspólną (R3),
* można analizować:

  * metodą oczkową,
  * metodą węzłową,
  * przez prawa Kirchhoffa,
  * przez twierdzenie Thévenina/Nortona.

---

## 🧠 7. Interpretacja fizyczna

* Źródła ( E_1 ) i ( E_2 ) mogą mieć różne wartości → powodują przepływ prądu przez gałąź środkową.
* Rezystor ( R_3 ) jest elementem sprzęgającym oba oczka.
* Jeśli ( E_1 = E_2 ) i ( R_1 = R_2 ), układ jest symetryczny.
* W przeciwnym przypadku pojawia się różnica potencjałów w węźle „a”.

---

Jeżeli chcesz, mogę teraz:

* 🔹 zapisać równania węzłowe,
* 🔹 zapisać równania oczkowe,
* 🔹 wyprowadzić postać macierzową,
* 🔹 policzyć napięcie węzła „a”,
* 🔹 wyznaczyć warunki symetrii,
* 🔹 przygotować wersję LaTeX/Markdown do materiałów dydaktycznych.


Przyjmuję zwroty prądów dokładnie jak na rysunku:

* (I_1): przez (R_1) **z lewej do węzła (a)** (w prawo),
* (I_2): przez (R_2) **z prawej do węzła (a)** (w lewo),
* (I_3): przez (R_3) **z węzła (a) w dół**,
* dolny przewód to węzeł odniesienia (0 V),
* źródła (E_1, E_2) mają zwrot napięcia „do góry” (górny zacisk jest o (E) wyżej od dolnego).

---

## 1) Równania Kirchhoffa

### I prawo Kirchhoffa (KCL) w węźle (a)

[
I_1 + I_2 - I_3 = 0
]

### II prawo Kirchhoffa (KVL) — oczko lewe

Idziemy: dół (\to) przez (E_1) do góry (\to) przez (R_1) do węzła (a) (\to) przez (R_3) w dół:
[
E_1 - R_1 I_1 - R_3 I_3 = 0
]

### II prawo Kirchhoffa (KVL) — oczko prawe

Analogicznie: dół (\to) przez (E_2) (\to) przez (R_2) (zgodnie z (I_2) od prawej do (a)) (\to) przez (R_3) w dół:
[
E_2 - R_2 I_2 - R_3 I_3 = 0
]

Mamy więc układ 3 równań:
[
\begin{cases}
I_1 + I_2 - I_3 = 0 \
E_1 - R_1 I_1 - R_3 I_3 = 0 \
E_2 - R_2 I_2 - R_3 I_3 = 0
\end{cases}
]

---

## 2) Rozwiązanie symboliczne

Z równań oczkowych:
[
I_1=\frac{E_1 - R_3 I_3}{R_1},
\qquad
I_2=\frac{E_2 - R_3 I_3}{R_2}
]

Podstawiamy do KCL (I_1+I_2=I_3):
[
\frac{E_1 - R_3 I_3}{R_1}+\frac{E_2 - R_3 I_3}{R_2}=I_3
]

Po uporządkowaniu:
[
\frac{E_1}{R_1}+\frac{E_2}{R_2}
===============================

I_3!\left(1+\frac{R_3}{R_1}+\frac{R_3}{R_2}\right)
]

Wygodnie wprowadzić
[
D = R_1R_2 + R_1R_3 + R_2R_3
]

Wtedy:

### Prąd w gałęzi środkowej

[
I_3=\frac{E_1R_2+E_2R_1}{D}
]

### Prąd przez (R_1)

[
I_1=\frac{E_1(R_2+R_3)-E_2R_3}{D}
]

### Prąd przez (R_2)

[
I_2=\frac{E_2(R_1+R_3)-E_1R_3}{D}
]

Łatwo sprawdzić, że spełniają (I_1+I_2=I_3).

---

## 3) Napięcia na rezystorach i napięcie węzła (a)

Z prawa Ohma:
[
U_1 = R_1 I_1,\quad U_2 = R_2 I_2,\quad U_3 = R_3 I_3
]

Ponieważ dolny węzeł ma 0 V, a (R_3) jest między (a) i dołem:
[
V_a = U_3 = R_3 I_3
]

czyli:
[
V_a=\frac{R_3(E_1R_2+E_2R_1)}{D}
]

Jeśli chcesz, mogę też rozpisać to samo metodą węzłową (jedno równanie dla (V_a)) i pokazać pełne przekształcenia krok po kroku.


To, że **dolny węzeł ma 0 V**, nie wynika z fizyki układu, tylko z **wyboru punktu odniesienia**.

Jest to decyzja czysto umowna, wynikająca z definicji napięcia.

---

## 1️⃣ Napięcie jest wielkością względną

Napięcie definiujemy jako różnicę potencjałów:

[
U_{AB} = V_A - V_B
]

Nie istnieje „bezwzględny potencjał” w klasycznej teorii obwodów — zawsze mierzymy różnicę między dwoma punktami.

Dlatego jeden punkt **możemy wybrać dowolnie jako poziom odniesienia (masę)** i przypisać mu:

[
V_{\text{ref}} = 0
]

---

## 2️⃣ Dlaczego wybiera się dolny węzeł?

W tym układzie dolny przewód:

* łączy dolne zaciski obu źródeł,
* łączy dolny koniec rezystora (R_3),
* jest wspólny dla całego obwodu,
* stanowi naturalny węzeł odniesienia.

W analizie węzłowej zawsze wybieramy:

* węzeł o największej liczbie połączeń,
* często wspólną „szynę powrotną”,
* punkt najwygodniejszy rachunkowo.

Tutaj dolny węzeł spełnia wszystkie te kryteria.

---

## 3️⃣ Co by było, gdybyśmy wybrali inny węzeł?

Gdybyśmy przyjęli np. (V_a = 0), wtedy:

* wszystkie potencjały przesunęłyby się o stałą wartość,
* prądy w obwodzie pozostałyby identyczne,
* różnice napięć byłyby takie same.

Dodanie stałej (C) do wszystkich potencjałów:

[
V_i' = V_i + C
]

nie zmienia żadnego napięcia między punktami, bo:

[
V_i' - V_j' = (V_i + C) - (V_j + C) = V_i - V_j
]

To oznacza, że układ równań Kirchhoffa jest **niezmienniczy względem przesunięcia potencjału o stałą**.

---

## 4️⃣ Interpretacja fizyczna

Można to porównać do:

* wyboru poziomu „0 m” w geodezji,
* wyboru poziomu energii potencjalnej w mechanice.

Nie ma znaczenia, gdzie ustawimy zero — liczą się różnice wysokości.

---

## 5️⃣ Znaczenie matematyczne

W metodzie węzłowej liczba równań wynosi:

[
N_{\text{węzłów}} - 1
]

Odejmujemy jeden, ponieważ jeden potencjał wybieramy jako odniesienie.

W tym układzie są dwa węzły:

* węzeł (a),
* dolny węzeł.

Dlatego wystarczy jedno równanie węzłowe — dla (V_a).

---

## 6️⃣ Podsumowanie

Dolny węzeł ma 0 V, ponieważ:

* napięcie jest definiowane jako różnica potencjałów,
* jeden potencjał musi zostać przyjęty jako odniesienie,
* wybieramy punkt najwygodniejszy obliczeniowo,
* wybór ten nie wpływa na prądy ani napięcia między elementami.

Jeżeli chcesz, mogę pokazać formalnie, że macierz przewodności układu jest osobliwa przed ustaleniem węzła odniesienia — to ładnie pokazuje, dlaczego trzeba „ustalić zero”.


