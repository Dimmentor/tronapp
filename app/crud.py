from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from tronpy import Tron


def get_wallet_info(address: str):
    try:
        tron = Tron(network='shasta')

        account = tron.get_account(address)
        balance = account.get("balance", 0) / 1_000_000
        bandwidth = account.get("bandwidth", 0)
        energy = account.get("energy", 0)

        return {
            "balance": balance,
            "bandwidth": bandwidth,
            "energy": energy,
        }
    except Exception as e:
        raise ValueError(f"Не удалось получить информацию по кошельку {address}: {e}")


def create_wallet_request(db: Session, request: schemas.WalletRequestCreate):
    try:
        wallet_info = get_wallet_info(request.address)
        db_request = models.WalletRequest(
            address=request.address,
            balance=wallet_info["balance"],
            bandwidth=wallet_info["bandwidth"],
            energy=wallet_info["energy"],
        )
        db.add(db_request)
        db.commit()
        db.refresh(db_request)
        return db_request
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=f"{ve}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Не удалось сохранить информацию в базу данных: {e}")


def get_wallet_requests(db: Session, skip: int = 0, limit: int = 10):
    try:
        return db.query(models.WalletRequest).offset(skip).limit(limit).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при выгрузке информации из базы данных: {e}")
