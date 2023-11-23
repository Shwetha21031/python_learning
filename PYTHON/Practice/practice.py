def multiple_yield():  
    for i in range(5):
        str1 = "First String"  
        yield str1  

        str2 = "Second string"  
        yield str2  

        str3 = "Third String"  
        yield str3  
obj = multiple_yield() 
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
def Convert_dict(a):  
    init = iter(list1)  
    res_dct = dict(zip(init, init))  
    return res_dct  
  
  
# Driver code  
list1 = ['x', 1, 'y', 2, 'z', 3]  
# print(Convert_dict(list1))  

# a = "abc"
# b = "abc" "def"
# print(b)

# clear the list by replacing all the elements with an empty list
# letters[:] = []














