from sqlalchemy.orm import Session
from app.models import StockPrice   
from app.repositories import CompanyRepository 
from datetime import datetime   

class StockPriceRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def init_stock_price(self, data, company, ipo_date):
        try:
            company_id = CompanyRepository.get_company_by_ticker(self, company).id
            history = data.history(start=ipo_date, end=datetime.today().date())
            for date, price in history.items():
                stock_price = StockPrice(
                    company_id = company_id,
                    date = date.date(), 
                    open = price['Open'],   
                    high = price['High'],   
                    low = price['Low'],
                    close = price['Close'],
                    volume = round(price['Volume'])
                )
                self.db.add(stock_price)
        except Exception as e:
            print(e)
            return  
    def get_stock_prices_by_company_id(self, company_id: int):
        return self.db.query(StockPrice).filter(StockPrice.company_id == company_id).all()  
    
    def get_stock_price_by_company_id_and_date(self, company_id: int, date: str):
        return self.db.query(StockPrice).filter(StockPrice.company_id == company_id, StockPrice.date == date).first()
    
    
    