from app.ml.inference import extract_keywords, get_embedding
from app.services.vector_store import search_similar_places

def recommend_places(user_text: str):
    keywords = extract_keywords(user_text)
    embedding = get_embedding(keywords)
    recommendations = search_similar_places(embedding)
    return recommendations
