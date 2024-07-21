class Employee:
    def getName(self):
        print(f"your name is {self.name}")

    @property
    def name(self):#2.here use property decorator of instance attribute.
        return f'{self.first_name} {self.last_name}'
        
    @name.setter
    def name(self,value):#3.here setter decorator use to split the return of property function
        self.first_name = value.split(" ")[0]
        self.last_name = value.split(" ")[1]

user=Employee()
user.name="Rajdip Das"#1.here name is user/instance attribute
print(user.first_name)#print Rajdip

user.getName()


'''
date= 15/07/2024
abstraction Encapsulation and Property and setter decorator...."today we learn".....
*here the user does not know about the operation to give the first name and last name separetly this is call data abstraction
and *the whole operation are in one class(Employee class)this mean to bind the whole operation in one capsule is called Encapsulation
'''

