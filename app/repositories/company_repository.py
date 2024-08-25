from sqlalchemy.orm import Session
from app.models import Company

class CompanyRepository:    

    def __init__(self, db: Session):
        self.db = db 

    def create_company(self, ticker: str, name: str, ipo_date: str, current_price: float, change: float, last_update: str): 
        try:
            company = Company(
                ticker = ticker,
                name = name,
                ipo_date = ipo_date,
                current_price = current_price,
                change = change,
                last_update = last_update
            )
            self.db.add(company)
            self.db.commit()
        except Exception as e:
            print(e)
            return False
        return True

    def get_company_by_name(self, name: str):
        return self.db.query(Company).filter(Company.name == name).first()
    
    def get_company_by_ticker(self, ticker:str):
        return self.db.query(Company).filter(Company.ticker == ticker).first()
    