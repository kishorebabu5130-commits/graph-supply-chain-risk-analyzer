from pydantic import BaseModel


class SupplierRiskResponse(BaseModel):
    supplier_id: int
    supplier_name: str
    risk_score: float
    risk_level: str