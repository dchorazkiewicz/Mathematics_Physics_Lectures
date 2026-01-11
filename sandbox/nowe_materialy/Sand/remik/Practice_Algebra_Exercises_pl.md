<<<<<<< HEAD
# Dział 1 — Algebra Liniowa: Ćwiczenia

## Macierze i podstawowe operacje

1. Dla macierzy

$$
A=\begin{pmatrix}1 & 2\\ 3 & 4\end{pmatrix} \quad \text{i} \quad B=\begin{pmatrix}0 & -1\\ 2 & 1\end{pmatrix}
$$

   oblicz

   - $A+B$
   - $A-B$
   - $2A$
   - $A^2$
   - $3B-2A$
   - $A\cdot B$
   - sprawdź, czy $A\cdot B = B\cdot A$.

2. Dla macierzy

$$
   A=\begin{pmatrix}1 & 0\\ 0 & 2\end{pmatrix}, 
   \quad
   B =\begin{pmatrix}2 & 0\\ 0 & 4\end{pmatrix}, 
   \quad
   C=\begin{pmatrix}4 & 0\\ 0 & 8\end{pmatrix},
   \quad
   D=\begin{pmatrix}8 & 0\\ 0 & 16\end{pmatrix}
$$

sprawdź, czy

$$
A\cdot B\cdot C\cdot D = B\cdot A\cdot D\cdot C = D\cdot C\cdot B\cdot A.
$$


3. Dana jest macierz

$$
   C=\begin{pmatrix}
   1 & 0 & 2\\
   -1 & 3 & 1\\
   0 & 2 & -1
   \end{pmatrix}.
$$

   Wyznacz macierz otrzymaną po przestawieniu wierszy: zamień 1. i 3. wiersz, a następnie dodaj do 2. wiersza dwukrotność nowego 1. wiersza. Zapisz wszystkie kroki dla każdej operacji.

4. Pokaż, że macierz diagonalna $D=\operatorname{diag}(2,-3,5)$ jest przemienna z dowolną macierzą diagonalną $E=\operatorname{diag}(a,b,c)$. Dodatkowo oblicz $D^{3}$ oraz, jeśli istnieje, $D^{-1}$.

6. $\star$ Dla macierzy
 
   $$
   P=\begin{pmatrix}1 & 1 & 0\\ 0 & 1 & 1\\ 1 & 0 & 1\end{pmatrix}
   $$

   oblicz $P^{2}$ i $P^{3}$. Czy ciąg $P^{n}$ ma zauważalny wzorzec dla $n=1,2,3$?



9. $\star\star$ Macierze Pauliego są zdefiniowane jako:

   $$
   \sigma_x = \begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}, \quad
   \sigma_y = \begin{pmatrix}0 & -i\\ i & 0\end{pmatrix}, \quad
   \sigma_z = \begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix}
   $$

   gdzie $i$ to jednostka urojona. Sprawdź, że:

   - $\sigma_x^2 = \sigma_y^2 = \sigma_z^2 = I$ (macierz jednostkowa)
   - $\sigma_x\sigma_y = i\sigma_z$, $\sigma_y\sigma_z = i\sigma_x$, $\sigma_z\sigma_x = i\sigma_y$
   - $\{\sigma_i, \sigma_j\} = 2\delta_{ij}I$ (antykomutator)


## Wyznaczniki

1. Oblicz wyznacznik macierzy

$$
\mathbf{A} =
\begin{pmatrix}
2 & 3 \\
1 & 4
\end{pmatrix}
, \qquad
\mathbf{B} =
\begin{pmatrix}
5 & 6 \\
7 & 8
\end{pmatrix}
, \qquad
\mathbf{C} =
\begin{pmatrix}
-1 & 2 \\
3 & 0
\end{pmatrix}
$$

   $$
   A=\begin{pmatrix}
   2 & 3 & 1\\
   0 & -1 & 4\\
   5 & 2 & 0
   \end{pmatrix}
   \quad
   B=\begin{pmatrix}
   1 & 2 & 2\\
   4 & 0 & 0\\
   7 & 8 & 9
   \end{pmatrix}
   \qquad
   C=\begin{pmatrix}
   3 & 0 & 2\\
   2 & 0 & -2\\
   0 & 1 & 1
   \end{pmatrix}
   $$

   używając metody Sarrusa.

2. Wyznacz wyznaczniki używając rozwinięcia Laplace\'a:

   $$
   A=\begin{pmatrix}
   1
   \end{pmatrix}
   \quad
   B=\begin{pmatrix}
   1 & 0 & 2\\
   3 & 1 & 0\\
   4 & 5 & 6
   \end{pmatrix}
   \quad
   C=\begin{pmatrix}
   1 & 2 & 3 & 4\\
   0 & 1 & 0 & 0\\
   0 & 0 & 1 & 1\\
   0 & 0 & 0 & 2
   \end{pmatrix} 
   $$

3. Pokaż, że jeżeli w macierzy dwa wiersze są równe, to wyznacznik jest równy zero. Daj przykład macierzy $3\times3$ z dwoma równymi wierszami i oblicz jej wyznacznik. Uzasadnij, dlaczego tak się dzieje.

5. Dla macierzy zależnej od parametru $t$:

   $$
   M(t)=\begin{pmatrix}
   t & 1\\
   2 & t\\
   \end{pmatrix}
   $$

   oblicz $\det(M(t))$ i znajdź wartości $t$, dla których macierz jest osobliwa.

6. Rozwiąż równanie

   $$
   \det\begin{pmatrix}
   x & 3\\
   2 & x
   \end{pmatrix} = 0
   $$

7. $\star$ Rozwiąż równanie

   $$
   \det\begin{pmatrix}
   x & 3\\
   2 & -x
   \end{pmatrix} = 0
   $$




10. Oblicz wyznacznik macierzy
   $$
   \begin{vmatrix}
   a & a & a \\
   -a & a & a \\
   -a & -a & a
   \end{vmatrix}
   \quad
   \text{oraz}
   \quad
   \begin{vmatrix}
   a & 0 & b \\
   0 & c & 0 \\
   d & 0 & a
   \end{vmatrix}
   $$

8. Sprawdź słuszność:

 
$$
   \begin{vmatrix}
   a+b & b \\
   c+d & d
   \end{vmatrix}
   =
   \begin{vmatrix}
   a & b \\
   c & d
   \end{vmatrix}
$$



## Odwracanie macierzy

1. Znajdź rząd macierzy:

$$\mathbf{B} =
\begin{pmatrix}
4 & -3 & 7 \\
-1 & 6 & 3 \\
2 & 9 & 1
\end{pmatrix}$$

2. Znajdź macierz odwrotną używając wzoru dla macierzy $2\times2$
   $$
   A=\begin{pmatrix}2 & 1\\ 5 & 3\end{pmatrix}
   \qquad
   B=\begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}
   \qquad
   C=\begin{pmatrix}4 & 7\\ 2 & 6\end{pmatrix}
   $$


3. Dla macierzy

   $$
   A=\begin{pmatrix}1 & 2\\ 2 & 5\end{pmatrix}
   \quad
   B=\begin{pmatrix}12& 5\\ 7 & 3\end{pmatrix}
   \quad
   C=\begin{pmatrix}1 & 2 & 3\\ 0 & 1 & 4\\ 5 & 6 & 0\end{pmatrix}
   \quad
   D=\begin{pmatrix}2 & 0 & 1\\ 1 & 3 & 0\\ 0 & 4 & 5\end{pmatrix}
   $$

   oblicz macierze odwrotne za pomocą metod:

   - dołączania macierzy jednostkowej i wykonywania eliminacji Gaussa-Jordana,
   - użycia wzoru z macierzami dopełnień algebraicznych

   Czyli dla każdej macierzy podaj dwie metody obliczenia macierzy odwrotnej (jeśli istnieje).

4. Sprawdź, czy macierz

   $$
   H=\begin{pmatrix}1 & 2 & 3\\ 2 & 4 & 6\\ 0 & 1 & 1\end{pmatrix}
   $$

   jest odwracalna. Uzasadnij odpowiedź (użyj wyznacznika). Czy można było zauważyć to bez obliczania wyznacznika? Co musiałoby się stać, aby macierz była odwracalna?

5. Dla macierzy $A$ spełniającej $A^{2}=I$ pokaż, że $A^{-1}=A$. Podaj przykład niebanalnej macierzy $2\times2$ spełniającej ten warunek (innej niż $I$ i $-I$). Ile jest takich macierzy?

6. Oblicz macierz odwrotną macierzy diagonalnej $D=\operatorname{diag}(2,5,-3,1)$, jeżeli istnieje. Omów warunek istnienia odwrotności dla macierzy diagonalnej.

6. Rozwiąż równania macierzowe:

a) 
   
$$
\begin{bmatrix} 2 & 5 \\\ 1 & 3 \end{bmatrix} \cdot X = \begin{bmatrix} 4 & -6 \\\ 2 & 1 \end{bmatrix}
$$

b) 

$$
\begin{bmatrix} 2 & 1 \\\ 5 & 3 \end{bmatrix} \cdot X = \begin{bmatrix} 1 & 2 \\\ 3 & 4 \end{bmatrix}
$$

c) 
   
$$
X \cdot \begin{bmatrix} 1 & 1 & -1 \\\ 2 & 1 & 0 \\\ 1 & -1 & 1 \end{bmatrix} = \begin{bmatrix} 1 & -3 & 3 \\\ 4 & 3 & 2 \\\ 1 & -2 & 5 \end{bmatrix}
$$

d) 

$$
\begin{bmatrix} 3 & 2 & 3 \\\ 1 & 1 & 2 \\\ 3 & 2 & 4 \end{bmatrix} \cdot X = \begin{bmatrix} 1 & 2 & 3 \\\ 1 & -1 & 2 \\\ 2 & 2 & 4 \end{bmatrix}
$$

## Układy równań liniowych

1. Rozwiąż układ równań:

   $$
   \begin{aligned} 2x+3y&=5,\\ x-4y&=-2. \end{aligned}
   $$

   używając metod: Cramera, eliminacji Gaussa i macierzy odwrotnej.

2. Rozwiąż układ trzech równań z trzema niewiadomymi:

   $$
   \begin{aligned} x+y+z&=6,\\ 2x-y+3z&=14,\\ -x+2y-z&=-2. \end{aligned}
   $$

   używając metod: Cramera, eliminacji Gaussa i macierzy odwrotnej.

3. $\star$ Rozważ układ parametryczny zależny od $\lambda$:

   $$
   \begin{aligned} x+\lambda y&=1,\\ 2x+(1+\lambda)y&=3. \end{aligned}
   $$

   Określ wartości $\lambda$, dla których układ ma jedno rozwiązanie, nieskończenie wiele rozwiązań lub brak rozwiązań.

4. Dla macierzy współczynników

   $$
   A=\begin{pmatrix}1 & 1 & 1\\ 0 & 2 & -1\\ 2 & -1 & 3\end{pmatrix}
   $$

   i pionowego wektora prawych stron $b=(4,1,3)^{\top}$ rozwiąż $Ax=b$ i sprawdź wynik przez podstawienie.


5. Rozwiąż układy równań:

   a)

   $$
   \begin{cases}
   x_1 + 4x_2 + 3x_3 = 1, \\
   2x_1 + 5x_2 + 4x_3 = 4, \\
   x_1 - 3x_2 - 2x_3 = 5;
   \end{cases}
   $$

   b)

   $$
   \begin{cases}
   x_1 - 2x_2 - 3x_3 = 2, \\
   x_1 - 4x_2 - 13x_3 = 14, \\
   -3x_1 + 5x_2 + 4x_3 = 0;
   \end{cases}
   $$

   c)

   $$
   \begin{cases}
   x_1 - 2x_2 - 3x_3 = 2, \\
   x_1 - 4x_2 - 13x_3 = 14, \\
   -3x_1 + 5x_2 + 4x_3 = 2;
   \end{cases}
   $$

   d)

   $$
   \begin{cases}
   -4x_1 + 3x_2 + 2x_3 = -2, \\
   5x_1 - 4x_2 + x_3 = 3;
   \end{cases}
   $$

   e)

   $$
   \begin{cases}
   -4x_1 + 3x_2 = 2, \\
   5x_1 - 4x_2 = 0, \\
   2x_1 - x_2 = a;
   \end{cases}
   $$

   f)

   $$
   \begin{cases}
   4x_1 + 5x_3 = 6, \\
   x_2 - 6x_3 = -2, \\
   3x_1 + 4x_3 = 3;
   \end{cases}
   $$

   g)

   $$
   \begin{cases}
   3x_1 - x_2 - 2x_3 = 2, \\
   2x_2 - x_3 = -1, \\
   3x_1 - 5x_2 = 3;
   \end{cases}
   $$

   h)

   $$
   \begin{cases}
   -x_1 + 2x_2 + 3x_3 = 0, \\
   x_1 - 4x_2 - 13x_3 = 0, \\
   -3x_1 + 5x_2 + 4x_3 = 0;
   \end{cases}
   $$


   i)

   $$
   \begin{cases}
   x_1 + x_2 + x_3 = 0, \\
   2x_1 + 4x_2 + 3x_3 = 0, \\
   4x_2 + 4x_3 = 0;
   \end{cases}
   $$

   j)

   $$
   \begin{cases}
   x_1 + x_2 + x_3 = -2, \\
   2x_1 + 4x_2 - 3x_3 = 3, \\
   4x_2 + 2x_3 = 2;
   \end{cases}
   $$

   k)

   $$
   \begin{cases}
   4x_1 + 4x_3 = 8, \\
   x_2 - 6x_3 = -3, \\
   3x_1 + x_2 - 3x_3 = 3;
   \end{cases}
   $$

   l)

   $$
   \begin{cases}
   5x_1 - 3x_2 = -7, \\
   -2x_1 + 9x_2 = 4, \\
   2x_1 + 4x_2 = -2;
   \end{cases}
   $$

=======
# Dział 1 — Algebra Liniowa: Ćwiczenia

## Macierze i podstawowe operacje

1. Dla macierzy

$$
A=\begin{pmatrix}1 & 2\\ 3 & 4\end{pmatrix} \quad \text{i} \quad B=\begin{pmatrix}0 & -1\\ 2 & 1\end{pmatrix}
$$

   oblicz

   - $A+B$
   - $A-B$
   - $2A$
   - $A^2$
   - $3B-2A$
   - $A\cdot B$
   - sprawdź, czy $A\cdot B = B\cdot A$.

2. Dla macierzy

$$
   A=\begin{pmatrix}1 & 0\\ 0 & 2\end{pmatrix}, 
   \quad
   B =\begin{pmatrix}2 & 0\\ 0 & 4\end{pmatrix}, 
   \quad
   C=\begin{pmatrix}4 & 0\\ 0 & 8\end{pmatrix},
   \quad
   D=\begin{pmatrix}8 & 0\\ 0 & 16\end{pmatrix}
$$

sprawdź, czy

$$
A\cdot B\cdot C\cdot D = B\cdot A\cdot D\cdot C = D\cdot C\cdot B\cdot A.
$$


3. Dana jest macierz

$$
   C=\begin{pmatrix}
   1 & 0 & 2\\
   -1 & 3 & 1\\
   0 & 2 & -1
   \end{pmatrix}.
$$

   Wyznacz macierz otrzymaną po przestawieniu wierszy: zamień 1. i 3. wiersz, a następnie dodaj do 2. wiersza dwukrotność nowego 1. wiersza. Zapisz wszystkie kroki dla każdej operacji.

4. Pokaż, że macierz diagonalna $D=\operatorname{diag}(2,-3,5)$ jest przemienna z dowolną macierzą diagonalną $E=\operatorname{diag}(a,b,c)$. Dodatkowo oblicz $D^{3}$ oraz, jeśli istnieje, $D^{-1}$.

6. $\star$ Dla macierzy
 
   $$
   P=\begin{pmatrix}1 & 1 & 0\\ 0 & 1 & 1\\ 1 & 0 & 1\end{pmatrix}
   $$

   oblicz $P^{2}$ i $P^{3}$. Czy ciąg $P^{n}$ ma zauważalny wzorzec dla $n=1,2,3$?



9. $\star\star$ Macierze Pauliego są zdefiniowane jako:

   $$
   \sigma_x = \begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}, \quad
   \sigma_y = \begin{pmatrix}0 & -i\\ i & 0\end{pmatrix}, \quad
   \sigma_z = \begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix}
   $$

   gdzie $i$ to jednostka urojona. Sprawdź, że:

   - $\sigma_x^2 = \sigma_y^2 = \sigma_z^2 = I$ (macierz jednostkowa)
   - $\sigma_x\sigma_y = i\sigma_z$, $\sigma_y\sigma_z = i\sigma_x$, $\sigma_z\sigma_x = i\sigma_y$
   - $\{\sigma_i, \sigma_j\} = 2\delta_{ij}I$ (antykomutator)


## Wyznaczniki

1. Oblicz wyznacznik macierzy

$$
\mathbf{A} =
\begin{pmatrix}
2 & 3 \\
1 & 4
\end{pmatrix}
, \qquad
\mathbf{B} =
\begin{pmatrix}
5 & 6 \\
7 & 8
\end{pmatrix}
, \qquad
\mathbf{C} =
\begin{pmatrix}
-1 & 2 \\
3 & 0
\end{pmatrix}
$$

   $$
   A=\begin{pmatrix}
   2 & 3 & 1\\
   0 & -1 & 4\\
   5 & 2 & 0
   \end{pmatrix}
   \quad
   B=\begin{pmatrix}
   1 & 2 & 2\\
   4 & 0 & 0\\
   7 & 8 & 9
   \end{pmatrix}
   \qquad
   C=\begin{pmatrix}
   3 & 0 & 2\\
   2 & 0 & -2\\
   0 & 1 & 1
   \end{pmatrix}
   $$

   używając metody Sarrusa.

2. Wyznacz wyznaczniki używając rozwinięcia Laplace\'a:

   $$
   A=\begin{pmatrix}
   1
   \end{pmatrix}
   \quad
   B=\begin{pmatrix}
   1 & 0 & 2\\
   3 & 1 & 0\\
   4 & 5 & 6
   \end{pmatrix}
   \quad
   C=\begin{pmatrix}
   1 & 2 & 3 & 4\\
   0 & 1 & 0 & 0\\
   0 & 0 & 1 & 1\\
   0 & 0 & 0 & 2
   \end{pmatrix} 
   $$

3. Pokaż, że jeżeli w macierzy dwa wiersze są równe, to wyznacznik jest równy zero. Daj przykład macierzy $3\times3$ z dwoma równymi wierszami i oblicz jej wyznacznik. Uzasadnij, dlaczego tak się dzieje.

5. Dla macierzy zależnej od parametru $t$:

   $$
   M(t)=\begin{pmatrix}
   t & 1\\
   2 & t\\
   \end{pmatrix}
   $$

   oblicz $\det(M(t))$ i znajdź wartości $t$, dla których macierz jest osobliwa.

6. Rozwiąż równanie

   $$
   \det\begin{pmatrix}
   x & 3\\
   2 & x
   \end{pmatrix} = 0
   $$

7. $\star$ Rozwiąż równanie

   $$
   \det\begin{pmatrix}
   x & 3\\
   2 & -x
   \end{pmatrix} = 0
   $$




10. Oblicz wyznacznik macierzy
   $$
   \begin{vmatrix}
   a & a & a \\
   -a & a & a \\
   -a & -a & a
   \end{vmatrix}
   \quad
   \text{oraz}
   \quad
   \begin{vmatrix}
   a & 0 & b \\
   0 & c & 0 \\
   d & 0 & a
   \end{vmatrix}
   $$

8. Sprawdź słuszność:

 
$$
   \begin{vmatrix}
   a+b & b \\
   c+d & d
   \end{vmatrix}
   =
   \begin{vmatrix}
   a & b \\
   c & d
   \end{vmatrix}
$$



## Odwracanie macierzy

1. Znajdź rząd macierzy:

$$\mathbf{B} =
\begin{pmatrix}
4 & -3 & 7 \\
-1 & 6 & 3 \\
2 & 9 & 1
\end{pmatrix}$$

2. Znajdź macierz odwrotną używając wzoru dla macierzy $2\times2$
   $$
   A=\begin{pmatrix}2 & 1\\ 5 & 3\end{pmatrix}
   \qquad
   B=\begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}
   \qquad
   C=\begin{pmatrix}4 & 7\\ 2 & 6\end{pmatrix}
   $$


3. Dla macierzy

   $$
   A=\begin{pmatrix}1 & 2\\ 2 & 5\end{pmatrix}
   \quad
   B=\begin{pmatrix}12& 5\\ 7 & 3\end{pmatrix}
   \quad
   C=\begin{pmatrix}1 & 2 & 3\\ 0 & 1 & 4\\ 5 & 6 & 0\end{pmatrix}
   \quad
   D=\begin{pmatrix}2 & 0 & 1\\ 1 & 3 & 0\\ 0 & 4 & 5\end{pmatrix}
   $$

   oblicz macierze odwrotne za pomocą metod:

   - dołączania macierzy jednostkowej i wykonywania eliminacji Gaussa-Jordana,
   - użycia wzoru z macierzami dopełnień algebraicznych

   Czyli dla każdej macierzy podaj dwie metody obliczenia macierzy odwrotnej (jeśli istnieje).

4. Sprawdź, czy macierz

   $$
   H=\begin{pmatrix}1 & 2 & 3\\ 2 & 4 & 6\\ 0 & 1 & 1\end{pmatrix}
   $$

   jest odwracalna. Uzasadnij odpowiedź (użyj wyznacznika). Czy można było zauważyć to bez obliczania wyznacznika? Co musiałoby się stać, aby macierz była odwracalna?

5. Dla macierzy $A$ spełniającej $A^{2}=I$ pokaż, że $A^{-1}=A$. Podaj przykład niebanalnej macierzy $2\times2$ spełniającej ten warunek (innej niż $I$ i $-I$). Ile jest takich macierzy?

6. Oblicz macierz odwrotną macierzy diagonalnej $D=\operatorname{diag}(2,5,-3,1)$, jeżeli istnieje. Omów warunek istnienia odwrotności dla macierzy diagonalnej.

6. Rozwiąż równania macierzowe:

a) 
   
$$
\begin{bmatrix} 2 & 5 \\\ 1 & 3 \end{bmatrix} \cdot X = \begin{bmatrix} 4 & -6 \\\ 2 & 1 \end{bmatrix}
$$

b) 

$$
\begin{bmatrix} 2 & 1 \\\ 5 & 3 \end{bmatrix} \cdot X = \begin{bmatrix} 1 & 2 \\\ 3 & 4 \end{bmatrix}
$$

c) 
   
$$
X \cdot \begin{bmatrix} 1 & 1 & -1 \\\ 2 & 1 & 0 \\\ 1 & -1 & 1 \end{bmatrix} = \begin{bmatrix} 1 & -3 & 3 \\\ 4 & 3 & 2 \\\ 1 & -2 & 5 \end{bmatrix}
$$

d) 

$$
\begin{bmatrix} 3 & 2 & 3 \\\ 1 & 1 & 2 \\\ 3 & 2 & 4 \end{bmatrix} \cdot X = \begin{bmatrix} 1 & 2 & 3 \\\ 1 & -1 & 2 \\\ 2 & 2 & 4 \end{bmatrix}
$$

## Układy równań liniowych

1. Rozwiąż układ równań:

   $$
   \begin{aligned} 2x+3y&=5,\\ x-4y&=-2. \end{aligned}
   $$

   używając metod: Cramera, eliminacji Gaussa i macierzy odwrotnej.

2. Rozwiąż układ trzech równań z trzema niewiadomymi:

   $$
   \begin{aligned} x+y+z&=6,\\ 2x-y+3z&=14,\\ -x+2y-z&=-2. \end{aligned}
   $$

   używając metod: Cramera, eliminacji Gaussa i macierzy odwrotnej.

3. $\star$ Rozważ układ parametryczny zależny od $\lambda$:

   $$
   \begin{aligned} x+\lambda y&=1,\\ 2x+(1+\lambda)y&=3. \end{aligned}
   $$

   Określ wartości $\lambda$, dla których układ ma jedno rozwiązanie, nieskończenie wiele rozwiązań lub brak rozwiązań.

4. Dla macierzy współczynników

   $$
   A=\begin{pmatrix}1 & 1 & 1\\ 0 & 2 & -1\\ 2 & -1 & 3\end{pmatrix}
   $$

   i pionowego wektora prawych stron $b=(4,1,3)^{\top}$ rozwiąż $Ax=b$ i sprawdź wynik przez podstawienie.


5. Rozwiąż układy równań:

   a)

   $$
   \begin{cases}
   x_1 + 4x_2 + 3x_3 = 1, \\
   2x_1 + 5x_2 + 4x_3 = 4, \\
   x_1 - 3x_2 - 2x_3 = 5;
   \end{cases}
   $$

   b)

   $$
   \begin{cases}
   x_1 - 2x_2 - 3x_3 = 2, \\
   x_1 - 4x_2 - 13x_3 = 14, \\
   -3x_1 + 5x_2 + 4x_3 = 0;
   \end{cases}
   $$

   c)

   $$
   \begin{cases}
   x_1 - 2x_2 - 3x_3 = 2, \\
   x_1 - 4x_2 - 13x_3 = 14, \\
   -3x_1 + 5x_2 + 4x_3 = 2;
   \end{cases}
   $$

   d)

   $$
   \begin{cases}
   -4x_1 + 3x_2 + 2x_3 = -2, \\
   5x_1 - 4x_2 + x_3 = 3;
   \end{cases}
   $$

   e)

   $$
   \begin{cases}
   -4x_1 + 3x_2 = 2, \\
   5x_1 - 4x_2 = 0, \\
   2x_1 - x_2 = a;
   \end{cases}
   $$

   f)

   $$
   \begin{cases}
   4x_1 + 5x_3 = 6, \\
   x_2 - 6x_3 = -2, \\
   3x_1 + 4x_3 = 3;
   \end{cases}
   $$

   g)

   $$
   \begin{cases}
   3x_1 - x_2 - 2x_3 = 2, \\
   2x_2 - x_3 = -1, \\
   3x_1 - 5x_2 = 3;
   \end{cases}
   $$

   h)

   $$
   \begin{cases}
   -x_1 + 2x_2 + 3x_3 = 0, \\
   x_1 - 4x_2 - 13x_3 = 0, \\
   -3x_1 + 5x_2 + 4x_3 = 0;
   \end{cases}
   $$


   i)

   $$
   \begin{cases}
   x_1 + x_2 + x_3 = 0, \\
   2x_1 + 4x_2 + 3x_3 = 0, \\
   4x_2 + 4x_3 = 0;
   \end{cases}
   $$

   j)

   $$
   \begin{cases}
   x_1 + x_2 + x_3 = -2, \\
   2x_1 + 4x_2 - 3x_3 = 3, \\
   4x_2 + 2x_3 = 2;
   \end{cases}
   $$

   k)

   $$
   \begin{cases}
   4x_1 + 4x_3 = 8, \\
   x_2 - 6x_3 = -3, \\
   3x_1 + x_2 - 3x_3 = 3;
   \end{cases}
   $$

   l)

   $$
   \begin{cases}
   5x_1 - 3x_2 = -7, \\
   -2x_1 + 9x_2 = 4, \\
   2x_1 + 4x_2 = -2;
   \end{cases}
   $$

>>>>>>> e92b450a6eb7229f5b401387041bd6b230d8f396
