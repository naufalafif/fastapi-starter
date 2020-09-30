from pydantic import BaseModel
from typing import Any


class BaseResponse(BaseModel):
    status: bool
    message: str
    data: Any
