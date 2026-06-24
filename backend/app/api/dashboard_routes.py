from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.services import dashboard_service

router = APIRouter()

#Overview API

@router.get(
    "/overview"
)
def dashboard_overview(
    db: Session = Depends(
        get_db
    )
):
    return dashboard_service.get_dashboard_overview(
        db
    )



#Network Health API

@router.get(
    "/network-health"
)
def network_health(
    db: Session = Depends(
        get_db
    )
):
    return dashboard_service.get_network_health(
        db
    )


#Network Resilience API

@router.get(
    "/network-resilience"
)
def network_resilience(
    db: Session = Depends(
        get_db
    )
):
    return dashboard_service.get_network_resilience(
        db
    )


#Executive Summary API

@router.get(
    "/executive-summary"
)
def executive_summary(
    db: Session = Depends(
        get_db
    )
):
    return dashboard_service.get_executive_summary(
        db
    )


