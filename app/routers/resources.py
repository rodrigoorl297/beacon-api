from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.db import get_db
from app.models import Service
from app.schemas import ServiceIn, ServiceOut

router = APIRouter(prefix="/services", tags=["services"])


@router.get("", response_model=list[ServiceOut])
def list_items(db: Session = Depends(get_db), _: str = Depends(get_current_user)):
    return db.query(Service).order_by(Service.id.desc()).all()


@router.post("", response_model=ServiceOut, status_code=status.HTTP_201_CREATED)
def create_item(body: ServiceIn, db: Session = Depends(get_db), _: str = Depends(get_current_user)):
    row = Service(**body.model_dump())
    db.add(row)
    db.commit()
    db.refresh(row)
    return row


@router.get("/{item_id}", response_model=ServiceOut)
def get_item(item_id: int, db: Session = Depends(get_db), _: str = Depends(get_current_user)):
    row = db.get(Service, item_id)
    if not row:
        raise HTTPException(status_code=404, detail="not found")
    return row
