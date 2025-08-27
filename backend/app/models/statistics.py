from pydantic import BaseModel
from typing import List


class ProductStats(BaseModel):
    product_id: str
    product_name: str
    total_orders: int
    total_sold: int
    revenue: float


class MarketStats(BaseModel):
    market_id: str
    market_name: str
    total_orders: int
    total_revenue: float
    top_products: List[ProductStats]


class UserStats(BaseModel):
    user_id: str
    total_orders: int
    total_spent: float
    favorite_markets: List[str] 