class Calculator:
    @staticmethod
    def hello():
        print("hello there.....")
    # def __init__(self,number):
    #     self.number=number
    #     print('the number is: ',self.number)
    #     print(f'squere:{self.number**2}\ncube:{self.number**3}\nroot:{self.number**(1/2)}')

    def __init__(self,value):
        self.value=value
    def squere(self):
        print(f'the squere is: {self.value*self.value}')
    def cube(self):
        print(f'the cube is: {self.value*self.value*self.value}')
    def root(self):
        print(f'the root is: {self.value**(1/2)}')
# number=int(input("Enter number: "))
raju=Calculator(3)#Calculetor(raju,value)
raju.hello()#its a Static method
raju.root()#Calculetor.root(raju)
raju.squere()
raju.cube()