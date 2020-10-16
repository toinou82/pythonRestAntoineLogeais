"""
schema.py : model to be converted in json by fastapi
"""
from typing import Optional

from pydantic import BaseModel


# common Base Class for Items (abstract class)
class ItemBase(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

# item witout id, only for creation purpose
class ItemCreate(ItemBase):
    pass

# item from database with id
class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
