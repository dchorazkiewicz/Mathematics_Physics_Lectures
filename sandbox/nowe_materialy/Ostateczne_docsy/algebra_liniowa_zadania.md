# Dział 1 — Algebra Liniowa: Zadania

Poniżej znajdują się przykładowe zadania do samodzielnego rozwiązania. Dla każdego podrozdziału przygotowano 5 zadań o zróżnicowanym stopniu trudności. Niektóre zadania zawierają podpowiedzi lub sugestie metod rozwiązania.

## Macierze i podstawowe operacje

1. Dla macierzy $A=\begin{pmatrix}1 & 2\\ 3 & 4\end{pmatrix}$ i $B=\begin{pmatrix}0 & -1\\ 2 & 1\end{pmatrix}$ oblicz $A+B$, $A-B$, $2A$ oraz $A\cdot B$. Sprawdź, czy $A\cdot B = B\cdot A$.

2. Dana jest macierz

$$
C=\begin{pmatrix}
1 & 0 & 2\\
-1 & 3 & 1\\
0 & 2 & -1
\end{pmatrix}.
$$

Wyznacz macierz otrzymaną po przestawieniu wierszy: zamień 1. i 3. wiersz, a następnie dodaj do 2. wiersza dwukrotność nowego 1. wiersza.

3. Dla wektorów kolumnowych $u=(1,-2,3)^{\top}$ oraz $v=(2,0,-1)^{\top}$ zapisz je jako macierze i oblicz $u+v$, $u-v$ oraz iloczyny macierzowe $u\,v^{\top}$ i $v\,u^{\top}$. Jaka jest ranga macierzy $u\,v^{\top}$?

4. Pokaż, że macierz diagonalna $D=\operatorname{diag}(2,-3,5)$ jest przemienna z dowolną macierzą diagonalną $E=\operatorname{diag}(a,b,c)$. Dodatkowo oblicz $D^{3}$ oraz, jeśli istnieje, $D^{-1}$.

5. Dla macierzy $P=\begin{pmatrix}1 & 1 & 0\\ 0 & 1 & 1\\ 1 & 0 & 1\end{pmatrix}$ oblicz $P^{2}$ i $P^{3}$. Czy ciąg $P^{n}$ ma zauważalny wzorzec dla $n=1,2,3$?

## Wyznaczniki

1. Oblicz wyznacznik macierzy

$$
A=\begin{pmatrix}
2 & 3 & 1\\
0 & -1 & 4\\
5 & 2 & 0
\end{pmatrix}
$$

używając metody Sarrusa.

2. Wyznacz $\det(B)$ dla

$$
B=\begin{pmatrix}
1 & 2 & 3 & 4\\
0 & 1 & -1 & 2\\
2 & 0 & 1 & 1\\
1 & -1 & 0 & 2
\end{pmatrix}
$$

przez rozwinięcie Laplace'a względem najlepiej nadającego się wiersza lub kolumny.

3. Pokaż, że jeżeli w macierzy dwa wiersze są równe, to wyznacznik jest równy zero. Daj przykład macierzy $3\times3$ z dwoma równymi wierszami i oblicz jej wyznacznik.

4. Oblicz wyznacznik macierzy trójkątnej $T$ o elementach diagonalnych $(3,-2,5,1)$. (Krótka nota: wyznacznik macierzy trójkątnej to iloczyn elementów diagonalnych.)

5. Dla macierzy zależnej od parametru $t$:

$$
M(t)=\begin{pmatrix}
t & 1 & 0\\
2 & t & 3\\
0 & 1 & t
\end{pmatrix}
$$

oblicz $\det(M(t))$ i znajdź wartości $t$, dla których macierz jest singularna.

## Odwracanie macierzy

1. Znajdź macierz odwrotną $A^{-1}$ dla

$$
A=\begin{pmatrix}2 & 1\\ 5 & 3\end{pmatrix}
$$

używając wzoru dla macierzy $2\times2$.

2. Dla macierzy $3\times3$

$$
G=\begin{pmatrix}1 & 2 & 3\\ 0 & 1 & 4\\ 5 & 6 & 0\end{pmatrix}
$$

oblicz macierz odwrotną za pomocą metody Gaussa–Jordana (dołącz macierz jednostkową i wykonaj eliminację).

3. Sprawdź, czy macierz

$$
H=\begin{pmatrix}1 & 2 & 3\\ 2 & 4 & 6\\ 0 & 1 & 1\end{pmatrix}
$$

jest odwracalna. Uzasadnij odpowiedź (użyj wyznacznika lub rangi).

4. Dla macierzy $A$ spełniającej $A^{2}=I$ (tzw. involucja) pokaż, że $A^{-1}=A$. Podaj przykład niebanalnej macierzy $2\times2$ spełniającej ten warunek (innej niż $I$ i $-I$).

5. Oblicz macierz odwrotną macierzy diagonalnej $D=\operatorname{diag}(2,5,-3,1)$, jeżeli istnieje. Omów warunek istnienia odwrotności dla macierzy diagonalnej.


## Układy równań liniowych

1. Rozwiąż układ równań:

$$
\begin{aligned}
2x+3y&=5,\\
x-4y&=-2.
\end{aligned}
$$

Użyj metody eliminacji Gaussa.

2. Rozwiąż układ trzech równań z trzema niewiadomymi:

$$
\begin{aligned}
x+y+z&=6,\\
2x-y+3z&=14,\\
-x+2y-z&=-2.
\end{aligned}
$$

Użyj metody macierzy odwrotnej (jeżeli macierz współczynników jest odwracalna).

3. Zastosuj regułę Cramera, aby rozwiązać układ:

$$
\begin{aligned}
x+2y&=3,\\
3x-y&=5.
\end{aligned}
$$

Pokaż kroki i obliczenia macierzy wyznacznikowych.

4. Rozważ układ parametryczny zależny od $\lambda$:

$$
\begin{aligned}
x+\lambda y&=1,\\
2x+(1+\lambda)y&=3.
\end{aligned}
$$

Określ wartości $\lambda$, dla których układ ma jedno rozwiązanie, nieskończenie wiele rozwiązań lub brak rozwiązań.

5. Dla macierzy współczynników

$$
A=\begin{pmatrix}1 & 1 & 1\\ 0 & 2 & -1\\ 2 & -1 & 3\end{pmatrix}
$$

i wektora prawych stron $b=(4,1,3)^{\top}$ rozwiąż $Ax=b$ i sprawdź wynik przez podstawienie.

---

Plik przygotowany jako przykładowy zestaw zadań. Jeśli chcesz, mogę:

- Rozszerzyć do plików dla działów 2 i 3 w analogicznym stylu.
- Dodać rozwiązania lub wskazówki krok po kroku dla każdego zadania.
- Sformatować zadania jako zestaw egzaminacyjny (numeracja, czas, punktacja).

Powiedz, co mam przygotować dalej.

---

Plik przygotowany jako przykładowy zestaw zadań. Jeśli chcesz, mogę:

- Rozszerzyć do plików dla działów 2 i 3 w analogicznym stylu.
- Dodać rozwiązania lub wskazówki krok po kroku dla każdego zadania.
- Sformatować zadania jako zestaw egzaminacyjny (numeracja, czas, punktacja).

Powiedz, co mam przygotować dalej.
