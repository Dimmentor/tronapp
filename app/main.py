from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/wallet/")
def create_wallet(request: schemas.WalletRequestCreate, db: Session = Depends(get_db)):
    return crud.create_wallet_request(db=db, request=request)

@app.get("/wallet/", response_model=list[schemas.WalletRequest])
def read_wallets(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    wallets = crud.get_wallet_requests(db, skip=skip, limit=limit)
    return wallets