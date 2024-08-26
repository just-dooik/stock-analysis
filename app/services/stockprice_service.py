import yfinance as yf
import pandas as pd
from sqlalchemy.orm import Session
from app.repositories import StockPriceRepository, CompanyRepository
from app.src.companyList import companyList 
from datetime import datetime
import logging

class StockPriceService:
    def __init__(self, db: Session):
        self.db = db
        self.companyRepository = CompanyRepository(db)  
        self.stockPriceRepository = StockPriceRepository(db)        
    

    # stock price 데이터를 초기화하는 함수  
    # adjusted_close는 수정 종가이므로 처음에 추가가 안 된다. 추후 계산 후 집어넣어야함
    def init_stock_price(self):
        logging.info("Initializing stock price data")   
        try:
            for company in companyList:
                company_id = self.companyRepository.get_company_by_ticker(company).id
                ipo_date = self.companyRepository.get_company_by_ticker(company).ipo_date
                data = yf.download(company, start=ipo_date, end=datetime.today().date())    
                for date, price in data.iterrows():
                    if self.stockPriceRepository.get_stock_price_by_company_id_and_date(company_id, date.date()):
                        continue
                    stock_price = self.stockPriceRepository.create_stock_price(
                        company_id, 
                        date.date(),
                        float(price['Open']),
                        float(price['High']), 
                        float(price['Low']), 
                        float(price['Close']), 
                        float(price['Adj Close']),
                        int(price['Volume'])
                    )
    
        except Exception as e:
            print(e)    
            logging.error(e)
            return False



    def get_stock_prices_by_company_id(self, company_id: int):
        return self.stockPriceRepository.get_stock_prices_by_company_id(company_id)