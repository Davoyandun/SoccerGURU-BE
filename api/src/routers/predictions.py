from fastapi import APIRouter
from factories.use_cases import get_llm_prediction_use_case

predictions_router = APIRouter()


@predictions_router.get("/predictions/{team_id_1}/{team_id_2}")
async def get_prediction(team_id_1: int, team_id_2: int):
    try:
        # Call the proper use case to get the data
        prediction = get_llm_prediction_use_case()
        return prediction

    except Exception as e:
        return {"error": str(e)}
