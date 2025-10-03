# Student Guide: Learning Linear Algebra with Your AI Assistant

Welcome to an interactive guide to the world of matrices! The purpose of this document is to show you how you can use tools such as Gemini to explore linear algebra topics on your own and at your own pace.

## Key to success: your activity and curiosity

Before we begin, remember the most important thing: this tool exists to serve you. The following tips will help you make the most of it.

**You are in charge of your learning!**

This guide and the included prompts are only starting points. Real learning begins when you start asking your own questions.

* Don't understand a term? Ask the AI: "Explain what an 'algebraic complement' (cofactor) is in the simplest possible way."
* An example is unclear? Ask for another: "Can you show me how to apply Sarrus' rule to a different 3x3 matrix?"
* Want to check yourself? Verify your thinking: "If I understand correctly, a determinant equal to zero means the matrix is in some sense 'singular', right?"

**Take responsibility for your learning**

Approach this task seriously. The AI assistant is your personal interactive textbook and sparring partner, not a machine for mindlessly generating answers. You can't cheat here — the only person you will be fooling is yourself. The goal is understanding, not mechanically copying questions. If you don't spend time actively thinking, asking questions, and attempting to solve problems on your own, the knowledge will not stick. What you don't understand now will resurface on a quiz or exam. Failure to master the material will be your failure, not the tool's. Use this opportunity wisely.

---

## Topic 1: Definition and interpretation of the determinant

**Key concepts:** In this section you'll learn and understand the terms: determinant, square matrix, geometric interpretation of the determinant.

* **Step 1: Building intuition**
    * **Prompt 1.1:** "Explain what the determinant of a matrix is. Why can we compute it only for square matrices? Use a simple analogy."
    * **Prompt 1.2:** "What is the geometric interpretation of the determinant for 2x2 and 3x3 matrices? What does it mean if the determinant is positive, negative, or zero?"

* **Step 2: Practice and interactive exercises**
    * **Prompt 1.3:** "I have matrix A = [[3, 1], [4, 2]]. Show me how its column vectors, [3, 4] and [1, 2], form a parallelogram on the plane. How does the area of that parallelogram relate to the determinant of this matrix?"

* **Step 3: Mini-quiz**
    * **Prompt 1.4:** "Give me 3 questions to check whether I understand the concept of determinant. One question should concern its geometric interpretation, and another should be true/false (e.g., 'The determinant can be computed for any matrix')."

---

## Topic 2: Sarrus' rule (for 2x2 and 3x3 matrices)

**Key concepts:** In this section you'll learn: the formula for the determinant of a 2x2 matrix, Sarrus' rule for a 3x3 matrix.

* **Step 1: Building intuition**
    * **Prompt 2.1:** "Show me the formula for the determinant of a 2x2 matrix. Illustrate it on a simple example, e.g., for [[a, b], [c, d]]."
    * **Prompt 2.2:** "Explain step by step how Sarrus' rule works for computing the determinant of a 3x3 matrix. Use the scheme of appending the first two columns and multiplying along diagonals."

* **Step 2: Practice and interactive exercises**
    * **Prompt 2.3:** "Create a 3x3 matrix named B. Guide me step by step through computing its determinant using Sarrus' rule. Ask me for the product along each diagonal and then for the final sum."

* **Step 3: Mini-quiz**
    * **Prompt 2.4:** "Give me two matrices: one 2x2 and one 3x3. Ask me to compute their determinants. Check my results."

---

## Topic 3: Laplace expansion — the universal method

**Key concepts:** In this section you'll learn: minor, algebraic complement (cofactor), Laplace expansion.

* **Step 1: Building intuition**
    * **Prompt 3.1:** "What is the minor and the cofactor of an element of a matrix? Explain using a 3x3 matrix example showing how to find M_12 and the cofactor A_12."
    * **Prompt 3.2:** "Explain how Laplace expansion works. Why is it more universal than Sarrus' rule? Show how to use it by expanding the determinant along a chosen row or column."

* **Step 2: Practice and interactive exercises**
    * **Prompt 3.3:** "Create a 4x4 matrix. Together choose a row or column that looks simplest (for example, has the most zeros). Guide me through computing the determinant of that matrix using Laplace expansion along the chosen row/column."

* **Step 3: Mini-quiz**
    * **Prompt 3.4:** "Give me a 4x4 matrix with one zero. Ask me to compute its determinant using Laplace expansion. Check my result."

---

## Topic 4: Elementary row operations method (Gaussian method)

**Key concepts:** In this section you'll learn: the effect of elementary row operations on the determinant, computing the determinant by reducing to a triangular matrix.

* **Step 1: Building intuition**
    * **Prompt 4.1:** "How do the three elementary row operations (swapping rows, multiplying a row by a scalar, adding a multiple of one row to another) affect the determinant?"
    * **Prompt 4.2:** "Explain how to compute the determinant by bringing a matrix to echelon (triangular) form using elementary operations. What is the determinant of a triangular matrix?"

* **Step 2: Practice and interactive exercises**
    * **Prompt 4.3:** "Create a 4x4 matrix. Walk me step by step through computing its determinant using elementary row operations. After each operation, remind me how the determinant value changed."

* **Step 3: Mini-quiz**
    * **Prompt 4.4:** "Give me a 3x3 matrix and ask me to compute its determinant using Gaussian elimination. Check my result."

---

## Finale: Test your knowledge and discover applications

**Step 1: Final test**

* **Prompt 5.1:** "Prepare a comprehensive test on determinants. I want it to contain 4 tasks of varying difficulty, each to be solved by a different method (Sarrus, Laplace, Gauss) and one question about geometric interpretation."

**Step 2: Why learn this? Applications of determinants**

* **Prompt 6.1 (Systems of equations):** "How are determinants used to solve systems of linear equations? Explain the idea of Cramer's rule on a simple example of a system of two equations with two unknowns."
* **Prompt 6.2 (From math to code):** "I just computed a determinant by hand. Now show me how to perform the same operation in Python using NumPy. I want to see how the code reflects what I did on paper."

**Step 3: What next? A preview of the next module**

* **Prompt 7.1 (Preview):** "I have mastered determinants. What is the next logical step in learning linear algebra? Give me a short, one-sentence preview of what an 'inverse matrix' is and why the determinant is key to finding it."

Good luck on your journey through linear algebra!
