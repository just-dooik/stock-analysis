from sqlalchemy import Column, Integer, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship 
from app.database import Base

class StockSplit(Base):
    __tablename__ = 'stock_splits'  
    id = Column(Integer, primary_key=True, index=True)  
    company_id = Column(Integer, ForeignKey('companies.id'))    
    date = Column(Date, index=True)
    split_ratio = Column(Numeric)   
    company = relationship('Company', back_populates='stock_splits')    
    