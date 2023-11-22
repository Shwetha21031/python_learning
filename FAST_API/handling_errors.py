# You could need to tell the client that:

# The client doesn't have enough privileges for that operation.
# The client doesn't have access to that resource.
# The item the client was trying to access doesn't exist.

from fastapi import FastAPI, HTTPException
from fastapi import  Request,status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.responses import HTMLResponse
from starlette.exceptions import HTTPException as starletteException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from fastapi.exception_handlers import request_validation_exception_handler

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items-header/{item_id}")
async def read_item_header(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my error"},
        )
    return {"item": items[item_id]}


# customExceptions
class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}


# this gives us an human readable simple error when you type string or anything other that int in this case
# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     return PlainTextResponse(str(exc), status_code=400)

# # starlette exception handling
# @app.exception_handler(starletteException)
# def http_exception_handler(request ,exc):
#     return PlainTextResponse(str(exc.detail),status_code=exc.status_code)

# @app.get("/Validationitems/{item_id}")
# async def read_item(item_id: int):
#     if item_id == 3:
#         raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
#     return {"item_id": item_id}


# overriding the httpException error handler
# The RequestValidationError contains the body it received with invalid data.
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request : Request , exc: RequestValidationError):
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=jsonable_encoder({"detail":exc.errors(),"body":exc.body}))

class Item(BaseModel):
    title: str
    size: int


@app.post("/items/")
async def create_item(item: Item):
    return item
