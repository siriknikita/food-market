from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class ProductBase(BaseModel):
    market_id: str
    name: str = Field(..., max_length=200)
    description: Optional[str] = None
    price: float = Field(..., gt=0)
    stock_quantity: int = Field(..., ge=0)
    category: str
    sub_category: Optional[str] = None
    tags: List[str] = []
    images: List[str] = []


class ProductCreate(ProductBase):
    pass


class ProductInDB(ProductBase):
    id: str
    created_at: datetime
    updated_at: datetime


class ProductPublic(ProductBase):
    id: str
    created_at: datetime
    updated_at: datetime


class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=200)
    description: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    stock_quantity: Optional[int] = Field(None, ge=0)
    category: Optional[str] = None
    sub_category: Optional[str] = None
    tags: Optional[List[str]] = None
    images: Optional[List[str]] = None 