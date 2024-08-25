from sqlalchemy.orm import Session
from app.models import StockSplit
from app.repositories import CompanyRepository
import yfinance as yf

class StockSplitRepository: 
    def __init__(self, db: Session):
        self.db = db

    # StockSplit 테이블에 데이터를 추가하는 함수    
    def init_stock_split(self, data, company, ipo_date):  
        try: 
            ticker = yf.Ticker(company) 
            company_id = CompanyRepository.get_company_by_ticker(self, company).id
            splits = ticker.splits
            for date, split_ratio in splits.items():
                split = StockSplit(
                    company_id = company_id,
                    date = date,
                    split_ratio = split_ratio
                )
                self.db.add(split)  

        except Exception as e:
            print(e)
            return False
            

    def get_stock_splits_by_company_id(self, company_id: int):
        return self.db.query(StockSplit).filter(StockSplit.company_id == company_id).all()  
    
