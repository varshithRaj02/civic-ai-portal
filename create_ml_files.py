from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Sample training data
texts = [
    "water leakage in street",
    "road completely broken",
    "street light not working",
    "garbage not collected",
    "sewage overflow",
    "tree fallen on road"
]

labels = [
    "Medium",
    "High",
    "Low",
    "Medium",
    "High",
    "Medium"
]

# Create vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Train model
model = RandomForestClassifier()
model.fit(X, labels)

# Ensure folder exists
os.makedirs("app/ml", exist_ok=True)

# Save files
joblib.dump(model, "app/ml/priority_model.pkl")
joblib.dump(vectorizer, "app/ml/vectorizer.pkl")

print("Model and vectorizer created successfully!")