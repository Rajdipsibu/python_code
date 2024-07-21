class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
        #to Addition two Complex no:
    def __add__(self,c2):
        return Complex(self.r + c2.r,self.i + c2.r ) 
    #to Addition two Complex no:
    def __mul__(self,c2):
        return Complex(self.r * c2.r,self.i * c2.i ) 
    '''
        <__main__.Complex object at 0x000001FDDF9D5F70>
        <__main__.Complex object at 0x000001FDDF9D5F70>
        Now
        3 + 5i
        2 + 12i
        for __str__()
    '''
    def __str__(self):
        return f'{self.r} + {self.i}i'

a=Complex(1, 3)
b=Complex(2, 4)
print(a + b)
print(a*b)
