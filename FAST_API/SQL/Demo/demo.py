from sqlalchemy import create_engine , ForeignKey , String , Integer , Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# declarative base = we are going to use this to create the model of our table ( class )
Base = declarative_base()

