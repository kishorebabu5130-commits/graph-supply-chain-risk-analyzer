from sqlalchemy.orm import Session

from app.models.supplier import Supplier
from app.schemas.supplier import (
    SupplierCreate,
    SupplierUpdate
)


def get_all_suppliers(db: Session):
    return db.query(Supplier).all()


def get_supplier_by_id(
    db: Session,
    supplier_id: int
):
    return (
        db.query(Supplier)
        .filter(Supplier.id == supplier_id)
        .first()
    )


def create_supplier(
    db: Session,
    supplier_data: SupplierCreate
):
    supplier = Supplier(
        **supplier_data.model_dump()
    )

    db.add(supplier)
    db.commit()
    db.refresh(supplier)

    return supplier


def update_supplier(
    db: Session,
    supplier_id: int,
    supplier_data: SupplierUpdate
):
    supplier = get_supplier_by_id(
        db,
        supplier_id
    )

    if not supplier:
        return None

    update_fields = supplier_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_fields.items():
        setattr(
            supplier,
            field,
            value
        )

    db.commit()
    db.refresh(supplier)

    return supplier


def delete_supplier(
    db: Session,
    supplier_id: int
):
    supplier = get_supplier_by_id(
        db,
        supplier_id
    )

    if not supplier:
        return False

    db.delete(supplier)
    db.commit()

    return True