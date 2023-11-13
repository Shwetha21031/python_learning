import json

class Employee:
    def addEmp(self):
        self.eno = input('enter employee number: ')
        self.name = input('enter employee name: ')
        self.desig = input('enter employee designation: ')

        data = {
            'e_no': self.eno,
            'name': self.name,
            'designation': self.desig
        }

        print("data entered : \n", data)

        try:
            with open('empDetails.json', 'r') as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            print('file not found, created a new one')
            existing_data = {}

        existing_data[self.eno] = data

        with open('empDetails.json', 'w') as file:
            json.dump(existing_data, file, indent=4)
            print('data added')

    def viewData(self):
        with open('empDetails.json','r') as file:
            data = json.load(file)
            for k,v in data.items():
                print(k,v)

    def delData(self):
        id = input('enter id to be deleted: ')
        with open('empDetails.json','r') as file:
            data = json.load(file)
            if id in data.keys():
                print('deleted: ',data[id])
                del data[id]
                with open('empDetails.json','w') as updated_data:
                    json.dump(data,updated_data, indent=4)
                    print(data,'deleted successfully')
            else:
                print('id not found')

    def updateData(self):
        id = input('enter id to be updated: ')


        with open('empDetails.json', 'r') as file:
            data = json.load(file)
            if id in data.keys():
                ename = input('enter employee\'s new name: ')
                edesig = input('enter employee\'s new designation: ')
                newdata = {
                    'e_no': id,
                    'name': ename,
                    'designation': edesig
                }

                print("data entered : \n", newdata)
                data[id] = newdata

                with open('empDetails.json', 'w') as file:
                    json.dump(data, file, indent=4)
                    print('data updated successfully')
            else:
                print("id not found")

employee1 = Employee()
# employee1.addEmp()
# employee1.viewData()
# employee1.delData()
# employee1.updateData()
