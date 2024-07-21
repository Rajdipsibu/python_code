class a:
    b=3
    @classmethod
    def getshow(cls):
        print(f"the class atrribute of b is {cls.b}")
#with out @classmethod 
# o/p==the class atrribute of b is 100
c=a()
c.b=100
c.getshow()