from typing import Optional

from pydantic import BaseModel


# Shared properties
class BookBase(BaseModel):
    title: Optional[str] = None
    isbn: Optional[str] = None


class BookCreate(BookBase):
    title: str
    isbn: str


class BookUpdate(BookBase):
    pass
