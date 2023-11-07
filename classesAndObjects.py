class MyClass:
  x = 5
  
obj1 = MyClass()
print(obj1.x)



class Person:
    def __init__(self, name, age):
      self.name = name
      self.age = age
      print("init method invoked")
      
p1 = Person("riya",22)
print(p1.name,p1.age)


# class Employee: 
#     def __init__(self, name, age, id): 
#         self.name = name 
#         self.age = age
#         self.id = id 

# employeeObject = Employee('employeeName', 20, 1101)

# print(employeeObject)
# print(employeeObject.__str__())
# print(employeeObject.__repr__())


# class Employee: 
#     def __init__(self, name, age, id): 
#         self.name = name 
#         self.age = age
#         self.id = id 
    
#     def __str__(self):
#         return f'Employee name is {self.name}, employee\'s age is {self.age} and id is {self.id}'

# employeeObject = Employee('employeeName', 20, 1101)

# print(employeeObject.__str__())
# print(employeeObject)
# print(str(employeeObject))
# print(employeeObject.__repr__())



# class Cylinder:
#     pi = 3.14
#     def __init__(self, radius, height):
#         self.radius = radius
#         self.height = height
    
#     def __str__(self):
#         return "You just called __str__"

#     def __repr__(self):
#         return "You just called __repr__"

# cylinderOne = Cylinder(3, 6)

# print(cylinderOne)

# print(repr(cylinderOne))

# print(str(cylinderOne))


# methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# self
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()


# inheritance
class Shapes: #parent
    def __init__(self, color):
        self.color = color
    
    def defination(self):
        print('this shape is of color',self.color)
        
circle = Shapes("green")
circle.defination()
        
class Triangle(Shapes):
    pass

triangle1 = Triangle("red")
triangle1.defination()

class Rectangle(Shapes):
    def __init__(self,color,width,height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(abc):
        return abc.width*abc.height
 
rec1 = Rectangle("blue",20,30)
print(rec1.area())
rec1.defination()



# iterator
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))