from fastapi import APIRouter
from pydantic import BaseModel
from model.inference import run_inference

router = APIRouter()

class Input(BaseModel):
    prompt: str

class Output(BaseModel):
    response: str

@router.post("", response_model=Output)
def predict(input_data: Input):
    result = run_inference(input_data.prompt)
    return {"response": result}
