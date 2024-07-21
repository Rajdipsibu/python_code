class Number:
    def __init__(self,n):
        self.n=n
    def __add__(self,number):#without this 1.# execute you understande i hope u better understand....
        return self.n+number.n

a=Number(1)
b=Number(2)
print(a+b)#1.give a TypeError: unsupported operand type(s) for +: 'Number' and 'Number'