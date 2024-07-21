class Vector:
    def  __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def __add__(self,others):
        result=Vector(self.a+others.a,self.b+others.b,self.c+others.c)
        return result
    def __mul__(self,others):
        result=(self.a*others.a+self.b*others.b+self.c*others.c)
        return result
    def __str__(self):
        return f'{self.a}i+{self.b}j+{self.c}k'
    
v1= Vector (1,2,3)
v2= Vector (4,5,6)
print(v1+v2)
print(v1*v2)
v3=Vector(7,8,9)
print(v1+v3)
print(v1*v3)