import datetime
from typing import Union, List
from pydantic import BaseModel, Field


class Context(BaseModel):
    ingredients: List[str] = Field(min_items=1)


class Response(BaseModel):
    message: str