## 1.1 NumPy

[Home](README.md)

### What is NumPy?

NumPy is a fundamental package in Python and is widely used across various fields, including data science and software engineering in order to perform many kinds of scientific computing. This library provides a basis for many of these operations, such as multidimensional arrays, matrices, and many basic mathematical operations to save the programmer time from computing them instead. You can learn more about NumPy [here.](https://numpy.org/)

This part of the workshop will cover the basics of NumPy, including how to install it, create arrays, and perform common operations.

### Following along

You can follow along with this workshop by creating a new Python file and typing the code snippets provided, then running `python3 filename.py` in your terminal. You could also run it directly from the terminal by typing `python3` to enter the Python interpreter, and then typing the code line by line. We recommend this method to get started quickly!

You can also use an online Python interpreter like [Repl.it](https://repl.it/) to run the code.

### Let's Get Started!

First, we need to install the library using pip (or pip3). You can just enter the following:

`pip install numpy` or `pip3 install numpy`

Then, after we've installed the library, just in any python file, we can say:

`import numpy as np`

**Note:** It's extremely common practice to reference to NumPy as np, and we recommend it as well.

### Common uses and examples of NumPy

Here are some of its most common uses:

1. **Array Operations**:

   - NumPy provides a powerful array object, `ndarray`, that supports a wide range of mathematical operations, including element-wise operations, matrix manipulations, and advanced indexing.
   - Example:

   ```python
   # Create a NumPy array
   a = np.array([1, 2, 3, 4])

   # Element-wise operations
   b = a * 2  # Multiply each element by 2
   print(b)  # Output: [2 4 6 8]

   # Matrix manipulation
   A = np.array([[1, 2], [3, 4]])
   B = np.array([[5, 6], [7, 8]])
   C = np.dot(A, B)  # Matrix multiplication
   print(C)  # Output: [[19 22]
           #          [43 50]]
   ```

2. **Mathematical Functions**:

   - It offers a variety of mathematical functions for operations like linear algebra, statistical analysis, and more. This includes functions for trigonometry, logarithms, and exponentials, among others.

   - Example:

   ```python
   # Trigonometric functions
   angles = np.array([0, np.pi/2, np.pi])
   sines = np.sin(angles)
   print(sines)  # Output: [0. 1. 0.]

   # Logarithms
   values = np.array([1, 10, 100])
   logs = np.log10(values)
   print(logs)  # Output: [0. 1. 2.]
   ```

3. **Data Analysis**:

   - NumPy is often used as the foundation for other data analysis libraries like Pandas. It handles numerical data efficiently and integrates well with other data manipulation tools.

   - Example:

   ```python
   # Create a NumPy array
   data = np.array([1, 2, 3, 4, 5])

   import pandas as pd ## We'll cover this in the next section!

   # Convert to a Pandas DataFrame
   df = pd.DataFrame(data, columns=['Values'])
   print(df)
   ```

4. **Scientific Computing**:

   - In scientific computing, NumPy is used for tasks such as simulations, numerical solutions of differential equations, and other mathematical modeling.

   - Example:

   ```python
   # Generate data for a simple simulation
   x = np.linspace(0, 10, 100)
   y = np.sin(x)
   ```

5. **Signal and Image Processing**:

   - NumPy is employed in signal processing and image manipulation, where array-based operations are crucial for filtering, transformation, and analysis. We'll see this an application of this in a later section.

6. **Statistical Analysis**:

   - It provides functions for computing descriptive statistics like mean, median, variance, and standard deviation, which are useful in data analysis and scientific research.

   - Example:

   ```python
   # Generate some data
   data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

   # Compute statistics
   mean = np.mean(data)
   median = np.median(data)
   variance = np.var(data)
   std_dev = np.std(data)

   print(f'Mean: {mean}')  # Output: Mean: 5.5
   print(f'Median: {median}')  # Output: Median: 5.5
   print(f'Variance: {variance}')  # Output: Variance: 8.25
   print(f'Standard Deviation: {std_dev}')  # Output: Standard Deviation: 2.8722813232690143
   ```

7. **Integration with Other Libraries**:

   - NumPy arrays are often used as inputs or outputs for other scientific computing libraries, such as SciPy, TensorFlow, and PyTorch.

   - In essence, NumPy can provide a crucial baseline for better use of other libraries. The operations provided in NumPy are essential for many other mathematical based libraries, and is apart of the reason NumPy is considered the most used python library.

8. **Performance Optimization**:

   - By using NumPy, you can perform operations much faster compared to using native Python lists, due to its underlying implementation in C and the use of efficient array operations.

   - Example:

   ```python
   # Create a large NumPy array
   size = 10**6
   array = np.random.random(size)
   print(array) #look at how big this is!

   import time

   # Time a NumPy operation
   start_time = time.time()
   result = np.sqrt(array)
   end_time = time.time()

   print(f'Time taken: {end_time - start_time} seconds')
   ```

NumPy is a powerful library that provides a wide range of functions for numerical computing. It is a fundamental tool for data analysis, scientific computing, and machine learning in Python.

**Side note:** Throughout this workshop we imported various libraries as we needed them for the examples. Do not do this in your code! It is best practice to import all libraries at the beginning of your script.

---

## 1.2. Pandas

### What is Pandas?

Pandas are mammals of the family Ursidae, usually characterised by their white coat with black patches around the eyes, ears, legs and shoulders-- oh, sorry. Wrong pandas...

Pandas is a widely used, fast, flexible, and open source data analysis and manipulation tool built in Python. It can be used widely for data wrangling and handling datasets, and is commonly paired with NumPy (see we told you) in order to create the most efficient dataframe library in Python. You can learn more about Pandas [here.](https://pandas.pydata.org/)

This part of the workshop will cover the basics of Pandas, including how to install it, load datasets, and perform common operations.

### Let's Get Started

Very similar to NumPy, we can simply use pip or pip3 to install:

`pip install pandas` or `pip3 install pandas`

Now that we've installed the library, we just need to say in a python file:

`import pandas as pd`

**Note:** Once again, pd is an extremely common naming convention, and we recommend using it.

For this part of the workshop, we'll also need to install the `seaborn` library, which is a data visualization library based on Matplotlib. You can install it using:

`pip install seaborn` or `pip3 install seaborn`

Then you can import it using:

`import seaborn as sns`

Pandas is particularly useful for working with tabular data. We’ll use a simple dataset to explore Pandas’ functionality. For this example, we’ll use the **'tips'** dataset, which contains information about restaurant tips.

### Loading a dataset into a DataFrame

Pandas can load datasets from various sources such as CSV files, Excel files, or directly from URLs. For simplicity, let’s use the `seaborn` library to load the **'tips'** dataset.

```python
import seaborn as sns
import pandas as pd

# Load the 'tips' dataset using Seaborn and convert it to a Pandas DataFrame
tips = sns.load_dataset('tips')

# Display the first few rows of the dataset
print(tips.head())
```

We just created a DataFrame called `tips` from the 'tips' dataset. The `head()` function displays the first few rows of the DataFrame.

- **DataFrame**: A two-dimensional labeled data structure with columns of potentially different types. It is similar to a spreadsheet or SQL table, but with more powerful features. Most of the data you'll work with using Pandas will be in the form of DataFrames.

What does the output look like?

You can inspect the structure of the DataFrame by checking its shape and columns:

```python
# Display the shape of the DataFrame
print(tips.shape) # The .shape attribute returns a tuple representing the dimensions of the DataFrame, giving you the number of rows and columns.

# Display the column names
print(tips.columns)
```

### Selecting Data from a DataFrame

Pandas makes it easy to select specific columns or rows of a DataFrame.

1. **Selecting a single column**:

   ```python
   # Select the 'total_bill' column
   total_bill = tips['total_bill']
   print(total_bill.head())
   ```

2. **Selecting multiple columns**:

   ```python
   # Select 'total_bill' and 'tip' columns
   bills_and_tips = tips[['total_bill', 'tip']]
   print(bills_and_tips.head())
   ```

3. **Selecting rows based on a condition**:

   Suppose you want to select all rows where the customer is a smoker:

   ```python
   smokers = tips[tips['smoker'] == 'Yes']
   print(smokers.head())
   ```

### Basic Data Analysis with Pandas

Now that you’ve learned how to select data, let’s perform some basic analysis to understand the dataset better.

1. **Descriptive statistics**:

   Pandas can generate summary statistics for each numerical column in your DataFrame:

   ```python
   # Generate summary statistics for numerical columns
   print(tips.describe())
   ```

   This will show important metrics such as the mean, standard deviation, and quartiles.

2. **Calculating the average tip**:

   You can use the `mean()` function to calculate the average tip amount:

   ```python
   # Calculate the average tip
   avg_tip = tips['tip'].mean()
   print(f"Average Tip: {avg_tip}")
   ```

3. **Grouping data by a category**:

   Let’s group the data by the day of the week and calculate the average total bill for each day:

   ```python
   # Group the data by 'day' and calculate the average total bill for each day
   avg_bill_per_day = tips.groupby('day')['total_bill'].mean()
   print(avg_bill_per_day)
   ```

   Grouping data like this is extremely powerful for analyzing trends.

### Data Cleaning with Pandas

Cleaning data is an essential step in any data analysis process. Let’s explore a few techniques for handling missing data and dealing with duplicates.

1. **Handling missing data**:

   You can check for missing values in your dataset with `isnull()`:

   ```python
   # Check for missing values
   print(tips.isnull().sum())
   ```

   If any missing values are present, you can fill or drop them:

   ```python
   # Fill missing values with the median
   tips.fillna(tips.median(), inplace=True)

   # Alternatively, drop rows with missing values
   # tips.dropna(inplace=True)
   ```

2. **Removing duplicates**:

   To remove duplicate rows from the dataset:

   ```python
   # Remove duplicate rows
   tips.drop_duplicates(inplace=True)
   ```

### Saving DataFrames to Files

Once you’ve finished analyzing or cleaning your data, you can save your DataFrame to a file. Pandas supports multiple formats like CSV, Excel, and JSON.

1. **Saving a DataFrame to a CSV file**:

   ```python
   # Save the DataFrame to a CSV file
   tips.to_csv('tips_cleaned.csv', index=False)
   ```

2. **Saving a DataFrame to an Excel file**:

   ```python
   # Save the DataFrame to an Excel file
   tips.to_excel('tips_cleaned.xlsx', index=False)
   ```

Pandas is a powerful library for data analysis and manipulation in Python. It provides a wide range of functions for loading, cleaning, analyzing, and saving data, making it an essential tool for data scientists, analysts, and researchers.

Congratulations! Now you know the basics of data analysis with Pandas. You can also now use NumPy to perform mathematical operations. These are fundamental libraries and tools for machine learning in Python, and the tools that follow in this workshop all build upon these two libraries. Next, let's learn about Seaborn, a data visualization library that works well with Pandas.

[Next: Seaborn](02_seaborn.md)
