from sqlalchemy.orm import Session
from app.models import StockPrice   

class StockPriceRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_stock_prices_by_company_id(self, company_id: int):
        return self.db.query(StockPrice).filter(StockPrice.company_id == company_id).all()  
    
    def get_stock_price_by_company_id_and_date(self, company_id: int, date: str):
        return self.db.query(StockPrice).filter(StockPrice.company_id == company_id, StockPrice.date == date).first()
    
    
    