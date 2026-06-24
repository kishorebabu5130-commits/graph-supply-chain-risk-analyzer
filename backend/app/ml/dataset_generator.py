import pandas as pd
import numpy as np


def generate_dataset(
    rows=1000
):

    np.random.seed(42)

    data = {
        "reliability_score":
            np.random.uniform(
                0.3,
                1.0,
                rows
            ),

        "lead_time_days":
            np.random.randint(
                1,
                30,
                rows
            ),

        "dependency_count":
            np.random.randint(
                0,
                10,
                rows
            )
    }

    df = pd.DataFrame(data)

    risk_score = (
        (1 - df["reliability_score"]) * 50
        +
        (df["lead_time_days"] * 1.5)
        +
        (df["dependency_count"] * 5)
    )

    df["risk_level"] = np.where(
        risk_score < 25,
        "LOW",
        np.where(
            risk_score < 50,
            "MEDIUM",
            np.where(
                risk_score < 75,
                "HIGH",
                "CRITICAL"
            )
        )
    )

    return df