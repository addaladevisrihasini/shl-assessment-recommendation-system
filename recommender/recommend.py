import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("data/shl_catalog.csv")

# Combine all columns into one text field
df["combined_text"] = df.astype(str).agg(" ".join, axis=1)

# Convert text to vectors
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(df["combined_text"])

def recommend(query, top_k=5):
    query_vec = vectorizer.transform([query])
    similarity_scores = cosine_similarity(query_vec, X)[0]
    top_indices = similarity_scores.argsort()[-top_k:][::-1]
    return df.iloc[top_indices]

if __name__ == "__main__":
    results = recommend("python data science entry level")
    print(results.head())
