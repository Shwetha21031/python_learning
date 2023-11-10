# defining a decorator
def hello_decorator(func):
	def inner():
		print("Hello, this is before function execution")
		func()
		print("This is after function execution")
	return inner

# way 1
def function_to_be_used1():
	print("This is inside the function1 !!")
# passing 'function_to_be_used1' inside the
# decorator to control its behaviour
function_to_be_used1 = hello_decorator(function_to_be_used1)
# calling the function
# function_to_be_used1()


# way 2
@hello_decorator
def function_to_be_used2():
	print("This is inside the function2 !!")
 
# function_to_be_used2()


# example 2
def greet(fx):
    def mfx(*args,**kwargs):
        print("good morning")
        fx(*args,**kwargs)
    return mfx

@greet
def say_hi():
    print("Hi there!")
    
# say_hi()

@greet
def count(a,b):
    print(a+b)
# count(3,4)


@greet
def square(n):
    return n


def decorate(fx):
    def inner():
        x = fx()
        return x*x
    return inner


def decorate2(fx):
    def inner():
        x = fx()
        return 2*x
    return inner

@decorate
@decorate2
def num():
    return 5

@decorate2
@decorate
def num2():
    return 10

print(num())
print(num2())

    
    