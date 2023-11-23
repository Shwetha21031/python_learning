from sqlalchemy import ForeignKey, create_engine,MetaData,Table ,Column,Integer,String,text

engine  = create_engine("sqlite:///sample.db",echo=True)

meta = MetaData()

# creating table
Students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String),
)

# another table
addresses = Table(
   'addresses', meta, 
   Column('id', Integer, primary_key = True), 
   Column('st_id', Integer, ForeignKey('students.id')), 
   Column('postal_add', String), 
   Column('email_add', String))
meta.create_all(engine)
conn = engine.connect()

# ins = Students.insert().values(name = 'Krish')
# print(ins.compile().params)
# result = conn.execute(ins)

# conn.execute(Students.insert(), [
#    {'name':'Rajiv', 'lastname' : 'Khanna'},
#    {'name':'Komal','lastname' : 'Bhandari'},
#    {'name':'Abdul','lastname' : 'Sattar'},
#    {'name':'Priya','lastname' : 'Rajhans'},
# ])

output = conn.execute(Students.select()).fetchall()
print(output)
# conn.commit()

# selecting rows
s = Students.select()
result = conn.execute(s)
row = result.fetchone()
# print("single row: ",row)

# for row in result:
#    print (row)
   
# using queries
s = Students.select().where(Students.c.id>2)
result = conn.execute(s)

# for row in result:
#    print (row)
   
   
   
# Using Textual SQL
t = text("SELECT * FROM Students")
result = conn.execute(t)
# for i in result:
#     print(i)

# updating 
# stmt=Students.update().where(Students.c.lastname=='Khanna').values(lastname='Kapoor')
# conn.execute(stmt)
# s = Students.select()
# conn.execute(s).fetchall()
# conn.commit()

# stmt = Students.delete().where(Students.c.id > 2)
# conn.execute(stmt)
# conn.commit()

# updating multiple tables
stmt = Students.update().\
   values(name = 'xyz').\
   where(Students.c.id == addresses.c.id)
conn.execute(stmt)
conn.commit()
