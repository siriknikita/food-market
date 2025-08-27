from pydantic import BaseModel, EmailStr, Field
from typing import Literal, Optional
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr
    name: str = Field(..., max_length=100)
    role: Literal["customer", "market_admin", "super_admin"] = "customer"
    locale: Literal["en", "ua"] = "en"


class UserCreate(UserBase):
    password: str = Field(..., min_length=8)


class UserInDB(UserBase):
    id: str
    hashed_password: str
    created_at: datetime
    updated_at: datetime


class UserPublic(UserBase):
    id: str
    created_at: datetime
    updated_at: datetime


class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    locale: Optional[Literal["en", "ua"]] = None 