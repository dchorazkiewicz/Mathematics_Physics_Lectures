# Lista 5 – Elektromagnetyzm I: Pole i siły

---


## Zadanie 1 – Potencjał i energia

Dla ładunku punktowego $q = 4\ \mu\mathrm{C}$

1. Oblicz potencjał w $r = 0.3\ \mathrm{m}$.
2. Oblicz różnicę potencjałów między $0.3\,\mathrm{m}$ i $0.6\,\mathrm{m}$.
3. Oblicz pracę przeniesienia ładunku próbnego $q_0 = 2\,\mu\mathrm{C}$.
4. Oblicz natężenie pola z pochodnej potencjału.
5. Porównaj z prawem Coulomba.

---

## Zadanie 2 – Siła Coulomba

Dane są dwa ładunki punktowe:

$$q_1 = 3\ \mu\mathrm{C}, \quad q_2 = -5\ \mu\mathrm{C}$$

zlokalizowane w punktach:

$$r_1 = (0,0), \quad r_2 = (0.4, 0.3)\,\mathrm{m}$$

1. Wyznacz wektor siły działającej na $q_2$.
2. Oblicz jej wartość.
3. Wyznacz energię potencjalną układu.
4. Oblicz pracę potrzebną do rozdzielenia ładunków na odległość $2\,\mathrm{m}$.

---

## Zadanie 3 – Pole w punkcie od układu ładunków

Dane są dwa ładunki punktowe:

* $+q\  \text{w punkcie}\  (-a, 0)$
* $+2q\  \text{w punkcie}\  (a, 0)$

Odpowiedz na następujące pytania:

1. Wyznacz wektor pola $\vec E(0, y)$, $\vec E(x, 0)$ oraz ogólnie $\vec E(x, y)$.
2. Wyznacz warunek, dla którego składowe $E_x = 0$, $E_y = 0$ oraz zero pola $\vec E = 0$.
3. Oblicz pole dla: $a = 0.2\,\mathrm{m}$, $y = 0.3\,\mathrm{m}$, $q = 2\,\mu\mathrm{C}$.
4. Zbadaj granicę $y \gg a$.
5. Czy istnieje punkt zerowego pola na osi $y$?

---

## Zadanie 4 – Ruch cząstki w jednorodnym polu

Dane są następujące warunki początkowe

* $m = 0.02\ \mathrm{kg}$
* $q = 1\ \mathrm{mC}$
* $\vec E = (30, 100)\,\mathrm{N/C}$
* $\vec v(0) = (20, 0)\,\mathrm{m/s}$
* $\vec r(0) = (0, 0)$

Dla nich 

1. Napisz równania ruchu i rozwiąż je analitycznie.
2. Narysuj trajektorię ruchu.
3. Oblicz czas osiągnięcia prędkości pionowej $50\,\mathrm{m/s}$.
4. Oblicz energię kinetyczną po $t = 0.05\,\mathrm{s}$.
5. Sprawdź zgodność z bilansem energii.

---

## Zadanie 5 – Kondensator: energia i siła

Mamy kondensator płaski:

* $S = 0.02\,\mathrm{m^2}$
* $d = 5\,\mathrm{mm}$
* $U = 500\,\mathrm{V}$

Odpowiedz na następujące pytania:

1. Oblicz pojemność.
2. Oblicz energię zgromadzoną w kondensatorze.
3. Oblicz natężenie pola między okładkami.
4. Oblicz gęstość energii pola.
5. Oblicz siłę przyciągania między okładkami.


---

## Zadanie 6 – Mapa pola w 2D

Układ: trzy dowolne ładunki w płaszczyźnie.

1. Zaimplementuj funkcję obliczającą wektor pola $\vac E(x, y)$.
2. Wygeneruj mapę wektorową pola.
3. Znajdź numerycznie punkt równowagi.
4. Zbadaj stabilność punktu równowagi (małe przesunięcie).
5. Porównaj z przypadkiem dwóch ładunków.

Wymaganie: wizualizacja HTML z możliwością zmiany położenia ładunków.

---

## Zadanie 7 – Ruch w polu centralnym

Mamy pole:

$$
E(r) = k \frac{Q}{r^2} \hat r
$$

1. Zapisz równanie ruchu cząstki.
2. Rozważ przypadek ruchu radialnego.
3. Zaimplementuj metodę RK4.
4. Zbadaj przypadek energii dodatniej i ujemnej.
5. Porównaj z analogią grawitacyjną.

Wymaganie: animacja toru ruchu.

---

## Zadanie 8 – Energia układu trzech ładunków

1. Zapisz energię całkowitą układu.
2. Oblicz energię dla konfiguracji trójkąta równobocznego.
3. Zbadaj zmianę energii przy zmianie znaku jednego ładunku.
4. Znajdź konfigurację minimalnej energii (numerycznie).
5. Zinterpretuj stabilność układu.

---

## Zadanie 9 – Dipol w zewnętrznym polu

Dipol w jednorodnym polu $E_0$.

1. Wyprowadź wzór na moment siły działający na dipol.
2. Oblicz energię potencjalną dipola.
3. Wyznacz równanie ruchu kątowego.
4. Zlinearyzuj równanie dla małych wychyleń.
5. Zinterpretuj układ jako oscylator harmoniczny.

---

## Zadanie 10 – Strumień pola (weryfikacja prawa Gaussa)

1. Zdefiniuj strumień pola elektrycznego.
2. Rozważ sferę wokół ładunku punktowego.
3. Zaimplementuj dyskretną aproksymację strumienia.
4. Zbadaj zależność od liczby punktów siatki.
5. Porównaj z wynikiem analitycznym.
