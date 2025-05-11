import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import GridSearchCV

# Load dataset
df = pd.read_csv(r'E:\4th semester\AI Lab\lab 09\customer_value_dataset.csv')

# Display initial data info
print("Initial data info:")
print(df.info())

# Handle missing values - Simple approach: drop rows with missing values
df = df.dropna()

# Feature selection: drop the target column for training
X = df.drop('high_value', axis=1)
y = df['high_value']

# Feature scaling: Standardize features to ensure they have similar scales
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train a Support Vector Machine classifier
svm_model = SVC(kernel='linear', random_state=42)
svm_model.fit(X_train, y_train)

# Make predictions
y_pred = svm_model.predict(X_test)

# Evaluate the model's performance
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("Classification Report:\n", classification_report(y_test, y_pred))

# Identify decision boundary (hyperplane) coefficients
print("Support Vector Machine Coefficients (Hyperplane parameters):")
print(svm_model.coef_)

# Optional: Grid Search to find the best hyperparameters for the SVM model
param_grid = {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']}
grid_search = GridSearchCV(SVC(), param_grid, cv=5)
grid_search.fit(X_train, y_train)

# Best hyperparameters
print("Best Hyperparameters from Grid Search:", grid_search.best_params_)

# Function to classify a new customer
def classify_customer(customer_data):
    customer_data_scaled = scaler.transform([customer_data])
    prediction = svm_model.predict(customer_data_scaled)[0]
    return "High-Value" if prediction == 1 else "Low-Value"

# Example: Classify a new customer
new_customer = [30, 1500, 12, 6]  # [age, total_spending, visits_last_6_months, purchase_frequency]
result = classify_customer(new_customer)
print(f"New customer classification: {result}")
