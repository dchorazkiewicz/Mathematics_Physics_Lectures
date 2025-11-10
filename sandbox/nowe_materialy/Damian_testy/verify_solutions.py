#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Skrypt Pythona rozwiązujący zadania z Algebry Liniowej.

Ten skrypt wykorzystuje bibliotekę SymPy do obliczeń symbolicznych i numerycznych
oraz zapisuje wszystkie wyniki i kroki do pliku 'algebra_solutions.log'.
"""

import logging
from pathlib import Path
import sympy as sp

# Konfiguracja logowania
# Zapisujemy log w katalogu tego skryptu (sandbox/nowe_materialy/Damian_testy/)
# Tworzymy katalog, jeśli nie istnieje, i ustawiamy pełną ścieżkę do pliku logu.
log_dir = Path(__file__).resolve().parent
log_dir.mkdir(parents=True, exist_ok=True)
log_file = log_dir / 'algebra_solutions.log'

# 'w' oznacza, że plik logu będzie nadpisywany przy każdym uruchomieniu
logging.basicConfig(
    filename=str(log_file),
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8'
)
logger = logging.getLogger()

# --- Funkcje pomocnicze do logowania ---

def log_task(section, task_num, description=""):
    """Loguje nagłówek nowego zadania."""
    header = f" Dział {section} — Zadanie {task_num} "
    separator = "=" * (80 - len(header))
    logger.info(f"\n{separator}{header}")
    if description:
        logger.info(description)

def log_result(label, value):
    """Loguje etykietę i wynik obliczenia."""
    # Używamy str() i pretty-printing SymPy do czytelnego formatowania
    logger.info(f"{label}:\n{sp.pretty(value, use_unicode=True)}")

def log_info(message):
    """Loguje informację tekstową lub komentarz."""
    logger.info(message)

def log_check(label, value1, value2, result):
    """Loguje sprawdzenie równości."""
    logger.info(f"Sprawdzenie: {label}")
    logger.info(f"  LHS:\n{sp.pretty(value1, use_unicode=True)}")
    logger.info(f"  RHS:\n{sp.pretty(value2, use_unicode=True)}")
    logger.info(f"  Wynik: {result}")

# --- Główna funkcja rozwiązująca ---

def solve_linear_algebra():
    """Główna funkcja wykonująca wszystkie zadania."""
    
    logger.info("Rozpoczęcie rozwiązywania zadań z Algebry Liniowej.")

    # ##################################################################
    # Dział 1 — Macierze i podstawowe operacje
    # ##################################################################

    log_task(1, 1, "Podstawowe operacje na macierzach A i B")
    try:
        A = sp.Matrix([[1, 2], [3, 4]])
        B = sp.Matrix([[0, -1], [2, 1]])
        log_result("A", A)
        log_result("B", B)
        
        log_result("A + B", A + B)
        log_result("A - B", A - B)
        log_result("2A", 2 * A)
        log_result("3B - 2A", 3 * B - 2 * A)
        
        AB = A * B
        BA = B * A
        log_result("A * B", AB)
        log_result("B * A", BA)
        log_check("A * B = B * A", AB, BA, AB == BA)
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 1.1: {e}")

    log_task(1, 2, "Sprawdzenie przemienności iloczynu macierzy diagonalnych")
    try:
        A = sp.diag(1, 2)
        B = sp.diag(2, 4)
        C = sp.diag(4, 8)
        D = sp.diag(8, 16)
        
        R1 = A * B * C * D
        R2 = B * A * D * C
        R3 = D * C * B * A
        
        log_result("A*B*C*D", R1)
        log_result("B*A*D*C", R2)
        log_result("D*C*B*A", R3)
        log_check("A*B*C*D = B*A*D*C = D*C*B*A", R1, R2, R1 == R2 and R2 == R3)
        log_info("Wniosek: Macierze diagonalne są przemienne.")
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 1.2: {e}")

    log_task(1, 3, "Operacje na wierszach macierzy C")
    try:
        C = sp.Matrix([[1, 0, 2], [-1, 3, 1], [0, 2, -1]])
        log_result("Macierz początkowa C", C)
        
        C_step1 = C.copy()
        C_step1.row_swap(0, 2)
        log_result("Krok 1: Zamiana wierszy 1. i 3.", C_step1)
        
        C_step2 = C_step1.copy()
        C_step2[1, :] = C_step2[1, :] + 2 * C_step2[0, :]
        log_result("Krok 2: Dodanie 2 * (nowy wiersz 1) do wiersza 2.", C_step2)
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 1.3: {e}")

    log_task(1, 4, "Operacje na wektorach kolumnowych u i v")
    try:
        u = sp.Matrix([1, -2, 3])
        v = sp.Matrix([2, 0, -1])
        log_result("u", u)
        log_result("v", v)
        
        log_result("u + v", u + v)
        log_result("u - v", u - v)
        
        uvT = u * v.T
        vuT = v * u.T
        log_result("u * v^T (iloczyn zewnętrzny)", uvT)
        log_result("v * u^T (iloczyn zewnętrzny)", vuT)
        
        rank_uvT = uvT.rank()
        log_result(f"Rząd macierzy u*v^T", rank_uvT)
        log_info("Rząd macierzy będącej iloczynem zewnętrznym dwóch niezerowych wektorów jest zawsze równy 1.")
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 1.4: {e}")

    log_task(1, 5, "Macierz diagonalna D")
    try:
        a, b, c = sp.symbols('a b c')
        D = sp.diag(2, -3, 5)
        E = sp.diag(a, b, c)
        
        log_result("D", D)
        log_result("E", E)
        
        DE = D * E
        ED = E * D
        log_check("D * E = E * D", DE, ED, DE == ED)
        log_info("Macierze diagonalne są przemienne.")
        
        log_result("D^3", D**3)
        log_result("D^-1 (macierz odwrotna)", D.inv())
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 1.5: {e}")

    log_task(1, 6, "Potęgi macierzy P")
    try:
        P = sp.Matrix([[1, 1, 0], [0, 1, 1], [1, 0, 1]])
        P2 = P**2
        P3 = P**3
        
        log_result("P", P)
        log_result("P^2", P2)
        log_result("P^3", P3)
        log_info("Obserwacja wzorca: Wartości w macierzy rosną.")
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 1.6: {e}")

    log_task(1, 7, "Iloczyn macierzy rotacji R(theta)")
    try:
        t1, t2 = sp.symbols('theta_1 theta_2')
        
        def R(theta):
            return sp.Matrix([
                [sp.cos(theta), -sp.sin(theta)],
                [sp.sin(theta),  sp.cos(theta)]
            ])
            
        LHS = R(t1) * R(t2)
        RHS = R(t1 + t2)
        
        log_result("R(t1) * R(t2)", LHS)
        log_result("R(t1 + t2)", RHS)
        
        # Używamy simplify do trygonometrii
        LHS_simple = sp.simplify(LHS)
        RHS_simple = sp.simplify(RHS)
        
        log_result("R(t1) * R(t2) [po uproszczeniu]", LHS_simple)
        log_result("R(t1 + t2) [po uproszczeniu]", RHS_simple)
        log_check("R(t1)R(t2) = R(t1 + t2)", LHS_simple, RHS_simple, LHS_simple == RHS_simple)
        log_info("Tożsamość została potwierdzona.")
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 1.7: {e}")

    log_task(1, 8, "Macierz rotacji jako szereg potęgowy (eksponenta macierzy)")
    try:
        log_info("UWAGA: Szeregi dla sin(x) i cos(x) w treści zadania są zamienione i niepoprawne.")
        log_info("Poprawny szereg cos(x) = 1 - x^2/2! + x^4/4! - ...")
        log_info("Poprawny szereg sin(x) = x - x^3/3! + x^5/5! - ...")
        log_info("Pokażemy, że R(theta) = exp(A) = I + A + A^2/2! + ...")
        
        theta = sp.symbols('theta')
        A = sp.Matrix([[0, -theta], [theta, 0]])
        
        # SymPy potrafi obliczyć eksponentę macierzy symbolicznie
        exp_A = sp.exp(A)
        
        def R(theta):
            return sp.Matrix([
                [sp.cos(theta), -sp.sin(theta)],
                [sp.sin(theta),  sp.cos(theta)]
            ])
        
        R_theta = R(theta)
        
        log_result("A", A)
        log_result("exp(A) [obliczone przez SymPy]", exp_A)
        log_result("R(theta)", R_theta)
        log_check("exp(A) = R(theta)", exp_A, R_theta, exp_A == R_theta)
        log_info("Dowód: exp(A) = I*cos(theta) + J*sin(theta), gdzie J = A/theta, co jest równe R(theta).")
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 1.8: {e}")

    log_task(1, 9, "Macierze Pauliego")
    try:
        i = sp.I
        I_2 = sp.eye(2)
        
        sx = sp.Matrix([[0, 1], [1, 0]])
        sy = sp.Matrix([[0, -i], [i, 0]])
        sz = sp.Matrix([[1, 0], [0, -1]])
        
        log_result("sigma_x", sx)
        log_result("sigma_y", sy)
        log_result("sigma_z", sz)
        
        log_info("--- Sprawdzenie kwadratów ---")
        log_check("sigma_x^2 = I", sx**2, I_2, sx**2 == I_2)
        log_check("sigma_y^2 = I", sy**2, I_2, sy**2 == I_2)
        log_check("sigma_z^2 = I", sz**2, I_2, sz**2 == I_2)

        log_info("--- Sprawdzenie iloczynów (relacje komutacji) ---")
        log_check("sigma_x * sigma_y = i * sigma_z", sx * sy, i * sz, sx * sy == i * sz)
        log_check("sigma_y * sigma_z = i * sigma_x", sy * sz, i * sx, sy * sz == i * sx)
        log_check("sigma_z * sigma_x = i * sigma_y", sz * sx, i * sy, sz * sx == i * sy)

        log_info("--- Sprawdzenie antykomutatorów {sigma_i, sigma_j} = sigma_i*sigma_j + sigma_j*sigma_i = 2*delta_ij*I ---")
        # i = j
        log_check("{sigma_x, sigma_x} = 2I", sx*sx + sx*sx, 2*I_2, sx*sx + sx*sx == 2*I_2)
        log_check("{sigma_y, sigma_y} = 2I", sy*sy + sy*sy, 2*I_2, sy*sy + sy*sy == 2*I_2)
        log_check("{sigma_z, sigma_z} = 2I", sz*sz + sz*sz, 2*I_2, sz*sz + sz*sz == 2*I_2)
        # i != j (powinny dać macierz zerową)
        log_check("{sigma_x, sigma_y} = 0", sx*sy + sy*sx, sp.zeros(2), sx*sy + sy*sx == sp.zeros(2))
        log_check("{sigma_y, sigma_z} = 0", sy*sz + sz*sy, sp.zeros(2), sy*sz + sz*sy == sp.zeros(2))
        log_check("{sigma_z, sigma_x} = 0", sz*sx + sx*sz, sp.zeros(2), sz*sx + sx*sz == sp.zeros(2))
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 1.9: {e}")

    # ##################################################################
    # Dział 2 — Wyznaczniki
    # ##################################################################

    log_task(2, 1, "Obliczanie wyznaczników (metoda Sarrusa)")
    try:
        A = sp.Matrix([[2, 3, 1], [0, -1, 4], [5, 2, 0]])
        B = sp.Matrix([[1, 2, 2], [4, 0, 0], [7, 8, 9]])
        C = sp.Matrix([[3, 0, 2], [2, 0, -2], [0, 1, 1]])
        
        log_result(f"det(A) dla A = \n{sp.pretty(A, use_unicode=True)}", A.det())
        log_result(f"det(B) dla B = \n{sp.pretty(B, use_unicode=True)}", B.det())
        log_result(f"det(C) dla C = \n{sp.pretty(C, use_unicode=True)}", C.det())
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 2.1: {e}")

    log_task(2, 2, "Obliczanie wyznaczników (rozwinięcie Laplace'a)")
    try:
        A = sp.Matrix([[1]])
        B = sp.Matrix([[1, 0, 2], [3, 1, 0], [4, 5, 6]])
        C = sp.Matrix([[1, 2, 3, 4], [0, 1, 0, 0], [0, 0, 1, 1], [0, 0, 0, 2]])
        
        # SymPy może użyć konkretnej metody
        log_result(f"det(A) dla A = \n{sp.pretty(A, use_unicode=True)}", A.det(method='laplace'))
        log_result(f"det(B) dla B = \n{sp.pretty(B, use_unicode=True)}", B.det(method='laplace'))
        log_result(f"det(C) dla C = \n{sp.pretty(C, use_unicode=True)}", C.det(method='laplace'))
        log_info(f"Dla C (macierz trójkątna), wyznacznik to iloczyn diagonali: 1*1*1*2 = 2.")
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 2.2: {e}")

    log_task(2, 3, "Wyznacznik macierzy z dwoma równymi wierszami")
    try:
        log_info("Uzasadnienie: Jeśli macierz ma dwa równe wiersze, operacja elementarna polegająca na odjęciu jednego z tych wierszy od drugiego (która nie zmienia wartości wyznacznika) prowadzi do powstania wiersza zerowego. Wyznacznik macierzy zawierającej wiersz zerowy jest zawsze równy 0.")
        M = sp.Matrix([[5, 8, -1], [1, 2, 3], [1, 2, 3]])
        log_result(f"Przykładowa macierz M = \n{sp.pretty(M, use_unicode=True)}", M)
        log_result("det(M)", M.det())
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 2.3: {e}")

    log_task(2, 4, "Wyznacznik macierzy trójkątnej T")
    try:
        log_info("Wyznacznik macierzy trójkątnej (górnej lub dolnej) jest równy iloczynowi elementów na jej głównej przekątnej.")
        det_T = 3 * (-2) * 5 * 1
        log_result("Wyznacznik T", det_T)
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 2.4: {e}")

    log_task(2, 5, "Wyznacznik macierzy M(t) z parametrem")
    try:
        t = sp.symbols('t')
        M_t = sp.Matrix([[t, 1], [2, t]])
        log_result("M(t)", M_t)
        
        det_M_t = M_t.det()
        log_result("det(M(t))", det_M_t)
        
        singular_t = sp.solve(det_M_t, t)
        log_result(f"Macierz jest singularna (det=0) dla t =", singular_t)
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 2.5: {e}")

    log_task(2, 6, "Rozwiązanie równania det = 0")
    try:
        x = sp.symbols('x')
        M = sp.Matrix([[x, 3], [2, x]])
        det_M = M.det()
        equation = sp.Eq(det_M, 0)
        log_result("Równanie", equation)
        
        solutions = sp.solve(equation, x)
        log_result("Rozwiązania", solutions)
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 2.6: {e}")

    log_task(2, 7, "Rozwiązanie równania det = 0 (wariant)")
    try:
        x = sp.symbols('x')
        M = sp.Matrix([[x, 3], [2, -x]])
        det_M = M.det()
        equation = sp.Eq(det_M, 0)
        log_result("Równanie", equation)
        
        solutions = sp.solve(equation, x)
        log_result("Rozwiązania", solutions)
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 2.7: {e}")

    log_task(2, 8, "Obliczenie wyznacznika symbolicznego 3x3")
    try:
        x, y = sp.symbols('x y')
        M = sp.Matrix([
            [x, y, x + y],
            [y, x + y, x],
            [x + y, x, y]
        ])
        log_result("Macierz M", M)
        det_M = M.det()
        log_result("det(M)", det_M)
        log_result("det(M) [uproszczone]", sp.simplify(det_M))
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 2.8: {e}")

    log_task(2, 9, "Wyznacznik Vandermonde'a")
    try:
        x, y, z, u = sp.symbols('x y z u')
        
        log_info("--- Część 1: 3x3 ---")
        M3 = sp.Matrix([
            [1, 1, 1],
            [x, y, z],
            [x**2, y**2, z**2]
        ])
        LHS = M3.det()
        RHS = (z - x) * (z - y) * (y - x)
        
        # factor() jest lepsze niż simplify() do pokazania postaci iloczynowej
        log_result("LHS (obliczony wyznacznik)", sp.factor(LHS))
        log_result("RHS (oczekiwany wynik)", RHS)
        log_check("LHS = RHS", sp.simplify(LHS - RHS), 0, sp.simplify(LHS - RHS) == 0)

        log_info("\n--- Część 2: 4x4 ---")
        M4 = sp.Matrix([
            [1, 1, 1, 1],
            [x, y, z, u],
            [x**2, y**2, z**2, u**2],
            [x**3, y**3, z**3, u**3]
        ])
        det_M4 = M4.det()
        log_result(f"Wyznacznik 4x4 (postać iloczynowa)", sp.factor(det_M4))
        log_info("Ogólny wzór: (u-x)(u-y)(u-z)(z-x)(z-y)(y-x)")
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 2.9: {e}")

    log_task(2, 10, "Obliczenie dwóch wyznaczników")
    try:
        a, b, c, d = sp.symbols('a b c d')
        
        M1 = sp.Matrix([
            [a, a, a],
            [-a, a, a],
            [-a, -a, a]
        ])
        log_result(f"Wyznacznik M1 = \n{sp.pretty(M1, use_unicode=True)}", M1.det())
        
        M2 = sp.Matrix([
            [a, 0, b],
            [0, c, 0],
            [d, 0, a]
        ])
        log_result(f"Wyznacznik M2 = \n{sp.pretty(M2, use_unicode=True)}", M2.det())
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 2.10: {e}")

    log_task(2, 11, "Sprawdzenie związków na wyznacznikach")
    try:
        a, b, c, d, x = sp.symbols('a b c d x')
        RHS = sp.Matrix([[a, b], [c, d]]).det()
        log_result("Wyznacznik bazowy |a b; c d|", RHS)
        
        log_info("\n--- Podpunkt a) ---")
        LHS_a = sp.Matrix([[a + b, b], [c + d, d]]).det()
        log_result("Wyznacznik |a+b b; c+d d|", LHS_a)
        log_check("a) LHS = RHS", LHS_a, RHS, LHS_a == RHS)
        
        log_info("\n--- Podpunkt b) ---")
        LHS_b = sp.Matrix([[a + b*x, b], [c + d*x, d]]).det()
        log_result("Wyznacznik |a+bx b; c+dx d|", LHS_b)
        log_check("b) LHS = RHS", LHS_b, RHS, LHS_b == RHS)
        log_info("Wniosek: Dodanie do kolumny wielokrotności innej kolumny nie zmienia wyznacznika.")
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 2.11: {e}")

    # ##################################################################
    # Dział 3 — Odwracanie macierzy
    # ##################################################################

    log_task(3, 1, "Odwrotność macierzy 2x2")
    try:
        A = sp.Matrix([[2, 1], [5, 3]])
        B = sp.Matrix([[0, 1], [1, 0]])
        C = sp.Matrix([[4, 7], [2, 6]])
        
        log_result(f"A^-1 dla A = \n{sp.pretty(A, use_unicode=True)}", A.inv())
        log_result(f"B^-1 dla B = \n{sp.pretty(B, use_unicode=True)}", B.inv())
        log_result(f"C^-1 dla C = \n{sp.pretty(C, use_unicode=True)}", C.inv())
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 3.1: {e}")

    log_task(3, 2, "Obliczanie macierzy odwrotnych dwiema metodami")
    try:
        matrices = {
            'A': sp.Matrix([[1, 2], [2, 5]]),
            'B': sp.Matrix([[12, 5], [7, 3]]),
            'C': sp.Matrix([[1, 2, 3], [0, 1, 4], [5, 6, 0]]),
            'D': sp.Matrix([[2, 0, 1], [1, 3, 0], [0, 4, 5]])
        }
        
        for name, M in matrices.items():
            logger.info(f"\n--- Obliczenia dla macierzy {name} ---")
            log_result(f"Macierz {name}", M)
            if M.det() == 0:
                log_info(f"Macierz {name} jest nieodwracalna (det=0).")
                continue
                
            # Metoda Gaussa-Jordana
            inv_GJ = M.inv(method='GJ')
            log_result(f"{name}^-1 (Metoda Gaussa-Jordana)", inv_GJ)
            
            # Metoda dopełnień algebraicznych (adjugate)
            inv_ADJ = M.inv(method='ADJ')
            log_result(f"{name}^-1 (Metoda dopełnień / wzór z mac. doł.)", inv_ADJ)
            
            log_check(f"{name}: Metoda GJ = Metoda ADJ", inv_GJ, inv_ADJ, inv_GJ == inv_ADJ)
            
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 3.2: {e}")

    log_task(3, 3, "Sprawdzenie odwracalności macierzy H")
    try:
        H = sp.Matrix([[1, 2, 3], [2, 4, 6], [0, 1, 1]])
        log_result("Macierz H", H)
        
        det_H = H.det()
        log_result("det(H)", det_H)
        
        if det_H == 0:
            log_info("Odpowiedź: Macierz H jest nieodwracalna (singularna), ponieważ jej wyznacznik jest równy 0.")
            log_info("Uzasadnienie (bez liczenia): Tak, można to było zauważyć. Drugi wiersz [2, 4, 6] jest dwukrotnością pierwszego wiersza [1, 2, 3]. Oznacza to, że wiersze są liniowo zależne, co implikuje, że wyznacznik jest równy 0.")
            log_info("Aby macierz była odwracalna, wszystkie jej wiersze (i kolumny) muszą być liniowo niezależne, a jej wyznacznik musi być różny od zera.")
        else:
            log_info("Macierz H jest odwracalna.")
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 3.3: {e}")

    log_task(3, 4, "Macierz inwolutywna (A^2 = I)")
    try:
        log_info("Dowód: Mamy A^2 = I. Mnożąc obie strony równania lewostronnie przez A^-1 (zakładając, że istnieje), otrzymujemy:")
        log_info("A^-1 * (A^2) = A^-1 * I")
        log_info("(A^-1 * A) * A = A^-1")
        log_info("I * A = A^-1")
        log_info("A = A^-1. (c.n.d.)")
        
        log_info("\nNiebanalny przykład (inny niż I lub -I): macierz permutacji lub odbicia.")
        A_ex = sp.Matrix([[0, 1], [1, 0]])
        log_result("Przykład A", A_ex)
        log_result("A^2", A_ex**2)
        log_check("A^-1 = A", A_ex.inv(), A_ex, A_ex.inv() == A_ex)
        
        log_info("Ile jest takich macierzy? Nieskończenie wiele. Np. każda macierz postaci [[a, b], [c, -a]] gdzie a^2 + bc = 1.")
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 3.4: {e}")

    log_task(3, 5, "Odwrotność macierzy diagonalnej D")
    try:
        D = sp.diag(2, 5, -3, 1)
        log_result("Macierz D", D)
        
        log_info("Warunek istnienia odwrotności: Macierz diagonalna jest odwracalna wtedy i tylko wtedy, gdy wszystkie jej elementy na diagonali są niezerowe (ponieważ wyznacznik jest iloczynem tych elementów).")
        log_info("W tym przypadku det(D) = 2*5*(-3)*1 = -30 != 0, więc istnieje.")
        
        inv_D = D.inv()
        log_result("D^-1", inv_D)
        log_info("Odwrotnością macierzy diagonalnej jest macierz diagonalna zawierająca odwrotności elementów z diagonali macierzy wyjściowej.")
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 3.5: {e}")

    log_task(3, 6, "Rozwiązywanie równań macierzowych")
    try:
        log_info("\n--- Podpunkt a) AX = B ---> X = A^-1 * B ---")
        A_a = sp.Matrix([[2, 5], [1, 3]])
        B_a = sp.Matrix([[4, -6], [2, 1]])
        X_a = A_a.inv() * B_a
        log_result("X", X_a)
        
        log_info("\n--- Podpunkt b) AX = B ---> X = A^-1 * B ---")
        A_b = sp.Matrix([[2, 1], [5, 3]])
        B_b = sp.Matrix([[1, 2], [3, 4]])
        X_b = A_b.inv() * B_b
        log_result("X", X_b)
        
        log_info("\n--- Podpunkt c) XA = B ---> X = B * A^-1 ---")
        A_c = sp.Matrix([[1, 1, -1], [2, 1, 0], [1, -1, 1]])
        B_c = sp.Matrix([[1, -3, 3], [4, 3, 2], [1, -2, 5]])
        X_c = B_c * A_c.inv()
        log_result("X", X_c)
        
        log_info("\n--- Podpunkt d) AX = B ---> X = A^-1 * B ---")
        A_d = sp.Matrix([[3, 2, 3], [1, 1, 2], [3, 2, 4]])
        B_d = sp.Matrix([[1, 2, 3], [1, -1, 2], [2, 2, 4]])
        X_d = A_d.inv() * B_d
        log_result("X", X_d)
        
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 3.6: {e}")

    # ##################################################################
    # Dział 4 — Układy równań liniowych
    # ##################################################################

    log_task(4, 1, "Rozwiązanie układu 2x2 trzema metodami")
    try:
        A = sp.Matrix([[2, 3], [1, -4]])
        b = sp.Matrix([5, -2])
        log_result("Macierz A", A)
        log_result("Wektor b", b)
        
        log_info("\n--- Metoda 1: Wzory Cramera ---")
        det_A = A.det()
        Ax = A.copy()
        Ax[:, 0] = b
        Ay = A.copy()
        Ay[:, 1] = b
        
        x = Ax.det() / det_A
        y = Ay.det() / det_A
        log_result(f"det(A) = {det_A}, det(Ax) = {Ax.det()}, det(Ay) = {Ay.det()}", "")
        log_result("Rozwiązanie (Cramer)", sp.Matrix([x, y]))
        
        log_info("\n--- Metoda 2: Eliminacja Gaussa (SymPy LUsolve) ---")
        sol_gauss = A.LUsolve(b)
        log_result("Rozwiązanie (Gauss)", sol_gauss)
        
        log_info("\n--- Metoda 3: Macierz odwrotna (X = A^-1 * b) ---")
        sol_inv = A.inv() * b
        log_result("Rozwiązanie (Odwrotna)", sol_inv)
        
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 4.1: {e}")

    log_task(4, 2, "Rozwiązanie układu 3x3 trzema metodami")
    try:
        A = sp.Matrix([[1, 1, 1], [2, -1, 3], [-1, 2, -1]])
        b = sp.Matrix([6, 14, -2])
        log_result("Macierz A", A)
        log_result("Wektor b", b)
        
        log_info("\n--- Metoda 1: Wzory Cramera ---")
        det_A = A.det()
        Ax = A.copy(); Ax[:, 0] = b
        Ay = A.copy(); Ay[:, 1] = b
        Az = A.copy(); Az[:, 2] = b
        
        x = Ax.det() / det_A
        y = Ay.det() / det_A
        z = Az.det() / det_A
        log_result(f"det(A) = {det_A}, det(Ax) = {Ax.det()}, det(Ay) = {Ay.det()}, det(Az) = {Az.det()}", "")
        log_result("Rozwiązanie (Cramer)", sp.Matrix([x, y, z]))
        
        log_info("\n--- Metoda 2: Eliminacja Gaussa (SymPy LUsolve) ---")
        sol_gauss = A.LUsolve(b)
        log_result("Rozwiązanie (Gauss)", sol_gauss)
        
        log_info("\n--- Metoda 3: Macierz odwrotna (X = A^-1 * b) ---")
        sol_inv = A.inv() * b
        log_result("Rozwiązanie (Odwrotna)", sol_inv)
        
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 4.2: {e}")

    log_task(4, 3, "Układ parametryczny z lambda")
    try:
        lmbda = sp.symbols('lambda')
        A = sp.Matrix([[1, lmbda], [2, 1 + lmbda]])
        b = sp.Matrix([1, 3])
        
        det_A = A.det()
        log_result("det(A)", det_A)
        
        singular_lambda = sp.solve(det_A, lmbda)
        log_result(f"Wyznacznik jest równy 0 dla lambda =", singular_lambda)
        
        log_info(f"Przypadek 1: Jedno rozwiązanie (układ oznaczony)")
        log_info(f"Występuje, gdy det(A) != 0, czyli dla lambda != {singular_lambda[0]}")
        
        log_info(f"\nPrzypadek 2: Sprawdzenie dla lambda = {singular_lambda[0]}")
        A_sub = A.subs(lmbda, singular_lambda[0])
        Aug = A_sub.row_join(b) # Macierz rozszerzona
        log_result(f"Macierz rozszerzona [A|b] dla lambda = {singular_lambda[0]}", Aug)
        
        Aug_rref, pivots = Aug.rref()
        log_result("Postać zredukowana (RREF)", Aug_rref)
        
        log_info("Drugi wiersz [0, 0, 1] oznacza 0x + 0y = 1, co jest sprzecznością.")
        log_info(f"Wniosek dla lambda = {singular_lambda[0]}: Układ jest sprzeczny (brak rozwiązań).")
        
        log_info("\n--- Podsumowanie ---")
        log_info(f"1. Jedno rozwiązanie: dla lambda != {singular_lambda[0]}")
        log_info(f"2. Brak rozwiązań: dla lambda = {singular_lambda[0]}")
        log_info("3. Nieskończenie wiele rozwiązań: Nigdy.")
        
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 4.3: {e}")

    log_task(4, 4, "Rozwiązanie Ax=b i sprawdzenie")
    try:
        A = sp.Matrix([[1, 1, 1], [0, 2, -1], [2, -1, 3]])
        b = sp.Matrix([4, 1, 3])
        
        log_result("Macierz A", A)
        log_result("Wektor b", b)
        
        x_sol = A.LUsolve(b)
        log_result("Rozwiązanie x", x_sol)
        
        check = A * x_sol
        log_result("Sprawdzenie (A * x)", check)
        log_check("A * x = b", check, b, check == b)
        
    except Exception as e:
        logger.error(f"Błąd w Zadaniu 4.4: {e}")

    log_task(4, 5, "Zbiór układów równań")
    try:
        x1, x2, x3, a = sp.symbols('x1 x2 x3 a')
        vars_list = [x1, x2, x3]
        
        # Funkcja pomocnicza do rozwiązywania i logowania
        def solve_and_log(label, equations, variables):
            log_info(f"\n--- Podpunkt {label} ---")
            log_info("Układ równań:")
            for eq in equations:
                log_info(f"  {sp.Eq(eq, 0)}")
            try:
                solution = sp.solve(equations, variables)
                log_result("Rozwiązanie", solution if solution else "Brak rozwiązań (układ sprzeczny)")
            except Exception as e:
                logger.warning(f"Nie udało się rozwiązać układu: {e}")

        # a)
        eqs_a = [
            x1 + 4*x2 + 3*x3 - 1,
            2*x1 + 5*x2 + 4*x3 - 4,
            x1 - 3*x2 - 2*x3 - 5
        ]
        solve_and_log('a', eqs_a, vars_list)

        # b)
        eqs_b = [
            x1 - 2*x2 - 3*x3 - 2,
            x1 - 4*x2 - 13*x3 - 14,
            -3*x1 + 5*x2 + 4*x3
        ]
        solve_and_log('b', eqs_b, vars_list)

        # c)
        eqs_c = [
            x1 - 2*x2 - 3*x3 - 2,
            x1 - 4*x2 - 13*x3 - 14,
            -3*x1 + 5*x2 + 4*x3 - 2
        ]
        solve_and_log('c', eqs_c, vars_list)

        # d) Układ nieoznaczony (więcej zmiennych niż równań)
        eqs_d = [
            -4*x1 + 3*x2 + 2*x3 - (-2),
            5*x1 - 4*x2 + x3 - 3
        ]
        solve_and_log('d', eqs_d, vars_list)

        # e) Układ z parametrem 'a'
        log_info(f"\n--- Podpunkt e) ---")
        eqs_e = [
            -4*x1 + 3*x2 - 2,
            5*x1 - 4*x2,
            2*x1 - x2 - a
        ]
        log_info("Układ równań:")
        for eq in eqs_e: log_info(f"  {sp.Eq(eq, 0)}")
        # Rozwiązujemy pierwsze dwa równania dla x1, x2
        sol_e_part = sp.solve(eqs_e[:2], [x1, x2])
        if sol_e_part:
            log_result("Rozwiązanie (x1, x2) z pierwszych dwóch równań", sol_e_part)
            # Podstawiamy do trzeciego, aby znaleźć warunek na 'a'
            cond_a = eqs_e[2].subs(sol_e_part)
            val_a = sp.solve(cond_a, a)
            log_result(f"Układ ma rozwiązanie tylko dla 'a' równego", val_a[0])
            log_result("Pełne rozwiązanie (x1, x2) przy tym warunku na 'a'", sol_e_part)
        else:
            log_info("Układ sprzeczny (pierwsze dwa równania).")

        # f)
        eqs_f = [
            4*x1 + 5*x3 - 6,
            x2 - 6*x3 - (-2),
            3*x1 + 4*x3 - 3
        ]
        solve_and_log('f', eqs_f, vars_list)

        # g) Układ nieoznaczony (zależny)
        eqs_g = [
            3*x1 - x2 - 2*x3 - 2,
            2*x2 - x3 - (-1),
            3*x1 - 5*x2 - 3
        ]
        solve_and_log('g', eqs_g, vars_list)

        # h) Układ jednorodny
        eqs_h = [
            -x1 + 2*x2 + 3*x3,
            x1 - 4*x2 - 13*x3,
            -3*x1 + 5*x2 + 4*x3
        ]
        solve_and_log('h', eqs_h, vars_list)
        log_info("Uwaga: To układ jednorodny. SymPy zwraca jedno z rozwiązań bazowych przestrzeni zerowej, jeśli jest niezerowa.")
        # Sprawdzenie, czy jest tylko rozwiązanie trywialne
        A_h = sp.Matrix([[-1, 2, 3], [1, -4, -13], [-3, 5, 4]])
        if A_h.det() != 0:
            log_info("Wyznacznik != 0, jedyne rozwiązanie to (0, 0, 0).")
        else:
            log_info("Wyznacznik = 0, istnieje nieskończenie wiele rozwiązań (niezerowe).")


        # i) Układ jednorodny
        eqs_i = [
            x1 + x2 + x3,
            2*x1 + 4*x2 + 3*x3,
            4*x2 + 4*x3
        ]
        solve_and_log('i', eqs_i, vars_list)

        # j)
        eqs_j = [
            x1 + x2 + x3 - (-2),
            2*x1 + 4*x2 - 3*x3 - 3,
            4*x2 + 2*x3 - 2
        ]
        solve_and_log('j', eqs_j, vars_list)

        # k)
        eqs_k = [
            4*x1 + 4*x3 - 8,
            x2 - 6*x3 - (-3),
            3*x1 + x2 - 3*x3 - 3
        ]
        solve_and_log('k', eqs_k, vars_list)

        # l) Układ nadokreślony (3 równania, 2 niewiadome)
        eqs_l = [
            5*x1 - 3*x2 - (-7),
            -2*x1 + 9*x2 - 4,
            2*x1 + 4*x2 - (-2)
        ]
        solve_and_log('l', eqs_l, [x1, x2])

    except Exception as e:
        logger.error(f"Błąd w Zadaniu 4.5: {e}")

    logger.info("\nZakończono rozwiązywanie wszystkich zadań.")
    print("Wszystkie zadania zostały rozwiązane. Wyniki zapisano w pliku 'algebra_solutions.log'.")


# --- Uruchomienie skryptu ---
if __name__ == "__main__":
    try:
        # Inicjalizacja ładnego drukowania w SymPy (dla logów)
        sp.init_printing(use_unicode=True, wrap_line=False)
        solve_linear_algebra()
    except ImportError:
        print("BŁĄD: Biblioteka SymPy nie jest zainstalowana.")
        print("Proszę zainstalować ją używając: pip install sympy")
        logger.critical("BŁĄD: Biblioteka SymPy nie jest zainstalowana.")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")
        logger.critical(f"Krytyczny błąd skryptu: {e}", exc_info=True)