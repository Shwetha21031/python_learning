# methods/functions/operators with the same name that can be executed on many objects or classes.


# Function Polymorphism
# An example of a Python function that can be used on different objects is the len() function.


# Class Polymorphism
# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()
  
# Inheritance clas polymorphism
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")  
boat1 = Boat("Ibiza", "Touring 20")  
plane1 = Plane("Boeing", "747")  

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
  
  
  
# x=400
def func():
    # global x
    x = 10
    def innerFunc():
        # print(x)
        pass
    innerFunc()
print(x)
func()