def my_function():
  print("Hello from a function")
  
my_function()

# Information can be passed into functions as arguments
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


# Arbitrary Arguments, *args
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Keyword Arguments, **kwargs
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
# or
# If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# return values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))

# recursion
def recursive_func(k):
    if(k>0):
        sum = k+recursive_func(k-1)
        return(sum)
    else:
        return 0

print(recursive_func(6))


# factorial of a number
def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)
    
print(fact(5))

# fibbonacci series
def fibonacci(num):
    if num <= 1:
        return 1
    else:
        return (fibonacci(num - 1) + fibonacci(num - 2))

print(fibonacci(4))