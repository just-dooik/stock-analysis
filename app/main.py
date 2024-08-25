from fastapi import FastAPI
from .database import engine, Base
from .services import CompanyService    
from .database import SessionLocal
from contextlib import asynccontextmanager

Base.metadata.create_all(bind=engine)

def init():
    print("Before connecting to the database")
    db = SessionLocal()  # Session 객체 생성
    try:
        print("After connecting to the database")
        companyService = CompanyService(db)
        companyService.init_all()   
        print("After initializing all")
    finally:
        db.close()  # Session 닫기
        print("Database connection closed")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 애플리케이션이 시작될 때 초기화 작업을 수행합니다.
    print("Starting application")
    init()
    yield
    # 애플리케이션이 종료될 때 종료 작업을 수행할 수 있습니다.
    print("Shutting down application")

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root():
    init()
    print("Hello World")
    return {"Hello": "World"}