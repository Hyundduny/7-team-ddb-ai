from fastapi import APIRouter
from app.services.recommender import recommend_places
from app.schemas.recommend_schema import RecommendRequest, RecommendResponse

router = APIRouter()

@router.post("/recommend", response_model=RecommendResponse)
def recommend(request: RecommendRequest):
    results = recommend_places(request.text)
    return RecommendResponse(recommendations=results)
