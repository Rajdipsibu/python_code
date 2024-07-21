class TwoDVactor:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def Display(self):
        print(f'2 D Vactor is: {self.i}i + {self.j}j')

class ThreeDVactor(TwoDVactor):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def Display(self):
        print(f'3 D Vactor is: {self.i}i + {self.j}j + {self.k}k')

a=TwoDVactor(1,2)
b=ThreeDVactor(1,2,3)
a.Display()
b.Display()

    
