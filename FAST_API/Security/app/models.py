from pydantic import BaseModel , Field , EmailStr
class PostSchema(BaseModel):
    id:int = Field(default=0)
    title:str = Field(default=None)
    content : str=Field(default=None)
    class Config:
        schema_extra = {
            "post_demo": {
                "title": "some title",
                "content": "some content"
            }
        }
        
class UserSchema(BaseModel):
    fullname : str = Field(default=None)
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    class Config:
        the_schema = {
            "user_demo":{
                "name" : "Bek",
                "email":"help@bek.com",
                "password":"123"
            }
        }

class UserLoginSchema(BaseModel):
    email : str = Field(default=None)
    password : str = Field(default=None)
    class Config:
        the_schema = {
            "user_demo":{
                "email":"help@bek.com",
                "password":"123"
            }
        }