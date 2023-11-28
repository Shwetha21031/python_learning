from fastapi import Depends, FastAPI, HTTPException,Body
from sqlalchemy.orm import Session
from typing import Annotated,List
from pydantic import BaseModel
from database import SessionLocal, engine
import models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    'http://localhost:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
    
)

class UserBase(BaseModel):
    fullname : str
    email : str
    designation: str
    is_active :bool
    
class UserModel(UserBase):
    id : int
    
    class Config:
        orm_mode = True
        
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session , Depends(get_db)]

models.Base.metadata.create_all(bind=engine)

@app.post("/users/", response_model=UserModel, tags=["Users"])
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.Users(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/",response_model= list[UserModel] ,tags=["Users"])
async def get_users(db:db_dependency ,skip: int = 0, limit: int = 100):
    users = db.query(models.Users).offset(skip).limit(limit).all()
    return users


@app.put("/users/{id}", response_model=UserModel, tags=["Users"])
async def update_user( db: db_dependency, id: int ,user: UserBase = Body(),):
    db_user = db.query(models.Users).filter(models.Users.id == id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in user.model_dump().items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete("/users/{id}", response_model=dict, tags=["Users"])
async def delete_user(id: int, db: db_dependency):
    db_user = db.query(models.Users).filter(models.Users.id == id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}


# @app.get("/users/{user_id}", response_model=schemas.User ,tags=["Users"])
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user





