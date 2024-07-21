class Programmer:
    company='Microsoft'
    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
        print(f"{self.company}\nname:{self.name}\nsalary:{self.salary}\nlanguage:{self.language}")
rajdip=Programmer('rajdip',100000000000,'Python')