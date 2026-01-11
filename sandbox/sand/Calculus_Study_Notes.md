# Workflow & Environment Setup for Calculus Study Notes

As future engineers, mastering the tools to document your learning process is as important as the calculation itself. We will use **Visual Studio Code (VSC)** to build a professional knowledge base for your Calculus course.

Below is the roadmap for organizing your study materials, ranging from simple daily notes to comprehensive documentation.

### Level 1: The Basics – Markdown & Project Structure

Start here to keep your focus on learning Calculus (Analysis) concepts without getting distracted by complex formatting software.

**1. File Organization**

Do not keep all your lecture notes and exercises in one massive file. It makes reviewing specific topics difficult.

* Create a dedicated **Project Folder** for your Calculus notes.
* Create separate `.md` (Markdown) files for each topic.
* Use a clear naming convention to make searching easier, for example:
    * `01_Sequences_and_Series.md`
    * `02_Differential_Calculus.md`
    * `03_Integral_Calculus.md`

**2. Writing & Mathematics**

VS Code allows you to write text and mathematical formulas simultaneously. Use the preview function (usually `Ctrl+Shift+V`) to see your notes rendered in real-time. We use LaTeX syntax for math:

* **Inline math:** Use single dollar signs for formulas within a sentence.
    Example: The derivative of sine is $\frac{d}{dx}\sin(x) = \cos(x)$.

* **Display math:** Use double dollar signs to center complex formulas on a new line.

$$
\lim_{x \to 0} \frac{\ln(1+x)}{x} = 1
$$

This ensures your study notes are accurate and easy to read during revision.

### Level 2: Portability – Converting to PDF

While `.md` files are great for editing, you need a stable format to bring to class or share with others.

**We strongly recommend using Pandoc for this task.**

* **Why Pandoc?** It is the industry standard for document conversion. Unlike simple "one-click" extensions, Pandoc gives you full control over the output and handles complex LaTeX math correctly.
* **The "Easy Way" Warning:** Simple VS Code extensions (like *Markdown PDF*) often rely on basic HTML conversion and fail to render advanced mathematical symbols correctly. Do not choose the easy path if it results in broken formulas.

**Your Goal:** A professional PDF.
You are free to use any tool, but if your chosen method fails to render math symbols (e.g., showing raw code like `$\int$` instead of the symbol), the document is unacceptable.

### Level 3: Advanced – Moving to LaTeX

If you plan to compile your notes into a larger, comprehensive document (like a full semester summary) or need more complex formatting, transitioning to full **LaTeX** is the logical next step.

* Install a TeX distribution (like TeX Live or MiKTeX).
* Install the **LaTeX Workshop** extension in VS Code.

This approach gives you better tools for managing large documents and is the preferred path when your notes outgrow the capabilities of simple Markdown.

---

### Expectations for Class Materials

When you come to class or consult on a topic, please adhere to these standards:

1.  **Format:** Have your notes ready as a **PDF**. Do not rely on opening raw `.md` files or showing screenshots.
2.  **Readability:** Ensure all mathematical symbols are properly rendered.
3.  **Organization:** Your document should have clear headings corresponding to the Calculus topics we are discussing.

---

### Your First Assignment: Setting Up Your Digital Notebook

For our next session, you will set up your environment and create your first set of notes. This assignment ensures you are comfortable with the tools we will use throughout the course.

**1. Environment Setup:**

* **Install Visual Studio Code (VSC):** If you haven't already, download and install VSC.
* **Install AI Assistant Extensions:** Enhance your workflow by installing an AI assistant plugin for VSC (e.g., GitHub Copilot, Gemini, etc.). This is highly encouraged.
* **Create a Project:**
    * Create a new project folder for your calculus notes.
    * **Initialize a Git repository** in this folder (`git init`).
    * (Optional but Recommended) Create a repository on GitHub and push your project to it. A local repository is the minimum requirement.

**2. Your First Note:**

* **Choose a Topic:** Select any topic from Mathematical Analysis. A good starting point is the **definition of the limit of a sequence**.
* **Create a Markdown File:** Inside your project, create a new `.md` file for your topic.
* **Write the Content:** Your note should include:
    * The formal definition of the chosen concept.
    * Several fully solved examples, with each step clearly explained from beginning to end.
* **Generate a PDF:** Convert your `.md` file into a clean PDF document. **We recommend setting up Pandoc** to ensure high-quality output. If you use other tools, verify that they do not break the mathematical notation.

**3. Be Ready to Present:**

* In our next class, be prepared to **share your screen**.
* You should be able to demonstrate your workflow: how you edit the Markdown file, use the VSC preview, and present the final PDF. The goal is to show that you can manage your notes effectively.