from sqlalchemy.orm import Session

from app.models.dependency import Dependency
from app.schemas.dependency import DependencyCreate


def create_dependency(
    db: Session,
    data: DependencyCreate
):
    dependency = Dependency(
        **data.model_dump()
    )

    db.add(dependency)
    db.commit()
    db.refresh(dependency)

    return dependency


def get_all_dependencies(
    db: Session
):
    return db.query(
        Dependency
    ).all()