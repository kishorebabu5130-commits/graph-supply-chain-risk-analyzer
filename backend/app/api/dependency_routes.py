from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db

from app.schemas.dependency import (
    DependencyCreate,
    DependencyResponse
)

from app.services import dependency_service

router = APIRouter()

#Create Dependency

@router.post(
    "/",
    response_model=DependencyResponse
)
def create_dependency(
    dependency: DependencyCreate,
    db: Session = Depends(get_db)
):
    return dependency_service.create_dependency(
        db,
        dependency
    )

#List Dependencies

@router.get(
    "/",
    response_model=List[DependencyResponse]
)
def list_dependencies(
    db: Session = Depends(get_db)
):
    return dependency_service.get_all_dependencies(
        db
    )


