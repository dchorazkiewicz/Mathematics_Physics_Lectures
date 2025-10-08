# Student Guide: Learning Linear Algebra with Your AI Assistant

Welcome to an interactive guide to the world of matrices! The purpose of this document is to show you how you can use tools such as Gemini to explore linear algebra topics on your own and at your own pace.

## Key to success: your activity and curiosity

**You are in charge of your learning!**

* Don't understand a term? Ask the AI: "Explain what a 'singular matrix' is in the simplest possible way."
* An example is unclear? Ask for another: "Can you show me how Gauss-Jordan elimination works on a different 2x2 matrix?"
* Want to check yourself? Verify your thinking: "If I understand correctly, an inverse matrix exists only when the determinant is nonzero, right?"

**Take responsibility for your learning**

Approach this task seriously. The AI assistant is your personal interactive textbook and sparring partner, not a machine for mindlessly generating answers. The goal is understanding, not mechanically copying questions. Failure to master the material will be your failure. Use this opportunity wisely.

---

## Topic 1: The concept of the inverse matrix

**Key concepts:** In this section you'll learn and understand the terms: inverse matrix, identity matrix, singular and nonsingular matrices.

* **Step 1: Building intuition**
    * **Prompt 1.1:** "Explain what an inverse matrix is. Use the analogy to multiplicative inverses of numbers (e.g., 5 and 1/5). What role does the identity matrix (I) play in this context?"
    * **Prompt 1.2:** "What does it mean that A * $A^{-1}$ = $A^{-1}$ * A = I? Why is this important? What is a singular and nonsingular matrix and how does that relate to the existence of an inverse?"

* **Step 2: Practice and interactive tasks**
    * **Prompt 1.3:** "I have matrix A = [[2, 1], [5, 3]] and matrix B = [[3, -1], [-5, 2]]. Let's check together whether B is the inverse of A. Guide me through computing A * B and check whether the result is the identity matrix."

* **Step 3: Mini-quiz**
    * **Prompt 1.4:** "Give me 3 conceptual questions about inverse matrices. One should be true/false, e.g., 'Every square matrix has an inverse.'"

---

## Topic 2: Cofactor method (determinant-based method)

**Key concepts:** In this section you'll learn: the existence condition for an inverse (det(A) != 0), cofactors, the adjugate matrix (transpose of the cofactor matrix), and the formula for the inverse matrix.

* **Step 1: Building intuition**
    * **Prompt 2.1:** "Explain step by step how to find the inverse using the determinant/cofactor method. Cover each stage: 1. Compute the determinant, 2. Build the matrix of minors, 3. Form the cofactor matrix, 4. Transpose to get the adjugate matrix, 5. Multiply by 1/det(A)."
    * **Prompt 2.2:** "Why is the condition det(A) != 0 so crucial in this method? What would happen if we tried to invert a matrix with determinant zero?"

* **Step 2: Practice and interactive tasks**
    * **Prompt 2.3:** "Create a 3x3 matrix A. Guide me step by step through computing its inverse using the cofactor method. At each stage ask me for results (e.g., 'What is the determinant?', 'What is the cofactor matrix?') and check my answers."

* **Step 3: Mini-quiz**
    * **Prompt 2.4:** "Give me a 2x2 matrix and ask me to find its inverse using the formula. Check my result."

---

## Topic 3: Determinant-free method (Gauss-Jordan elimination)

**Key concepts:** In this section you'll learn: the Gauss-Jordan method, the augmented matrix [A | I], and elementary row operations.

* **Step 1: Building intuition**
    * **Prompt 3.1:** "Explain how the Gauss-Jordan elimination method finds an inverse matrix. How do we form the augmented matrix [A | I] and what form [I | $A^{-1}$] do we aim for? Which three elementary row operations are allowed?"
    * **Prompt 3.2:** "Which method do you think is better or faster for hand calculations: cofactors or Gauss-Jordan? Which is more commonly implemented on computers and why?"

* **Step 2: Practice and interactive tasks**
    * **Prompt 3.3:** "Create a 3x3 matrix A and form the augmented matrix [A | I]. Guide me step by step through the elementary row operations to transform the left side into the identity matrix. After each operation show the current augmented matrix."

* **Step 3: Mini-quiz**
    * **Prompt 3.4:** "Give me a 3x3 matrix where one method is clearly simpler (e.g., zeros that simplify calculations). Ask me to find the inverse by my chosen method and check the result."

---

## Finale: Test your knowledge and discover applications

* **Prompt 5.1:** "Prepare a combined test on inverse matrices. I want it to contain 2 tasks: one computational for a 3x3 matrix using cofactors and one computational for a 3x3 matrix using Gauss-Jordan."

* **Prompt 6.1 (Systems of equations):** "How is the inverse matrix used to solve linear systems in the form A*x = b? Show how to transform the equation to find 'x'. Why is this method elegant theoretically but often impractical for large systems compared to other methods?"
* **Prompt 6.2 (From math to code):** "I just computed an inverse by hand. Now show me how to perform the same operation in Python using NumPy. Let's compare results."

* **Prompt 7.1 (Preview):** "I have mastered inverse matrices. What is the next logical step in learning linear algebra? Give me a short, one-sentence preview of how we will now combine knowledge of matrices, determinants and inverses to solve linear systems."

Good luck on your journey through linear algebra!
