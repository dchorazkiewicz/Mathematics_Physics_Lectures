import numpy as np

# Ustawienia wydruku dla czytelności
np.set_printoptions(precision=3, suppress=True)

print("--- Weryfikacja: Macierze i podstawowe operacje ---")
# Zadanie 1
A1 = np.array([[1, 2], [3, 4]])
B1 = np.array([[0, -1], [2, 1]])

print("A =\n", A1)
print("B =\n", B1)
print("A + B =\n", A1 + B1)
print("A - B =\n", A1 - B1)
print("2A =\n", 2 * A1)
print("3B - 2A =\n", 3 * B1 - 2 * A1)
print("A * B =\n", A1 @ B1)
print("B * A =\n", B1 @ A1)
print("-" * 20)


print("\n--- Weryfikacja: Wyznaczniki ---")
# Zadanie 1
A2 = np.array([[2, 3, 1], [0, -1, 4], [5, 2, 0]])
B2 = np.array([[1, 2, 2], [4, 0, 0], [7, 8, 9]])
C2 = np.array([[3, 0, 2], [2, 0, -2], [0, 1, 1]])

print("det(A) =", np.linalg.det(A2))
print("det(B) =", np.linalg.det(B2))
print("det(C) =", np.linalg.det(C2))
print("-" * 20)


print("\n--- Weryfikacja: Odwracanie macierzy ---")
# Zadanie 1
A3 = np.array([[2, 1], [5, 3]])
B3 = np.array([[0, 1], [1, 0]])
C3 = np.array([[4, 7], [2, 6]])

print("inv(A) =\n", np.linalg.inv(A3))
print("inv(B) =\n", np.linalg.inv(B3))
print("inv(C) =\n", np.linalg.inv(C3))
print("-" * 20)


print("\n--- Weryfikacja: Układy równań liniowych ---")
# Zadanie 1
A4 = np.array([[2, 3], [1, -4]])
b4 = np.array([5, -2])
x4 = np.linalg.solve(A4, b4)
print("Rozwiązanie x, y dla układu 1:", x4, f"(czyli x={x4[0]}, y={x4[1]})")
print(f"Sprawdzenie: 14/11 = {14/11}, 9/11 = {9/11}")


# Zadanie 2
A5 = np.array([[1, 1, 1], [2, -1, 3], [-1, 2, -1]])
b5 = np.array([6, 14, -2])
try:
    x5 = np.linalg.solve(A5, b5)
    print("Rozwiązanie x, y, z dla układu 2:", x5, f"(czyli x={x5[0]}, y={x5[1]}, z={x5[2]})")
    print(f"Sprawdzenie: -4/3 = {-4/3}, 4/3 = {4/3}")
except np.linalg.LinAlgError as e:
    print("Błąd przy rozwiązywaniu układu 2:", e)

print("-" * 20)
