# Lista 1 – Matematyczne podstawy

---

## Zadanie 1 – Wektory i przekształcenia liniowe

Proszę wypisać wszystkie kroki obliczeń a nie same wyniki.

**Dane są dwa wektory w przestrzeni trójwymiarowej:**

$$
\vec a = (2,-1,3), \qquad
\vec b = (1,4,-2)
$$

* Oblicz długości wektorów $|\vec a|$, $|\vec b|$.
* Wyznacz wektor znormalizowany $\hat a = \frac{\vec a}{|\vec a|}$.
* Oblicz iloczyn skalarny $\vec a \cdot \vec b$ oraz kąt między wektorami.
* Oblicz iloczyn wektorowy $\vec a \times \vec b$ i pole równoległoboku rozpiętego na tych wektorach.

**Dla macierzy:**

$$
A =
\begin{pmatrix}
2 & 1 & 0 \\
0 & 1 & -1 \\
1 & 0 & 1
\end{pmatrix}
$$

* Oblicz $A\vec a$.
* Oblicz $\det A$.
* Sprawdź, czy przekształcenie zachowuje orientację przestrzeni.

---

## Zadanie 2 – Tor parametryczny, prędkość i przyspieszenie

Proszę wypisać wszystkie kroki obliczeń a nie same wyniki. Proszę narysować wykres toru i wektorów prędkości oraz przyspieszenia w wybranych punktach.

Dane jest równanie parametryczne toru:

$$
\vec r(t) = \bigl(t^2,\sin t, 5\bigr)
$$

* Wyznacz prędkość
   $$
   \vec v(t) = \frac{d\vec r}{dt}
   $$
* Wyznacz przyspieszenie
   $$
   \vec a(t) = \frac{d^2 \vec r}{dt^2}
   $$
* Oblicz $|\vec v(1)|$.
* Oblicz $\vec v \cdot \vec a$.
* Oblicz $\vec v \times \vec a$.

---

## Zadanie 3 – Całkowanie ruchu

### A) Dla danej prędkości:

$$
\vec v(t) = \bigl(2t,3,-e^{-t}\bigr), \qquad
\vec r(0) = (0,1,2)
$$

1. Wyznacz
   $$
   \vec r(t) = \vec r(0) + \int_0^t \vec v(\tau)\, d\tau
   $$
2. Wyznacz przyspieszenie $\vec a(t)$.

### B) Dla danego przyspieszenia:

$$
\vec a(t) = \bigl(4,-\sin t,0\bigr),
\qquad
\vec v(0) = (1,0,2),
\qquad
\vec r(0) = (0,0,0)
$$

1. Wyznacz
   $$
   \vec v(t) = \vec v(0) + \int_0^t \vec a(\tau)\, d\tau
   $$
2. Wyznacz
   $$
   \vec r(t) = \int_0^t \vec v(\tau)\, d\tau+ \vec r(0)
   $$

---

## Zadanie 4 – Geometria krzywych parametrycznych

Zbadaj następujące krzywe:

A) $\ x(t) = R\cos t,\quad  y(t) = R\sin t$

B) $\ x(t) = a\cos t, \quad y(t) = b\sin t$

C) $\ x(t) = t, \quad   y(t) = t^2$

D) $\ x(t) = \cosh t, \quad y(t) = \sinh t$

Dla każdej krzywej:

1. Wyeliminuj parametr (jeśli możliwe).
2. Określ typ krzywej.
3. Wyznacz prędkość $\vec v(t)$ i przyspieszenie $\vec a(t)$.
4. Sprawdź, czy prędkość/przyspieszenie ma stałą wartość ($|\vec v| = const$ lub $|\vec a| = const$).
---

## Zadanie 5 – Krzywizna toru i przyspieszenie normalne

Dla elipsy:

$$
x = a\cos t, \qquad y = b\sin t
$$

1. Wyznacz wektor prędkości $\vec v(t)$ oraz przyspieszenia $\vec a(t)$.
2. Wyznacz jednostkowy wektor styczny do toru
   $$
   \hat T(t)=\frac{\vec v(t)}{|\vec v(t)|}.
   $$
3. Rozłóż przyspieszenie na składową styczną i normalną:
   $$
   \vec a(t)=\vec a_t(t)+\vec a_n(t),
   $$
   oraz wyznacz wartość przyspieszenia normalnego $a_n(t)=|\vec a_n(t)|$.
4. Korzystając z relacji
   $$
   a_n=\frac{v^2}{R},
   $$
   wyznacz promień krzywizny toru w punkcie $t=0$.
5. Porównaj wynik z przypadkiem okręgu $a=b$.

### **Interpretacja fizyczna.**
Odpowiedz na pytania:

* Czy większa krzywizna toru oznacza większe przyspieszenie normalne?
* W którym miejscu elipsy tor jest bardziej „zakrzywiony”: przy końcu półosi większej czy mniejszej?
* Wyjaśnij, dlaczego przyspieszenie normalne można interpretować jako przyczynę zmiany kierunku ruchu.

---

## Zadanie 6 – Długość krzywej i całkowanie numeryczne

Dany jest tor parametryczny w 2D:

$$
x(t) = t,\qquad y(t)=t^2,\qquad t\in[0,1]
$$

1. Wyznacz wektor prędkości:
$$
\vec v(t)=\frac{d\vec r}{dt}
$$
2. Wyznacz wartość prędkości $|\vec v(t)|$.
3. Zapisz długość łuku toru jako całkę:
$$
s = \int_0^1 |\vec v(t)|\,dt
$$
4. Oblicz tę całkę analitycznie (jeśli możliwe) lub sprowadź ją do postaci wymagającej metody numerycznej.
5. Zaimplementuj metodę trapezów w HTML/JS do obliczenia $s$:
    - sprawdź zbieżność wyniku przy rosnącej liczbie podziałów $N$,
    - wykonaj wykres błędu w funkcji $N$.

Wymaganie: wizualizacja toru oraz możliwość zmiany $N$ w aplikacji.

---

## Zadanie 7 – Praca siły wzdłuż toru

Dana siła: 

$$
\vec F(x,y) = (y, 2x)
$$

Tor:

$$
x = t, \qquad y = t^2, \qquad t \in [0,1]
$$

1. Wyznacz wektor prędkości $\vec v(t)$.
2. Oblicz pracę wykonaną przez siłę $\vec F$ wzdłuż toru, czyli całkę krzywoliniową:
$$
W = \int_C \vec F \cdot d\vec r
$$
3. Zapisz całkę jako granicę sumy Riemanna i oblicz jej wartość numerycznie w HTML/JS, porównując z wynikiem analitycznym (jeśli możliwe).

---

## Zadanie 8 – Równanie różniczkowe I rzędu

$$
\frac{dy}{dt} = -k y
$$

1. Rozwiąż równanie.
2. Zwizualizuj rozwiązanie w aplikacji html/js dla różnych wartości parametru $k$ i różnych warunków początkowych $y(0)$.

---

## Zadanie 9 – Oscylator harmoniczny

$$
\frac{d^2 x}{dt^2} + \omega^2 x = 0
$$

1. Znajdź rozwiązanie ogólne.
2. Rozwiąż dla zadanych warunków początkowych.
3. Zwizualizuj (aplikacja html): $x(t)$, $x'(t)$, $x''(t)$ dla wybranych parametrów i warunków początkowych.


---

## Zadanie 10 – Moment pędu w ruchu po okręgu

Rozważ ruch po okręgu w płaszczyźnie $xy$:

$$
\vec r(t)=\bigl(R\cos(\omega t),\,R\sin(\omega t),\,0\bigr)
$$

1. Wyznacz prędkość:
$$
\vec v(t)=\dot{\vec r}(t)
$$
2. Oblicz moment pędu względem początku układu:
$$
\vec L(t)=m\,\vec r(t)\times \vec v(t)
$$
3. Pokaż, że $|\vec L|=mR^2\omega$ jest stałe, a wektor $\vec L$ jest prostopadły do płaszczyzny ruchu.
4. Zinterpretuj zwrot $\vec L$ (reguła prawej dłoni).
5. (Opcjonalnie) Dodaj stałą siłę dośrodkową i policz moment siły:
$$
\vec \tau = \vec r \times \vec F
$$
Sprawdź zależność $\vec \tau = \frac{d\vec L}{dt}$ dla ruchu jednostajnego po okręgu.
