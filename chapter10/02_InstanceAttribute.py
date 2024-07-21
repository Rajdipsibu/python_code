class Employee:
    Name="Rajdip Das"#Class Attribute........
    Salary="1200000"
    Language="python"

Harry=Employee()
Harry.Name='Harry'#instance attribute..........
print(f'Name: {Harry.Name}\nLanguage: {Harry.Language}\nSalary: {Harry.Salary}')
'''
so here,
instance attribute take preference over Class Attribute.


means,'name' as C.A. (Rajdip Das)
and alse Harry Obj have same 'name'as Ins.A.
but priority is given by Ins.A.
'''