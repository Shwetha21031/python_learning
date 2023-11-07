import demoModule
import platform

x = dir(demoModule) #this dir() function prints all the functions or objects present in dfemoModule
print(x)

demoModule.greet("abc")

print(demoModule.person)
demoModule.person["name"] = 'laila'
print(demoModule.person)

from demoModule import person as p
p['age']=25
print (p["age"] ,"new age")

x = platform.system()
print(x)
