"""
file crud.py
manage CRUD and adapt model data from db to schema data to api rest
"""

from typing import Optional
from sqlalchemy.orm import Session

import models, schemas


def get_item(db: Session, item_id: int):
    # read from the database (get method read from cache)
    # return object read or None if not found
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def get_items_by_name(db: Session, name: str):
    return db.query(models.Item)            \
        .filter(models.Item.name == name)   \
        .order_by(models.Item.price)        \
        .all()


def get_items_by_partname(db: Session, name: str):
    return db.query(models.Item).filter(models.Item.name.like(f'%{name}%')).all()

def get_items_by_range_price(db: Session, price_min: Optional[int] = None, price_max: Optional[int] = None):
    if price_min is None and price_max is None:
        return None
    elif price_min is None:
        return db.query(models.Item).filter(models.Item.price <= price_max).all()
    elif price_max is None:
        return db.query(models.Item).filter(models.Item.price >= price_min).all()
    else:
        return db.query(models.Item) \
                .filter(
                    models.Item.price >= price_min,
                    models.Item.price <= price_max) \
                .all()

def create_item(db: Session, item: schemas.ItemCreate):
    # convert schema object from rest api to db model object
    db_item = models.Item(name=item.name, price=item.price, is_offer=item.is_offer)
    # add in db cache and force insert
    db.add(db_item)
    db.commit()
    # retreive object from db (to read at least generated id)
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item: schemas.Item):
    db_item = db.query(models.Item).filter(models.Item.id == item.id).first()
    if db_item is not None:
        # update data from db
        db_item.name = item.name
        db_item.price = item.price
        db_item.is_offer = item.is_offer
        # validate update in db
        db.commit()
    # return updated object or None if not found
    return db_item

def delete_item(db: Session, item_id: int):
     db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
     if db_item is not None:
         # delete object from ORM
         db.delete(db_item)
         # validate delete in db
         db.commit()
     # return deleted object or None if not found
     return db_item

