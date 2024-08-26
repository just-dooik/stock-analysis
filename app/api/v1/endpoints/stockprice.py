import fastapi
from fastapi import APIRouter, Depends, HTTPException   
from app.services import StockPriceService  
from app.schemas import StockPrice
from app.database import get_db 
from sqlalchemy.orm import Session  

router = APIRouter()

@router.get("/{company_id}", response_model=list[StockPrice])   
async def get_stock_prices_by_company_id(company_id: int, db: Session = Depends(get_db)):  
    stockPriceService = StockPriceService(db)
    stock_prices = stockPriceService.get_stock_prices_by_company_id(company_id)
    if stock_prices is None:
        raise HTTPException(status_code=404, detail="Stock prices not found")
    return stock_prices