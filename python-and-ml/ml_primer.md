[Home](README.md)

[Back](03_scikit-learn.md)

# What is Machine Learning (ML)?

Machine Learning (ML) is a subset of artificial intelligence (AI) that allows systems to learn and make their own decisions based on data provided. Instead of being explicitly programmed to perform tasks, many ML models learn patterns from data and make predictions or decisions based on their learning.

## Traditional Programming vs. Machine Learning:

- **Traditional Programming**: The developer writes rules that the computer follows to get a result.
  - Input + Rules = Output
- **Machine Learning**: The system learns the rules by analyzing the data, allowing it to generalize and handle new, unseen data.
  - Input + Output = Rules

# Types of Machine Learning

There are three major types of machine learning, classified based on how the algorithm learns from the input data.

## Supervised Learning:

- **Description**: The model is trained on labeled data, meaning both input and corresponding output (label) are known. The model learns a mapping from inputs to outputs.
- **Example**: Spam detection in emails, where the model learns to classify emails as "spam" or "not spam" based on past labeled data
- **Types of Supervised Learning**:
  - **Classification**: The task of predicting discrete labels (e.g., email spam or not spam, digits 0-9).
  - **Regression**: Predicting continuous values (e.g., predicting house prices or stock prices).
- **Examples of Algorithms**: Linear Regression, Decision Trees, Random Forest.

## Unsupervised Learning:

- **Description**: The model is trained on unlabeled data, meaning only the input is known. The model tries to find patterns or groupings in the data without explicit output labels.
- **Example**: Customer segmentation in marketing, where the goal is to group customers based on purchasing behaviors without pre-labeled groups.
- **Types of Unsupervised Learning**:
  - **Clustering**: Grouping similar data points together (e.g., grouping similar customers).
  - **Dimensionality Reduction**: Reducing the number of input variables to simplify the data (e.g., Principal Component Analysis).
- **Example of Algorithms**: K-Means Clustering, Hierarchical Clustering, DBSCAN.

## Reinforcement Learning:

- **Description**: The model learns by interacting with an environment, receiving rewards or penalties based on actions it takes. Over time, the model learns to maximize the total reward.
- **Example**: Game-playing AI (e.g., auto chess engines), where the model tries to win by making optimal moves based on rewards (winning) and penalties (losing).
- **Key Concepts**: Agent, environment, reward, action, state.
- **Examples of Algorithms**: Q-Learning, Deep Q-Networks (DQN), Proximal Policy Optimization (PPO).

# Common Use Cases of Machine Learning

Machine learning is used in a wide variety of industries and applications. Here are some common use cases:

## 1. Classification:

- **Spam Detection**: Identifying whether an email is spam or not based on content.
- **Image Recognition**: Classifying images (e.g., recognizing handwritten digits, classifying objects in pictures).
- **Fraud Detection**: Identifying fraudulent transactions or activity in financial systems.

## 2. Regression:

- **House Price Prediction**: Predicting the price of a house based on feature like size, location, and number of rooms.
- **Stock Market Forecasting**: Predicting the future price of stocks based on historical data.

## 3. Clustering:

- **Customer Segmentation**: Grouping customers into segments based on purchasing behavior for targeted marketing.
- **Document Clustering**: Automatically grouping documents into topics or themes.

## 4. Anomaly Detection:

- **Fraud Detection**: Identifying unusual patterns in transaction data that may indicate fraudulent activity.
- **Network Security**: Detecting unusual access patterns in a network to identify potential security breaches.

## 5. Recommendation Systems:

- **Movie Recommendations**: Suggesting movies or products to users based on past behavior (e.g., Netflix, Amazon).
- **Music Recommendations**: Recommending new music tracks based on a user's listening history.

# How Machine Learning is Done (High-Level Workflow)

The process of building and deploying a machine learning model involves several key steps:

## 1. Collect Data:

- The first step is gathering the data you will use to train the model. This could be from databases, APIs, or other sources. The more data you have, the better the model can learn.
- **Example**: Collecting past email data to classify spam or not spam

## 2. Preprocess Data:

- **Data Cleaning**: Handle missing values, remove duplicates, and correct inconsistent data.
- **Feature Scaling**: Standardize or normalize data to ensure all features contribute equally.
- **Encoding**: Convert categorical data into numerical form (e.g., using one-hot encoding).
- **Train-Test Split**: Split the data into training and testing sets (typically 70%-80% for training and 20%-30% for testing).

## 3. Choose and Train a Model:

- Select an appropriate algorithm for the task (e.g., decision tree for classification, linear regression for regression tasks).
- Train the model using the training dataset. The model learns patterns by minimizing errors.

## 4. Evaluate the Model:

- Test the model on the test set to see how well it generalizes the unseen data.
- Use performance metrics (e.g., accuracy, precision, recall) to measure the quality of the model.

## 5. Improve the Model:

- Tune hyperparameters, add more features, or try different algorithms to improve performance.
- Cross-validation is often used to better estimate model performance by averaging results across multiple train-test splits

## 6. Deploy the Model:

- Once the model has good performance metrics, it can be deployed to make predictions on real-world data.
- In production, the model may need to be monitored and retrained as new data comes in.

# Performance Metrics

After training a model, it's crucial to evaluate its performance using the right metrics. Here are the most common ones for classification and regression:

## For Classification:

### 1. Accuracy:

- **Description**: The proportion of correct predictions (true positive + true negatives) out of all predictions
- **Formula**:
  $$\text{Accuracy} = \frac{\text{True Positives} + \text{True Negatives}}{\text{Total Samples}}$$
- **When to Use**: Useful when data is balanced. If the dataset is imbalanced, accuracy might be misleading.

### 2. Precision:

- **Description**: The proportion of true positive predictions out of all predicted positives.
- **Formula**:
  $$\text{Precision} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}}$$
- **When to Use**: Important when false positives are costly (e.g., spam detection).

### 3. Recall (Sensitivity/True Positive Rate):

- **Description**: The proportion of true positives out of all actual positives.
- **Formula**:
  $$\text{Recall} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}}$$
- **When to Use**: Important when false negatives are costly (e.g., medical diagnosis)

### 4. F1 Score:

- **Description**: The harmonic mean of precision and recall.
- **Formula**:
  $$F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$
- **When to Use**: A balanced measure when both precision and recall are important.

## For Regression:

### 1. Mean Squared Error (MSE):

- **Description**: The average squared difference between actual and predicted values. Lower values indicate better model performance.
- **Formula**:
  $$\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$
- **When to Use**: A simpler alternative to MSE, especially for datasets with outliers.

### 2. Mean Absolute Error (MAE):

- **Description**: The average absolute difference between actual and predicted values. Less sensitive to outliers than MSE.
- **Formula**:
  $$\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} \left| y_i - \hat{y}_i \right|$$
- **When to Use**: A simpler alternative to MSE, especially for datasets with outliers.

### 3. R-squared (R^2^):

- **Description**: The proportion of the variance in the target variable explained by the model. Values range from 0 to 1, with 1 being a perfect fit.
- **Formula**:
  $$R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$$
- **When to Use**: Provides an overall measure of how well the model explains the data.
