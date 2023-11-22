# from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

# engine = create_engine('sqlite:///college.db', echo=True, pool_pre_ping=True)

# meta = MetaData()

# students = Table(
#     'students', meta,
#     Column('id', Integer, primary_key=True),
#     Column('name', String),
#     Column('lastname', String),
# )

# students.insert().values([
#                     {"name": "some name"},
#                     {"name": "some other name"},
#                     {"name": "yet another name"},
#                 ])
# # table name
# # for t in meta.sorted_tables: 
# #     print(t.name)


# # access the column "employee_id":
# # students.columns.employee_id

# # # or just
# # students.c.employee_id

# # # via string
# # students.c["employee_id"]

# # # a tuple of columns may be returned using multiple strings
# # # (new in 2.0)
# # emp_id, name, type = students.c["employee_id", "name", "type"]

# # # iterate through all columns
# # for c in students.c:
# #     print(c)

# # # get the table's primary key columns
# # for primary_key in students.primary_key:
# #     print(primary_key)

# # # get the table's foreign key objects:
# # for fkey in students.foreign_keys:
# #     print(fkey)

# # # access the table's MetaData:
# # students.metadata

# # # access a column's name, type, nullable, primary key, foreign key
# # students.c.employee_id.name
# # students.c.employee_id.type
# # students.c.employee_id.nullable
# # students.c.employee_id.primary_key
# # students.c.employee_dept.foreign_keys

# # # get the "key" of a column, which defaults to its name, but can
# # # be any user-defined string:
# # students.c.employee_name.key

# # # access a column's table:
# # students.c.employee_id.table is students

# # # get the table related by a foreign key
# # list(students.c.employee_dept.foreign_keys)[0].column.table

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String), 
)

# conn = engine.connect()
# result = conn.execute(students.insert().values(id=23,name = 'Revi'))
# conn.commit()

# s = students.select()
conn = engine.connect()
# result = conn.execute(s)

# for row in result:
#    print (row)
   
# from sqlalchemy import text
# t = text("SELECT * FROM students")
# result = conn.execute(t)
# for res in result:
#    print (res)

from sqlalchemy.sql import text
s = text("select students.name, students.lastname from students where students.name between :x and :y")
result=conn.execute(s, x = 'A', y = 'L').fetchall()
for res in result:
   print (res)
