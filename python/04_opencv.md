## 4. OpenCV

[Home](README.md)

[Back: Scikit-learn](03_scikit-learn.md)

In this section, we will learn about OpenCV, a powerful Python library for computer vision and image processing. We will use OpenCV to load, manipulate, and analyze images.

OpenCV is great for a wide range of tasks, including image loading, displaying, processing, and computer vision applications. An app that recognizes faces in images, a system that detects objects in videos, and a tool that measures distances in images are just a few examples of what you can build with OpenCV.

### Installing OpenCV

1. **Open your terminal** (or command prompt) and run the following command to install OpenCV:

   ```bash
   pip install opencv-python
   ```

2. **Verify the installation** by opening a Python interpreter and running:

   ```python
   import cv2
   print(cv2.__version__)
   ```

   If there are no errors and the version is printed, OpenCV is installed correctly.

### Loading and Displaying an Image

OpenCV is commonly used for image loading, displaying, and processing. Let’s start by loading and displaying an image.

1. **Download a sample image**:

   Download an image that you want to work with (for example, a `.jpg` or `.png` file). Save it in your working directory.

2. **Loading and displaying the image**:

   ```python
   import cv2

   # Load the image from file
   img = cv2.imread("sample_image.jpg")

   # Display the image in a window
   cv2.imshow("Sample Image", img)

   # Wait for a key press and close the window
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   ```

   - **`cv2.imread()`**: Loads the image from the specified file.
   - **`cv2.imshow()`**: Displays the image in a window.
   - **`cv2.waitKey(0)`**: Waits for a key press before closing the window.
   - **`cv2.destroyAllWindows()`**: Closes all OpenCV windows.

### Basic Image Manipulation

Now that we’ve loaded and displayed an image, let’s perform some basic image manipulations, such as resizing, converting to grayscale, and drawing shapes.

1. **Resizing the image**:

   ```python
   # Resize the image to half its original dimensions
   resized_img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

   # Display the resized image
   cv2.imshow("Resized Image", resized_img)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   ```

2. **Converting the image to grayscale**:

   ```python
   # Convert the image to grayscale
   gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

   # Display the grayscale image
   cv2.imshow("Grayscale Image", gray_img)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   ```

3. **Drawing shapes on the image**:

   ```python
   # Draw a red rectangle on the image
   img_with_rectangle = img.copy()
   cv2.rectangle(img_with_rectangle, (50, 50), (200, 200), (0, 0, 255), 3)

   # Display the image with the rectangle
   cv2.imshow("Image with Rectangle", img_with_rectangle)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   ```

   - **`cv2.rectangle()`**: Draws a rectangle on the image. The arguments specify the top-left and bottom-right corners of the rectangle, the color (in BGR format), and the thickness.

### Basic Image Processing Techniques

OpenCV provides many functions for image processing. Let's explore two basic operations: blurring an image and detecting edges.

1. **Blurring the image**:

   Blurring is a common image processing operation used to reduce noise or smooth the image.

   ```python
   # Apply a Gaussian blur to the image
   blurred_img = cv2.GaussianBlur(img, (15, 15), 0)

   # Display the blurred image
   cv2.imshow("Blurred Image", blurred_img)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   ```

2. **Detecting edges with the Canny algorithm**:

   Edge detection is a key step in many computer vision tasks, helping identify object boundaries.

   ```python
   # Apply the Canny edge detection algorithm
   edges = cv2.Canny(img, 100, 200)

   # Display the edges
   cv2.imshow("Edges", edges)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   ```

   - **`cv2.Canny()`**: Detects edges in the image. The two arguments (100, 200) are thresholds for edge detection.

### Image Thresholding

Thresholding is an important technique in image processing where we convert a grayscale image into a binary image by choosing a threshold value. Pixels below the threshold are turned black, and pixels above are turned white.

1. **Convert the image to grayscale and apply a binary threshold**:

   ```python
   # Convert the image to grayscale
   gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

   # Apply binary thresholding
   _, thresholded_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)

   # Display the thresholded image
   cv2.imshow("Thresholded Image", thresholded_img)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   ```

2. **Try different threshold values** to see how it affects the image.

### Drawing and Writing on Images

In this exercise, you will draw shapes and text on an image using OpenCV’s drawing functions.

1. **Draw a circle and add text to the image**:

   ```python
   # Copy the image to avoid modifying the original
   img_copy = img.copy()

   # Draw a blue circle on the image
   cv2.circle(img_copy, (150, 150), 50, (255, 0, 0), -1)

   # Add text to the image
   cv2.putText(img_copy, 'OpenCV Workshop', (10, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

   # Display the image with the circle and text
   cv2.imshow("Image with Circle and Text", img_copy)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   ```

2. **Experiment with different shapes and text styles** to enhance your image.

---

Congrats! You've just learned how to use OpenCV for image loading, manipulation, and processing. OpenCV is a powerful library with many more features for computer vision and image processing tasks. By using features such as edge detection, thresholding, and drawing functions, you can perform a wide range of image processing tasks. Combining these techniques with machine learning models can lead to powerful computer vision applications.

Next, we will explore Hugging Face Transformers, a popular library for natural language processing tasks.

[Next: Hugging Face Transformers](05_hugging_face_transformers.md)
