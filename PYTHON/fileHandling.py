import os
# The open() function takes two parameters; filename, and mode.

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)



# Assume we have the following file, located in the same folder as Python:

f = open("demofile.txt","r")
print(f.read())
f.close()
print("----------")
# if file is located at a different location
f = open("C:/Users/Sannamalai/Desktop/file/welcome.txt")
print(f.read())
print("---------- only 5 characters")
f = open("C:/Users/Sannamalai/Desktop/file/welcome.txt")
print(f.read(5))
print("----------only one line")
f = open("C:/Users/Sannamalai/Desktop/file/welcome.txt")
print(f.readline())
print(f.readline())
# looping
for x in f:
  print(x)
  
  
f.close()


# Open the file "demofile2.txt" and append content to the file:
f = open("demofile.txt","a")
f.write("\n appending content to the file")
f.close()

f=open("demofile.txt","r")
print(f.read())
f.close()

# Open the file "demofile3.txt" and overwrite the content:
f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
f = open("demofile3.txt", "r")
print(f.read())


# Create a New File
# f = open("newFile.txt","x") 

# to check if file exists
if(os.path.exists("newFile.txt")):
    print ("The file already exists.")
else:
    print("the file does not exist")
    
# to remove a file
if(os.path.exists("newFile.txt")):
    os.remove("newFile.txt")
else:
    print("the file does not exist")


