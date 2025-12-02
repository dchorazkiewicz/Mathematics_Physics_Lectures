# Section 1 — Linear Algebra: Exercises

## Matrices and basic operations

1. For matrices

$$
A=\begin{pmatrix}1 & 2\\ 3 & 4\end{pmatrix} \quad \text{i} \quad B=\begin{pmatrix}0 & -1\\ 2 & 1\end{pmatrix}
$$

   calculate

   - $A+B$
   - $A-B$
   - $2A$
   - $A^2$
   - $3B-2A$
   - $A\cdot B$
   - check if $A\cdot B = B\cdot A$.

2. For matrices

$$
   A=\begin{pmatrix}1 & 0\\ 0 & 2\end{pmatrix}, 
   \quad
   B =\begin{pmatrix}2 & 0\\ 0 & 4\end{pmatrix}, 
   \quad
   C=\begin{pmatrix}4 & 0\\ 0 & 8\end{pmatrix},
   \quad
   D=\begin{pmatrix}8 & 0\\ 0 & 16\end{pmatrix}
$$

check if

$$
A\cdot B\cdot C\cdot D = B\cdot A\cdot D\cdot C = D\cdot C\cdot B\cdot A.
$$


3. Given the matrix

$$
   C=\begin{pmatrix}
   1 & 0 & 2\\
   -1 & 3 & 1\\
   0 & 2 & -1
   \end{pmatrix}.
$$

   Determine the matrix obtained after interchanging the rows: swap the 1st and 3rd row, and then add twice the new 1st row to the 2nd row. Write down all steps for each operation.

4. Show that the diagonal matrix $D=\operatorname{diag}(2,-3,5)$ commutes with any diagonal matrix $E=\operatorname{diag}(a,b,c)$. Additionally, calculate $D^{3}$ and, if it exists, $D^{-1}$.

6. $\star$ For the matrix
 
   $$
   P=\begin{pmatrix}1 & 1 & 0\\ 0 & 1 & 1\\ 1 & 0 & 1\end{pmatrix}
   $$

   calculate $P^{2}$ and $P^{3}$. Does the sequence $P^{n}$ have a noticeable pattern for $n=1,2,3$?



9. $\star\star$ The Pauli matrices are defined as:

   $$
   \sigma_x = \begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}, \quad
   \sigma_y = \begin{pmatrix}0 & -i\\ i & 0\end{pmatrix}, \quad
   \sigma_z = \begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix}
   $$

   where $i$ is the imaginary unit. Verify that:

   - $\sigma_x^2 = \sigma_y^2 = \sigma_z^2 = I$ (identity matrix)
   - $\sigma_x\sigma_y = i\sigma_z$, $\sigma_y\sigma_z = i\sigma_x$, $\sigma_z\sigma_x = i\sigma_y$
   - $\{\sigma_i, \sigma_j\} = 2\delta_{ij}I$ (anticommutator)


## Determinants

1. Calculate the determinant of the matrices

$$
\mathbf{A} =
\begin{pmatrix}
2 & 3 \\
1 & 4
\end{pmatrix}
, \qquad
\mathbf{B} =
\begin{pmatrix}
5 & 6 \\
7 & 8
\end{pmatrix}
, \qquad
\mathbf{C} =
\begin{pmatrix}
-1 & 2 \\
3 & 0
\end{pmatrix}
$$

   $$
   A=\begin{pmatrix}
   2 & 3 & 1\\
   0 & -1 & 4\\
   5 & 2 & 0
   \end{pmatrix}
   \quad
   B=\begin{pmatrix}
   1 & 2 & 2\\
   4 & 0 & 0\\
   7 & 8 & 9
   \end{pmatrix}
   \qquad
   C=\begin{pmatrix}
   3 & 0 & 2\\
   2 & 0 & -2\\
   0 & 1 & 1
   \end{pmatrix}
   $$

   using the Sarrus method.

2. Determine the determinants using Laplace expansion:

   $$
   A=\begin{pmatrix}
   1
   \end{pmatrix}
   \quad
   B=\begin{pmatrix}
   1 & 0 & 2\\
   3 & 1 & 0\\
   4 & 5 & 6
   \end{pmatrix}
   \quad
   C=\begin{pmatrix}
   1 & 2 & 3 & 4\\
   0 & 1 & 0 & 0\\
   0 & 0 & 1 & 1\\
   0 & 0 & 0 & 2
   \end{pmatrix} 
   $$

3. Show that if two rows in a matrix are equal, the determinant is zero. Give an example of a $3\times3$ matrix with two equal rows and calculate its determinant. Justify why this happens.

5. For the matrix dependent on parameter $t$:

   $$
   M(t)=\begin{pmatrix}
   t & 1\\
   2 & t\\
   \end{pmatrix}
   $$

   calculate $\det(M(t))$ and find the values of $t$ for which the matrix is singular.

6. Solve the equation

   $$
   \det\begin{pmatrix}
   x & 3\\
   2 & x
   \end{pmatrix} = 0
   $$

7. $\star$ Solve the equation

   $$
   \det\begin{pmatrix}
   x & 3\\
   2 & -x
   \end{pmatrix} = 0
   $$




10. Calculate the determinant of the matrices
   $$
   \begin{vmatrix}
   a & a & a \\
   -a & a & a \\
   -a & -a & a
   \end{vmatrix}
   \quad
   \text{oraz}
   \quad
   \begin{vmatrix}
   a & 0 & b \\
   0 & c & 0 \\
   d & 0 & a
   \end{vmatrix}
   $$

8. Verify the validity of:

 
$$
   \begin{vmatrix}
   a+b & b \\
   c+d & d
   \end{vmatrix}
   =
   \begin{vmatrix}
   a & b \\
   c & d
   \end{vmatrix}
$$



## Matrix Inversion

1. Find the rank of the matrix:

$$\mathbf{B} =
\begin{pmatrix}
4 & -3 & 7 \\
-1 & 6 & 3 \\
2 & 9 & 1
\end{pmatrix}$$

2. Find the inverse matrix using the $2\times2$ matrix formula
   $$
   A=\begin{pmatrix}2 & 1\\ 5 & 3\end{pmatrix}
   \qquad
   B=\begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}
   \qquad
   C=\begin{pmatrix}4 & 7\\ 2 & 6\end{pmatrix}
   $$


3. For the matrices

   $$
   A=\begin{pmatrix}1 & 2\\ 2 & 5\end{pmatrix}
   \quad
   B=\begin{pmatrix}12& 5\\ 7 & 3\end{pmatrix}
   \quad
   C=\begin{pmatrix}1 & 2 & 3\\ 0 & 1 & 4\\ 5 & 6 & 0\end{pmatrix}
   \quad
   D=\begin{pmatrix}2 & 0 & 1\\ 1 & 3 & 0\\ 0 & 4 & 5\end{pmatrix}
   $$

   calculate the inverse matrices using the methods:

   - adjoining the identity matrix and performing Gauss-Jordan elimination,
   - using the formula with cofactor matrices

   That is, for each matrix, provide two methods for calculating the inverse matrix (if it exists).

4. Check if the matrix

   $$
   H=\begin{pmatrix}1 & 2 & 3\\ 2 & 4 & 6\\ 0 & 1 & 1\end{pmatrix}
   $$

   is invertible. Justify the answer (use the determinant). Could this have been noticed without calculating the determinant? What would have to happen for the matrix to be invertible?

5. For a matrix $A$ satisfying $A^{2}=I$ show that $A^{-1}=A$. Give an example of a non-trivial $2\times2$ matrix satisfying this condition (other than $I$ and $-I$). How many such matrices are there?

6. Calculate the inverse matrix of the diagonal matrix $D=\operatorname{diag}(2,5,-3,1)$, if it exists. Discuss the condition for the existence of the inverse for a diagonal matrix.

6. Solve the matrix equations:

a) 
   
$$
\begin{bmatrix} 2 & 5 \\\ 1 & 3 \end{bmatrix} \cdot X = \begin{bmatrix} 4 & -6 \\\ 2 & 1 \end{bmatrix}
$$

b) 

$$
\begin{bmatrix} 2 & 1 \\\ 5 & 3 \end{bmatrix} \cdot X = \begin{bmatrix} 1 & 2 \\\ 3 & 4 \end{bmatrix}
$$

c) 
   
$$
X \cdot \begin{bmatrix} 1 & 1 & -1 \\\ 2 & 1 & 0 \\\ 1 & -1 & 1 \end{bmatrix} = \begin{bmatrix} 1 & -3 & 3 \\\ 4 & 3 & 2 \\\ 1 & -2 & 5 \end{bmatrix}
$$

d) 

$$
\begin{bmatrix} 3 & 2 & 3 \\\ 1 & 1 & 2 \\\ 3 & 2 & 4 \end{bmatrix} \cdot X = \begin{bmatrix} 1 & 2 & 3 \\\ 1 & -1 & 2 \\\ 2 & 2 & 4 \end{bmatrix}
$$

## Systems of linear equations

1. Solve the system of equations:

   $$
   \begin{aligned} 2x+3y&=5,\\ x-4y&=-2. \end{aligned}
   $$

   using the methods: Cramer's rule, Gauss elimination, and inverse matrix.

2. Solve the system of three equations with three unknowns:

   $$
   \begin{aligned} x+y+z&=6,\\ 2x-y+3z&=14,\\ -x+2y-z&=-2. \end{aligned}
   $$

   using the methods: Cramer's rule, Gauss elimination, and inverse matrix.

3. $\star$ Consider the parametric system dependent on $\lambda$:

   $$
   \begin{aligned} x+\lambda y&=1,\\ 2x+(1+\lambda)y&=3. \end{aligned}
   $$

   Determine the values of $\lambda$ for which the system has one solution, infinitely many solutions, or no solutions.

4. For the coefficient matrix

   $$
   A=\begin{pmatrix}1 & 1 & 1\\ 0 & 2 & -1\\ 2 & -1 & 3\end{pmatrix}
   $$

   and the vertical right-hand side vector $b=(4,1,3)^{\top}$ solve $Ax=b$ and check the result by substitution.


5. Solve the systems of equations:

   a)

   $$
   \begin{cases}
   x_1 + 4x_2 + 3x_3 = 1, \\
   2x_1 + 5x_2 + 4x_3 = 4, \\
   x_1 - 3x_2 - 2x_3 = 5;
   \end{cases}
   $$

   b)

   $$
   \begin{cases}
   x_1 - 2x_2 - 3x_3 = 2, \\
   x_1 - 4x_2 - 13x_3 = 14, \\
   -3x_1 + 5x_2 + 4x_3 = 0;
   \end{cases}
   $$

   c)

   $$
   \begin{cases}
   x_1 - 2x_2 - 3x_3 = 2, \\
   x_1 - 4x_2 - 13x_3 = 14, \\
   -3x_1 + 5x_2 + 4x_3 = 2;
   \end{cases}
   $$

   d)

   $$
   \begin{cases}
   -4x_1 + 3x_2 + 2x_3 = -2, \\
   5x_1 - 4x_2 + x_3 = 3;
   \end{cases}
   $$

   e)

   $$
   \begin{cases}
   -4x_1 + 3x_2 = 2, \\
   5x_1 - 4x_2 = 0, \\
   2x_1 - x_2 = a;
   \end{cases}
   $$

   f)

   $$
   \begin{cases}
   4x_1 + 5x_3 = 6, \\
   x_2 - 6x_3 = -2, \\
   3x_1 + 4x_3 = 3;
   \end{cases}
   $$

   g)

   $$
   \begin{cases}
   3x_1 - x_2 - 2x_3 = 2, \\
   2x_2 - x_3 = -1, \\
   3x_1 - 5x_2 = 3;
   \end{cases}
   $$

   h)

   $$
   \begin{cases}
   -x_1 + 2x_2 + 3x_3 = 0, \\
   x_1 - 4x_2 - 13x_3 = 0, \\
   -3x_1 + 5x_2 + 4x_3 = 0;
    \end{cases}
   $$


   i)

   $$
   \begin{cases}
   x_1 + x_2 + x_3 = 0, \\
   2x_1 + 4x_2 + 3x_3 = 0, \\
   4x_2 + 4x_3 = 0;
   \end{cases}
   $$

   j)

   $$
   \begin{cases}
   x_1 + x_2 + x_3 = -2, \\
   2x_1 + 4x_2 - 3x_3 = 3, \\
   4x_2 + 2x_3 = 2;
   \end{cases}
   $$

   k)

   $$
   \begin{cases}
   4x_1 + 4x_3 = 8, \\
   x_2 - 6x_3 = -3, \\
   3x_1 + x_2 - 3x_3 = 3;
   \end{cases}
   $$

   l)

   $$
   \begin{cases}
   5x_1 - 3x_2 = -7, \\
   -2x_1 + 9x_2 = 4, \\
   2x_1 + 4x_2 = -2;
   \end{cases}
   $$