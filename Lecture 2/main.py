from enum import Enum

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.post("/")
async def post():
    return {"message": "hello from the post route"}


@app.put("/")
async def put():
    return {"message": "hello from the put route"}


@app.get("/users")
async def list_users():
    return {"message": "list users route"}


@app.get("/users/me")
async def get_current_user():
    return {"Message": "this is the current user"}


@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}


class NameEnum(str, Enum):
    tin = "tin"
    thuan = "thuan"
    noc = "noc"


@app.get("/name/{name}")
async def get_food(name: NameEnum):
    if name == NameEnum.tin:
        return {"name": name, "message": "you are handsome"}

    if name.value == "thuan":
        return {
            "name": name,
            "message": "you are noob",
        }
    return {"name": name, "message": "you are noob"}


#you cannot redefine a path operation
@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]