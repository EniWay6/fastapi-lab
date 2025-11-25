import httpx
import json
import redis.asyncio as redis
from src.config import settings

class CatService:
    API_URL = "https://catfact.ninja/fact"

    async def get_fact(self):
        # 1. Підключаємось до Redis
        client = redis.from_url(settings.REDIS_URL, encoding="utf-8", decode_responses=True)
        
        try:
            # 2. Перевіряємо кеш
            cache_key = "cat_fact_day"
            cached_fact = await client.get(cache_key)
            
            if cached_fact:
                return {"fact": cached_fact, "source": "Redis Cache ⚡"}

            # 3. Якщо кешу немає - запит до зовнішнього API
            async with httpx.AsyncClient() as http_client:
                response = await http_client.get(self.API_URL)
                data = response.json()
                fact = data.get("fact")

            # 4. Зберігаємо в Redis на 60 секунд
            await client.set(cache_key, fact, ex=60)
            
            return {"fact": fact, "source": "External API 🌍"}
            
        finally:
            await client.close()