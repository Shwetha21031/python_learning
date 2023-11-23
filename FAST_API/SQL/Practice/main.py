from sqlalchemy import create_engine, ForeignKey, MetaData, Table, Column, Integer, String , CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# sql-alchemy is an sql toolkit and object relational mapping 
# a python module - that allows us to map python objects and classes to database tables and entries, so no need to write sql code and we can focus on the objects 
Base = declarative_base()

# person class
class Person(Base):
    __tablename__ = "People"
    
    ssn = Column("ssn",Integer,primary_key=True)
    firstname = Column("firstname",String)
    lastname = Column("lastname",String)
    gender = Column("gender",CHAR)
    age = Column("age",Integer)
    
    def __init__(self,ssn,first,last,gender,age):
        self.ssn = ssn
        self.firstname = first
        self.lastname = last
        self.gender = gender
        self.age = age
    
    def __repr__(self):
        return f"({self.ssn} {self.firstname} {self.lastname} {self.gender} {self.age})"



class Thing(Base):
    __tablename__ = "things"
    
    tid = Column("tid",Integer,primary_key=True)
    description = Column("description",String)
    owner = Column(Integer, ForeignKey("People.ssn"))
    
    def __init__(self,tid,description,owner):
        self.tid = tid
        self.description = description
        self.owner = owner
    
    def __repr__(self):
        return  f"({self.tid} , {self.description} , owned by {self.owner})"
        
engine = create_engine(f"sqlite:///practice.db",echo=True) 
Base.metadata.create_all(bind=engine)
# the person table will run after this line of code
# if the db is not present itll create a new one
# sql alchemy is compatible with different bunch of database like sqlite , mysql
# echo true makes our sql commands appear in the terminal


Session = sessionmaker(bind=engine)
session = Session()

person = Person(121,"abc","def",'m',23)
# session.add(person)
# session.commit #this will close the file /flush / commit the changes to the database

p1 = Person(123,"abcd","defh",'m',23)
p2 = Person(124,"abce","defi",'f',22)
p3 = Person(125,"abcf","defj",'m',24)
p4 = Person(126,"abcg","defk",'f',21)

# session.add(p1)
# session.add(p2)
# session.add(p3)
# session.add(p4)
# session.commit()

results = session.query(Person).all()
# print(results) #we get all the people in the form of list p from db

res = session.query(Person).filter(Person.age > 22)
# for i in res:
#     print(i)
    
# res = session.query(Person).filter(Person.lastname.like("%h%"))
# for i in res:
#     print(i)
    
# res = session.query(Person).filter(Person.lastname.in_(['defg']))
# for i in res:
#     print(i)

t1 = Thing(1,"car",p1.ssn)
t2 = Thing(2,"car",p2.ssn)
# session.add(t1)
# session.add(t2)

# session.commit()

res  = session.query(Thing,Person).filter(Thing.owner == Person.ssn).all()
for r in res:
    print(r)