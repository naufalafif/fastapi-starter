from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from src.crud.base import CRUDBase
from src.database.models.books import Book
from src.schema.books_schema import BookCreate, BookUpdate


class CRUDItem(CRUDBase[Book, BookCreate, BookUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: BookCreate, owner_id: int
    ) -> Book:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[Book]:
        return (
            db.query(self.model)
            .filter(Book.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


book = CRUDItem(Book)
