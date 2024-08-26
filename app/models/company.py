from sqlalchemy import Column, Integer, String, Date, Numeric
from app.database import Base
from sqlalchemy.orm import relationship 

class Company(Base):    
    __tablename__ = 'companies'
    
    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, unique=True, index=True)
    name = Column(String, index=True)      
    ipo_date = Column(Date)
    current_price = Column(Numeric)
    change = Column(Numeric)
    last_update = Column(Date)

    stock_prices = relationship('StockPrice', back_populates='company', cascade='all, delete-orphan')   