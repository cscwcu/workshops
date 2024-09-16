## 3. Scikit-learn

[Home](README.md)

[Back: Seaborn](02_seaborn.md)

Scikit-learn is a popular Python library for machine learning that provides simple and efficient tools for data analysis and modeling. It includes a wide range of algorithms for classification, regression, clustering, dimensionality reduction, and more. By the end of this section, you will have created your very own machine learning model using Scikit-learn.

### Installing Scikit-learn

1. **Open your terminal** (or command prompt) and run the following command to install Scikit-learn:

   ```bash
   pip install scikit-learn
   ```

2. **Verify the installation** by opening a Python interpreter and running:

   ```python
   import sklearn
   print(sklearn.__version__)
   ```

   If there are no errors, Scikit-learn is installed correctly.

### The Basics of Machine Learning

Before we continue, take some time to go through our [Machine Learning Primer](ml_primer.md) to understand the basic concepts and terminology used in machine learning. This will help you follow along with the examples in this section.

Scikit-learn makes it easy to implement many machine learning algorithms with just a few lines of code. We will start by working with a simple supervised learning problem: predicting whether a flower is of the species **Iris-setosa**, **Iris-versicolor**, or **Iris-virginica** based on its measurements.

### Loading the Iris Dataset

Scikit-learn comes with some built-in datasets, including the famous **Iris** dataset. Let's load this dataset and take a quick look at its structure:

1. **Load the dataset**:

   ```python
   from sklearn.datasets import load_iris
   import pandas as pd

   # Load Iris dataset
   iris = load_iris()

   # Convert to a Pandas DataFrame for easier manipulation
   iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
   iris_df['species'] = iris.target
   print(iris_df.head())
   ```

   You should see the first few rows of the dataset, which includes the sepal and petal measurements of the flowers.

   The **species** column is a numerical representation of the three Iris species, where:

   - 0: Iris-setosa
   - 1: Iris-versicolor
   - 2: Iris-virginica

### Building a Simple Machine Learning Model

Now that we have the data loaded, let’s train a machine learning model to classify the species of Iris flowers based on their measurements. We will use a **Decision Tree Classifier** for this task, which is a simple yet effective algorithm for classification problems.

1. **Splitting the data into training and test sets**:

   Before training the model, we need to split the dataset into two parts: one for training the model and one for testing it to see how well it performs on unseen data.

   ```python
   from sklearn.model_selection import train_test_split

   # Split the data into training and testing sets (80% train, 20% test)
   X = iris_df[['sepal length (cm)', 'sepal width (cm)']]  # Features (sepal measurements)
   y = iris_df['species']  # Labels (species)

   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
   ```

   Here, we are using the sepal length and sepal width as features to predict the species of the flowers.

2. **Training the Decision Tree Classifier**:

   Now, let’s create and train a Decision Tree model on the training data.

   ```python
   from sklearn.tree import DecisionTreeClassifier

   # Initialize the model
   clf = DecisionTreeClassifier()

   # Train the model using the training data
   clf.fit(X_train, y_train)
   ```

3. **Making Predictions**:

   Once the model is trained, we can use it to predict the species of the flowers in the test set.

   ```python
   # Use the model to make predictions on the test data
   y_pred = clf.predict(X_test)

   # Compare the predictions to the actual labels
   print(y_pred[:5])  # Show the first 5 predictions
   print(y_test.values[:5])  # Show the first 5 actual labels
   ```

   The predicted species (numerical form) will be compared to the actual species to see how well the model performed.

   Just like that, you've created a simple machine learning model using Scikit-learn!

### Evaluating the Model’s Performance

We can evaluate the performance of our model using accuracy, which is the percentage of correct predictions.

1. **Calculating the accuracy**:

   ```python
   from sklearn.metrics import accuracy_score

   # Calculate the accuracy of the model
   accuracy = accuracy_score(y_test, y_pred)
   print(f"Model Accuracy: {accuracy * 100:.2f}%")
   ```

   The accuracy score will tell us how often the model correctly predicted the species of the flowers in the test set.

### Training a k-Nearest Neighbors Classifier

Now that you've built a Decision Tree Classifier, let's try another popular algorithm: **k-Nearest Neighbors (k-NN)**. The k-NN algorithm is easy to understand and often performs well on simple datasets.

1. **Initialize and train a k-Nearest Neighbors classifier**:

   ```python
   from sklearn.neighbors import KNeighborsClassifier

   # Initialize the k-NN model
   knn = KNeighborsClassifier(n_neighbors=3)

   # Train the model
   knn.fit(X_train, y_train)
   ```

2. **Make predictions and evaluate the model**:

   ```python
   # Make predictions on the test data
   y_pred_knn = knn.predict(X_test)

   # Calculate the accuracy of the k-NN model
   accuracy_knn = accuracy_score(y_test, y_pred_knn)
   print(f"k-NN Model Accuracy: {accuracy_knn * 100:.2f}%")
   ```

3. **Compare the performance** of the k-NN model to the Decision Tree model. Which one performed better on the Iris dataset?

### Visualizing Decision Boundaries

To better understand how machine learning models make decisions, let's visualize the decision boundaries created by the Decision Tree model.

In machine learning, a decision boundary is a line or surface that separates different classes in the feature space. When a model like a Decision Tree or k-Nearest Neighbors classifies new data points, it does so by determining on which side of the decision boundary those points fall.

In a simple two-dimensional example, if we plot two features (like sepal length and sepal width), the decision boundary would be a line that splits the feature space into regions corresponding to different classes, such as the three Iris species. Any point on one side of the boundary is predicted to belong to one class, and points on the other side belong to another class.

Visualizing decision boundaries helps us understand how a machine learning model separates different classes and makes predictions.

1. **Visualize the decision boundaries** using the following code:

   ```python
   import numpy as np
   import matplotlib.pyplot as plt

   # Create a mesh grid
   x_min, x_max = X_train.iloc[:, 0].min() - 1, X_train.iloc[:, 0].max() + 1
   y_min, y_max = X_train.iloc[:, 1].min() - 1, X_train.iloc[:, 1].max() + 1
   xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))

   # Predict the label for every point in the mesh grid
   Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
   Z = Z.reshape(xx.shape)

   # Plot the decision boundary
   plt.contourf(xx, yy, Z, alpha=0.8)
   plt.scatter(X_train.iloc[:, 0], X_train.iloc[:, 1], c=y_train, edgecolor='k', marker='o')
   plt.title('Decision Tree Decision Boundaries (Using Sepal Length and Sepal Width)')
   plt.xlabel('Sepal Length')
   plt.ylabel('Sepal Width')
   plt.show()
   ```

   This plot will show how the Decision Tree model splits the feature space into different regions, each representing one of the species.

### Titanic Survival Prediction

Check out our [Titanic Survival Prediction project](titanic_survival/README.md) to see a practical example of using Scikit-learn to predict survival on the Titanic based on passenger data!

---

In this section, we installed Scikit-learn, trained a Decision Tree classifier, and evaluated its performance. We also compared it to a k-Nearest Neighbors model and visualized the decision boundaries. Scikit-learn's simplicity and versatility make it a great choice for building and testing machine learning models.

In the next section, we will explore a popular library for computer vision: OpenCV.

[Next: OpenCV](04_opencv.md)
