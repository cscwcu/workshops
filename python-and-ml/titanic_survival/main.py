# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load the Titanic dataset
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic = pd.read_csv(url)

# Preprocessing: select relevant features and handle missing data
titanic = titanic[['Survived', 'Pclass', 'Sex', 'Age', 'Fare', 'Embarked']]
titanic.dropna(inplace=True)  # Drop rows with missing data

# Convert categorical data to numerical data
titanic['Sex'] = titanic['Sex'].map({'male': 0, 'female': 1})  # Encode male/female as 0/1
titanic['Embarked'] = titanic['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})  # Encode embark points as 0/1/2

# Separate features (X) and target (y)
X = titanic[['Pclass', 'Sex', 'Age', 'Fare', 'Embarked']]
y = titanic['Survived']

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100)
rf_model.fit(X_train, y_train)

# Predict on the test set
y_pred = rf_model.predict(X_test)

# Display classification results
print("Model trained! Here's the performance on the test set:")
print(classification_report(y_test, y_pred, target_names=["Did Not Survive", "Survived"]))

# Function to get audience input
def get_audience_input():
    """
    Get input from the audience to predict if they would have survived the Titanic.

    Returns:
        list: A list containing the input data in the correct format for prediction
    """
    print("\nLet's see if you would have survived the Titanic!")
    
    # Get input from the audience
    pclass = int(input("Enter your class (1 = 1st class, 2 = 2nd class, 3 = 3rd class): "))
    sex = input("Enter your sex (male/female): ").strip().lower()
    sex = 0 if sex == 'male' else 1
    age = float(input("Enter your age: "))
    fare = float(input("Enter your fare (e.g., 7.25): "))
    embarked = input("Enter your embarking port (C = Cherbourg, Q = Queenstown, S = Southampton): ").strip().upper()
    embarked = {'C': 0, 'Q': 1, 'S': 2}[embarked]

    # Prepare the input data in the correct format for prediction
    audience_data = [[pclass, sex, age, fare, embarked]]
    return audience_data

# Get audience input and make a prediction
audience_data = get_audience_input()
prediction = rf_model.predict(audience_data)
predicted_outcome = "survived" if prediction[0] == 1 else "died"

print(f"The model predicts: You would have {predicted_outcome}!")
