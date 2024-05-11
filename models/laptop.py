from typing import Optional
from pydantic import BaseModel,Field

class Laptop(BaseModel):

    name: Optional[str]
    user:Optional[str]
    budget: Optional[int] = Field(default=0,description="this is the budget of the laptop eg(100000)")
    os: Optional[str]
    primary_use: Optional[str]
    description:Optional[str]
    image_url: Optional[str]
    battery: Optional[int]
    ram: Optional[int]
    storage: Optional[str]
    displaysize: Optional[int]
    displayres: Optional[str]
    weight: Optional[float]
    Rating: float
    Processor: Optional[str]
    url: Optional[str]


def desearialize(data) -> dict:
    return {
            "id" : str(data["_id"]),
            "user":data["user"],
            "name": data["name"],
            "budget": data["budget"],
            "os": data["os"],
            "primary_use": data["primary_use"],
            "description": data["description"],
            "image_url":  data["image_url"],
            "battery": data["battery"],
            "ram": data["ram"],
            "storage": data["storage"],
            "displaysize": data["displaysize"],
            "displayres": data["displayres"],
            "weight": data["weight"],
            "Rating": data["Rating"],
            "Processor": data["Processor"],
            "url": data["url"]
}

def desearialize_list(data)-> list[dict]:
    return [desearialize(laptop) for laptop in data]