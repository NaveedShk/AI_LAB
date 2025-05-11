import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder

# Load dataset
df = pd.read_csv(r'E:\4th semester\AI Lab\lab 09\house_data.csv')  # Make sure this file is in the same directory as your script

# Display initial info
print("Initial data info:")
print(df.info())

# Handle missing values
df = df.dropna()  # Drop rows with missing values

# Encode categorical variables
categorical_cols = ['neighborhood']
encoder = OneHotEncoder(drop='first', sparse_output=False)
encoded_cats = encoder.fit_transform(df[categorical_cols])

# Fix column names to match the number of encoded columns
encoded_columns = [f"{categorical_cols[0]}_{cat}" for cat in encoder.categories_[0][1:]]
encoded_df = pd.DataFrame(encoded_cats, columns=encoded_columns)

# Combine encoded categorical data with the rest
df = df.drop(columns=categorical_cols)
df = pd.concat([df.reset_index(drop=True), encoded_df.reset_index(drop=True)], axis=1)

# Define features and target
X = df.drop('price', axis=1)
y = df['price']

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"Model RMSE: {rmse:.2f}")
print(f"Model R² score: {r2:.2f}")

# Feature importance
feature_importances = pd.Series(model.feature_importances_, index=X.columns)
important_features = feature_importances.sort_values(ascending=False)
print("Top features influencing price:")
print(important_features.head())

# Predict price for a new house
def predict_price(features_dict):
    input_df = pd.DataFrame([features_dict])

    # Encode categorical values
    encoded_input = encoder.transform(input_df[categorical_cols])
    encoded_columns = [f"{categorical_cols[0]}_{cat}" for cat in encoder.categories_[0][1:]]
    encoded_input_df = pd.DataFrame(encoded_input, columns=encoded_columns)

    # Merge numeric and encoded features
    input_df = input_df.drop(columns=categorical_cols)
    input_df = pd.concat([input_df.reset_index(drop=True), encoded_input_df.reset_index(drop=True)], axis=1)

    return model.predict(input_df)[0]

# Example prediction
new_house = {
    'square_footage': 2200,
    'bedrooms': 3,
    'bathrooms': 2,
    'age': 10,
    'neighborhood': 'Downtown'
}
predicted_price = predict_price(new_house)
print(f"Predicted price for the new house: ${predicted_price:,.2f}")
