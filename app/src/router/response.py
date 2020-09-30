from pydantic import BaseModel
from typing import Any, List, Optional


class BaseResponse(BaseModel):
    status: bool
    message: str
    data: Any
    errors: Optional[List]
