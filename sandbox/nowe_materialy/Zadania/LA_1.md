Jasne, oto zawartość raportu w formacie Markdown.

# Zbiór Zadań z Algebry Liniowej: Poziom Akademicki

## Dział 1: Algebra Liniowa

### Macierze i podstawowe operacje

1.  Dane są macierze $A = \begin{pmatrix} 1 & -2 & 0 \\ 3 & 5 & -1 \end{pmatrix}$, $B = \begin{pmatrix} 0 & 4 & -2 \\ -1 & 1 & 3 \end{pmatrix}$ oraz $C = \begin{pmatrix} 2 & -1 \\ 0 & 3 \\ 1 & -4 \end{pmatrix}$. Oblicz (jeśli to możliwe): $A + B$, $A - 2B$, $A^T$, $B \cdot C$, $C \cdot A$.

2.  Wyznacz macierz $X$ spełniającą równanie: $3(A - 2X) + 5B^T = 2(B^T - 5X) + A$, gdzie $A = \begin{pmatrix} 1 & 0 \\ -1 & 2 \end{pmatrix}$ oraz $B = \begin{pmatrix} 3 & 1 \\ 0 & -2 \end{pmatrix}$.

3.  Skonstruuj macierz symetryczną $S$ oraz macierz antysymetryczną $A$ wymiaru $3 \times 3$, których elementy są niezerowe. Następnie, dla macierzy $M = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$, oblicz $S+A$ oraz sprawdź, czy macierz $M^T M$ jest symetryczna.

4.  Rozwiąż macierzowy układ równań, znajdując macierze $X$ i $Y$:
    $$
    \begin{cases}
    X + Y = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix} \\
    2X - 3Y = \begin{pmatrix} -1 & 2 \\ 5 & 1 \end{pmatrix}
    \end{cases}
    $$

5.  Dla macierzy $A = \begin{pmatrix} 1 & 2 & 1 \\ 0 & -1 & 3 \end{pmatrix}$ oraz $B = \begin{pmatrix} -2 & 0 & 1 \\ 1 & 4 & -1 \end{pmatrix}$, zweryfikuj, obliczając obie strony niezależnie, czy zachodzi tożsamość $(A+B)^T = A^T + B^T$.

### Mnożenie macierzy

1.  Dane są macierze $A = \begin{pmatrix} 1 & 0 & -2 \\ 2 & 3 & 0 \\ -1 & 1 & 4 \end{pmatrix}$ oraz $B = \begin{pmatrix} 0 & -1 & 1 \\ 2 & 1 & 0 \\ 3 & -2 & 5 \end{pmatrix}$. Oblicz iloczyny $A \cdot B$ oraz $B \cdot A$. Czy mnożenie macierzy jest przemienne?

2.  Znajdź dwie niezerowe macierze $A, B \in \mathbb{R}^{2 \times 2}$ takie, że ich iloczyn $A \cdot B$ jest macierzą zerową.

3.  Dla macierzy $A = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{pmatrix}$, oblicz $f(A)$, gdzie $f(x) = x^3 - 6x^2 + 12x - 8$. Wynik podaj w postaci macierzy, a $f(A)$ oblicz jako $A^3 - 6A^2 + 12A - 8I$, gdzie $I$ jest macierzą jednostkową.

4.  Sprawdź, czy dla macierzy $A = \begin{pmatrix} 1 & -1 \\ 0 & 2 \end{pmatrix}$ i $B = \begin{pmatrix} 3 & 0 \\ 1 & 1 \end{pmatrix}$ zachodzi równość $(A-B)(A+B) = A^2 - B^2$. Jaki warunek muszą spełniać macierze $A$ i $B$, aby ta równość była prawdziwa?

5.  Znajdź wszystkie macierze $B$ postaci $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$, które komutują z macierzą $A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$, tzn. spełniają warunek $A \cdot B = B \cdot A$.

### Wyznaczniki: Metoda Sarrusa i Rozwinięcie Laplace'a

1.  Stosując metodę Sarrusa, oblicz wyznacznik macierzy $A = \begin{pmatrix} 2 & -1 & 3 \\ 1 & 4 & -2 \\ -3 & 0 & 5 \end{pmatrix}$.

2.  Oblicz wyznacznik macierzy $B = \begin{pmatrix} 1 & -2 & 4 \\ 0 & 3 & -1 \\ 5 & 2 & -3 \end{pmatrix}$, stosując rozwinięcie Laplace'a:
    a) względem drugiego wiersza,
    b) względem trzeciej kolumny.
    Porównaj otrzymane wyniki.

3.  Używając rozwinięcia Laplace'a względem najdogodniejszego wiersza lub kolumny, oblicz wyznacznik macierzy:
    $$
    C = \begin{pmatrix}
    3 & 0 & -1 & 2 \\
    1 & 4 & 0 & 5 \\
    -2 & 2 & 0 & 1 \\
    -1 & 0 & 6 & 3
    \end{pmatrix}
    $$

4.  Oblicz wyznacznik macierzy $D$ wymiaru $5 \times 5$ poprzez wielokrotne zastosowanie rozwinięcia Laplace'a.
    $$
    D = \begin{pmatrix}
    7 & 0 & -2 & 0 & 0 \\
    1 & 2 & 8 & 0 & 0 \\
    -3 & 0 & 4 & 0 & 0 \\
    5 & 9 & -6 & 2 & 1 \\
    -1 & 4 & 3 & 3 & -1
    \end{pmatrix}
    $$

5.  Rozwiąż równanie $\det(A - \lambda I) = 0$, gdzie $A = \begin{pmatrix} 4 & 1 & 0 \\ 1 & 4 & 0 \\ 0 & 0 & 2 \end{pmatrix}$, $I$ jest macierzą jednostkową, a $\lambda$ jest niewiadomą.

### Wyznaczniki: Metoda operacji elementarnych i własności

1.  Sprowadzając macierz do postaci trójkątnej górnej za pomocą operacji elementarnych na wierszach, oblicz wyznacznik:
    $$
    A = \begin{pmatrix}
    1 & 2 & -1 & 0 \\
    2 & 5 & 1 & 3 \\
    -1 & -3 & 0 & -2 \\
    0 & 1 & 4 & 4
    \end{pmatrix}
    $$

2.  Wiadomo, że $\det(A) = -3$ dla pewnej macierzy $A \in \mathbb{R}^{4 \times 4}$. Korzystając z własności wyznaczników, oblicz:
    a) $\det(2A)$
    b) $\det(A^T \cdot A)$
    c) $\det(A^3)$
    d) $\det(A^{-1})$

3.  Bez obliczania wyznacznika, uzasadnij, dlaczego wyznacznik poniższej macierzy jest równy zero.
    $$
    B = \begin{pmatrix}
    1 & 2 & 3 & 4 \\
    5 & 6 & 7 & 8 \\
    -1 & 0 & 1 & 2 \\
    5 & 8 & 11 & 14
    \end{pmatrix}
    $$
    (Wskazówka: zbadaj liniową zależność wierszy).

4.  Znajdź wszystkie wartości parametru $p \in \mathbb{R}$, dla których macierz $C$ jest osobliwa (tzn. $\det(C) = 0$).
    $$
    C = \begin{pmatrix}
    1 & 1 & 1 \\
    1 & p & p^2 \\
    1 & 2 & 3
    \end{pmatrix}
    $$

5.  Nie obliczając wyznacznika w sposób bezpośredni, znajdź pierwiastki rzeczywiste równania:
    $$
    \begin{vmatrix}
    1 & 1 & 1 & 1 \\
    1 & x & 1 & 1 \\
    1 & 1 & x^2 & 1 \\
    1 & 1 & 1 & x^3
    \end{vmatrix} = 0
    $$

### Odwracanie macierzy: Metoda dopełnień algebraicznych

1.  Wyznacz macierz odwrotną do macierzy $A = \begin{pmatrix} 5 & -2 \\ -7 & 3 \end{pmatrix}$ za pomocą wzoru z macierzą dołączoną.

2.  Stosując metodę dopełnień algebraicznych (macierzy dołączonej), znajdź macierz odwrotną do:
    $$
    B = \begin{pmatrix}
    2 & 1 & 0 \\
    -1 & 3 & 2 \\
    0 & -1 & 1
    \end{pmatrix}
    $$

3.  Sprawdź, czy macierz $C = \begin{pmatrix} 1 & -2 & 3 \\ 2 & -3 & 1 \\ 3 & -5 & 4 \end{pmatrix}$ jest odwracalna. Jeśli tak, znajdź $C^{-1}$ metodą dopełnień algebraicznych.

4.  Dla jakich wartości parametru $k \in \mathbb{R}$ macierz $D$ jest odwracalna? Dla tych wartości wyznacz $D^{-1}$.
    $$
    D = \begin{pmatrix}
    1 & 0 & 2 \\
    0 & k & -1 \\
    1 & 1 & 1
    \end{pmatrix}
    $$

5.  Dla macierzy $A = \begin{pmatrix} 1 & 0 & 1 \\ 2 & 1 & 0 \\ 3 & 2 & 1 \end{pmatrix}$, oblicz jej macierz dołączoną $A^D$ (transponowaną macierz dopełnień) i wykonaj mnożenie $A \cdot A^D$, aby zweryfikować tożsamość $A \cdot A^D = \det(A) \cdot I$.

### Odwracanie macierzy: Metoda Gaussa-Jordana

1.  Stosując metodę operacji elementarnych (metodę Gaussa-Jordana), znajdź macierz odwrotną do:
    $$
    A = \begin{pmatrix}
    1 & 2 & 3 \\
    0 & 1 & 2 \\
    -1 & 0 & 1
    \end{pmatrix}
    $$

2.  Wyznacz macierz odwrotną do macierzy $B$ metodą bezwyznacznikową (Gaussa-Jordana).
    $$
    B = \begin{pmatrix}
    1 & 0 & -1 & 2 \\
    0 & 1 & 1 & -1 \\
    1 & 0 & 0 & 1 \\
    0 & 1 & 0 & 1
    \end{pmatrix}
    $$

3.  Używając metody eliminacji Gaussa-Jordana na macierzy $[C | I]$, pokaż, że macierz $C = \begin{pmatrix} 1 & 2 & -1 \\ 3 & 7 & -5 \\ -2 & -4 & 2 \end{pmatrix}$ jest osobliwa (nieodwracalna).

4.  Rozwiąż równanie macierzowe $A \cdot X = B$, gdzie $A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \\ 0 & 1 & 1 \end{pmatrix}$ i $B = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{pmatrix}$. W tym celu najpierw znajdź $A^{-1}$ metodą Gaussa-Jordana.

5.  Znajdź macierz odwrotną do macierzy trójkątnej dolnej $L$ za pomocą metody Gaussa-Jordana.
    $$
    L = \begin{pmatrix}
    2 & 0 & 0 & 0 \\
    -1 & 3 & 0 & 0 \\
    4 & -2 & 1 & 0 \\
    -3 & 1 & 5 & -1
    \end{pmatrix}
    $$

### Układy równań liniowych: Metoda Cramera

1.  Stosując wzory Cramera, rozwiąż układ równań:
    $$
    \begin{cases}
    2x - 3y = 7 \\
    5x + 4y = 6
    \end{cases}
    $$

2.  Rozwiąż poniższy układ równań, korzystając z metody Cramera.
    $$
    \begin{cases}
    x + 2y - z = 2 \\
    3x - y + 2z = 7 \\
    -x + y + 3z = 6
    \end{cases}
    $$

3.  Zbadaj, dla jakich wartości parametru $a \in \mathbb{R}$ poniższy układ jest układem Cramera. Dla tych wartości znajdź rozwiązanie, stosując wzory Cramera.
    $$
    \begin{cases}
    ax + y + z = 1 \\
    x + ay + z = 1 \\
    x + y + az = 1
    \end{cases}
    $$

4.  Rozwiąż układ równań o współczynnikach ułamkowych za pomocą wzorów Cramera.
    $$
    \begin{cases}
    \frac{1}{2}x + y - z = 1 \\
    x - \frac{1}{3}y + 2z = 0 \\
    2x + y - \frac{1}{4}z = 2
    \end{cases}
    $$

5.  W układzie czterech równań z czterema niewiadomymi, nie rozwiązując całego układu, oblicz wartość niewiadomej $z$ za pomocą wzorów Cramera.
    $$
    \begin{cases}
    x + y + z + t = 10 \\
    x - y + z - t = 0 \\
    2x + y - z + 2t = 12 \\
    x + 2y + 2z - t = 13
    \end{cases}
    $$

### Układy równań liniowych: Metoda eliminacji Gaussa

1.  Stosując metodę eliminacji Gaussa, rozwiąż układ równań oznaczony:
    $$
    \begin{cases}
    x + 2y + 3z = 14 \\
    2x + 5y + 2z = 18 \\
    3x + y + z = 10
    \end{cases}
    $$

2.  Rozwiąż układ nieoznaczony metodą eliminacji Gaussa i podaj jego rozwiązanie ogólne w zależności od jednego lub więcej parametrów.
    $$
    \begin{cases}
    x - 2y + z + t = 1 \\
    2x - 4y + 3z - t = 2 \\
    -x + 2y + 2z - 8t = -1
    \end{cases}
    $$

3.  Pokaż, że poniższy układ równań jest sprzeczny, sprowadzając jego macierz rozszerzoną do postaci schodkowej.
    $$
    \begin{cases}
    x + y - 3z = -1 \\
    2x + y - 2z = 1 \\
    x + y + z = 3 \\
    x + 2y - 3z = 1
    \end{cases}
    $$

4.  Znajdź rozwiązanie ogólne układu jednorodnego i podaj bazę przestrzeni rozwiązań tego układu.
    $$
    \begin{cases}
    x_1 + 3x_2 - x_3 + 5x_4 = 0 \\
    2x_1 + 7x_2 - 4x_3 + 11x_4 = 0 \\
    -x_1 - 2x_2 - x_3 - 4x_4 = 0
    \end{cases}
    $$

5.  Zbadaj, w zależności od wartości parametru $a \in \mathbb{R}$, liczbę rozwiązań układu równań, stosując metodę eliminacji Gaussa.
    $$
    \begin{cases}
    x + ay + z = 1 \\
    2x + 2y + 2z = 3 \\
    x + y + az = a
    \end{cases}
    $$

### Układy równań liniowych: Metoda macierzy odwrotnej

1.  Zapisz układ równań w postaci macierzowej $A \vec{x} = \vec{b}$. Następnie znajdź $A^{-1}$ metodą dopełnień algebraicznych i użyj jej do obliczenia wektora rozwiązań $\vec{x}$.
    $$
    \begin{cases}
    x + 2y = 5 \\
    3x + 5y = 14
    \end{cases}
    $$

2.  Rozwiąż układ równań metodą macierzy odwrotnej. Macierz odwrotną znajdź za pomocą metody Gaussa-Jordana.
    $$
    \begin{cases}
    x + y + z = 6 \\
    x + 2y + 3z = 14 \\
    x + 3y + 6z = 25
    \end{cases}
    $$

3.  Dana jest macierz $A = \begin{pmatrix} 1 & -1 & 0 \\ 0 & 1 & -1 \\ 1 & 0 & 1 \end{pmatrix}$. Znajdź $A^{-1}$, a następnie wykorzystaj ją do rozwiązania trzech układów równań $A \vec{x} = \vec{b_i}$ dla $\vec{b_1} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$, $\vec{b_2} = \begin{pmatrix} 0 \\ 2 \\ -1 \end{pmatrix}$ oraz $\vec{b_3} = \begin{pmatrix} 3 \\ -2 \\ 4 \end{pmatrix}$.

4.  Rozwiąż równanie macierzowe $X \cdot A = B$, gdzie $A = \begin{pmatrix} 2 & 1 \\ 3 & 2 \end{pmatrix}$ oraz $B = \begin{pmatrix} -1 & 1 \\ 0 & 4 \end{pmatrix}$. (Wskazówka: $X = B \cdot A^{-1}$).

5.  Dla jakich wartości parametru $m \in \mathbb{R}$ można rozwiązać poniższy układ metodą macierzy odwrotnej? Dla tych wartości podaj wzór na macierz odwrotną do macierzy głównej układu.
    $$
    \begin{cases}
    mx + y = 1 \\
    x + my = -1
    \end{cases}
    $$