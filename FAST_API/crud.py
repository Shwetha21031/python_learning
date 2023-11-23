from fastapi import FastAPI,Path,HTTPException,status
from enum import Enum
from pydantic import BaseModel

app = FastAPI()

class Emp(BaseModel):
    name : str 
    designation : str | None = 'trainee'
    
employees:Emp = {
    1: {
        "name": 'abc',
        "designation" : "frontend"
    } 
}

class Tags(Enum):
    Get = "Get"
    Post = "Post"
    Put = "Put"
    Delete = "Delete"

@app.get("/get-employee",tags=[Tags.Get])
def get_Employees():
    if(employees):
        return employees
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail='no users')

@app.get("/get-employee/{id}",tags=[Tags.Get])
def get_Employee(id: int = Path(description="get individual employee by id")):
    if id in employees:
        return employees[id]
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='id not found')
    
@app.post("/create-employee",tags=[Tags.Post])
def create_Employee(emp : Emp, id : int):
    if id in employees:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='id already exists')
    else:
        employees.update({id:emp})
        return {"created employee":emp}

@app.put("/update-employee/{id}",tags=[Tags.Put])
def update_Employee(*,id: int = Path(description="update individual employee by id") , emp : Emp):
    if id in employees.keys():
        employees[id] = emp
        return {"updated employee": emp}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='id not found')

@app.delete("/employees/{id}",tags=[Tags.Delete])
def delete_Employee(id: int= Path(description="delete employee by id")):
    if id in employees.keys():
        del employees[id]
        return "deleted employee"
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='id not found')