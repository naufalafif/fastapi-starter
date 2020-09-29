from fastapi import FastAPI
from uvicorn import run
from src.router.api import router
from src.database.engine import Base

app = FastAPI(title='Auto Absence')
app.include_router(router)

if __name__ == '__main__':
    run(app=app)
