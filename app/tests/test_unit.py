import pytest
from unittest.mock import patch
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal


@pytest.fixture
def db():
    db = SessionLocal()
    models.Base.metadata.create_all(bind=db.bind)
    yield db
    models.Base.metadata.drop_all(bind=db.bind)


@patch('app.crud.get_wallet_info')
def test_create_wallet_request(mock_get_wallet_info, db: Session):
    mock_get_wallet_info.return_value = {
        "balance": 100.0,
        "bandwidth": 200,
        "energy": 300,
    }

    request_data = schemas.WalletRequestCreate(address="TCesycuUXj8sYB5hW1eexf1duqzB8En3gy")
    wallet_request = crud.create_wallet_request(db=db, request=request_data)

    assert wallet_request.id is not None
    assert wallet_request.address == "TCesycuUXj8sYB5hW1eexf1duqzB8En3gy"
    assert wallet_request.balance == 100.0
    assert wallet_request.bandwidth == 200
    assert wallet_request.energy == 300
