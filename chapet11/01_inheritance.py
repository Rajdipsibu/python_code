class Employee:
    Company='Tata'
    def getDetails(self):
        print(f'the employee name is {self.name} and the salary is {self.salary}')

# class Programmer:
#     Company='TCS'
#     def getDetails(self):
#         print(f'the employee name is {self.name} and the salary is {self.salary}')
#     def language(self):
#         print(f'the name of {self.name}, he is good in {self.lang}')

class Programmer (Employee):
    Company='TCS'
    def language(self):
        print(f'the name of {self.name}, he is good in {self.lang}')

a=Employee()
b=Programmer()
print(a.Company,'\n',b.Company)