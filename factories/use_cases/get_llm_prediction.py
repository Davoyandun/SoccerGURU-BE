from factories.repositories import llm_repository
from core.src.use_cases.get_llm_prediction import GetLLMPrediction

def get_llm_prediction_use_case() -> GetLLMPrediction:
    return GetLLMPrediction(llm_repository=llm_repository())
