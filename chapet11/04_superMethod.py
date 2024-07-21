class Employee:
    def __init__(self):
        print("Constractor of Employee")
    a=1
class Programmer(Employee):
    def __init__(self):
        print("Constractor of Programmer")
        super().__init__()
    b=2
class Manager(Programmer):
    def __init__(self):
        print("Constractor of Manager")
        super().__init__()
    c=3

obj1=Employee()
print(obj1.a)
obj2=Programmer()
print(obj2.a,obj2.b)
obj3=Manager()
print(obj3.a,obj3.b,obj3.c)