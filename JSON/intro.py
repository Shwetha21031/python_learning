
import json
from typing import Any

# JSON string 
employee = '{"id":"09", "name": "Nitin", "department":"Finance"}'
# print("This is JSON", type(employee) , employee) 
hobbies = '["singing","drawing","killing"]'
# print(type(hobbies))

# json to python
dict = json.loads(employee)
# print(dict,type(dict)," python format ")
l = json.loads(hobbies)
print(type(l))

# python to json
employee = json.dumps(dict)
# print("json format",type(employee))
hobbies = json.dumps(l)
# print(type(hobbies))


# object to json
from json import JSONEncoder

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

class VehicleEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

print("Encode Vehicle Object into JSON")
vehicleJson = json.dumps(vehicle, indent=4, cls=VehicleEncoder)
# print(vehicleJson)

# json to object

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

def vehicleDecoder(obj):
        return Vehicle(obj['name'], obj['engine'], obj['price'])

vehicleObj = json.loads('{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }',
           object_hook=vehicleDecoder)

# print("Type of decoded object from JSON Data")
# print(type(vehicleObj))
# print("Vehicle Details")
# print(vehicleObj.name, vehicleObj.engine, vehicleObj.price)



# context managers
# with open('demo.json','r') as file:
    # print(file.read())
    
var = { 
      "Subjects": {
                  "Maths":85,
                  "Physics":90
                   }
      }   

# serializing
# with open("demo.json",'w') as file:
#     json.dump(var,file)
    
#deserializing
# with open("demo.json","r") as file:
#     x = json.load(file)
    # print(x["Subjects"]["Maths"])


# check whether json is valid or invalid
def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

InvalidJsonData = """{ "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000 "bonus":800} } } }"""
isValid = validateJSON(InvalidJsonData)

print("Given JSON string is Valid : ", isValid)
