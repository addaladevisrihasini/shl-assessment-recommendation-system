import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("data/shl_catalog.csv")

# Combine all columns into one text field
df["combined_text"] = df.astype(str).agg(" ".join, axis=1)

# Create TF-IDF vectors ONCE
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(df["combined_text"])


def recommend(query, top_k=5, min_similarity=0.1):
    query_vec = vectorizer.transform([query])
    similarity_scores = cosine_similarity(query_vec, X)[0]

    sorted_indices = similarity_scores.argsort()[::-1]

    filtered_indices = [
        i for i in sorted_indices
        if similarity_scores[i] >= min_similarity
    ]

    if not filtered_indices:
        return None

    top_indices = filtered_indices[:top_k]
    return df.iloc[top_indices]
