# Dictionaries are written with curly brackets, and have keys and values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  1:'abc'
}
print(thisdict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# Print the number of items in the dictionary:
print(len(thisdict))

# The dict() Constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# Get a list of the keys:
x = thisdict.keys()

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

# Get a list of the values:
x = car.values()
car["year"] = 2020
print(x) 

# to get a particular key 
my_dict ={"Java":100, "Python":112, "C":11}
print("One line Code Key value: ", list(my_dict.keys()) 
      [list(my_dict.values()).index(100)])

# Get a list of the key:value pairs
x = thisdict.items()

# Update the "year" of the car by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

# The pop() method removes the item with the specified key name:
thisdict.pop("model")
print(thisdict,"removed model")

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict.popitem()
print(thisdict)

# The del keyword can also delete the dictionary completely:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict

# The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

# Print all key names in the dictionary, one by one:
for x in thisdict:
  print(x)
  
# You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
  print(x)
  
# You can use the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
  print(x)
  
# Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
  print(x, y)
  
# Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Make a copy of a dictionary with the dict() function:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# nested dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# or

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# Print the name of child 2:
print(myfamily["child2"]["name"])



details = {
  'name' : 'karan',
  'password' : '123'
}
newname = input("enter a name: ")
details["name"] = newname
print(details)



tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
# {'jack': 4098, 'sape': 4139, 'guido': 4127}
print(tel['jack'])
# 4098
del tel['sape']
tel['irv'] = 4127
print(tel)
# {'jack': 4098, 'guido': 4127, 'irv': 4127}
print(list(tel))
# ['jack', 'guido', 'irv']
print(sorted(tel))
# ['guido', 'irv', 'jack']
print('guido' in tel)
# True
print('jack' not in tel)
# False