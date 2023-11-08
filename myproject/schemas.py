from pydantic import BaseModel

class RestaurantBase(BaseModel):
    name: str
    address: str
    rating: float

class RestaurantCreate(RestaurantBase):
    pass

class Restaurant(RestaurantBase):
    id: int

    class Config:
        orm_mode = True

class OwnerBase(BaseModel):
    name: str
    telephone: str
    restaurant_id: int

class OwnerCreate(OwnerBase):
    pass

class Owner(OwnerBase):
    id: int

    class Config:
        orm_mode = True

class MenuItemBase(BaseModel):
    item_name: str
    description: str
    price: float
    restaurant_id: int

class MenuItemCreate(MenuItemBase):
    pass

class MenuItem(MenuItemBase):
    id: int

    class Config:
        orm_mode = True