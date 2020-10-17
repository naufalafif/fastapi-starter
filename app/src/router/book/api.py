from fastapi import Depends, Response, status, HTTPException
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from app.src.router.security import is_authenticated
import app.src.router.book.object as book_object
from app.src.schema import books_schema as schema
from typing import List

router = InferringRouter()


@cbv(router)
class BookClassView:
    is_authenticated: bool = Depends(is_authenticated)
    res: Response

    @router.get("/", response_model=List[schema.BookInDB])
    def get_books(self, skip: int = 0, limit: int = 20):
        books = book_object.get_books(skip=skip, limit=limit)
        return books

    @router.get("/{book_id}", response_model=schema.BookInDB)
    def get_book(self, book_id: int):
        book = book_object.get_book(book_id=book_id)
        if book is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="data not found")
        return book

    @router.post("/", response_model=schema.BookInDB)
    def create_book(self, data: schema.BookCreate):
        created_book = book_object.create_book(book_data=data)
        return created_book
