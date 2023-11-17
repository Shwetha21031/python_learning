# A request body is data sent by the client to your API.
# When you need to send data from a client (let's say, a browser) to your API, you send it as a request body.
# A response body is the data your API sends to the client. Your API almost always has to send a response body

# put ,patch  or post
from fastapi import FastAPI,Path,Body
from pydantic import BaseModel,Field,HttpUrl
from typing import List,Annotated

app = FastAPI()


# we pass in the data using the pydantic
class Item(BaseModel):
    name:str
    description: str | None = None
    tax: float | None = None
    price:float 


# @app.post('/items')
# async def create_item(item : Item):
#     item_dict = item.model_dump()
#     if item.tax:
#         item_dict.update({"total": item.tax + item.price})
#     return item_dict

# @app.put('/items/{item_id}')
# async def put_items(item_id:int , item: Item , q : str | None = None):
#     result = {"item_id":item_id , **item.model_dump()}
#     if q:
#         result.update({"q":q})
#     return result


# multiple body parameters -----------------------
class Users(BaseModel):
    username : str |  None = None ,
    password : str |  None = None 

# @app.put('/items/{item_id}')
# async def update_items(
#     *,
#     item_id:int=Path(ge=0,lt=10),
#     q: str | None = None, 
#     item:Item | None = None ,
#     # user:Users | None = None,
#     importance : int = Body(embed=True)
#     ):
#     response = {"item_id":item_id}
#     if q:
#         response.update({"q":q})
#     if item:
#         response.update({"items": item})
#     # if user:
#     #     response.update({"users": user})
#     if importance:
#         response.update({"importance": importance})
#     return response

# here both body parameters are optionals


# Field -----------------------------------------------
class Item2(BaseModel):
    name: str
    des : str | None = Field(
        None,
        title='hii',
        description='qwertyiop',
        max_length=30
    )
    price: float | None = Field(
        None,
        description='qwertyiopasdfghjkl',
    )

# @app.put('/items/{item_id}')
# async def update_items(
#     item_id: str | None = None,
#     item : Item2 | None = Body()
#     ):
    
#     response = {"item_id":item_id,**item.model_dump()}
#     return response
    
# body nested model---------------------------------------
class Image(BaseModel):
    url: HttpUrl
    name:str

class Item(BaseModel):
    name: str
    price: float
    tags: list[str] = [] #list of strings ,or
    tags1: List[str] = [] #list of strings
    tags2 : set[str] = set() #set of strings
    image: Image | None = None
    imageList: List[Image] | None = None
 

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results

# bodies with pure lists
# @app.put("/items/multiple")
# async def create_mutiple_images(images:List[Image]=Body(embed=True)):
#     return images 

# Declare Request Example Data --------------------------------- @
# You can declare examples of the data your app can receive.
class Item(BaseModel):
    name: str = Field(examples=['abcd'])
    description: str | None = Field(examples=['lorem30'])
    price: int = Field(examples=[10])
    tax: float | None  = Field(examples=[1])
    
    # model_config = { 
# it will be used in the API docs.
        # "json_schema_extra": {
        #     "examples": [
        #         {
        #             "name": "Foo",
        #             "description": "A very nice Item",
        #             "price": 35.4,
        #             "tax": 3.2,
        #             # "pay": 300
        #         }
        #     ]
        # }
    # }


# example in body
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item = Body(example={
#                     "name": "Foo",
#                     "description": "A very nice Item",
#                     "price": 35.4,
#                     "tax": 3.2,
#                     # "pay": 300
#                 })):
#     results = {"item_id": item_id, "item": item}
#     return results


# Using the openapi_examples Parameter
# You can declare the OpenAPI-specific examples in FastAPI with the parameter openapi_examples
@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Annotated[
        Item,
        Body(
            openapi_examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            },
        ),
    ],
):
    results = {"item_id": item_id, "item": item}
    return results