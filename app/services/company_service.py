import yfinance as yf   
import pandas as pd
from sqlalchemy.orm import Session
from app.repositories import StockPriceRepository, CompanyRepository
from app.src.companyList import companyList 
from datetime import datetime
import logging

# 처음 데이터를 가져올 때 사용하는 함수
class CompanyService: 
    def __init__(self, db: Session):
        self.db = db
        self.companyRepository = CompanyRepository(db)
        self.stockPriceRepository = StockPriceRepository(db)   

    def init_company(self):
        print("Initializing data")  
        try:
            for company in companyList:
                if(self.companyRepository.get_company_by_ticker(company)):
                    continue
                data = yf.Ticker(company)
                ipo_date = pd.to_datetime(data.info.get('firstTradeDateEpochUtc'), unit='s').date()
                
                ticker = company
                name = data.info['shortName']
                current_price = data.info['currentPrice']
                change = round(current_price - data.info['regularMarketPreviousClose'], 2)
                last_update = datetime.today().date()
                
                self.companyRepository.create_company(ticker, name, ipo_date, current_price, change, last_update)
                
                logging.info(f"Company {name} created") 

        except Exception as e:
            print(e)
            return False    
        return True
    
    def get_companies(self):
        return self.companyRepository.get_companies()   
    
    def get_company_by_id(self, company_id: int):
        return self.companyRepository.get_company_by_id(company_id) 