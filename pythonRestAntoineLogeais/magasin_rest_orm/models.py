"""
model.py : database row <-> objet python
"""
from sqlalchemy import Boolean, Column, Integer, String, Numeric
    #, ForeignKey
#from sqlalchemy.orm import relationship

from database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=150), nullable=False)
    price = Column(Numeric(precision=5, scale=2), nullable=False)
    is_offer = Column(Boolean, nullable=True)
