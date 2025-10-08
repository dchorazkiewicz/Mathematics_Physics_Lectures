# Student Guide: Learning Linear Algebra with Your AI Assistant

Welcome to an interactive guide to the world of matrices! In this final part of the algebra section we will combine everything we've learned to solve systems of linear equations.

## Key to success: your activity and curiosity

**You are in charge of your learning!**

* Don't understand a term? Ask the AI: "What is the difference between a determined and an underdetermined system?"
* An example is unclear? Ask for another: "Can you show me how Gaussian elimination works for a system that has no solutions?"
* Want to check yourself? Verify your thinking: "If I understand correctly, the inverse-matrix method works only for Cramer systems, right?"

**Take responsibility for your learning**

Approach this task seriously. The goal is understanding. Failure to master the material will be your failure. Use this opportunity wisely.

---

## Topic 1: Systems of equations in matrix language

**Key concepts:** In this section you'll learn: matrix form of a system (A x = b), coefficient matrix, vector of unknowns, right-hand side vector.

* **Step 1: Building intuition**
    * **Prompt 1.1:** "Show me how to write a system of three linear equations with three unknowns in matrix form A*x = b. Explain what the coefficient matrix A, the unknown vector x and the right-hand side vector b are."
    * **Prompt 1.2:** "Why is this notation useful? What advantages does viewing the system as a single matrix equation give us?"

* **Step 2: Practice and interactive tasks**
    * **Prompt 1.3:** "I'll give you the system: 2x + y - z = 8, -3x - y + 2z = -11, -2x + y + 2z = -3. Ask me to define the matrix A, vector x and vector b for this system. Check my answers."

* **Step 3: Mini-quiz**
    * **Prompt 1.4:** "Give me 2 short questions to check if I understand how to transform a system to matrix form and back."

---

## Topic 2: Inverse matrix method and Cramer's rule

**Key concepts:** In this section you'll learn: solving a system using the inverse matrix, Cramer systems, Cramer's rule.

* **Step 1: Building intuition**
    * **Prompt 2.1:** "Explain how to solve A*x = b using the inverse matrix A^{-1}. Show step by step how from A*x = b we obtain x = A^{-1}*b. What condition must A satisfy for this method to work?"
    * **Prompt 2.2:** "What is Cramer's rule? How do we compute the main determinant (W) and determinants for individual unknowns (Wx, Wy, etc.)? How do we get the solution from these values? When is this method applicable?"

* **Step 2: Practice and interactive tasks**
    * **Prompt 2.3:** "Take a simple 2x2 system: {5x + 2y = 4, 7x + 3y = 5}. Guide me step by step through solving it using the inverse-matrix method. Then solve it using Cramer's rule and compare results."

* **Step 3: Mini-quiz**
    * **Prompt 2.4:** "Give me a 2x2 system and ask me to solve it by my chosen method (Cramer's or inverse-matrix). Check my result."

---

## Topic 3: Gaussian elimination method

**Key concepts:** In this section you'll learn: augmented matrix of the system, elementary row operations, echelon form, Kronecker-Capelli theorem (intuition).

* **Step 1: Building intuition**
    * **Prompt 3.1:** "Explain the idea of Gaussian elimination. How do we form the augmented matrix [A | b]? How do we reduce it to row-echelon form using elementary row operations? How do we read the solution from row-echelon form?"
    * **Prompt 3.2:** "How can you recognize that a system is inconsistent using Gaussian elimination (e.g., getting a row [0 0 0 | 5])? And how to recognize that it's underdetermined (e.g., getting a zero row [0 0 0 | 0])? (Intuition of the Kronecker-Capelli theorem)"

* **Step 2: Practice and interactive tasks**
    * **Prompt 3.3:** "Take the system: {x + y + 2z = 9, 2x + 4y - 3z = 1, 3x + 6y - 5z = 0}. Guide me step by step through solving it using Gaussian elimination. After each row operation show how the augmented matrix changes."

* **Step 3: Mini-quiz**
    * **Prompt 3.4:** "Give me a system of 3 equations with 3 unknowns and ask me to solve it using Gaussian elimination. Check my result."

---

## Topic 4: Comparing methods

**Key concepts:** In this section you will compare the learned methods and learn to choose the appropriate one for a problem.

* **Step 1: Building intuition**
    * **Prompt 4.1:** "Let's compare three methods: Cramer's rule, inverse-matrix method and Gaussian elimination. Which is fastest for small 2x2 systems? Which is the most universal and also works for non-square or systems without a unique solution? Which is most efficient computationally for large systems and why is it used most often in software?"

* **Step 2: Practice and interactive tasks**
    * **Prompt 4.2:** "Give me 3 different systems (e.g., 2x2, 3x3, and one underdetermined or inconsistent). For each ask which method I would choose to solve it and why. Discuss my choices with me."

---

## Finale: Test your knowledge and close the Algebra chapter

**Step 1: Final test**

This is the final topic of the linear algebra series in this cycle. Let's check everything is clear.

* **Prompt 5.1:** "Prepare a combined test for solving systems of equations. I want it to contain 3 tasks, each to be solved by a different method: one by Cramer's rule, one by the inverse-matrix method, and one by Gaussian elimination."

**Step 2: Why learn this? Applications of systems of equations**

* **Prompt 6.1 (Practical problems):** "Give me a simple, real-life example of a problem that can be modeled and solved using a system of linear equations. E.g., a diet planning problem, mixing ingredients, or a simple electrical circuit (using Kirchhoff's laws)."
* **Prompt 6.2 (From math to code):** "I just solved a system by hand. Now show me how to do the same in Python using NumPy, using the function `np.linalg.solve()`."

**Step 3: What next? Preview of the next section**

Congratulations! You have completed the first fundamental part of the course: Linear Algebra.

* **Prompt 7.1 (Preview):** "I can operate on matrices and solve systems of equations. What is the next major branch of mathematics we'll explore? Give me a short, one-sentence preview of what 'Analytic Geometry' is and how it connects to the algebra I've just learned."

Good luck on your journey through mathematics!
