#__init__(),is a method which is first run when the object is created.....ok:)
class Employee:
    # Name="Rajdip Das"
    # Salary="1200000"
    # Language="python"
    def __init__(self,name,salary,language):#also call 'dunder method' 
        self.name=name
        self.salary=salary
        self.language=language
        print("its a init method................")
        print(f"name:{self.name},salary:{self.salary},language:{self.language}")

        
    

Rajdip=Employee('sandip',400000,'JavaScipt')#create a obj with parameter.....