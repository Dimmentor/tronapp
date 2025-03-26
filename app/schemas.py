from pydantic import BaseModel
from pydantic import ConfigDict


class WalletRequestBase(BaseModel):
    address: str
    # balance: float
    # bandwidth: float
    # energy: float


class WalletRequestCreate(WalletRequestBase):
    pass


class WalletRequest(WalletRequestBase):
    id: int
    balance: float
    bandwidth: float
    energy: float

    model_config = ConfigDict(from_attributes=True)
