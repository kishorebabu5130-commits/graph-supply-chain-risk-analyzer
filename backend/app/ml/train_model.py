from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import (
    train_test_split
)

from sklearn.preprocessing import (
    LabelEncoder
)

import joblib

from app.ml.dataset_generator import (
    generate_dataset
)


#Training Function

def train_model():

    df = generate_dataset()

    X = df[
        [
            "reliability_score",
            "lead_time_days",
            "dependency_count"
        ]
    ]

    y = df["risk_level"]

    encoder = LabelEncoder()

    y_encoded = encoder.fit_transform(y)

    X_train, X_test, y_train, y_test = (
        train_test_split(
            X,
            y_encoded,
            test_size=0.2,
            random_state=42
        )
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    joblib.dump(
        model,
        "risk_model.pkl"
    )

    joblib.dump(
        encoder,
        "risk_encoder.pkl"
    )

    accuracy = model.score(
        X_test,
        y_test
    )

    return {
        "accuracy": round(
            accuracy,
            4
        )
    }