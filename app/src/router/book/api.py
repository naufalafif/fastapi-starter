from fastapi import Depends, Response, status
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from app.src.router.security import is_authenticated
import app.src.router.book.object as book_object
from app.src.router.response import BaseResponse
from app.src.utils.response_builder import ResponseBuilder
from app.src.utils.json_util import sql_object_to_dict
from app.src.schema import BookCreate

router = InferringRouter()


@cbv(router)
class GeneralCBV:
    is_authenticated: bool = Depends(is_authenticated)
    res: Response

    @router.get("/", response_model=BaseResponse)
    def get_books(self, skip: int = 0, limit: int = 20):
        responses = ResponseBuilder()
        books = book_object.get_books(skip=skip, limit=limit)
        responses.message = "successfully fetch books data"
        responses.status = True
        responses.data = [sql_object_to_dict(book) for book in books]
        return responses.to_dict()

    @router.get("/{book_id}", response_model=BaseResponse)
    def get_book(self, book_id: int):
        responses = ResponseBuilder()

        book = book_object.get_book(book_id=book_id)
        if book is None:
            responses.message = "book not found"
            responses.status = False
            self.res.status_code = status.HTTP_404_NOT_FOUND
            return responses.to_dict()

        responses.message = f"successfully fetch book {book_id} data"
        responses.status = True
        responses.data = sql_object_to_dict(book)
        return responses.to_dict()

    @router.post("/", response_model=BaseResponse)
    def create_book(self, data: BookCreate):
        responses = ResponseBuilder()

        created_book = book_object.create_book(book_data=data)
        responses.message = f"book {data.title} successfully created"
        responses.status = True
        responses.data = sql_object_to_dict(created_book)
        return responses.to_dict()
