# **Przewodnik Interaktywny 1.1: Wprowadzenie do Macierzy i Podstawowe Operacje**

---

## **Cel tego modułu**

Witaj w pierwszym module naszej podróży przez algebrę liniową! Ten przewodnik to Twoja mapa. Używaj jej, aby prowadzić dialog z AI, które będzie Twoim osobistym tutorem.

Pamiętaj o zasadzie **odwróconej klasy**: ten materiał przerabiasz samodzielnie w domu wypracowując samodzielnie intuicję, aby na zajęciach skupić się na dyskusji i rozwiązywaniu trudniejszych problemów.

**Celem tej sesji jest:** 
- zrozumienie, czym jest macierz
- opanowanie fundamentalnych operacji: dodawania, odejmowania, mnożenia przez skalar 
- mnożenia macierzy.

---

## **Krok 1: Jak Komunikować się z AI? Prosty Zapis Matematyczny**

Zanim zaczniemy, ustalmy prosty sposób zapisu obiektów matematycznych w czacie. Ja będę pokazywać Ci macierze i wektory w sformatowanej, "książkowej" formie. Ty, aby mi odpowiedzieć, nie musisz używać skomplikowanych narzędzi. Wystarczy prosta konwencja tekstowa.

### **Zapis wektorów**

Wektory zapisuj jako listę liczb w nawiasach kwadratowych. Przykładowo, wektor:

$$
\mathbf{v} = [1, 2, 3]
$$

zapisz w czacie jako `v = [1, 2, 3]`.

### **Zapis macierzy**

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

## **Krok 2: Czym jest Macierz?**

### **Krok 2.1: Teoria**

Zanim zaczniemy cokolwiek liczyć, musimy zrozumieć, z czym pracujemy. Macierz to jedno z centralnych pojęć w matematyce i informatyce. 

**Twoje zadanie (Dialog z AI):**

> Poproś AI, aby wyjaśniło Ci w prostych słowach, **czym jest macierz**. Zadaj serię pytań, aby zgłębić temat. Zacznij od: *"Co to jest macierz i do czego służy? Podaj mi jakąś intuicyjną analogię z życia codziennego."* Następnie zapytaj: *"Jak opisuje się rozmiar macierzy (wymiary)? Co to znaczy, że macierz jest rozmiaru 3x5?"* Na koniec poproś o przykłady: *"Co to jest macierz kwadratowa, diagonalna, jednostkowa i zerowa? Pokaż mi przykłady."*

### **Krok 2.2: Praktyka**

Świetnie! Masz już podstawy teoretyczne. Czas sprawdzić, czy kluczowe pojęcia są dla Ciebie jasne. Stosuj mini-quizy, aby utrwalić wiedzę.

**Twoje zadanie (Dialog z AI):**

> Poproś AI o przygotowanie krótkiego **mini-quizu**. Powiedz: *"Przygotuj mi interaktywny mini-quiz zawierający cztery proste pytania testowe, które sprawdzą, czy rozumiem pojęcia rozmiaru macierzy, elementu a_ij oraz macierzy kwadratowej. Chcę samodzielnie odpowiedzieć, a Ty sprawdzisz moje odpowiedzi."*

---

## **Krok 3: Podstawowe Operacje – Dodawanie, Odejmowanie i Mnożenie przez Skalar**

### **Krok 3.1: Teoria**

Te operacje są bardzo intuicyjne. Opierają się na działaniach na poszczególnych elementach macierzy.

**Twoje zadanie (Dialog z AI):**

> Najpierw poproś o teorię, a potem przejdź do praktyki. Zapytaj AI o zasady: *"Jakie są zasady dodawania i odejmowania macierzy? Kiedy można wykonać te działania?"* oraz *"Jak działa mnożenie macierzy przez liczbę (skalar)?"*

### **Krok 3.2: Praktyka**

Teraz czas na zadania z Twojej listy ćwiczeń. Spróbuj rozwiązać je najpierw samodzielnie na kartce. Jeśli utkniesz, poproś AI o **wskazówkę**, a nie o gotowe rozwiązanie. Pamiętaj, uczymy się krytycznego korzystania z technologii!

#### **Zadanie**

Oblicz sumę oraz różnicę macierzy:

$$
\mathbf{A}+\mathbf{B}
$$

$$
\mathbf{B}-\mathbf{A}
$$

dla macierzy:

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

#### **Zadanie**
Oblicz iloczyny macierzy przez skalar:

$$
2\mathbf{B}
$$

$$
-3\mathbf{C}
$$

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

## **Krok 4: Mnożenie Macierzy**

### **Krok 4.1: Teoria**

Mnożenie macierzy jest mniej intuicyjne niż dodawanie, ale to jedna z najważniejszych operacji w całej algebrze liniowej. Zrozumienie tej zasady jest absolutnie kluczowe.

**Twoje zadanie (Dialog z AI):**

> Poproś AI o dokładne wyjaśnienie: *"Wyjaśnij mi krok po kroku, na czym polega mnożenie macierzy. Użyj schematu 'wiersz razy kolumna'."* Następnie dopytaj o warunek konieczny: "Jaki warunek muszą spełniać wymiary macierzy, żeby można było je pomnożyć?

**Twoje zadanie (Dialog z AI):**

> Zapytaj AI: *"Czy mnożenie macierzy jest przemienne? Jeśli nie, to dlaczego?"* Poproś o prosty przykład: *"Pokaż mi na prostym przykładzie, że mnożenie macierzy na ogół nie jest przemienne"*, czyli:
> 
> $$
> \mathbf{A} \cdot \mathbf{B} \neq \mathbf{B} \cdot \mathbf{A}
> $$

### **Krok 4.2: Praktyka**

Przeanalizujmy wspólnie jeden przykład, a resztę spróbujesz samodzielnie.

#### **Zadanie**

Obliczmy iloczyn macierzy:

$$\mathbf{A}\cdot \mathbf{B}$$

gdzie:

$$
\mathbf{A}=
\begin{pmatrix}
\color{red}1 & \color{red}2\\
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
({\color{red}{\text{wiersz 1 z A}}}) \cdot ({\color{blue}{\text{kolumna 1 z B}}}) = {\color{red}1} \cdot {\color{blue}5} + {\color{red}2} \cdot {\color{blue}7} = 5 + 14 = 19
$$

Teraz samodzielnie oblicz pozostałe trzy wynikowe elementy. Zweryfikuj wynik z AI.

#### **Zadanie**

Dla macierzy:

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

oblicz iloczyny:

$$\mathbf{A} \cdot \mathbf{D}$$

oraz

$$\mathbf{D} \cdot \mathbf{E}$$

Zastanów się, dlaczego nie można obliczyć iloczynu $\mathbf{A} \cdot \mathbf{E}$.

#### **Zadanie**

**Twoje zadanie (Dialog z AI):**
> Zapytaj: *"Pokaż mi jak wygląda podniesienie macierzy 3x3 do potęgi 3."*

---

## **Krok 5: Podsumowanie**

Gratulacje! Przeszedłeś przez fundamenty definicji macierzy i operacji na macierzach. 

### **5.1 Końcowy Quiz**

Możesz teraz kompleksowo sprawdzić swoją wiedzę pod egzamin z przedmiotu. Zapytaj AI o quiz podsumowujący cały materiał do samodzielnego wykonania:

> *"Przygotuj mi quiz z 10 trudnymi pytaniami, które sprawdzą pod egzamin moją wiedzę na temat dodawania, odejmowania, mnożenia przez skalar oraz mnożenia macierzy. Chcę samodzielnie odpowiedzieć, a Ty sprawdzisz moje odpowiedzi."*

### **5.2 Opcjonalne rozszerzenie**

**1. Pytanie o zastosowania:** Gdzie w realnym świecie (np. w grafice komputerowej, analizie danych) mogą być wykorzystywane operacje na macierzach, których się dziś nauczyłeś?

**2. Pytanie o wykorzystanie technologii:** Czy potrafisz zaimplementować wspominane obiekty i operacje w języku programowania (np. Python, MATLAB)? Jakie biblioteki mogłyby Ci w tym pomóc?

**3. Pytanie o naukowy sposób zapisu:** Jak zapisałbyś swoje notatki z tego materiału do profesjonalnego formatu (np. przy użyciu LaTeX, Markdown, Jupyter/Colab, GitHub, singlefile)?
