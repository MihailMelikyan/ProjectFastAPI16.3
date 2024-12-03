from fastapi import FastAPI, Path, HTTPException
from typing import Annotated

app = FastAPI()

users = {1: {"имя": "Example", "age": 20}
         }


@app.get("/users")
async def read_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def create_users(username: str = Path(min_length=3, max_length=9, example="Igor"),
                       age: int = Path(ge=0, le=99, example="2")) -> str:
    current_index:str = str(int(max(users, key=int)) + 1)
    users[current_index] = {"Имя": username, "возраст": age}
    return f"User {current_index} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_users(user_id: int = Path(example=1),
                       username: str = Path(min_length=3, max_length=9, example="Igor"),
                       age: int = Path(ge=0, le=99, example=2)) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: str = Path(description="Please enter the User ID")):
    if user_id in users:
        del users[user_id]
        return {"detail": "Пользователь удален"}
    raise HTTPException(status_code=404, detail="Пользователь не найден")
