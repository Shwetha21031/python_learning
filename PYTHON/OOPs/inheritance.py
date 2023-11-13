# Inheritance is the capability of one class to derive or inherit the properties from another class.

# Types of Inheritance
# Single Inheritance: Single-level inheritance enables a derived class to inherit characteristics from a single-parent class.
# Multilevel Inheritance: Multi-level inheritance enables a derived class to inherit properties from an immediate parent class which in turn inherits properties from his parent class. 
# Hierarchical Inheritance: Hierarchical-level inheritance enables more than one derived class to inherit properties from a parent class.
# Multiple Inheritance: Multiple-level inheritance enables one derived class to inherit properties from more than one base class.

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
# x.printname()

class Student(Person):
    def __init__(self, fname, lname , year):
        # Person.__init__(self, fname, lname) 
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen" ,2019)
# x.printname()
# x.welcome()


# single inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()
# dog.speak()  # Inherits 'speak' method from Animal class
# dog.bark()   # Invokes 'bark' method from Dog class


# Multiple Inheritance:
# In multiple inheritance, a class is derived from more than one base class.

class Bird:
    def chirp(self):
        print("Bird chirps")

    def walk(self):
        print('walks on 2 legs')

class Dog:
    def bark(self):
        print("Dog barks")
    
    def walk(self):
        print('walks on 4 legs')

class DogBird(Dog, Bird):
    def action(self):
        print("Performs actions of both Dog and Bird")

db = DogBird()
# db.bark()    # Invokes 'bark' method from Dog class
# db.chirp()   # Invokes 'chirp' method from Bird class
# db.action()  # Invokes 'action' method from DogBird class
# db.walk()    # Invokes 'Dogs' method as it was mentioned first as parameter
 
# Multilevel Inheritance:
# In multilevel inheritance, a class is derived from a base class, and another class is derived from this derived class.
class Animal:
    def speak(self):
        print("Animal speaks")

    def walk(self):
        print(' animal walks on 4 legs')


class Dog(Animal):
    def bark(self):
        print("Dog barks")

    def walk(self):
        print('Dog walks on 4 legs')


class Labrador(Dog):
    def fetch(self):
        print("Labrador fetches")
    def walk(self):
        print('lab walks on 4 legs')


# lab = Labrador()
# lab.speak()  # Inherits 'speak' method from Animal class
# lab.bark()   # Inherits 'bark' method from Dog class
# lab.fetch()  # Invokes 'fetch' method from Labrador class
# lab.walk()
# # Explicitly calling the 'walk' method from the Dog class
# Dog.walk(lab)

# Hierarchical Inheritance:
# In hierarchical inheritance, multiple classes are derived from a single base class.

class Animal:
    def speak(self):
        print("Animal speaks")
    def likes(self):
        print('everything')

class Dog(Animal):
    def bark(self):
        print("Dog barks")
    def likes(self):
        print('biscutes')

class Cat(Animal):
    def meow(self):
        print("Cat meows")
    def likes(self):
        print('fish')
        super().likes()  # Invoke the 'likes' method of the Animal class

dog = Dog()
cat = Cat()

dog.speak()  # Inherits 'speak' method from Animal class
dog.bark()   # Invokes 'bark' method from Dog class

cat.speak()  # Inherits 'speak' method from Animal class
cat.meow()   # Invokes 'meow' method from Cat class

cat.likes()

print(type(Animal))
print(type(dog))