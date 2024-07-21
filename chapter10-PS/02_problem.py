class Calculator:
    def __init__(self,number):
        self.number=number
        print('the number is: ',self.number)
        print(f'squere:{self.number**2}\ncube:{self.number**3}\nroot:{self.number**(1/2)}')

# number=int(input("Enter number: "))
raju=Calculator(3)