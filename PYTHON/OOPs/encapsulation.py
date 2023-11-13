# wrapping data and the methods that work on data within one unit. 
# restrictions on accessing variables and methods directly and can prevent the accidental modification of data. 
# To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variables.


# Python Access Modifiers

# The public Access Modifier
# The public member is accessible from inside or outside the class.

# The protected Access Modifier
# The protected member is accessible. from inside the class and its sub-class. Define a protected member by prefixing the member name with an underscore, for example −
# _points

# The private Access Modifier
# The private member is accessible only inside class. Define a private member by prefixing the member name with two underscores, for example −
# __age


class EncapsulationExample:
    def __init__(self):
        # Public attribute
        self.public_variable = "I am public"

        # Protected attribute (convention: _variable)
        self._protected_variable = "I am protected"

        # Private attribute (convention: __variable)
        self.__private_variable = "I am private"

    # Public method
    def public_method(self):
        print("This is a public method")

    # Protected method
    def _protected_method(self):
        print("This is a protected method")

    # Private method
    def __private_method(self):
        print("This is a private method")

    # Public method accessing private variable
    def access_private_variable(self):
        print("Accessing private variable:", self.__private_variable)

# Create an instance of the class
obj = EncapsulationExample()

# Access public members
print(obj.public_variable)     # Accessing public variable
obj.public_method()            # Accessing public method

# Access protected members
print(obj._protected_variable)  # Accessing protected variable
obj._protected_method()         # Accessing protected method

# Access private members (not recommended, usually accessed through public methods)
obj.access_private_variable()   # Accessing private variable through a public method
# obj.__private_method()       # Uncommenting this line will result in an AttributeError, as it's not directly accessible

