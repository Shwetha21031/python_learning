# The class can be defined as a collection of objects. 
# It is a logical entity 

# empty classes
class Dog:
    pass

class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    
    def get_grade(self):
        return self.grade
    
class Grades:
    def __init__(self,course,maxStudent):
        self.course = course
        self.maxStudent  = maxStudent
        self.students  = []

    def add_student(self,student):
        if(len(self.students)<self.maxStudent):
            self.students.append(student)
        else:
            print('more students cant be added')
    def avg_grade(self):
        avg = 0
        for i in self.students:
            avg += i.get_grade()
        
        return avg/len(self.students)


        

s1 = Student('Maria',77)
s2 = Student('Rose',90)
s3 = Student('Sina',97)

science = Grades('science',2)
science.add_student(s1)
science.add_student(s2)
science.add_student(s3)

print(science.avg_grade())



        