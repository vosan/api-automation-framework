"""
Pydantic model for Category Details API response.
"""
from typing import List
from pydantic import BaseModel
from .promotion import Promotion

class CategoryResponse(BaseModel):
    Name: str
    CanRelist: bool
    Promotions: List[Promotion]
