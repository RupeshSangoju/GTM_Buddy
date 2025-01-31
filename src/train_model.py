import pandas as pd
import numpy as np
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from preprocess_data import load_data

# Load dataset
df = load_data("dataset/data.xlsx")

# Convert text to TF-IDF vectors
vectorizer = TfidfVectorizer(max_features=1000)
X = vectorizer.fit_transform(df["text_snippet"]).toarray()

# Convert labels to binary matrix
all_labels = ["Objection", "Pricing Discussion", "Security", "Competition"]
Y = df["labels"].apply(lambda labels: [1 if label in labels else 0 for label in all_labels]).tolist()

# Train-test split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Train Model
classifier = MultiOutputClassifier(RandomForestClassifier(n_estimators=200))
classifier.fit(X_train, Y_train)

# Evaluate Model
predictions = classifier.predict(X_test)
print(classification_report(Y_test, predictions, target_names=all_labels))

# Save model
joblib.dump(classifier, "models/classifier.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")
print("Model saved successfully!")
