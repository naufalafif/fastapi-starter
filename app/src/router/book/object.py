from app.src.crud import book
from app.src.database import session_manager


def get_books(limit, skip):
    with session_manager() as db:
        return book.get_multi(db=db, limit=limit, skip=skip)
