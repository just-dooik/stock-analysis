from pydantic import BaseModel
from datetime import date

class StockPrice(BaseModel):
    company_id: int 
    date: date
    open: float
    high: float
    low: float
    close: float
    adjusted_close: float
    volume: int

    class Config: 
        orm_mode = True 