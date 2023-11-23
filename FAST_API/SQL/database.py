from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///sql_app.db"
# this database will be in the same folder

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"  
#this is only for postgres

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# The argument:
# connect_args={"check_same_thread": False}
# ...is needed only for SQLite

# Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Now we will use the function declarative_base() that returns a class.
Base = declarative_base()
