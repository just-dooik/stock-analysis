import fastapi
from fastapi import APIRouter, Depends, HTTPException   
from app.services import CompanyService
from app.schemas import Company 
from app.database import get_db 
from sqlalchemy.orm import Session  

router = APIRouter()


@router.get("/", response_model=list[Company])
async def get_companies(db: Session = Depends(get_db)):
    companyService = CompanyService(db)  
    return companyService.get_companies()


@router.get("/{id}", response_model=Company)
async def get_company(id: int, db: Session = Depends(get_db)):  
    companyService = CompanyService(db)
    company = companyService.get_company_by_id(id)
    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return company
