from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
import uvicorn
import crud, database, schemas

app = FastAPI(
    title="Student Database"
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
database.create_tables()

# creating the student
@app.post("/students/", status_code=status.HTTP_201_CREATED )
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    if (student.mobile_number < 10000000000) and (student.mobile_number > 1000000000) :
        return crud.create_student(db, student.model_dump())
    else: 
        raise HTTPException(status_code=400 , detail="phone number should be of 10 digit")

# getting student by id
@app.get("/students/{student_id}", status_code=status.HTTP_202_ACCEPTED )
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"data":db_student,"message":"data recieved successfully"}

# all students
@app.get("/students/", response_model=list[schemas.Student] ,status_code=status.HTTP_200_OK)
def read_all_students(db: Session = Depends(get_db)):
    return crud.get_all_students(db)

# modify student
@app.put("/students/{student_id}" )
def update_student(student_id: int, updated_data: schemas.StudentUpdate, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    if (updated_data.mobile_number < 10000000000) and (updated_data.mobile_number > 1000000000) :
        return crud.update_student(db, student_id, updated_data.model_dump())
    else: 
        raise HTTPException(status_code=400 , detail="phone number should be of 10 digit")

# del student
@app.delete("/students/{student_id}" )
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return crud.delete_student(db, student_id)

# mobile or email
@app.get("/students/details/" )
def get_student_by_mobile_or_email(mobile: int | None = None, email: str | None = None, db: Session = Depends(get_db)):
    if (mobile is None) and (email is None):
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="enter either mobile number or phone number")
    if (mobile or email):
        db_student = crud.get_student_by_mobile_or_email(db, mobile, email)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


# getting student by age
@app.get("/students/age/{age}", response_model=list[schemas.Student] ) 
def get_students_by_age(age: int, db: Session = Depends(get_db)):
    return crud.get_students_by_age(db, age)


# getting student by course name
@app.get("/students/course/{course_name}", response_model=list[schemas.Student] )
def get_students_by_course(course_name: str, db: Session = Depends(get_db)):
    return crud.get_students_by_course(db, course_name)

# creating course
@app.post("/courses/" )
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    return crud.create_course(db=db, course=course)
    
    
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

