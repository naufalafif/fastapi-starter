from fastapi import Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from app.src.router.security import is_authenticated
import app.src.router.book.object as book_object

router = InferringRouter()


@cbv(router)
class GeneralCBV:
    is_authenticated: bool = Depends(is_authenticated)

    @router.get("/")
    def get_books(self, skip: int = 0, limit: int = 20):
        response = book_object.get_books(skip=skip, limit=limit)
        return {
            "status": True,
            "data": response
        }

    @router.get("/{book_id}")
    def get_book(self, book_id: int):
        return {
            "status": True,
            "id": book_id
        }

    @router.post("/")
    def create_book(self):
        return {
            "status": True
        }

    @router.put("/{book_id}")
    def update_book(self, book_id: int):
        return {
            "status": True,
            "id": book_id
        }


