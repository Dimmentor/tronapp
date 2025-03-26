from sqlalchemy import Column, Integer, String, Float
from .database import Base


class WalletRequest(Base):
    __tablename__ = "wallet_requests"

    id = Column(Integer, primary_key=True, index=True)  # порядковый номер запроса
    address = Column(String, index=True)  # номер кошелька
    balance = Column(Float)
    bandwidth = Column(Float)
    energy = Column(Float)
