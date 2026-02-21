Przyjmuję **prądy oczkowe zgodnie z rysunkiem** (zgodnie ze strzałkami w oczkach 1,2,3), wszystkie **zgodnie z ruchem wskazówek zegara**:

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

