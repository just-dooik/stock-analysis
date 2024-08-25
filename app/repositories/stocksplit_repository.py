from sqlalchemy.orm import Session
from app.models import StockSplit

class StockSplitRepository: 
    def __init__(self, db: Session):
        self.db = db

    def get_stock_splits_by_company_id(self, company_id: int):
        return self.db.query(StockSplit).filter(StockSplit.company_id == company_id).all()  
    