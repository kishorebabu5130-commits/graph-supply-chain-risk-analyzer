#predictions
#---------------------------------------------------
#id
#supplier_id
#risk_score
#risk_level
#confidence
#model_version
#predicted_at


from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    ForeignKey,
    DateTime
)

from datetime import datetime

from app.db.database import Base


class Prediction(Base):
    __tablename__ = "predictions"

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

    risk_score = Column(
        Float,
        nullable=False
    )

    risk_level = Column(
        String(50),
        nullable=False
    )

    confidence = Column(
        Float,
        nullable=False
    )

    model_version = Column(
        String(50),
        default="1.0"
    )

    predicted_at = Column(
        DateTime,
        default=datetime.utcnow
    )