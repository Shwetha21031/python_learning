from pydantic import BaseModel
from typing import List 
from pydantic import BaseModel, Field , EmailStr
from datetime import date
class CourseBase(BaseModel):
    student_id: int
    course_name: str | None = None
    description: str | None = None

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: int

    class Config:
        orm_mode = True

class StudentBase(BaseModel):
    name: str = Field(default="abc")
    date_of_birth: date | None = None
    age: int = Field(gt=0, lt=35)
    mobile_number: int | None = Field(gt=1000000000, lt=10000000000)
    address: str = Field(default=" model house street")
    class_level: int | None = Field(default=11)
    email: EmailStr = Field(pattern=r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$")
    courses: List[CourseBase] | None = []

class StudentCreate(StudentBase):
    pass


class StudentUpdate(StudentBase):
    pass
# class StudentUpdate(BaseModel):
#     name: str = Field(default="abc")
#     date_of_birth: date | None = None
#     age: int = Field(gt=0, lt=35)
#     mobile_number: int | None = Field(default=1234567890)
#     address: str = Field(default=" model house street")
#     class_level: int | None = Field(default=11)
#     email: EmailStr = Field(default="abc@gmail.com")

class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True





