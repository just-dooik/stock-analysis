from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .database import engine, Base  

Base.metadata.create_all(bind=engine)


app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}
