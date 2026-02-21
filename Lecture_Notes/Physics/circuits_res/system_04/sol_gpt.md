Oto uporządkowana **notatka podsumowująca analizę układu** wraz ze sprawdzeniem zgodności rysunku z prawami obwodów.

---

# 📘 Analiza obwodu prądu stałego $U = 60 V$

## 1️⃣ Struktura układu

Układ składa się z:

* Źródła napięcia:
  $$
  U = 60\text{ V}
  $$

* Czterech rezystorów:
  $$
  R_1=2\Omega,\quad R_2=4\Omega,\quad R_3=12\Omega,\quad R_4=16\Omega
  $$

Topologia:

* $R_1$ i $R_2$ — połączenie **szeregowe**
* Gałąź ($R_1+R_2$) jest **równoległa** do $R_3$
* Rezystor $R_4$ jest **szeregowo** z całym blokiem równoległym

Schemat odpowiada strukturze:

$$
R_4 + \big[ (R_1+R_2) \parallel R_3 \big]
$$

---

## 2️⃣ Obliczenie rezystancji zastępczej

Najpierw:

$$
R_{12}=R_1+R_2=2+4=6\Omega
$$

Połączenie równoległe:

$$
R_{123}=\frac{R_{12}R_3}{R_{12}+R_3}
=\frac{6\cdot12}{6+12}
=\frac{72}{18}
=4\Omega
$$

Całkowita rezystancja:

$$
R_{eq}=R_{123}+R_4=4+16=20\Omega
$$

---

## 3️⃣ Prąd całkowity

Z prawa Ohma:

$$
I=\frac{U}{R_{eq}}=\frac{60}{20}=3\text{ A}
$$

Zatem rysunek poprawnie pokazuje **3 A w gałęzi głównej**.

---

## 4️⃣ Rozkład prądów w rozgałęzieniu

Spadek napięcia na $R_4$:

$$
U_4=I R_4=3\cdot16=48\text{ V}
$$

Napięcie na bloku równoległym:

$$
U_{123}=60-48=12\text{ V}
$$

Prądy w gałęziach:

$$
I_{12}=\frac{12}{6}=2\text{ A}
$$
$$
I_3=\frac{12}{12}=1\text{ A}
$$

Sprawdzenie KCL:

$$
I_{12}+I_3=2+1=3\text{ A}=I
$$

Zgadza się.

---

## 5️⃣ Spadki napięć na elementach

$$
U_1=2\cdot2=4\text{ V}
$$
$$
U_2=2\cdot4=8\text{ V}
$$
$$
U_3=1\cdot12=12\text{ V}
$$
$$
U_4=3\cdot16=48\text{ V}
$$

Kontrola:

* Gałęzie równoległe:
  $$
  U_1+U_2=4+8=12\text{ V}=U_3
  $$
* Cała pętla:
  $$
  48+12=60\text{ V}
  $$

---

# ✅ Czy rysunek opisuje rzeczywisty układ?

Tak — układ jest **fizycznie spójny** i zgodny z prawami:

### ✔ I prawo Kirchhoffa (węzłowe)

Suma prądów w węźle się zgadza.

### ✔ II prawo Kirchhoffa (oczka)

Suma spadków napięć równa napięciu źródła.

### ✔ Prawo Ohma

Wszystkie spadki napięć są zgodne z obliczonymi prądami.

### ✔ Bilans mocy

Moc źródła:
$$
P=UI=60\cdot3=180\text{ W}
$$

Moc na rezystorach:

$$
P_1=8\text{ W},\quad
P_2=16\text{ W},\quad
P_3=12\text{ W},\quad
P_4=144\text{ W}
$$

Suma:
$$
8+16+12+144=180\text{ W}
$$

Zgadza się.

---

# 🎯 Wniosek końcowy

Rysunek:

* poprawnie przedstawia topologię układu,
* poprawnie pokazuje wartość prądu 3 A,
* jest w pełni zgodny z prawami Kirchhoffa,
* opisuje rzeczywisty, fizycznie możliwy obwód.

---

Jeśli chcesz, mogę przygotować teraz:

* 📄 wersję dydaktyczną do pokazania studentom,
* 📊 wersję skróconą „na jedną stronę A4”,
* 📐 analizę metodą węzłową w jednym równaniu,
* 📎 wersję LaTeX (PDF-ready).
