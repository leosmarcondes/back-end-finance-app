from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated, List
#from sqlalchemy.orm import Session
from pydantic import BaseModel
#from database import SessionLocal, engine
#import models
from fastapi.middleware.cors import CORSMiddleware
from model import model

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

class TransationBase(BaseModel):
    amount: float
    category: str
    description: str
    is_income: bool
    date: str

class TransationModel(TransationBase):
    id: int

    class Config: 
        orm_mode = True

db: model = model()

@app.post("/transations/", response_model=TransationModel)
async def create_transation(transation: TransationBase, db: db): 
    
    table = db.transations
    query = db(
               (table.amount == transation.amount) &
               (table.category == transation.category) &
               (table.description == transation.description) &
               (table.is_income == transation.is_income) &
               (table.date == transation.date)
            )
    selection = query.select(table.id).first()

    if selection is None:
        id = table.insert(
            amount=transation.amount,
            category=transation.category,
            description=transation.description,
            is_income=transation.is_income,
            date=transation.date
        ) 
    else:
        id = selection.id
    
    db.commit()

    return id

@app.get("/transations/", response_model=List[TransationModel])
async def read_transations(db: db, skip: int=0, limit: int = 100):

    query = db.offset(skip).limit(limit).all()

    return query