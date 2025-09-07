Course repository and mandatory using colab!
Course original repository: 
Link to the original repository with stored course files: https://github.com/dchorazkiewicz/Math-2024-25-Winter
We will be working using  colab Jupyters online! https://colab.research.google.com/
Your own repository: 
You will be working on your own GitHub repository! After you will have github account, you will have to fork (fancy name for copying) the original repository to your own account:
Log in on internet browser to your GitHub account.
Go in the browser to the original repository https://github.com/dchorazkiewicz/Math-2024-25-Winter
Click on the "Fork" button in the upper right corner of the page.
Wait a moment, and you will be redirected to your own repository.
Copy the link to your repository (you will need it to open Jupyter notebooks in Colab), which will be of the form: https://github.com/YOUR_NAME/Math-2024-25-Winter
Visit Colab: https://colab.research.google.com/ and click on the "GitHub" tab.
Paste the link to your repository in the search bar and press enter.
You will see the list of files in your repository, and you can open them in Colab.
You can now work on the files, make changes, and save them in your repository.
Remember to save your work in your repository, so you can show it during the classes!
Ps. advanced users might use Visual Studio and run Jupyters locally.
 
Extra notes: github, emails, other useful technologies
Create an account on GitHub (free!) -- required for participation and course completion.
We recommend using your student email address (@student.vizja.pl, etc. so you can claim free github copilot (later).
Requiring problem: while setting account check spam box on https://poczta.vizja.pl/ or https://outlook.office.com/mail/!!!).
Get access https://colab.google/ -- required for participation and course completion.
An account on Google Colab or for advanced users, a local Python environment (e.g., Anaconda) -- required for participation and course completion.
 
Technologies used in the course:
Python https://www.python.org/
Visual Studio Code https://code.visualstudio.com/
Visual Studio Code Plugins: Python, GitHub Copilot, GitHub Repositories, Remote Repositories, Jupyter, Git Graph
Markdown https://www.markdownguide.org/
Jupyter Notebook https://jupyter.org/
Google Colab https://colab.research.google.com/
GitHub: http://github.com
LaTeX: https://www.latex-project.org/get/
Geogebra https://www.geogebra.org/
Wolfram Alpha https://www.wolframalpha.com/
 
---

Approaches to Problem Sets
### Approaches to Problem Sets:
 
As you work through the problem sets, there are several methods available to you. While I expect most of you will rely on the fifth method below, that's perfectly fine—use whatever approach suits you best.
Since you've forked the original repository, use your own GitHub link to open the files in COLAB. When you're done, just save your work directly in GitHub (File > Save a copy in GitHub). Please stick to the provided Jupyter files for the exercises. With over 150 students, I won’t have time to search through hidden folders or renamed files! The Jupyter files include knowledge, examples, and implementation—just add your solutions there so everything is in one place.
 
Let’s go over the various approaches:
 
---
 
1. **Markdown Notes**  

   Write your solutions as if you were taking notes on paper but encode your steps using markdown and LaTeX. If you're unsure about the LaTeX syntax, feel free to ask ChatGPT/Gemini for assistance. Remember to ask just to write markdown notes with the $...$ and $$...$$ for math.
---
 
2. **Take a Photo of Your Handwritten Notes**  

   You can also write your notes by hand, then upload a photo and ask ChatGPT to convert them into markdown format. Make sure to ask just to write markdown notes with the $...$ and $$...$$ for math.
 
---
 
3. **Using Built-in Python Functions**  

Technology, like Python’s built-in commands, should be used for checking your understanding, not as a substitute for learning the material. While you’ll naturally want to try functions like det(A) to compute a matrix’s determinant, this alone won’t help you truly grasp the calculation process. Let me put it simply: you can’t rely solely on built-in commands and feel like you've achieved something. It's essential to understand the underlying concepts.
During the exam, handing your lecturer a page that just says "DET(A)" won’t earn you any points—a piece of paper can’t run Python!
🙂
You can use Python to verify your answers or to speed up repetitive tasks (which is why we sometimes provide large Python functions to help with row manipulation in methods like Gauss). However, coding is not the main objective here—it’s just a tool to mimic the handwritten steps and assist in checking your work.
 
---
 
4. **Coding Your Solution**  

 It is ok if you decide to code the solution from scratch. Even if your method isn't the most efficient, the key is that you’ve figured out the process and know what needs to be done. Well done! However, always aim to understand *why* the code works, and how mathematically explain it.
---
 
5. **The Recommended Method for some sceptics**  

   During class, demonstrate that you understand the steps involved by manually showing what to multiply, add, etc. Use Jupyter Notebook as a handy calculator—type the operations, and use your cursor to point out how you’re performing the calculations step by step.  
 
   For instance, write something like:
 
   ```python

   value = 1 * 3 * (-2) + ...  # showing Sarrus cross products with proper signs

   ```
 
   This helps illustrate the process. Afterward, use Python to verify your result:  

   ```python

   "your calculated value" == "python-calculated value"

   ```
 
   This will give you a True/False result. Always double-check your work and learn from any discrepancies!
 
This way you don't have to wait for teacher to tell you if you are right or wrong!
 
---
 
6. **Think Critically and Innovate**  

   Always think about how you can improve your approach, whether through optimization or clearer implementation.
 
   For example:
 
   ```python

   import sympy as sp

   B = sp.Matrix([[2, 3], [1, 4]])
 
   def determ2x2(matrix):

       return (matrix[0,0] * matrix[1,1]) - (matrix[0,1] * matrix[1,0])
 
   determ2x2(B)

   ```
 
---
 
Remark about AI 
Use GPTChat/Gemini/Claude to help you work through the problems:   
- Ask it to show you the solution step by step (write all additional info), "explain me as I'm 5 year-old", "write me in turkish"
- Request the markdown code so you can easily use it in your COLAB notebooks.  
- Have it generate Python code to implement the solution.
 
Note that there are two kinds of chats: "Githhub-programmer-codes trained chats" (like "Gemini in colab"/ Copilots good for giving you code) and the one trained on all human knowledge, like Gpt4o (smarter, seeing pictures!) Make sure you use both for right tasks.
 
 
Most importantly: **understand** the steps being done, so that you can perform them by hand during the exam. Python is there to verify the correct result and assist you in studying—especially during your time at Vizja.
 
### Final Note
 
Moving forward, all feedback will be provided ONLY during our MS Teams sessions (+ maybe use the general ms teams channel so other might help you). Please make sure to attend these classes, as we discuss solutions and review how students approached the problems. It’s crucial we make the most of our classroom time—both for your benefit and mine. You have a lot going on in your student life, so let’s maximize our class time. I have 150 students, and plenty classes and I won't be available so generously. 
 
In the some past exercises (other groups) many people only used the det() function, but the aim was to apply the Laplace method... so totally ignore everything. What next? Instead of applying the Gauss Method, I will see again only python det(F)? Please put in the effort to follow the specific methods outlined in each assignment. These techniques are crucial for your understanding, and they will help you prepare for exams, where you’ll need to solve problems manually, without a computer. 


---

About the course
The main idea of our exercise sessions is that you have to show your understanding of the material. This is your chance to demonstrate what you've learned, not a time to figure things out from scratch, be a muted passive viewer, or fake attendance.

My role is only to guide you. I'm here to point out any mistakes, highlight areas you've missed, and help you improve your approach. 
But the learning is all on you! You are responsible for mastering the material. I can only show you how to learn more effectively and efficiently.
 
To make the most of our class, it's essential that you complete the exercises in advance. Our class time will be spent discussing your work, refining it, and diving deeper into the concepts. Faking doing exercises by ignoring specific orders (like doing only det(...) command over the whole matrix while exercising concerning the Laplace method) won't be tolerated long.
 
We've given you access to Colab and made you use forked repositories to open dedicated files and save your work. Colab will be your personal playground for learning. It might feel like an extra step and complication at first, but soon you'll see it’s a real advantage, especially with the use of modern tools like AI chats. It will also help you greatly in further studying at university. There no easier way than the one we proposed.
The main goal is for you to understand the topics so well that you can solve them by hand on paper (note, that you have this type of exam with the lecturer!). This platform, along with modern tools like AI, lets you experiment, explore, and check your work in ways that help you learn faster. You can generate hundreds of pages of things, but without reading it you will be left with nothing.
 
You can and you should write math in markdown, use gptchats technology to check your results in real-time! You can use it to get explanations, and definitions tailored for you. Just use it intelligently.
 
Think of me as your coach. I'm not here to run laps around the track for you! There's no benefit for you in watching me or your classmates run. You need to do all the running. I'm just here to guide and support you, helping you get better. You are not willing to do it? You can't provide me a fork of the original repository, which costs 2 minutes? You still don't know that there are files to do, you don't know what has to be done? Then you are out of the team. I don't even understand why you came here. I won't allow you to waste the time of people who are committed to getting from the course as much as they can.

---

UPDATED Schedule
Assignments: update 27.11.2024
You come to class with these problems ALREADY SOLVED - > we discuss the problem, obstacles, improve [we won't do them from scratch!] Mathematics C1 [W.SIE.IN.1000] -> please put thumbs up, if you read.
 
20.11
27.11
04.12
Scope of the course
00_Introduction
What_is_Jupyter_Notebook.ipynb     READ IT!!! To learn more about jupyter in COLAB (how to better format things]
01_Linear_Algebra
01_Matrices
LA_Matrix_basic_operations_en.ipynb
LA_Matrix_determinants_2x2_3x3_en.ipynb
LA_Matrix_determinant_Laplace_en.ipynb
LA_Matrix_inversion_by_formula_en.ipynb 
LA_Matrix_inversion_of_a_matrix_using_gauss_en.ipynb 
LA_Matrix_triangular_en.ipynb
02_Systems_of_Linear_Equations
LA_SoLE_old_school_en.ipynb  [LAST EXAMPLE is just for you for fail, and make you want advance methods!]
LA_SoLE_Cramer_en.ipynb
LA_SoLE_Gauss_en.ipynb
LA_SoLE_inverse_matrix_en.ipynb
 03_Vectors  
 LA_Vectors_introduction_en.ipynb  
 LA_Vectors_products_en.ipynb  
 LA_Vectors_projections_en.ipynb 
02_Analytic_Geometry
05_Lines
exercise_list.md (at least START! to just face problems like lack of ipynb, lack of lecture material in Notebooks_EN, open Geogebra)
06_Conic_Curves
exercise_list.md
07_Planes_in_Space
exercise_list.md
08_Second_Order_Surfaces
exercise_list.md
LINKS:
 
Lecture notes:
 
1) https://htmlpreview.github.io/?https://github.com/dchorazkiewicz/Math-2024-25-Winter/blob/main/Lecture_Notes/Analytic_Geometry.html
 
2) https://htmlpreview.github.io/?https://github.com/dchorazkiewicz/Math-2024-25-Winter/blob/main/Lecture_Notes/Linear_Algebra.html
 
Exercise list:
 
3) https://htmlpreview.github.io/?https://github.com/dchorazkiewicz/Math-2024-25-Winter/blob/main/Lecture_Notes/Exercises.html
 
4) Example solutions: https://github.com/dchorazkiewicz/Math-2024-25-Winter/blob/main/Lecture_Notes/Example_solutions.md (study the code, copy paste, modify it, use chatgpt to change this into your example, ask gemini for latex or markdown notes
 
remember about $ $ and $$ $$ for math and not \( \) o \[ \]
 
 
----
PAST: You are expected to COMPLETE the exercises ON YOUR OWN prior to the exercises classes (with minor problems). You have to create your forked repository (from the original archive: https://github.com/dchorazkiewicz/Math-2024-25-Winter)  and put there your solution including your solutions at the end of the each file. Don't wait for lecture! Notebook_EN files have the notes showing you the material, also you have implementation examples (use them or propose other way... no problem, just show your understanding!) 

---

Fake presence, lack of repositories, lack of work in the repositories = failing the course
Mathematics C1 [W.SIE.IN.1000] 
 
This screenshot is just small sample what can be seen by me.  It seems that we have a group of committed students, which basically covers people who delivered the forked repositories: yesterday and today I was telling that is mandatory, and only 13 people did it.    I understand that 21 other people accept grade 2.0 (failing the course) and I can delete you from the MS Teams?  Funny enough 16 people tried to mark their presence during classes. Next week I want hear solutions from other people! Share the screen, etc.
 
I will be monitoring your activity (from time to time in your repositories) and I require everybody to contribute to showing solutions. 
 
---

Update of Lecture Notes and Exercises
Update 1.12.2024
Lecture notes (written by D. Chorążkiewicz and me):
Linear Algebra https://htmlpreview.github.io/?https://github.com/dchorazkiewicz/Math-2024-25-Winter/blob/main/Lecture_Notes/Linear_Algebra.html
Analytic Geometry https://htmlpreview.github.io/?https://github.com/dchorazkiewicz/Math-2024-25-Winter/blob/main/Lecture_Notes/Analytic_Geometry.html
Calculus https://htmlpreview.github.io/?https://github.com/dchorazkiewicz/Math-2024-25-Winter/blob/main/Lecture_Notes/Calculus.html
List of Exercises (it contains the Calculus part now!)
All course exercises https://github.com/dchorazkiewicz/Math-2024-25-Winter/blob/main/Lecture_Notes/Exercises.md 
Syllabus content
(for you to generate the notes in Colab jupyters)
Linear Algebra
Matrices
Introduction to matrices and arithmetic operations on matrices, types of matrices, determinants (Laplace expansion method, Gauss-Jordan method), and their properties, algebraic complements, minors, cofactors, rank. Finding the inverse of a matrix by various methods. 6 10
Linear Equations
Systems of linear equations and methods for solving them, Cramer's Rule, matrix method for solving systems of linear equations, Gaussian elimination method. 4 5
Analytic Geometry
Vector Algebra
Coordinate systems in the plane and space, vectors, linear operations on vectors, basis, finding the coordinates of a vector in a new basis, projection of a vector onto an axis, properties and applications of scalar product, vector product, and mixed product.
Curves and surfaces
Utilizing algebraic language to describe curves and surfaces in Cartesian spaces, including the parametrization of curves and surfaces. Implicit and explicit equations of curves and surfaces.
Additionally, matrix calculus and systems of linear equations are reinterpreted geometrically, providing deeper insights into the structure of linear transformations, projections, and the geometric relationships between vectors, planes, and spaces within the framework of analytic geometry.
Calculus
Differential Calculus
Sequences, real functions, and limits as foundational concepts for calculus. Exploration of derivatives, including their definition, rules, and higher-order derivatives. Applications of derivatives in analyzing the behavior of functions, including finding extrema, inflection points, and solving optimization problems. Geometric interpretations such as tangents to curves and rates of change. Introduction to Taylor series, providing approximations of functions.
Integrals
Introduction to definite and indefinite integrals, fundamental theorem of calculus, and techniques of integration such as substitution and integration by parts. Applications of integrals in calculating areas, volumes of solids of revolution, arc lengths, and solving real-world problems such as accumulation functions and probability distributions. Geometric interpretation of integration as the accumulation of quantities under a curve. 3 6
Differential Equations
Introduction to ordinary differential equations (ODEs). Applications in modeling physical systems, population dynamics, and growth/decay processes, emphasizing the role of differential equations in connecting calculus to real-world phenomena.

---
 
List of exercises: https://github.com/dchorazkiewicz/Math-2024-25-Winter/blob/main/Lecture_Notes/Exercises.md

---

Trial Test, Test-1, Test-2
This is to inform you about two tests ahead of you. Before that, I will now share a Trial Test so you can try the technology. 
 
Trial Test  conducted online via MS Forms. 
When:  I will open it tomorrow on 11:00 AM. The deadline for Trial Test is Tuesday 20:00.
 
Format of all Tests: Online via MS Forms (it will show up in the MS Teams Assignments)
 
 Test-1  conducted online via MS Forms. 
When: Wednesday, December 11 (start 18:00 – Friday, December 13 (end 22:00), 2024
Material Covered: Matrices + Linear Equations (sections: 1-10 https://github.com/dchorazkiewicz/Math-2024-25-Winter/blob/main/Lecture_Notes/Exercises.md) 

Test-2 conducted online via MS Forms
When: Wednesday, December 18 (start 17:30) – Thursday, December 19 (end 20:00), 2024
Material Covered: Vectors + Analytic Geometry (sections: 11-17 https://github.com/dchorazkiewicz/Math-2024-25-Winter/blob/main/Lecture_Notes/Exercises.md) 
Please prepare well and make sure you submit within the time window.
 
Mathematics C1 [W.SIE.IN.1000]
 
---

Good formatting example:

Minimal formating. Bringiging useful formula, solving a problem, finding answer + SUPPORTING visualization link to  Geogebra.
 
https://www.geogebra.org/graphing/xdsa4uyv <- see this


# Task 5: Line Through $A(1,2)$ Parallel to $\vec{v} = [2,3]$

1. **Determine the Slope**:
   The direction vector $\vec{v} = [2, 3]$ gives:
   $$
   m = \frac{3}{2}
   $$

2. **Write the Equation**:
   Using the point-slope form:
   $$
   y - y_1 = m(x - x_1)
   $$
   Substitute $m = \frac{3}{2}$, $x_1 = 1$, and $y_1 = 2$:
   $$
   y - 2 = \frac{3}{2}(x - 1)
   $$

3. **Simplify**:
   Expand and simplify:
   $$
   y = \frac{3}{2}x + \frac{1}{2}
   $$

**Final Answer**: The equation of the line is $y = \frac{3}{2}x + \frac{1}{2}$.

**Visualisation**: <a href="https://www.geogebra.org/graphing/xdsa4uyv" rel="noreferrer noopener" title="https://www.geogebra.org/graphing/xdsa4uyv" target="_blank">https://www.geogebra.org/graphing/xdsa4uyv</a>

---

Consultations
Three consultations in the semester:
12.12.2024 (tomorrow, 1h) = 10:15-11:15 Link to Teams If you don't need anything, don't come.
07.01.2025 (Tuesday, 1h) = 11:15-12:15 Link to Teams If you don't need anything, don't come.
03.02.2024 (Monday, 1h) = 09:00-10:00 Link to Teams will be updated
Join conversation


---

Example ipynb
Analytic Geometry
We now have two weeks to cover the entirety of Analytical Geometry and the remaining topics from Vectors.
 
Analytical Geometry is a little bit different:
you have to create a jupyter files in the corresponding directories! (this time inside there are just markdown list of exercises)
you have to deal with the fact that we haven't provided you notes and implementations (do the notes for yourself (!) - we showed you how to do it!). The list of topics from syllabus is here Mathematics - Syllabus.xlsx which can help you in preparing topics.
you don't have to make supporting notes but you have to do exercises in some way 
you need to start using Geogebra (this the best thing to help you understand analytical geometry!) https://www.geogebra.org/calculator (description how to use it is notes I talked about in the post above. Use https://github.com/dchorazkiewicz/Math-2024-25-Winter/blob/main/Lecture_Notes/Analytic_Geometry.html you have to put in https://htmlpreview.github.io/?

In case of problem with creating a file go to Github and UPLOAD the example file to proper directories and start working on solutions.
 
Let me also remind you that starting this week, I’ll be assigning a "2.0" as a final grade for those not working in Colab, not attending, or faking presence. We’re entering very complex topics, and we really don't have time for this situations.
03_Vectors
LA_Vectors_introduction_en.ipynb [do exercises to present it in class 14/15 Nov]
LA_Vectors_products_en.ipynb [do exercises to present it in class 14/15 Nov]
LA_Vectors_projections_en.ipynb [do exercises to present it in class 21/22 Nov]
02_Analytic_Geometry
05_Lines
exercise_list.md [do exercises to present it in class 21/22 Nov]
06_Conic_Curves
exercise_list.md [do exercises to present it in class 28/29 Nov]
07_Planes_in_Space
exercise_list.md [do exercises to present it in class 28/29 Nov]
08_Second_Order_Surfaces
exercise_list.md [do exercises to present it in class 28/29 Nov]
start-example.ipynb
 

 ---

 January Repositories
Dear Students,  
 
This is a reminder that on 2nd January 2024, I will be (fast and roughly) reviewing your repositories. Please ensure that all exercises are completed and uploaded according to the material we have covered in class. Failure to complete the required work will result in an automatic failing of the course. 
 
I can only fast review it, so I don't have to explain to you how important that you don't have too much of irregularities (mess, joint and unnamed files). As far I'm concerned: I don't see files where they are expected = no files , and no files = no passing. You know exactly what it means the have good notes, don't ask me about it, just make sure they are good enough.
 
Inside your repo//Math-2024-25-Winter/Notebooks_EN/ I expect to find folders(directories)
 
01_Linear Algebra

   - Ensure all exercises in the given ipynb files (openable by Colab) are completed and organized in subfolders like it was originally intended.
 
02_Analytic Geometry

   -  Create/Upload on GitHub '*.ipynb` files and make the exercises in them. Here I allow for files to be directly inside 02_Analytic_Geometry (but it would be nice to see them in subfolders). We mentioned the fact of colab not seeing *.md files many times in classes (read the General Thread!) Asking about it proves that you are not attending to classes in a sufficient way to pass.
 
Please take this deadline seriously and ensure your work is well-organized and up-to-date. Majority, who worked basically have nothing to do, whereas the rest... will understand better what it means to work systematically 
 
Mathematics C1 [W.SIE.IN.1000]
 
You have chaos in your repo? Clean it. Don't ask me if I will accept your mess.  Nobody wants anybody's mess. Edit names directly in Github. Create folders. Edit paths of files. Use my screenshot/ask chatgpt/youtube about how to change files names, create subdirectories, etc.
 
---

Missing repositories.
I was screening your repos... it seems that plenty of people want to fail. 
 
I said...  ACTIVITY and PRESENTING SOLUTIONS providing discussion, explanation in the CLASS + 25th sets exercises of perfect notes must be done before I will grant you final grade. If I won't get it both from you = you will get 2.0. Your microphone doesn't work? Your screen doesn't work? You have to go somewhere? 2.0.
 
Your choice and ony you to blame.
 
Tuesday = we have 3x45, time window 8:00-10:00 (there is no lecture in this spot, instead classes).
Wednesday = we have 4x45, time window 14:30-17:00.
 
Mathematics C1 [W.SIE.IN.1000]


---

More explaining
You are in the C1 exercise group and the W1 lecture group.
 
Requirements to Pass C1:
To pass C1, you must complete all 25 exercise sets (not just the 25th set!)  + I need to HEAR YOU PRESENTING MATERIAL/SHOWING YOUR UNDERSTANDING.
 
You have seen many students fulfilling these requirements—there are no exceptions! . You want to say that you didn't know that, good 2.0 for not following the course.
 
If you have completed the repository but are not willing to present your understanding in the class, your grade will be 2.0.

If you have not completed the repository, your grade will 2.0.
 
From now one I AM NOT AVAILABLE BESIDES CLASSES. I WON'T BE EXPLAINING ANYTHING BEYOND CLASSES
 I WILL BE ONLY IN THE CLASSES and explaining things in the classes.
 
Classes:
Tuesday = we have 3x45, time window 8:00-10:00 (there is no lecture in this spot, instead classes).
Wednesday = we have 4x45, time window 14:30-17:00.
 
Preliminary Grades & Deadline:
I have entered preliminary grades in the Verbis system. However, you still have 7 hours of classes time left to fulfill the requirements. It’s your choice. It is not my problem that I will fail you even with 75% of done things. It is your problem that you haven't delivered everything. Don't exaggerate about how much work it was to have the chat generate the notes for you. You come to the airport without passport and 2 hours late and blame airport?
If you meet both requirements within this time, you will pass.
If not, the preliminary grade will stand as it adequately showing that you didn't meet requirements.
Not satisfied with value your grade? You still have an opportunity—during class! Convince me WITH THE KNOWLEDGE and not empty promises or some excuses.
 
Next Steps - W1 Lecture Exam:
Once you pass C1, you will need to pass the W1 lecture exam.

Details will be announced later, but the exam will take place on February 10th.
Only students with a positive C1 grade will be allow to take it. 
 
That is standard university practice (classes with exercises and classes with lecturers have separate grades). Sometime classes have the character of kolokwium/colloquium (fancy name), but it means that there is lecture that not ends with the grade and only laboratories assigned to the lecture are grade. This course is having W1 grade and C1 grade separately.
 
Mathematics C1 [W.SIE.IN.1000]
 

 | Porównanie prognoz vs. wyników (Wrocław, 10.08) | Rzeczywiste podium                                          | Moje typy TOP3 (przed)                                        |                         Trafienia | Uwagi (tempo/tor/klucz)                                                                    |
| ----------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------- | --------------------------------: | ------------------------------------------------------------------------------------------ |
| Gonitwa 1 (2400 m, kłusaki)                     | 1) Love You Gagou • 2) Lady Mary • 3) Misclick              | 1) Lady Mary • 2) Libero OV • 3) Love You Gagou               |               2/3 (bez zwycięzcy) | Start wolny bez bata; galopy Libero/My Boy Juke, wyścig „na chodzie”, faworyt doścignięty. |
| Gonitwa 2 (1400 m, 2-l.)                        | 1) Power Bay • 2) Rusałka • 3) Frezja                       | 1) Power Bay • 2) Rusałka • 3) Zorban                         |                2/3 (ze zwycięzcą) | Debiuty: papier zagrał; Frezja lepsza niż wskazywały wcześniejsze założenia.               |
| Gonitwa 3 (1600 m, araby)                       | 1) Esseda • 2) Perana • 3) Camelia SKK                      | 1) Esseda • 2) Złocica • 3) Kemar                             |                1/3 (ze zwycięzcą) | Mocny finisz Essedy; Perana/Camelia zrobiły duży skok formy.                               |
| Gonitwa 4 (1600 m, araby)                       | 1) Wessana • 2) Shami Al Khal. • 3) Adon Al Khal.           | 1) Madja de Faust • 2) Adon • 3) Kind of Magic                |               1/3 (bez zwycięzcy) | Debiut Wessany „łatwo” – duże zaskoczenie; Madja zawiodła.                                 |
| Gonitwa 5 (1907 m, IV gr. A)                    | 1) Sunny Boo • 2) Gold of Treville • 3) Szakal              | 1) Sunny Boo • 2) Persja • 3) Mr Horn                         |                1/3 (ze zwycięzcą) | Sunny Boo kontrola; G.o.T. i Szakal progres; Mr Horn rozczarował z wagi.                   |
| Gonitwa 6 (1907 m, IV gr. B)                    | 1) High Hope • 2) Umań • 3) Królowa Kinga                   | 1) Umań • 2) Królowa Kinga • 3) Grey Eminence                 |               2/3 (bez zwycięzcy) | #1 zagrał tor/tempo; Umań dobry, Grey pod formą.                                           |
| Gonitwa 7 (1907 m, araby)                       | 1) Pasadera • 2) Pagonia • 3) Wasalka                       | 1) Wasalka • 2) Livorna • 3) Pagonia                          |               2/3 (bez zwycięzcy) | Pasadera „łatwo” – step forward; długi finisz.                                             |
| Gonitwa 8 (2200 m, HCP III)                     | 1) American Bassett • 2) Son of Jameson • 3) Lady Agnieszka | 1) Son of Jameson • 2) American Bassett • 3) Invincible Fairy |               2/3 (bez zwycięzcy) | Top weight nie przeszkodził; Lady Agnieszka solidna, IF nie wytrzymała końcówki.           |
| Gonitwa 9 (2400–2460 m, kłusaki)                | 1) Hugo Des Bois • 2) Factoriel • 3) Habanera               | 1) Factoriel • 2) Keyval • 3) Kaline Restelan                 |               1/3 (bez zwycięzcy) | Hugo lepiej zagrał metraż i rozkład sił; Keyval/Kaline zawiodły.                           |
| **Suma dnia**                                   | —                                                           | —                                                             | **14/27 podium (3/9 zwycięzców)** | Tor 3.1 neutralny; lekka przewaga koni „idących w tempie” i tych z dobrym prowadzeniem.    |
