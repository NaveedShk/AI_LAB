import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset
df = pd.read_csv(r'E:\4th semester\AI Lab\lab 09\spam_dataset.csv')

# Features and target
X = df['email_text']
y = df['label']  # 1 = spam, 0 = not spam

# Convert text to numerical features using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
X_vectorized = vectorizer.fit_transform(X)

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Train a Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Function to classify new incoming emails
def classify_email(email_text):
    email_vec = vectorizer.transform([email_text])
    prediction = model.predict(email_vec)[0]
    return "Spam" if prediction == 1 else "Not Spam"

# Example prediction
new_email = "Win a brand new car by entering this contest now!"
result = classify_email(new_email)
print(f"New email classification: {result}")
