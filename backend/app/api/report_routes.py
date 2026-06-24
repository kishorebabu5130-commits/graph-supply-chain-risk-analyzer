from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from fastapi.responses import Response

from app.db.database import get_db

from app.services import report_service

router = APIRouter()


#Risk Report API

@router.get(
    "/risk-report"
)
def risk_report(
    db: Session = Depends(
        get_db
    )
):
    return report_service.generate_risk_report(
        db
    )


#Chart Data API

@router.get(
    "/chart-data"
)
def chart_data(
    db: Session = Depends(
        get_db
    )
):
    return report_service.get_chart_data(
        db
    )

#Graph Visualization API

@router.get(
    "/graph-visualization"
)
def graph_visualization(
    db: Session = Depends(
        get_db
    )
):
    return report_service.get_graph_visualization(
        db
    )


#Export Suppliers CSV

@router.get(
    "/export/suppliers"
)
def export_suppliers(
    db: Session = Depends(
        get_db
    )
):

    csv_data = (
        report_service
        .export_suppliers_csv(
            db
        )
    )

    return Response(
        content=csv_data,
        media_type="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=suppliers.csv"
        }
    )


#Export Risk CSV


@router.get(
    "/export/risk-report"
)
def export_risk_report(
    db: Session = Depends(
        get_db
    )
):

    csv_data = (
        report_service
        .export_risk_csv(
            db
        )
    )

    return Response(
        content=csv_data,
        media_type="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=risk_report.csv"
        }
    )


