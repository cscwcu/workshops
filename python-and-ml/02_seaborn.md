## 2. Seaborn

[Home](README.md)

[Back: NumPy and Pandas](01_numpy_and_pandas.md)

In this section, we'll learn how to install Seaborn, a powerful Python library for creating informative and attractive data visualizations. We'll also work with a sample dataset to explore its features.

### Installing Seaborn

1. **Open your terminal** (or command prompt) and run the following command to install Seaborn and Matplotlib (Seaborn depends on Matplotlib for drawing plots):

   ```bash
   pip install seaborn matplotlib
   ```

2. **Verify the installation** by opening a Python interpreter and running:

   ```python
   import seaborn as sns
   import matplotlib.pyplot as plt
   ```

   If there are no errors, Seaborn is installed correctly.

### Exploring a Sample Dataset

Seaborn comes with several built-in datasets, making it easy to experiment with. In this section, we’ll use the **'tips'** dataset, which contains information about the tips collected by waiters in a restaurant. Let's load the dataset and create a simple visualization.

1. **Loading the dataset**:

   ```python
   import seaborn as sns
   import matplotlib.pyplot as plt

   # Load the built-in 'tips' dataset
   tips = sns.load_dataset("tips")
   ```

2. **Inspecting the dataset**:

   Let's inspect the first few rows of the dataset to understand its structure:

   ```python
   print(tips.head())
   ```

   What output do you see?

3. **Plotting the data**:

   Seaborn makes it easy to create different types of plots. Let’s start by creating a **scatter plot** to see the relationship between the total bill and the tip amount:

   ```python
   sns.scatterplot(x="total_bill", y="tip", data=tips)
   plt.title("Total Bill vs. Tip")
   plt.show()
   ```

   This simple scatter plot shows how the tip changes as the total bill increases.

### Customizing Your Visualizations

Seaborn allows you to easily customize your plots. For example, let’s change the colors based on whether the customer is a smoker or not, and we’ll use different markers for men and women:

```python
sns.scatterplot(x="total_bill", y="tip", hue="smoker", style="sex", data=tips)
plt.title("Total Bill vs. Tip (Colored by Smoker, Style by Sex)")
plt.show()
```

- **`hue="smoker"`**: Colors the points based on whether the customer was a smoker.
- **`style="sex"`**: Uses different markers for male and female customers.

### Creating a Bar Plot

Bar plots are another great way to visualize categorical data. Let’s look at the average tip amount for each day of the week:

```python
sns.barplot(x="day", y="tip", data=tips)
plt.title("Average Tip by Day of the Week")
plt.show()
```

This plot helps us easily compare the average tip amounts across different days.

---

### Exercise 2.1: Creating a Box Plot

Box plots are useful for visualizing the distribution of data. For this exercise, we will create a box plot to visualize the distribution of total bills based on the day of the week.

1. In your terminal or Python environment, use the following code to generate the plot:

   ```python
   sns.boxplot(x="day", y="total_bill", data=tips)
   plt.title("Distribution of Total Bill by Day")
   plt.show()
   ```

2. Observe the plot and see how the total bill distributions vary between different days.

---

### Exercise 2.2: Visualizing Correlation with a Heatmap

Heatmaps are a great way to visualize the correlation between different variables in a dataset. In this exercise, we will create a heatmap that shows the correlation between different numerical columns in the dataset.

1. Use the following code to generate the heatmap:

   ```python
   # Select only the numeric columns for correlation calculation
   numeric_columns = tips.select_dtypes(include=['float64', 'int64'])

   # Now create the heatmap with the correlation matrix of the numeric columns
   sns.heatmap(numeric_columns.corr(), annot=True, cmap="coolwarm")

   plt.title("Correlation Heatmap of Tips Dataset")
   plt.show()
   ```

2. Examine the heatmap to identify any strong correlations between variables like `total_bill` and `tip`.

---

In this section, we installed Seaborn and explored its basic functionalities using the built-in **'tips'** dataset. You now have the tools to create various plots, including scatter plots, bar plots, box plots, and heatmaps. Seaborn's ease of use and flexibility make it a great choice for quick and informative visualizations.

Next, we're gonna get into the fun stuff: machine learning with Scikit-learn!

[Next: Scikit-learn](03_scikit-learn.md)
