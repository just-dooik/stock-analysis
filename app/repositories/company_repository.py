from sqlalchemy.orm import Session
from app.models import Company

class CompanyRepository:    

    def __init__(self, db: Session):
        self.db = db

    def get_company_by_name(self, name: str):
        return self.db.query(Company).filter(Company.name == name).first()
    
    def get_company_by_ticker(self, ticker:str):
        return self.db.query(Company).filter(Company.ticker == ticker).first()
    