from sqlalchemy import Column, Integer, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship 
from app.database import Base

class StockPrice(Base):
    __tablename__ = 'stock_prices'
    id = Column(Integer, primary_key=True, index=True)  
    company_id = Column(Integer, ForeignKey('companies.id'))    
    date = Column(Date, index=True) 
    open = Column(Numeric)
    high = Column(Numeric)  
    low = Column(Numeric)
    close = Column(Numeric)
    adjusted_close = Column(Numeric)
    volume = Column(Integer)

    company = relationship('Company', back_populates='stock_prices')    

