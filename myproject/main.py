import os

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
import crud
from database import SessionLocal, engine

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/restaurants", response_model=schemas.Restaurant)
def create_restaurant(restaurant: schemas.RestaurantCreate, db: Session = Depends(get_db)):
    return crud.create_restaurant(db=db, restaurant=restaurant)

@app.get("/restaurants/", response_model=list[schemas.Restaurant])
def read_restaurants(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    restaurants = crud.get_restaurants(db, skip, limit)
    return restaurants

@app.get("/restaurants/{restaurant_id}", response_model=schemas.Restaurant)
def read_restaurants(restaurant_id: int, db: Session = Depends(get_db)):
    db_restaurant = crud.get_restaurant(db, restaurant_id=restaurant_id)
    if db_restaurant is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_restaurant

@app.post("/owners", response_model=schemas.Owner)
def create_owner(owner: schemas.OwnerCreate, db: Session = Depends(get_db)):
    return crud.create_owner(db=db, owner=owner)

@app.get("/owners/", response_model=list[schemas.Owner])
def read_owners(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    owners = crud.get_owners(db, skip, limit)
    return owners

@app.post("/menuitems", response_model=schemas.MenuItem)
def create_menu_item(menu_item: schemas.MenuItemCreate, db: Session = Depends(get_db)):
    return crud.create_menu_item(db=db, menu_item=menu_item)

@app.get("/menuitems/{restaurant_id}", response_model=list[schemas.MenuItem])
def read_menu_items(restaurant_id: int, db: Session = Depends(get_db)):
    menu_items = crud.get_menu_items(db, restaurant_id)
    return menu_items