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
# print(f.read())
# f.close()
# print("----------")
# # if file is located at a different location
# f = open("C:/Users/Sannamalai/Desktop/file/welcome.txt")
# print(f.read())
# print("---------- only 5 characters")
# f = open("C:/Users/Sannamalai/Desktop/file/welcome.txt")
# print(f.read(5))
# print("----------only one line")
# f = open("C:/Users/Sannamalai/Desktop/file/welcome.txt")
# print(f.readline())
# print(f.readline())
# # looping
# for x in f:
#   print(x)
  
  
f.close()


# Open the file "demofile2.txt" and append content to the file:
f = open("demofile.txt","a")
# f.write("\n appending content to the file")
# f.close()

# f=open("demofile.txt","r")
# print(f.read())
f.close()

# Open the file "demofile3.txt" and overwrite the content:
# f = open("demofile.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()
# f = open("demofile3.txt", "r")
# print(f.read())


# Create a New File
# f = open("newFile.txt","x") 

# to check if file exists
# if(os.path.exists("newFile.txt")):
#     print ("The file already exists.")
# else:
#     print("the file does not exist")
    
# # to remove a file
# if(os.path.exists("newFile.txt")):
#     os.remove("newFile.txt")
# else:
#     print("the file does not exist")

# f = open('demofile.txt','r')
# f.seek(7)
# data = f.read(25)
# print(data)

# replace a particular word
with open('demofile.txt', 'r') as file:
      file_contents = file.read()

      updated_contents = file_contents.replace('Woops', 'ohohhh')

with open('demofile.txt', 'w') as file:
   file.write(updated_contents)
   print(file.tell()) 
   file.truncate(35)
   print(file.tell()) 
print(file.closed)
 
 
# custom context manager
from contextlib import contextmanager
import os
@contextmanager
def open_file(file,mode):
    try:
        with open(file, mode) as f:
            yield f
    except Exception as e:
        raise IOError(e)
    finally:
        f.close()
        
# with open_file('demofile.txt','w') as f:
#     f.write('rewritten')
    
# print(f.closed)


 
# changing directories
# cwd = os.getcwd()
# os.chdir('JSON')
# print(os.listdir())

@contextmanager
def  change_dir(dest):
    try:
        cwd = os.getcwd()
        os.chdir(dest)
        yield
    finally:
        os.chdir(cwd)

   
with change_dir('JSON'):
    print(os.listdir())
    

# working with binary files
# some_bytes = b'\x21'

# with open("demofile.txt", "wb") as binary_file:
   
#     # Write bytes to file
#     binary_file.write(some_bytes)