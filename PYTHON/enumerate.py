l1 = ["eat", "sleep", "repeat"]

print(enumerate(l1)) # returns an object
print(list(enumerate(l1)))

for i in enumerate(l1):
    # print(i)
    pass
    
# accessing next element
enum_list = enumerate(l1)
print(next(enum_list))
print(next(enum_list))
print(next(enum_list))