from fastapi import FastAP,status
from pydantic import BaseModel 
from typing import Literal

app = FastAPI()


class UserBase(BaseModel):
    username: str
    email: str
    full_name: str | None = None

# class UserIn(UserBase):
#   password: str

# class UserOut(UserBase):
#     pass

# Don't do this in production!
# @app.post("/user/",response_model=UserOut)
# async def create_user(user: UserIn) :
#     return user
# or
# @app.post("/user/")
# async def create_user(user: UserIn) -> UserBase:
#     return user


# Return Type and Data Filtering
class Item(BaseModel):
    name:str
    des:str | None = None
    tax: float = 10.5
    
items = {
    "foo": {"name":"Foo","des":"Something about Foo"},
    "bar": {"name":"Bar","tax":23},
    'baz': {"name":"Baz","des":None}
}


# response_model_exclude_unset
@app.get("/items/{item_id}",response_model=Item ,
response_model_exclude_unset=True)
async def read_item_name(item_id: Literal["foo","bar","baz"]):
    return items[item_id]

# response_model_include
@app.get("/items/{item_id}/name",response_model=Item ,
         response_model_include={"name","des"})
async def read_item_name(item_id: Literal["foo","bar","baz"]):
    return items[item_id]

# response_model_exclude
@app.get("/items/{item_id}/public",response_model=Item ,response_model_exclude={"tax"})
async def read_item_public(item_id: Literal["foo","bar","baz"]):
    return items[item_id]



# ExtraModels-----------------
# The input model needs to be able to have a password.
# The output model should not have a password.
# The database model would probably need to have a hashed password.
class UserIn(BaseModel):
    username: str
    password: str
    email: str
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: str
    full_name: str | None = None


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: str
    full_name: str | None = None
    
def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password

def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db

@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved

# response status code
@app.post('/items/',status_code=status.HTTP_404_NOT_FOUND)
def create_items(name:str):
    return {"name":name}