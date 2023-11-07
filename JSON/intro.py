
import json
import urllib.parse
# JSON string 
employee = '{"id":"09", "name": "Nitin", "department":"Finance"}'
print("This is JSON", type(employee) , employee) 
hobbies = '["singing","drawing","killing"]'
print(type(hobbies))

# json to python
dict = json.loads(employee)
print(dict,type(dict)," python format ")
l = json.loads(hobbies)
print(type(l))

# python to json
employee = json.dumps(dict)
print("json format",type(employee))
hobbies = json.dumps(l)
print(type(hobbies))


# context managers
with open('demo.json','r') as file:
    print(file.read())
    
var = { 
      "Subjects": {
                  "Maths":85,
                  "Physics":90
                   }
      }   

# serializing
with open("demo.json",'w') as file:
    json.dump(var,file)
    
#deserializing
with open("demo.json","r") as file:
    x = json.load(file)
    print(x["Subjects"]["Maths"])


