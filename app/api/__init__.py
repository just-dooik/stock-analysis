from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.v1 import company, stockprice, tech_indicator  


api_router = APIRouter()
api_router.include_router(company.router, prefix="/company", tags=["company"])
api_router.include_router(stockprice.router, prefix="/stockprice", tags=["stockprice"]) 
api_router.include_router(tech_indicator.router, prefix="/tech_indicator", tags=["tech_indicator"]) 