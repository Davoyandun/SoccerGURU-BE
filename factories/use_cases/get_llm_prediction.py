from factories.repositories import llm_repository
from core.src.use_cases.create_llm_prediction import CreatePrediction

def create_llm_prediction_use_case() -> CreatePrediction:
    return CreatePrediction(ai_assistant_repository=llm_repository())
