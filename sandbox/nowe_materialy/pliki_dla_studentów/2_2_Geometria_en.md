# Student Guide: Learning Geometry with Your AI Assistant

Welcome to an interactive guide to analytic geometry! In this part we'll learn how to multiply vectors in different ways and what follows from those operations.

## Key to success: your activity and curiosity

**You are in charge of your learning!**

* Don't understand a term? Ask the AI: "Explain what 'orthogonality' means in the context of vectors." 
* An example is unclear? Ask for another: "Can you show me how the right-hand rule works for other vectors?"
* Want to check yourself? Verify your thinking: "If I understand correctly, the dot product of two vectors is a number, while the cross product is a new vector, right?"

**Take responsibility for your learning**

Approach this task seriously. The goal is understanding. Failure to master the material will be your failure. Use this opportunity wisely.

---

## Topic 1: Dot product — measuring angles and similarity

**Key concepts:** In this section you'll learn: dot product (algebraic and geometric definitions), the angle between vectors, the orthogonality condition.

* **Step 1: Building intuition**
    * **Prompt 1.1:** "What is the dot product? Give its algebraic definition (coordinate-based) and geometric definition (using cosine of the angle). What does the dot product value tell us about the vectors (e.g., when it is positive, negative, or zero)?"
    * **Prompt 1.2:** "How can we use the dot product to compute the angle between two vectors? And how can we quickly check whether two vectors are perpendicular?"

* **Step 2: Practice and interactive tasks**
    * **Prompt 1.3:** "I have vectors u=[1, 2, 3] and v=[-2, 1, 0]. Guide me step by step through computing their dot product. Then use the result to compute the cosine of the angle between them. Finally ask me whether these vectors are perpendicular."

* **Step 3: Mini-quiz**
    * **Prompt 1.4:** "Give me two 3D vectors. Ask me to compute their dot product and to determine whether the angle between them is acute, right, or obtuse. Check my answer."

---

## Topic 2: Cross product — finding perpendiculars in 3D

**Key concepts:** In this section you'll learn: cross product (only in 3D), the right-hand rule, applications to computing the area of a parallelogram.

* **Step 1: Building intuition**
    * **Prompt 2.1:** "What is the cross product and why does it only work in 3D? What is the result of this operation? Explain the right-hand rule for determining the direction of the resulting vector."
    * **Prompt 2.2:** "How do we compute the cross product using the symbolic determinant of a 3x3 matrix? What geometric meaning does the magnitude of the resulting vector have? (hint: area)"
    * **Prompt 2.3:** "Is the cross product commutative? What happens if we swap the order of the vectors (u x v vs v x u)?"

* **Step 2: Practice and interactive tasks**
    * **Prompt 2.3:** "I have vectors u=[1, 0, 0] and v=[0, 1, 0]. Guide me through computing their cross product u x v. Check whether the result agrees with the right-hand rule. Then compute the area of the parallelogram spanned by these vectors."

* **Step 3: Mini-quiz**
    * **Prompt 2.4:** "Give me two 3D vectors. Ask me to compute their cross product. Check my result."

---

## Topic 3: Scalar triple product — volume and coplanarity

**Key concepts:** In this section you'll learn: scalar triple product, its geometric interpretation (volume of a parallelepiped), the coplanarity condition.

* **Step 1: Building intuition**
    * **Prompt 3.1:** "What is the scalar triple product of three vectors? How is it computed (as a dot of a cross, or via a determinant)?"
    * **Prompt 3.2:** "What is the geometric interpretation of the absolute value of the scalar triple product? What does it mean if the scalar triple product of three vectors is zero?"

* **Step 2: Practice and interactive tasks**
    * **Prompt 3.3:** "I have three vectors: u=[2,0,0], v=[0,3,0] and w=[0,0,4]. Guide me through computing their scalar triple product. What is the volume of the parallelepiped spanned by these vectors? Does the result match intuition?"
    * **Prompt 3.4:** "Now take vectors u=[1,2,3], v=[4,5,6] and w=[7,8,9]. Compute their scalar triple product. What does the result tell us about the geometric arrangement of these vectors?"

* **Step 3: Mini-quiz**
    * **Prompt 3.5:** "Give me three 3D vectors. Ask me to compute the volume of the parallelepiped they span and to state whether they lie in the same plane. Check my answers."

---

## Finale: Test your knowledge and prepare for the next step

**Step 1: Final test**

* **Prompt 4.1:** "Prepare a combined test on vector multiplication. I want 3 tasks: 1. Compute the angle between two vectors. 2. Find a vector perpendicular to two others. 3. Check whether three vectors are coplanar."

**Step 2: Why learn this? Applications**

* **Prompt 5.1 (Physics):** "How is the cross product used in physics? Explain using torque or the Lorentz force as an example."
* **Prompt 5.2 (Computer Graphics):** "How are dot and cross products used in 3D graphics? Briefly explain their role in computing lighting (angle of incidence) and determining surface normals."

**Step 3: What next? Preview of the next module**

* **Prompt 6.1 (Preview):** "I have mastered vector multiplication. How can I now use this knowledge to describe objects in space? Give a short, one-sentence preview of how vectors help define lines and planes."

Good luck on your journey through geometry!
