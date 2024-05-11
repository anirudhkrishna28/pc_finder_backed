from fastapi import FastAPI,APIRouter
from models.auth import Admin
from database.config import owner_collection,user_collection
from models.auth import deserialize_admin,deserialize_user

owner_route =  APIRouter(tags=["owner"])
login_route = APIRouter(tags=["user"])



@owner_route.post("/owner/register")
async def add_owner(admin:Admin):
    print(admin)
    admin = dict(admin)
    
    data = owner_collection.find_one({"username":admin["username"]})
    if not data:
        owner_collection.insert_one(admin)
        x = owner_collection.find_one({"username":admin["username"]})
        return {"message":"owner added successfully","owner":deserialize_admin(x)}
    else:
        return {"message":"owner already exists"}
    

@owner_route.post("/owner/login")
async def login_owner(admin:Admin):
    data = owner_collection.find_one(dict(admin))
    if data:
        return {"message":"login successful","owner":deserialize_admin(data)}
    else:
        return {"message":"login failed"}
    


@login_route.post("/user/register")
async def add_owner(admin:Admin):
    # print(admin)
    admin = dict(admin)
    
    data = user_collection.find_one({"username":admin["username"]})
    if not data:
        user_collection.insert_one(admin)
        x = user_collection.find_one({"username":admin["username"]})
        return {"message":"user added successfully","user":deserialize_user(x)}
    else:
        return {"message":"user already exists"}
    

@login_route.post("/user/login")
async def login_owner(admin:Admin):
    data = user_collection.find_one(dict(admin))
    if data:
        return {"message":"login successful","user":deserialize_user(data)}
    else:
        return {"message":"login failed"}

