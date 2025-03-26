import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal, engine, Base

# Создаем тестовую базу данных
@pytest.fixture(scope="module")
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="module")
def client(test_db):
    with TestClient(app) as client:
        yield client

def test_create_wallet(client):
    response = client.post("/wallet/", json={"address": "TCesycuUXj8sYB5hW1eexf1duqzB8En3gy"})
    assert response.status_code == 200
    data = response.json()
    assert data["address"] == "TCesycuUXj8sYB5hW1eexf1duqzB8En3gy"
    assert "balance" in data
    assert "bandwidth" in data
    assert "energy" in data

def test_read_wallets(client):
    response = client.get("/wallet/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)