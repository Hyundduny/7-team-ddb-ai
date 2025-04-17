from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, List
from model.inference import run_inference

router = APIRouter()

class Input(BaseModel):
    placeId: str
    category : str
    placeName : str
    menus : Dict
    reviews : List

class Output(BaseModel):
    placeId: str
    keywords : List
    introduction : str

@router.post("", response_model=Output)
def predict(input_data: Input):
    result = run_inference(input_data.prompt)
    return {"response": result}
