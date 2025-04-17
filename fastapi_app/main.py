from fastapi import FastAPI
from routers import inference, health

app = FastAPI()

app.include_router(inference.router, prefix="/predict", tags=["Inference"])
app.include_router(health.router, prefix="/health", tags=["Health"])
