import pandas as pd
from sqlalchemy.orm import Session
from app.repositories import StockPriceRepository, CompanyRepository
from datetime import datetime
import logging


class TechIndicatorService:
    def __init__(self, db: Session):
        self.db = db
        self.companyRepository = CompanyRepository(db)
        self.stockPriceRepository = StockPriceRepository(db)

    def calculate_sma(self, company_id: int, window: int):
        # SQLAlchemy 객체를 받아옵니다
        stock_prices = self.stockPriceRepository.get_stock_prices_by_company_id_in_desc(company_id)
        
        # SQLAlchemy 객체에서 데이터 추출 및 DataFrame 변환
        stock_prices_dict = [sp.__dict__ for sp in stock_prices]
        
        # DataFrame으로 변환
        stock_prices_df = pd.DataFrame(stock_prices_dict)
        
        # 필요하지 않은 SQLAlchemy 내부 속성 제거
        if '_sa_instance_state' in stock_prices_df.columns:
            stock_prices_df = stock_prices_df.drop('_sa_instance_state', axis=1)
        
        # 'adjusted_close' 컬럼이 있는지 확인
        if 'adjusted_close' not in stock_prices_df.columns:
            logging.error("'adjusted_close' column not found in the data.")
            raise KeyError("'adjusted_close' column not found in the data.")
        
        # 이동 평균 계산
        stock_prices_df['SMA'] = stock_prices_df['adjusted_close'].rolling(window=window).mean()
    
        
        result = stock_prices_df[['date', 'SMA']].dropna()
        # 결과 반환
        return result.to_dict(orient='records')
    

    def calculate_rsi(self, company_id: int, window: int):  
        stock_prices = self.stockPriceRepository.get_stock_prices_by_company_id_in_desc(company_id)
        
        stock_prices_dict = [sp.__dict__ for sp in stock_prices]

        stock_prices_df = pd.DataFrame(stock_prices_dict)

        if '_sa_instance_state' in stock_prices_df.columns:
            stock_prices_df = stock_prices_df.drop('_sa_instance_state', axis=1)

        if 'adjusted_close' not in stock_prices_df.columns:
            logging.error("'adjusted_close' column not found in the data.")
            raise KeyError("'adjusted_close' column not found in the data.")
        
        # RSI 계산
        delta = stock_prices_df['adjusted_close'].diff()    
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))

        stock_prices_df['RSI'] = rsi    

        result = stock_prices_df[['date', 'RSI']].dropna()

        return result.to_dict(orient='records')
    
    

