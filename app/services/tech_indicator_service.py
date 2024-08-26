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
        adjusted_close = self.stockPriceRepository.get_adjusted_close_by_company_id(company_id)

        adjusted_close_df = pd.DataFrame(adjusted_close, columns=['adjusted_close', 'date'])
        
        # 이동 평균 계산
        adjusted_close_df['SMA'] = adjusted_close_df['adjusted_close'].rolling(window=window).mean()
    
        
        result = adjusted_close_df[['date', 'SMA']].dropna()
        # 결과 반환
        return result.to_dict(orient='records')
    

    def calculate_rsi(self, company_id: int, window: int):  
        adjusted_close = self.stockPriceRepository.get_adjusted_close_by_company_id(company_id)

        adjusted_close_df = pd.DataFrame(adjusted_close, columns=['adjusted_close', 'date'])
        
        # RSI 계산
        delta = adjusted_close_df['adjusted_close'].diff()    
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))

        adjusted_close_df['RSI'] = rsi    

        result = adjusted_close_df[['date', 'RSI']].dropna()

        return result.to_dict(orient='records')
    def calculate_bbands(self, company_id: int, window: int = 20, num_stdev: int = 2):
        # calculate_sma 함수에서 리스트로 반환된 값을 DataFrame으로 변환
        sma_list = self.calculate_sma(company_id, window)
        sma_df = pd.DataFrame(sma_list)

        # 표준편차를 계산하여 볼린저 밴드 상한선과 하한선을 계산합니다.
        rolling_std = sma_df['SMA'].rolling(window=window).std()
        upper_band = sma_df['SMA'] + num_stdev * rolling_std
        lower_band = sma_df['SMA'] - num_stdev * rolling_std

        # 최종 결과 DataFrame을 만듭니다.
        result = pd.DataFrame({
            'date': sma_df['date'],
            'upper_band': upper_band,
            'lower_band': lower_band
        }).dropna()

        # 결과를 dict 형식으로 변환하여 반환합니다.
        return result.to_dict(orient='records')