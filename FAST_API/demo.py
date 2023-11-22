# from fastapi import FastAPI


# app = FastAPI()

# @app.get('/blog')
# def index(limit):
#     return {'data':f'blog list'}

# @app.get('/blog/unpublished')
# def unpublished():
#     return {'data':'list of unpublished blogs'}

# @app.get('/blog/{id}')
# def get_id(id):
#     return {'data': id}

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: list[str] = []


@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item


@app.get("/items/")
async def read_items() -> list[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]