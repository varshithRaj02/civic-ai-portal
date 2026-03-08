import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib

# Training dataset
data = {

"text":[

"live electric wire hanging near school",
"major road collapse causing accidents",
"gas leak smell near residential building",
"electric pole about to fall",

"garbage pile near market",
"drainage water overflowing on road",
"water leakage from pipeline",

"street light not working",
"broken bench in park",
"small potholes on road"

],

"priority":[

"High",
"High",
"High",
"High",

"Medium",
"Medium",
"Medium",

"Low",
"Low",
"Low"

]

}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer(
ngram_range=(1,2),
stop_words="english"
)

X = vectorizer.fit_transform(df["text"])

model = RandomForestClassifier()

model.fit(X, df["priority"])

joblib.dump(model,"priority_model.pkl")
joblib.dump(vectorizer,"vectorizer.pkl")

print("Model trained successfully")