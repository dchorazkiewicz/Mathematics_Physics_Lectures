Jasne, oto transkrypcja zadań z przesłanych zdjęć w formacie Markdown z formułami LaTeX.

***

### Strona z ćwiczeniami 1-8

**Wniosek.** Jeżeli w układzie n równań liniowych jednorodnych o n niewiadomych macierz współczynników przy niewiadomych jest nieosobliwa, to układ taki posiada jedynie rozwiązanie zerowe.

**ĆWICZENIA**

**1.** Wypisz inwersje w permutacjach (3, 7, 2, 6, 5, 4, 8, 1), (4, 6, 5, 7, 2, 1, 3).

**2.** Do jakiej klasy należą permutacje (7, 3, 8, 2, 4, 1, 6, 5), (4, 9, 2, 1, 7, 5, 3, 6, 8)?

**3.** Oblicz liczbę inwersji w permutacjach:
a) (n, n-1, n-2, ..., 2, 1);

b) (2n-1, 2n, 2n-3, 2n-2, ..., 1, 2);

c) (1, 3, ..., 2n+1, 2, 4, ..., 2n).

**4.** Dana jest permutacja zbioru początkowych dziewięciu liczb naturalnych. Dobierz liczby i oraz k tak, aby
a) permutacja (1, 2, 7, 4, i, 5, 6, k, 9) była parzysta;

b) permutacja (1, i, 2, 5, k, 4, 8, 9, 7) była nieparzysta.

**5.** Wiadomo, że w permutacji ($a_1, a_2, ..., a_n$) występuje p inwersji. Ile inwersji występuje w permutacji ($a_n, a_{n-1}, ..., a_2, a_1$)?

**6.** Oblicz wyznaczniki następujących macierzy:
a)

$$
\begin{vmatrix}
3 & 7 \\
18 & 5
\end{vmatrix}
$$

b)

$$
\begin{bmatrix}
4 & 7 & 2 \\
-3 & 2 & 1 \\
4 & 5 & 7
\end{bmatrix}
$$

**7.** Oblicz wyznaczniki:
a)

$$
\begin{vmatrix}
\sin x & \cos x \\
-\cos x & \sin x
\end{vmatrix}
$$

b)
$$
\begin{vmatrix}
a+b & a-b \\
a-b & a+b
\end{vmatrix}
$$

**8.** Sprawdź słuszność następujących związków:
a)

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

b)

$$
\begin{vmatrix}
a+bx & b \\
c+dx & d
\end{vmatrix}
=
\begin{vmatrix}
a & b \\
c & d
\end{vmatrix}
$$

***

### Strona 51

**9.** Oblicz wyznaczniki:

a)

$$
\begin{vmatrix}
a & a & a \\
-a & a & a \\
-a & -a & a
\end{vmatrix}
$$

b)

$$
\begin{vmatrix}
a & 0 & b \\
0 & c & 0 \\
d & 0 & a
\end{vmatrix}
$$

c)

$$
\begin{vmatrix}
a & e & f \\
0 & b & g \\
0 & 0 & c
\end{vmatrix}
$$

**10.** Oblicz wyznaczniki:

a)

$$
\begin{vmatrix}
3 & 7 & -2 \\
1 & 4 & 5 \\
3 & 1 & -1
\end{vmatrix}
$$

b)

$$
\begin{vmatrix}
4 & 1 & 5 \\
2 & -3 & 4 \\
-1 & 2 & -2
\end{vmatrix}
$$

c)

$$
\begin{vmatrix}
3 & -2 & 1 \\
7 & -1 & 4 \\
2 & 3 & -2
\end{vmatrix}
$$

**11.** Weźmy pod uwagę macierze:

$A_3 = \begin{bmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{bmatrix}$;

$A'_3 = \begin{bmatrix} a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \\ a_{11} & a_{12} & a_{13} \end{bmatrix}$.

Jaki jest związek między wyznacznikami tych macierzy? Odpowiedź na to samo pytanie dla macierzy

$A = \begin{bmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \dots & \dots & \dots & \dots \\ a_{n1} & a_{n2} & \dots & a_{nn} \end{bmatrix}$;

$A' = \begin{bmatrix} a_{21} & a_{22} & \dots & a_{2n} \\ a_{31} & a_{32} & \dots & a_{3n} \\ \dots & \dots & \dots & \dots \\ a_{n1} & a_{n2} & \dots & a_{nn} \\ a_{11} & a_{12} & \dots & a_{1n} \end{bmatrix}$.

**12.** Bez obliczania wyznacznika udowodnij, że jest on podzielny przez a) 3, 
b) 4, 
c) 5:
a)

$$
\begin{vmatrix}
2 & 5 & 7 \\
4 & 3 & 2 \\
1 & 4 & 2
\end{vmatrix}
$$

b)

$$
\begin{vmatrix}
7 & -2 & 4 \\
3 & 1 & 5 \\
3 & 9 & -7
\end{vmatrix}
$$

c)

$$
\begin{vmatrix}
4 & 1 & 3 \\
2 & 5 & 7 \\
4 & 4 & 5
\end{vmatrix}
$$

**13.** Wykaż, że zachodzą następujące równości:

a)

$$
\begin{vmatrix}
3a-1 & a & 2a \\
6a-1 & 2a-1 & 5a \\
4a & a & 3a+1
\end{vmatrix} = (a-1)^2(a+1)
$$

b)

$$
\begin{vmatrix}
1 & a & -b \\
1 & 2a & a+b \\
1 & a & a-2b
\end{vmatrix} = a(a-b)
$$

***

### Strona 52

**14.** Oblicz wyznaczniki:

a)

$$
\begin{vmatrix}
3 & 1 & 1 & 1 \\
1 & 3 & 1 & 1 \\
1 & 1 & 3 & 1 \\
1 & 1 & 1 & 3
\end{vmatrix}
$$

b)

$$
\begin{vmatrix}
1 & 2 & 3 & 4 \\
2 & 3 & 4 & 1 \\
3 & 4 & 1 & 2 \\
4 & 1 & 2 & 3
\end{vmatrix}
$$

c)

$$
\begin{vmatrix}
x & y & x+y \\
y & x+y & x \\
x+y & x & y
\end{vmatrix}
$$

d)

$$
\begin{vmatrix}
1 & 5 & 7 & -2 \\
4 & 3 & 1 & -1 \\
2 & 3 & -2 & 1 \\
4 & -1 & 2 & -3
\end{vmatrix}
$$

e)

$$
\begin{vmatrix}
7 & 3 & 2 & 1 \\
4 & 5 & -1 & 4 \\
3 & 2 & 1 & 1 \\
0 & 5 & 3 & 2
\end{vmatrix}
$$

f)

$$
\begin{vmatrix}
4 & 3 & -1 & 2 \\
2 & 2 & 3 & 7 & 4 \\
8 & -4 & 2 & 1 \\
7 & 3 & -5 & 4
\end{vmatrix}
$$

**15.** Dana jest macierz
$A = \begin{bmatrix} 1 & x & a \\ 2 & -a & 3 \\ 4 & -1 & x \end{bmatrix}$.
a) Wypisz przekątne tej macierzy odpowiadające następującym permutacjom wskaźników kolumn: (1, 3, 2), (3, 1, 2), (2, 1, 3).

b) Dla podanych przekątnych oblicz iloczyny przekątniowe.

c) Oblicz wszystkie iloczyny przekątniowe macierzy A oraz ich sumę.

d) Oblicz wyznacznik macierzy A metodą Sarrusa oraz przez rozwinięcie według elementów pierwszej kolumny.

**16.** Oblicz wyznaczniki:
a)

$$
\begin{vmatrix}
1 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 3
\end{vmatrix}
$$

b)

$$
\begin{vmatrix}
1 & 0 & 0 & 0 \\
0 & 2 & 0 & 0 \\
0 & 0 & 3 & 0 \\
0 & 0 & 0 & 4
\end{vmatrix}
$$

c)

$$
\begin{vmatrix}
1 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 3 & 0 & 0 \\
0 & 0 & 0 & 3 & 0 \\
0 & 0 & 0 & 0 & 5
\end{vmatrix}
$$

d)

$$
\begin{vmatrix}
1 & a & a \\
0 & 2 & a \\
0 & 0 & 3
\end{vmatrix}
$$

e)

$$
\begin{vmatrix}
1 & a & a & a \\
0 & 2 & a & a \\
0 & 0 & 3 & a \\
0 & 0 & 0 & 4
\end{vmatrix}
$$

f)

$$
\begin{vmatrix}
1 & a & a & a & a \\
0 & 1 & a & a & a \\
0 & 0 & 3 & a & a \\
0 & 0 & 0 & 3 & a \\
0 & 0 & 0 & 0 & 5
\end{vmatrix}
$$

**17.** Dana jest macierz kwadratowa A stopnia n-tego. Tworzymy macierz A' wypisując kolumny macierzy A w odwrotnej kolejności. Jaki jest związek między wyznacznikami tych macierzy?

***

### Strona 53

**18.** Wykaż, że zachodzi równość

$$
\begin{vmatrix}
1 & 1 & 1 \\
x & y & z \\
x^2 & y^2 & z^2
\end{vmatrix}
= (z-x)(z-y)(y-x)
$$

Udowodnij podobną równość dla wyznacznika
$$
\begin{vmatrix}
1 & 1 & 1 & 1 \\
x & y & z & u \\
x^2 & y^2 & z^2 & u^2 \\
x^3 & y^3 & z^3 & u^3
\end{vmatrix}
$$

**19.** Wyznacz macierz odwrotną względem macierzy A postaci:
a) $\begin{bmatrix} 1 & 2 \\ 2 & 5 \end{bmatrix}$

b) $\begin{bmatrix} 1 & 2 \\ 3 & 7 \end{bmatrix}$

c) $\begin{bmatrix} 1 & 2 & -3 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{bmatrix}$

d) $\begin{bmatrix} 4 & 2 & 3 \\ 2 & 1 & 2 \\ 5 & 2 & 4 \end{bmatrix}$

e) $\begin{bmatrix} 2 & 2 & 3 \\ 1 & -1 & 0 \\ -1 & 2 & 1 \end{bmatrix}$

f) $\begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & -1 \\ 1 & -1 & 1 \\ 1 & -1 & -1 \end{bmatrix}$

g) $\begin{bmatrix} 2 & 1 & 0 & 0 \\ 3 & 2 & 0 & 0 \\ 1 & 1 & 3 & 4 \\ 2 & -1 & 2 & 3 \end{bmatrix}$

**20.** Rozwiąż równania macierzowe:
a) $\begin{bmatrix} 2 & 5 \\ 1 & 3 \end{bmatrix} \cdot X = \begin{bmatrix} 4 & -6 \\ 2 & 1 \end{bmatrix}$

b) $\begin{bmatrix} 2 & 1 \\ 5 & 3 \end{bmatrix} \cdot X = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$
Jasne, oto transkrypcja zadań z przesłanych zdjęć w formacie Markdown z formułami LaTeX.

***

### Strona z ćwiczeniami 1-8

**Wniosek.** Jeżeli w układzie n równań liniowych jednorodnych o n niewiadomych macierz współczynników przy niewiadomych jest nieosobliwa, to układ taki posiada jedynie rozwiązanie zerowe.

**ĆWICZENIA**

**1.** Wypisz inwersje w permutacjach (3, 7, 2, 6, 5, 4, 8, 1), (4, 6, 5, 7, 2, 1, 3).

**2.** Do jakiej klasy należą permutacje (7, 3, 8, 2, 4, 1, 6, 5), (4, 9, 2, 1, 7, 5, 3, 6, 8)?

**3.** Oblicz liczbę inwersji w permutacjach:
a) (n, n-1, n-2, ..., 2, 1);

b) (2n-1, 2n, 2n-3, 2n-2, ..., 1, 2);

c) (1, 3, ..., 2n+1, 2, 4, ..., 2n).

**4.** Dana jest permutacja zbioru początkowych dziewięciu liczb naturalnych. Dobierz liczby i oraz k tak, aby
a) permutacja (1, 2, 7, 4, i, 5, 6, k, 9) była parzysta;

b) permutacja (1, i, 2, 5, k, 4, 8, 9, 7) była nieparzysta.

**5.** Wiadomo, że w permutacji ($a_1, a_2, ..., a_n$) występuje p inwersji. Ile inwersji występuje w permutacji ($a_n, a_{n-1}, ..., a_2, a_1$)?

**6.** Oblicz wyznaczniki następujących macierzy:
a)

$$
\begin{vmatrix}
3 & 7 \\
18 & 5
\end{vmatrix}
$$

b)

$$
\begin{bmatrix}
4 & 7 & 2 \\
-3 & 2 & 1 \\
4 & 5 & 7
\end{bmatrix}
$$

**7.** Oblicz wyznaczniki:
a)

$$
\begin{vmatrix}
\sin x & \cos x \\
-\cos x & \sin x
\end{vmatrix}
$$

b)
$$
\begin{vmatrix}
a+b & a-b \\
a-b & a+b
\end{vmatrix}
$$

**8.** Sprawdź słuszność następujących związków:
a)

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

b)

$$
\begin{vmatrix}
a+bx & b \\
c+dx & d
\end{vmatrix}
=
\begin{vmatrix}
a & b \\
c & d
\end{vmatrix}
$$

***

### Strona 51

**9.** Oblicz wyznaczniki:

a)

$$
\begin{vmatrix}
a & a & a \\
-a & a & a \\
-a & -a & a
\end{vmatrix}
$$

b)

$$
\begin{vmatrix}
a & 0 & b \\
0 & c & 0 \\
d & 0 & a
\end{vmatrix}
$$

c)

$$
\begin{vmatrix}
a & e & f \\
0 & b & g \\
0 & 0 & c
\end{vmatrix}
$$

**10.** Oblicz wyznaczniki:

a)

$$
\begin{vmatrix}
3 & 7 & -2 \\
1 & 4 & 5 \\
3 & 1 & -1
\end{vmatrix}
$$

b)

$$
\begin{vmatrix}
4 & 1 & 5 \\
2 & -3 & 4 \\
-1 & 2 & -2
\end{vmatrix}
$$

c)

$$
\begin{vmatrix}
3 & -2 & 1 \\
7 & -1 & 4 \\
2 & 3 & -2
\end{vmatrix}
$$

**11.** Weźmy pod uwagę macierze:

$A_3 = \begin{bmatrix} a_{11} & a_{12} & a_{13} \\\ a_{21} & a_{22} & a_{23} \\\ a_{31} & a_{32} & a_{33} \end{bmatrix}$;

$A'_3 = \begin{bmatrix} a_{21} & a_{22} & a_{23} \\\ a_{31} & a_{32} & a_{33} \\\ a_{11} & a_{12} & a_{13} \end{bmatrix}$.

Jaki jest związek między wyznacznikami tych macierzy? Odpowiedź na to samo pytanie dla macierzy

$A = \begin{bmatrix} a_{11} & a_{12} & \dots & a_{1n} \\\ a_{21} & a_{22} & \dots & a_{2n} \\\ \dots & \dots & \dots & \dots \\\ a_{n1} & a_{n2} & \dots & a_{nn} \end{bmatrix}$;

$A' = \begin{bmatrix} a_{21} & a_{22} & \dots & a_{2n} \\\ a_{31} & a_{32} & \dots & a_{3n} \\\ \dots & \dots & \dots & \dots \\\ a_{n1} & a_{n2} & \dots & a_{nn} \\\ a_{11} & a_{12} & \dots & a_{1n} \end{bmatrix}$.

**12.** Bez obliczania wyznacznika udowodnij, że jest on podzielny przez a) 3, 
b) 4, 
c) 5:
a)

$$
\begin{vmatrix}
2 & 5 & 7 \\
4 & 3 & 2 \\
1 & 4 & 2
\end{vmatrix}
$$

b)

$$
\begin{vmatrix}
7 & -2 & 4 \\
3 & 1 & 5 \\
3 & 9 & -7
\end{vmatrix}
$$

c)

$$
\begin{vmatrix}
4 & 1 & 3 \\
2 & 5 & 7 \\
4 & 4 & 5
\end{vmatrix}
$$

**13.** Wykaż, że zachodzą następujące równości:

a)

$$
\begin{vmatrix}
3a-1 & a & 2a \\
6a-1 & 2a-1 & 5a \\
4a & a & 3a+1
\end{vmatrix} = (a-1)^2(a+1)
$$

b)

$$
\begin{vmatrix}
1 & a & -b \\
1 & 2a & a+b \\
1 & a & a-2b
\end{vmatrix} = a(a-b)
$$

***

### Strona 52

**14.** Oblicz wyznaczniki:

a)

$$
\begin{vmatrix}
3 & 1 & 1 & 1 \\
1 & 3 & 1 & 1 \\
1 & 1 & 3 & 1 \\
1 & 1 & 1 & 3
\end{vmatrix}
$$

b)

$$
\begin{vmatrix}
1 & 2 & 3 & 4 \\
2 & 3 & 4 & 1 \\
3 & 4 & 1 & 2 \\
4 & 1 & 2 & 3
\end{vmatrix}
$$

c)

$$
\begin{vmatrix}
x & y & x+y \\
y & x+y & x \\
x+y & x & y
\end{vmatrix}
$$

d)

$$
\begin{vmatrix}
1 & 5 & 7 & -2 \\
4 & 3 & 1 & -1 \\
2 & 3 & -2 & 1 \\
4 & -1 & 2 & -3
\end{vmatrix}
$$

e)
$$
\begin{vmatrix}
7 & 3 & 2 & 1 \\
4 & 5 & -1 & 4 \\
3 & 2 & 1 & 1 \\
0 & 5 & 3 & 2
\end{vmatrix}
$$

f)
$$
\begin{vmatrix}
4 & 3 & -1 & 2 \\
2 & 2 & 3 & 7 & 4 \\
8 & -4 & 2 & 1 \\
7 & 3 & -5 & 4
\end{vmatrix}
$$

**15.** Dana jest macierz
$A = \begin{bmatrix} 1 & x & a \\\ 2 & -a & 3 \\\ 4 & -1 & x \end{bmatrix}$.
a) Wypisz przekątne tej macierzy odpowiadające następującym permutacjom wskaźników kolumn: (1, 3, 2), (3, 1, 2), (2, 1, 3).

b) Dla podanych przekątnych oblicz iloczyny przekątniowe.

c) Oblicz wszystkie iloczyny przekątniowe macierzy A oraz ich sumę.

d) Oblicz wyznacznik macierzy A metodą Sarrusa oraz przez rozwinięcie według elementów pierwszej kolumny.

**16.** Oblicz wyznaczniki:
a)

$$
\begin{vmatrix}
1 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 3
\end{vmatrix}
$$

b)
$$
\begin{vmatrix}
1 & 0 & 0 & 0 \\
0 & 2 & 0 & 0 \\
0 & 0 & 3 & 0 \\
0 & 0 & 0 & 4
\end{vmatrix}
$$

c)
$$
\begin{vmatrix}
1 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 3 & 0 & 0 \\
0 & 0 & 0 & 3 & 0 \\
0 & 0 & 0 & 0 & 5
\end{vmatrix}
$$

d)
$$
\begin{vmatrix}
1 & a & a \\
0 & 2 & a \\
0 & 0 & 3
\end{vmatrix}
$$

e)
$$
\begin{vmatrix}
1 & a & a & a \\
0 & 2 & a & a \\
0 & 0 & 3 & a \\
0 & 0 & 0 & 4
\end{vmatrix}
$$

f)
$$
\begin{vmatrix}
1 & a & a & a & a \\
0 & 1 & a & a & a \\
0 & 0 & 3 & a & a \\
0 & 0 & 0 & 3 & a \\
0 & 0 & 0 & 0 & 5
\end{vmatrix}
$$

**17.** Dana jest macierz kwadratowa A stopnia n-tego. Tworzymy macierz A' wypisując kolumny macierzy A w odwrotnej kolejności. Jaki jest związek między wyznacznikami tych macierzy?

***

### Strona 53

**18.** Wykaż, że zachodzi równość

$$
\begin{vmatrix}
1 & 1 & 1 \\
x & y & z \\
x^2 & y^2 & z^2
\end{vmatrix}
= (z-x)(z-y)(y-x)
$$

Udowodnij podobną równość dla wyznacznika
$$
\begin{vmatrix}
1 & 1 & 1 & 1 \\
x & y & z & u \\
x^2 & y^2 & z^2 & u^2 \\
x^3 & y^3 & z^3 & u^3
\end{vmatrix}
$$

**19.** Wyznacz macierz odwrotną względem macierzy A postaci:
a) $\begin{bmatrix} 1 & 2 \\\ 2 & 5 \end{bmatrix}$

b) $\begin{bmatrix} 1 & 2 \\\ 3 & 7 \end{bmatrix}$

c) $\begin{bmatrix} 1 & 2 & -3 \\\ 0 & 1 & 2 \\\ 0 & 0 & 1 \end{bmatrix}$

d) $\begin{bmatrix} 4 & 2 & 3 \\\ 2 & 1 & 2 \\\ 5 & 2 & 4 \end{bmatrix}$

e) $\begin{bmatrix} 2 & 2 & 3 \\\ 1 & -1 & 0 \\\ -1 & 2 & 1 \end{bmatrix}$

f) $\begin{bmatrix} 1 & 1 & 1 \\\ 1 & 1 & -1 \\\ 1 & -1 & 1 \\\ 1 & -1 & -1 \end{bmatrix}$

g) $\begin{bmatrix} 2 & 1 & 0 & 0 \\\ 3 & 2 & 0 & 0 \\\ 1 & 1 & 3 & 4 \\\ 2 & -1 & 2 & 3 \end{bmatrix}$

**20.** Rozwiąż równania macierzowe:
a) $\begin{bmatrix} 2 & 5 \\\ 1 & 3 \end{bmatrix} \cdot X = \begin{bmatrix} 4 & -6 \\\ 2 & 1 \end{bmatrix}$

b) $\begin{bmatrix} 2 & 1 \\\ 5 & 3 \end{bmatrix} \cdot X = \begin{bmatrix} 1 & 2 \\\ 3 & 4 \end{bmatrix}$

c) $X \cdot \begin{bmatrix} 1 & 1 & -1 \\\ 2 & 1 & 0 \\\ 1 & -1 & 1 \end{bmatrix} = \begin{bmatrix} 1 & -3 & 3 \\\ 4 & 3 & 2 \\\ 1 & -2 & 5 \end{bmatrix}$

d) $\begin{bmatrix} 3 & 2 & 3 \\\ 1 & 1 & 2 \\\ 3 & 2 & 4 \end{bmatrix} \cdot X = \begin{bmatrix} 1 & 2 & 3 \\\ 1 & -1 & 2 \\\ 2 & 2 & 4 \end{bmatrix}$

***

### Strona 62

**7°. Rozwiążemy jeszcze układ równań**
$$
\begin{cases}
x_1 - 4x_2 + 4x_3 = 0, \\
2x_1 + x_2 + 2x_3 = 0, \\
x_1 - x_2 + 2x_3 = 0.
\end{cases}
$$

Eliminując $x_1$ z równań drugiego i trzeciego otrzymamy
$$
\begin{cases}
x_1 - 4x_2 + 4x_3 = 0, \\
9x_2 - 6x_3 = 0, \\
3x_2 - 2x_3 = 0.
\end{cases}
$$

Wyrugowanie niewiadomej $x_2$ z równań pierwszego i trzeciego prowadzi do układu
$$
\begin{cases}
x_1 + \frac{4}{3}x_3 = 0, \\
x_2 - \frac{2}{3}x_3 = 0, \\
0 = 0.
\end{cases}
$$

Odrzucając równość $0=0$ otrzymamy układ dwóch równań, który ma nieskończenie wiele rozwiązań postaci $(-\frac{4}{3}x_3, \frac{2}{3}x_3, x_3)$.

**ĆWICZENIA**

**1. Rozwiąż układy równań:**
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

***

### Strona 63

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

m)
$$
\begin{cases}
5x_1 - 3x_2 - 7x_3 + x_4 = 10, \\
-x_1 + 2x_2 + 6x_3 - 3x_4 = -3, \\
x_1 + x_2 + 4x_3 - 5x_4 = 0;
\end{cases}
$$

n)
$$
\begin{cases}
x_1 + 2x_2 = 1, \\
-3x_1 + 2x_2 = -2, \\
2x_1 + 3x_2 = 1;
\end{cases}
$$

o)
$$
\begin{cases}
2x_1 + x_2 - x_3 - x_4 = 1, \\
-x_1 - 2x_2 + x_3 - 2x_4 = 0, \\
5x_1 + x_2 - 2x_3 - 5x_4 = 3;
\end{cases}
$$

p)
$$
\begin{cases}
-x_1 + 3x_2 + 3x_3 + 2x_4 + 5x_5 = 2, \\
-3x_1 + 5x_2 + 2x_3 + 3x_4 + 4x_5 = 2, \\
-3x_1 + x_2 - 5x_3 - 7x_5 = -2, \\
-5x_1 + 7x_2 + x_3 + 16x_4 + x_5 = 10;
\end{cases}
$$

q)
$$
\begin{cases}
2x_1 - x_2 - x_3 - x_4 = 0, \\
2x_1 - x_2 - 3x_4 = 0, \\
3x_1 - x_3 + x_4 = 0, \\
2x_1 + 2x_2 - 2x_3 + 5x_4 = 0;
\end{cases}
$$

r)
$$
\begin{cases}
x_1 + x_2 - 3x_3 = -1, \\
2x_1 + x_2 - 2x_3 = 1, \\
x_1 + x_2 + x_3 = 3, \\
x_1 + 2x_2 - 3x_3 = 1;
\end{cases}
$$

s)
$$
\begin{cases}
2x_1 + x_2 + x_3 = 2, \\
x_1 + 3x_2 + x_3 = 5, \\
x_1 + x_2 + 5x_3 = -7, \\
2x_1 + 3x_2 - 3x_3 = 14;
\end{cases}
$$

t)
$$
\begin{cases}
2x_1 - x_2 + 3x_3 = 3, \\
3x_1 + x_2 - 5x_3 = 0, \\
4x_1 - x_2 + x_3 = 3, \\
x_1 + 3x_2 - 13x_3 = -6;
\end{cases}
$$

u)
$$
\begin{cases}
x_1 + 3x_2 + 2x_3 = 0, \\
2x_1 - x_2 + 3x_3 = 0, \\
3x_1 - 5x_2 + 4x_3 = 0, \\
x_1 + 17x_2 + 4x_3 = 0;
\end{cases}
$$

w)
$$
\begin{cases}
2x_1 + x_2 - x_3 + x_4 = 1, \\
3x_1 - 2x_2 + 2x_3 - 3x_4 = 2, \\
5x_1 + x_2 - x_3 + 2x_4 = -1, \\
2x_1 - x_2 + x_3 - 3x_4 = 4;
\end{cases}
$$

***

### Strona z ćwiczeniami 2-6

x)
$$
\begin{cases}
2x_1 - x_2 + x_3 - x_4 = 1, \\
2x_1 - x_2 - 3x_4 = 2, \\
3x_1 - x_3 + x_4 = -3, \\
2x_1 + 2x_2 - 2x_3 + 5x_4 = -6.
\end{cases}
$$

**2. Wykaż, że układ równań**
$$
\begin{cases}
-4x_1 + 3x_2 + ax_3 = c, \\
5x_1 - 4x_2 + bx_3 = d
\end{cases}
$$
posiada rozwiązanie przy wszelkich wartościach a, b, c, d.

**3. Dla jakich wartości a, b, c, układ równań**
$$
\begin{cases}
-4x_1 + 3x_2 = a, \\
5x_1 - 4x_2 = b, \\
-3x_1 + 2x_2 = c
\end{cases}
$$
posiada rozwiązanie?

**4. Dla jakiej wartości a układ równań**
$$
\begin{cases}
x_1 + 3x_2 - 2x_3 = 2, \\
3x_1 + 9x_2 - 2x_3 = 2, \\
2x_1 + 6x_2 + x_3 = a
\end{cases}
$$
ma rozwiązanie?

**5. Zbadaj, kiedy układ równań**
$$
\begin{cases}
x_1 - 3x_2 = 2, \\
3x_1 + ax_2 = 6, \\
2x_1 - 6x_2 = b
\end{cases}
$$
ma rozwiązanie.

**6. Zbadaj, kiedy układ równań**
$$
\begin{cases}
2ax_1 + x_2 + x_3 = 4, \\
x_1 + ax_2 + x_3 = 3, \\
x_1 + 2ax_2 + x_3 = 4
\end{cases}
$$
ma rozwiązanie.