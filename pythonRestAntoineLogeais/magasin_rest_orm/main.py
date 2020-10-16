from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: Optional[int] = 0, limit: Optional[int] = 100, db: Session = Depends(get_db)):
    # read items from database
    items = crud.get_items(db, skip=skip, limit=limit)
    # return them as json
    return items

@app.get("/items/by_id/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item to read not found")
    return db_item

@app.get("/items/by_name", response_model=List[schemas.Item])
def read_items_by_name(n: Optional[str] = None, db: Session = Depends(get_db)):
    # read items from database
    items = crud.get_items_by_name(db=db, name=n)
    # return them as json
    return items

@app.get("/items/by_partname", response_model=List[schemas.Item])
def read_items_by_partname(n: Optional[str] = None, db: Session = Depends(get_db)):
    # read items from database
    items = crud.get_items_by_partname(db=db, name=n)
    # return them as json
    return items

@app.get("/items/by_price", response_model=List[schemas.Item])
def read_items_by_price(pmin: Optional[float] = None,
                           pmax: Optional[float] = None,
                           db: Session = Depends(get_db)):
    # read items from database
    items = crud.get_items_by_range_price(db=db, price_min=pmin, price_max=pmax)
    if items is None:
        raise HTTPException(status_code=404, detail="Item for empty range price not found")
    # return them as json
    return items

@app.post("/items/", response_model=schemas.Item)
def create_user(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    # receive json item without id and return json item from database with new id
    return crud.create_item(db=db, item=item)

@app.put("/items/", response_model=schemas.Item)
def update_item(item: schemas.Item, db: Session = Depends(get_db)):
    db_item = crud.update_item(db, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item to update not found")
    return db_item

@app.delete("/items/{item_id}", response_model=schemas.Item)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item to delete not found")
    return db_item



