from pydantic import BaseModel  
from datetime import datetime


class Company(BaseModel):
    id: int
    ticker: str
    name: str
    ipo_date: datetime
    current_price: float
    change: float
    last_update: datetime

    class Config:
        orm_mode = True