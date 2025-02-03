from pydantic import BaseModel


class PredictionRequest(BaseModel):
    teams_data: str
