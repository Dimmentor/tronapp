from sqlalchemy.orm import Session
from . import models, schemas
from tronpy import Tron


def get_wallet_info(address: str):
    # Тестовая сеть
    tron = Tron(network='shasta')

    account = tron.get_account(address)
    # при отсутствии возвращает 0
    balance = account.get("balance", 0)
    bandwidth = account.get("bandwidth", 0)
    energy = account.get("energy", 0)

    return {
        "balance": balance,
        "bandwidth": bandwidth,
        "energy": energy,
    }


def create_wallet_request(db: Session, request: schemas.WalletRequestCreate):
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


def get_wallet_requests(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.WalletRequest).offset(skip).limit(limit).all()
