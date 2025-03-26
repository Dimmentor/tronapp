Микросервис на FastApi, выводящий значения кошелька в сети Tron и сохраняющий полученные значения в базу данных 

Краткий путеводитель:

1)запускаем тесты: pytest

2)запускаем сервер: uvicorn app.main:app --port 5050

3)get-запрос: http://127.0.0.1:5050/wallet/

4)пагинация в get-запросе: http://127.0.0.1:5050/wallet/?skip=0&limit=5 - пример пагинации

5)пример post-запроса на http://127.0.0.1:5050/wallet/ Передаем в body существующий кошелек с тестовым балансом shasta: 

{ "address": "TCesycuUXj8sYB5hW1eexf1duqzB8En3gy"}


Стек: FastAPI, Tronpy, SQLAlchemy+SQLite, Pytest, Uvicorn, Alembic
