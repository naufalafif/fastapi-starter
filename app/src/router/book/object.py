from app.src.crud import book
from app.src.database import session_manager
from app.src.schema import BookCreate


def get_books(limit, skip):
    with session_manager() as db:
        return book.get_multi(db=db, limit=limit, skip=skip)


def get_book(book_id):
    with session_manager() as db:
        return book.get(db=db, id=book_id)


def create_book(book_data: BookCreate):
    with session_manager() as db:
        created_book = book.create(db=db, obj_in=book_data)
        return created_book
