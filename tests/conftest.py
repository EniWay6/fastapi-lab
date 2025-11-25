import os

import fakeredis.aioredis
import pytest
from fastapi.testclient import TestClient

from src.main import app

# Щоб тести не лізли в справжню базу, можна встановити режим тестування
os.environ["TESTING"] = "1"


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def mock_redis(monkeypatch):
    # Створюємо фейковий Redis
    fake_r = fakeredis.aioredis.FakeRedis(decode_responses=True)

    # Підміняємо функцію get_redis в модулі, де вона використовується
    # УВАГА: Перевір шлях src.external_api.service.redis.from_url якщо ти використовуєш інший підхід
    # Найпростіше мокати саме залежність, якщо вона використовується в роутері
    return fake_r
