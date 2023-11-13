#  It involves hiding the complex implementation details of an object and exposing only the essential features or functionalities. Abstraction allows you to focus on what an object does rather than how it achieves its functionality.

# In Python, abstraction is often achieved through abstract classes and abstract methods, using the ABC (Abstract Base Class) module. 

from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete class implementing Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Concrete class implementing Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Using the abstraction
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Both Circle and Rectangle classes implement the abstract methods area and perimeter
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())
