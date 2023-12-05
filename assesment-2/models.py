from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    date_of_birth = Column(Date)
    age = Column(Integer)
    mobile_number = Column(Integer, unique=True, index=True)
    address = Column(String)
    class_level = Column(Integer)
    email = Column(String, index=True, unique=True)
    courses = relationship("Course", back_populates="student")

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    course_name = Column(String,unique=True)
    description = Column(String)
    student_id = Column(Integer, ForeignKey("students.id"))
    student = relationship("Student", back_populates="courses")


