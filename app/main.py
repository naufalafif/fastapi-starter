from fastapi import FastAPI
from uvicorn import run
from app.src.router.api import router
from app.src.database.engine import Base
from app.src.core import config

app = FastAPI(title=config.PROJECT_NAME)
app.include_router(router)

if __name__ == '__main__':
    run(app=app)
