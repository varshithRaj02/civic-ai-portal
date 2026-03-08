from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def find_similar(new_text, past_texts):

    # If no previous complaints exist
    if not past_texts or len(past_texts) == 0:
        return 0

    texts = [new_text] + past_texts

    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(texts)

    # If only one document exists
    if tfidf.shape[0] < 2:
        return 0

    similarity_matrix = cosine_similarity(tfidf[0:1], tfidf[1:])

    return float(similarity_matrix.max())