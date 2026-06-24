from pydantic import BaseModel


class PredictionRequest(BaseModel):

    reliability_score: float
    lead_time_days: int
    dependency_count: int


class PredictionResponse(BaseModel):

    predicted_risk: str