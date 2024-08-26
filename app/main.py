from fastapi import FastAPI
from .database import engine, Base
from .services import CompanyService, StockPriceService
from .database import SessionLocal
from contextlib import asynccontextmanager
from app.api import api_router
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.FileHandler("app.log")

Base.metadata.create_all(bind=engine)

def init():
    logging.info("Initializing data")
    db = SessionLocal()  # Session 객체 생성
    try:
        logging.info("Connecting to the database")  
        companyService = CompanyService(db)
        stockPriceService = StockPriceService(db)   
        companyService.init_company()
        stockPriceService.init_stock_price()
        logging.info("Data initialized")    
    finally:
        db.close()  # Session 닫기
        logging.info("Database connection closed")  

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 애플리케이션이 시작될 때 초기화 작업을 수행합니다.
    logging.info("Application startup")
    init()
    yield
    # 애플리케이션이 종료될 때 종료 작업을 수행할 수 있습니다.
    logging.info("Application shutdown")    

app = FastAPI(lifespan=lifespan)

app.include_router(api_router)