## 7. Introduction to Jupyter Notebooks

[Home](README.md)

[Back: Hugging Face Transformers](05_hugging_face_transformers.md)

In this section, we'll explore Jupyter Notebooks, an interactive environment that makes it easy to write and run Python code. We will cover the basics of installing Jupyter, creating a notebook, and using it to write and execute code.

### Before We Continue

Before starting, ensure you have Python and `pip` installed on your machine. Jupyter Notebooks can be installed using `pip`, which will also handle any dependencies.

#### Step 1: Installing Jupyter Notebooks

1. **Open your terminal** (or command prompt) and run the following command to install Jupyter:

   ```bash
   pip install notebook
   ```

   To ensure your installation:

   ```bash
   jupyter --version
   ```

#### Step 2: Starting Jupyter Notebooks

Once installed, you can start Jupyter Notebooks from your terminal.

```bash
jupyter notebook
```

This command will open the Jupyter Notebook interface in your default web browser.

#### Step 3: Creating a New Notebook

In the Jupyter interface, you can create a new notebook:

1. Navigate to the home page of Jupyter Notebooks.
2. Click on "New" in the upper right corner and select Python 3 (or another kernel if you prefer).

This action will open a new notebook in a new tab.

#### Step 4: Writing and Running Code

In your new notebook, you can write and execute Python code in cells. Each cell can contain code or Markdown.

Write some code in a cell, such as:

```python
print("Hello Jupyter!")
```

We can then run the shell using `Shift + Enter` or clicking the run button in the toolbar. Then, we can see our code as an output!

### Step 5: Adding markdown

You can also use Markdown cells to write formatted text, equations, or explanations.

1. Add a new cell by clicking on the "+" button in the toolbar and select Markdown from the dropdown menu.

2. Write some Markdown text, for example:

```markdown
# This is a Heading

Here is some **bold** text and some _italic_ text.

- Bullet list
- Another item

1. Numbered list
2. Another item
```

3. Again, we can run the cell and see our markdown content get generated!

#### Step 6: Saving and Sharing Your Work

You can save your notebook to preserve your work:

1. Save your notebook by clicking on "File" and then "Save and Checkpoint."

2. The notebook is saved as a `.ipynb` file, which you can share with others.

3. Download your notebook by selecting "File" > "Download as" and choosing a format (e.g., `.html`, `.pdf`).

## So why do people use Jupyter Notebooks?

1. **Interactive Coding Environment**

   - **Immediate Feedback:** Users can write and execute code in small chunks, or cells, and see results immediately. This interactivity is ideal for experimentation and iterative development.
   - **Code and Output Together:** Code and its output are kept together in one place, making it easier to follow the flow of computation and results.

2. **Rich Text Support**

   - **Markdown Cells:** Jupyter supports Markdown for rich text formatting, allowing users to include headings, lists, links, and other text formatting. This makes it easy to document code, describe processes, and provide explanations or analyses alongside the code.
   - **LaTeX Support:** For scientific and mathematical notation, Jupyter Notebooks support LaTeX, allowing users to include complex equations and symbols.

3. **Data Visualization**

   - **Inline Plots:** Visualizations such as charts, graphs, and plots can be displayed inline within the notebook using libraries like Matplotlib, Seaborn, and Plotly. This integration makes it straightforward to analyze and interpret data visually.
   - **Interactive Widgets:** Jupyter supports interactive widgets (via libraries like ipywidgets) that allow users to create interactive visualizations and dashboards directly within the notebook.

4. **Documentation and Reporting**

   - **Self-Contained Documents:** Jupyter Notebooks can serve as comprehensive documents that include code, results, visualizations, and narrative text all in one place. This makes them excellent for creating reports, tutorials, and presentations.
   - **Export Options:** Notebooks can be exported in various formats such as HTML, PDF, and slides, making it easy to share and present work.
