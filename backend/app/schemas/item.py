from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    barcode: Optional[str] = None
    price: Decimal = Field(..., gt=0)
    stock: int = Field(..., ge=0)


class ItemCreate(ItemBase):
    pass


class ItemUpdate(BaseModel):
    name: Optional[str] = None
    barcode: Optional[str] = None
    price: Optional[Decimal] = None
    stock: Optional[int] = None


class ItemRead(ItemBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
