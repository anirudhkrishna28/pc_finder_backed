from routes.laptoproute import laptop_route
from routes.shops import shop_route
from fastapi import FastAPI
from routes.login import owner_route,login_route
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(laptop_route,tags=['laptops'])
app.include_router(shop_route,tags=['shops'])
app.include_router(owner_route)
app.include_router(login_route)