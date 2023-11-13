# The object is an entity that has a state and behavior associated with it.

# An object consists of:

# State: It is represented by the attributes of an object. It also reflects the properties of an object.
# Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
# Identity: It gives a unique name to an object and enables one object to interact with other objects.

class Dog:
    pass

# object


obj = Dog()

# Class methods must have an extra first parameter in the method definition. We do not give a value for this parameter when we call the method, Python provides it
# If we have a method that takes no arguments, then we still have to have one argument.

# When we call a method of this object as myobject.method(arg1, arg2), this is automatically converted by Python into MyClass.method(myobject, arg1, arg2)


# __init__
#  It is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object 
class Dog:
     
    # class attribute
    attr1 = "mammal"
 
    # Instance attribute
    def __init__(self, name):
        self.name = name

# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
 
# Accessing class attributes
print("Rodger is a {}".format(Rodger.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))
 
# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))