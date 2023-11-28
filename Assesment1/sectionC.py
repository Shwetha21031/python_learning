import os , csv , json , re

def createFolders():
    # creating main folder
    try:
        os.mkdir("Archive-viewer")
    except:
        print("folder Archive-viewer already exists")

    # creating sub folders 
    subFolders = ["BackEnd","FrontEnd","QA"]
    try:
        for folder in subFolders: 
            os.mkdir(f"Archive-viewer/{folder}")
    except:
        print("folder already exists")

# Validate email using regular expression
def validate_email(email):
        email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        return re.match(email_regex, email)


class Employee:
    # adding a new employee for the given folder
    def add_Employee(self):
        print("---------creating a new employee--------")
        file = input("enter correct folders path: ")
        
        if(os.path.exists(file)):
            id = input("enter id: ")
            name = input("enter name: ")
            age = input("enter age: ")
            mobile = input("enter mobile number: ")
            email = input("Enter employee email: ")
            #loop until you enter a valid email 
            while not validate_email(email):
                print("Please enter a valid email. (eg: abc@gmail.com)")
                email = input("Enter employee email: ")
            # enter skills seperated with comma
            skills = input("enter skills : ")
            dict = {
                    "name": name,
                    "age": age,
                    "mobile": mobile,
                    "email": email,
                    "skills": skills
                }
            print(f'Employee details with id {id} : {dict}')
            
            # writing employee details to the json file
            try:
                with open(f'{file}/team_members_details.json', 'r') as file_to_read:
                    existing_data = json.load(file_to_read)
            except FileNotFoundError:
                print('--json file not found, created a new one')
                existing_data = {}
                existing_data[id] = dict

            with open(f'{file}/team_members_details.json', 'w') as file_to_write:
                existing_data[id] = dict
                json.dump(existing_data, file_to_write, indent=4)
                print('--data added')

        else:
            print('invalid path')  



    # to view and update the csv file
    def view_Employee(self):
        file = input("enter correct folders path: ")
        try:
            with open(f'{file}/team_members_details.json', 'r') as file_to_read:
                existing_data = json.load(file_to_read)
                print(existing_data)
        except FileNotFoundError:
            print('file not found')
            return
        
        # writing the new details to the csv file
        with open(f'{file}/team_members_details.csv', 'w', newline='') as csv_file:
            fieldnames = ['ID', 'Name', 'Age', 'Mobile', 'Email', 'Skills']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for emp_id, emp_data in existing_data.items():
                writer.writerow({
                    'ID': emp_id,
                    'Name': emp_data['name'],
                    'Age': emp_data['age'],
                    'Mobile': emp_data['mobile'],
                    'Email': emp_data['email'],
                    'Skills': emp_data['skills']
                })
    
    
    
    # to delete a particular data with id from the given folder
    def del_Data(self):
        file = input("enter correct folder path: ")
        try:
            with open(f'{file}/team_members_details.json', 'r') as file_to_read:
                id = input("enter the id to delete: ")
                datas = json.load(file_to_read)
                if id in datas.keys():
                    del datas[id]
                    with open(f'{file}/team_members_details.json','w') as updated_datas:
                        json.dump(datas,updated_datas, indent=4)
                        print('\n deleted successfully')
                else:
                    print('id not found')
        except FileNotFoundError:
            print('file not found')
            return
        
        
        
    # update data from a particular folder
    def update_Employee(self):
        file = input("enter correct folder path: ")
        try:
            with open(f'{file}/team_members_details.json', 'r') as file_to_read:
                id = input('enter id to be updated: ')
                data = json.load(file_to_read)
                if id in data.keys():
                    print("----enter new credentials------")
                    name = input("enter name: ")
                    age = input("enter age: ")
                    mobile = input("enter mobile number: ")
                    email = input("Enter employee email: ")
                    while not validate_email(email):
                        print("Invalid email format. Please enter a valid email.")
                        email = input("Enter employee email: ")
                    skills = input("enter skills : ")
                    dict = {
                            "name": name,
                            "age": age,
                            "mobile": mobile,
                            "email": email,
                            "skills": skills
                        }

                    print(f'Employee details with id {id} : {dict}')
                    
                    data[id] = dict
                    with open(f'{file}/team_members_details.json', 'w') as files:
                        json.dump(data, files, indent=4)
                        print('data updated successfully')
                else:
                    print("id not found")
        except FileNotFoundError:
            print('file not found')
            return
        
             
# createFolders()
e1 = Employee()
e1.add_Employee()
# e1.view_Employee()
# e1.del_Data()
# e1.update_Employee()

    



