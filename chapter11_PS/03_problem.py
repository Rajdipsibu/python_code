class Employee:
    @property
    def salaryAfterIncrement(self):
        return self.salary+(self.salary*self.increment)/100 #new salary calculation..
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,New_salary):
        self.increment=(New_salary/self.salary-1)*100


emp=Employee()
emp.salary=int(input("Enter your salary: ")) #old salary 100
emp.increment=int(input("Enter increment: ")) #5% increment
print(f'New salary: {emp.salaryAfterIncrement}')
print(f'Total Increment:{emp.increment}')
'''
new salary =old salary+old ssalary*increment/100
'''