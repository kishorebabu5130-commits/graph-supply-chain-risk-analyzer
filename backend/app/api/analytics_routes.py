from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services import analytics_service

router = APIRouter()


@router.get("/high-risk-suppliers")
def high_risk_suppliers(
    db: Session = Depends(get_db)
):
    return analytics_service.get_high_risk_suppliers(db)


@router.get("/risk-summary")
def risk_summary(
    db: Session = Depends(get_db)
):
    return analytics_service.get_risk_summary(db)


@router.get("/top-risk-suppliers")
def top_risk_suppliers(
    db: Session = Depends(get_db)
):
    return analytics_service.get_top_risk_suppliers(db)