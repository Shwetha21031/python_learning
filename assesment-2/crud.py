from sqlalchemy import and_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from models import Student, Course
import schemas
from fastapi import HTTPException ,status

def create_student(db: Session, student_data: dict):
    try:
        db_student = Student(**student_data)
        db.add(db_student) 
        db.commit()
        db.refresh(db_student)
        return {"data":db_student,"message":"data created successfully"}
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE , detail="Unique constraint failedu")
    except ValueError:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE ,detail="Invalid data types")

def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

def get_all_students(db: Session):
    return db.query(Student).all()

def update_student(db: Session, student_id: int, updated_data: dict):
    try:
        db_student = db.query(Student).filter(Student.id == student_id).first()
        for key, value in updated_data.items():
            setattr(db_student, key, value)
        db.commit()
        db.refresh(db_student)
        return {"data":db_student,"message":"data updated successfully"}
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE , detail="Unique constraint failedu")
    except ValueError:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE ,detail="Invalid data types")

def delete_student(db: Session, student_id: int):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    db.delete(db_student)
    db.commit()
    return  {"data":db_student,"message":"data deleted successfully"}

def get_student_by_mobile_or_email(db: Session, mobile: int, email: str):
    if email is None:
        return db.query(Student).filter((Student.mobile_number == mobile)).first()
    elif mobile is None:
        return db.query(Student).filter((Student.email == email)).first()  
    else:
        return db.query(Student).filter(and_(Student.mobile_number == mobile , Student.email == email)).first()

def get_students_by_age(db: Session, age: int):
    return db.query(Student).filter(Student.age == age).all()

def get_students_by_course(db: Session, course_name: str):
    return db.query(Student).join(Course).filter(Course.course_name == course_name).all()


def create_course(db: Session, course: schemas.CourseCreate):
    try:
        db_course = Course(**course.model_dump())
        db.add(db_course)
        db.commit()
        db.refresh(db_course)
        return {"data":db_course,"message":"data created successfully"}
    except IntegrityError:
        return "UNIQUE constraint failed"