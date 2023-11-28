from fastapi import FastAPI ,Body
from app.models import PostSchema , UserSchema , UserLoginSchema
from app.auth.jwt_handler import signJWT

posts = [
    {
        "id":1,
        "title":"penguins",
        "text":"group of aquatic flightless birds"
    },
    {
        "id":2,
        "title":"tigers",
        "text":"largest living cats"
    },
    {
        "id":3,
        "title":"koalas",
        "text":"adorable herbivores"
    }
]

users =[]


app = FastAPI()

# get for testing
@app.get("/",tags=["Test"])
def greet():
    return {"Hello":"World"}

# get posts
@app.get("/posts",tags=["Posts"])
def get_posts():
    return {"data":posts}

# get single post by id
@app.get("/posts/{id}",tags=["Posts"])
def get_one_post(id: int):
    if (id > len(posts)):
        return {
            "error":"no posts on this id"
        }
    for post in posts:
        if post["id"] == id:
            return{
                "data": post
            }
            
@app.post("/posts",tags=["Posts"])
def add_posts(post : PostSchema):
    post.id = len(posts)+1
    posts.append(post.model_dump())
    return {
        "info" : post
    }
    
# create a new user
@app.post("/user/signup",tags=["Users"])
def user_signup(user : UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        else:
            return False
        
@app.post("/user/login",tags=["Users"])
def user_login(user:UserLoginSchema = Body()):
    if check_user(user):
        return signJWT(user.email)
    else:
        return{
            "error":"Invalid email details"
        }