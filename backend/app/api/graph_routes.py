from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.services import graph_service

router = APIRouter()


#Graph Endpoint 

@router.get("/")
def get_graph(
    db: Session = Depends(get_db)
):
    return graph_service.get_graph_data(
        db
    )


#Centrality Endpoint

@router.get("/centrality")
def centrality(
    db: Session = Depends(get_db)
):
    return graph_service.get_centrality_metrics(
        db
    )


