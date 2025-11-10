# Dział 1 — Algebra Liniowa: Rozwiązania

## Macierze i podstawowe operacje

1. Dla macierzy $A=\begin{pmatrix}1 & 2\\ 3 & 4\end{pmatrix}$ i $B=\begin{pmatrix}0 & -1\\ 2 & 1\end{pmatrix}$:

   - $A+B = \begin{pmatrix}1+0 & 2-1\\ 3+2 & 4+1\end{pmatrix} = \begin{pmatrix}1 & 1\\ 5 & 5\end{pmatrix}$
   - $A-B = \begin{pmatrix}1-0 & 2-(-1)\\ 3-2 & 4-1\end{pmatrix} = \begin{pmatrix}1 & 3\\ 1 & 3\end{pmatrix}$
   - $2A = \begin{pmatrix}2\cdot1 & 2\cdot2\\ 2\cdot3 & 2\cdot4\end{pmatrix} = \begin{pmatrix}2 & 4\\ 6 & 8\end{pmatrix}$
   - $3B-2A = \begin{pmatrix}0 & -3\\ 6 & 3\end{pmatrix} - \begin{pmatrix}2 & 4\\ 6 & 8\end{pmatrix} = \begin{pmatrix}-2 & -7\\ 0 & -5\end{pmatrix}$
   - $A\cdot B = \begin{pmatrix}1\cdot0+2\cdot2 & 1\cdot(-1)+2\cdot1\\ 3\cdot0+4\cdot2 & 3\cdot(-1)+4\cdot1\end{pmatrix} = \begin{pmatrix}4 & 1\\ 8 & 1\end{pmatrix}$
   - $B\cdot A = \begin{pmatrix}0\cdot1+(-1)\cdot3 & 0\cdot2+(-1)\cdot4\\ 2\cdot1+1\cdot3 & 2\cdot2+1\cdot4\end{pmatrix} = \begin{pmatrix}-3 & -4\\ 5 & 8\end{pmatrix}$
   - Sprawdzenie: $A\cdot B \neq B\cdot A$. Mnożenie macierzy nie jest przemienne.

2. Dla macierzy diagonalnych $A, B, C, D$:
Mnożenie macierzy diagonalnych jest przemienne. Wynika to z faktu, że mnożenie odpowiadających sobie elementów na diagonali jest przemienne.
   $A\cdot B = \operatorname{diag}(1\cdot2, 2\cdot4) = \operatorname{diag}(2, 8)$
   $B\cdot A = \operatorname{diag}(2\cdot1, 4\cdot2) = \operatorname{diag}(2, 8)$
   Zatem $A\cdot B = B\cdot A$. Ta właściwość rozszerza się na iloczyn dowolnej liczby macierzy diagonalnych, więc równość $A\cdot B\cdot C\cdot D = B\cdot A\cdot D\cdot C = D\cdot C\cdot B\cdot A$ jest prawdziwa.

## Wyznaczniki

1. Obliczanie wyznaczników metodą Sarrusa:

   - $A=\begin{pmatrix} 2 & 3 & 1\\ 0 & -1 & 4\\ 5 & 2 & 0 \end{pmatrix}$
     $\det(A) = (2 \cdot (-1) \cdot 0) + (3 \cdot 4 \cdot 5) + (1 \cdot 0 \cdot 2) - (1 \cdot (-1) \cdot 5) - (2 \cdot 4 \cdot 2) - (3 \cdot 0 \cdot 0)$
     $\\det(A) = 0 + 60 + 0 - (-5) - 16 - 0 = 60 + 5 - 16 = 49$

   - $B=\begin{pmatrix} 1 & 2 & 2\\ 4 & 0 & 0\\ 7 & 8 & 9 \end{pmatrix}$
     $\\det(B) = (1 \cdot 0 \cdot 9) + (2 \cdot 0 \cdot 7) + (2 \cdot 4 \cdot 8) - (2 \cdot 0 \cdot 7) - (1 \cdot 0 \cdot 8) - (2 \cdot 4 \cdot 9)$
     $\\det(B) = 0 + 0 + 64 - 0 - 0 - 72 = -8$

   - $C=\begin{pmatrix} 3 & 0 & 2\\ 2 & 0 & -2\\ 0 & 1 & 1 \end{pmatrix}$
     $\\det(C) = (3 \cdot 0 \cdot 1) + (0 \cdot (-2) \cdot 0) + (2 \cdot 2 \cdot 1) - (2 \cdot 0 \cdot 0) - (3 \cdot (-2) \cdot 1) - (0 \cdot 2 \cdot 1)$
     $\\det(C) = 0 + 0 + 4 - 0 - (-6) - 0 = 4 + 6 = 10$

2. Wyznaczniki używając rozwinięcia Laplace'a:
   - $C=\begin{pmatrix} 1 & 2 & 3 & 4\\ 0 & 1 & 0 & 0\\ 0 & 0 & 1 & 1\\ 0 & 0 & 0 & 2 \end{pmatrix}$
     Jest to macierz trójkątna górna. Jej wyznacznik jest iloczynem elementów na głównej przekątnej.
     $\\det(C) = 1 \cdot 1 \cdot 1 \cdot 2 = 2$

## Odwracanie macierzy

1. Wzór dla macierzy $2\times2$: $A^{-1} = \frac{1}{\det(A)}\begin{pmatrix}d & -b\\ -c & a\end{pmatrix}$

   - $A=\begin{pmatrix}2 & 1\\ 5 & 3\end{pmatrix}$
     $\\det(A) = 2\cdot3 - 1\cdot5 = 1$
     $A^{-1} = \frac{1}{1}\begin{pmatrix}3 & -1\\ -5 & 2\end{pmatrix} = \begin{pmatrix}3 & -1\\ -5 & 2\end{pmatrix}$

   - $B=\begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}$
     $\\det(B) = 0\cdot0 - 1\cdot1 = -1$
     $B^{-1} = \frac{1}{-1}\begin{pmatrix}0 & -1\\ -1 & 0\end{pmatrix} = \begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix} = B$

   - $C=\begin{pmatrix}4 & 7\\ 2 & 6\end{pmatrix}$
     $\\det(C) = 4\cdot6 - 7\cdot2 = 24 - 14 = 10$
     $C^{-1} = \frac{1}{10}\begin{pmatrix}6 & -7\\ -2 & 4\end{pmatrix} = \begin{pmatrix}0.6 & -0.7\\ -0.2 & 0.4\end{pmatrix}$

## Układy równań liniowych

1. Rozwiąż układ równań:
   $$
   \begin{aligned} 2x+3y&=5 \\ x-4y&=-2 \end{aligned}
   $$
   - **Metoda macierzy odwrotnej**:
     $\\begin{pmatrix}2 & 3\\ 1 & -4\end{pmatrix}\begin{pmatrix}x\\ y\end{pmatrix} = \begin{pmatrix}5\\ -2\end{pmatrix}$
     $A = \begin{pmatrix}2 & 3\\ 1 & -4\end{pmatrix}$, $\\det(A) = -8 - 3 = -11$
     $A^{-1} = \frac{1}{-11}\begin{pmatrix}-4 & -3\\ -1 & 2\end{pmatrix}$
     $\\begin{pmatrix}x\\ y\end{pmatrix} = \frac{1}{-11}\begin{pmatrix}-4 & -3\\ -1 & 2\end{pmatrix}\begin{pmatrix}5\\ -2\end{pmatrix} = \frac{1}{-11}\begin{pmatrix}-20+6\\ -5-4\end{pmatrix} = \frac{1}{-11}\begin{pmatrix}-14\\ -9\end{pmatrix} = \begin{pmatrix}14/11\\ 9/11\end{pmatrix}$
     Rozwiązanie: $x = 14/11$, $y = 9/11$.

2. Rozwiąż układ trzech równań z trzema niewiadomymi:
   $$
   \begin{aligned} x+y+z&=6 \\ 2x-y+3z&=14 \\ -x+2y-z&=-2 \end{aligned}
   $$
   - **Metoda eliminacji Gaussa**:
     $\\begin{pmatrix} 1 & 1 & 1 & | & 6 \\ 2 & -1 & 3 & | & 14 \\ -1 & 2 & -1 & | & -2 \end{pmatrix} \xrightarrow{R_2-2R_1, R_3+R_1} \begin{pmatrix} 1 & 1 & 1 & | & 6 \\ 0 & -3 & 1 & | & 2 \\ 0 & 3 & 0 & | & 4 \end{pmatrix}$
     Z ostatniego wiersza: $3y = 4 \implies y = 4/3$.
     Z drugiego wiersza: $-3y + z = 2 \implies -3(4/3) + z = 2 \implies -4 + z = 2 \implies z = 6$.
     Z pierwszego wiersza: $x+y+z = 6 \implies x + 4/3 + 6 = 6 \implies x = -4/3$.
     Rozwiązanie: $x = -4/3$, $y = 4/3$, $z = 6$.
