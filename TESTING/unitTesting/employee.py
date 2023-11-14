# import requests
class Employee:

    raise_amt = 1.05

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay 
    
    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'
    
    @property
    def fullName(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # def monthly_schedule(self,month):
    #     res = requests.get(f'http://company.com/{self.last}/{month}')
    #     if res.ok:
    #         return res.text
    #     else:
    #         return 'Bad Response!'

    