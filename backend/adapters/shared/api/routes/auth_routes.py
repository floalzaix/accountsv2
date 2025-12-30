#
#   Imports
#

from fastapi import APIRouter

# Perso



#
#   Routes
#

auth_routes = APIRouter()

@auth_routes.post("/register")
async def register(email: str, password: str, pseudo: str):
    return {"message": "User registered successfully"}

@auth_routes.post("/login")
async def login(email: str, password: str):
    return {"message": "User logged in successfully"}
