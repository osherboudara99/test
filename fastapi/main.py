from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Gender, Role, UserUpdateRequest


# localhost:8000/docs shows us interactive documentation

# localhost:8000/redoc shows us non-interactive documentation


# Initialize FASTAPI
app = FastAPI()

# Create Database from Pydantic classes
db: List[User] = [
    User(
        id=uuid4(), # Will change after everytime we restart application
        first_name="Osher", 
        last_name="Boudara", 
        gender=Gender.male, 
        roles=[Role.student]
    ),
    User(
        id=UUID("6f78ea8c-090b-4c83-b92f-e8345a8ab55f"), # FIXED ID
        first_name="Alexa", 
        last_name="Johnsoin", 
        gender=Gender.female, 
        roles=[Role.admin, Role.user]
    )

]


# HTTP requests

@app.get("/")
async def root():
    return {"Hello":"Json"}


@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_users(user: User): # Defining User class as parameter
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_users(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user) 
            return
    raise HTTPException(
        status_code=404,
        detail= f"User with ID {user_id} does not exist!"
    )

@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name 
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code=404,
        detail= f"User with ID {user_id} does not exist!"
    )   
    
