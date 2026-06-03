# Lista 10 – Fizyka relatywistyczna

---

## Zadanie 1 – Dylatacja czasu

Statek kosmiczny porusza się z prędkością:

$$
v = 0.8c
$$

1. Oblicz czynnik Lorentza:
   $$
   \gamma = \frac{1}{\sqrt{1-\frac{v^2}{c^2}}}
   $$
2. Ile czasu upłynie na Ziemi, jeśli na statku minie 5 lat?
3. Jaki procentowo jest efekt dylatacji?
4. Co dzieje się w granicy $v \to c$?
5. Zinterpretuj wynik fizycznie.

---

## Zadanie 2 – Kontrakcja długości

Rakieta o długości własnej:

$$
L_0 = 120\,\mathrm{m}
$$

porusza się z prędkością $0.6c$.

1. Oblicz długość obserwowaną przez nieruchomego obserwatora:
   $$
   L = \frac{L_0}{\gamma}
   $$
2. Jaki jest procent skrócenia?
3. Czy obserwator w rakiecie widzi skrócenie?
4. Co jest wielkością niezmienniczą?
5. Zinterpretuj paradoks „rakieta w tunelu”.

---

## Zadanie 3 – Transformacja Lorentza

Dane zdarzenia w układzie $S$:

$$
x_1 = 0, \quad t_1 = 0
$$

$$
x_2 = 900\,\mathrm{m}, \quad t_2 = 4\,\mu\mathrm{s}
$$

Układ $S'$ porusza się z prędkością $v=0.6c$.

1. Zastosuj transformację:
   $$
   x' = \gamma (x - vt)
   $$
   $$
   t' = \gamma \left(t - \frac{vx}{c^2}\right)
   $$
2. Oblicz współrzędne drugiego zdarzenia w $S'$.
3. Czy kolejność zdarzeń może się zmienić?
4. Oblicz interwał czasoprzestrzenny:
   $$
   s^2 = c^2 t^2 - x^2
   $$
5. Sprawdź jego niezmienniczość.

---

## Zadanie 4 – Paradoks bliźniąt

Bliźniak A pozostaje na Ziemi.
Bliźniak B leci z prędkością $0.9c$ przez 10 lat (czas ziemski) i wraca.

1. Oblicz czas własny bliźniaka B.
2. O ile lat młodszy wraca?
3. Czy symetria układów odniesienia jest pełna?
4. Wskaż moment złamania symetrii.
5. Zinterpretuj w języku czasoprzestrzeni Minkowskiego.

---

## Zadanie 5 – Miony w atmosferze

Miony powstają na wysokości 10 km.

Czas życia własny:

$$
\tau_0 = 2.2\,\mu\mathrm{s}
$$

Prędkość:

$$
v = 0.995c
$$

1. Oblicz czynnik Lorentza.
2. Oblicz średni czas życia w układzie Ziemi:
   $$
   \tau = \gamma \tau_0
   $$
3. Jaką drogę średnio przebywa mion?
4. Czy bez relatywistyki dotarłby do powierzchni?

---


## Zadanie 6 – Diagram Minkowskiego (HTML obowiązkowo)

1. Zaimplementuj transformację Lorentza jako macierz.
2. Narysuj osie $ct$ i $x$.
3. Narysuj osie $ct'$ i $x'$.
4. Zaznacz stożek świetlny.
5. Umożliw zmianę prędkości suwakiem.
6. Zinterpretuj geometrycznie dylatację czasu i kontrakcję długości.

---

## Zadanie 7 – Relatywistyczna energia i pęd

$$
E = \gamma mc^2
$$

$$
p = \gamma mv
$$

1. Oblicz energię całkowitą elektronu dla $v=0.95c$.
2. Oblicz energię kinetyczną:
   $$
   E_k = (\gamma-1)mc^2
   $$
3. Porównaj z wynikiem klasycznym $\frac12 mv^2$.
4. Zbadaj granicę $v \ll c$.
5. Zinterpretuj relację:
   $$
   E^2 = p^2 c^2 + m^2 c^4
   $$

---

## Zadanie 8 – Grawitacyjne przesunięcie ku czerwieni

Przybliżenie (słabe pole):

$$
\frac{\Delta f}{f} \approx \frac{\Delta \Phi}{c^2}
$$

1. Wyprowadź przesunięcie dla powierzchni Ziemi.
2. Oblicz względną zmianę częstotliwości.
3. Zinterpretuj jako dylatację czasu grawitacyjnego.
4. Oszacuj efekt dla gwiazdy neutronowej.
5. Porównaj rząd wielkości z eksperymentami laboratoryjnymi.

---

## Zadanie 9 – Promień Schwarzschilda

$$
r_s = \frac{2GM}{c^2}
$$

1. Oblicz $r_s$ dla masy Słońca.
2. Oblicz $r_s$ dla Ziemi.
3. Oblicz przesunięcie ku czerwieni przy $r=1.5r_s$.
4. Co dzieje się przy $r \to r_s$?
5. Zinterpretuj horyzont zdarzeń.

---

## Zadanie 10 – Numeryczna symulacja ruchu relatywistycznego

Relatywistyczne równanie ruchu:

$$
\frac{d}{dt}(\gamma m v) = F
$$

1. Zaimplementuj metodę RK4.
2. Porównaj ruch przy stałej sile w modelu klasycznym i relatywistycznym.
3. Zbadaj asymptotyczne zbliżanie się do $c$.
4. Wykonaj wykres $v(t)$ i $x(t)$ dla obu modeli.
5. Oceń różnice energetyczne między modelami.
