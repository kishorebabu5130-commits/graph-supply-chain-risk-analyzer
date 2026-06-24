from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db

from app.schemas.supplier import (
    SupplierCreate,
    SupplierUpdate,
    SupplierResponse
)

from app.services import supplier_service

router = APIRouter()

#List Suppliers

@router.get(
    "/",
    response_model=List[SupplierResponse]
)
def list_suppliers(
    db: Session = Depends(get_db)
):
    return supplier_service.get_all_suppliers(db)


#Get Supplier

@router.get(
    "/{supplier_id}",
    response_model=SupplierResponse
)
def get_supplier(
    supplier_id: int,
    db: Session = Depends(get_db)
):
    supplier = supplier_service.get_supplier_by_id(
        db,
        supplier_id
    )

    if not supplier:
        raise HTTPException(
            status_code=404,
            detail="Supplier not found"
        )

    return supplier


#Create Supplier

@router.post(
    "/",
    response_model=SupplierResponse,
    status_code=201
)
def create_supplier(
    supplier: SupplierCreate,
    db: Session = Depends(get_db)
):
    return supplier_service.create_supplier(
        db,
        supplier
    )


#Update Supplier

@router.patch(
    "/{supplier_id}",
    response_model=SupplierResponse
)
def update_supplier(
    supplier_id: int,
    supplier: SupplierUpdate,
    db: Session = Depends(get_db)
):
    updated_supplier = (
        supplier_service.update_supplier(
            db,
            supplier_id,
            supplier
        )
    )

    if not updated_supplier:
        raise HTTPException(
            status_code=404,
            detail="Supplier not found"
        )

    return updated_supplier


#Delete Supplier

@router.delete(
    "/{supplier_id}",
    status_code=204
)
def delete_supplier(
    supplier_id: int,
    db: Session = Depends(get_db)
):
    success = supplier_service.delete_supplier(
        db,
        supplier_id
    )

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Supplier not found"
        )
    
