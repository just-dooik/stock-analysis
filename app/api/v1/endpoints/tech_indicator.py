import fastapi
from fastapi import APIRouter, Depends, HTTPException   
from app.services import TechIndicatorService   
from app.database import get_db 
from sqlalchemy.orm import Session  

router = APIRouter()    

def get_tech_indicator_service(db: Session = Depends(get_db)):
    return TechIndicatorService(db)


@router.get("/sma/{company_id}/{window}", response_model=list)
async def get_sma(company_id: int, window: int, techIndicatorService: TechIndicatorService = Depends(get_tech_indicator_service)):  
    return techIndicatorService.calculate_sma(company_id, window)


@router.get("/rsi/{company_id}/{window}", response_model=list)  
async def get_rsi(company_id: int, window: int, techIndicatorService = Depends(get_tech_indicator_service)):      
    return techIndicatorService.calculate_rsi(company_id, window)   

@router.get("/bbands/{company_id}/{window}/{stdev}", response_model=list)   
async def get_bbands(company_id: int, window: int, stdev: int, techIndicatorService = Depends(get_tech_indicator_service)):      
    return techIndicatorService.calculate_bbands(company_id, window, stdev)    