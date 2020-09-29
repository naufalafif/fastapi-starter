from src.crud.crud_book import book
from src.database.session import session_manager


def get_books(limit, skip):
    with session_manager() as db:
        return book.get_multi(db=db, limit=limit, skip=skip)
