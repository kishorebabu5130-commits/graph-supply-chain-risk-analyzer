from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class SupplierCreate(BaseModel):
    supplier_name: str
    country: str
    category: str

    reliability_score: float = Field(
        default=0.9,
        ge=0.0,
        le=1.0
    )

    lead_time_days: int = Field(
        default=7,
        ge=1
    )

    is_active: bool = True


class SupplierUpdate(BaseModel):
    supplier_name: Optional[str] = None
    country: Optional[str] = None
    category: Optional[str] = None
    reliability_score: Optional[float] = None
    lead_time_days: Optional[int] = None
    is_active: Optional[bool] = None


class SupplierResponse(BaseModel):
    id: int
    supplier_name: str
    country: str
    category: str
    reliability_score: float
    lead_time_days: int
    is_active: bool
    created_at: datetime

    model_config = {
        "from_attributes": True
    }