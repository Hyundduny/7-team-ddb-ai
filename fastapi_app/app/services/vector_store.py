def search_similar_places(query_embedding: list[float], top_k: int = 3):
    # 실제로는 FAISS/Chroma 등 벡터DB에서 검색해야 함
    # 예시: 임의의 장소 벡터와 유사도 계산
    dummy_places = [
        {"id": 1, "embedding": [3.0, 2.0, 1.0]},
        {"id": 21, "embedding": [2.0, 2.0, 2.0]},
        {"id": 32, "embedding": [1.0, 2.0, 3.0]},
    ]
    def cosine_sim(a, b):
        import numpy as np
        a, b = np.array(a), np.array(b)
        return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))
    results = [
        {"id": p["id"], "similarity_score": cosine_sim(query_embedding, p["embedding"])}
        for p in dummy_places
    ]
    results.sort(key=lambda x: x["similarity_score"], reverse=True)
    return results[:top_k]
