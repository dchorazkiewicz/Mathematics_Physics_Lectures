# Lista 4 – Drgania i fale: systemy dynamiczne i propagacja zaburzeń


## Zadanie 1 – Ruch harmoniczny: parametry ruchu

Dana jest funkcja opisująca ruch harmoniczny:

$$
x(t) = A \cos(\omega t + \varphi)
$$

1. Wyznacz okres $T$ oraz częstotliwość $f$.
2. Wyznacz maksymalną prędkość oraz maksymalne przyspieszenie.
3. Dla $A = 0.2\ \mathrm{m}$, $f = 2\ \mathrm{Hz}$:

   * oblicz $\omega$,
   * oblicz $v_{\max}$,
   * oblicz $a_{\max}$.

Odpowiedzi: pełne wyprowadzenie + interpretacja.

---

## Zadanie 2 – Energia oscylatora harmonicznego

Dany jest układ o parametrach początkowych:

* $m = 1\ \mathrm{kg}$
* $k = 100\ \mathrm{N/m}$
* $x(0) = 2\ \mathrm{m}$
* $v(0) = 1\ \mathrm{m/s}$

1. Wyznacz częstość własną.
2. Oblicz energię całkowitą układu.
3. Dla jakiego wychylenia energia kinetyczna stanowi 50% energii całkowitej?

Odpowiedzi: pełne wyprowadzenie + interpretacja.

---

## Zadanie 3 – Fala harmoniczna

Dane jest równanie fali:

$$
y(x,t) = A \sin(kx - \omega t)
$$

1. Wyznacz długość fali.
2. Wyznacz prędkość fazową.
3. Oblicz $v$ dla $k = 4\pi$, $\omega = 20\pi$.
4. Czy punkt $x = \lambda$ drga w fazie z punktem $x = 0$?

Odpowiedzi: pełne wyprowadzenie + interpretacja.

---

## Zadanie 4 – Równanie falowe

Dana jest funkcja:

$$
y(x,t) = A \cos(kx - \omega t)
$$

1. Sprawdź, że spełnia równanie falowe:
$$
\frac{\partial^2 y}{\partial t^2} = v^2 \frac{\partial^2 y}{\partial x^2}
$$
2. Wyznacz zależność między $v$, $k$ i $\omega$.

Odpowiedzi: relacja algebraiczna.

---

## Zadanie 5 – Superpozycja fal, dudnienia i prędkość grupowa

Dane są dwie fale harmoniczne:

$$
y_1(x,t)=A\sin(kx-\omega t)
$$

$$
y_2(x,t)=A\sin(kx-(\omega+\Delta\omega)t)
$$

1. Wyznacz falę wypadkową $y=y_1+y_2$ i sprowadź ją do postaci iloczynu (nośna × obwiednia).

2. Zidentyfikuj częstość dudnień oraz okres dudnień w punkcie $x=0$.

3. Zinterpretuj fizycznie: co opisuje obwiednia, a co fala nośna?

4. Uzyj pythona/html/js do wygenerowania dwóch fal i ich superpozycji, pokazując zjawisko dudnień i ruch obwiedni.

---

## Zadanie 6 – Oscylator tłumiony

Równanie:

$$
m \frac{d^2 x}{dt^2} + b \frac{dx}{dt} + k x = 0
$$

1. Wyprowadź ogólne rozwiązanie dla każdego przypadku.
2. Przedstaw klasyfikację przypadków: podtłumiony, krytyczny, przetłumiony.
3. Rozwiąż równanie numerycznie (RK4).
4. Zbadaj wpływ parametru $b$.
5. Wygeneruj wykres $x(t)$.
6. Wygeneruj portret fazowy.

Wymaganie HTML: interaktywny suwak dla $b$.

---

## Zadanie 7 – Oscylator wymuszony i rezonans

$$
m \frac{d^2 x}{dt^2} + b \frac{dx}{dt} + k x = F_0 \cos(\Omega t)
$$

1. Rozwiąż równanie analitycznie, wyznaczając amplitudę drgań w funkcji $\Omega$.
2. Rozwiąż równanie numerycznie.
3. Zbadaj amplitudę ustaloną w funkcji $\Omega$.
4. Wygeneruj wykres rezonansowy.
5. Zbadaj przesunięcie fazowe.
6. Zinterpretuj zjawisko rezonansu.

Wymaganie HTML: interaktywna zmiana częstotliwości wymuszenia.

---

## Zadanie 8 – Dwie sprzężone sprężyny (dwa stopnie swobody)

Dwie masy połączone ze ścianami w konfiguracji szeregowej sprężynami o stałych $k_1$ i $k_2$ i $k_3$.


1. Zapisz równania ruchu.
2. Wyznacz częstości własne.
3. Znajdź mody normalne.
4. Rozwiąż numerycznie dla dowolnych warunków początkowych.
5. Zidentyfikuj wymianę energii między masami.

Wymaganie HTML: animacja ruchu obu mas.

---

## Zadanie 9 – Łańcuch $N$ sprężyn (dyskretny model fali)

Układ: $N$ mas połączonych sprężynami.

1. Zapisz równania ruchu.
2. Rozwiąż numerycznie dla $N = 20, 50, 100$.
3. Wprowadź lokalne zaburzenie początkowe.
4. Obserwuj propagację impulsu.
5. Zbadaj wpływ wartości $k$ i $m$ na prędkość propagacji.

Wymaganie HTML: animacja całego łańcucha.

---

## Zadanie 10 – Wahadło podwójne i chaos deterministyczny

Cel: **czysto numeryczna analiza** wahadła podwójnego i wizualizacja chaosu deterministycznego.

Rozważ wahadło podwójne (dwa masywne punkty $m_1, m_2$ na nieważkich prętach $l_1, l_2$) w jednorodnym polu grawitacyjnym $g$. Równania ruchu przyjmij ze standardowej postaci dla wahadła podwójnego (nie wyprowadzamy ich analitycznie na tej liście).

1. Zapisz współrzędne $(x_1,y_1)$ oraz $(x_2,y_2)$ w funkcji kątów $(\theta_1,\theta_2)$ (do animacji).
2. Zaimplementuj numeryczną całkę równań (np. RK4) i sprawdź stabilność numeryczną (np. dryf energii dla różnych $\Delta t$).
3. Zbadaj wrażliwość na warunki początkowe: **symuluj jednocześnie 50 kopii** układu z minimalnie różnymi warunkami początkowymi (np. perturbacja tylko w $\theta_2(0)$ rzędu $10^{-4}$–$10^{-2}$ rad).
4. Eksperymentuj z różnymi skalami perturbacji i obserwuj rozbieganie trajektorii.

Parametry startowe (do ujednolicenia wyników): $m_1=m_2=1$, $l_1=l_2=1$, $g=9.81$, krok całkowania $\Delta t\le 0.01\,\mathrm{s}$.

Wymaganie HTML: animacja wahadła podwójnego w trybie „ensemble” — **50 wahadeł jednocześnie**, każde w **innym kolorze**, aby było widać rozbieganie; dodaj reset i możliwość ustawienia skali perturbacji.
