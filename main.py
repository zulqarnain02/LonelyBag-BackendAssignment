from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from fastapi.responses import JSONResponse

app = FastAPI()

# Pydantic model for User
class User(BaseModel):
    id: int
    name: str
    phone_no: str
    address: str

# Pydantic model for User Update
class UserUpdate(BaseModel):
    name: str
    phone_no: str
    address: str

# In-memory storage for users
users = {}

# Create a new user
@app.post("/users/", status_code=201)
async def create_user(user: User):
    if user.id in users:
        raise HTTPException(status_code=400, detail="User ID already exists")
    users[user.id] = user
    return {"message": "User created successfully"}

# Search users by name - This needs to be BEFORE the get_user route
@app.get("/users/search")
async def search_users(name: str):
    matching_users = [user for user in users.values() if name.lower() in user.name.lower()]
    return matching_users

# Get user by ID
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

# Update user details
@app.put("/users/{user_id}")
async def update_user(user_id: int, user_update: UserUpdate):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Update the user while preserving the ID
    users[user_id] = User(
        id=user_id,
        name=user_update.name,
        phone_no=user_update.phone_no,
        address=user_update.address
    )
    return {"message": "User updated successfully"}

# Delete user by ID
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return {"message": "User deleted successfully"}