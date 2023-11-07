def add(a,b):
    return a+b
print(add(5,10))

# lambda function
square = lambda a : a*a
print(square(5))

sum = lambda a,b,c:a+b+c
print(sum(3,4,2))

# to double n number of times
def times(n):
    return lambda x:x * n
double_times = times(2)
print(double_times(4))