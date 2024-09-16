## 7. Introduction to Jupyter Notebooks

[Home](README.md)

[Back: Hugging Face Transformers](05_hugging_face_transformers.md)

In this section, we'll explore Jupyter Notebooks, an interactive environment that makes it easy to write and run Python code. We will cover the basics of installing Jupyter, creating a notebook, and using it to write and execute code.

Jupyter Notebooks are useful for when you've completed a project, done some data or visualization work, and want to share your results with others. They are also great for teaching and learning, as they allow you to combine code, text, and visualizations in one document.

### Installing Jupyter Notebooks

1. **Open your terminal** (or command prompt) and run the following command to install Jupyter:

   ```bash
   pip install notebook
   ```

   To ensure your installation:

   ```bash
   jupyter --version
   ```

### Starting Jupyter Notebooks

Once installed, you can start Jupyter Notebooks from your terminal.

```bash
jupyter notebook
```

This command will open the Jupyter Notebook interface in your default web browser.

### Creating a New Notebook

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

1. Save your notebook by clicking on "File" and then "Save Notebook" or "Save Notebook As" to save a copy.

2. The notebook is saved as a `.ipynb` file, which you can share with others.

3. Export your notebook by selecting "File" > "Save and Export Notebook As" and choosing a format (e.g., `.html`, `.pdf`).

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

### Exercise 6.1

Let's try using OpenCV to load and display an image in a Jupyter Notebook. Follow these steps:

1. **Ensure OpenCV and Matplotlib are Installed**:
   If you haven’t already installed OpenCV and Matplotlib, open a new terminal window and run the following command:

```bash
pip install opencv-python matplotlib
```

2. **Download or Use a Sample Image**:
   You can download an image from the internet or use a local image. Place the image in the same directory as your Jupyter Notebook, or use an image URL for loading. You can also use the image in this repository.

3. **Write and Run the Following Code** in a Jupyter Notebook:

```python
# Import necessary libraries
import cv2
from matplotlib import pyplot as plt

# Load an image using OpenCV (ensure the path is correct for your local image)
# If using a URL, you can load the image using requests and BytesIO
image = cv2.imread('sample_image.jpg')

# Check if the image was loaded correctly
if image is None:
      print("Image not found. Please check the file path or URL.")
else:
      # Convert the image from BGR (OpenCV default) to RGB for displaying correctly
      image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

      # Display the image using matplotlib
      plt.imshow(image_rgb)
      plt.title('Displayed Image with OpenCV in Jupyter Notebook')
      plt.axis('off')  # Hide the axis for better display
      plt.show()
```

#### Explanation:

- **`cv2.imread('sample_image.jpg')`**: Loads the image from the specified file path.
- **`cv2.cvtColor(image, cv2.COLOR_BGR2RGB)`**: Converts the image from BGR (used by OpenCV) to RGB (used by most other tools like Matplotlib).
- **`plt.imshow(image_rgb)`**: Displays the image in the Jupyter Notebook using Matplotlib.

#### Notes:

- Make sure that the image file (`sample_image.jpg`) exists in the working directory, or adjust the file path to the correct location of your image.
- If you encounter issues loading the image, ensure the file path is correct or try loading an image from a URL.

### Exercise 6.2

Let's do some image processing on the picture we just loaded and extract some data from it.

**Perform Basic Image Processing**:
We'll apply basic image processing techniques such as converting the image to grayscale, applying edge detection, and plotting histograms of color channels.

**Write and Run the Following Code** in Jupyter Notebook:

```python
# Import necessary libraries
import cv2
from matplotlib import pyplot as plt

# Load the image using OpenCV (ensure the path is correct)
image = cv2.imread('sample_image.jpg')

if image is None:
    print("Image not found. Please check the file path or URL.")
else:
    # Convert the image from BGR (OpenCV default) to RGB for correct display
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Convert the image to grayscale for further processing
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply edge detection using Canny algorithm
    edges = cv2.Canny(image_gray, 100, 200)

    # Display original, grayscale, and edge-detected images
    plt.figure(figsize=(12, 6))

    # Original image
    plt.subplot(1, 3, 1)
    plt.imshow(image_rgb)
    plt.title('Original Image')
    plt.axis('off')

    # Grayscale image
    plt.subplot(1, 3, 2)
    plt.imshow(image_gray, cmap='gray')
    plt.title('Grayscale Image')
    plt.axis('off')

    # Edge-detected image
    plt.subplot(1, 3, 3)
    plt.imshow(edges, cmap='gray')
    plt.title('Edge Detection (Canny)')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

    # Plotting color histograms for RGB channels
    # Split the image into R, G, B channels
    channels = cv2.split(image_rgb)
    colors = ("r", "g", "b")
    plt.figure()
    plt.title("Color Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")

    for channel, color in zip(channels, colors):
        hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])

    plt.show()
```

#### Explanation:

1. **Grayscale Conversion**:

   - We convert the original image to grayscale using `cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)`, which simplifies the image by reducing the color information to a single intensity channel.

2. **Edge Detection (Canny)**:

   - The **Canny edge detector** is used to find edges in the grayscale image with `cv2.Canny(image_gray, 100, 200)`. This is helpful for detecting outlines of objects in the image.

3. **Displaying Multiple Images**:

   - The original, grayscale, and edge-detected images are displayed side by side using Matplotlib's `subplot()` functionality for comparison.

4. **Color Histogram**:
   - We plot histograms for the Red, Green, and Blue channels of the image using `cv2.calcHist()`. This gives insights into the distribution of color intensities in the image, which can be useful for tasks like image classification, analysis, or color-based segmentation.

---

Congratulations! You learned how to use Jupyter Notebooks to write and execute Python code, create visualizations, and document your work. Jupyter Notebooks are a powerful tool for data analysis, machine learning, and sharing your projects with others.

[End](end.md)
