from sqlalchemy import Column, Integer, String, Float, ForeignKey

from database import Base


class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)
    address = Column(String(75), index=True)
    rating = Column(Float, index=True)

class Owner(Base):
    __tablename__ = "owners"

    id = Column(Integer, primary_key=True, index=True)
    name= Column(String(50), index=True)
    telephone = Column(String(20), index=True)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))

class MenuItem(Base):
    __tablename__ = "menuitems"

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String(50), index=True)
    description = Column(String(255), index=True)
    price = Column(Float, index=True)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))