
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def div(a,b):
    if(b==0):
        raise ValueError('b cannot be 0')
    return a/b

def mul(a,b):
    return a*b

print(div(10,-2))