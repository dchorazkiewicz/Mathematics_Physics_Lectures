# Lista 8 – Statystyka i pomiary

---

## Zadanie 1 – Statystyka opisowa serii pomiarowej

Dane są pomiary długości pręta (w cm):

$$
x = [12.10,\ 12.08,\ 12.12,\ 12.11,\ 12.09,\ 12.13,\ 12.07,\ 12.10]
$$

1. Oblicz średnią arytmetyczną $\bar{x}$.
2. Oblicz wariancję i odchylenie standardowe próby $s$.
3. Oblicz niepewność średniej:
   $$
   u(\bar{x}) = \frac{s}{\sqrt{n}}
   $$
4. Podaj wynik w formacie:
   $$
   x = \bar{x} \pm u(\bar{x})
   $$
5. Wyjaśnij różnicę między odchyleniem standardowym $s$ a niepewnością średniej $u(\bar{x})$.
6. Zakładając rozkład normalny, oblicz przedziały:
    - $\bar{x} \pm s$
    - $\bar{x} \pm 2s$
    - $\bar{x} \pm 3s$
   i zinterpretuj je jako poziomy ufności (68–95–99).

---

## Zadanie 2 – Propagacja niepewności metodą różniczki zupełnej (opór z prawa Ohma)

Opór wyznaczany jest z pomiarów napięcia i prądu:

$$
R = \frac{U}{I}
$$

Dane:

$$
U = 5.23 \pm 0.04\ \mathrm{V}
$$

$$
I = 0.482 \pm 0.006\ \mathrm{A}
$$

1. Oblicz wartość oporu $R$.
2. Wyprowadź wzór na niepewność względną metodą różniczki zupełnej.
3. Oblicz niepewność względną $\frac{u(R)}{R}$ i wskaż, który pomiar (U czy I) dominuje niepewność.

---

## Zadanie 3 – Propagacja niepewności (gęstość)

Gęstość prostopadłościanu:

$$
\rho = \frac{m}{abc}
$$

Dane:

$$
m = 128.4 \pm 0.2\ \mathrm{g}
$$

$$
a = 5.20 \pm 0.02\ \mathrm{cm}
$$

$$
b = 2.10 \pm 0.02\ \mathrm{cm}
$$

$$
c = 1.50 \pm 0.01\ \mathrm{cm}
$$

1. Oblicz wartość $\rho$.
2. Wyprowadź wzór na niepewność względną metodą różniczki zupełnej.
3. Wskaż, który pomiar daje największy wkład do niepewności.

---

## Zadanie 4 – Regresja liniowa i wyznaczenie przyspieszenia ziemskiego (estymacja parametru)

Model swobodnego spadku:

$$
h = \frac{1}{2} g t^2
$$

Dane:

$$
h\ [\mathrm{m}] = [0.20,\ 0.40,\ 0.60,\ 0.80,\ 1.00]
$$

$$
t\ [\mathrm{s}] = [0.202,\ 0.287,\ 0.351,\ 0.404,\ 0.452]
$$

1. Przekształć model do postaci liniowej:
   $$
   h = k t^2
   $$
2. Wykonaj regresję liniową $h$ względem $t^2$.
3. Wyznacz $g$.
4. Oszacuj niepewność $u(g)$.
5. Oceń jakość dopasowania (analiza reszt lub współczynnik determinacji $R^2$).

---

## Zadanie 5 – Błędy systematyczne vs statystyczne

Trzy grupy studentów mierzy długość tego samego pręta.

Otrzymano wyniki:

Grupa A:
$$
x = [10.01,\ 9.99,\ 10.02,\ 9.98,\ 10.00]
$$

Grupa B:
$$
x = [10.42,\ 10.40,\ 10.41,\ 10.43,\ 10.39]
$$

Grupa C:
$$
x = [9.6,\ 10.5,\ 10.2,\ 9.8,\ 10.4]
$$

1. Dla każdej grupy oblicz:
    - średnią,
    - odchylenie standardowe,
    - niepewność średniej.
2. Załóż, że prawdziwa wartość wynosi:
   $$
   x_{\mathrm{true}} = 10.00
   $$
   Porównaj wyniki grup z wartością prawdziwą.
3. Określ dla każdej grupy:
    - czy dominuje błąd statystyczny,
    - czy występuje błąd systematyczny.
4. Zaproponuj możliwe przyczyny błędu systematycznego (min. 2).
5. Wyjaśnij, dlaczego zwiększenie liczby pomiarów nie usuwa błędu systematycznego.
6. (Refleksja) Czy wynik:
   
   $$
   x = 10.41 \pm 0.01
   $$
   jest „lepszy” niż:
   $$
   x = 10.00 \pm 0.20
   $$
   Uzasadnij.

Odpowiedź: obliczenia + interpretacja.

---

## Zadanie 6 (HTML) – Centralne Twierdzenie Graniczne

Zbuduj aplikację symulującą rozkład średniej z próby.

Wymagania:

1. Wybór rozkładu źródłowego (jednostajny / wykładniczy / dwupunktowy / normalny).
2. Ustawianie liczebności próby $n$ i liczby prób $N$.
3. Generowanie $N$ średnich $\bar{x}$.
4. Histogram rozkładu $\bar{x}$.
5. Porównanie empirycznego odchylenia z wartością teoretyczną $\sigma/\sqrt{n}$.
6. Możliwość nałożenia krzywej Gaussa.
7. Krótka analiza wpływu $n$ na kształt rozkładu.

Do oddania: plik HTML + opis wniosków.

---

## Zadanie 7 (HTML) – Wahadło matematyczne: pomiar $g$

Chcemy zbudować aplikację do pomiaru przyspieszenia ziemskiego $g$ za pomocą wahadła matematycznego, mierząc okres drgań.

$$
g=4\pi^2 \frac{L}{T^2}
$$

Wymagania aplikacji

1. Użytkownik ustawia długość $L$ i jej niepewność $u(L)$.
2. Pierwsze naciśnięcie spacji uruchamia ruch i stoper.
3. Kolejne naciśnięcia rejestrują kolejne przejścia przez minimum.
4. Aplikacja zapisuje czasy $t_i$ i wyznacza okresy:
   $$
   T_i = t_{i+1} - t_i
   $$
5. Oblicz:
    - średni okres $\bar{T}$,
    - odchylenie standardowe $s_T$,
    - niepewność średniej:
     $$
     u(T) = \frac{s_T}{\sqrt{n}}
     $$
6. Wyznacz:
   $$
   g = 4\pi^2 \frac{L}{\bar{T}^2}
   $$
7. Zastosuj propagację niepewności:
   $$
   u(g)=\sqrt{\left(\frac{\partial g}{\partial L}u(L)\right)^2+
   \left(\frac{\partial g}{\partial T}u(T)\right)^2}
   $$
8. Wyświetl wynik:
   $$
   g = \hat{g} \pm u(g)
   $$
   oraz procentowe wkłady niepewności od $L$ i od $T$.

Do oddania: plik HTML + raport z min. 5 okresów.

---

## Zadanie 8 (HTML) – Oscylator masa–sprężyna: pomiar częstotliwości i wyznaczenie $k$

Chcemy zbudować aplikację do wyznaczania stałej sprężystości $k$ za pomocą pomiaru okresu drgań układu masa–sprężyna.

$$
k = 4\pi^2 \frac{m}{T^2}
$$

Wymagania aplikacji:

1. Użytkownik ustawia masę $m$ i jej niepewność $u(m)$.
2. Pierwsze naciśnięcie spacji uruchamia ruch i stoper.
3. Kolejne naciśnięcia rejestrują kolejne przejścia przez minimum.
4. Aplikacja wyznacza:
   - okresy $T_i$,
   - średni okres $\bar{T}$,
   - $s_T$,
   - $u(T) = \frac{s_T}{\sqrt{n}}$
5. Wyznacz częstotliwość:
   $$
   f = \frac{1}{\bar{T}}
   $$
   oraz jej niepewność:
   $$
   u(f) = \frac{u(T)}{\bar{T}^2}
   $$
6. Wyznacz stałą sprężyny:
   $$
   k = 4\pi^2 \frac{m}{\bar{T}^2}
   $$
7. Zastosuj propagację niepewności:
   $$
   u(k)=\sqrt{\left(\frac{\partial k}{\partial m}u(m)\right)^2+
   \left(\frac{\partial k}{\partial T}u(T)\right)^2}
   $$
8. Wyświetl wynik:
   $$
   k = \hat{k} \pm u(k)
   $$
   oraz procentowe wkłady niepewności od $m$ i od $T$.

Do oddania: plik HTML + raport z min. 10 okresów.
