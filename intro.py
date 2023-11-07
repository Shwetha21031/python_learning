print('Hello World')

#casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x,y,z)


#type - You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))

#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Global keyword
def myfunc():
  global abc
  abc = "fantastic"

myfunc()

print("Python is " + abc)

d = 10
print(d)
d = "hello"
print(d)


#data types
dataType = "Hello World"	
dataType = 20	
dataType = 20.5	
dataType = 1j	
dataType = ["apple", "banana", "cherry"]	
dataType = ("apple", "banana", "cherry")		
dataType = range(6)	
dataType = {"name" : "John", "age" : 36}		
dataType = {"apple", "banana", "cherry"}	
dataType = frozenset({"apple", "banana", "cherry"})	
dataType = True	
dataType = b"Hello"	
dataType = bytearray(5)	
dataType = memoryview(bytes(5))	
dataType = None	
print(type(dataType))
