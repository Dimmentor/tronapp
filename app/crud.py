from sqlalchemy.orm import Session
from . import models, schemas
from tronpy import Tron


def get_wallet_info(address: str):
    # Подключаемся к тестовой сети Shasta
    tron = Tron(network='shasta')

    # Получаем информацию о кошельке
    account = tron.get_account(address)

    # Проверяем наличие необходимых ключей
    balance = account.get("balance", 0) / 1_000_000  # Преобразуем в TRX, если ключ отсутствует, используем 0
    bandwidth = account.get("bandwidth", 0)  # Если ключ отсутствует, используем 0
    energy = account.get("energy", 0)  # Если ключ отсутствует, используем 0

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