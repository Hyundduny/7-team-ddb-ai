from pydantic import BaseModel

class RecommendRequest(BaseModel):
    text: str

class Recommendation(BaseModel):
    id: int
    similarity_score: float

class RecommendResponse(BaseModel):
    recommendations: list[Recommendation]
