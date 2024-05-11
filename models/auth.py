from pydantic import BaseModel

class Login(BaseModel):
    username:str
    password:str

class Admin(BaseModel):
    username:str
    password:str


def deserialize_admin(data):
    return {
        "_id":str(data["_id"]),
        "username":data["username"],
    }

def deserialize_user(data):
    return {
        "_id":str(data["_id"]),
        "username":data["username"],
    }