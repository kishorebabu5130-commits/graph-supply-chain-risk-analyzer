from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.db.database import Base


class Dependency(Base):
    __tablename__ = "dependencies"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    supplier_id = Column(
        Integer,
        ForeignKey("suppliers.id"),
        nullable=False
    )

    depends_on_supplier_id = Column(
        Integer,
        ForeignKey("suppliers.id"),
        nullable=False
    )

    dependency_weight = Column(
        Float,
        default=1.0
    )

    dependency_type = Column(
        String(100),
        default="material"
    )

    supplier = relationship(
        "Supplier",
        foreign_keys=[supplier_id],
        back_populates="dependencies"
    )

    depends_on = relationship(
        "Supplier",
        foreign_keys=[depends_on_supplier_id]
    )