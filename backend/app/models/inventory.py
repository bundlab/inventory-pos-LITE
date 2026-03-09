from datetime import datetime
from decimal import Decimal
from typing import Optional

from sqlmodel import Field, SQLModel


class ItemBase(SQLModel):
    name: str = Field(max_length=200)
    barcode: Optional[str] = Field(default=None, max_length=100)
    price: Decimal = Field(max_digits=12, decimal_places=2)
    stock: int = Field(default=0, ge=0)


class Item(ItemBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None


class TransactionBase(SQLModel):
    item_id: int
    quantity: int
    total: Decimal
    type: str = Field(default="sale")  # sale / purchase / adjustment


class Transaction(TransactionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
