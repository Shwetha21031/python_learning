import json
import requests


# data fetching
base_url = 'https://jsonplaceholder.typicode.com/todos'
json_data = requests.get(base_url).json()
data = json_data[0:10]
# print(type(data),"data")

final_data = json.dumps(data, indent = 4)
# print(type(final_data),"finaldata")

file3 = open('apiData.json','w')
file3.write(final_data)
file3.close()


#Deserialize a JSON String to an Object in Python
f = open("apiData.json",'r')
data = json.load(f)
for x in data:
    print(f"id : {x["id"]}, title: {x["title"]}")
    
f.close()

# appending data to a jsonfile
def appendData(new_data,file="apiData.json"):
    with open(file,'r+') as f:
        fetched_data = json.load(f)
        print(type(fetched_data))
        fetched_data.append(new_data)
        # json.dump(fetched_data,f,indent=4)
        
y = {
        "userId": 2,
        "id": 2,
        "title": "quis ut nam facilis et officia qui",
        "completed": False
}

appendData(y)


def write_json(new_data, filename='demo.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["emp_details"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)
 
   
y = {"emp_name":"Nikhil",
     "email": "nikhil@geeksforgeeks.org",
     "job_profile": "Full Time"
    }
     
write_json(y) 