from typing import Optional

from pydantic import BaseModel


# Shared properties
class BookBase(BaseModel):
    title: Optional[str] = None
    isbn: Optional[str] = None


# Properties to receive on item creation
class BookCreate(BookBase):
    title: str
    isbn: str


# Properties to receive on item update
class BookUpdate(BookBase):
    pass


