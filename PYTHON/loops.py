# Python has two primitive loop commands:

# while loops
# for loops


# while 
# Print i as long as i is less than 6:

i = 1
while i < 6:
  print(i)
  i += 1
  
# break
# Exit the loop when i is 3:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
# continue
# With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
# With the else statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


  
#for
# looping through a string
str = "hello"
for i in str:
    print(i)
    
# looping through a list
myList = ["apple","banana","mango"]
for x in myList:
    print(x)
    
# looping through a tuple
myList = tuple(myList)
for x in myList:
    print(x)
    
# looping through a set
mySet = {'a','b','c'}
for i in mySet:
    print(i)
    
# looping through dictionary
myDict = {
    'a':"abc",
    "b":"bcd",
    "c":"cde"
}
for i in myDict:
    print(f'Key :{i}, Value:{myDict[i]}')


for x in range(5):
    print(x)
    
    
# Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)
  
# Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
  print(x)
else:
  print("Finally finished!")
  
# nested loop
# Print each adjective for every fruit:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)