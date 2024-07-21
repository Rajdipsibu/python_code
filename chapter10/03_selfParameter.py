# what is self parameter
class Employee:
    Name="Rajdip Das"
    Salary="1200000"
    Language="python"
    # def getLove():#here not accept anu argument so .....its gave a error  !!!
    #     print("I Love You.......")
    def getLove(self):#self is argument 
        print("I Love You.......")
    def getDetails(self):
        print(f'language: {self.Language},,,Salary: {self.Salary}')

Harry=Employee()
Harry.getDetails()
Harry.getLove()#Employee.getLove(Harry)   this pass a Argument (Harry)



#with out self compiler give a--
# "TypeError: Employee.getLove() takes 0 positional arguments but 1 was given"