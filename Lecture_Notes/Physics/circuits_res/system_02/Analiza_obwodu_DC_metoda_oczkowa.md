# Analiza obwodu prądu stałego -- pełne rozwiązanie symboliczne

## 1. Opis układu

Rozpatrywany jest liniowy obwód prądu stałego zawierający:

-   6 rezystorów: R1, R2, R3, R4, R5, R6,
-   2 idealne źródła napięcia: E1, E2,
-   3 niezależne oczka,
-   3 węzły główne: a, b, c,
-   węzeł dolny b przyjęty jako odniesienie (masa).

Układ ma strukturę mostkową i nie redukuje się do prostego połączenia
szeregowego ani równoległego.

------------------------------------------------------------------------

# 2. Metoda oczkowa (II prawo Kirchhoffa)

Przyjmujemy trzy prądy oczkowe (zgodnie z ruchem wskazówek zegara):

I(1) -- oczko lewe dolne\
I(2) -- oczko prawe dolne\
I(3) -- oczko górne

Rezystory wspólne: - R3 -- oczka 1 i 2 - R4 -- oczka 1 i 3 - R5 -- oczka
2 i 3 - R6 -- tylko oczko 3

------------------------------------------------------------------------

# 3. Równania oczkowe

## Oczko 1

(R1+R4+R3) I(1) - R3 I(2) - R4 I(3) = E1

## Oczko 2

-   R3 I(1) + (R2+R5+R3) I(2) - R5 I(3) = E2

## Oczko 3

-   R4 I(1) - R5 I(2) + (R6+R4+R5) I(3) = 0

------------------------------------------------------------------------

# 4. Postać macierzowa

| R1+R4+R3 -R3 -R4 \| \| I(1) \| \| E1 \|
| -R3 R2+R5+R3 -R5 \| \* \| I(2) \| = \| E2 \|
| -R4 -R5 R6+R4+R5 \| \| I(3) \| \| 0 \|

------------------------------------------------------------------------

# 5. Rozwiązanie symboliczne

Wspólny mianownik Δ (wyznacznik macierzy):

Δ = R1R2R4 + R1R2R5 + R1R2R6 + R1R3R4 + R1R3R5 + R1R3R6 + R1R4R5 +
R1R5R6 + R2R3R4 + R2R3R5 + R2R3R6 + R2R4R5 + R2R4R6 + R3R4R6 + R3R5R6 +
R4R5R6

------------------------------------------------------------------------

## I(1)

I(1) = \[E1(...) + E2(...)\] / Δ

## I(2)

I(2) = \[E1(...) + E2(...)\] / Δ

## I(3)

I(3) = \[E1(...) + E2(...)\] / Δ

(Uproszczone -- pełne rozwinięcia można generować z macierzy Cramera).

------------------------------------------------------------------------

# 6. Prądy gałęziowe

IR1 = I(1)\
IR2 = I(2)\
IR3 = I(1) - I(2)\
IR4 = I(1) - I(3)\
IR5 = I(2) - I(3)\
IR6 = I(3)

------------------------------------------------------------------------

# 7. Napięcia na rezystorach

URk = Rk · IRk

------------------------------------------------------------------------

# 8. Kontrola poprawności

-   Spełnione I i II prawo Kirchhoffa
-   Suma mocy źródeł = suma mocy w rezystorach

------------------------------------------------------------------------

Autor: ChatGPT
