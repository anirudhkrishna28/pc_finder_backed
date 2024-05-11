from fastapi import FastAPI,APIRouter
from database.config import collection
from database.config import shop_collection
from models.laptop import Laptop
from models.laptop import desearialize,desearialize_list
from typing import Optional
from pydantic import Field
from bson import ObjectId



laptop_route = APIRouter()

@laptop_route.get('/lap/laptops')
async def get_laptops():
    try:
        data = collection.find({})

        if data:
            return {"laptops": desearialize_list(data)}
        else:
            return {"message": "No laptops found"}
    except Exception:
        return {"message": "Error fetching laptops"}


@laptop_route.post("/lap/add")
async def add_laptop(laptop:Laptop):
    try:
        collection.insert_one(dict(laptop))
        return {"message":"laptop added"}
    except Exception as e :
        return {"message":e}

@laptop_route.delete("/lap/delete")
async def delete_laptop(name:str):
    try:
        collection.delete_one({"name":name})
        return {"message":"laptop deleted"} 
    except Exception as e :
        return {"message":"error"}


@laptop_route.get("/lap/info")
async def get_info(name:Optional[str] = "",os:Optional[str] = "",displayres:Optional[str] = ""):
    query = {}
    if name:
        query["name"] = name
    if os:
        query["os"] = os
    if displayres:
        query["displayres"] = displayres
    data = collection.find(query)
    return {"message":desearialize_list(data)}


@laptop_route.put("/lap/update_rating")
async def update_laptop_rating(user:str,name:str,new_rating:float):
    old_rating = collection.find_one({"user":user,"name":name})
    if old_rating:
        print("found user")
        d = desearialize(old_rating) 
        x = (d["Rating"] + new_rating) / 2
        collection.update_one({"user":user,"name":name}, {"$set":{"Rating":x}})
        shop_collection.update_one({"_id": ObjectId(user), "laptops.name": name}, {"$set": {"laptops.$.Rating": x}})
        return {"message":"rating updated successfully"}
    else:
        {"message":"user or laptop not found"}
    
 