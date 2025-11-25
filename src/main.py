from fastapi import FastAPI
from src.users.router import router as users_router
from src.external_api.router import router as cats_router

app = FastAPI()

app.include_router(users_router)
app.include_router(cats_router)

@app.get("/")
def root():
    return {"message": "Lab works!"}