from fastapi import FastAPI
from typing import Optional
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}





# # @app.get('/items/{item_id}')
# # def read_item(item_id):
# #     return {"item_id":item_id}


# # with types
# # @app.get('/items/{item_id}')
# # def read_item(item_id: int):
# #     return {"item_id":item_id}
# # error if you type any string
# # {"detail":[{"type":"int_parsing","loc":["path","item_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"abc","url":"https://errors.pydantic.dev/2.5/v/int_parsing"}]}

# @app.get('/items/{item_id}')
# def read_item(item_id: int):
#     return {"item_id":item_id}

# @app.get('/users/me')
# def read_user_me():
#      return {"user_id": "the current user"}


# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}

# # Predefined values
# # If you have a path operation that receives a path parameter, but you want the possible valid path parameter values to be predefined, you can use a standard Python Enum.
# from enum import Enum

# class names(str,Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"

# @app.get('/models/{name}')
# def get_model(name:names):
#     if name is names.alexnet:
#         return {"name": name, "message": "Deep Learning FTW!"}

#     if name.value == "lenet":
#         return {"name": name, "message": "LeCNN all the images"}

#     return {"name": name, "message": "Have some residuals"}

# # Path parameters containing paths¶
# # Let's say you have a path operation with a path /files/{file_path}.
# # But you need file_path itself to contain a path, like home/johndoe/myfile.txt. 
# # So, the URL for that file would be something like: /files/home/johndoe/myfile.txt.

# # openApi dosent support, you can still do it in FastAPI, using one of the internal tools from Starlette.


# # Path convertor
# # Using an option directly from Starlette you can declare a path parameter containing a path using a URL like:
# # /files/{file_path:path}

# @app.get("/files/{file_path:path}")
# async def read_file(file_path: str):
#     return {"file_path": file_path}


# # # query parameter
# # fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
# # @app.get("/items/")
# # async def read_item(skip: int = 0, limit: int = 10):
# #     return fake_items_db[skip : skip + limit]


# # # optional parameter
# # @app.get("/items/{item_id}")
# # async def read_item(item_id: str, q: str | None = None):
# #     if q:
# #         return {"item_id": item_id, "q": q}
# #     return {"item_id": item_id}

# # query parameter type conversions
# # @app.get("/items/{item_id}")
# # async def read_item(item_id: str, q: str | None = None, short: bool = False):
# #     item = {"item_id": item_id}
# #     if q:
# #         item.update({"q": q})
# #     if not short:
# #         item.update(
# #             {"description": "This is an amazing item that has a long description"}
# #         )
# #     return item

# @app.get('/blog')
# def index(limit=10,published: bool = True,sort : Optional[str] = None):
#     if published:
#         return {'data': f'{limit} published blogs from the db'}
#     return {'data':f'blog list limit {limit} , published all'}

# # Multiple path and query parameters
# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(
#     user_id: int, item_id: str, q: str | None = None, short: bool = False
# ):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item


# # requestBody
from pydantic import BaseModel

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
# app = FastAPI()
# @app.post("/items/")
# async def create_item(item: Item):
#     return item

# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.dict()}

# class Blog(BaseModel):
#     title: str
#     body: str
#     published: Optional[bool] 

# @app.post('/blog')
# def create_blog(blog : Blog):
#     return {'data':'Blog is created with title as {blog.title}'}

#Query Parameters and String Validations -----------------------------
# We are going to enforce that even though q is optional, whenever it is provided, its length doesn't exceed 50 characters.

from typing import Annotated

from fastapi import  Query
# @app.get("/items/")
# async def read_items(q: Annotated[str | None , Query(max_length=5)] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results



# You can also add a parameter min_length:
# async def read_items(
#     q: Annotated[str | None, Query(min_length=3, max_length=5)] = None
# ):


# Add regular expressions
#     q: Annotated[
#         str | None, Query(min_length=3, max_length=10, pattern="^fixedquery$")
#     ] = None,

# Pydantic v1 regex instead of pattern
# q: Annotated[
    #     str | None, Query(min_length=3, max_length=50, regex="^fixedquery$")
    # ] = None,
    
# default values
# q: Annotated[str, Query(min_length=3)] = "fixedquery")
# q: Annotated[str, Query()] = "rick"

# Make it required
# q: str
# q: Annotated[str, Query(min_length=3

# Required with Ellipsis (...)
# q: Annotated[str, Query(min_length=3)] = ...

# Required with None
# q: Annotated[Union[str, None], Query(min_length=3)] = ...

# Query parameter list / multiple values
# q: Annotated[Union[list[str], None], Query()] = None
# q: Annotated[list, Query()] = []

# Query parameter list / multiple values with defaults
# q: Annotated[list[str], Query()] = ["foo", "bar"]

# You can add a title:
#  q: Annotated[Union[str, None], Query(title="Query string", min_length=3)] = None

# And a description:
#   description="Query string for the items to search in the database that have a good match",

# Deprecating parameters
# deprecated=True,

# Exclude from OpenAPI
#  hidden_query: Annotated[Union[str, None], Query(include_in_schema=False)] = None

from typing import Union
@app.get("/items/")
async def read_items(
    q: Annotated[
        Union[str, None],
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            # deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Path Parameters and Numeric Validations---------------------------
from fastapi import  Path
@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[Union[str, None], Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# greater than or equal
# async def read_items(
#     item_id: Annotated[int, Path(title="The ID of the item to get", ge=1)], q: str
# ):

# greater than and less than or equal
# async def read_items(
#     item_id: Annotated[int, Path(title="The ID of the item to get", gt=0, le=1000)],
#     q: str,
# ):

# Number validations: floats, greater than and less than
# async def read_items(
#     *,
#     item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
#     q: str,
#     size: Annotated[float, Query(gt=0, lt=10.5)],
# ):


# Body - Multiple Parameters ------------------------
# Mix Path, Query and body parameters:

# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None


# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
#     q: Union[str, None] = None,
#     item: Union[Item, None] = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     return results


# But you can also declare multiple body parameters, e.g. item and user:
#     results = {"item_id": item_id, "item": item, "user": user}


