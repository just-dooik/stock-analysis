from sqlalchemy.orm import Session
from app.models import Dividend 
from app.repositories import CompanyRepository  

class DividendRepository:    

    def __init__(self, db: Session):
        self.db = db

    def init_dividend(self, data, company, ipo_date):   
        try:
            company_id = CompanyRepository.get_company_by_ticker(self, company).id
            dividends = data.dividends
            for date, dividend in dividends.items():
                dividend = Dividend(
                    company_id = company_id,
                    date = date,
                    dividend = dividend
                )
                self.db.add(dividend)  

        except Exception as e:
            print(e)
            return False    

    def get_dividends_by_company_id(self, company_id: int):
        return self.db.query(Dividend).filter(Dividend.company_id == company_id).all()

    
