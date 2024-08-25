from pydantic import BaseModel  
from datetime import date

class CompanyBase(BaseModel):
    ticker: str
    name: str
    ipo_date: date
    change: float


class CompanyCreate(CompanyBase):
    pass    

class Company(CompanyBase):
    id: int
    created_at: date
    updated_at: date

    class Config:
        orm_mode = True 