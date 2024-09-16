# Python and Machine Learning Workshop

#### Author(s): Daniel Aoulou, Zach Eanes, Kaushal Patel (Computer Science Club at Western Carolina University)

Last revised: 09-16-2024

## Description

This workshop will cover some Python libraries to get you started with machine learning and allow you to put together interesting projects. We will cover tools for data processing, visualization, machine learning, and working with machine learning models. We will also introduce you to Jupyter Notebooks, a popular tool for data analysis and machine learning.

## Table of Contents

1. [NumPy and Pandas](01_numpy_and_pandas.md)
2. [Seaborn](02_seaborn.md)
3. [Scikit-learn](03_scikit-learn.md)
4. [OpenCV](04_opencv.md)
5. [Hugging Face Transformers](05_hugging_face_transformers.md)
6. [Jupyter Notebooks](06_jupyter_notebooks.md)

## 0. Preface: Why Python?

Python is a versatile programming language that is widely used in the field of data science and machine learning. It is known for its simplicity and readability, making it an excellent choice for beginners. Python has a large number of libraries that are specifically designed for data analysis, machine learning, and scientific computing.

Python's syntax is simple and easy to learn, making it the perfect choice for programmers who want to quickly put together projects and learn new concepts. Python is also a great choice for experienced programmers who want to prototype new ideas and algorithms.

This workshop assumes that you have installed Python and PIP. If you haven't, you can download Python from the official website at [https://www.python.org/downloads/](https://www.python.org/downloads/). PIP is a package manager for Python that allows you to install libraries and tools. You can find more information about PIP at [https://pypi.org/project/pip/](https://pypi.org/project/pip/).

### Using a virtual environment

One of the cool things about Python is that you can create virtual environments to manage dependencies for different projects. This allows you to isolate the dependencies for each project and avoid conflicts between different versions of libraries. It's also great for experimenting with new tools without affecting your system-wide Python installation.

To create a virtual environment, you can use the `venv` module that comes with Python. Here's how you can create a virtual environment:

```bash
# Create a new virtual environment
python -m venv myenv ## Side note: if any of the python commands don't work, try using `python3` instead of `python`

# Activate the virtual environment
source myenv/bin/activate
```

Once you have activated the virtual environment, you can install libraries using PIP. When you're done working on your project, you can deactivate the virtual environment by running `deactivate`.

We recommend using a virtual environment for this workshop, as we will be installing different versions of certain libraries depending on the examples we cover.

[Next: NumPy and Pandas](01_numpy_and_pandas.md)
