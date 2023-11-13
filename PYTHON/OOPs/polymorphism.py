# Polymorphism simply means having many forms. For example, we need to determine if the given species of birds fly or not, using polymorphism we can do this using a single function.


class Bird:
   
    def intro(self):
        print("There are many types of birds.")
 
    def flight(self):
        print("Most of the birds can fly but some cannot.")
 
class sparrow(Bird):
   
    def flight(self):
        print("Sparrows can fly.")
 
class ostrich(Bird):
 
    def flight(self):
        print("Ostriches cannot fly.")
 
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
 
obj_bird.intro()
obj_bird.flight()
 
obj_spr.intro()
obj_spr.flight()
 
obj_ost.intro()
obj_ost.flight()



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
  
