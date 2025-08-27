from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime


class MarketBase(BaseModel):
    name: str = Field(..., max_length=200)
    description: Optional[str] = None
    contact_email: EmailStr
    contact_phone: Optional[str] = None
    address: Optional[str] = None


class MarketCreate(MarketBase):
    owner_id: str


class MarketInDB(MarketBase):
    id: str
    owner_id: str
    created_at: datetime
    updated_at: datetime


class MarketPublic(MarketBase):
    id: str
    created_at: datetime
    updated_at: datetime


class MarketUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=200)
    description: Optional[str] = None
    contact_phone: Optional[str] = None
    address: Optional[str] = None 