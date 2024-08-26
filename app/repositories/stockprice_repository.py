from sqlalchemy import asc, desc
from sqlalchemy.orm import Session
from app.models import StockPrice   
import logging


class StockPriceRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_stock_price(self, company_id: int, date: str, open: float, high: float, low: float, close: float, adjusted_close: float, volume: int):  
        try:
            stock_price = StockPrice(
                company_id = company_id,
                date = date,
                open = open,
                high = high,
                low = low,
                close = close,
                adjusted_close = adjusted_close, 
                volume = volume
            )
            self.db.add(stock_price)
            self.db.commit()
        except Exception as e:
            print(e)
            return  
        
    
    def get_stock_prices_by_company_id(self, company_id: int):
        return self.db.query(StockPrice).filter(StockPrice.company_id == company_id).all()  
    
    def get_stock_prices_by_company_id_in_desc(self, company_id: int):
        return self.db.query(StockPrice).filter(StockPrice.company_id == company_id).order_by(desc(StockPrice.date)).all()
    
    def get_stock_prices_by_company_id_in_asc(self, company_id: int):
        return self.db.query(StockPrice).filter(StockPrice.company_id == company_id).order_by(asc(StockPrice.date)).all()   
    
    def get_stock_price_by_company_id_and_date(self, company_id: int, date: str):
        return self.db.query(StockPrice).filter(StockPrice.company_id == company_id, StockPrice.date == date).first()

    def get_adjusted_close_by_company_id(self, company_id: int):
        return self.db.query(StockPrice.adjusted_close).filter(StockPrice.company_id == company_id).all()   