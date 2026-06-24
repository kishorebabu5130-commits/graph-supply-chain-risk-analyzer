from app.ml.train_model import (
    train_model
)

from app.ml.predictor import (
    predict_risk
)



def train():

    return train_model()


def predict(data):

    risk = predict_risk(
        data.reliability_score,
        data.lead_time_days,
        data.dependency_count
    )

    return {
        "predicted_risk": risk
    }


    