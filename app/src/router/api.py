from fastapi import APIRouter
from .book import api as book

router = APIRouter()

router.include_router(book.router, prefix='/book', tags=['Books'])
