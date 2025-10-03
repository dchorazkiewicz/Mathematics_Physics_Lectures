# Student Guide: Learning Linear Algebra with Your AI Assistant

Welcome to an interactive guide to the world of matrices! The purpose of this document is to show you how you can use tools such as Gemini to explore linear algebra topics on your own and at your own pace.

## Key to success: your activity and curiosity

Before we begin, remember the most important thing: this tool exists to serve you. The following tips will help you make the most of it.

**You are in charge of your learning!**

This guide and the included prompts are only starting points. Real learning begins when you start asking your own questions.

* Don't understand a term? Ask the AI: "Explain what a 'scalar' is in the simplest possible way."
* An example is unclear? Ask for another: "Can you give me another, more practical example of matrix multiplication?"
* Want to check yourself? Verify your thinking: "If I understand correctly, to add two matrices they must have exactly the same dimensions, right?"

**Take responsibility for your learning**

Approach this task seriously. The AI assistant is your personal interactive textbook and sparring partner, not a machine for mindlessly generating answers. You can't cheat here — the only person you will be fooling is yourself. The goal is understanding, not mechanically copying questions. If you don't spend time actively thinking, asking questions, and attempting to solve problems on your own, the knowledge will not stick. What you don't understand now will resurface on a quiz or exam. Failure to master the material will be your failure, not the tool's. Use this opportunity wisely.

## How to start? Technical tips

**How should you use this guide?**

Below you will find a series of topics. Each is divided into three sections:

* **Building intuition:** Ready-made prompts you can ask the AI to explain the key concepts.
* **Practice and interactive exercises:** Prompts that turn the AI into your practice partner.
* **Mini-quiz:** Short tests to verify the knowledge you've gained.

You can start by copying the prepared prompts in quotes — it's a great starting point. Remember, you steer the learning process. If you don't know what to ask next, ask the AI for help, for example: "What else can I ask to better understand this topic?"

**How to write matrices in chat?**

For the AI to understand which matrix you mean, it's best to use nested list notation. Put each row of the matrix in its own square brackets `[]`, and wrap the whole thing in an additional pair of brackets. Separate elements in a row with commas.
For example the matrix:

$$A= \begin{bmatrix} 1 & 2 & 3 \\\ 4 & 5 & 6 \end{bmatrix}$$

You would write in chat as: `[[1, 2, 3], [4, 5, 6]]`
So we have a list of lists: the outer list contains two elements (rows), and each of those is another list with three elements (columns).

---

## Topic 1: What is a matrix? Definitions and basics

**Key concepts:** In this section you'll learn and understand the terms: matrix, entry (element) of a matrix, row, column, dimension of a matrix.
Before we start more complicated operations, we need to understand what a matrix is.

* **Step 1: Building intuition**
    * **Prompt 1.1:** "Explain what a matrix is using a simple real-world analogy, e.g., a spreadsheet or the board in the game Battleship."
    * **Prompt 1.2:** "Define the basic terms related to matrices: entry, row, column, matrix dimension (e.g., 3x4). Give a simple example of a matrix and label all those parts on it."

* **Step 2: Practice and interactive exercises**
    * **Prompt 1.3:** "Create for me a matrix A of size 3x4 with arbitrary integers. Then ask me to indicate the entry located in the second row and third column (a_23) and the entry in the first row and fourth column (a_14). Check my answer and, if incorrect, explain why it is wrong."

* **Step 3: Mini-quiz**
    * **Prompt 1.4:** "Give me 3 short questions to check if I understand what a matrix is, its dimensions, and how to identify its entries. One question should be true/false."

---

## Topic 2: Special matrices

**Key concepts:** In this section you'll learn the terms: square matrix, zero matrix, diagonal matrix, identity matrix, transpose, transposition.

* **Step 1: Building intuition**
    * **Prompt 2.1:** "Explain and give examples of the following special matrices: square matrix, zero matrix, diagonal matrix, identity matrix and transpose. What are their characteristic properties?"
    * **Prompt 2.2:** "Show how transposing a 3x2 matrix looks. Explain step by step what happens to rows and columns."

* **Step 2: Practice and interactive exercises**
    * **Prompt 2.3:** "Provide me with a square matrix B of size 4x4 that is not diagonal. Ask me to transpose it. Then check my result."
    * **Prompt 2.4:** "Create a 3x3 matrix and ask me whether it is diagonal, identity, or none of those. I want you to check my answer and reasoning."

* **Step 3: Mini-quiz**
    * **Prompt 2.5:** "Prepare a mini-quiz. Give me 4 example matrices and I should identify their type (square, diagonal, identity, zero). One of the matrices should fit several types at once. Check my answers."

---

## Topic 3: Addition, subtraction and scalar multiplication

**Key concepts:** In this section you will learn: matrix addition and subtraction, scalar multiplication, scalar.

* **Step 1: Building intuition**
    * **Prompt 3.1:** "Explain how to add and subtract matrices. What condition must matrices satisfy for these operations to be valid? Show this on an example of two 2x3 matrices."
    * **Prompt 3.2:** "What does 'multiplying a matrix by a scalar' mean? Illustrate by multiplying a 2x2 matrix by the number 5 and explain what happens to each element."

* **Step 2: Practice and interactive exercises**
    * **Prompt 3.3:** "Create two matrices A and B of size 3x3. Walk me step by step through computing the expression: 2*A - B. At each stage ask me for the result, and at the end check the final answer."

* **Step 3: Mini-quiz**
    * **Prompt 3.4:** "Give me 3 calculation tasks: one with addition, one with subtraction and one with scalar multiplication. One of the tasks should be impossible to perform — my task will be to notice that and explain why."

* **Step 4: Optional extension - Geometric intuition**
    * **Prompt 3.5 (Scaling visualization):** "Let's use a simple visualization. Imagine a square in the plane with vertices at (0,0), (1,0), (1,1), (0,1). Write those vertices as a 2x4 matrix. Show me what happens to this square (how its vertices change) when we multiply that matrix by a scalar, e.g., 2 or 0.5. How does this algebraic operation affect the geometry of the shape?"

---

## Topic 4: Matrix multiplication

**Key concepts:** In this section you will learn: rules of matrix multiplication, the dimension condition for multiplication, non-commutativity of matrix multiplication.

* **Step 1: Building intuition**
    * **Prompt 4.1:** "Explain the dimension condition for matrix multiplication. If I have a matrix A of size m x n and a matrix B of size p x q, what relations between m, n, p, q must hold to compute A*B? What will be the dimension of the result matrix?"
    * **Prompt 4.2:** "Show step by step how to multiply a matrix A (2x3) by a matrix B (3x2). Focus on how one element of the result, e.g., c_11, is computed. Use a visualization or colors to show which row multiplies which column."
    * **Prompt 4.3:** "Is matrix multiplication commutative? That is, does A*B always equal B*A? Provide a counterexample to illustrate this."

* **Step 2: Practice and interactive exercises**
    * **Prompt 4.4:** "Create two matrices A (2x2) and B (2x2). Ask me to compute A*B. I want you to prompt me to compute each element of the result (c_11, c_12, c_21, c_22), checking my calculations along the way."

* **Step 3: Mini-quiz**
    * **Prompt 4.5:** "Prepare a quiz on matrix multiplication. Give me two pairs of matrices. For the first pair ask to check if multiplication is possible and, if so, to give the dimension of the result. For the second pair (e.g., 2x2 and 2x2) ask to perform the full multiplication."

* **Step 4: Common pitfalls**
    * **Prompt 4.6 (Pitfalls summary):** "Summarize 3 common mistakes students make when multiplying matrices. For example: confusing the dimension condition, assuming commutativity (A*B = B*A), or confusing matrix multiplication with element-wise multiplication. How can I avoid them?"

---

## Finale: Test your knowledge and discover applications

**Step 1: Final test — you decide when you're done!**

When you feel you understand all the above topics, it's time for a comprehensive test.

* **Prompt 5.1:** "Prepare a comprehensive test covering basic matrix operations. I want it to contain 5 tasks of varying difficulty, covering definitions, special matrices, addition, subtraction, scalar multiplication, and matrix multiplication."

After solving the test, analyze your answers carefully with the AI. If you made mistakes, that's great — it's the best time to learn. Return to the problematic topics.

* **Prompt 5.2 (example):** "In the test I had trouble with matrix multiplication. Can we practice it again? Give me two new examples and guide me step by step."

Remember: the end of learning is set by your full understanding of the topic, not by reaching the end of this document. Be honest with yourself — go back to materials until you feel confident.

**Step 2: Why learn this? Discover applications of matrices**

Abstract knowledge is interesting, but it becomes powerful when you see its practical uses. Spend a moment discovering where matrices hide in everyday problems.

* **Prompt 6.1 (Computer Science):** "Explain in simple terms how matrices are used in computer graphics to rotate and scale 3D objects. Can you give a simple example?"
* **Prompt 6.2 (Science and Engineering):** "Give examples of matrix use in other fields such as physics, engineering, economics or data analysis. I want to understand what real problems they help solve."
* **Prompt 6.3 (From math to code):** "I just computed a matrix multiplication by hand. Now show me how to perform the same operation in Python using NumPy. I want to see how the code reflects what I did on paper."

Understanding why you learn something is the best motivation to continue.

**Step 3: What next? A preview of the next module**

Well-designed learning paths create a sense of continuity. Spark your curiosity and see where the learning goes next.

* **Prompt 7.1 (Preview):** "I've mastered basic matrix operations. What is the next logical step in learning linear algebra? Give me a short, one-sentence preview of what determinants are and why they matter, without going into details."

Good luck on your journey through linear algebra!

