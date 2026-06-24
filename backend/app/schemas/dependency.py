from pydantic import BaseModel


class DependencyCreate(BaseModel):
    supplier_id: int
    depends_on_supplier_id: int
    dependency_weight: float = 1.0
    dependency_type: str = "material"


class DependencyResponse(BaseModel):
    id: int
    supplier_id: int
    depends_on_supplier_id: int
    dependency_weight: float
    dependency_type: str

    model_config = {
        "from_attributes": True
    }