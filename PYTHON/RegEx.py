import re

# Search the string to see if it starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x) #returns match object
print(x.span())

# Return an empty list if no match was found:
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

txt = "The rain in Spain"
#Check if the string starts with "The":
x = re.findall("\AThe", txt)
print(x)
if x:
  print("Yes, there is a match!")
else:
  print("No match")
  
  
  
txt = "The rain in Spain"
#Check if the string contains any digits (numbers from 0-9)
x = re.findall("\d", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# The findall() Function
# Print a list of all matches:
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

# Split at each white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)


# removing digits
msg="the0bsjhcb34njkn54njn"
x=(''.join(re.split("\d",msg)))
print(x)



# The sub() function replaces the matches with the text of your choice:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)