# Zrozumienie Granic Ciągów

Ten dokument stanowi krótkie wprowadzenie do pojęcia granic ciągów w analizie matematycznej.

## Czym jest ciąg?

Ciąg to uporządkowana lista liczb. Możemy oznaczyć ciąg jako $(a_n)$, gdzie $n$ jest liczbą naturalną ($n \in \mathbb{N}$). 

Na przykład, ciąg $(a_n) = \frac{1}{n}$ dla $n \ge 1$ wygląda następująco:
$1, \frac{1}{2}, \frac{1}{3}, \frac{1}{4}, \dots$

## Granica ciągu

Granica ciągu to wartość, do której "dążą" wyrazy ciągu. Jeśli ciąg ma granicę, mówimy, że jest **zbieżny**.

### Formalna definicja

Ciąg $(a_n)$ ma granicę $L$, jeśli dla każdej liczby $\epsilon > 0$ istnieje liczba naturalna $N$ taka, że dla wszystkich $n > N$ zachodzi $|a_n - L| < \epsilon$.

Zapisujemy to jako:
$$ 
\lim_{n \to \infty} a_n = L 
$$ 

Ta definicja jest często nazywana **definicją epsilon-N** granicy. Oznacza ona, że bez względu na to, jak małą dodatnią liczbę $\epsilon$ wybierzesz, zawsze możesz znaleźć w ciągu taki punkt ($N$), po którym wszystkie wyrazy znajdują się w odległości mniejszej niż $\epsilon$ od granicy $L$.

### Przykład: Granica ciągu $(a_n) = \frac{1}{n}$

Udowodnijmy, że granica ciągu $(a_n) = \frac{1}{n}$ wynosi 0.

$$ 
\lim_{n \to \infty} \frac{1}{n} = 0 
$$ 

**Dowód:**

Zgodnie z definicją, dla dowolnego $\epsilon > 0$, musimy znaleźć takie $N$, że dla wszystkich $n > N$ zachodzi:
$$ 
\left| \frac{1}{n} - 0 \right| < \epsilon 
$$ 
To upraszcza się do:
$$ 
\frac{1}{n} < \epsilon 
$$ 
Rozwiązując ze względu na $n$, otrzymujemy:
$$ 
n > \frac{1}{\epsilon} 
$$ 
Zatem, jeśli wybierzemy $N$ jako dowolną liczbę całkowitą większą niż $\frac{1}{\epsilon}$, to dla każdego $n > N$ warunek $|a_n - 0| < \epsilon$ będzie spełniony.

Na przykład, jeśli wybierzemy $\epsilon = 0.01$, to musimy znaleźć takie $N$, że dla wszystkich $n > N$, $\frac{1}{n} < 0.01$. Oznacza to $n > 100$. Możemy więc wybrać $N=100$. Dla wszystkich $n > 100$ wyrazy ciągu są bliżej 0 niż 0.01.

To potwierdza, że granica ciągu rzeczywiście wynosi 0.

## Inny przykład: Ciąg stały

Rozważmy ciąg $(b_n) = c$, gdzie $c$ jest stałą. Wyrazy to $c, c, c, \dots$.
Granica tego ciągu to $c$.

$$ 
\lim_{n \to \infty} c = c 
$$ 

**Dowód:**
Dla dowolnego $\epsilon > 0$, musimy znaleźć takie $N$, że dla wszystkich $n > N$:
$$ 
|b_n - c| < \epsilon 
$$ 
Ponieważ $b_n = c$, staje się to:
$$ 
|c - c| = 0 < \epsilon 
$$ 
Ta nierówność jest prawdziwa dla każdego $\epsilon > 0$ i dla wszystkich $n$. Możemy więc wybrać dowolne $N$, na przykład $N=1$.

To pokazuje, że pojęcie granicy jest zgodne z naszą intuicją.

## Szczegółowy dowód: Granica ciągu $(a_n) = \frac{n^2-1}{n^2}$

Przejdźmy przez dowód, że granica ciągu $(a_n) = \frac{n^2-1}{n^2}$ wynosi 1.

**Krok 1: Uprość wyrażenie i zidentyfikuj granicę**

Po pierwsze, często pomocne jest uproszczenie wyrażenia algebraicznego ciągu, aby lepiej zrozumieć jego zachowanie, gdy $n$ staje się bardzo duże.

$$ a_n = \frac{n^2-1}{n^2} = \frac{n^2}{n^2} - \frac{1}{n^2} = 1 - \frac{1}{n^2} $$ 

Gdy $n$ dąży do nieskończoności ($n \to \infty$), wyraz $\frac{1}{n^2}$ zbliża się do 0. Zatem intuicyjnie granica ciągu powinna wynosić $1 - 0 = 1$. Naszym celem jest udowodnienie tego formalnie.

Chcemy udowodnić, że:
$$ \lim_{n \to \infty} \left(1 - \frac{1}{n^2}\right) = 1 $$ 

**Krok 2: Zastosuj definicję Epsilon-N granicy**

Formalna definicja granicy mówi, że dla każdej małej dodatniej liczby $\epsilon$ (epsilon) musimy być w stanie znaleźć odpowiadającą jej liczbę całkowitą $N$, tak aby wszystkie wyrazy ciągu po $N$-tym wyrazie znajdowały się w odległości $\epsilon$ od granicy.

Zapiszmy to matematycznie. Musimy pokazać, że dla każdego $\epsilon > 0$ istnieje takie $N$, że dla wszystkich $n > N$:
$$ |a_n - L| < \epsilon 
$$ 
W naszym przypadku $a_n = 1 - \frac{1}{n^2}$, a granica $L=1$. Podstawiamy to do wzoru:
$$ \left| \left(1 - \frac{1}{n^2}\right) - 1 \right| < \epsilon 
$$ 

**Krok 3: Rozwiąż nierówność ze względu na n**

Teraz upraszczamy wyrażenie wewnątrz wartości bezwzględnej:
$$ \left| -\frac{1}{n^2} \right| < \epsilon 
$$ 
Poniważ wartość bezwzględna liczby ujemnej jest jej dodatnim odpowiednikiem:
$$ \frac{1}{n^2} < \epsilon 
$$ 
Naszym celem jest znalezienie, jakie musi być $n$, aby ta nierówność była prawdziwa. Chcemy wyizolować $n$. Najpierw możemy wziąć odwrotność obu stron. Pamiętaj, aby odwrócić znak nierówności, gdy to robisz:
$$ n^2 > \frac{1}{\epsilon} 
$$ 
Teraz bierzemy pierwiastek kwadratowy z obu stron. Ponieważ $n$ jest dodatnią liczbą całkowitą, musimy wziąć pod uwagę tylko dodatni pierwiastek:
$$ n > \sqrt{\frac{1}{\epsilon}} 
$$ 

**Krok 4: Wybierz N i zakończ dowód**

Ta ostatnia nierówność mówi nam dokładnie, jak znaleźć nasze $N$. Jeśli wybierzemy $N$ jako dowolną liczbę całkowitą większą niż $\sqrt{\frac{1}{\epsilon}}$, to dla każdej liczby całkowitej $n$ większej niż $N$, nasz warunek początkowy $|a_n - 1| < \epsilon$ będzie prawdziwy.

Zobaczmy to na konkretnym przykładzie. Załóżmy, że ktoś rzuci nam wyzwanie z $\epsilon = 0.01$. Musimy znaleźć działające $N$.
Używając naszego wzoru, potrzebujemy $n > \sqrt{\frac{1}{0.01}}$.
$$ n > \sqrt{100} 
$$ 
$$ n > 10 
$$ 
Możemy więc wybrać $N=10$. Gwarantuje to, że dla każdego wyrazu w ciągu, gdzie $n > 10$ (np. $n=11, 12, \dots$), wartość tego wyrazu będzie mniejsza niż $0.01$ od naszej granicy 1.

Ponieważ możemy znaleźć takie $N$ dla *dowolnego* wyboru $\epsilon > 0$, formalnie udowodniliśmy, że:
$$ \lim_{n \to \infty} \frac{n^2-1}{n^2} = 1 
$$ 
