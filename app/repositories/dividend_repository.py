from sqlalchemy.orm import Session
from app.models import Dividend 

class DividendRepository:    

    def __init__(self, db: Session):
        self.db = db

    def get_dividends_by_company_id(self, company_id: int):
        return self.db.query(Dividend).filter(Dividend.company_id == company_id).all()

    
