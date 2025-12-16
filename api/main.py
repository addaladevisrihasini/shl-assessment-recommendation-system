from fastapi import FastAPI
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI(title="SHL Assessment Recommendation API")

# Load data
df = pd.read_csv("data/shl_catalog.csv")
df["combined_text"] = df.astype(str).agg(" ".join, axis=1)

# Vectorize
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(df["combined_text"])

@app.get("/")
def home():
    return {"message": "SHL Assessment Recommendation API is running"}

@app.get("/recommend")
def recommend(query: str, top_k: int = 5):
    query_vec = vectorizer.transform([query])
    similarity_scores = cosine_similarity(query_vec, X)[0]
    top_indices = similarity_scores.argsort()[-top_k:][::-1]
    results = df.iloc[top_indices]
    return results.to_dict(orient="records")
