from sqlalchemy.orm import Session

from app.models.supplier import Supplier
from app.models.dependency import Dependency

from app.services.graph_service import build_graph



#Dashboard Overview


def get_dashboard_overview(
    db: Session
):

    supplier_count = db.query(
        Supplier
    ).count()

    dependency_count = db.query(
        Dependency
    ).count()

    return {
        "total_suppliers":
            supplier_count,

        "total_dependencies":
            dependency_count
    }



#Network Health


def get_network_health(
    db: Session
):

    suppliers = db.query(
        Supplier
    ).all()

    if not suppliers:
        return {
            "network_health_score": 0
        }

    total = sum(
        supplier.reliability_score
        for supplier in suppliers
    )

    score = (
        total /
        len(suppliers)
    ) * 100

    return {
        "network_health_score":
            round(score, 2)
    }


#Network Resilience

def get_network_resilience(
    db: Session
):

    graph = build_graph(db)

    node_count = graph.number_of_nodes()

    edge_count = graph.number_of_edges()

    if node_count == 0:
        return {
            "resilience_score": 0
        }

    score = (
        edge_count /
        node_count
    ) * 100

    return {
        "resilience_score":
            round(score, 2)
    }



#Executive Summary

def get_executive_summary(
    db: Session
):

    overview = get_dashboard_overview(
        db
    )

    health = get_network_health(
        db
    )

    resilience = get_network_resilience(
        db
    )

    return {
        "overview":
            overview,

        "network_health":
            health,

        "network_resilience":
            resilience
    }



