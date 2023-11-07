# MAP -------------
l = [1,2,3,4]

def cube(x):
    return x**3

newl = list(map(cube,l))
print(newl)
# using lambda function
newl = list(map(lambda x: x*x*x, l))
print(newl)

# FILTER --------------
l = [2,3,4,6,4,5,7,8,9]
def filter_fuc(a):
    return a%2==0
newlist = list(filter(filter_fuc, l))
print(newlist)

# using lambda function
newlist = list(filter(lambda x:x%2==0,l))
print(newlist)

# REDUCE ---------------

from functools import reduce
numbers = [3,4,7,4,5,8]
sum = reduce(lambda x,y:x+y,numbers)
print(sum)