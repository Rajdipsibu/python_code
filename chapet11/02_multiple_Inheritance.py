class Employee:
    Company='Tata'
    # name='Raju'
    # language='C-language'
    def getEmp_Details(self):
        print(f'the Company name {self.Company} ')#employee name is {self.name}----->{self.language}

class Coder:
    # Company='Tesla'
    name='Biju'
    # language='Java'
    def getCod_Details(self):
        print(f'employee name is {self.name}')#the Company name {self.Company} ----->{self.language}

class Programmer (Employee,Coder):
    # Company='FaceBook'
    # name='Sonu'
    language='Python'
    def getPro_Details(self):
        print(f'----->{self.language}')#the Company name {self.Company} employee name is {self.name}

user=Programmer()
user.getEmp_Details()
user.getCod_Details()
user.getPro_Details()