from sqlalchemy import Column, Integer, Date, Numeric, ForeignKey   
from sqlalchemy.orm import relationship
from app.database import Base

class Dividend(Base):
    __tablename__ = 'dividends'
    id = Column(Integer, primary_key=True, index=True)  
    company_id = Column(Integer, ForeignKey('companies.id'))    
    date = Column(Date, index=True)
    dividend = Column(Numeric)   
    company = relationship('Company', back_populates='dividends')