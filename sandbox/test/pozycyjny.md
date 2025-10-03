## Jak przedstawić liczbę w dowolnym systemie pozycyjnym? Kompletny przewodnik.

Wszyscy jesteśmy przyzwyczajeni do systemu dziesiętnego, ale świat informatyki, matematyki i techniki często korzysta z innych podstaw, takich jak system binarny (dwójkowy), ósemkowy czy szesnastkowy. Zrozumienie, jak dowolna liczba może być reprezentowana w dowolnym systemie, jest kluczową umiejętnością. Okazuje się, że cała procedura opiera się na jednym, eleganckim twierdzeniu matematycznym.

### ## Fundament: Twierdzenie o Dzieleniu z Resztą

Podstawą całej metody jest **Twierdzenie o Dzieleniu z Resztą**. Mówi ono, że dla dowolnej liczby całkowitej $L$ i dowolnej dodatniej liczby całkowitej $b$ (naszej przyszłej podstawy), istnieją **jednoznacznie określone** liczby całkowite:

* $q$ (iloraz)
* $r$ (reszta)

takie, że zachodzi równość:

$$L = q \cdot b + r$$

Najważniejszy jest warunek nałożony na resztę: $0 \le r < b$. Gwarantuje on, że reszta $r$ **zawsze będzie prawidłową cyfrą** w systemie o podstawie $b$ (który używa cyfr od 0 do $b-1$).

---

### ## Cel: Wzór Ogólny na Liczbę

Naszym celem jest przedstawienie liczby $L$ w systemie o podstawie $b$ jako ciąg cyfr $(c_k c_{k-1} ... c_1 c_0)_b$. Jest to skrócony zapis **postaci wielomianowej**:

$$L = c_k \cdot b^k + c_{k-1} \cdot b^{k-1} + \dots + c_1 \cdot b^1 + c_0 \cdot b^0$$

Cała sztuka polega na znalezieniu tych współczynników $c_k, c_{k-1}, \dots, c_0$, które są właśnie cyframi naszej liczby. Zastosowanie twierdzenia o dzieleniu z resztą w pętli (iteracyjnie) pozwala nam je znaleźć jedna po drugiej.

---

### ## Zastosowanie w Praktyce: Rozkład Liczby 23

Aby zobaczyć, jak to działa, przeanalizujemy jeden przykład — rozkład liczby **23** — na trzy różne sposoby, używając dwóch metod prezentacji: tabelarycznej i algebraicznej.

### **Podstawa b = 2 (System Binarny)**

#### **1. Metoda Tabelaryczna (Algorytmiczna)**

Ta metoda jest szybka i idealna do obliczeń. Dzielimy liczbę (a potem kolejne ilorazy) przez podstawę `2` i zapisujemy reszty.

| Dzielenie (L / 2) | Iloraz (q) | Reszta (r) | Cyfra |
| :--- | :---: | :---: | :--- |
| 23 / 2 | 11 | **1** | $c_0$ |
| 11 / 2 | 5 | **1** | $c_1$ |
| 5 / 2 | 2 | **1** | $c_2$ |
| 2 / 2 | 1 | **0** | $c_3$ |
| 1 / 2 | 0 | **1** | $c_4$ |

Gdy iloraz osiąga 0, kończymy. Cyfry odczytujemy od dołu do góry.

**Wynik:** $23_{10} = 10111_2$

#### **2. Metoda Algebraiczna (Wyprowadzenie Wzoru)**

Ta metoda pokazuje, jak z kolejnych dzieleń "buduje się" ostateczny wzór wielomianowy.

* **Krok 1: Zapis zagnieżdżony**

$$23 = 11 \cdot 2 + \mathbf{1}$$

$$23 = (5 \cdot 2 + \mathbf{1}) \cdot 2 + \mathbf{1}$$

$$23 = ((2 \cdot 2 + \mathbf{1}) \cdot 2 + \mathbf{1}) \cdot 2 + \mathbf{1}$$

$$23 = (((1 \cdot 2 + \mathbf{0}) \cdot 2 + \mathbf{1}) \cdot 2 + \mathbf{1}) \cdot 2 + \mathbf{1}$$

$$23 = (((\mathbf{1}) \cdot 2 + \mathbf{0}) \cdot 2 + \mathbf{1}) \cdot 2 + \mathbf{1}) \cdot 2 + \mathbf{1}$$

* **Krok 2: Przejście do postaci wielomianowej**

    Otwierając nawiasy w powyższym wyrażeniu, otrzymujemy:
 
$$23 = \mathbf{1} \cdot 2^4 + \mathbf{0} \cdot 2^3 + \mathbf{1} \cdot 2^2 + \mathbf{1} \cdot 2^1 + \mathbf{1} \cdot 2^0$$
 
    Współczynniki przy potęgach dwójki to nasze cyfry: `10111`.

### **Podstawa b = 3 (System Trójkowy)**

#### **1. Metoda Tabelaryczna**

| Dzielenie (L / 3) | Iloraz (q) | Reszta (r) | Cyfra |
| :--- | :---: | :---: | :--- |
| 23 / 3 | 7 | **2** | $c_0$ |
| 7 / 3 | 2 | **1** | $c_1$ |
| 2 / 3 | 0 | **2** | $c_2$ |

Czytając od dołu: **212**.
**Wynik:** $23_{10} = 212_3$

#### **2. Metoda Algebraiczna**

* **Krok 1: Zapis zagnieżdżony**

$$23 = 7 \cdot 3 + \mathbf{2}$$

$$23 = (\mathbf{2} \cdot 3 + \mathbf{1}) \cdot 3 + \mathbf{2}$$

* **Krok 2: Postać wielomianowa**

$$23 = \mathbf{2} \cdot 3^2 + \mathbf{1} \cdot 3^1 + \mathbf{2} \cdot 3^0$$

    Współczynniki to `212`.

### **Podstawa b = 4 (System Czwórkowy)**

#### **1. Metoda Tabelaryczna**

| Dzielenie (L / 4) | Iloraz (q) | Reszta (r) | Cyfra |
| :--- | :---: | :---: | :--- |
| 23 / 4 | 5 | **3** | $c_0$ |
| 5 / 4 | 1 | **1** | $c_1$ |
| 1 / 4 | 0 | **1** | $c_2$ |

Czytając od dołu: **113**.
**Wynik:** $23_{10} = 113_4$

#### **2. Metoda Algebraiczna**

* **Krok 1: Zapis zagnieżdżony**

$$23 = 5 \cdot 4 + \mathbf{3}$$

$$23 = (\mathbf{1} \cdot 4 + \mathbf{1}) \cdot 4 + \mathbf{3}$$

* **Krok 2: Postać wielomianowa**

$$23 = \mathbf{1} \cdot 4^2 + \mathbf{1} \cdot 4^1 + \mathbf{3} \cdot 4^0$$

    Współczynniki to `113`.

---

### ## Podsumowanie

Jak widać, obie metody prowadzą do tego samego wyniku i są dwiema stronami tego samego medalu.

* **Metoda tabelaryczna** to czysty, mechaniczny algorytm, idealny do szybkich obliczeń.
* **Metoda algebraiczna** daje głębsze zrozumienie, pokazując, jak iteracyjne stosowanie twierdzenia o dzieleniu z resztą bezpośrednio prowadzi do definicji liczby w systemie pozycyjnym.

Opanowanie tego procesu pozwala na swobodne poruszanie się między różnymi systemami liczbowymi i jest fundamentalną wiedzą w wielu dziedzinach nauki.