from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import select, Session

from app.database import get_session
from app.models.inventory import Item
from app.schemas.item import ItemCreate, ItemRead, ItemUpdate

router = APIRouter()


@router.post("/", response_model=ItemRead, status_code=201)
def create_item(item: ItemCreate, session: Session = Depends(get_session)):
    db_item = Item.from_orm(item)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


@router.get("/", response_model=list[ItemRead])
def read_items(
    skip: int = 0,
    limit: int = 100,
    session: Session = Depends(get_session),
):
    statement = select(Item).offset(skip).limit(limit)
    return session.exec(statement).all()


@router.get("/{item_id}", response_model=ItemRead)
def read_item(item_id: int, session: Session = Depends(get_session)):
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.patch("/{item_id}", response_model=ItemRead)
def update_item(
    item_id: int, item_update: ItemUpdate, session: Session = Depends(get_session)
):
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item_data = item_update.dict(exclude_unset=True)
    for key, value in item_data.items():
        setattr(item, key, value)

    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int, session: Session = Depends(get_session)):
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    session.delete(item)
    session.commit()
    return None
