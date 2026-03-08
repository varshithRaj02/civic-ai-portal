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

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = RandomForestClassifier()
model.fit(X, labels)

os.makedirs("app/ml", exist_ok=True)

joblib.dump(model, "app/ml/priority_model.pkl")

print("Model created successfully!")