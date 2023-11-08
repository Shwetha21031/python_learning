import json
class Person:
    def __init__(self, id,name, age):
        self.id = id
        self.name = name
        self.age = age
    def upload_data(self):
        new_person ={
            "id": self.id,
            "name": self.name,
            "age": self.age
        }
        with open("practice.json",'a+') as file:
            file_data = json.load(file)
            file_data["age"].update(new_person)
            file.seek(0)
            json.dump(file_data, file, indent = 4)
    
    
        
p1 = Person(2,"karan",23)
p1.upload_data()
p1.write_json()