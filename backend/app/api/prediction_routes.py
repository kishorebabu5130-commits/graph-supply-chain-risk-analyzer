from fastapi import APIRouter

from app.schemas.prediction import (
    PredictionRequest,
    PredictionResponse
)

from app.services import (
    prediction_service
)





router = APIRouter()

@router.post("/train")
def train_model():
    return prediction_service.train()

#Predict Endpoint


@router.post(
    "/",
    response_model=PredictionResponse
)
def predict(
    request: PredictionRequest
):

    return prediction_service.predict(
        request
    )


