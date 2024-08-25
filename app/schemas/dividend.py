from pydantic import BaseModel  
from datetime import date

class DividendBase(BaseModel):      
    company_id: int
    date: date
    dividend: float 

class DividendCreate(DividendBase):
    pass

class Dividend(DividendBase):   
    id: int
    created_at: date    
    updated_at: date    

    class Config: 
        orm_mode = True 
        