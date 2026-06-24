import joblib


def predict_risk(
    reliability_score,
    lead_time_days,
    dependency_count
):

    model = joblib.load(
        "risk_model.pkl"
    )

    encoder = joblib.load(
        "risk_encoder.pkl"
    )

    prediction = model.predict(
        [[
            reliability_score,
            lead_time_days,
            dependency_count
        ]]
    )

    risk = encoder.inverse_transform(
        prediction
    )[0]

    return risk