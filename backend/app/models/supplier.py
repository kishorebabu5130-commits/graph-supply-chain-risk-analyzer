#suppliers
#----------------------------------------------------
#id
#supplier_name
#country
#category
#reliability_score
#lead_time_days
#is_active
#created_at
#updated_at


from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    DateTime
)

from datetime import datetime
from app.db.database import Base
from sqlalchemy.orm import relationship

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)

    supplier_name = Column(String(255), nullable=False)

    country = Column(String(100), nullable=False)

    category = Column(String(100), nullable=False)

    reliability_score = Column(Float, default=1.0)

    lead_time_days = Column(Integer, default=7)

    is_active = Column(Boolean, default=True)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    dependencies = relationship(
        "Dependency",
        foreign_keys="Dependency.supplier_id",
        back_populates="supplier"
    )

    