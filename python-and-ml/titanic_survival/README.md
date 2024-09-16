# Titanic Survival Prediction

This project demonstrates a simple machine learning classification task using the Titanic dataset. The goal is to predict whether a passenger would have survived the Titanic disaster based on their class, sex, age, fare, and embarkation port.

## Project Overview

Using a Random Forest Classifier, we train a model on the Titanic dataset to classify passengers as "Survived" or "Did Not Survive" based on various input features. After training, the model can make predictions based on user input, allowing the audience to see if they would have survived the Titanic disaster.

### Dataset

The dataset used is from the [Datasciencedojo Titanic dataset](https://github.com/datasciencedojo/datasets/blob/master/titanic.csv). The relevant features used in this project include:

- **Pclass**: Passenger class (1st, 2nd, 3rd)
- **Sex**: Gender (male/female)
- **Age**: Passenger's age
- **Fare**: Ticket price
- **Embarked**: Embarkation point (C = Cherbourg, Q = Queenstown, S = Southampton)

The dataset is preprocessed to handle missing data and encode categorical variables like gender and embarkation points.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/cscwcu/workshops.git
   cd python-and-ml/titanic_survival
   ```

2. **Install the necessary dependencies**:

   This project uses Python's `pandas`, `scikit-learn`, and `matplotlib` libraries. You can install the dependencies via `pip`:

   ```bash
   pip install pandas scikit-learn matplotlib
   ```

## How to Run the Project

1. **Run the Python script**:

   Execute the Python script to train the model and predict Titanic survival based on user input:

   ```bash
   python main.py
   ```

2. **Enter the following details when prompted**:

   - **Class**: Enter your passenger class (1 = 1st class, 2 = 2nd class, 3 = 3rd class).
   - **Sex**: Enter your gender (male/female).
   - **Age**: Enter your age (e.g., 28).
   - **Fare**: Enter your ticket fare (e.g., 7.25).
   - **Embarkation Port**: Enter your port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton).

   The script will then use the trained Random Forest model to predict whether you would have survived the Titanic disaster.

## Example Output

```bash
Model trained! Here's the performance on the test set:
              precision    recall  f1-score   support

 Did Not Survive       0.86      0.91      0.88       105
       Survived       0.81      0.73      0.77        74

    accuracy                           0.84       179
   macro avg       0.83      0.82      0.83       179
weighted avg       0.84      0.84      0.84       179

Let's see if you would have survived the Titanic!
Enter your class (1 = 1st class, 2 = 2nd class, 3 = 3rd class): 2
Enter your sex (male/female): male
Enter your age: 30
Enter your fare (e.g., 7.25): 12.75
Enter your embarkation port (C = Cherbourg, Q = Queenstown, S = Southampton): S

The model predicts: You would have Did Not Survive.
```

## Model Evaluation

The Random Forest model is trained on 80% of the dataset and tested on 20%. The `classification_report` from `scikit-learn` provides metrics like precision, recall, and F1-score to evaluate the model's performance. The script achieves approximately 84% accuracy in predicting survival.
