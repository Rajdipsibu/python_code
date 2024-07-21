class Employee:
    Name="Rajdip Das"
    Salary="1200000"
    Language="python"

    @staticmethod#without any argument passes the method will be executed....happy
    def getMorning():
        print("Good Morning Rajdip bro........")

Rajdip=Employee()

Rajdip.getMorning()
print(f'Name: {Rajdip.Name}\nLanguage: {Rajdip.Language}\nSalary: {Rajdip.Salary}')