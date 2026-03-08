from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def find_similar(description, past_complaints):

    texts = [description] + past_complaints

    vectorizer = TfidfVectorizer(stop_words="english")

    tfidf = vectorizer.fit_transform(texts)

    similarity_matrix = cosine_similarity(tfidf[0:1], tfidf[1:])

    score = similarity_matrix.max()

    return round(float(score),2)