from typing import Annotated

from fastapi import Body, Depends, FastAPI, HTTPException, Header

app = FastAPI()

# dependency
async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

# another dependency
async def hello():
    return "world"

# @app.get("/items/")
# async def read_items(commons: Annotated[dict, Depends(common_parameters)],hello:str = Depends(hello) ):
#     return {"commons" :commons , 'hello': hello}

# if you want to have the same functionality
# @app.get("/users/")
# async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
#     return commons


# classes as dependencies ---------------------------
# editors can't provide a lot of support (like completion) for dicts, because they can't know their keys and value types.

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# class
class CommonQueryParams:
    def __init__(self,item_id : int, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit
        self.item_id = item_id

# @app.get("/items/{item_id}")
# async def read_items(commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]):
#     response = {}
#     if commons.q:
#         response.update({"q": commons.q})
#     items = fake_items_db[commons.skip : commons.skip + commons.limit]
#     response.update({"items": items})
#     return response

# sub dependencies-------------------------------

def query_extractor(q: str | None = None):
    return q


def query_or_body_extractor(
    q: Annotated[str, Depends(query_extractor)],
    last_query: Annotated[str | None, Body] = None,
):
    if not q:
        return last_query
    return q


# @app.post("/item")
# async def read_query(
#     query_or_body: Annotated[str, Depends(query_or_body_extractor)]
# ):
    # return {"q_or_body": query_or_body}


# another example
# Dependency 1
def common_parameters(q: str = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

# Subdependency 2, which depends on Dependency 1
def subdependency_common(params: dict = Depends(common_parameters)):
    return f"Subdependency: {params}"

# Main dependency that uses Subdependency 2
def main_dependency(subdep_result: str = Depends(subdependency_common)):
    return f"Main Dependency using Subdependency: {subdep_result}"

@app.get("/items/")
async def read_items(result: str = Depends(main_dependency)):
    return {"message": result}

# dependencies in path operation decorators and global dependencies ----

async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


# @app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
# async def read_items():
#     return [{"item": "Foo"}, {"item": "Bar"}]

# global dependency
# app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])


# @app.get("/itemss/")
# async def read_items():
#     return [{"item": "Portal Gun"}, {"item": "Plumbus"}]


# @app.get("/users/")
# async def read_users():
#     return [{"username": "Rick"}, {"username": "Morty"}]