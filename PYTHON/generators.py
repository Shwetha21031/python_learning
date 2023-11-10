# A generator function that yields 3 integers

def generate_3_int():
    yield 1
    yield 2
    yield 3
    
# print(generate_3_int()) #returns an object

# for i in generate_3_int():
#     print(i) 

#  or

x = generate_3_int()
# print(next(x))
# print(next(x))
# print(next(x))

# A simple generator for Fibonacci Numbers 
def fib(n):
    a,b = 0,1
    while a<n:
        yield a
        a,b = b,a+b
        
# for i in fib(5):
#     print(i)
    
    
# generator expression 
x = (i  for i in range(10) if i%2==0 )
for i in x:
    print(i)
