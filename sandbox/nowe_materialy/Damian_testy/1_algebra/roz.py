#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from numpy.linalg import det, solve as np_solve, matrix_power, LinAlgError
from sympy import symbols, Eq, solve as sympy_solve
import sys

# Ustawienia drukowania dla numpy, aby wyniki były czytelniejsze
np.set_printoptions(precision=5, suppress=True)

def solve_zadanie_1():
    """
    Oblicz wartość wyrażenia:
    det([[2, 1], [3, 4]]) - det([[1, 0, 2], [0, 3, 1], [0, 0, 2]])
    """
    print("## Zadanie 1")
    A = np.array([[2, 1], [3, 4]])
    B = np.array([[1, 0, 2], [0, 3, 1], [0, 0, 2]])
    
    det_A = det(A)  # det(A) = 2*4 - 1*3 = 8 - 3 = 5
    det_B = det(B)  # det(B) = 1*3*2 = 6 (macierz trójkątna górna)
    
    result = det_A - det_B
    
    print(f"det(A) = {det_A}")
    print(f"det(B) = {det_B}")
    print(f"Wynik: {det_A} - {det_B} = {result}")
    print("Poprawna odpowiedź: B) -1")
    print("-" * 30)


def solve_zadanie_2():
    """
    Rozwiąż równanie: det([[x, x], [3, x]]) = 0
    """
    print("## Zadanie 2")
    x = symbols('x')
    
    # Wyznacznik: x*x - x*3
    determinant_expr = x*x - 3*x
    
    # Równanie: x^2 - 3x = 0  => x(x - 3) = 0
    equation = Eq(determinant_expr, 0)
    
    solutions = sympy_solve(equation, x)
    
    print(f"Równanie: det([[x, x], [3, x]]) = 0")
    print(f"Postać algebraiczna: {determinant_expr} = 0")
    print(f"Rozwiązania: {solutions}")
    print("Poprawna odpowiedź: A) x = 0; x = 3")
    print("-" * 30)


def solve_zadanie_3():
    """
    Oblicz wartość wyrażenia M^100 dla M = macierz obrotu i theta = pi/4.
    """
    print("## Zadanie 3")
    theta = np.pi / 4
    n = 100
    
    # Macierz M to macierz obrotu R(theta)
    # Posiada własność: R(theta)^n = R(n*theta)
    
    final_theta = n * theta  # 100 * (pi / 4) = 25*pi
    
    # R(25*pi) = R(24*pi + pi) = R(pi) (ponieważ 24*pi to 12 pełnych obrotów)
    # R(pi) = [[cos(pi), -sin(pi)], [sin(pi), cos(pi)]] = [[-1, 0], [0, -1]]
    
    # Obliczenie analityczne:
    cos_final = np.cos(final_theta) # cos(25*pi) = -1
    sin_final = np.sin(final_theta) # sin(25*pi) = 0
    
    result_matrix = np.array([
        [cos_final, -sin_final],
        [sin_final, cos_final]
    ])
    
    # Można też obliczyć wprost przez potęgowanie macierzy:
    # M = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    # M_100 = matrix_power(M, n)
    # print(f"Wynik z matrix_power:\n{M_100}") # Da ten sam wynik
    
    print(f"Obliczamy M^100 dla theta = pi/4.")
    print(f"Korzystamy z własności R(theta)^n = R(n*theta)")
    print(f"n*theta = 100 * (pi/4) = 25*pi")
    print(f"R(25*pi) jest równoważne R(pi), ponieważ 25pi = 12*(2pi) + pi.")
    print(f"R(pi) = [[cos(pi), -sin(pi)], [sin(pi), cos(pi)]]")
    print(f"Wynik (zaokrąglony):\n{np.round(result_matrix).astype(int)}")
    print("Poprawna odpowiedź: C) [[-1, 0], [0, -1]]")
    print("-" * 30)


def solve_zadanie_4():
    """
    det(A) = 5 (A jest 2x2). Oblicz det(3A).
    """
    print("## Zadanie 4")
    det_A = 5
    n = 2  # Wymiar macierzy (2x2)
    k = 3  # Skalar
    
    # Własność: det(k*A) = k^n * det(A)
    det_kA = (k**n) * det_A
    
    print(f"Dane: det(A) = {det_A}, wymiar n = {n}, skalar k = {k}")
    print(f"Korzystamy z własności: det(k*A) = k^n * det(A)")
    print(f"Obliczenia: det(3*A) = 3^{n} * {det_A} = {k**n} * {det_A} = {det_kA}")
    print("Poprawna odpowiedź: C) 45")
    print("-" * 30)


def solve_zadanie_5():
    """
    Wektor v = [sqrt(2), -sqrt(2)] jest przekształcany przez macierz obrotu o kąt pi/2.
    """
    print("## Zadanie 5")
    v = np.array([np.sqrt(2), -np.sqrt(2)])
    theta = np.pi / 2
    
    # Macierz obrotu o pi/2
    R = np.array([
        [np.cos(theta), -np.sin(theta)],  # [[0, -1],
        [np.sin(theta), np.cos(theta)]   #  [1,  0]]
    ])
    
    # Mnożenie macierz * wektor (numpy domyślnie traktuje 'v' jako wektor kolumnowy w tej operacji)
    v_prime = R @ v
    
    # v_prime[0] = 0*sqrt(2) + (-1)*(-sqrt(2)) = sqrt(2)
    # v_prime[1] = 1*sqrt(2) + 0*(-sqrt(2))   = sqrt(2)
    
    print(f"Wektor v = {v}")
    print(f"Macierz obrotu R(pi/2):\n{np.round(R).astype(int)}")
    print(f"Nowy wektor v' = R * v = {v_prime}")
    print("Poprawna odpowiedź: D) [sqrt(2), sqrt(2)]")
    print("-" * 30)


def solve_zadanie_6():
    """
    det(A) = 7, det(B) = 3 (obie 2x2). Jaki jest det(AB)?
    """
    print("## Zadanie 6")
    det_A = 7
    det_B = 3
    
    # Twierdzenie Cauchy'ego: det(A*B) = det(A) * det(B)
    det_AB = det_A * det_B
    
    print(f"Dane: det(A) = {det_A}, det(B) = {det_B}")
    print(f"Korzystamy z twierdzenia Cauchy'ego: det(A*B) = det(A) * det(B)")
    print(f"Obliczenia: det(A*B) = {det_A} * {det_B} = {det_AB}")
    print("Poprawna odpowiedź: B) 7 * 3")
    print("-" * 30)


def solve_zadanie_7():
    """
    Rozwiąż układ równań: [[1, 2], [3, 4]] * [x, y] = [5, 11]
    """
    print("## Zadanie 7")
    A = np.array([[1, 2], [3, 4]])
    b = np.array([5, 11])
    
    try:
        solution = np_solve(A, b)
        print(f"Rozwiązujemy układ A*x = b, gdzie:")
        print(f"A =\n{A}")
        print(f"b = {b}")
        print(f"Rozwiązanie [x, y] = {solution}")
        
        # Sprawdzenie:
        # 1*(1) + 2*(2) = 1 + 4 = 5 (Zgadza się)
        # 3*(1) + 4*(2) = 3 + 8 = 11 (Zgadza się)
        
        print("Poprawna odpowiedź: A) [1, 2]^T")
        
    except LinAlgError as e:
        print(f"Nie udało się rozwiązać układu: {e}")
        
    print("-" * 30)


def solve_zadanie_8():
    """
    Dla jakiego alpha układ ma rozwiązanie:
    -4x1 + 3x2 = 2
     5x1 - 4x2 = 0
     2x1 -  x2 = alpha
    """
    print("## Zadanie 8")
    # Układ jest nadokreślony. Rozwiązujemy pierwsze dwa równania
    # i sprawdzamy, jakie alpha musi być, aby spełnić trzecie.
    
    A_sub = np.array([[-4, 3], [5, -4]])
    b_sub = np.array([2, 0])
    
    try:
        # Rozwiązujemy układ 2x2
        solution = np_solve(A_sub, b_sub)
        x1 = solution[0]
        x2 = solution[1]
        
        print(f"Rozwiązanie pierwszych dwóch równań: x1 = {x1}, x2 = {x2}")
        
        # Oczekiwane rozwiązanie: x1 = -8, x2 = -10
        # Sprawdzenie:
        # -4(-8) + 3(-10) = 32 - 30 = 2 (OK)
        #  5(-8) - 4(-10) = -40 + 40 = 0 (OK)
        
        # Wstawiamy x1 i x2 do trzeciego równania, aby znaleźć alpha
        # 2*x1 - x2 = alpha
        alpha = 2 * x1 - x2
        
        print(f"Wstawiamy do trzeciego równania: alpha = 2*({x1}) - ({x2})")
        print(f"alpha = {alpha}")
        # alpha = 2*(-8) - (-10) = -16 + 10 = -6
        
        print("Poprawna odpowiedź: B) alpha = -6")
        
    except LinAlgError as e:
        print(f"Nie udało się rozwiązać układu 2x2: {e}")
        
    print("-" * 30)


def solve_zadanie_9():
    """
    Rozwiąż układ:
    4x1 + 5x3 = 6
    x2 - 6x3 = -2
    3x1 + 4x3 = 3
    """
    print("## Zadanie 9")
    A = np.array([
        [4, 0, 5],
        [0, 1, -6],
        [3, 0, 4]
    ])
    b = np.array([6, -2, 3])
    
    try:
        # det(A) = 4(1*4 - (-6)*0) - 0(...) + 5(0*0 - 1*3) = 4(4) - 15 = 16 - 15 = 1
        # Skoro det(A) != 0, istnieje unikalne rozwiązanie.
        
        solution = np_solve(A, b)
        print(f"Rozwiązujemy układ A*x = b...")
        print(f"Rozwiązanie [x1, x2, x3] = {solution}")
        
        # Sprawdzenie z opcją A: {x1 = 9, x2 = -38, x3 = -6}
        # (1): 4(9) + 5(-6) = 36 - 30 = 6 (OK)
        # (2): (-38) - 6(-6) = -38 + 36 = -2 (OK)
        # (3): 3(9) + 4(-6) = 27 - 24 = 3 (OK)
        
        print("Poprawna odpowiedź: A) {x1 = 9, x2 = -38, x3 = -6}")
        
    except LinAlgError as e:
        print(f"Nie udało się rozwiązać układu: {e}")
        
    print("-" * 30)


def solve_zadanie_10():
    """
    Rozwiąż układ:
    3x1 - x2 - 2x3 = 2
    2x2 - x3 = -1
    3x1 - 5x2 = 3
    """
    print("## Zadanie 10")
    A = np.array([
        [3, -1, -2],
        [0, 2, -1],
        [3, -5, 0]
    ])
    b = np.array([2, -1, 3])
    
    # Sprawdźmy wyznacznik macierzy A
    det_A = det(A)
    # det(A) = 3(2*0 - (-1)*(-5)) - (-1)(0*0 - (-1)*3) + (-2)(0*(-5) - 2*3)
    # det(A) = 3(0 - 5) + 1(0 + 3) - 2(0 - 6)
    # det(A) = 3(-5) + 1(3) - 2(-6) = -15 + 3 + 12 = 0
    
    print(f"Sprawdzanie wyznacznika macierzy A: det(A) = {det_A}")
    
    # Skoro det(A) = 0, układ jest nieoznaczony (nieskończenie wiele rozwiązań)
    # lub sprzeczny (brak rozwiązań).
    # Funkcja np_solve() zgłosi błąd "Singular matrix".
    
    try:
        solution = np_solve(A, b)
        # Ten kod nie powinien się wykonać
        print(f"Znaleziono rozwiązanie (niespodziewane): {solution}")
    except LinAlgError as e:
        print(f"Wystąpił błąd (zgodnie z oczekiwaniami): {e}")
        
        # Sprawdźmy ręcznie (metoda podstawiania):
        # (2): x3 = 2*x2 + 1
        # (3): 3*x1 = 3 + 5*x2  => x1 = 1 + (5/3)*x2
        # Wstawiamy do (1):
        # 3*(1 + 5/3*x2) - x2 - 2*(2*x2 + 1) = 2
        # 3 + 5*x2 - x2 - 4*x2 - 2 = 2
        # (5 - 1 - 4)*x2 + (3 - 2) = 2
        # 0*x2 + 1 = 2
        # 1 = 2
        # Otrzymaliśmy sprzeczność.
        
        print("Ręczna analiza (metoda podstawiania) prowadzi do sprzeczności (1 = 2).")
        print("Poprawna odpowiedź: D) Układ jest sprzeczny.")
        
    print("-" * 30)


# Główna funkcja uruchamiająca wszystkie rozwiązania
def main():
    solve_zadanie_1()
    solve_zadanie_2()
    solve_zadanie_3()
    solve_zadanie_4()
    solve_zadanie_5()
    solve_zadanie_6()
    solve_zadanie_7()
    solve_zadanie_8()
    solve_zadanie_9()
    solve_zadanie_10()

if __name__ == "__main__":
    main()