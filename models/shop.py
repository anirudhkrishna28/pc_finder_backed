from fastapi import APIRouter
from pydantic import BaseModel
shop_router = APIRouter()
from models.laptop import Laptop
from database.config import shop_collection
from typing import Optional

class Shop(BaseModel):
    name:str
    id:str
    admin:bool
    description:str
    location:str
    rating:float
    mobile_no:int
    photo_url:str
    laptops:Optional[list[Laptop]]


def desearialize_shop(data):
    return {
        "name": data["name"],
        "id" : data["id"],
        "admin": data["admin"],
        "description": data["description"],
        "location": data["location"],
        "rating": data["rating"],
        "mobile_no": data["mobile_no"],
        "photo_url": data["photo_url"],
        "laptops": [laptop for laptop in data["laptops"] ]
    }

def desearialize_shop_list(data):
    return [desearialize_shop(shop) for shop in data]
