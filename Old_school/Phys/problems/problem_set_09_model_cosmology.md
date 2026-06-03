# Lista 9 – Kosmologia modelowa: od epicykli do grawitacji

---

## Zadanie 1 – Model Ptolemeusza

1. Zapisz ruch planety jako sumę:
    - ruchu po deferencie (okrąg główny),
    - ruchu po epicyklu.
   Przykładowy zapis parametryczny:
   $$
   x(t) = R \cos(\omega t) + r \cos(\Omega t)
   $$
   $$
   y(t) = R \sin(\omega t) + r \sin(\Omega t)
   $$
2. Wyprowadź równania parametryczne toru.
3. Zbadaj warunek występowania ruchu wstecznego (retrogradacji).
4. Określ momenty zmiany kierunku ruchu w projekcji kątowej.

**HTML (obowiązkowo):**

- suwaki: $R$, $r$, $\omega$, $\Omega$,
- ślad toru,
- wykres długości ekliptycznej $\varphi(t)$.

---

## Zadanie 2 – Model Kopernika

1. Zaimplementuj ruch dwóch planet po okręgach wokół Słońca:
   $$
   \vec r_Z(t) = R_Z (\cos \omega_Z t, \sin \omega_Z t)
   $$
   $$
   \vec r_M(t) = R_M (\cos \omega_M t, \sin \omega_M t)
   $$
2. Wyznacz położenie Marsa względem Ziemi:
   $$
   \vec r_{M/Z}(t) = \vec r_M(t) - \vec r_Z(t)
   $$
3. Zidentyfikuj momenty retrogradacji.
4. Porównaj tor względny z modelem epicyklicznym.

**HTML:**

- widok heliocentryczny,
- widok geocentryczny,
- przełącznik układu odniesienia.

---

## Zadanie 3 – Porównanie modeli: liczba parametrów i jakość opisu

1. Dopasuj parametry epicyklu do toru wygenerowanego w modelu heliocentrycznym.
2. Porównaj liczbę parametrów w obu modelach.
3. Oceń, który model jest bardziej ekonomiczny.
4. Zinterpretuj wynik w kontekście uproszczenia opisu zjawisk.

---

## Zadanie 4 – I i II prawo Keplera

1. Zaimplementuj orbitę eliptyczną:

   $$
   r(\theta) = \frac{a(1-e^2)}{1 + e \cos \theta}
   $$
2. Zmieniaj mimośród $e$ i obserwuj kształt toru.
3. Numerycznie oblicz pole zakreślone w równych przedziałach czasu:
   $$
   A = \frac{1}{2} \int r^2 \, d\theta
   $$
4. Zweryfikuj prawo równych pól.

**HTML:**

- wizualizacja ogniska,
- rysowanie wycinków pola,
- dynamiczne porównanie pól.

---

## Zadanie 5 – III prawo Keplera (analiza danych)

1. Wczytaj dane dla kilku planet $(a, T)$.
2. Wykreśl zależność:
   $$
   T^2 \text{ w funkcji } a^3
   $$
3. Wykonaj regresję liniową.
4. Oszacuj stałą proporcjonalności z relacji:
   $$
   T^2 = C a^3
   $$
5. Oceń jakość dopasowania ($R^2$).

---

## Zadanie 6 – Ruch dwóch ciał i barycentrum

1. Zdefiniuj środek masy:
   $$
   \vec R = \frac{m_1 \vec r_1 + m_2 \vec r_2}{m_1 + m_2}
   $$
2. Pokaż, że dla układu izolowanego:
   $$
   m_1 \vec r_1 + m_2 \vec r_2 = \text{const}
   $$
3. Zapisz równania ruchu:
   $$
   m_1 \ddot{\vec r}_1 = - G \frac{m_1 m_2}{|\vec r_1 - \vec r_2|^3} (\vec r_1 - \vec r_2)
   $$
   $$
   m_2 \ddot{\vec r}_2 = - G \frac{m_1 m_2}{|\vec r_2 - \vec r_1|^3} (\vec r_2 - \vec r_1)
   $$
4. Zbadaj zależność toru od stosunku mas $m_1/m_2$.

**HTML:**

- trajektorie obu ciał,
- zaznaczone barycentrum,
- suwak zmiany stosunku mas.

---

## Zadanie 7 – Grawitacja Newtona i klasyfikacja orbit

Ruch w polu centralnym:

$$
\vec F = -\frac{GMm}{r^2} \hat r
$$

Energia całkowita:

$$
E = \frac{1}{2} m v^2 - \frac{GMm}{r}
$$

1. Zbadaj numerycznie przypadki:
    - $E < 0$ (orbita związana),
    - $E = 0$ (parabola),
    - $E > 0$ (hiperbola).
2. Określ warunki początkowe prowadzące do różnych typów orbit.

**HTML:**

- zmiana prędkości początkowej,
- wykres energii w czasie,
- klasyfikacja toru.

---

## Zadanie 8 – Perturbacja i precesja orbity (rozszerzenie newtonowskie)

Zmodyfikowany potencjał:

$$
U(r) = -\frac{GMm}{r} + \frac{\alpha}{r^2}
$$

1. Zaimplementuj równania ruchu.
2. Zaobserwuj precesję peryhelium.
3. Zbadaj wpływ parametru $\alpha$.

**HTML:**

- animacja dryfu osi elipsy,
- pomiar kąta precesji.

---

## Zadanie 9 – Układ trzech ciał (problem klasyczny)

1. Zapisz równania ruchu dla trzech mas.
2. Zaimplementuj metodę numeryczną (np. RK4).
3. Zbadaj stabilność konfiguracji.

**HTML:**

- animacja ruchu trzech ciał,
- możliwość zmiany mas i warunków początkowych.

---

## Zadanie 10 – Analiza stabilności i wielkości zachowanych

1. Monitoruj dla układu trzech ciał:
    - energię całkowitą $E(t)$,
    - moment pędu $\vec L = \vec r \times m \vec v$,
    - położenie środka masy.
2. Oceń stabilność metody numerycznej.
3. Porównaj różne kroki czasowe $\Delta t$.
4. Zbadaj wpływ schematu całkowania na zachowanie orbit.
