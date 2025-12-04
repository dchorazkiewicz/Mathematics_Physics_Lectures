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

### Level 2: Portability – Converting to PDF (Pandoc)

While `.md` files are great for editing, you need a stable format to bring to class or share with others.

* Install **Pandoc** on your system.
* Use a VS Code extension (like *Markdown PDF*) to convert your topic notes into **PDFs**.

This allows you to generate a clean, readable document from your notes. When asked to show your work or notes during class, you should present this generated PDF, not the raw code.

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