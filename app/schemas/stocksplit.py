from pydantic import BaseModel  
from datetime import date

class StockSplitBase(BaseModel):
    company_id: int
    date: date
    split_ratio: float  

class StockSplitCreate(StockSplitBase):
    pass

class StockSplit(StockSplitBase):
    id: int
    created_at: date
    updated_at: date

    class Config:
        orm_mode = True
