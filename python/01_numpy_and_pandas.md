## 1. NumPy

[Home](README.md)

### What is NumPy?

NumPy is a fundamental package in Python and is widely used across various fields, including data scientists and software engineers in order to
perform any kind of scientific computing. This library provides a basis for many of these
operations, such as multidimensional arrays, matrices, and many basic mathematical
operations to save the programmer time from computing them instead.

[Click this link to explore more on their website.](https://numpy.org/)

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

   - NumPy is employed in signal processing and image manipulation, where array-based operations are crucial for filtering, transformation, and analysis.

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

   # Time a NumPy operation
   start_time = time.time()
   result = np.sqrt(array)
   end_time = time.time()

   print(f'Time taken: {end_time - start_time} seconds')
   ```

---

## 2. Pandas

### What is Pandas?

Panda bears are usually characterised by their white coat with black patches around the eyes, ears, legs and shoulders -- oh, sorry. Wrong pandas...

Pandas is a widely used, fast, flexible, and open source data analysis and manipulation tool built in python. It can be used widely for data wrangling and handling datasets, and is commonly paired with NumPy (see we told you) in order to create the most efficient dataframe library in python.01_numpy_and_pandas

### Let's Get Started

Very similar to NumPy, we can simply use pip or pip3 to install:

`pip install pandas` or `pip3 install pandas`

Now that we've installed the library, we just need to say in a python file:

`import pandas as pd`

**Note:** Once again, pd is an extremely common naming convention, and we once again recommend it.

### Common use cases and examples of Pandas

Here are some common use cases along with examples:

1. **Data Cleaning and Preparation**

   - **Handling Missing Data:** Handle missing data by filling it in or dropping rows/columns.

     ```python
     import pandas as pd

     df = pd.DataFrame({'A': [1, 2, None], 'B': [4, None, 6]})
     df.fillna(df.mean(), inplace=True)  # Filling missing values with column means
     ```

   - **Removing Duplicates:** Identify and remove duplicate rows.
     ```python
     df = pd.DataFrame({'A': [1, 2, 2, 3], 'B': [4, 5, 5, 6]})
     df.drop_duplicates(inplace=True)
     ```

2. **Data Transformation**

   - **Applying Functions:** Apply functions to columns or rows using `.apply()`.

     ```python
     df = pd.DataFrame({'A': [1, 2, 3]})
     df['B'] = df['A'].apply(lambda x: x ** 2)  # Applying a function to square values
     ```

   - **Grouping Data:** Aggregate data by group.
     ```python
     df = pd.DataFrame({'Category': ['A', 'B', 'A', 'B'], 'Value': [10, 20, 30, 40]})
     grouped = df.groupby('Category').sum()
     ```

3. **Data Exploration and Analysis**

   - **Descriptive Statistics:** Get summary statistics of your data.

     ```python
     df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
     stats = df.describe()  # Returns count, mean, std, min, 25%, 50%, 75%, max
     ```

   - **Correlation Analysis:** Compute correlation matrices to understand relationships between variables.
     ```python
     df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [2, 4, 6, 8]})
     correlation = df.corr()  # Compute correlation matrix
     ```

4. **Data Visualization**

   - **Plotting:** Use pandas to create basic plots.
     ```python
     df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [2, 4, 6, 8]})
     df.plot(kind='scatter', x='A', y='B')  # Scatter plot
     ```

5. **Time Series Analysis**

   - **Date and Time Handling:** Work with date/time data and perform resampling or shifting.
     ```python
     dates = pd.date_range('2024-01-01', periods=5, freq='D')
     df = pd.DataFrame({'Date': dates, 'Value': [1, 2, 3, 4, 5]})
     df.set_index('Date', inplace=True)
     df_resampled = df.resample('W').sum()  # Resample by week and sum values
     ```

6. **Merging and Joining Data**

   - **Combining Datasets:** Merge or join different DataFrames.
     ```python
     df1 = pd.DataFrame({'ID': [1, 2, 3], 'Value1': ['A', 'B', 'C']})
     df2 = pd.DataFrame({'ID': [1, 2, 4], 'Value2': ['D', 'E', 'F']})
     merged = pd.merge(df1, df2, on='ID', how='inner')  # Inner join on 'ID'
     ```

7. **Reading and Writing Data**

   - **CSV Files:** Read and write data from/to CSV files.

     ```python
     df = pd.read_csv('data.csv')  # Reading a CSV file
     df.to_csv('output.csv', index=False)  # Writing to a CSV file
     ```

   - **Excel Files:** Read from and write to Excel files.
     ```python
     df = pd.read_excel('data.xlsx', sheet_name='Sheet1')  # Reading from Excel
     df.to_excel('output.xlsx', index=False)  # Writing to Excel
     ```

8. **Data Aggregation and Pivoting**

   - **Pivot Tables:** Create pivot tables to summarize data.
     ```python
     df = pd.DataFrame({'A': ['foo', 'foo', 'bar', 'bar'], 'B': ['one', 'two', 'one', 'two'], 'C': [10, 20, 30, 40]})
     pivot_table = df.pivot_table(values='C', index='A', columns='B', aggfunc='sum')
     ```

These use cases cover a broad range of tasks in data science and analysis, making pandas a versatile tool for working with data in Python.

[Next: Seaborn](02_seaborn.md)
