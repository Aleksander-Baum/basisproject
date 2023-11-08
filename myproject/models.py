from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    address = Column(String, index=True)
    rating = Column(Float, index=True)

    items = relationship("MenuItem", back_populates="restaurants")

class Owner(Base):
    __tablename__ = "owners"

    id = Column(Integer, primary_key=True, index=True)
    name= Column(String, index=True)
    telephone = Column(String, index=True)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))

class MenuItem(Base):
    __tablename__ = "menuitems"

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float, index=True)

    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))

    restaurants = relationship("Restaurant", back_populates="items")
