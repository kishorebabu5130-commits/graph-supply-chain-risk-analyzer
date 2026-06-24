from sqlalchemy.orm import Session

from app.models.supplier import Supplier
from app.models.dependency import Dependency

from app.ml.predictor import predict_risk




#High Risk Suppliers Function

def get_high_risk_suppliers(
    db: Session
):

    suppliers = db.query(
        Supplier
    ).all()

    result = []

    for supplier in suppliers:

        dependency_count = db.query(
            Dependency
        ).filter(
            Dependency.supplier_id ==
            supplier.id
        ).count()

        risk = predict_risk(
            supplier.reliability_score,
            supplier.lead_time_days,
            dependency_count
        )

        if risk in [
            "HIGH",
            "CRITICAL"
        ]:

            result.append({
                "supplier_id":
                    supplier.id,

                "supplier_name":
                    supplier.supplier_name,

                "risk_level":
                    risk
            })

    return result

#Risk Summary Function

def get_risk_summary(
    db: Session
):

    suppliers = db.query(
        Supplier
    ).all()

    summary = {
        "LOW": 0,
        "MEDIUM": 0,
        "HIGH": 0,
        "CRITICAL": 0
    }

    for supplier in suppliers:

        dependency_count = db.query(
            Dependency
        ).filter(
            Dependency.supplier_id ==
            supplier.id
        ).count()

        risk = predict_risk(
            supplier.reliability_score,
            supplier.lead_time_days,
            dependency_count
        )

        summary[risk] += 1

    return summary


#Top Risk Suppliers Function

def get_top_risk_suppliers(
    db: Session
):

    suppliers = db.query(
        Supplier
    ).all()

    result = []

    for supplier in suppliers:

        dependency_count = db.query(
            Dependency
        ).filter(
            Dependency.supplier_id ==
            supplier.id
        ).count()

        risk = predict_risk(
            supplier.reliability_score,
            supplier.lead_time_days,
            dependency_count
        )

        score = (
            (1 - supplier.reliability_score)
            * 50
            +
            supplier.lead_time_days
            * 1.5
            +
            dependency_count
            * 5
        )

        result.append({
            "supplier_id":
                supplier.id,

            "supplier_name":
                supplier.supplier_name,

            "risk_score":
                round(score, 2),

            "risk_level":
                risk
        })

    result.sort(
        key=lambda x:
        x["risk_score"],
        reverse=True
    )

    return result[:10]