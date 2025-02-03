from fastapi import Depends, APIRouter, HTTPException

from factories.use_cases import create_llm_prediction_use_case
from core.src.use_cases import CreatePrediction
from ..dtos import PredictionRequest

predictions_router = APIRouter()
OPENAI_ASSISTANT_NAME = "marketing"


@predictions_router.post("/")
async def create_prediction(
    request: PredictionRequest,
    use_case: CreatePrediction = Depends(create_llm_prediction_use_case),
):
    try:
        prediction = use_case.run(request.teams_data, OPENAI_ASSISTANT_NAME)
        return prediction

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
