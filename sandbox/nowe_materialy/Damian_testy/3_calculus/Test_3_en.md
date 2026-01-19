## Problem 1
Find limit of the $a_n = \frac{2n^2 + 3n + 2}{5-2n^2}$ sequence at $n \to \infty$.

* A) $-1$
* B) $1$
* C) $\infty$
* D) $\frac{2}{5}$

## Problem 2
Find limit of the function $f(x) = \frac{\sin(x-\pi)}{x}$ at $x \to 0$.

* A) $0$
* B) $1$
* C) $-1$
* D) $\infty$

## Problem 3
Calculate the derivative of the function $y(x) = 2x^3 - 3x^2 + 8x - 9$.

* A) $6x^2 - 6x + 8$
* B) $6x^3 - 6x^2 + 8x$
* C) $2x^2 - 3x + 8$
* D) $6x^2 - 6x$

## Problem 4
Calculate the derivative of the function $y(x) = x\sin(x)+1$.

* A) $\sin(x) + x\cos(x)$
* B) $\cos(x)$
* C) $\sin(x) - x\cos(x)$
* D) $x\cos(x)$

## Problem 5
Calculate the integral $\int (x^2+3x+5)x dx$.

* A) $\frac{x^4}{4} + x^3 + \frac{5x^2}{2} + C$
* B) $x^3 + 3x^2 + 5x + C$
* C) $\frac{x^3}{3} + \frac{3x^2}{2} + 5x + C$
* D) $3x^2 + 6x + 5 + C$

\newpage

## Problem 6
Calculate the integral $\int x\sin(x^2) dx$.

* A) $-\frac{1}{2}\cos(x^2)$
* B) $2x\cos(x^2) + C$
* C) $-\frac{1}{2}\cos(x^2) + C$
* D) $-\cos(x^2) + C$

## Problem 7
Calculate the integral $\int \frac{x+2}{x+1} dx$.

* A) $x + \ln|x+1| + C$
* B) $\ln|x+1| + C$
* C) $x - \ln|x+1| + C$
* D) $1 + \frac{1}{x+1} + C$

## Problem 8
Find the area bounded by the x-axis and the curve $y = x^2$ on the interval $[0,2]$.

* A) $\frac{8}{3}$
* B) $4$
* C) $\frac{4}{3}$
* D) $\frac{1}{3}x^3+C$

## Problem 9
A particle moves along a straight line with its position at time $t$ given by the function $x(t) = t^3 - 6t^2 + 9t + 2$. Find the velocity $V(t) = \frac{dx(t)}{dt}$ and acceleration $a(t) = \frac{d^2x(t)}{dt^2}$ of the particle at time $t = 2$.

* A) Velocity: 0, Acceleration: -3
* B) Velocity: 3, Acceleration: 0
* C) Velocity: -3, Acceleration: 0
* D) Velocity: -3, Acceleration: 12

## Problem 10
Solve the differential equation $\frac{dy}{dx} = \frac{x+2}{x+1}$ with the initial condition $y(0) = 1$.

* A) $y(x) = x + \ln|x+1| + C$
* B) $y(x) = \ln|x+1| + 1$
* C) $y(x) = x + \ln|x+1| + 1$
* D) $y(x) = \frac{-1}{(x+1)^2}$

---
### Answers

1. **A**
2. **C**
3. **A**
4. **A**
5. **A**
6. **C**
7. **A**
8. **A**
9. **C**
10. **C**

###  WYNIKI ZADAŃ

Zadanie 1: -1

Zadanie 2: -1

Zadanie 3: 6*x^2 - 6*x + 8

Zadanie 4: x*cos(x) + sin(x)

Zadanie 5: x^4/4 + x^3 + 5*x^2/2 + C

Zadanie 6: -cos(x^2)/2 + C

Zadanie 7: x + log(x + 1) + C

Zadanie 8: 8/3

Zadanie 9: Prędkość v(2) = -3, 
Przyspieszenie a(2) = 0

Zadanie 10: x + log(x + 1) + 1


### Python code

```python
import sympy as sp

# Definiowanie symboli
n = sp.symbols('n')
x = sp.symbols('x')
t = sp.symbols('t')

print("--- WYNIKI ZADAŃ ---")

# Problem 1: Granica ciągu
expr1 = (2*n**2 + 3*n + 2) / (5 - 2*n**2)
limit1 = sp.limit(expr1, n, sp.oo)
print(f"Zadanie 1: {limit1}")

# Problem 2: Granica funkcji
expr2 = sp.sin(x - sp.pi) / x
limit2 = sp.limit(expr2, x, 0)
print(f"Zadanie 2: {limit2}")

# Problem 3: Pochodna wielomianu
expr3 = 2*x**3 - 3*x**2 + 8*x - 9
deriv3 = sp.diff(expr3, x)
print(f"Zadanie 3: {deriv3}")

# Problem 4: Pochodna iloczynu
expr4 = x * sp.sin(x) + 1
deriv4 = sp.diff(expr4, x)
print(f"Zadanie 4: {deriv4}")

# Problem 5: Całka nieoznaczona
expr5 = (x**2 + 3*x + 5) * x
integral5 = sp.integrate(expr5, x)
print(f"Zadanie 5: {integral5} + C")

# Problem 6: Całka przez podstawienie
expr6 = x * sp.sin(x**2)
integral6 = sp.integrate(expr6, x)
print(f"Zadanie 6: {integral6} + C")

# Problem 7: Całka wymierna
expr7 = (x + 2) / (x + 1)
integral7 = sp.integrate(expr7, x)
print(f"Zadanie 7: {integral7} + C")

# Problem 8: Pole powierzchni (całka oznaczona)
expr8 = x**2
area8 = sp.integrate(expr8, (x, 0, 2))
print(f"Zadanie 8: {area8}")

# Problem 9: Prędkość i przyspieszenie
x_t = t**3 - 6*t**2 + 9*t + 2
v_t = sp.diff(x_t, t)
a_t = sp.diff(v_t, t)
v_2 = v_t.subs(t, 2)
a_2 = a_t.subs(t, 2)
print(f"Zadanie 9: Prędkość v(2) = {v_2}, Przyspieszenie a(2) = {a_2}")

# Problem 10: Równanie różniczkowe
y = sp.Function('y')
diff_eq = sp.Eq(y(x).diff(x), (x + 2) / (x + 1))
solution = sp.dsolve(diff_eq, y(x), ics={y(0): 1})
print(f"Zadanie 10: {solution.rhs}")
```


