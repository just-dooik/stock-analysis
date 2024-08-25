from sqlalchemy import Column, Integer, String, Date, Numeric
from app.database import Base
from sqlalchemy.orm import relationship 

class Company(Base):    
    __tablename__ = 'companies'
    
    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, unique=True, index=True)
    name = Column(String, index=True)      
    sector = Column(String)
    ipo_date = Column(Date)
    change = Column(Numeric)
    last_update = Column(Date)  

    stock_prices = relationship('StockPrice', back_populates='company', cascade='all, delete-orphan')   
    dividends = relationship('Dividend', back_populates='company', cascade='all, delete-orphan')    
    stock_splits = relationship('StockSplit', back_populates='company', cascade='all, delete-orphan')   