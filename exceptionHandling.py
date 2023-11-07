try:
  print(x)
except:
  print("An exception occurred")



try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
  
  
# In this example, the try block does not generate any error:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
  
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
  
  
# finally
try:
    f=open("demofile.txt")
    try:
        f.write("lorem")
    except:
        print("something went wrong")
    finally:
        f.close()
except:
    print("something went wrong")
    

# raise Exception()
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

# Raise a TypeError if x is not an integer:
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")