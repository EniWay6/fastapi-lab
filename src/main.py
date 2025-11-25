from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.core.logging.logging_config import setup_logging
from src.core.logging.sentry import init_sentry
from src.external_api.router import router as cats_router
from src.users.router import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Запуск логування
    init_sentry()
    setup_logging()
    yield


app = FastAPI(lifespan=lifespan)

app = FastAPI()

app.include_router(users_router)
app.include_router(cats_router)


@app.get("/")
def root():
    return {"message": "Lab works!"}
