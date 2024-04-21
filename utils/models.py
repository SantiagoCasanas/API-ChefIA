from typing import List, Optional
from pydantic import BaseModel, Field


class Context(BaseModel):
    ingredients: List[str] = Field(min_items=1)


class Response(BaseModel):
    message: str


class IngredientResponse(BaseModel):
    ingredients: Optional[str]
