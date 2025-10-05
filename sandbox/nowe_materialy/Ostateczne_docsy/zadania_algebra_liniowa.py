import numpy as np
from sympy import symbols, Matrix, sin, cos, I, solve, pretty_print

# Do niektórych zadań symbolicznych (np. z parametrami) używamy biblioteki SymPy.
# Do obliczeń numerycznych na konkretnych liczbach używamy NumPy.

# Dział 1 — Algebra Liniowa: Zadania

print("Dział 1 — Algebra Liniowa: Zadania")

# ==========================================
# Macierze i podstawowe operacje
# ==========================================
print("\n## Macierze i podstawowe operacje")

# --- Zadanie 1 ---
print("\n--- Zadanie 1 ---")
A = np.array([[1, 2], [3, 4]])
B = np.array([[0, -1], [2, 1]])
print("A:\n", A)
print("B:\n", B)
print("A + B:\n", A + B)
print("A - B:\n", A - B)
print("2 * A:\n", 2 * A)
print("3 * B - 2 * A:\n", 3 * B - 2 * A)
print("A @ B (iloczyn macierzowy):\n", A @ B)
print("B @ A:\n", B @ A)
print("Czy A*B = B*A?", np.array_equal(A @ B, B @ A))

# --- Zadanie 3 ---
print("\n--- Zadanie 3 ---")
C = np.array([[1, 0, 2], [-1, 3, 1], [0, 2, -1]])
print("Oryginalna macierz C:\n", C)
C_mod = C.copy()
# Zamiana wiersza 1 i 3
C_mod[[0, 2]] = C_mod[[2, 0]]
print("Po zamianie wierszy 1 i 3:\n", C_mod)
# Dodanie do 2. wiersza dwukrotności nowego 1. wiersza
C_mod[1] = C_mod[1] + 2 * C_mod[0]
print("Po dodaniu do 2. wiersza dwukrotności nowego 1. wiersza:\n", C_mod)

# --- Zadanie 4 ---
print("\n--- Zadanie 4 ---")
u = np.array([[1], [-2], [3]])
v = np.array([[2], [0], [-1]])
print("u:\n", u)
print("v:\n", v)
print("u + v:\n", u + v)
print("u - v:\n", u - v)
uv_T = u @ v.T
print("u * v^T:\n", uv_T)
print("Rząd macierzy u * v^T:", np.linalg.matrix_rank(uv_T))
vu_T = v @ u.T
print("v * u^T:\n", vu_T)

# --- Zadanie 5 ---
print("\n--- Zadanie 5 ---")
D = np.diag([2, -3, 5])
print("Macierz D:\n", D)
print("D^3:\n", np.linalg.matrix_power(D, 3))
if np.linalg.det(D) != 0:
    D_inv = np.linalg.inv(D)
    print("D^-1:\n", D_inv)
else:
    print("Macierz D jest osobliwa, nie ma odwrotności.")

# --- Zadanie 7 (Symboliczne) ---
print("\n--- Zadanie 7 (Symboliczne) ---")
theta1, theta2 = symbols('theta1 theta2')
R1 = Matrix([[cos(theta1), -sin(theta1)], [sin(theta1), cos(theta1)]])
R2 = Matrix([[cos(theta2), -sin(theta2)], [sin(theta2), cos(theta2)]])
R_sum = Matrix([[cos(theta1 + theta2), -sin(theta1 + theta2)], [sin(theta1 + theta2), cos(theta1 + theta2)]])
# Sprawdzenie tożsamości R(t1)R(t2) = R(t1+t2)
is_equal = (R1 * R2).simplify() == R_sum.simplify()
print("R(t1) * R(t2):")
pretty_print((R1 * R2).simplify())
print("R(t1 + t2):")
pretty_print(R_sum)
print(f"Czy R(t1) * R(t2) == R(t1 + t2)? {is_equal}")


# --- Zadanie 9 (Symboliczne, Macierze Pauliego) ---
print("\n--- Zadanie 9 (Symboliczne, Macierze Pauliego) ---")
sigma_x = Matrix([[0, 1], [1, 0]])
sigma_y = Matrix([[0, -I], [I, 0]])
sigma_z = Matrix([[1, 0], [0, -1]])
I_2 = Matrix([[1, 0], [0, 1]])

print("sigma_x^2 == I?", sigma_x**2 == I_2)
print("sigma_y^2 == I?", sigma_y**2 == I_2)
print("sigma_z^2 == I?", sigma_z**2 == I_2)
print("sigma_x * sigma_y == i * sigma_z?", (sigma_x * sigma_y).simplify() == I * sigma_z)
print("sigma_y * sigma_z == i * sigma_x?", (sigma_y * sigma_z).simplify() == I * sigma_x)
print("sigma_z * sigma_x == i * sigma_y?", (sigma_z * sigma_x).simplify() == I * sigma_y)


# ==========================================
# Wyznaczniki
# ==========================================
print("\n## Wyznaczniki")

# --- Zadanie 1 ---
print("\n--- Zadanie 1 ---")
A_det = np.array([[2, 3, 1], [0, -1, 4], [5, 2, 0]])
B_det = np.array([[1, 2, 2], [4, 0, 0], [7, 8, 9]])
C_det = np.array([[3, 0, 2], [2, 0, -2], [0, 1, 1]])
print(f"det(A): {np.linalg.det(A_det):.2f}")
print(f"det(B): {np.linalg.det(B_det):.2f}")
print(f"det(C): {np.linalg.det(C_det):.2f}")

# --- Zadanie 5 ---
print("\n--- Zadanie 5 (Parametryczne) ---")
t = symbols('t')
M_t = Matrix([[t, 1], [2, t]])
det_M_t = M_t.det()
print("det(M(t)):", det_M_t)
singular_values = solve(det_M_t, t)
print("Wartości t, dla których macierz jest osobliwa:", singular_values)

# ==========================================
# Odwracanie macierzy
# ==========================================
print("\n## Odwracanie macierzy")

# --- Zadanie 1 ---
print("\n--- Zadanie 1 ---")
A_inv_1 = np.array([[2, 1], [5, 3]])
B_inv_1 = np.array([[0, 1], [1, 0]])
C_inv_1 = np.array([[4, 7], [2, 6]])
print("inv(A):\n", np.linalg.inv(A_inv_1))
print("inv(B):\n", np.linalg.inv(B_inv_1))
print("inv(C):\n", np.linalg.inv(C_inv_1))

# --- Zadanie 2 ---
print("\n--- Zadanie 2 ---")
A_inv_2 = np.array([[1, 2], [2, 4]])
B_inv_2 = np.array([[12, 5], [7, 3]])
C_inv_2 = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])

print("Macierz A:\n", A_inv_2)
if np.linalg.det(A_inv_2) == 0:
    print("Macierz A jest osobliwa, nie ma odwrotności.")
else:
    print("inv(A):\n", np.linalg.inv(A_inv_2))

print("\nMacierz B:\n", B_inv_2)
print("inv(B):\n", np.linalg.inv(B_inv_2))

print("\nMacierz C:\n", C_inv_2)
print("inv(C):\n", np.linalg.inv(C_inv_2))

# --- Zadanie 3 ---
print("\n--- Zadanie 3 ---")
H = np.array([[1, 2, 3], [2, 4, 6], [0, 1, 1]])
print("Macierz H:\n", H)
det_H = np.linalg.det(H)
print(f"det(H): {det_H:.2f}")
if np.isclose(det_H, 0):
    print("Macierz H jest osobliwa (wyznacznik bliski zera).")
else:
    print("Macierz H nie jest osobliwa.")

# ==========================================
# Układy równań liniowych
# ==========================================
print("\n## Układy równań liniowych")

# --- Zadanie 1 ---
print("\n--- Zadanie 1 ---")
A_eq1 = np.array([[2, 3], [1, -4]])
b_eq1 = np.array([5, -2])
x_eq1 = np.linalg.solve(A_eq1, b_eq1)
print("Rozwiązanie układu 1 (x, y):", x_eq1)

# --- Zadanie 2 ---
print("\n--- Zadanie 2 ---")
A_eq2 = np.array([[1, 1, 1], [2, -1, 3], [-1, 2, -1]])
b_eq2 = np.array([6, 14, -2])
x_eq2 = np.linalg.solve(A_eq2, b_eq2)
print("Rozwiązanie układu 2 (x, y, z):", x_eq2)

# --- Zadanie 3 (Symboliczne) ---
print("\n--- Zadanie 3 (Symboliczne) ---")
lambda_sym = symbols('lambda')
A_eq3_sym = Matrix([[1, lambda_sym], [2, 1 + lambda_sym]])
det_A_eq3 = A_eq3_sym.det()
print("Wyznacznik macierzy układu 3:", det_A_eq3)
singular_lambda = solve(det_A_eq3, lambda_sym)
print(f"Układ ma jedno rozwiązanie, gdy wyznacznik != 0, czyli lambda != {singular_lambda[0]}")
# Analiza dla lambda = 1
A_lambda_1 = Matrix([[1, 1], [2, 2]])
b_lambda_1 = Matrix([1, 3])
# Rząd macierzy A i macierzy rozszerzonej [A|b]
print(f"Dla lambda = {singular_lambda[0]}:")
print("Rząd macierzy A:", A_lambda_1.rank())
print("Rząd macierzy rozszerzonej:", A_lambda_1.row_join(b_lambda_1).rank())
print("Rzędy są różne, więc układ jest sprzeczny (brak rozwiązań).")

# --- Zadanie 4 ---
print("\n--- Zadanie 4 ---")
A_eq4 = np.array([[1, 1, 1], [0, 2, -1], [2, -1, 3]])
b_eq4 = np.array([4, 1, 3])
x_eq4 = np.linalg.solve(A_eq4, b_eq4)
print("Rozwiązanie układu 4:", x_eq4)
# Sprawdzenie
print("A * x:", A_eq4 @ x_eq4)
print("Czy A*x == b?", np.allclose(A_eq4 @ x_eq4, b_eq4))
