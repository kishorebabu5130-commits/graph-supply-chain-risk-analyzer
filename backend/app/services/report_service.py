import csv
import io

from sqlalchemy.orm import Session

from app.models.supplier import Supplier
from app.models.dependency import Dependency

from app.ml.predictor import predict_risk

from app.services.graph_service import build_graph


#Risk Report

def generate_risk_report(
    db: Session
):

    suppliers = db.query(
        Supplier
    ).all()

    report = []

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

        report.append({
            "supplier_id":
                supplier.id,

            "supplier_name":
                supplier.supplier_name,

            "risk_level":
                risk
        })

    return report


#Chart Data

def get_chart_data(
    db: Session
):

    suppliers = db.query(
        Supplier
    ).all()

    result = {
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

        result[risk] += 1

    return {
        "risk_distribution":
            result
    }


#Graph Visualization

def get_graph_visualization(
    db: Session
):

    graph = build_graph(db)

    nodes = []

    edges = []

    for node in graph.nodes(
        data=True
    ):
        nodes.append({
            "id": node[0],
            "name":
                node[1].get(
                    "name",
                    f"Supplier {node[0]}"
                )
        })

    for edge in graph.edges(
        data=True
    ):
        edges.append({
            "source":
                edge[0],

            "target":
                edge[1],

            "weight":
                edge[2].get(
                    "weight",
                    1
                )
        })

    return {
        "nodes":
            nodes,

        "edges":
            edges
    }


#Export Suppliers CSV

def export_suppliers_csv(
    db: Session
):

    suppliers = db.query(
        Supplier
    ).all()

    output = io.StringIO()

    writer = csv.writer(
        output
    )

    writer.writerow([
        "ID",
        "Name",
        "Country",
        "Category",
        "Reliability",
        "Lead Time"
    ])

    for supplier in suppliers:

        writer.writerow([
            supplier.id,
            supplier.supplier_name,
            supplier.country,
            supplier.category,
            supplier.reliability_score,
            supplier.lead_time_days
        ])

    return output.getvalue()


#Export Risk CSV


def export_risk_csv(
    db: Session
):

    report = generate_risk_report(
        db
    )

    output = io.StringIO()

    writer = csv.writer(
        output
    )

    writer.writerow([
        "Supplier ID",
        "Supplier Name",
        "Risk Level"
    ])

    for item in report:

        writer.writerow([
            item["supplier_id"],
            item["supplier_name"],
            item["risk_level"]
        ])

    return output.getvalue()


