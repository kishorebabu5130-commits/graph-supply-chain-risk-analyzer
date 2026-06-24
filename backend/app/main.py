from fastapi import FastAPI

from app.db.database import (engine,Base)

from app.api import supplier_routes

from app.api import supplier_routes
from app.api import dependency_routes
from app.api import graph_routes
from app.api import prediction_routes
from app.api import analytics_routes
from app.api import dashboard_routes

from app.api import report_routes




Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Graph Supply Chain Risk Analyzer",
    version="1.0.0"
)

app.include_router(
    supplier_routes.router,
    prefix="/suppliers",
    tags=["Suppliers"]
)


@app.get("/")
def root():
    return {
        "message": "Graph Supply Chain Risk Analyzer"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }

app.include_router(
    supplier_routes.router,
    prefix="/suppliers",
    tags=["Suppliers"]
)

app.include_router(
    dependency_routes.router,
    prefix="/dependencies",
    tags=["Dependencies"]
)

app.include_router(
    graph_routes.router,
    prefix="/graph",
    tags=["Graph"]
)


app.include_router(
    prediction_routes.router,
    prefix="/predict",
    tags=["Prediction"]
)


app.include_router(
    analytics_routes.router,
    prefix="/analytics",
    tags=["Analytics"]
)

app.include_router(
    dashboard_routes.router,
    prefix="/dashboard",
    tags=["Dashboard"]
)

app.include_router(
    report_routes.router,
    prefix="/reports",
    tags=["Reports"]
)