from sqlalchemy import Boolean, Column, Integer, String
from database import Base


class Users(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String)
    email = Column(String, unique=True, index=True)
    designation = Column(String)
    is_active = Column(Boolean, default=True)


