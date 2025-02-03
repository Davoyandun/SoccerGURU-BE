from fastapi import Depends, APIRouter, HTTPException

from factories.use_cases import create_llm_prediction_use_case
from core.src.use_cases import CreatePrediction

predictions_router = APIRouter()
OPENAI_ASSISTANT_NAME = "marketing"


@predictions_router.get("/home-team/{home_team_id}/away-team/{away_team_id}")
async def create_prediction(
    home_team_id: str,
    away_team_id: str,
    use_case: CreatePrediction = Depends(create_llm_prediction_use_case),
):
    try:
        prediction = use_case(OPENAI_ASSISTANT_NAME, home_team_id, away_team_id)
        return prediction

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
