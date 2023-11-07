
#strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#accessing
a = "Hello, World!"
print(a[1])

# Loop through the letters in the word "banana":
for x in "banana":
  print(x)
  
# The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))

# Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)

# Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)


# slicing
b = "Hello, World!"
print(b[2:5])
b = "Hello, World!"
print(b[-5:-2])

# upper
a = "Hello, World!"
print(a.upper())

# lowercase
a = "Hello, World!"
print(a.lower())

# removes white space
a = " Hello, World! "
print(a.strip())

# Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

# split
a = "Hello, World!"
print(a.split(","))
print(a.split())

# centered
txt = "banana"
x = txt.center(20)
print(x)

# index
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

# find
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

# isDecimal vs isDigit
a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G
print(a.isdecimal())
print(a.isdigit())
print(b.isdecimal())

# join
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

# partition
# Search for the word "bananas", and return a tuple with three elements:
txt = "I could eat bananas all day"
x = txt.partition("bananas")
txt = "i could eat bananas all day with bananas lalalaa"
x = txt.partition("bananas")
print(x)


# falsy values
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#identity operator
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y