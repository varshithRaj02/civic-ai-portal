def predict_priority(text):
    text = text.lower()

    if any(w in text for w in ["accident", "fire", "collapse", "danger"]):
        return "High"
    if any(w in text for w in ["leak", "broken", "not working"]):
        return "Medium"
    return "Low"
