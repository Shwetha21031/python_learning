from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
# async def read_item(item_id): # youll recieve a string 
async def read_item(item_id: int): #with types
    return {"item_id": item_id}



# Order matters
# @app.get("/users")
# async def read_users():
#     return ["Rick", "Morty"]

# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}
# Otherwise, the path for /users/{user_id} would match also for /users/me, "thinking" that it's receiving a parameter user_id with a value of "me".



# Predefined values
# you want the possible valid path parameter values to be predefined, you can use a standard Python Enum
# from enum import Enum
# class ModelName(str, Enum): #you'll get options in thedocumentation
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"
# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}
#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}
#     return {"model_name": model_name, "message": "Have some residuals"}

# Path convertor
# Using an option directly from Starlette you can declare a path parameter containing a path using a URL like:
# /files/{file_path:path}
# You could need the parameter to contain /home/johndoe/myfile.txt, with a leading slash (/).
# In that case, the URL would be: /files//home/johndoe/myfile.txt, with a double slash (//) between files and home.

# --------------advance (after query parameter)

# you can declare the same type of validations and metadata for path parameters with Path
# from typing import Annotated
# from fastapi import Path, Query

# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="The ID of the item to get")],
#     q: Annotated[str | None, Query(alias="item-query")] = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results


# # Order the parameters as you need
# @app.get("/items/{item_id}")
# # async def read_items(q: str, item_id: int = Path(title="The ID of the item to get")): # without annotated 
# # async def read_items(*, item_id: int = Path(title="The ID of the item to get"), q: str): # without annotated but with *
# async def read_items(
#     q: str, item_id: Annotated[int, Path(title="The ID of the item to get")]
# ): #with annotated
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results


# numeric validations ----------------------
# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title="The ID of the item to get", ge=1)], q: str
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
# size: Annotated[float, Query(gt=0, lt=10.5)],
# gt: greater than
# ge: greater than or equal
# lt: less than
# le: less than or equal