from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class OrderItem(BaseModel):
    product_id: str
    quantity: int = Field(..., gt=0)


class OrderBase(BaseModel):
    user_id: str
    market_id: str
    items: List[OrderItem]
    comment: Optional[str] = None
    status: str = Field(default="pending", regex="^(pending|confirmed|delivered|cancelled)$")


class OrderCreate(OrderBase):
    pass


class OrderInDB(OrderBase):
    id: str
    created_at: datetime
    updated_at: datetime


class OrderPublic(OrderBase):
    id: str
    created_at: datetime
    updated_at: datetime


class OrderUpdate(BaseModel):
    status: Optional[str] = Field(None, regex="^(pending|confirmed|delivered|cancelled)$")
    comment: Optional[str] = None 