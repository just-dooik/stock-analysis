from pydantic import BaseModel
from datetime import date
from typing import Optional

class StockPriceBase(BaseModel):
    company_id: int 
    date: date
    open: float
    high: float
    low: float
    close: float
    adjusted_close: Optional[float] = None
    volume: int

class StockPriceCreate(StockPriceBase): 
    pass

class StockPrice(StockPriceBase):
    id: int
    created_at: date
    updated_at: date

    class Config:
        orm_mode = True