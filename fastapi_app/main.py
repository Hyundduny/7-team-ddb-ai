from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import inference, health
from app.api.v1.endpoints.recommend import router as recommend_router

app = FastAPI(title="추천 서비스 API")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(inference.router, prefix="/predict", tags=["Inference"])
app.include_router(health.router, prefix="/health", tags=["Health"])
app.include_router(recommend_router, prefix="/api/v1", tags=["recommendations"])

@app.get("/")
async def root():
    return {"message": "추천 서비스 API가 실행 중입니다."}
