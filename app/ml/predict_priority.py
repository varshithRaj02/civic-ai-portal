import joblib
import os

base_dir = os.path.dirname(__file__)

model_path = os.path.join(base_dir, "priority_model.pkl")
vectorizer_path = os.path.join(base_dir, "vectorizer.pkl")

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)


def detect_risk(text):

    text = text.lower()

    safety_keywords = [
        "electric", "wire", "live wire", "fire",
        "gas leak", "collapse", "danger"
    ]

    health_keywords = [
        "sewage", "garbage", "waste",
        "dirty water", "drain"
    ]

    for k in safety_keywords:
        if k in text:
            return "Safety Hazard"

    for k in health_keywords:
        if k in text:
            return "Public Health"

    return "General Issue"


def predict_priority(text):

    vec = vectorizer.transform([text])

    prediction = model.predict(vec)[0]

    probs = model.predict_proba(vec)

    severity_score = max(probs[0])

    risk = detect_risk(text)

    return {
        "priority": prediction,
        "severity_score": round(float(severity_score), 2),
        "risk_type": risk
    }