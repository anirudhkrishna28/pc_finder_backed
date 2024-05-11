from fastapi import APIRouter
from pydantic import BaseModel
from models.laptop import Laptop
from database.config import shop_collection
from typing import Optional
from models.shop import Shop,desearialize_shop,desearialize_shop_list
from bson import ObjectId
import routes.laptoproute as lr
from database.config import collection


shop_route = APIRouter()


@shop_route.get("/shop/{id}")
async def get_owner(id: str):
    print(id)
    data = shop_collection.find({"id": id})
    d = desearialize_shop_list(data)
    if len(d) > 0:
        return d
    else:
        return {"error": "Shop not found"}

@shop_route.post("/shop/add")
async def add_shop(shop:Shop):
    existing_shop = shop_collection.find_one({"name": shop.name, "id": shop.id})
    print("exist:",existing_shop)
    if existing_shop:
        print("already exists")
        return {"error": "Shop already exists"}
    else:
        print("inserted")
        shop_collection.insert_one(dict(shop))
        return {"message":"Shop inserted successfully"}

@shop_route.post("/shop/add_laptop")
async def add_laptop(laptop: Laptop):
    existing_laptop_shop = shop_collection.find_one({"id": laptop.user})
    if existing_laptop_shop and any(l["user"] == laptop.user for l in existing_laptop_shop.get("laptops", [])):
        return {"message": "Laptop already exists in shop_collection"}

    existing_laptop = collection.find_one({"id": laptop.user})
    if existing_laptop:
        return {"message": "Laptop already exists in collection"}

    shop_collection.update_one({"id": laptop.user}, {"$push": {"laptops": dict(laptop)}})
    collection.insert_one(dict(laptop))
    return {"message": "Laptop added successfully"}


@shop_route.delete("/shop/delete")
async def del_laptop(user:str,laptop:Laptop):
    shop_collection.update_one({"_id":ObjectId(user)}, {"$pull":{"laptops":dict(laptop)}})
     
    return {"message":"laptop deleted successfully"}

@shop_route.get("/shop/get/laptops")
async def get_laptops(user:str):
    data = shop_collection.find_one({"_id":ObjectId(user)})
    if data:
        return {"laptops":desearialize_shop(data)["laptops"]}
    else:
        return {"message":"unable to find data"}
    

@shop_route.put("/shop/update-rating")
async def update_shop_rating(user:str,new_rating:float):
    try:
        
        x = shop_collection.find_one({"_id":ObjectId(user)})
        y = 0
        if x["rating"] > 0:
            y = (x["rating"] + new_rating)/2
        else:
            y = new_rating
        shop_collection.update_one({"_id":ObjectId(user)},{"$set":{"rating":y}})
        return {"message":"rating updated successfully"}
    except:
        return {"message":"error updating the data"}