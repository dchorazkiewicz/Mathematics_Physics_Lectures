### **Przewodnik Interaktywny 1.1: Wprowadzenie do Macierzy i Podstawowe Operacje**

---

#### **Cel tego modułu**

Witaj w pierwszym module naszej podróży przez algebrę liniową! Celem tej sesji jest zrozumienie, czym jest macierz i opanowanie fundamentalnych operacji: **dodawania, odejmowania, mnożenia przez skalar** oraz **mnożenia macierzy**. Ten przewodnik to Twoja mapa. Używaj jej, aby prowadzić dialog z AI, które będzie Twoim osobistym tutorem.

Pamiętaj o zasadzie **odwróconej klasy**: ten materiał przerabiasz samodzielnie w domu, aby na zajęciach synchronicznych skupić się na dyskusji i rozwiązywaniu trudniejszych problemów.

---

### **Krok 1: Jak Komunikować się z AI? Prosty Zapis Matematyczny**

Zanim zaczniemy, ustalmy prosty sposób zapisu obiektów matematycznych w czacie. Ja będę pokazywać Ci macierze i wektory w sformatowanej, "książkowej" formie. Ty, aby mi odpowiedzieć, nie musisz używać skomplikowanych narzędzi. Wystarczy prosta konwencja tekstowa.

##### **Zapis wektorów**

Wektory zapisuj jako listę liczb w nawiasach kwadratowych. Przykładowo, wektor:

$$\mathbf{v} = [1, 2, 3]$$

zapisz w czacie jako `v = [1, 2, 3]`.

##### **Zapis macierzy**

Macierze zapisuj jako listę list, gdzie każda wewnętrzna lista to jeden wiersz macierzy. Na przykład macierz:

$$
\mathbf{A} = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}
$$

zapisz jako `A = [[1, 2], [3, 4]]`. Inny przykład to macierz:

$$
\mathbf{D} = \begin{pmatrix} -1 & 2 & 3 \\ 4 & 0 & 6 \end{pmatrix}
$$

którą zapiszesz jako `D = [[-1, 2, 3], [4, 0, 6]]`.

Ten prosty system pozwoli nam się bez problemu komunikować.

---

### **Krok 2: Czym jest Macierz? Budowanie Intuicji**

Zanim zaczniemy cokolwiek liczyć, musimy zrozumieć, z czym pracujemy. Macierz to jedno z centralnych pojęć w matematyce i informatyce.

> **➡️ Twoje zadanie (Dialog z AI):**
> Poproś AI, aby wyjaśniło Ci w prostych słowach, **czym jest macierz**. Zadaj serię pytań, aby zgłębić temat. Zacznij od: *"Co to jest macierz i do czego służy? Podaj mi jakąś intuicyjną analogię z życia codziennego."* Następnie zapytaj: *"Jak opisuje się rozmiar macierzy (wymiary)? Co to znaczy, że macierz jest rozmiaru 3x5?"* Na koniec poproś o przykłady: *"Co to jest macierz kwadratowa, diagonalna, jednostkowa i zerowa? Pokaż mi przykłady."*

---

### **Krok 3: Interaktywna Weryfikacja Wiedzy**

Świetnie! Masz już podstawy teoretyczne. Czas sprawdzić, czy kluczowe pojęcia są dla Ciebie jasne.

> **➡️ Twoje zadanie (Dialog z AI):**
> Poproś AI o przygotowanie krótkiego testu. Powiedz: *"Przygotuj mi 3 proste pytania testowe, które sprawdzą, czy rozumiem pojęcia rozmiaru macierzy, elementu a_ij oraz macierzy kwadratowej. Chcę samodzielnie odpowiedzieć, a Ty sprawdzisz moje odpowiedzi."*

---

### **Krok 4: Podstawowe Operacje – Dodawanie, Odejmowanie i Mnożenie przez Skalar**

Te operacje są bardzo intuicyjne. Opierają się na działaniach na poszczególnych elementach macierzy.

> **➡️ Twoje zadanie (Dialog z AI):**
> Najpierw poproś o teorię, a potem przejdź do praktyki. Zapytaj AI o zasady: *"Jakie są zasady dodawania i odejmowania macierzy? Kiedy można wykonać te działania?"* oraz *"Jak działa mnożenie macierzy przez liczbę (skalar)?"*

#### **Ćwiczenia praktyczne**
Teraz czas na zadania z Twojej listy ćwiczeń. Spróbuj rozwiązać je najpierw samodzielnie na kartce. Jeśli utkniesz, poproś AI o **wskazówkę**, a nie o gotowe rozwiązanie. Pamiętaj, uczymy się krytycznego korzystania z technologii!

##### **Zadanie 1.1**
Oblicz sumę oraz różnicę macierzy:
$$\mathbf{A}+\mathbf{B}$$
$$\mathbf{B}-\mathbf{A}$$
dla:
$$
\mathbf{A}=
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
$$
$$
\mathbf{B}=
\begin{pmatrix}
5 & 6 \\
7 & 8
\end{pmatrix}
$$

##### **Zadanie 1.2**
Oblicz iloczyny macierzy przez skalar:

$$2\mathbf{B}$$

$$-3\mathbf{C}$$

dla:

$$
\mathbf{B}=
\begin{pmatrix}
5 & 6 \\
7 & 8
\end{pmatrix}
$$

$$
\mathbf{C}=
\begin{pmatrix}
-1 & 2 \\
3 & 0
\end{pmatrix}
$$

---

### **Krok 5: Mnożenie Macierzy – Kluczowa i Mniej Oczywista Operacja**

Mnożenie macierzy jest mniej intuicyjne niż dodawanie, ale to jedna z najważniejszych operacji w całej algebrze liniowej. Zrozumienie tej zasady jest absolutnie kluczowe.

> **➡️ Twoje zadanie (Dialog z AI):**
> Poproś AI o dokładne wyjaśnienie: *"Wyjaśnij mi krok po kroku, na czym polega mnożenie macierzy. Użyj schematu 'wiersz razy kolumna'."* Następnie dopytaj o warunek konieczny: *"Jaki warunek muszą spełniać wymiary macierzy, żeby można było je pomnożyć?"* Na koniec, poproś o kluczowy wniosek: *"Pokaż mi na prostym przykładzie, że mnożenie macierzy na ogół nie jest przemienne"*, czyli:
> $$
> \mathbf{A} \cdot \mathbf{B} \neq \mathbf{B} \cdot \mathbf{A}
> $$

#### **Ćwiczenia praktyczne**

Przeanalizujmy wspólnie jeden przykład, a resztę spróbujesz samodzielnie.

##### **Zadanie 1.3 (wspólne)**
Obliczmy iloczyn macierzy:

$$\mathbf{A}\cdot \mathbf{B}$$

gdzie:

$$
\mathbf{A}=
\begin{pmatrix}
\color{red}1 & \color{red}2 \\
3 & 4
\end{pmatrix}
$$

$$
\mathbf{B}=
\begin{pmatrix}
\color{blue}5 & 6 \\
\color{blue}7 & 8
\end{pmatrix}
$$

Element w pierwszym wierszu i pierwszej kolumnie macierzy wynikowej to iloczyn skalarny pierwszego wiersza macierzy A i pierwszej kolumny macierzy B:

$$
(\color{red}{\text{wiersz 1 z A}}) \cdot (\color{blue}{\text{kolumna 1 z B}}) = \color{red}1 \cdot \color{blue}5 + \color{red}2 \cdot \color{blue}7 = 5 + 14 = 19
$$

Teraz samodzielnie oblicz pozostałe trzy elementy. Zweryfikuj wynik z AI.

##### **Zadanie 1.4 (samodzielne)**
Oblicz iloczyny:

$$\mathbf{A} \cdot \mathbf{D}$$

oraz

$$\mathbf{D} \cdot \mathbf{E}$$

Zastanów się, dlaczego nie można obliczyć iloczynu $\mathbf{A} \cdot \mathbf{E}$.

$$
\mathbf{A}=
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
$$

$$
\mathbf{D}=
\begin{pmatrix}
-1 & 2 & 3 \\
4 & 0 & 6
\end{pmatrix}
$$

$$
\mathbf{E}=
\begin{pmatrix}
1 & 2\\
4 & 5\\
7 & 8
\end{pmatrix}
$$

---

### **Krok 6: Podsumowanie i Przygotowanie do Zajęć**

Gratulacje! Przeszedłeś przez fundamenty operacji na macierzach. To solidna baza do dalszej nauki.

#### **Zadanie z Gwiazdką (do prezentacji na zajęciach)**

Rozważ dwie ogólne macierze 2x2:

$$
\mathbf{A}=
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
$$

$$
\mathbf{B}=
\begin{pmatrix}
e & f \\
g & h
\end{pmatrix}
$$

Oblicz iloczyny $\mathbf{A} \cdot \mathbf{B}$ oraz $\mathbf{B} \cdot \mathbf{A}$. Porównaj wyniki i na tej podstawie sformułuj wniosek, jaki warunek musiałyby spełniać elementy obu macierzy, aby ich mnożenie było przemienne. Przygotuj się, aby przedstawić swój tok rozumowania na zajęciach.

#### **Pytania do Refleksji (przygotuj się do dyskusji)**

**1. Pytanie o trudność:** Która koncepcja z dzisiejszego materiału była dla Ciebie najbardziej zaskakująca lub najtrudniejsza do zrozumienia?

**2. Pytanie o zastosowania:** Gdzie w realnym świecie (np. w grafice komputerowej, analizie danych) mogą być wykorzystywane operacje na macierzach, których się dziś nauczyłeś?

**3. Pytanie o narzędzia:** Czy AI pomogło Ci zrozumieć materiał? W którym momencie jego pomoc była najbardziej wartościowa, a gdzie wolałbyś inne wyjaśnienie?

#### **Co dalej?**

W następnym module zajmiemy się **wyznacznikami macierzy**. To potężne narzędzie, które powie nam wiele o właściwościach macierzy i układów równań. Do zobaczenia na zajęciach!